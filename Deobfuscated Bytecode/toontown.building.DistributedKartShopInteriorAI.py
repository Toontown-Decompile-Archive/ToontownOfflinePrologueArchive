# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.building.DistributedKartShopInteriorAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedKartShopInteriorAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedKartShopInteriorAI')

    def __init__(self, blockNumber, air, interiorZone):
        DistributedObjectAI.__init__(self, air)
        self.zone = interiorZone
        self.block = blockNumber

    def setZoneIdAndBlock(self, zone, block):
        self.zone = zone
        self.block = block

    def getZoneIdAndBlock(self):
        return [
         self.zone, self.block]