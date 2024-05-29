# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.parties.DistributedPartyActivityAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.parties import PartyGlobals, PartyUtils

class DistributedPartyActivityAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPartyActivityAI')

    def __init__(self, air, parent, activityTuple):
        DistributedObjectAI.__init__(self, air)
        self.parent = parent
        x, y, h = activityTuple[1:]
        self.x = PartyUtils.convertDistanceFromPartyGrid(x, 0)
        self.y = PartyUtils.convertDistanceFromPartyGrid(y, 1)
        self.h = h * PartyGlobals.PartyGridHeadingConverter
        self.toonsPlaying = []

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getH(self):
        return self.h

    def getPartyDoId(self):
        return self.parent

    def updateToonsPlaying(self):
        self.sendUpdate('setToonsPlaying', [self.toonsPlaying])

    def toonJoinRequest(self):
        avId = self.air.getAvatarIdFromSender()
        if avId not in self.air.doId2do:
            self.air.writeServerEvent('suspicious', avId, 'tried to enter activity from another shard!')
            return
        self.toonsPlaying.append(avId)
        self.updateToonsPlaying()

    def toonExitRequest(self):
        avId = self.air.getAvatarIdFromSender()
        self.toonsPlaying.remove(avId)
        self.updateToonsPlaying()

    def toonExitDemand(self):
        self.toonExitRequest()

    def toonReady(self):
        pass