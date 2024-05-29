# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.OrthoWalk
# Compiled at: 2014-04-30 09:53:54
from toontown.toonbase.ToonBaseGlobal import *
from direct.task.Task import Task
from direct.interval.IntervalGlobal import *
from OrthoDrive import *
from direct.directnotify import DirectNotifyGlobal

class OrthoWalk:
    notify = DirectNotifyGlobal.directNotify.newCategory('OrthoWalk')
    BROADCAST_POS_TASK = 'OrthoWalkBroadcastPos'

    def __init__(self, orthoDrive, collisions=1, broadcast=1, broadcastPeriod=0.2):
        self.orthoDrive = orthoDrive
        self.collisions = collisions
        self.broadcast = broadcast
        self.broadcastPeriod = broadcastPeriod
        self.priority = self.orthoDrive.priority + 1
        self.lt = base.localAvatar

    def destroy(self):
        self.orthoDrive.destroy()
        del self.orthoDrive

    def start(self):
        self.notify.debug('OrthoWalk start')
        if self.collisions:
            self.initCollisions()
        if self.broadcast:
            self.initBroadcast()
        self.orthoDrive.start()

    def stop(self):
        self.notify.debug('OrthoWalk stop')
        self.shutdownCollisions()
        self.shutdownBroadcast()
        self.orthoDrive.stop()

    def initCollisions(self):
        self.notify.debug('OrthoWalk initCollisions')
        lt = base.localAvatar
        lt.collisionsOn()
        self.__collisionsOn = 1

    def shutdownCollisions(self):
        if not hasattr(self, '_OrthoWalk__collisionsOn'):
            return
        del self.__collisionsOn
        self.notify.debug('OrthoWalk shutdownCollisions')
        lt = base.localAvatar
        lt.collisionsOff()

    def initBroadcast(self):
        self.notify.debug('OrthoWalk initBroadcast')
        self.timeSinceLastPosBroadcast = 0.0
        self.lastPosBroadcast = self.lt.getPos()
        self.lastHprBroadcast = self.lt.getHpr()
        self.storeStop = 0
        lt = self.lt
        lt.d_clearSmoothing()
        lt.sendCurrentPosition()
        taskMgr.remove(self.BROADCAST_POS_TASK)
        taskMgr.add(self.doBroadcast, self.BROADCAST_POS_TASK, priority=self.priority)

    def shutdownBroadcast(self):
        self.notify.debug('OrthoWalk shutdownBroadcast')
        taskMgr.remove(self.BROADCAST_POS_TASK)

    def doBroadcast(self, task):
        dt = globalClock.getDt()
        self.timeSinceLastPosBroadcast += dt
        if self.timeSinceLastPosBroadcast >= self.broadcastPeriod:
            self.sendCurrentPosition()
        return Task.cont

    def sendCurrentPosition(self):
        self.timeSinceLastPosBroadcast -= self.broadcastPeriod
        self.lt.cnode.broadcastPosHprXyh()