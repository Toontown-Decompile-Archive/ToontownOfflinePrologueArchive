# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.DivingTreasure
# Compiled at: 2014-04-30 09:53:54
from direct.showbase.DirectObject import DirectObject
from toontown.toonbase.ToontownGlobals import *
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import *
import DivingGameGlobals

class DivingTreasure(DirectObject):

    def __init__(self, i):
        self.treasureNode = render.attachNewNode('treasure')
        loadBase = 'phase_4/models/minigames/'
        self.chest = loader.loadModel(loadBase + 'treasure')
        self.chest.reparentTo(self.treasureNode)
        self.chest.setPos(0, 0, -25)
        self.chest.setScale(1, 0.7, 1)
        self.chestId = i
        self.grabbedId = 0
        self.moveLerp = Sequence()
        self.treasureNode.setScale(0.04)
        self.treasureNode.setPos(-15 + 10.0 * i, 0.25, -36.0)
        cSphere = CollisionSphere(0.0, 0.0, 0.0, 45)
        cSphere.setTangible(0)
        name = str(i)
        cSphereNode = CollisionNode(name)
        cSphereNode.setIntoCollideMask(DivingGameGlobals.CollideMask)
        cSphereNode.addSolid(cSphere)
        self.chestNode = cSphereNode
        self.chestCNP = self.treasureNode.attachNewNode(cSphereNode)

    def destroy(self):
        self.ignoreAll()
        del self.chest
        self.moveLerp.finish()
        del self.moveLerp
        self.treasureNode.removeNode()
        del self.treasureNode