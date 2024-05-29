# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.movement.Mover
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from libotp import CMover
from direct.directnotify import DirectNotifyGlobal
from otp.movement.PyVec3 import PyVec3
from direct.showbase import PythonUtil
import __builtin__

class Mover:
    notify = DirectNotifyGlobal.directNotify.newCategory('Mover')
    SerialNum = 0
    Profile = 0
    Pstats = 1
    PSCCpp = 'App:Show code:moveObjects:MoverC++'
    PSCPy = 'App:Show code:moveObjects:MoverPy'
    PSCInt = 'App:Show code:moveObjects:MoverIntegrate'

    def __init__(self, objNodePath, fwdSpeed=1, rotSpeed=1):
        CMover.__init__(self, objNodePath, fwdSpeed, rotSpeed)
        self.serialNum = Mover.SerialNum
        Mover.SerialNum += 1
        self.VecType = Vec3
        self.impulses = {}
        if Mover.Pstats:
            self.pscCpp = PStatCollector(Mover.PSCCpp)
            self.pscPy = PStatCollector(Mover.PSCPy)
            self.pscInt = PStatCollector(Mover.PSCInt)

    def destroy(self):
        for name, impulse in self.impulses.items():
            Mover.notify.debug('removing impulse: %s' % name)
            self.removeImpulse(name)

    def addImpulse(self, name, impulse):
        if impulse.isCpp():
            CMover.addCImpulse(self, name, impulse)
        else:
            self.impulses[name] = impulse
            impulse._setMover(self)

    def removeImpulse(self, name):
        if name not in self.impulses:
            if not CMover.removeCImpulse(self, name):
                Mover.notify.warning("Mover.removeImpulse: unknown impulse '%s'" % name)
            return
        self.impulses[name]._clearMover(self)
        del self.impulses[name]

    def getCollisionEventName(self):
        return 'moverCollision-%s' % self.serialNum

    def move(self, dt=-1, profile=0):
        if Mover.Profile and not profile:

            def func(doMove=self.move):
                for i in xrange(10000):
                    doMove(dt, profile=1)

            __builtin__.func = func
            PythonUtil.startProfile(cmd='func()', filename='profile', sorts=['cumulative'], callInfo=0)
            del __builtin__.func
            return
        if Mover.Pstats:
            self.pscCpp.start()
        CMover.processCImpulses(self, dt)
        if Mover.Pstats:
            self.pscCpp.stop()
            self.pscPy.start()
        for impulse in self.impulses.values():
            impulse._process(self.getDt())

        if Mover.Pstats:
            self.pscPy.stop()
            self.pscInt.start()
        CMover.integrate(self)
        if Mover.Pstats:
            self.pscInt.stop()