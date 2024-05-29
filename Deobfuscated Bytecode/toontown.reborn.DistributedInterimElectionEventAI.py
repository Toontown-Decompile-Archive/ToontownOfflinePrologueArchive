# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.reborn.DistributedInterimElectionEventAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from direct.fsm.FSM import FSM
from otp.ai.MagicWordGlobal import *
from toontown.election.DistributedElectionCameraManagerAI import DistributedElectionCameraManagerAI
from toontown.reborn.DistributedSafezoneInvasionRebornAI import DistributedSafezoneInvasionRebornAI
from toontown.election.DistributedInvasionSuitAI import DistributedInvasionSuitAI
from toontown.election.InvasionMasterAI import InvasionMasterAI
from toontown.toonbase import ToontownGlobals
import SafezoneInvasionRebornGlobals, InterimElectionGlobals, random
from otp.distributed.OtpDoGlobals import *
from direct.task import Task

class DistributedInterimElectionEventAI(DistributedObjectAI, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedInterimElectionEventAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        FSM.__init__(self, 'ElectionFSM')
        self.air = air
        self.stateTime = globalClockDelta.getRealNetworkTime()
        self.pieTypeAmount = [4, 20, 1]
        self.cogDead = False
        self.master = InvasionMasterAI(self)
        self.toons = []
        self.suits = []

    def enterOff(self):
        self.requestDelete()

    def enterIdle(self):
        if config.GetBool('want-doomsday-reborn', False):
            if not hasattr(simbase.air, 'cameraManager'):
                camMgr = DistributedElectionCameraManagerAI(simbase.air)
                camMgr.spawnManager()

    def phraseSaidToFlippy(self, phraseId):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId, None)
        if not av:
            self.air.writeServerEvent('suspicious', avId=avId, issue="Someone tried to talk to Flippy while they aren't on the district!")
            return
        else:
            self.sendUpdate('flippySpeech', [avId, phraseId])
            return

    def wheelbarrowAvatarEnter(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId, None)
        if not av:
            self.air.writeServerEvent('suspicious', avId=avId, issue="Got a request for pies from a toon that isn't on the district!")
            return
        else:
            if av.hp > 0:
                av.b_setPieType(self.pieTypeAmount[0])
                av.b_setNumPies(self.pieTypeAmount[1])
                av.b_setPieThrowType(self.pieTypeAmount[2])
            self.sendUpdate('flippySpeech', [avId, 1])
            return

    def setPieTypeAmount(self, type, num):
        self.pieTypeAmount = [type, num]

    def enterEvent(self):
        event = simbase.air.doFind('ElectionEvent')
        if event is None:
            event = DistributedInterimElectionEventAI(simbase.air)
            event.generateWithRequired(2000)
        self.eventSequence = Sequence(Func(event.b_setState, 'PreShow'), Wait(29), Func(event.b_setState, 'Begin'), Wait(10), Func(event.b_setState, 'AlecSpeech'), Wait(148), Func(event.b_setState, 'VoteBuildup'), Wait(15), Func(event.b_setState, 'CogLanding'), Wait(145), Func(event.b_setState, 'Invasion'))
        self.eventSequence.start()
        return

    def enterPreShow(self):
        self.showAnnounceInterval = Sequence(Func(self.sendGlobalUpdate, 'TOON HQ: The Toon Council Interim Presidential Elections will be starting any second!'), Wait(5), Func(self.sendGlobalUpdate, 'TOON HQ: Please silence your shticker books and keep any neighs, rruffs, and owooos to a low rustle.'))
        self.showAnnounceInterval.start()

    def exitPreShow(self):
        self.showAnnounceInterval.finish()

    def enterBegin(self):
        pass

    def enterAlecSpeech(self):
        pass

    def enterVoteBuildup(self):
        pass

    def enterCogLanding(self):
        pass

    def exitCogLanding(self):
        pass

    def enterInvasion(self):
        self.surleePhraseLoop = Sequence(Wait(30), Func(self.saySurleePhrase))
        self.invasionSequence = Sequence(Wait(19), Func(self.spawnInvasion), Func(self.surleePhraseLoop.loop))
        self.invasionSequence.start()

    def exitInvasion(self):
        self.invasionSequence.finish()
        self.surleePhraseLoop.finish()

    def enterInvasionEnd(self):
        self.cogDead = False

    def enterWrapUp(self):
        taskMgr.doMethodLater(60, self.b_setState, self.uniqueName('restart-election'), extraArgs=['Off'])

    def spawnInvasion(self):
        invasion = simbase.air.doFind('SafezoneInvasionReborn')
        if invasion is None:
            invasion = DistributedSafezoneInvasionRebornAI(simbase.air, self)
            invasion.generateWithRequired(2000)
        return

    def setSuitDamage(self, hp, kill=False):
        if self.state == 'InvasionEnd':
            invasion = simbase.air.doFind('SafezoneInvasionReborn')
            if invasion:
                invasion.setFinaleSuitStunned(hp, kill)
        elif not self.cogDead:
            self.cogDead = True
            self.suit = DistributedInvasionSuitAI(self.air, self)
            self.suit.dna.newSuit('le')
            self.suit.setSpawnPoint(99)
            self.suit.setLevel(4)
            self.suit.generateWithRequired(ToontownGlobals.ToontownCentral)
            self.suit.b_setSkeleRevives(1)
            self.suit.takeDamage(hp, True)

    def saySurleePhrase(self, phrase=None, interrupt=0, broadcast=False):
        if not phrase:
            phrase = random.choice(InterimElectionGlobals.SurleeTips)
        self.sendUpdate('saySurleePhrase', [phrase, interrupt, broadcast])

    def sendGlobalUpdate(self, text):
        for doId in simbase.air.doId2do:
            if str(doId)[:2] == '10':
                do = simbase.air.doId2do.get(doId)
                do.d_setSystemMessage(0, text)

    def setState(self, state):
        self.demand(state)

    def d_setState(self, state):
        self.stateTime = globalClockDelta.getRealNetworkTime()
        self.sendUpdate('setState', [state, self.stateTime])

    def b_setState(self, state):
        self.setState(state)
        self.d_setState(state)

    def getState(self):
        return (
         self.state, self.stateTime)


@magicWord(category=CATEGORY_MODERATION, types=[str])
def reborn(state):
    event = simbase.air.doFind('InterimElectionEvent')
    if config.GetBool('want-doomsday', False):
        return 'The first Election is running.'
    else:
        if event is None:
            event = DistributedInterimElectionEventAI(simbase.air)
            event.generateWithRequired(2000)
        if not hasattr(event, 'enter' + state):
            return 'Invalid state'
        if not config.GetBool('want-doomsday-reborn', False):
            if not state == 'Idle':
                return 'These states will crash the game when Elections are disabled!'
        event.b_setState(state)
        return 'Election event now in %r state' % state