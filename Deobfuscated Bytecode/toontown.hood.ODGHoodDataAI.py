# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.hood.ODGHoodDataAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
import HoodDataAI
from toontown.toonbase import ToontownGlobals
from toontown.safezone import ButterflyGlobals
from toontown.safezone.DistributedDGFlowerAI import DistributedDGFlowerAI
from toontown.classicchars import DistributedGoofyAI
from toontown.reborn.DistributedPrologue2EventAI import DistributedPrologue2EventAI
from toontown.reborn.DistributedPrologue3EventAI import DistributedPrologue3EventAI
from toontown.reborn.DistributedPrologue4EventAI import DistributedPrologue4EventAI

class ODGHoodDataAI(HoodDataAI.HoodDataAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('SZHoodAI')

    def __init__(self, air, zoneId=None):
        hoodId = ToontownGlobals.OldDaisyGardens
        if zoneId == None:
            zoneId = hoodId
        HoodDataAI.HoodDataAI.__init__(self, air, zoneId, hoodId)
        return

    def startup(self):
        self.notify.info('Creating zone... Old Daisy Gardens')
        HoodDataAI.HoodDataAI.startup(self)
        self.classicChar = None
        self.butterflies = []
        if simbase.config.GetBool('want-classic-chars', True):
            if simbase.config.GetBool('want-odg-goofy', True):
                self.createClassicChar()
        if self.air.config.GetBool('want-prologue', False):
            self.createPrologue2Event()
            self.createPrologue4Event()
            self.createPrologue3Event()
        self.flower = DistributedDGFlowerAI(self.air)
        self.flower.generateWithRequired(self.zoneId)
        self.createButterflies(ButterflyGlobals.DG)
        return

    def createClassicChar(self):
        self.classicChar = DistributedGoofyAI.DistributedGoofyAI(self.air)
        self.classicChar.generateWithRequired(self.zoneId)
        self.classicChar.start()

    def createPrologue2Event(self):
        self.pro2Ev = self.air.doFind('Prologue2Event')
        if self.pro2Ev is None:
            self.pro2Ev = DistributedPrologue2EventAI(self.air)
            self.pro2Ev.generateWithRequired(self.zoneId)
        self.pro2Ev.b_setState('Idle')
        return

    def createPrologue3Event(self):
        self.pro3Ev = self.air.doFind('Prologue3Event')
        if self.pro3Ev is None:
            self.pro3Ev = DistributedPrologue3EventAI(self.air)
            self.pro3Ev.generateWithRequired(21300)
        self.pro3Ev.b_setState('Idle')
        return

    def createPrologue4Event(self):
        self.pro4Ev = self.air.doFind('Prologue4Event')
        if self.pro4Ev is None:
            self.pro4Ev = DistributedPrologue4EventAI(self.air)
            self.pro4Ev.generateWithRequired(21834)
        self.pro4Ev.b_setState('Idle')
        return