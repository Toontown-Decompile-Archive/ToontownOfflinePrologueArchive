# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.MazeTreasure
# Compiled at: 2014-04-30 09:53:54
from direct.showbase.DirectObject import DirectObject
from toontown.toonbase.ToontownGlobals import *
from direct.directnotify import DirectNotifyGlobal

class MazeTreasure(DirectObject):
    RADIUS = 0.7

    def __init__(self, model, pos, serialNum, gameId):
        self.serialNum = serialNum
        self.nodePath = model.copyTo(render)
        self.nodePath.setPos(pos[0], pos[1], 1.0)
        self.sphereName = 'treasureSphere%s-%s' % (gameId, self.serialNum)
        self.collSphere = CollisionSphere(0, 0, 0, self.RADIUS)
        self.collSphere.setTangible(0)
        self.collNode = CollisionNode(self.sphereName)
        self.collNode.setIntoCollideMask(WallBitmask)
        self.collNode.addSolid(self.collSphere)
        self.collNodePath = self.nodePath.attachNewNode(self.collNode)
        self.collNodePath.hide()
        self.accept('enter' + self.sphereName, self.__handleEnterSphere)
        self.nodePath.flattenLight()

    def destroy(self):
        self.ignoreAll()
        self.nodePath.removeNode()
        del self.nodePath
        del self.collSphere
        self.collNodePath.removeNode()
        del self.collNodePath
        del self.collNode

    def __handleEnterSphere(self, collEntry):
        self.ignoreAll()
        messenger.send('MazeTreasureGrabbed', [self.serialNum])

    def showGrab(self):
        self.nodePath.reparentTo(hidden)
        self.collNode.setIntoCollideMask(BitMask32(0))