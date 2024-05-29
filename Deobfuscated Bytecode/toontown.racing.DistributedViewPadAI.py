# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.racing.DistributedViewPadAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from toontown.racing.DistributedKartPadAI import DistributedKartPadAI
from direct.distributed.ClockDelta import *

class DistributedViewPadAI(DistributedKartPadAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedViewPadAI')

    def __init__(self, air):
        DistributedKartPadAI.__init__(self, air)
        self.timestamp = globalClockDelta.getRealNetworkTime()

    def setLastEntered(self, timestamp):
        self.timestamp = timestamp

    def d_setLastEntered(self, timestamp):
        self.sendUpdate('setLastEntered', [timestamp])

    def b_setLastEntered(self, timestamp):
        self.setLastEntered(timestamp)
        self.d_setLastEntered(timestamp)

    def getLastEntered(self):
        return self.timestamp

    def updateTimer(self):
        self.b_setLastEntered(globalClockDelta.getRealNetworkTime())