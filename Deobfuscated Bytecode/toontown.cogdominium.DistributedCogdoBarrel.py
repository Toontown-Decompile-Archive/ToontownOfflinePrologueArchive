# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.cogdominium.DistributedCogdoBarrel
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from toontown.toonbase import ToontownGlobals, ToontownIntervals
from toontown.cogdominium import CogdoBarrelRoomConsts
from toontown.cogdominium import CogdoBarrelRoom
import random

class DistributedCogdoBarrel(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCogdoBarrel')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.barrelRoom = CogdoBarrelRoom.CogdoBarrelRoom()
        self.index = None
        self.state = None
        self.model = None
        self.collSphere = None
        self.collNode = None
        self.collNodePath = None
        self.availableTex = None
        self.usedTex = None
        self.brLaff = 0
        return

    def generate(self):
        DistributedObject.DistributedObject.generate(self)
        self.bumpSound = base.loadSfx(CogdoBarrelRoomConsts.BarrelBumpSound)
        self.grabSound = base.loadSfx(CogdoBarrelRoomConsts.BarrelGrabSound)

    def __setModel(self):
        self.model = loader.loadModel(CogdoBarrelRoomConsts.BarrelModel)
        self.model.setScale(CogdoBarrelRoomConsts.BarrelModelScale)
        self.model.setPos(self.__getProp('pos'))
        self.model.setH(self.__getProp('heading'))
        cogdoBarrelsNode = render.find('@@CogdoBarrels')
        if not cogdoBarrelsNode or cogdoBarrelsNode.isEmpty():
            cogdoBarrelsNode = render.attachNewNode('CogdoBarrels')
        self.model.reparentTo(cogdoBarrelsNode)
        self.availableTex = loader.loadTexture('phase_5/maps/tt_t_ara_cbr_Barrel_notUsed.jpg')
        self.usedTex = loader.loadTexture('phase_5/maps/tt_t_ara_cbr_Barrel_Used.jpg')
        self.model.setTexture(self.availableTex, 100)

    def __addCollision(self):
        if not self.collSphere:
            ax, ay, az = (0, 0, 0.5)
            bx, by, bz = (0, 0, 2.5)
            radius = 1
            self.collTube = CollisionTube(ax, ay, az, bx, by, bz, radius)
            self.collTube.setTangible(1)
            self.collSphere = CollisionSphere(*CogdoBarrelRoomConsts.BarrelCollParams)
            self.collSphere.setTangible(0)
            self.collNode = CollisionNode(self.uniqueName('barrelSphere'))
            self.collNode.setIntoCollideMask(ToontownGlobals.WallBitmask)
            self.collNode.addSolid(self.collSphere)
            self.collNode.addSolid(self.collTube)
            self.collNodePath = self.model.attachNewNode(self.collNode)
            self.collNodePath.hide()

    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        self.__setModel()
        self.__addCollision()

    def disable(self):
        DistributedObject.DistributedObject.disable(self)

    def delete(self):
        DistributedObject.DistributedObject.delete(self)
        ToontownIntervals.cleanup(self.__pulseIvalName())
        if self.model:
            self.model.removeNode()
            del self.model
            self.model = None
        self.ignore(self.uniqueName('enterbarrelSphere'))
        return

    def setIndex(self, index):
        self.index = index

    def __getProp(self, prop):
        return CogdoBarrelRoomConsts.BarrelProps[self.index][prop]

    def setState(self, state):
        self.state = state
        self.__updateState()

    def __updateState(self):
        if self.state == CogdoBarrelRoomConsts.StateAvailable:
            if self.model:
                self.model.unstash()
                self.model.setTexture(self.availableTex, 100)
            self.accept(self.uniqueName('enterbarrelSphere'), self.handleEnterSphere)
        elif self.state == CogdoBarrelRoomConsts.StateUsed:
            if self.model:
                self.model.unstash()
                self.model.setTexture(self.usedTex, 100)
            self.ignore(self.uniqueName('enterbarrelSphere'))
        elif self.state == CogdoBarrelRoomConsts.StateHidden or self.state == CogdoBarrelRoomConsts.StateCrushed:
            if self.model:
                self.model.stash()
            self.ignore(self.uniqueName('enterbarrelSphere'))
        else:
            if self.model:
                self.model.stash()
            self.ignore(self.uniqueName('enterbarrelSphere'))

    def handleEnterSphere(self, collEntry=None):
        base.playSfx(self.grabSound, volume=1, node=self.model, listener=camera)
        self.d_requestGrab()

    def d_requestGrab(self):
        self.sendUpdate('requestGrab', [])

    def setGrab(self, avId):
        toonup = CogdoBarrelRoomConsts.ToonUp
        if avId == base.localAvatar.doId:
            ToontownIntervals.start(ToontownIntervals.getPulseIval(self.model, self.__pulseIvalName(), 1.15, duration=0.2))
            self.setState(CogdoBarrelRoomConsts.StateUsed)
            self.brLaff = random.randint(toonup[0], toonup[1])

    def setReject(self):
        pass

    def getBarrelLaff(self):
        return self.brLaff

    def __pulseIvalName(self):
        return 'DistributedCogdoBarrelPulse%s' % self.doId

    def __str__(self):
        return 'Barrel %s' % self.index