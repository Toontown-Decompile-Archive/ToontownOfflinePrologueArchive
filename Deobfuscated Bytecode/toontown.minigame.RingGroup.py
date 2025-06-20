# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.RingGroup
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from toontown.toonbase.ToonBaseGlobal import *
from pandac.PandaModules import NodePath
import Ring, RingTrack, RingTrackGroup, RingGameGlobals

class RingGroup(NodePath):

    def __init__(self, trackGroup, ringModel, posScale, colorIndices):
        NodePath.__init__(self)
        self.assign(hidden.attachNewNode(base.localAvatar.uniqueName('ring-group')))
        self.__period = trackGroup.period
        self.__reverseFlag = trackGroup.reverseFlag
        self.__tOffset = trackGroup.tOffset
        self.__numRings = len(trackGroup.tracks)
        self.__rings = []
        self.__ringModels = []
        for i in range(0, self.__numRings):
            track = trackGroup.tracks[i]
            tOffset = trackGroup.trackTOffsets[i]
            ring = Ring.Ring(track, tOffset, posScale)
            ring.reparentTo(self)
            model = ringModel.copyTo(ring)
            model.setColor(RingGameGlobals.ringColors[colorIndices[i]][1])
            self.__rings.append(ring)
            self.__ringModels.append(model)

    def delete(self):
        for model in self.__ringModels:
            model.removeNode()

        for ring in self.__rings:
            ring.removeNode()

        del self.__rings
        del self.__ringModels

    def getRing(self, index):
        return self.__ringModels[index]

    def setT(self, t):
        normT = (t / self.__period + self.__tOffset) % 1.0
        if self.__reverseFlag:
            normT = 1.0 - normT
        for ring in self.__rings:
            ring.setT(normT)