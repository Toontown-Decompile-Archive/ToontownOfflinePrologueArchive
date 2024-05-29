# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.hood.CogNationCentral
# Compiled at: 2014-04-30 09:53:54
import CogHood
from toontown.toonbase import ToontownGlobals
from toontown.coghq import CogNationCentralCogHQLoader

class CogNationCentral(CogHood.CogHood):

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        CogHood.CogHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = ToontownGlobals.CogNationCentral
        self.cogHQLoaderClass = CogNationCentralCogHQLoader.CogNationCentralCogHQLoader
        self.storageDNAFile = None
        self.skyFile = 'phase_9/models/cogHQ/cog_sky'
        self.titleColor = (0.5, 0.5, 0.5, 1.0)
        return

    def load(self):
        CogHood.CogHood.load(self)
        self.sky.setScale(2.5)
        self.sky.setZ(-1)
        self.startSky()
        self.sewerCap = loader.loadModel('phase_14/models/props/sewerCap_prop')
        self.sewerCap.setPos(92.634, -0.055, 3.983)
        self.sewerCap.setScale(0.25)
        self.sewerCap.reparentTo(render)
        self.parentFSM.getStateNamed('CogNationCentral').addChild(self.fsm)

    def unload(self):
        self.stopSky()
        self.sewerCap.removeNode()
        del self.sewerCap
        self.parentFSM.getStateNamed('CogNationCentral').removeChild(self.fsm)
        del self.cogHQLoaderClass
        CogHood.CogHood.unload(self)

    def enter(self, *args):
        CogHood.CogHood.enter(self, *args)
        localAvatar.setCameraFov(ToontownGlobals.CogHQCameraFov)
        base.camLens.setNearFar(ToontownGlobals.CogHQCameraNear, ToontownGlobals.CogHQCameraFar)

    def exit(self):
        localAvatar.setCameraFov(ToontownGlobals.DefaultCameraFov)
        base.camLens.setNearFar(ToontownGlobals.DefaultCameraNear, ToontownGlobals.DefaultCameraFar)
        CogHood.CogHood.exit(self)