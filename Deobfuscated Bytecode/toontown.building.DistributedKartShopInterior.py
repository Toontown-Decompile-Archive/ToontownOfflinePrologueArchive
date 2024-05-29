# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.building.DistributedKartShopInterior
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObject import DistributedObject
from pandac.PandaModules import *
from toontown.building import ToonInteriorColors
from toontown.hood import ZoneUtil
from toontown.toonbase.ToonBaseGlobal import *
from toontown.toonbase.ToontownGlobals import *

class DistributedKartShopInterior(DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedKartShopInterior')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        self.dnaStore = cr.playGame.dnaStore

    def generate(self):
        DistributedObject.generate(self)

    def announceGenerate(self):
        DistributedObject.announceGenerate(self)
        self.__handleInteriorSetup()

    def disable(self):
        self.interior.removeNode()
        del self.interior
        DistributedObject.disable(self)

    def setZoneIdAndBlock(self, zoneId, block):
        self.zoneId = zoneId
        self.block = block

    def __handleInteriorSetup(self):
        self.interior = loader.loadModel('phase_6/models/karting/KartShop_Interior')
        self.interior.reparentTo(render)
        self.interior.flattenMedium()