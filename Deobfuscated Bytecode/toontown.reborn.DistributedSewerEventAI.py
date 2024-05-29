# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.reborn.DistributedSewerEventAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from direct.fsm.FSM import FSM
from otp.ai.MagicWordGlobal import *
from otp.distributed.OtpDoGlobals import *
from direct.task import Task

class DistributedSewerEventAI(DistributedObjectAI, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSewerEventAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        FSM.__init__(self, 'SewerFSM')
        self.air = air
        self.stateTime = globalClockDelta.getRealNetworkTime()
        self.toons = []
        self.suits = []

    def enterOff(self):
        self.requestDelete()

    def enterIdle(self):
        pass

    def enterEvent(self):
        event = simbase.air.doFind('SewerEvent')
        if event is None:
            event = DistributedSewerEventAI(simbase.air)
            event.generateWithRequired(14000)
        taskMgr.doMethodLater(82, self.b_setState, self.uniqueName('EventTwo'), extraArgs=['EventTwo'])
        return

    def enterEventTwo(self):
        pass

    def setState(self, state):
        self.demand(state)

    def d_setState(self, state):
        self.stateTime = globalClockDelta.getRealNetworkTime()
        self.sendUpdate('setState', [state, self.stateTime])

    def b_setState(self, state):
        self.setState(state)
        self.d_setState(state)

    def getState(self):
        return (
         self.state, self.stateTime)

    def applyReward(self):
        avId = self.air.getAvatarIdFromSender()
        toon = self.air.doId2do.get(avId)
        if toon:
            toon.doResistanceEffect(3, True)

    def applyReward2(self):
        avId = self.air.getAvatarIdFromSender()
        toon = self.air.doId2do.get(avId)
        if toon:
            toon.addPinkSlips(2)


@magicWord(category=CATEGORY_MODERATION, types=[str])
def sewerEv(state):
    event = simbase.air.doFind('SewerEvent')
    if not config.GetBool('want-doomsday-reborn', False):
        return 'Interim Elections are disabled.'
    else:
        if event is None:
            event = DistributedSewerEventAI(simbase.air)
            event.generateWithRequired(14000)
        if not hasattr(event, 'enter' + state):
            return 'Invalid state'
        event.b_setState(state)
        return 'Sewer event now in %r state' % state