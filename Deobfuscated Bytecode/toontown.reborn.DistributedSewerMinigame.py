# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.reborn.DistributedSewerMinigame
# Compiled at: 2014-04-30 09:53:54
from panda3d.core import *
from otp.nametag.NametagConstants import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from direct.distributed.DistributedObject import DistributedObject
from direct.fsm.FSM import FSM
from toontown.toon import NPCToons
from toontown.battle import BattleProps
from toontown.toonbase import ToontownGlobals
from otp.margins.WhisperPopup import *
from direct.directnotify import DirectNotifyGlobal
from toontown.distributed import DelayDelete
from StomperObstacle import StomperObstacle
from GavelObstacle import GavelObstacle
from GoonObstacle import GoonObstacle
from SecurityCameraObstacle import SecurityCameraObstacle
from ChopperObstacle import ChopperObstacle
from SewerHealBarrel import SewerHealBarrel

class DistributedSewerMinigame(DistributedObject, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSewerMinigame')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        FSM.__init__(self, 'SewerMinigameFSM')
        self.cr.sewerMinigame = self
        self.obstaclesSetup = False
        self.laffMeter = base.localAvatar.laffMeter
        self.book = base.localAvatar.book.bookOpenButton
        self.book2 = base.localAvatar.book.bookCloseButton
        self.activeIntervals = {}
        self.toonSphere = None
        self.rocky = NPCToons.createLocalNPC(14001)
        self.rocky.useLOD(1000)
        self.rocky.head = self.rocky.find('**/__Actor_head')
        self.rocky.initializeBodyCollisions('toon')
        self.rocky.setPos(0, -41, 5.65)
        self.rockyWalkInterval = Sequence(Func(self.rocky.loop, 'run'), self.rocky.posHprInterval(0.5, (0,
                                                                                                        -37,
                                                                                                        3.725), (0,
                                                                                                                 0,
                                                                                                                 0)), self.rocky.posHprInterval(13, (0,
                                                                                                                                                     134.5,
                                                                                                                                                     3.725), (0,
                                                                                                                                                              0,
                                                                                                                                                              0)), Func(self.rocky.loop, 'neutral'))
        self.tv = loader.loadModel('phase_4/models/events/election_tv')
        self.tv.setPosHprScale(1.5, 128, 25, 0, 0.0, 0.0, 1.5, 1.5, 1.5)
        self.videoSequence = None
        tvTex = loader.loadTexture('phase_4/maps/election_pallette_1_6_reborn.jpg')
        tvTs = self.tv.findTextureStage('*')
        self.tv.setTexture(tvTs, tvTex, 1)
        self.tvIdle = Sequence(self.tv.posInterval(2.5, (1.5, 128, 24), blendType='easeInOut'), self.tv.posInterval(2.5, (1.5,
                                                                                                                          128,
                                                                                                                          25), blendType='easeInOut'), self.tv.posInterval(2.5, (1.5,
                                                                                                                                                                                 128,
                                                                                                                                                                                 24), blendType='easeInOut'), self.tv.posInterval(2.5, (1.5,
                                                                                                                                                                                                                                        128,
                                                                                                                                                                                                                                        25), blendType='easeInOut'))
        self.prop = BattleProps.globalPropPool.getProp('propeller')
        propJoint = self.tv.find('**/topSphere')
        self.prop.reparentTo(propJoint)
        self.prop.loop('propeller', fromFrame=0, toFrame=8)
        self.prop.setPos(0, 1, 2)
        self.prop.setScale(2.0, 1.5, 1.0)
        standbyTex = loader.loadTexture('phase_4/maps/tv_standby_reborn.jpg')
        screenTs = self.tv.find('**/screen').findTextureStage('*')
        self.tv.find('**/screen').setTexture(screenTs, standbyTex, 1)
        self.tv.find('**/screen').setTexScale(screenTs, 1.2, 1.2)
        self.tv.find('**/screen').setTexOffset(screenTs, -0.09, -0.1)
        self.tv.find('**/screen').setTexHpr(screenTs, 1, 0, 0)
        self.crate1 = loader.loadModel('phase_10/models/cashbotHQ/CBWoodCrate')
        self.crate1.setScale(2.2)
        self.crate1.setPos(-7, 128, 3.725)
        self.crate2 = loader.loadModel('phase_10/models/cashbotHQ/CBWoodCrate')
        self.crate2.setScale(2.2)
        self.crate2.setPos(6.2, 128, 3.725)
        self.crate3 = loader.loadModel('phase_10/models/cashbotHQ/CBWoodCrate')
        self.crate3.setScale(2.3)
        self.crate3.setPos(19.7, 128, 4.625)
        self.crate4 = loader.loadModel('phase_10/models/cashbotHQ/CBWoodCrate')
        self.crate4.setScale(2.3)
        self.crate4.setPos(-20.5, 128, 4.625)
        self.crates = [
         self.crate1, self.crate2, self.crate3, self.crate4]
        self.sfxExplode = loader.loadSfx('phase_3.5/audio/sfx/ENC_cogfall_apart.ogg')
        self.crateExplosion = loader.loadModel('phase_3.5/models/props/explosion')
        self.crateExplosion.setBillboardPointEye()
        self.crateExplosion.setPos(0, 0, 2)
        self.placeholder1 = render.attachNewNode('explosion-placeholder')
        self.placeholder1.setPos(-7, 128, 3.725)
        self.placeholder1.setScale(3)
        self.placeholder2 = render.attachNewNode('explosion-placeholder')
        self.placeholder2.setPos(6.2, 128, 3.725)
        self.placeholder2.setScale(3)
        self.placeholder3 = render.attachNewNode('explosion-placeholder')
        self.placeholder3.setPos(19.7, 128, 4.625)
        self.placeholder3.setScale(3)
        self.placeholder4 = render.attachNewNode('explosion-placeholder')
        self.placeholder4.setPos(-20.5, 128, 4.625)
        self.placeholder4.setScale(3)
        self.crateDust = loader.loadModel('phase_3.5/models/props/dust_cloud')
        self.crateDust.setBillboardPointEye()
        self.crateDust.setPos(0, 0, 2)
        self.stomper1 = StomperObstacle(self)
        self.stomper1.setPos(68.33, 296.983, 23.525)
        self.stomper1.setScale(0.75)
        self.stomper2 = StomperObstacle(self)
        self.stomper2.setPos(68.33, 283.983, 23.525)
        self.stomper2.setScale(0.75)
        self.stomper3 = StomperObstacle(self)
        self.stomper3.setPos(68.33, 268.983, 24.425)
        self.stomper3.setScale(0.75)
        self.stomper4 = StomperObstacle(self)
        self.stomper4.setPos(68.33, 310.983, 24.425)
        self.stomper4.setScale(0.75)
        self.stomper5 = StomperObstacle(self)
        self.stomper5.setPos(170, 296.983, 3.725)
        self.stomper5.setScale(0.75)
        self.stomper6 = StomperObstacle(self)
        self.stomper6.setPos(170, 283.983, 3.725)
        self.stomper6.setScale(0.75)
        self.stomper7 = StomperObstacle(self)
        self.stomper7.setPos(170, 268.983, 4.625)
        self.stomper7.setScale(0.75)
        self.stomper8 = StomperObstacle(self)
        self.stomper8.setPos(170, 310.983, 4.625)
        self.stomper8.setScale(0.75)
        self.stomper9 = StomperObstacle(self)
        self.stomper9.setPos(262, 296.983, -16.075)
        self.stomper9.setScale(0.75)
        self.stomper10 = StomperObstacle(self)
        self.stomper10.setPos(262, 283.983, -16.075)
        self.stomper10.setScale(0.75)
        self.stomper11 = StomperObstacle(self)
        self.stomper11.setPos(262, 268.983, -15.175)
        self.stomper11.setScale(0.75)
        self.stomper12 = StomperObstacle(self)
        self.stomper12.setPos(262, 310.983, -15.175)
        self.stomper12.setScale(0.75)
        self.stomper13 = StomperObstacle(self)
        self.stomper13.setPos(290.39, 192.02, -15.175)
        self.stomper13.setScale(0.75)
        self.stomper14 = StomperObstacle(self)
        self.stomper14.setPos(330.309, 155.821, -15.175)
        self.stomper14.setScale(0.75)
        self.stomper15 = StomperObstacle(self)
        self.stomper15.setPos(290.39, 96.191, -15.175)
        self.stomper15.setScale(0.75)
        self.stomper16 = StomperObstacle(self)
        self.stomper16.setPos(330.309, 49.358, -15.175)
        self.stomper16.setScale(0.75)
        self.stompers = [
         self.stomper1, self.stomper2, self.stomper3, self.stomper4, self.stomper5, self.stomper6, self.stomper7, self.stomper8, self.stomper9, self.stomper10, self.stomper11, self.stomper12, self.stomper13, self.stomper14, self.stomper15, self.stomper16]
        self.gavel1 = GavelObstacle(self)
        self.gavel1.setIndex(1)
        self.gavel1.setPosHpr(-21.973, 210.944, 24.425, -87.728, 0, 0)
        self.gavel2 = GavelObstacle(self)
        self.gavel2.setIndex(1)
        self.gavel2.setPosHpr(21.331, 210.944, 24.425, 449.151, 0, 0)
        self.gavel3 = GavelObstacle(self)
        self.gavel3.setIndex(1)
        self.gavel3.setPosHpr(320, 296, -15.175, -2023, 0, 0)
        self.gavel4 = GavelObstacle(self)
        self.gavel4.setIndex(1)
        self.gavel4.setPosHpr(291, 267, -15.175, -2201.3, 0, 0)
        self.gavel5 = GavelObstacle(self)
        self.gavel5.setIndex(1)
        self.gavel5.setPosHpr(334, 9.3, -15.175, 132.4, 0, 0)
        self.gavel6 = GavelObstacle(self)
        self.gavel6.setIndex(1)
        self.gavel6.setPosHpr(303.35, -19.3, -15.175, -55, 0, 0)
        self.gavel7 = GavelObstacle(self)
        self.gavel7.setIndex(1)
        self.gavel7.setPosHpr(891.591, -16.575, 4.625, 44, 0, 0)
        self.gavel8 = GavelObstacle(self)
        self.gavel8.setIndex(1)
        self.gavel8.setPosHpr(863.781, 13.168, 4.625, 228, 0, 0)
        self.gavels = [
         self.gavel1, self.gavel2, self.gavel3, self.gavel4, self.gavel5, self.gavel6, self.gavel7, self.gavel8]
        self.goon1 = GoonObstacle(self)
        self.goon1.setStrength(10)
        self.goon1.setPosHpr(-6.89, 272.23, 23.525, -1813.49, 0, 0)
        self.goon1.setPath([-6.89, 272.23, 23.525], [17.387, 301.052, 23.525])
        self.goon2 = GoonObstacle(self)
        self.goon2.setStrength(10)
        self.goon2.setPosHpr(17.048, 267.604, 23.525, -1640.49, 0, 0)
        self.goon2.setPath([17.048, 267.604, 23.525], [-10.683, 272.045, 23.525])
        self.goon2.setReverseTheta(True)
        self.goon3 = GoonObstacle(self)
        self.goon3.setStrength(10)
        self.goon3.setPosHpr(37.726, 291.77, 23.525, -1640.49, 0, 0)
        self.goon3.setPath([37.726, 291.77, 23.525], [-4.856, 296.225, 23.525])
        self.goon3.setReverseTheta(True)
        self.goon4 = GoonObstacle(self)
        self.goon4.setStrength(15)
        self.goon4.setPosHpr(40.249, 309.755, 23.525, -1640.49, 0, 0)
        self.goon4.setPath([40.249, 303.755, 23.525], [40.823, 285.267, 23.525])
        self.goon4.setPathDuration(7)
        self.goon5 = GoonObstacle(self)
        self.goon5.setStrength(15)
        self.goon5.setPosHpr(87.099, 303.706, 23.083, -1640.49, 0, 0)
        self.goon5.setPath([87.099, 303.706, 23.083], [141.305, 277.422, 5.852])
        self.goon6 = GoonObstacle(self)
        self.goon6.setStrength(15)
        self.goon6.setPosHpr(115.892, 304.86, 14.479, -1640.49, 0, 0)
        self.goon6.setPath([115.892, 304.86, 14.479], [115.784, 271.53, 14.479])
        self.goon6.setPathDuration(9)
        self.goon6.setReverseTheta(True)
        self.goon7 = GoonObstacle(self)
        self.goon7.setStrength(15)
        self.goon7.setPosHpr(137.78, 275.436, 7.6, -1640.49, 0, 0)
        self.goon7.setPath([137.78, 275.436, 7.6], [137.64, 302.422, 7.6])
        self.goon7.setPathDuration(8)
        self.goon7.setReverseTheta(True)
        self.goon8 = GoonObstacle(self)
        self.goon8.setStrength(15)
        self.goon8.setPosHpr(239.106, 277.31, -14.312, -1640.49, 0, 0)
        self.goon8.setPath([239.106, 277.31, -14.312], [239.212, 302.4, -14.312])
        self.goon8.setPathDuration(9)
        self.goon9 = GoonObstacle(self)
        self.goon9.setStrength(15)
        self.goon9.setPosHpr(179.888, 281.688, 3.725, -1640.49, 0, 0)
        self.goon9.setPath([179.888, 281.688, 3.725], [235.849, 296.205, -13.825])
        self.goon9.setPathDuration(10)
        self.goon10 = GoonObstacle(self)
        self.goon10.setStrength(15)
        self.goon10.setPosHpr(188.76, 273.976, 1.264, -1640.49, 0, 0)
        self.goon10.setPath([188.76, 273.976, 1.264], [188.636, 304.722, 1.264])
        self.goon10.setPathDuration(9)
        self.goon10.setReverseTheta(True)
        self.goon11 = GoonObstacle(self)
        self.goon11.setStrength(20)
        self.goon11.setPosHpr(320, 50, -16.075, -1640.49, 0, 0)
        self.goon11.setPath([320, 50, -16.075], [320.01, 230, -16.075])
        self.goon11.setPathDuration(13)
        self.goon12 = GoonObstacle(self)
        self.goon12.setStrength(20)
        self.goon12.setPosHpr(310, 50, -16.075, -1640.49, 0, 0)
        self.goon12.setPath([310, 230, -16.075], [310.01, 50, -16.075])
        self.goon12.setPathDuration(13)
        self.goon13 = GoonObstacle(self)
        self.goon13.setStrength(20)
        self.goon13.setPosHpr(300, 50, -16.075, -1640.49, 0, 0)
        self.goon13.setPath([300, 50, -16.075], [300.01, 230, -16.075])
        self.goon13.setPathDuration(13)
        self.goon14 = GoonObstacle(self)
        self.goon14.setStrength(10)
        self.goon14.setPosHpr(455, -2.268, 3.725, -1640.49, 0, 0)
        self.goon14.setPath([455, -2.268, 3.725], [522.01, 11, 4.625])
        self.goon14.setPathDuration(7)
        self.goon15 = GoonObstacle(self)
        self.goon15.setStrength(10)
        self.goon15.setPosHpr(522.01, -32.1, 4.625, -1640.49, 0, 0)
        self.goon15.setPath([522.01, -32.1, 4.625], [455, -22, 3.725])
        self.goon15.setPathDuration(7)
        self.goon15.setReverseTheta(True)
        self.goon16 = GoonObstacle(self)
        self.goon16.setStrength(15)
        self.goon16.setPosHpr(535, -20.6, 3.725, -1640.49, 0, 0)
        self.goon16.setPath([535, -20.6, 3.725], [535.01, 4.2, 3.725])
        self.goon16.setPathDuration(7)
        self.goon17 = GoonObstacle(self)
        self.goon17.setStrength(20)
        self.goon17.setPosHpr(600, 2.1, 3.725, -1640.49, 0, 0)
        self.goon17.setPath([600, 2.1, 3.725], [460, 2.1, 3.725])
        self.goon17.setPathDuration(13)
        self.goon17.setReverseTheta(True)
        self.goon18 = GoonObstacle(self)
        self.goon18.setStrength(20)
        self.goon18.setPosHpr(460, -7.1, 3.725, -1640.49, 0, 0)
        self.goon18.setPath([460, -7.1, 3.725], [600, -7.1, 3.725])
        self.goon18.setPathDuration(13)
        self.goon19 = GoonObstacle(self)
        self.goon19.setStrength(20)
        self.goon19.setPosHpr(600, -14.6, 3.725, -1640.49, 0, 0)
        self.goon19.setPath([600, -14.6, 3.725], [460, -14.6, 3.725])
        self.goon19.setPathDuration(13)
        self.goon19.setReverseTheta(True)
        self.goon20 = GoonObstacle(self)
        self.goon20.setStrength(20)
        self.goon20.setPosHpr(460, -19.4, 3.725, -1640.49, 0, 0)
        self.goon20.setPath([460, -19.4, 3.725], [600, -19.4, 3.725])
        self.goon20.setPathDuration(13)
        self.goon21 = GoonObstacle(self)
        self.goon21.setStrength(10)
        self.goon21.setPosHpr(705, -2.268, 3.725, -1640.49, 0, 0)
        self.goon21.setPath([705, -2.268, 3.725], [772.01, 11, 4.625])
        self.goon21.setPathDuration(7)
        self.goon22 = GoonObstacle(self)
        self.goon22.setStrength(10)
        self.goon22.setPosHpr(772.01, -32.1, 4.625, -1640.49, 0, 0)
        self.goon22.setPath([772.01, -32.1, 4.625], [705, -22, 3.725])
        self.goon22.setPathDuration(7)
        self.goon22.setReverseTheta(True)
        self.goon23 = GoonObstacle(self)
        self.goon23.setStrength(15)
        self.goon23.setPosHpr(785, -20.6, 3.725, -1640.49, 0, 0)
        self.goon23.setPath([785, -20.6, 3.725], [785.01, 4.2, 3.725])
        self.goon23.setPathDuration(7)
        self.goon24 = GoonObstacle(self)
        self.goon24.setStrength(20)
        self.goon24.setPosHpr(850, 2.1, 3.725, -1640.49, 0, 0)
        self.goon24.setPath([850, 2.1, 3.725], [710, 2.1, 3.725])
        self.goon24.setPathDuration(13)
        self.goon24.setReverseTheta(True)
        self.goon25 = GoonObstacle(self)
        self.goon25.setStrength(20)
        self.goon25.setPosHpr(710, -7.1, 3.725, -1640.49, 0, 0)
        self.goon25.setPath([710, -7.1, 3.725], [850, -7.1, 3.725])
        self.goon25.setPathDuration(13)
        self.goon26 = GoonObstacle(self)
        self.goon26.setStrength(20)
        self.goon26.setPosHpr(850, -14.6, 3.725, -1640.49, 0, 0)
        self.goon26.setPath([850, -14.6, 3.725], [710, -14.6, 3.725])
        self.goon26.setPathDuration(13)
        self.goon26.setReverseTheta(True)
        self.goon27 = GoonObstacle(self)
        self.goon27.setStrength(20)
        self.goon27.setPosHpr(710, -19.4, 3.725, -1640.49, 0, 0)
        self.goon27.setPath([710, -19.4, 3.725], [850, -19.4, 3.725])
        self.goon27.setPathDuration(13)
        self.goons = [
         self.goon1, self.goon2, self.goon3, self.goon4, self.goon5, self.goon6, self.goon7, self.goon8, self.goon9, self.goon10, self.goon11, self.goon12, self.goon13, self.goon14, self.goon15, self.goon16, self.goon17, self.goon18, self.goon19, self.goon20, self.goon21, self.goon22, self.goon23, self.goon24, self.goon25, self.goon26, self.goon27]
        self.securityCamera1 = SecurityCameraObstacle(self)
        self.securityCamera1.setPosHpr(336.305, 192.02, -15.175, 36, 0, 0)
        self.securityCamera2 = SecurityCameraObstacle(self)
        self.securityCamera2.setPosHpr(285.39, 155.821, -15.175, -36, 0, 0)
        self.securityCamera3 = SecurityCameraObstacle(self)
        self.securityCamera3.setPosHpr(336.288, 96.191, -15.175, 36, 0, 0)
        self.securityCamera4 = SecurityCameraObstacle(self)
        self.securityCamera4.setPosHpr(285.298, 49.358, -15.175, -36, 0, 0)
        self.securityCameras = [
         self.securityCamera1, self.securityCamera2, self.securityCamera3, self.securityCamera4]
        self.chopper1 = ChopperObstacle(self)
        self.chopper1.setPosHpr(881.5, 64.8, 3.725, 180, 0, 0)
        self.chopper2 = ChopperObstacle(self)
        self.chopper2.setPosHpr(840.8, -25.775, 4.625, 60, 0, 0)
        self.chopper3 = ChopperObstacle(self)
        self.chopper3.setPosHpr(805.405, 6.112, 4.625, 114, 0, 0)
        self.chopper4 = ChopperObstacle(self)
        self.chopper4.setPosHpr(461.4, -10.5, 3.725, -267, 0, 0)
        self.chopper5 = ChopperObstacle(self)
        self.chopper5.setPosHpr(675, -10.5, 3.725, -267, 0, 0)
        self.choppers = [
         self.chopper1, self.chopper2, self.chopper3, self.chopper4, self.chopper5]
        self.healBarrel1 = SewerHealBarrel(self)
        self.healBarrel1.setPos(68.33, 310.983, 24.425)
        self.healBarrel2 = SewerHealBarrel(self)
        self.healBarrel2.setPos(304.99, 276.449, -16.075)
        self.healBarrel3 = SewerHealBarrel(self)
        self.healBarrel3.setPos(643, -8.3, 3.725)
        self.barrels = [
         self.healBarrel1, self.healBarrel2, self.healBarrel3]
        return

    def enterOff(self, offset):
        pass

    def exitOff(self):
        pass

    def setupObstacles(self):
        for stomper in self.stompers:
            stomper.loadModel()
            stomper.startStomper()
            stomper.reparentTo(render)

        for gavel in self.gavels:
            gavel.generate()
            gavel.setState('N')

        for goon in self.goons:
            goon.generate()
            goon.reparentTo(render)
            goon.request('Walk')
            goon.show()

        for securityCamera in self.securityCameras:
            securityCamera.generate()
            securityCamera.reparentTo(render)

        for chopper in self.choppers:
            chopper.generate()
            chopper.reparentTo(render)

        for barrel in self.barrels:
            barrel.generate()
            barrel.reparentTo(render)

        self.obstaclesSetup = True

    def disableObstacles(self):
        for stomper in self.stompers:
            stomper.disable()
            stomper.delete()

        for gavel in self.gavels:
            gavel.disable()
            gavel.delete()

        for goon in self.goons:
            goon.disable()
            goon.delete()

        for securityCamera in self.securityCameras:
            securityCamera.disable()
            securityCamera.delete()

        for chopper in self.choppers:
            chopper.disable()
            chopper.delete()

        for barrel in self.barrels:
            barrel.disable()
            barrel.delete()

        self.obstaclesSetup = False

    def deleteObstacles(self):
        del self.stompers
        self.stompers = []
        del self.gavels
        self.gavels = []
        del self.goons
        self.goons = []
        del self.securityCameras
        self.securityCameras = []
        del self.choppers
        self.choppers = []
        del self.barrels
        self.barrels = []

    def hideEach(self, obj):
        for x in obj:
            x.reparentTo(hidden)

    def __cleanupNPCs(self):
        npcs = [self.rocky]
        for npc in npcs:
            if npc:
                npc.removeActive()
                npc.hide()

    def delete(self):
        self.demand('Off', 0.0)
        self.ignore('entercnode')
        self.disableLocalToonSimpleCollisions()
        self.__cleanupNPCs()
        for crate in self.crates:
            crate.removeNode()

        del self.crates
        self.crates = []
        if self.obstaclesSetup == True:
            self.disableObstacles()
        self.deleteObstacles()
        if self.videoSequence:
            self.videoSequence.pause()
        self.prop.cleanup()
        self.prop.removeNode()
        self.tv.removeNode()
        self.cr.sewerMinigame = None
        DistributedObject.delete(self)
        return

    def enterIdle(self, offset):
        self.rocky.reparentTo(render)
        self.rocky.loop('neutral')
        self.rocky.addActive()
        for crate in self.crates:
            crate.reparentTo(render)

        self.tv.reparentTo(render)
        self.tvIdle.loop()
        self.welcomeInterval = Sequence(Func(self.rocky.setChatAbsolute, 'Toons, these are the Cog Nation Sewers... probably the nastiest place in the Tooniverse! ...quite literally.', CFSpeech | CFTimeout), Wait(8), Func(self.rocky.setChatAbsolute, 'Some fellow Resistance Rangers and Toon Troopers have been positioned up ahead by Lord Lowden Clear to assist you Toons in reaching Toontown- or should I say Cog Nation Central.', CFSpeech | CFTimeout), Wait(10), Func(self.rocky.setChatAbsolute, "I'm trying to tune into a signal being given to us by Doctor Surlee- these darned contraptions aren't working!", CFSpeech | CFTimeout), Wait(8), Func(self.rocky.setChatAbsolute, "Just sit sight, and wait for your fellow Toons to come along. I'll probably be in contact with Surlee by then.", CFSpeech | CFTimeout), Wait(8))
        self.welcomeInterval.loop()
        self.welcomeInterval.setT(offset)

    def exitIdle(self):
        self.welcomeInterval.finish()

    def enterEvent(self, offset):
        base.cr.playGame.hood.loader.music.stop()
        minigameMusic = loader.loadMusic('phase_14/audio/bgm/SE_minigame.ogg')
        minigameVideo = 'phase_14/video/SE_minigame_introduction.mp4'
        self.rocky.reparentTo(render)
        self.rocky.loop('neutral')
        self.rocky.addActive()
        self.eventInterval = Sequence(Func(base.camera.wrtReparentTo, render), Func(base.localAvatar.stopUpdateSmartCamera), Func(base.localAvatar.shutdownSmartCamera), Func(NodePath(base.marginManager).hide), Func(NodePath(self.laffMeter).hide), Func(NodePath(self.book).hide), base.camera.posHprInterval(5, (0,
                                                                                                                                                                                                                                                                                                                      -26.5,
                                                                                                                                                                                                                                                                                                                      7.325), (180,
                                                                                                                                                                                                                                                                                                                               0,
                                                                                                                                                                                                                                                                                                                               0), blendType='easeInOut'), Func(self.rocky.setChatAbsolute, "Hold up, Toons- I'm getting an incoming signal from Doctor Surlee!", CFSpeech | CFTimeout), Wait(4), Func(self.rocky.setChatAbsolute, 'I think we should take a look at the TV...', CFSpeech | CFTimeout), Wait(3), base.camera.posHprInterval(5, (2,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                103.6,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                25.325), (0,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          0,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          0), blendType='easeInOut'), Func(self.startVideo, self.tv, minigameVideo), Wait(54), Func(self.stopVideo), base.camera.posHprInterval(5, (0,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    75.6,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    19.325), (0,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              -15,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              0), blendType='easeInOut'), Func(self.crateExplosion.reparentTo, self.placeholder1), Func(base.playSfx, self.sfxExplode, volume=0.9), Func(self.crateDust.reparentTo, self.placeholder1), Wait(0.6), Func(self.crate1.reparentTo, hidden), Func(self.crateExplosion.reparentTo, self.placeholder2), Func(base.playSfx, self.sfxExplode, volume=0.9), Func(self.crateDust.reparentTo, self.placeholder2), Wait(0.6), Func(self.crate2.reparentTo, hidden), Func(self.crateExplosion.reparentTo, self.placeholder3), Func(base.playSfx, self.sfxExplode, volume=0.9), Func(self.crateDust.reparentTo, self.placeholder3), Wait(0.6), Func(self.crate3.reparentTo, hidden), Func(self.crateExplosion.reparentTo, self.placeholder4), Func(base.playSfx, self.sfxExplode, volume=0.9), Func(self.crateDust.reparentTo, self.placeholder4), Wait(0.6), Func(self.crate4.reparentTo, hidden), Func(self.crateExplosion.removeNode), Func(self.crateDust.removeNode), Wait(2), Func(self.rocky.setChatAbsolute, "You heard him Toons! Let's go!", CFSpeech | CFTimeout), Wait(1), Func(NodePath(base.marginManager).show), Func(NodePath(self.laffMeter).show), Func(NodePath(self.book).show), Func(base.localAvatar.attachCamera), Func(base.localAvatar.initializeSmartCamera), Func(base.localAvatar.startUpdateSmartCamera), Func(self.setupObstacles), Func(base.playMusic, minigameMusic, looping=1, volume=1), Func(self.rockyWalkInterval.start))
        self.eventInterval.start()
        self.eventInterval.setT(offset)

    def exitEvent(self):
        self.eventInterval.finish()

    def enterEventTwo(self, offset):
        pass

    def exitEventTwo(self):
        pass

    def setState(self, state, timestamp):
        self.request(state, globalClockDelta.localElapsedTime(timestamp))

    def b_setOuch(self, penalty, anim=None):
        self.notify.debug('b_setOuch %s' % penalty)
        av = base.localAvatar
        if not av.isStunned:
            self.d_setOuch(penalty)
            self.setOuch(penalty, anim)

    def d_setOuch(self, penalty):
        self.sendUpdate('setOuch', [penalty])

    def setOuch(self, penalty, anim=None):
        if anim == 'Squish':
            if base.cr.playGame.getPlace():
                base.cr.playGame.getPlace().fsm.request('squished')
        elif anim == 'Fall':
            if base.cr.playGame.getPlace():
                base.cr.playGame.getPlace().fsm.request('fallDown')
        av = base.localAvatar
        av.stunToon()
        av.playDialogueForString('!')

    def touchedGavel(self, gavel, entry):
        self.notify.debug('touchedGavel')
        attackCodeStr = entry.getIntoNodePath().getNetTag('attackCode')
        if attackCodeStr == '':
            self.notify.warning('Node %s has no attackCode tag.' % repr(entry.getIntoNodePath()))
            return
        attackCode = int(attackCodeStr)
        into = entry.getIntoNodePath()
        self.zapLocalToon(attackCode, into)

    def touchedGavelHandle(self, gavel, entry):
        attackCodeStr = entry.getIntoNodePath().getNetTag('attackCode')
        if attackCodeStr == '':
            self.notify.warning('Node %s has no attackCode tag.' % repr(entry.getIntoNodePath()))
            return
        attackCode = int(attackCodeStr)
        into = entry.getIntoNodePath()
        self.zapLocalToon(attackCode, into)

    def zapLocalToon(self, attackCode, origin=None):
        if localAvatar.ghostMode or localAvatar.isStunned:
            return
        messenger.send('interrupt-pie')
        place = self.cr.playGame.getPlace()
        currentState = None
        if place:
            currentState = place.fsm.getCurrentState().getName()
        if currentState != 'walk' and currentState != 'finalBattle' and currentState != 'crane':
            return
        else:
            toon = localAvatar
            fling = 1
            shake = 0
            if attackCode == ToontownGlobals.BossCogAreaAttack:
                fling = 0
                shake = 1
            if fling:
                if origin == None:
                    origin = self
                camera.wrtReparentTo(render)
                toon.headsUp(origin)
                camera.wrtReparentTo(toon)
            pos = toon.getPos()
            hpr = toon.getHpr()
            timestamp = globalClockDelta.getFrameNetworkTime()
            self.sendUpdate('zapToon', [pos[0],
             pos[1],
             pos[2],
             hpr[0] % 360.0,
             hpr[1],
             hpr[2],
             attackCode,
             timestamp])
            self.doZapToon(toon, fling=fling, shake=shake)
            return

    def showZapToon(self, toonId, x, y, z, h, p, r, attackCode, timestamp):
        if toonId == localAvatar.doId:
            return
        else:
            ts = globalClockDelta.localElapsedTime(timestamp)
            pos = Point3(x, y, z)
            hpr = VBase3(h, p, r)
            fling = 1
            toon = self.cr.doId2do.get(toonId)
            if toon:
                if attackCode == ToontownGlobals.BossCogAreaAttack:
                    pos = None
                    hpr = None
                    fling = 0
                else:
                    ts -= toon.smoother.getDelay()
                self.doZapToon(toon, pos=pos, hpr=hpr, ts=ts, fling=fling)
            return

    def doZapToon(self, toon, pos=None, hpr=None, ts=0, fling=1, shake=1):
        zapName = toon.uniqueName('zap')
        self.clearInterval(zapName)
        zapTrack = Sequence(name=zapName)
        if toon == localAvatar:
            self.toOuchMode()
            messenger.send('interrupt-pie')
            self.enableLocalToonSimpleCollisions()
        else:
            zapTrack.append(Func(toon.stopSmooth))

        def getSlideToPos(toon=toon):
            return render.getRelativePoint(toon, Point3(0, -5, 0))

        if pos != None and hpr != None:
            (
             zapTrack.append(Func(toon.setPosHpr, pos, hpr)),)
        toonTrack = Parallel()
        if shake and toon == localAvatar:
            toonTrack.append(Sequence(Func(camera.setZ, camera, 1), Wait(0.15), Func(camera.setZ, camera, -2), Wait(0.15), Func(camera.setZ, camera, 1)))
        if fling:
            toonTrack += [ActorInterval(toon, 'slip-backward'), toon.posInterval(0.5, getSlideToPos, fluid=1)]
        else:
            toonTrack += [ActorInterval(toon, 'slip-forward')]
        zapTrack.append(toonTrack)
        if toon == localAvatar:
            zapTrack.append(Func(self.disableLocalToonSimpleCollisions))
            currentState = self.state
            if currentState == 'BattleThree':
                zapTrack.append(Func(self.toFinalBattleMode))
            else:
                if hasattr(self, 'chairs'):
                    zapTrack.append(Func(self.toFinalBattleMode))
                else:
                    zapTrack.append(Func(self.toWalkMode))
        else:
            zapTrack.append(Func(toon.startSmooth))
        if ts > 0:
            startTime = ts
        else:
            zapTrack = Sequence(Wait(-ts), zapTrack)
            startTime = 0
        zapTrack.append(Func(self.clearInterval, zapName))
        zapTrack.delayDelete = DelayDelete.DelayDelete(toon, 'DistributedSewerMinigame.doZapToon')
        zapTrack.start(startTime)
        self.storeInterval(zapTrack, zapName)
        return

    def storeInterval(self, interval, name):
        if name in self.activeIntervals:
            ival = self.activeIntervals[name]
            if hasattr(ival, 'delayDelete') or hasattr(ival, 'delayDeletes'):
                self.clearInterval(name, finish=1)
        self.activeIntervals[name] = interval

    def cleanupIntervals(self):
        for interval in self.activeIntervals.values():
            interval.finish()
            DelayDelete.cleanupDelayDeletes(interval)

        self.activeIntervals = {}

    def clearInterval(self, name, finish=1):
        if self.activeIntervals.has_key(name):
            ival = self.activeIntervals[name]
            if finish:
                ival.finish()
            else:
                ival.pause()
            if self.activeIntervals.has_key(name):
                DelayDelete.cleanupDelayDeletes(ival)
                del self.activeIntervals[name]
        else:
            self.notify.debug('interval: %s already cleared' % name)

    def toOuchMode(self):
        if self.cr:
            place = self.cr.playGame.getPlace()
            if place and hasattr(place, 'fsm'):
                place.setState('ouch')

    def enableLocalToonSimpleCollisions(self):
        if not self.toonSphere:
            sphere = CollisionSphere(0, 0, 1, 1)
            sphere.setRespectEffectiveNormal(0)
            sphereNode = CollisionNode('SimpleCollisions')
            sphereNode.setFromCollideMask(ToontownGlobals.WallBitmask | ToontownGlobals.FloorBitmask)
            sphereNode.setIntoCollideMask(BitMask32.allOff())
            sphereNode.addSolid(sphere)
            self.toonSphere = NodePath(sphereNode)
            self.toonSphereHandler = CollisionHandlerPusher()
            self.toonSphereHandler.addCollider(self.toonSphere, localAvatar)
        self.toonSphere.reparentTo(localAvatar)
        base.cTrav.addCollider(self.toonSphere, self.toonSphereHandler)

    def disableLocalToonSimpleCollisions(self):
        if self.toonSphere:
            base.cTrav.removeCollider(self.toonSphere)
            self.toonSphere.detachNode()

    def toWalkMode(self):
        if self.cr:
            place = self.cr.playGame.getPlace()
            if place and hasattr(place, 'fsm'):
                place.setState('walk')

    def setGrab(self, avId, entId):
        for barrel in self.barrels:
            if id(barrel) == entId:
                barrel.setGrab(avId)

    def startVideo(self, tv, video):
        if not video:
            return
        if not video.endswith('.mp4'):
            return
        movie = loader.loadTexture(video)
        sound = loader.loadSfx(video)
        movie.synchronizeTo(sound)
        ts = self.tv.find('**/screen').findTextureStage('*')
        self.tv.find('**/screen').setTexture(ts, movie, 1)
        self.tv.find('**/screen').setTexScale(ts, movie.getTexScale())
        self.tv.find('**/screen').setTexOffset(ts, -0.09, -0.1)
        self.tv.find('**/screen').setTexPos(ts, 1, 0, 0)
        self.tv.find('**/screen').setTexHpr(ts, 1, 0, 0)
        self.videoSequence = Sequence(SoundInterval(sound, volume=1.0), Func(self.startVideo, self.tv.find('**/screen'), video))
        self.videoSequence.start()

    def stopVideo(self):
        if self.videoSequence:
            self.videoSequence.pause()
        standbyTex = loader.loadTexture('phase_4/maps/tv_standby_reborn.jpg')
        screenTs = self.tv.find('**/screen').findTextureStage('*')
        self.tv.find('**/screen').setTexture(screenTs, standbyTex, 1)
        self.tv.find('**/screen').setTexScale(screenTs, 1.2, 1.2)
        self.tv.find('**/screen').setTexOffset(screenTs, -0.09, -0.1)
        self.tv.find('**/screen').setTexHpr(screenTs, 1, 0, 0)