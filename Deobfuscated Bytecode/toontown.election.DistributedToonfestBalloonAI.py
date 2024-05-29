# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.election.DistributedToonfestBalloonAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.ClockDelta import *
from direct.fsm.FSM import FSM
from direct.task import Task
import ToonfestBalloonGlobals
from random import randint
from otp.ai.MagicWordGlobal import *

class DistributedToonfestBalloonAI(DistributedObjectAI, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedToonfestBalloonAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        FSM.__init__(self, 'ToonfestBalloonFSM')
        self.avId = 0
        self.stateTime = globalClockDelta.getRealNetworkTime()
        self.flightPathIndex = 0

    def b_setState(self, state, avId=0):
        if avId != self.avId:
            self.avId = avId
        self.setState(state)
        self.d_setState(state)

    def setState(self, state):
        self.demand(state)

    def d_setState(self, state):
        self.stateTime = globalClockDelta.getRealNetworkTime()
        self.sendUpdate('setState', [state, self.stateTime, self.avId])

    def getState(self):
        return (
         self.state, self.stateTime, self.avId)

    def enterOff(self):
        self.requestDelete()

    def enterWaiting(self):
        pass

    def enterNotReady(self):
        pass

    def requestEnter(self):
        avId = self.air.getAvatarIdFromSender()
        if self.state != 'Waiting':
            self.notify.warning('Received unexpected requestEnter from avId %d!' % avId)
            return
        if self.avId == avId:
            return
        self.b_setState('Occupied', avId)

    def enterOccupied(self):
        self.b_setFlightPath(randint(0, ToonfestBalloonGlobals.NumBalloonPaths - 1))
        taskMgr.doMethodLater(3.5, self.b_setState, 'balloon-startride-task', extraArgs=['StartRide', self.avId])

    def b_setFlightPath(self, flightPathIndex):
        self.setFlightPath(flightPathIndex)
        self.d_setFlightPath(flightPathIndex)

    def setFlightPath(self, flightPathIndex):
        self.flightPathIndex = flightPathIndex

    def d_setFlightPath(self, flightPathIndex):
        self.sendUpdate('setFlightPath', [flightPathIndex])

    def getFlightPath(self):
        return self.flightPathIndex

    def enterStartRide(self):
        taskMgr.doMethodLater(85, self.b_setState, 'balloon-riding-task', extraArgs=['RideOver', self.avId])

    def enterRideOver(self):
        taskMgr.doMethodLater(30, self.b_setState, 'balloon-cleaningup-task', extraArgs=['Waiting'])


@magicWord(category=CATEGORY_MODERATION, types=[str])
def balloon(state):
    event = simbase.air.doFind('ToonfestBalloon')
    if event is None:
        return 'There is no ToonFest Balloon here!'
    else:
        if not hasattr(event, 'enter' + state):
            return 'Invalid state'
        event.b_setState(state)
        return 'Balloon now in %r state' % state