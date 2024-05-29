# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.racing.DroppedGag
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from otp.avatar import ShadowCaster

class DroppedGag(NodePath, ShadowCaster.ShadowCaster):

    def __init__(self, name, geom):
        NodePath.__init__(self, name)
        ShadowCaster.ShadowCaster.__init__(self, False)
        self.gag = geom.copyTo(self)
        self.initializeDropShadow()
        self.setActiveShadow()
        self.dropShadow.setScale(1)

    def delete(self):
        ShadowCaster.ShadowCaster.delete(self)
        NodePath.removeNode(self)
        self.gag = None
        return

    def getGeomNode(self):
        return self.gag