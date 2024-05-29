# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.town.StreetAI
# Compiled at: 2014-04-30 09:53:54
from toontown.suit.DistributedSuitPlannerAI import DistributedSuitPlannerAI
from toontown.building.DistributedBuildingMgrAI import DistributedBuildingMgrAI

class StreetAI:

    def __init__(self, air, zoneId):
        self.air = air
        self.zoneId = zoneId
        self.air.dnaStoreMap[self.zoneId] = self.air.loadDNA(self.air.genDNAFileName(self.zoneId)).generateData()
        self.spawnObjects()

    def spawnObjects(self):
        filename = self.air.genDNAFileName(self.zoneId)
        self.air.dnaSpawner.spawnObjects(filename, self.zoneId)
        self.buildingMgr = DistributedBuildingMgrAI(self.air, self.zoneId, self.air.dnaStoreMap[self.zoneId], self.air.trophyMgr)
        self.sp = DistributedSuitPlannerAI(self.air, self.zoneId)
        self.sp.generateWithRequired(self.zoneId)
        self.sp.d_setZoneId(self.zoneId)
        self.sp.initTasks()