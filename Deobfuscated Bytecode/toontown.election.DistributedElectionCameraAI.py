# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.election.DistributedElectionCameraAI
# Compiled at: 2014-04-30 09:53:54
from direct.distributed.DistributedNodeAI import DistributedNodeAI
from direct.distributed.ClockDelta import *
from direct.task import Task
import math

class DistributedElectionCameraAI(DistributedNodeAI):

    def __init__(self, air):
        DistributedNodeAI.__init__(self, air)

    def getState(self):
        return self.state

    def setState(self, state, ts, x, y, z, h, p, target):
        self.state = [
         state, ts, x, y, z, h, p, target]

    def d_setState(self, state, ts, x, y, z, h, p, target):
        self.sendUpdate('setState', [state, ts, x, y, z, h, p, target])

    def b_setState(self, state, ts, x, y, z, h, p, target):
        self.setState(state, ts, x, y, z, h, p, target)
        self.d_setState(state, ts, x, y, z, h, p, target)

    def _moveTo(self, x, y, z, h, p):
        dist = self._dist(x, y, z)
        time = dist / 10.0 + 1.5
        self.b_setState('Move', globalClockDelta.getRealNetworkTime(), x, y, z, h, p, 0)
        taskMgr.remove('finish%d' % self.doId)
        taskMgr.doMethodLater(time, self.__finishMove, 'finish%d' % self.doId, extraArgs=[x, y, z])

    def _dist(self, x, y, z):
        return math.sqrt((self.getX() - x) ** 2 + (self.getY() - y) ** 2 + (self.getZ() - z) ** 2)

    def _followBehind(self, object):
        x, y, z = object.getPos()
        dist = self._dist(x, y - 10.0, z + 7.0)
        time = dist / 10.0 + 1.5
        self.b_setState('Follow', globalClockDelta.getRealNetworkTime(), 0, -15, 7, -90, -15, object.doId)
        taskMgr.remove('finish%d' % self.doId)
        taskMgr.doMethodLater(time, self.__finishMove, 'finish%d' % self.doId, extraArgs=[0, -15, 7])

    def _watch(self, object):
        x, y, z = object.getPos()
        dist = self._dist(x, y + 10.0, z + 7.0)
        time = dist / 10.0 + 1.5
        self.b_setState('Follow', globalClockDelta.getRealNetworkTime(), 0, 15, 7, 90, -15, object.doId)
        taskMgr.remove('finish%d' % self.doId)
        taskMgr.doMethodLater(time, self.__finishMove, 'finish%d' % self.doId, extraArgs=[0, 15, 7])

    def __finishMove(self, x, y, z):
        self.setPos(x, y, z)
        self.d_setXY(x, y)
        self.d_setZ(z)