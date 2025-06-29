# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.hood.SBHood
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
import ToonHood
from toontown.town import SBTownLoader
from toontown.safezone import SBSafeZoneLoader
from toontown.toonbase.ToontownGlobals import *
import SkyUtil

class SBHood(ToonHood.ToonHood):

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        ToonHood.ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = ScroogeBank
        self.townLoaderClass = SBTownLoader.SBTownLoader
        self.safeZoneLoaderClass = SBSafeZoneLoader.SBSafeZoneLoader
        self.storageDNAFile = 'phase_8/dna/storage_ODG.pdna'
        self.holidayStorageDNADict = {WINTER_DECORATIONS: ['phase_8/dna/winter_storage_SB.pdna'], WACKY_WINTER_DECORATIONS: [
                                    'phase_8/dna/winter_storage_SB.pdna'], 
           HALLOWEEN_PROPS: [
                           'phase_8/dna/halloween_props_storage_SB.pdna'], 
           SPOOKY_PROPS: [
                        'phase_8/dna/halloween_props_storage_SB.pdna']}
        self.skyFile = 'phase_3.5/models/props/TT_sky'
        self.spookySkyFile = 'phase_3.5/models/props/BR_sky'
        self.titleColor = (0.8, 0.6, 1.0, 1.0)
        cm = CardMaker('card')
        cm.setFrameFullscreenQuad()
        self.explosionCard = render2d.attachNewNode(cm.generate())
        self.explosionCard.setTransparency(1)
        self.explosionCard.setColorScale(0, 0, 0, 0)
        self.laffMeter = base.localAvatar.laffMeter
        self.book = base.localAvatar.book.bookOpenButton
        self.book2 = base.localAvatar.book.bookCloseButton

    def load(self):
        ToonHood.ToonHood.load(self)
        self.parentFSM.getStateNamed('SBHood').addChild(self.fsm)

    def unload(self):
        self.parentFSM.getStateNamed('SBHood').removeChild(self.fsm)
        ToonHood.ToonHood.unload(self)

    def enter(self, *args):
        ToonHood.ToonHood.enter(self, *args)
        localAvatar.setCameraFov(CogHQCameraFov)
        base.camLens.setNearFar(CogHQCameraNear, CogHQCameraFar)
        proEvSeq = Sequence(Func(NodePath(self.book).hide), Func(NodePath(self.laffMeter).hide), Func(base.localAvatar.disableSleeping), Func(base.localAvatar.obscureFriendsListButton, 1), Func(base.localAvatar.hideClarabelleGui), Func(base.localAvatar.chatMgr.obscure, 1, 1), Func(self.explosionCard.setColorScale, 0, 0, 0, 1), Wait(3), Func(localAvatar.sendUpdate, 'startProEv', []), self.explosionCard.colorScaleInterval(2, (0,
                                                                                                                                                                                                                                                                                                                                                                                                                                            0,
                                                                                                                                                                                                                                                                                                                                                                                                                                            0,
                                                                                                                                                                                                                                                                                                                                                                                                                                            0)))
        proEvSeq.start()

    def exit(self):
        localAvatar.setCameraFov(DefaultCameraFov)
        base.camLens.setNearFar(DefaultCameraNear, DefaultCameraFar)
        ToonHood.ToonHood.exit(self)

    def skyTrack(self, task):
        return SkyUtil.cloudSkyTrack(task)

    def startSky(self):
        if not self.sky.getTag('sky') == 'Regular':
            self.endSpookySky()
        SkyUtil.startCloudSky(self)

    def startSpookySky(self):
        if hasattr(self, 'sky') and self.sky:
            self.stopSky()
        self.sky = loader.loadModel(self.spookySkyFile)
        self.sky.setTag('sky', 'Halloween')
        self.sky.setScale(1.0)
        self.sky.setDepthTest(0)
        self.sky.setDepthWrite(0)
        self.sky.setColor(0.5, 0.5, 0.5, 1)
        self.sky.setBin('background', 100)
        self.sky.setFogOff()
        self.sky.reparentTo(camera)
        self.sky.setTransparency(TransparencyAttrib.MDual, 1)
        fadeIn = self.sky.colorScaleInterval(1.5, Vec4(1, 1, 1, 1), startColorScale=Vec4(1, 1, 1, 0.25), blendType='easeInOut')
        fadeIn.start()
        self.sky.setZ(0.0)
        self.sky.setHpr(0.0, 0.0, 0.0)
        ce = CompassEffect.make(NodePath(), CompassEffect.PRot | CompassEffect.PZ)
        self.sky.node().setEffect(ce)