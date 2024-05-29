# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.FactoryManagerAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
import DistributedFactoryAI
from toontown.toonbase import ToontownGlobals
from direct.showbase import DirectObject

class FactoryManagerAI(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('FactoryManagerAI')
    factoryId = None

    def __init__(self, air):
        DirectObject.DirectObject.__init__(self)
        self.air = air

    def getDoId(self):
        return 0

    def createFactory(self, factoryId, entranceId, players):
        factoryZone = self.air.allocateZone()
        if FactoryManagerAI.factoryId is not None:
            factoryId = FactoryManagerAI.factoryId
        factory = DistributedFactoryAI.DistributedFactoryAI(self.air, factoryId, factoryZone, entranceId, players)
        factory.generateWithRequired(factoryZone)
        return factoryZone