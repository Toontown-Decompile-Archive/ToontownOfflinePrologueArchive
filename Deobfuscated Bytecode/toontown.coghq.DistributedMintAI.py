# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.DistributedMintAI
# Compiled at: 2014-04-30 09:53:54
from direct.distributed import DistributedObjectAI
from otp.level import DistributedLevelAI
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.coghq import MintLayout, DistributedMintRoomAI
from toontown.coghq import BattleExperienceAggregatorAI

class DistributedMintAI(DistributedObjectAI.DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedMintAI')

    def __init__(self, air, mintId, zoneId, floorNum, avIds):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.mintId = mintId
        self.zoneId = zoneId
        self.floorNum = floorNum
        self.avIds = avIds

    def generate(self):
        DistributedObjectAI.DistributedObjectAI.generate(self)
        self.notify.info('generate %s, id=%s, floor=%s' % (self.doId, self.mintId, self.floorNum))
        self.layout = MintLayout.MintLayout(self.mintId, self.floorNum)
        self.rooms = []
        self.battleExpAggreg = BattleExperienceAggregatorAI.BattleExperienceAggregatorAI()
        for i in range(self.layout.getNumRooms()):
            room = DistributedMintRoomAI.DistributedMintRoomAI(self.air, self.mintId, self.doId, self.zoneId, self.layout.getRoomId(i), i * 2, self.avIds, self.battleExpAggreg)
            room.generateWithRequired(self.zoneId)
            self.rooms.append(room)

        roomDoIds = []
        for room in self.rooms:
            roomDoIds.append(room.doId)

        self.sendUpdate('setRoomDoIds', [roomDoIds])
        if __dev__:
            simbase.mint = self
        for avId in self.avIds:
            self.air.writeServerEvent('mintEntered', avId=avId, mintId=self.mintId, floorNum=self.floorNum, avIds=self.avIds)

    def requestDelete(self):
        self.notify.info('requestDelete: %s' % self.doId)
        for room in self.rooms:
            room.requestDelete()

        DistributedObjectAI.DistributedObjectAI.requestDelete(self)

    def delete(self):
        self.notify.info('delete: %s' % self.doId)
        if __dev__:
            if hasattr(simbase, 'mint') and simbase.mint is self:
                del simbase.mint
        del self.rooms
        del self.layout
        del self.battleExpAggreg
        DistributedObjectAI.DistributedObjectAI.delete(self)

    def getTaskZoneId(self):
        return self.mintId

    def allToonsGone(self):
        self.notify.info('allToonsGone')
        self.requestDelete()

    def getZoneId(self):
        return self.zoneId

    def getMintId(self):
        return self.mintId

    def getFloorNum(self):
        return self.floorNum