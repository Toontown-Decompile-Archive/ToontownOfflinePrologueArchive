# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.racing.FlyingGag
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from otp.avatar.ShadowCaster import ShadowCaster

class FlyingGag(NodePath, ShadowCaster):

    def __init__(self, name, geom=None):
        an = ActorNode('flyingGagAN')
        NodePath.__init__(self, an)
        self.actorNode = an
        self.gag = None
        self.gagNode = None
        ShadowCaster.__init__(self, False)
        if geom:
            self.gagNode = self.attachNewNode('PieNode')
            self.gag = geom.copyTo(self.gagNode)
            self.gag.setScale(3)
            self.gagNode.setHpr(0, -45, 0)
            self.gagNode.setPos(0, 0, 2)
            self.initializeDropShadow()
            self.setActiveShadow()
            self.dropShadow.setPos(0, 0, 2)
            self.dropShadow.setScale(3)
        return

    def delete(self):
        ShadowCaster.delete(self)
        NodePath.remove(self)
        self.gag = None
        return

    def getGeomNode(self):
        return self.gag