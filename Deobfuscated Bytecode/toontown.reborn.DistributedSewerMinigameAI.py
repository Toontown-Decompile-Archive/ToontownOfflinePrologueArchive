# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.reborn.DistributedSewerMinigameAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from direct.fsm.FSM import FSM
from otp.ai.MagicWordGlobal import *
from toontown.toon import InventoryBase
import random

class DistributedSewerMinigameAI(DistributedObjectAI, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSewerMinigameAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        FSM.__init__(self, 'SewerMinigameFSM')
        self.air = air
        self.stateTime = globalClockDelta.getRealNetworkTime()
        self.toons = []
        self.suits = []
        self.toonUpValues = [4, 8, 12, 16, 20]
        self.cameraDamage = [8, 12, 15]
        self.chopperDamage = [20, 25, 30]

    def enterOff(self):
        self.requestDelete()

    def enterIdle(self):
        pass

    def enterEvent(self):
        event = simbase.air.doFind('SewerMinigameEvent')
        if event is None:
            event = DistributedSewerMinigameAI(simbase.air)
            event.generateWithRequired(14100)
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

    def setOuch(self, penalty):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        self.notify.debug('setOuch %s' % penalty)
        if av and penalty > 0:
            av.takeDamage(penalty)
            if av.getHp() <= 0:
                av.inventory.zeroInv()
                av.d_setInventory(av.inventory.makeNetString())

    def zapToon(self, x, y, z, h, p, r, attackCode, timestamp):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return
        else:
            toon = simbase.air.doId2do.get(avId)
            if toon:
                self.d_showZapToon(avId, x, y, z, h, p, r, attackCode, timestamp)
                damage = 15
                if damage == None:
                    self.notify.warning('No damage listed for attack code %s' % attackCode)
                    damage = 5
                damage *= 1.0
                self.damageToon(toon, damage)
            return

    def d_showZapToon(self, avId, x, y, z, h, p, r, attackCode, timestamp):
        self.sendUpdate('showZapToon', [avId, 
         x, 
         y, 
         z, 
         h, 
         p, 
         r, 
         attackCode, 
         timestamp])

    def damageToon(self, toon, deduction):
        toon.takeDamage(deduction)
        if toon.getHp() <= 0:
            self.sendUpdate('toonDied', [toon.doId])
            empty = InventoryBase.InventoryBase(toon)
            toon.b_setInventory(empty.makeNetString())

    def requestGrab(self, entId):
        avId = self.air.getAvatarIdFromSender()
        self.notify.debug('requestGrab %s' % avId)
        if avId:
            self.d_setGrab(avId, entId)
        else:
            self.sendUpdate('setReject')

    def d_setGrab(self, avId, entId):
        self.notify.debug('d_setGrab %s' % avId)
        self.sendUpdate('setGrab', [avId, entId])
        av = self.air.doId2do.get(avId)
        if av:
            av.toonUp(random.choice(self.toonUpValues))

    def trapFire(self, isChopper):
        avId = self.air.getAvatarIdFromSender()
        toon = self.air.doId2do[avId]
        if toon:
            if isChopper == True:
                toon.takeDamage(random.choice(self.chopperDamage))
            else:
                toon.takeDamage(random.choice(self.cameraDamage))


@magicWord(category=CATEGORY_MODERATION, types=[str])
def sewerMg(state):
    event = simbase.air.doFind('SewerMinigame')
    if not config.GetBool('want-doomsday-reborn', False):
        return 'Interim Elections are disabled.'
    else:
        if event is None:
            event = DistributedSewerMinigameAI(simbase.air)
            event.generateWithRequired(14100)
        if not hasattr(event, 'enter' + state):
            return 'Invalid state'
        event.b_setState(state)
        return 'Sewer minigame now in %r state' % state