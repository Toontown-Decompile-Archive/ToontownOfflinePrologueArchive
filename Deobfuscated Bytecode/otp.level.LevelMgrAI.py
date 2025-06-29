# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.level.LevelMgrAI
# Compiled at: 2014-04-30 09:53:54
from direct.showbase.PythonUtil import Functor
import LevelMgrBase

class LevelMgrAI(LevelMgrBase.LevelMgrBase):

    def __init__(self, level, entId):
        LevelMgrBase.LevelMgrBase.__init__(self, level, entId)
        self.level.zoneNum2zoneId = {}
        self.level.zoneIds = []
        self.accept(self.level.getEntityOfTypeCreateEvent('zone'), self.handleZoneCreated)

    def destroy(self):
        del self.level.zoneIds
        del self.level.zoneNum2zoneId
        LevelMgrBase.LevelMgrBase.destroy(self)

    def handleZoneCreated(self, entId):
        zoneEnt = self.level.getEntity(entId)
        self.level.zoneNum2zoneId[zoneEnt.entId] = zoneEnt.getZoneId()
        self.privCreateSortedZoneIdList()
        self.accept(self.level.getEntityDestroyEvent(entId), Functor(self.handleZoneDestroy, entId))

    def handleZoneDestroy(self, entId):
        zoneEnt = self.level.getEntity(entId)
        del self.level.zoneNum2zoneId[zoneEnt.entId]
        self.privCreateSortedZoneIdList()

    def privCreateSortedZoneIdList(self):
        zoneNums = self.level.zoneNum2zoneId.keys()
        zoneNums.sort()
        self.level.zoneIds = []
        for zoneNum in zoneNums:
            self.level.zoneIds.append(self.level.zoneNum2zoneId[zoneNum])