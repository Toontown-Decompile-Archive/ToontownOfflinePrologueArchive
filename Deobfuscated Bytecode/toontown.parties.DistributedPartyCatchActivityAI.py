# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.parties.DistributedPartyCatchActivityAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from toontown.parties.DistributedPartyActivityAI import DistributedPartyActivityAI
from toontown.parties.DistributedPartyCatchActivityBase import DistributedPartyCatchActivityBase
from direct.task import Task
from direct.distributed.ClockDelta import globalClockDelta
from toontown.toonbase import TTLocalizer
import PartyGlobals

class DistributedPartyCatchActivityAI(DistributedPartyActivityAI, DistributedPartyCatchActivityBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPartyCatchActivityAI')

    def __init__(self, air, parent, activityTuple):
        DistributedPartyActivityAI.__init__(self, air, parent, activityTuple)
        self.numGenerations = 1
        self.generations = []
        self.player2catches = {}
        self.startTimestamp = globalClockDelta.getRealNetworkTime(bits=32)
        self.playing = False

    def delete(self):
        taskMgr.remove(self.taskName('newGeneration'))
        DistributedPartyActivityAI.delete(self)

    def getStartTimestamp(self):
        return self.startTimestamp

    def setStartTimestamp(self, ts):
        self.startTimestamp = ts

    def setGenerations(self, generations):
        self.generations = generations

    def toonJoinRequest(self):
        DistributedPartyActivityAI.toonJoinRequest(self)
        avId = self.air.getAvatarIdFromSender()
        self.player2catches[avId] = 0
        if not self.playing:
            self.__startGame()
            self.sendUpdate('setState', ['Active', globalClockDelta.getRealNetworkTime()])

    def toonExitDemand(self):
        avId = self.air.getAvatarIdFromSender()
        if avId not in self.toonsPlaying:
            self.air.writeServerEvent('suspicious', avId=avId, issue="Toon tried to exit a party game they're not using!")
            return
        else:
            catches = self.player2catches[avId]
            del self.player2catches[avId]
            av = self.air.doId2do.get(avId, None)
            if not av:
                self.air.writeServerEvent('suspicious', avId=avId, issue='Toon tried to award beans while not in district!')
                return
            if catches > PartyGlobals.CatchMaxTotalReward:
                catches = PartyGlobals.CatchMaxTotalReward
            self.sendUpdateToAvatarId(avId, 'showJellybeanReward', [catches, av.getMoney(), TTLocalizer.PartyCatchRewardMessage % (catches, catches)])
            av.addMoney(catches)
            DistributedPartyActivityAI.toonExitDemand(self)
            return

    def __startGame(self):
        self.playing = True
        self.calcDifficultyConstants(len(self.toonsPlaying))
        self.generations.append([self.numGenerations, globalClockDelta.getRealNetworkTime(bits=32), len(self.toonsPlaying)])
        self.numGenerations += 1
        self.sendUpdate('setGenerations', [self.generations])
        taskMgr.doMethodLater(self.generationDuration, self.__newGeneration, 'newGeneration%d' % self.doId, extraArgs=[])

    def __newGeneration(self):
        if len(self.toonsPlaying) > 0:
            self.__startGame()
        else:
            self.playing = False

    def getGenerations(self):
        return self.generations

    def requestActivityStart(self):
        pass

    def startRequestResponse(self, todo0):
        pass

    def claimCatch(self, generation, objNum, objType):
        avId = self.air.getAvatarIdFromSender()
        if avId not in self.toonsPlaying:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Toon tried to catch while not playing!')
            return
        if PartyGlobals.DOTypeId2Name[objType] != 'anvil':
            self.player2catches[avId] += 1
        self.sendUpdate('setObjectCaught', [avId, generation, objNum])