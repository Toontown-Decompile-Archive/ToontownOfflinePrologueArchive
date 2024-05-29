# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.reborn.DistributedPrologue4EventAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from direct.fsm.FSM import FSM
from otp.ai.MagicWordGlobal import *
from toontown.toonbase import ToontownGlobals
import random
from otp.distributed.OtpDoGlobals import *
from direct.task import Task

class DistributedPrologue4EventAI(DistributedObjectAI, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPrologue4EventAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        FSM.__init__(self, 'Prologue4EventFSM')
        self.air = air
        self.stateTime = globalClockDelta.getRealNetworkTime()
        self.toons = []
        self.suits = []

    def enterOff(self):
        self.requestDelete()

    def enterIdle(self):
        pass

    def enterEvent(self):
        event = simbase.air.doFind('Prologue4Event')
        if event is None:
            event = DistributedPrologue4EventAI(simbase.air)
            event.generateWithRequired(21834)
        taskMgr.doMethodLater(400, self.b_setState, self.uniqueName('EventTwo'), extraArgs=['EventTwo'])
        self.showAnnounceInterval = Sequence(Wait(64), Func(self.sendGlobalUpdate, 'TOON HQ: The Toon Council Presidential Elections will be starting any second!'), Wait(5), Func(self.sendGlobalUpdate, 'TOON HQ: Please silence your Shtickerbooks and keep any Oinks, Squeaks, and Owooos to a low rustle.'))
        self.showAnnounceInterval.start()
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

    def sendGlobalUpdate(self, text):
        for doId in simbase.air.doId2do:
            if str(doId)[:2] == '10':
                do = simbase.air.doId2do.get(doId)
                do.d_setSystemMessage(0, text)

    def clearPrologueFlag(self):
        if hasattr(self.air, 'inPrologue'):
            self.air.inPrologue = False
            del self.air.inPrologue