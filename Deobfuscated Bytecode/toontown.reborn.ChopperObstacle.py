# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.reborn.ChopperObstacle
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from toontown.coghq.StomperGlobals import *
from direct.distributed import ClockDelta
from direct.showbase.PythonUtil import lerp
from direct.actor.Actor import Actor
import math
from direct.directnotify import DirectNotifyGlobal
from pandac.PandaModules import NodePath
from direct.task import Task
from toontown.toonbase import ToontownGlobals
from toontown.coghq import BattleBlocker
import random
from math import *

def circleX(angle, radius, centerX, centerY):
    x = radius * cos(angle) + centerX
    return x


def circleY(angle, radius, centerX, centerY):
    y = radius * sin(angle) + centerY
    return y


def getCirclePoints(segCount, centerX, centerY, radius, wideX=1.0, wideY=1.0):
    returnShape = []
    for seg in range(0, int(segCount)):
        coordX = wideX * circleX(pi * 2.0 * float(float(seg) / float(segCount)), radius, centerX, centerY)
        coordY = wideY * circleY(pi * 2.0 * float(float(seg) / float(segCount)), radius, centerX, centerY)
        returnShape.append((coordX, coordY, 1))

    coordX = wideX * circleX(pi * 2.0 * float(0 / segCount), radius, centerX, centerY)
    coordY = wideY * circleY(pi * 2.0 * float(0 / segCount), radius, centerX, centerY)
    returnShape.append((coordX, coordY, 1))
    return returnShape


class ChopperObstacle(NodePath):
    notify = DirectNotifyGlobal.directNotify.newCategory('ChopperObstacle')
    chopperModels = ['phase_14/models/char/sewer_cogChopper_zero']

    def __init__(self, parent):
        node = hidden.attachNewNode('ChopperObstacle')
        NodePath.__init__(self, node)
        self.parent = parent
        self.trackBeamGN = None
        self.trackFloorGN = None
        self.trackX = 10.0
        self.trackY = -5.0
        self.radius = 5.0
        self.trackShape = []
        self.trackShape = getCirclePoints(7, 0.0, 0.0, self.radius)
        self.trackShapeFloor = []
        self.trackShapeFloor = getCirclePoints(16, 0.0, 0.0, self.radius)
        self.zFloat = 0.05
        self.projector = Point3(0, 0, 25)
        self.isToonIn = 0
        self.toonX = 0
        self.toonY = 0
        self.canDamage = 1
        self.accel = 1
        self.maxVel = 19.69
        self.vX = 0.0
        self.vY = 0.0
        self.targetX = self.trackX
        self.targetY = self.trackY
        self.target = 0
        self.trackTargetList = [None,
         None,
         None,
         None]
        self.lastTime = 0.0
        self.currentTime = 0.0
        self.delta = 0.0
        self.Norm = {}
        self.Norm['Red'] = 0.2
        self.Norm['Green'] = 0.2
        self.Norm['Blue'] = 0.2
        self.Norm['Alpha'] = 1.0
        self.Alert = {}
        self.Alert['Red'] = 1.0
        self.Alert['Green'] = 0.0
        self.Alert['Blue'] = 0.0
        self.Alert['Alpha'] = 1.0
        self.attackSound = loader.loadSfx('phase_9/audio/sfx/CHQ_GOON_tractor_beam_alarmed.ogg')
        self.onSound = loader.loadSfx('phase_11/audio/sfx/LB_camera_shutter_2.ogg')
        self.attackTrack = Parallel(SoundInterval(self.attackSound, node=self, volume=0.8), SoundInterval(self.onSound, node=self, volume=0.8))
        self.moveStartSound = loader.loadSfx('phase_11/audio/sfx/LB_laser_beam_on_2.ogg')
        self.moveStartTrack = Parallel(SoundInterval(self.moveStartSound, node=self, volume=0.4))
        self.moveLoopSound = loader.loadSfx('phase_11/audio/sfx/LB_laser_beam_hum_2.ogg')
        self.moveLoopSound.setLoop()
        self.moveLoopTrack = Parallel(SoundInterval(self.moveLoopSound, node=self, volume=0.4))
        self.moveStopSound = loader.loadSfx('phase_11/audio/sfx/LB_laser_beam_off_2.ogg')
        self.moveStopTrack = Parallel(SoundInterval(self.moveStopSound, node=self, volume=0.4))
        self.taskName = None
        self.modelPath = 0
        self.doId = id(self)
        return

    def generate(self):
        self.notify.debug('generate')
        self.trackBeamNode = self.attachNewNode('tracking Beam Node')
        self.trackBeamGN = GeomNode('tracking Beam')
        self.trackBeamNode.attachNewNode(self.trackBeamGN)
        self.trackBeamNode.setTransparency(TransparencyAttrib.MAlpha)
        self.trackBeamNode.setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd))
        self.trackBeamNode.setTwoSided(False)
        self.trackBeamNode.setDepthWrite(False)
        self.trackBeamNode.setColorScale(255, 255, 0, 1)
        self.trackFloorNode = self.attachNewNode('tracking floor Node')
        self.trackFloorGN = GeomNode('tracking Floor')
        self.trackFloorNode.attachNewNode(self.trackFloorGN)
        self.trackFloorNode.setTransparency(TransparencyAttrib.MAlpha)
        self.trackFloorNode.setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd))
        self.trackFloorNode.setTwoSided(False)
        self.trackFloorNode.setDepthWrite(False)
        self.trackFloorNode.setColorScale(255, 255, 0, 1)
        if not hasattr(self, 'trackTarget1'):
            self.trackTarget1 = None
        else:
            self.trackTargetList[1] = self.trackTarget1
        if not hasattr(self, 'trackTarget2'):
            self.trackTarget2 = None
        else:
            self.trackTargetList[2] = self.trackTarget2
        if not hasattr(self, 'trackTarget3'):
            self.trackTarget3 = None
        else:
            self.trackTargetList[3] = self.trackTarget3
        self.loadModel()
        self.detectName = 'chopper %s' % self.doId
        return

    def initCollisionGeom(self):
        pass

    def sendFail(self):
        self.battleStart()
        self.parent.sendUpdate('trapFire', [True])

    def battleStart(self):
        pass

    def setTarget(self, targetHash):
        targetCount = targetHash % 3
        sanity = 10
        self.target = None
        while targetCount >= 0 and sanity > 0:
            sanity -= 1
            for index in range(1, 4):
                if self.trackTargetList[index]:
                    if targetCount == 0:
                        self.target = self.trackTargetList[index]
                    targetCount -= 1

        return

    def setTrackTarget1(self, targetId):
        self.trackTarget1 = targetId
        self.trackTargetList[1] = targetId

    def setTrackTarget2(self, targetId):
        self.trackTarget2 = targetId
        self.trackTargetList[2] = targetId

    def setTrackTarget3(self, targetId):
        self.trackTarget3 = targetId
        self.trackTargetList[3] = targetId

    def __detect(self, task):
        distance = self.getDistance(localAvatar)
        greaterDim = self.gridScaleX
        if self.gridScaleY > self.gridScaleX:
            greaterDim = self.gridScaleY
        if distance < greaterDim * 1.6:
            if localAvatar.getPos(self)[0] > 0 and localAvatar.getPos(self)[0] < self.gridScaleX and localAvatar.getPos(self)[1] > 0 and localAvatar.getPos(self)[1] < self.gridScaleY:
                self.__toonHit()
            else:
                if self.isToonIn:
                    self.isToonIn = 0
                self.isToonIn = 0
        taskMgr.doMethodLater(0.1, self.__detect, self.detectName)
        return Task.done

    def __toonHit(self):
        posX = localAvatar.getPos(self)[0]
        posY = localAvatar.getPos(self)[1]
        tileX = int(posX / (self.gridScaleX / self.gridNumX))
        tileY = int(posY / (self.gridScaleY / self.gridNumY))
        if self.toonX != tileX or self.toonY != tileY or not self.isToonIn:
            self.toonX = tileX
            self.toonY = tileY
            self.isToonIn = 1
            if self.gridData[tileX][tileY] < len(self.gridSymbols):
                tileFunction = self.gridSymbols[self.gridData[tileX][tileY]][0]
                if tileFunction:
                    tileFunction()
            self.sendHit()
        self.isToonIn = 1

    def sendHit(self):
        self.parent.sendUpdate('hit', [self.toonX, self.toonY])

    def disable(self):
        self.notify.debug('disable')
        if self.moveLoopTrack.isPlaying():
            self.moveLoopTrack.finish()
        if self.attackTrack.isPlaying():
            self.attackTrack.finish()
        if self.moveStartTrack.isPlaying():
            self.moveStartTrack.finish()
        if self.moveStopTrack.isPlaying():
            self.moveStopTrack.finish()
        taskMgr.remove(self.detectName)

    def delete(self):
        self.notify.debug('delete')
        self.unloadModel()
        if self.taskName:
            taskMgr.remove(self.taskName)

    def loadModel(self):
        self.rotateNode = self.attachNewNode('rotate')
        self.model = Actor(self.chopperModels[self.modelPath])
        spotLight = self.model.find('**/spotLight').hide()
        spotLight1 = self.model.find('**/spotLight1').hide()
        if spotLight:
            spotLight.hide()
        if spotLight1:
            spotLight1.hide()
        self.model.setScale(0.5)
        self.model.reparentTo(self.rotateNode)
        self.model.loop('sewer_CogChopperL')
        self.model.setPosHpr(0, 1, 0, 180, 0, 0)
        self.taskName = 'chopperupdate %s' % self.doId
        taskMgr.add(self.__updateTrack, self.taskName, priority=25)

    def unloadModel(self):
        if self.model:
            self.model.cleanup()
            self.model.removeNode()
            del self.model
            self.model = None
        if self.trackBeamNode:
            self.trackBeamNode.removeNode()
            del self.trackBeamNode
            self.trackBeamNode = None
        if self.trackFloorNode:
            self.trackFloorNode.removeNode()
            del self.trackFloorNode
            self.trackFloorNode = None
        return

    def __updateTrack(self, task):
        self.rotateNode.setPos(self.projector)
        self.rotateNode.lookAt(Point3(self.trackX, self.trackY, 0.0))
        if base.localAvatar and not Vec3(base.localAvatar.getPos(self)).length() > 150:
            self.targetX = base.localAvatar.getPos(self)[0]
            self.targetY = base.localAvatar.getPos(self)[1]
        else:
            return Task.cont
        dt = globalClock.getDt()
        deccel = 1.0 - 1.0 * (dt * 7.0)
        if deccel < 0:
            deccel = 0.0
        dirX = 0.0
        dirY = 0.0
        distX = self.targetX - self.trackX
        distY = self.targetY - self.trackY
        trigDist = math.sqrt(distX * distX + distY * distY)
        totalDist = abs(distX) + abs(distY)
        propX = abs(distX) / (totalDist + 0.01)
        propY = abs(distY) / (totalDist + 0.01)
        if self.targetX != self.trackX:
            dirX = distX / abs(distX)
        if self.targetY != self.trackY:
            dirY = distY / abs(distY)
        if trigDist < self.radius * 0.5 + 1.0:
            self.vX = self.vX * deccel
            self.vY = self.vY * deccel
            self.moveStopTrack.start()
            self.moveLoopTrack.finish()
        else:
            if not self.moveLoopTrack.isPlaying():
                self.moveLoopTrack.start()
                self.moveStartTrack.start()
            self.vX += dirX * self.accel * propX
            self.vY += dirY * self.accel * propY
        if self.vX > self.maxVel:
            self.vX = self.maxVel
        if self.vX < -self.maxVel:
            self.vX = -self.maxVel
        if self.vY > self.maxVel:
            self.vY = self.maxVel
        if self.vY < -self.maxVel:
            self.vY = -self.maxVel
        self.trackX += self.vX * dt
        self.trackY += self.vY * dt
        self.genTrack()
        dist = self.getDist(base.localAvatar)
        if dist < self.radius and self.canDamage:
            self.canDamage = 0
            self.parent.sendUpdate('trapFire', [True])
            taskMgr.doMethodLater(2.0, self._resetDam, 'reset Damage')
            self.attackTrack.start()
        return Task.cont

    def _resetDam(self, task=None):
        self.canDamage = 1

    def getDist(self, thing):
        posTX = thing.getX()
        posTY = thing.getY()
        dx = thing.getPos(self)[0] - self.trackX
        dy = thing.getPos(self)[1] - self.trackY
        return sqrt(dx * dx + dy * dy)

    def genTrack(self):
        dist = self.getDist(base.localAvatar)
        draw = 1.0 / (0.01 + float(pow(dist, 0.4)))
        self.trackShape = []
        wideX = 1
        wideY = 1
        self.trackShape = getCirclePoints(5 + draw * 12.0, 0.0, 0.0, self.radius, wideX, wideY)
        self.trackShapeFloor = []
        self.trackShapeFloor = getCirclePoints(5 + draw * 50.0, 0.0, 0.0, self.radius, wideX, wideY)
        if self.trackBeamGN:
            self.trackBeamGN.removeAllGeoms()
        if self.trackFloorGN:
            self.trackFloorGN.removeAllGeoms()
        beamRed = 0.0
        beamGreen = 0.0
        beamBlue = 0.0
        beamAlpha = 1.0
        origin = {}
        origin['Red'] = 0.2
        origin['Green'] = 0.2
        origin['Blue'] = 0.2
        origin['Alpha'] = 1.0
        if self.canDamage:
            origin = self.Norm
        else:
            origin = self.Alert
        self.gFormat = GeomVertexFormat.getV3cp()
        self.trackBeamVertexData = GeomVertexData('holds my vertices', self.gFormat, Geom.UHDynamic)
        self.trackBeamVertexWriter = GeomVertexWriter(self.trackBeamVertexData, 'vertex')
        self.trackBeamColorWriter = GeomVertexWriter(self.trackBeamVertexData, 'color')
        self.trackFloorVertexData = GeomVertexData('holds my vertices', self.gFormat, Geom.UHDynamic)
        self.trackFloorVertexWriter = GeomVertexWriter(self.trackFloorVertexData, 'vertex')
        self.trackFloorColorWriter = GeomVertexWriter(self.trackFloorVertexData, 'color')
        self.trackBeamVertexWriter.addData3f(self.projector[0], self.projector[1], self.projector[2])
        self.trackBeamColorWriter.addData4f(origin['Red'], origin['Green'], origin['Blue'], origin['Alpha'])
        self.trackFloorVertexWriter.addData3f(self.trackX, self.trackY, self.zFloat)
        self.trackFloorColorWriter.addData4f(origin['Red'], origin['Green'], origin['Blue'], origin['Alpha'])
        for vertex in self.trackShape:
            self.trackBeamVertexWriter.addData3f(self.trackX + vertex[0], self.trackY + vertex[1], self.zFloat)
            self.trackBeamColorWriter.addData4f(beamRed, beamGreen, beamBlue, beamAlpha)

        for vertex in self.trackShapeFloor:
            self.trackFloorVertexWriter.addData3f(self.trackX + vertex[0], self.trackY + vertex[1], self.zFloat)
            self.trackFloorColorWriter.addData4f(origin['Red'], origin['Green'], origin['Blue'], origin['Alpha'])

        self.trackBeamTris = GeomTrifans(Geom.UHStatic)
        self.trackFloorTris = GeomTrifans(Geom.UHStatic)
        sizeTrack = len(self.trackShape)
        self.trackBeamTris.addVertex(0)
        for countVertex in range(1, sizeTrack + 1):
            self.trackBeamTris.addVertex(countVertex)

        self.trackBeamTris.addVertex(1)
        self.trackBeamTris.closePrimitive()
        self.trackBeamGeom = Geom(self.trackBeamVertexData)
        self.trackBeamGeom.addPrimitive(self.trackBeamTris)
        self.trackBeamGN.addGeom(self.trackBeamGeom)
        sizeTrack = len(self.trackShapeFloor)
        self.trackFloorTris.addVertex(0)
        for countVertex in range(1, sizeTrack + 1):
            self.trackFloorTris.addVertex(countVertex)

        self.trackFloorTris.addVertex(1)
        self.trackFloorTris.closePrimitive()
        self.trackFloorGeom = Geom(self.trackFloorVertexData)
        self.trackFloorGeom.addPrimitive(self.trackFloorTris)
        self.trackFloorGN.addGeom(self.trackFloorGeom)

    def setProjector(self, projPoint):
        self.projector = projPoint
        if self.trackBeamGN and self.trackFloorGN:
            self.genTrack()

    def setHideModel(self, flag):
        if flag:
            self.model.stash()
        else:
            self.model.unstash()