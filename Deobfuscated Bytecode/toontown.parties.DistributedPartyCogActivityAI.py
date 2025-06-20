# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.parties.DistributedPartyCogActivityAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.showbase.PythonUtil import bound
from toontown.parties.DistributedPartyTeamActivityAI import DistributedPartyTeamActivityAI
from toontown.toonbase import TTLocalizer
from toontown.parties import PartyGlobals

class DistributedPartyCogActivityAI(DistributedPartyTeamActivityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPartyCogActivityAI')
    startDelay = PartyGlobals.CogActivityStartDelay

    def announceGenerate(self):
        self.highscore = [
         '', 0]
        DistributedPartyTeamActivityAI.announceGenerate(self)

    def getDuration(self):
        return PartyGlobals.CogActivityDuration

    def pieHitsCog(self, avId, timestamp, hitCogNum, x, y, z, direction, part):
        av = self._getCaller()
        if not av:
            return
        if avId != av.doId:
            self.air.writeServerEvent('suspicious', av.doId, 'sent DistributedPartyCogActivityAI.pieHitsCog as someone else!', fakeId=avId)
            return
        if not (av.doId in self.toonIds[0] or av.doId in self.toonIds[1]):
            self.air.writeServerEvent('suspicious', avId, 'sent DistributedPartyCogActivityAI.pieHitsCog, but not playing')
            return
        if hitCogNum > 2:
            self.air.writeServerEvent('suspicious', avId, 'sent DistributedPartyCogActivityAI.pieHitsCog invalid cog num', hitCogNum=hitCogNum)
            return
        mult = PartyGlobals.CogPinataPushBodyFactor
        if part:
            mult = PartyGlobals.CogPinataPushHeadFactor
        if avId not in self.scores:
            self.scores[avId] = 0
        self.scores[avId] += mult
        self.cogDistances[hitCogNum] = bound(self.cogDistances[hitCogNum] + direction * mult, -1.0, 1.0)
        self.d_setCogDistances()

    def startActive(self, data):
        self.cogDistances = [
         0, 0, 0]
        self.scores = {}
        DistributedPartyTeamActivityAI.startActive(self, data)

    def d_setCogDistances(self):
        self.sendUpdate('setCogDistances', [self.cogDistances])

    def calcReward(self):
        for avId, s in self.scores.items():
            s = int(s / PartyGlobals.CogPinataPushBodyFactor)
            if s > self.highscore[1]:
                av = self.air.doId2do.get(avId)
                if av:
                    self.highscore[0] = av.getName()
                    self.highscore[1] = s

        scores = [
         0, 0]
        for d in self.cogDistances:
            team = 0
            if d > 0:
                team = 1
            scores[team] += int(abs(d) * 3333)

        self.b_setState('Conclusion', scores[0] * 10000 + scores[1])
        self._teamScores = scores

    def d_setHighScore(self):
        self.sendUpdate('setHighScore', self.highscore)

    def startConclusion(self, data):
        taskMgr.doMethodLater(PartyGlobals.CogActivityConclusionDuration, self.__exitConclusion, self.taskName('exitconc'))

    def finishConclusion(self):
        taskMgr.remove(self.taskName('exitconc'))

    def __exitConclusion(self, task):
        totalScore = sum(self._teamScores)

        def _sendReward(team):
            jb = max(5, self._teamScores[team] * (PartyGlobals.CogActivityBeansToAward / totalScore))
            winnerTeam = self._teamScores[team] > self._teamScores[team - 1]
            msg = TTLocalizer.PartyTeamActivityRewardMessage % jb
            if winnerTeam:
                jb += PartyGlobals.CogActivityWinBeans
                msg += TTLocalizer.PartyCogRewardBonus % (PartyGlobals.CogActivityWinBeans, 's')
            jb = int(jb)
            for avId in self.toonIds[team]:
                av = self.air.doId2do.get(avId)
                if av:
                    self.sendUpdateToAvatarId(avId, 'showJellybeanReward', [jb, av.getMoney(), msg])
                    av.addMoney(jb)

        _sendReward(0)
        _sendReward(1)
        self.toonsPlaying = []
        self.toonIds = ([], [])
        self.updateToonsPlaying()
        self.b_setState('WaitForEnough')
        return task.done