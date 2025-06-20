# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.hood.CashbotHQ
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
import CogHood
from toontown.toonbase import ToontownGlobals, TTLocalizer
from toontown.hood import ZoneUtil
from toontown.coghq import CashbotCogHQLoader

class CashbotHQ(CogHood.CogHood):
    notify = DirectNotifyGlobal.directNotify.newCategory('CashbotHQ')

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        CogHood.CogHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = ToontownGlobals.CashbotHQ
        self.cogHQLoaderClass = CashbotCogHQLoader.CashbotCogHQLoader
        self.storageDNAFile = None
        self.skyFile = 'phase_3.5/models/props/TT_sky'
        self.titleColor = (0.5, 0.5, 0.5, 1.0)
        return

    def load(self):
        CogHood.CogHood.load(self)
        self.parentFSM.getStateNamed('CashbotHQ').addChild(self.fsm)

    def unload(self):
        self.parentFSM.getStateNamed('CashbotHQ').removeChild(self.fsm)
        del self.cogHQLoaderClass
        CogHood.CogHood.unload(self)

    def enter(self, *args):
        CogHood.CogHood.enter(self, *args)
        localAvatar.setCameraFov(ToontownGlobals.CogHQCameraFov)
        base.camLens.setNearFar(ToontownGlobals.CashbotHQCameraNear, ToontownGlobals.CashbotHQCameraFar)

    def exit(self):
        localAvatar.setCameraFov(ToontownGlobals.DefaultCameraFov)
        base.camLens.setNearFar(ToontownGlobals.DefaultCameraNear, ToontownGlobals.DefaultCameraFar)
        CogHood.CogHood.exit(self)

    def spawnTitleText(self, zoneId, floorNum=None):
        if ZoneUtil.isMintInteriorZone(zoneId):
            text = '%s\n%s' % (ToontownGlobals.StreetNames[zoneId][-1], TTLocalizer.MintFloorTitle % (floorNum + 1))
            self.doSpawnTitleText(text)
        else:
            CogHood.CogHood.spawnTitleText(self, zoneId)