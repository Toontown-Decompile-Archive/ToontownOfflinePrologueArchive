# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.hood.PetShopFishAnimatedProp
# Compiled at: 2014-04-30 09:53:54
import AnimatedProp
from direct.actor import Actor
from direct.interval.IntervalGlobal import *

class PetShopFishAnimatedProp(AnimatedProp.AnimatedProp):

    def __init__(self, node):
        AnimatedProp.AnimatedProp.__init__(self, node)
        parent = node.getParent()
        self.fish = Actor.Actor(node, copy=0)
        self.fish.reparentTo(parent)
        self.fish.loadAnims({'swim': 'phase_4/models/props/exteriorfish-swim'})
        self.fish.pose('swim', 0)
        self.node = self.fish

    def delete(self):
        AnimatedProp.AnimatedProp.delete(self)
        self.fish.cleanup()
        del self.fish
        del self.node

    def enter(self):
        AnimatedProp.AnimatedProp.enter(self)
        self.fish.loop('swim')

    def exit(self):
        AnimatedProp.AnimatedProp.exit(self)
        self.fish.stop()