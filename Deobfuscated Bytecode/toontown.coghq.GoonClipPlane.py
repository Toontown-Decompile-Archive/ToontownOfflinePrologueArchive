# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.GoonClipPlane
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from otp.level import BasicEntities

class GoonClipPlane(BasicEntities.NodePathEntity):

    def __init__(self, level, entId):
        BasicEntities.NodePathEntity.__init__(self, level, entId)
        self.zoneNum = self.getZoneEntity().getZoneNum()
        self.initPlane()
        self.registerWithFactory()

    def destroy(self):
        self.unregisterWithFactory()
        BasicEntities.NodePathEntity.destroy(self)
        self.removeNode()

    def registerWithFactory(self):
        clipList = self.level.goonClipPlanes.get(self.zoneNum)
        if clipList:
            if self.entId not in clipList:
                clipList.append(self.entId)
        else:
            self.level.goonClipPlanes[self.zoneNum] = [
             self.entId]

    def unregisterWithFactory(self):
        clipList = self.level.goonClipPlanes.get(self.zoneNum)
        if clipList:
            if self.entId in clipList:
                clipList.remove(self.entId)

    def initPlane(self):
        self.coneClip = PlaneNode('coneClip')
        self.coneClip.setPlane(Plane(Vec3(1, 0, 0), Point3(0, 0, 0)))
        self.coneClipPath = self.attachNewNode(self.coneClip)

    def getPlane(self):
        return self.coneClipPath