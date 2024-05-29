# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.TwoDWalk
# Compiled at: 2014-04-30 09:53:54
from OrthoWalk import *

class TwoDWalk(OrthoWalk):
    notify = DirectNotifyGlobal.directNotify.newCategory('TwoDWalk')
    BROADCAST_POS_TASK = 'TwoDWalkBroadcastPos'

    def doBroadcast(self, task):
        dt = globalClock.getDt()
        self.timeSinceLastPosBroadcast += dt
        if self.timeSinceLastPosBroadcast >= self.broadcastPeriod:
            self.timeSinceLastPosBroadcast = 0
            self.lt.cnode.broadcastPosHprFull()
        return Task.cont