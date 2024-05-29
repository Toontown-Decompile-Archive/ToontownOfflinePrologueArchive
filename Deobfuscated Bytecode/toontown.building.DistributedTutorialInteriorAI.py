# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.building.DistributedTutorialInteriorAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedTutorialInteriorAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTutorialInteriorAI')

    def __init__(self, air, zoneId, npcId):
        DistributedObjectAI.__init__(self, air)
        self.zoneId = zoneId
        self.block = 0
        self.npcId = npcId

    def getZoneIdAndBlock(self):
        return (
         self.zoneId, self.block)

    def getTutorialNpcId(self):
        return self.npcId