# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.hood.HQTelescopeAnimatedProp
# Compiled at: 2014-04-30 09:53:54
import AnimatedProp
from direct.actor import Actor
from direct.interval.IntervalGlobal import *

class HQTelescopeAnimatedProp(AnimatedProp.AnimatedProp):

    def __init__(self, node):
        AnimatedProp.AnimatedProp.__init__(self, node)
        parent = node.getParent()
        self.telescope = Actor.Actor(node, copy=0)
        self.telescope.reparentTo(parent)
        self.telescope.loadAnims({'anim': 'phase_3.5/models/props/HQ_telescope-chan'})
        self.telescope.pose('anim', 0)
        self.node = self.telescope
        self.track = Sequence(Wait(5.0), self.telescope.actorInterval('anim', startFrame=0, endFrame=32), Wait(0.5), self.telescope.actorInterval('anim', startFrame=32, endFrame=78), Wait(0.5), self.telescope.actorInterval('anim', startFrame=79, endFrame=112), Wait(0.5), self.telescope.actorInterval('anim', startFrame=112, endFrame=79), Wait(0.5), self.telescope.actorInterval('anim', startFrame=78, endFrame=32), Wait(0.5), self.telescope.actorInterval('anim', startFrame=32, endFrame=78), Wait(0.5), self.telescope.actorInterval('anim', startFrame=79, endFrame=112), Wait(0.5), self.telescope.actorInterval('anim', startFrame=112, endFrame=148), Wait(4.0), name=self.uniqueName('HQTelescope'))

    def delete(self):
        AnimatedProp.AnimatedProp.delete(self)
        self.node.cleanup()
        del self.node
        del self.telescope
        del self.track

    def enter(self):
        AnimatedProp.AnimatedProp.enter(self)
        self.track.loop()

    def exit(self):
        AnimatedProp.AnimatedProp.exit(self)
        self.track.finish()