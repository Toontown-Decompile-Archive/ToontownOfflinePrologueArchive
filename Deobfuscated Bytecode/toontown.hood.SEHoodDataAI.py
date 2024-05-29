# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.hood.SEHoodDataAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
import HoodDataAI
from toontown.toonbase import ToontownGlobals
from toontown.reborn.DistributedSewerEventAI import DistributedSewerEventAI
from toontown.reborn.DistributedSewerMinigameAI import DistributedSewerMinigameAI

class SEHoodDataAI(HoodDataAI.HoodDataAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('HoodAI')

    def __init__(self, air, zoneId=None):
        hoodId = ToontownGlobals.Sewer
        if zoneId == None:
            zoneId = hoodId
        HoodDataAI.HoodDataAI.__init__(self, air, zoneId, hoodId)
        return

    def startup(self):
        self.notify.info('Creating zone... Sewer')
        HoodDataAI.HoodDataAI.startup(self)
        if self.air.config.GetBool('want-doomsday-reborn', False):
            self.spawnSewerEvent()
            self.spawnSewerMinigame()

    def spawnSewerEvent(self):
        sewerEv = self.air.doFind('SewerEvent')
        if sewerEv is None:
            sewerEv = DistributedSewerEventAI(self.air)
            sewerEv.generateWithRequired(self.zoneId)
        sewerEv.b_setState('Idle')
        return

    def spawnSewerMinigame(self):
        sewerMg = self.air.doFind('SewerMinigame')
        if sewerMg is None:
            sewerMg = DistributedSewerMinigameAI(self.air)
            sewerMg.generateWithRequired(14100)
        sewerMg.b_setState('Idle')
        return