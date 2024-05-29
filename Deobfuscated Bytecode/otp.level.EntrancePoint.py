# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.level.EntrancePoint
# Compiled at: 2014-04-30 09:53:54
from toontown.toonbase.ToontownGlobals import *
from direct.directnotify import DirectNotifyGlobal
import BasicEntities

class EntrancePoint(BasicEntities.NodePathEntity):

    def __init__(self, level, entId):
        BasicEntities.NodePathEntity.__init__(self, level, entId)
        self.rotator = self.attachNewNode('rotator')
        self.placer = self.rotator.attachNewNode('placer')
        self.initEntrancePoint()

    def destroy(self):
        self.destroyEntrancePoint()
        self.placer.removeNode()
        self.rotator.removeNode()
        del self.placer
        del self.rotator
        BasicEntities.NodePathEntity.destroy(self)

    def placeToon(self, toon, toonIndex, numToons):
        self.placer.setY(-self.radius)
        self.rotator.setH(-self.theta * (numToons - 1) * 0.5 + toonIndex * self.theta)
        toon.setPosHpr(self.placer, 0, 0, 0, 0, 0, 0)

    def initEntrancePoint(self):
        if self.entranceId >= 0:
            self.level.entranceId2entity[self.entranceId] = self

    def destroyEntrancePoint(self):
        if self.entranceId >= 0:
            if self.level.entranceId2entity.has_key(self.entranceId):
                del self.level.entranceId2entity[self.entranceId]

    if __dev__:

        def attribChanged(self, *args):
            BasicEntities.NodePathEntity.attribChanged(self, *args)
            self.destroyEntrancePoint()
            self.initEntrancePoint()