# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.building.DistributedTrophyMgrAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from operator import itemgetter

class DistributedTrophyMgrAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTrophyMgrAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.scores = {}
        self.scoreLists = ([], [], [])

    def requestTrophyScore(self):
        avId = self.air.getAvatarIdFromSender()
        if avId in self.scores:
            if avId in self.air.doId2do:
                self.air.doId2do[avId].sendUpdate('setTrophyScore', [self.scores[avId][1]])

    def removeTrophy(self, avId, numFloors):
        if avId not in self.scores:
            self.notify.warning('avId %d is not in scores' % avId)
            return
        self.scores[avId][1] -= numFloors
        if self.scores[avId][1] < 0:
            self.notify.warning('avId %d has a negative scorevalue?~?~?!' % avId)
            self.scores[avId][1] = 0
        self.sort()
        messenger.send('leaderboardChanged')
        messenger.send('leaderboardFlush')
        if avId in self.air.doId2do:
            self.air.doId2do[avId].sendUpdate('setTrophyScore', [self.scores[avId][1]])

    def addTrophy(self, avId, name, numFloors):
        if avId not in self.scores:
            if not self.air.doId2do.has_key(avId):
                return
            self.scores[avId] = [
             '', 0]
            self.scores[avId][1] = 0
            av = self.air.doId2do[avId]
            self.scores[avId][0] = av.getName()
        self.scores[avId][1] += numFloors
        self.sort()
        messenger.send('leaderboardChanged')
        messenger.send('leaderboardFlush')
        if avId in self.air.doId2do:
            self.air.doId2do[avId].sendUpdate('setTrophyScore', [self.scores[avId][1]])

    def sort(self):
        scoreList = []
        for avId, data in self.scores.items():
            scoreList.append((avId, data[0], data[1]))

        scoreList.sort(key=itemgetter(2), reverse=True)
        avIds = []
        names = []
        scores = []
        for avId, name, score in scoreList:
            avIds.append(avId)
            names.append(name)
            scores.append(score)
            if len(scores) == 10:
                break

        self.scoreLists = (
         avIds, names, scores)

    def getLeaderInfo(self):
        return self.scoreLists