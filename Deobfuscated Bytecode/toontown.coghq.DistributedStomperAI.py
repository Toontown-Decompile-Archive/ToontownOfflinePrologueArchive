# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.DistributedStomperAI
# Compiled at: 2014-04-30 09:53:54
from otp.ai.AIBase import *
from direct.interval.IntervalGlobal import *
from direct.directnotify import DirectNotifyGlobal
import DistributedCrusherEntityAI, StomperGlobals
from direct.distributed import ClockDelta

class DistributedStomperAI(DistributedCrusherEntityAI.DistributedCrusherEntityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedStomperAI')

    def __init__(self, level, entId, pairId=-1):
        DistributedCrusherEntityAI.DistributedCrusherEntityAI.__init__(self, level, entId)
        self.pairId = pairId

    def generate(self):
        DistributedCrusherEntityAI.DistributedCrusherEntityAI.generate(self)
        if self.switchId != 0:
            self.accept(self.getOutputEventName(self.switchId), self.reactToSwitch)
        self.d_startStomper()

    def delete(self):
        del self.pos
        self.ignoreAll()
        DistributedCrusherEntityAI.DistributedCrusherEntityAI.delete(self)

    def d_startStomper(self):
        self.sendUpdate('setMovie', [StomperGlobals.STOMPER_START, ClockDelta.globalClockDelta.getRealNetworkTime(), []])

    def reactToSwitch(self, on):
        if on:
            crushedList = []
            if self.crushCell:
                self.crushCell.updateCrushables()
                for id in self.crushCell.occupantIds:
                    if id in self.crushCell.crushables:
                        crushedList.append(id)

                self.sendCrushMsg()
            self.sendUpdate('setMovie', [StomperGlobals.STOMPER_STOMP, ClockDelta.globalClockDelta.getRealNetworkTime(), crushedList])
        else:
            self.sendUpdate('setMovie', [StomperGlobals.STOMPER_RISE, ClockDelta.globalClockDelta.getRealNetworkTime(), []])