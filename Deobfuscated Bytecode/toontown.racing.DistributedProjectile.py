# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.racing.DistributedProjectile
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.fsm import FSM
from direct.distributed.DistributedSmoothNode import DistributedSmoothNode
from otp.avatar.ShadowCaster import ShadowCaster

class DistributedProjectile(DistributedSmoothNode, ShadowCaster, NodePath):

    def __init__(self, cr):
        ShadowCaster.__init__(self)
        DistributedSmoothNode.__init__(self, cr)
        NodePath.__init__(self, 'Projectile')

    def announceGenerate(self):
        DistributedSmoothNode.announceGenerate(self)
        self.name = self.uniqueName('projectile')
        self.posHprBroadcastName = self.uniqueName('projectileBroadcast')
        geom = loader.loadModel('models/smiley')
        self.geom = geom
        self.geom.reparentTo(self)
        self.startSmooth()
        self.reparentTo(render)

    def generate(self):
        DistributedSmoothNode.generate(self)
        self.name = self.uniqueName('projectile')
        self.posHprBroadcastName = self.uniqueName('projectileBroadcast')
        geom = loader.loadModel('models/smiley')
        self.geom = geom
        self.geom.reparentTo(self)
        self.startSmooth()
        self.reparentTo(render)

    def setAvId(self, avId):
        self.avId = avId

    def delete(self):
        DistributedSmoothNode.delete(self)