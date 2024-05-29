# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.movement.Impulse
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.showbase import DirectObject

class Impulse(DirectObject.DirectObject):

    def __init__(self):
        self.mover = None
        self.nodePath = None
        return

    def destroy(self):
        pass

    def _process(self, dt):
        pass

    def _setMover(self, mover):
        self.mover = mover
        self.nodePath = self.mover.getNodePath()
        self.VecType = self.mover.VecType

    def _clearMover(self, mover):
        if self.mover == mover:
            self.mover = None
            self.nodePath = None
        return

    def isCpp(self):
        return 0