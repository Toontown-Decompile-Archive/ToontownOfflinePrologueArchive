# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.classicchars.DistributedDale
# Compiled at: 2014-04-30 09:53:54
from direct.showbase.ShowBaseGlobal import *
import DistributedCCharBase
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.fsm import State
import CharStateDatas
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer

class DistributedDale(DistributedCCharBase.DistributedCCharBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedDale')
    deferFor = 1

    def __init__(self, cr):
        try:
            self.DistributedDale_initialized
        except:
            self.DistributedDale_initialized = 1
            DistributedCCharBase.DistributedCCharBase.__init__(self, cr, TTLocalizer.Dale, 'da')
            self.fsm = ClassicFSM.ClassicFSM(self.getName(), [State.State('Off', self.enterOff, self.exitOff, ['Neutral']), State.State('Neutral', self.enterNeutral, self.exitNeutral, ['Walk']), State.State('Walk', self.enterWalk, self.exitWalk, ['Neutral'])], 'Off', 'Off')
            self.fsm.enterInitialState()
            self.handleHolidays()

    def disable(self):
        self.fsm.requestFinalState()
        DistributedCCharBase.DistributedCCharBase.disable(self)
        del self.neutralDoneEvent
        del self.neutral
        del self.walkDoneEvent
        if self.walk:
            self.walk.exit()
        del self.walk
        self.fsm.requestFinalState()

    def delete(self):
        try:
            self.DistributedDale_deleted
        except:
            del self.fsm
            self.DistributedDale_deleted = 1
            DistributedCCharBase.DistributedCCharBase.delete(self)

    def generate(self):
        DistributedCCharBase.DistributedCCharBase.generate(self)
        self.setX(self.getX() + ToontownGlobals.DaleOrbitDistance)
        name = self.getName()
        self.neutralDoneEvent = self.taskName(name + '-neutral-done')
        self.neutral = CharStateDatas.CharNeutralState(self.neutralDoneEvent, self)
        self.walkDoneEvent = self.taskName(name + '-walk-done')
        self.fsm.request('Neutral')

    def announceGenerate(self):
        DistributedCCharBase.DistributedCCharBase.announceGenerate(self)
        self.walk = CharStateDatas.CharFollowChipState(self.walkDoneEvent, self, self.chipId)

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterNeutral(self):
        self.neutral.enter()
        self.acceptOnce(self.neutralDoneEvent, self.__decideNextState)

    def exitNeutral(self):
        self.ignore(self.neutralDoneEvent)
        self.neutral.exit()

    def enterWalk(self):
        self.walk.enter()
        self.acceptOnce(self.walkDoneEvent, self.__decideNextState)

    def exitWalk(self):
        self.ignore(self.walkDoneEvent)
        self.walk.exit()

    def __decideNextState(self, doneStatus):
        self.fsm.request('Neutral')

    def setWalk(self, srcNode, destNode, timestamp, offsetX=0, offsetY=0):
        if destNode and not destNode == srcNode:
            self.walk.setWalk(srcNode, destNode, timestamp, offsetX, offsetY)
            self.fsm.request('Walk')

    def walkSpeed(self):
        return ToontownGlobals.DaleSpeed

    def setFollowChip(self, srcNode, destNode, timestamp, offsetX, offsetY):
        if destNode and not destNode == srcNode:
            self.walk.setWalk(srcNode, destNode, timestamp, offsetX, offsetY)
            self.fsm.request('Walk')

    def setChipId(self, chipId):
        self.chipId = chipId