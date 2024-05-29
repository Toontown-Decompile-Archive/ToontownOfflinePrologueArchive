# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.hood.SBHoodDataAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
import HoodDataAI
from toontown.toonbase import ToontownGlobals
from toontown.safezone import ButterflyGlobals
from toontown.reborn.DistributedPrologueEventAI import DistributedPrologueEventAI

class SBHoodDataAI(HoodDataAI.HoodDataAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('HoodAI')

    def __init__(self, air, zoneId=None):
        hoodId = ToontownGlobals.ScroogeBank
        if zoneId == None:
            zoneId = hoodId
        HoodDataAI.HoodDataAI.__init__(self, air, zoneId, hoodId)
        return

    def startup(self):
        self.notify.info('Creating prologue...')
        HoodDataAI.HoodDataAI.startup(self)
        self.butterflies = []
        self.proEv = None
        self.createButterflies(ButterflyGlobals.DG)
        if self.air.config.GetBool('want-prologue', False):
            self.createPrologueEvent()
        return

    def createPrologueEvent(self):
        self.proEv = self.air.doFind('PrologueEvent')
        if self.proEv is None:
            self.proEv = DistributedPrologueEventAI(self.air)
            self.proEv.generateWithRequired(self.zoneId)
        self.proEv.b_setState('Idle')
        return