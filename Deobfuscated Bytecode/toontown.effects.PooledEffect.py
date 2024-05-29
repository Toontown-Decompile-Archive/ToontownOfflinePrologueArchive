# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.effects.PooledEffect
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.showbase import Pool
from direct.showbase.DirectObject import DirectObject
import re

class PooledEffect(DirectObject, NodePath):
    pool = None
    poolLimit = 124

    @classmethod
    def getEffect(cls, context=''):
        if cls.pool is None:
            cls.pool = Pool.Pool()
        if cls.pool.hasFree():
            return cls.pool.checkout()
        else:
            free, used = cls.pool.getNumItems()
            if free + used < cls.poolLimit:
                cls.pool.add(cls())
                return cls.pool.checkout()
            return
            return

    @classmethod
    def cleanup(cls):
        if cls.pool:
            cls.pool.cleanup(cls.destroy)
            cls.pool = None
        return

    def __init__(self):
        NodePath.__init__(self, self.__class__.__name__)
        self.accept('clientLogout', self.__class__.cleanup)

    def destroy(self, item=None):
        if item:
            self.pool.remove(item)
        self.ignore('clientLogout')
        self.removeNode()