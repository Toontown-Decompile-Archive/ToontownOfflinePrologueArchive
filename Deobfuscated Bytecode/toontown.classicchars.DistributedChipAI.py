# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.classicchars.DistributedChipAI
# Compiled at: 2014-04-30 09:53:54
from otp.ai.AIBaseGlobal import *
import DistributedCCharBaseAI
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.task import Task
import random
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
import CharStateDatasAI

class DistributedChipAI(DistributedCCharBaseAI.DistributedCCharBaseAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedChipAI')

    def __init__(self, air):
        DistributedCCharBaseAI.DistributedCCharBaseAI.__init__(self, air, TTLocalizer.Chip)
        self.fsm = ClassicFSM.ClassicFSM('DistributedChipAI', [
         State.State('Off', self.enterOff, self.exitOff, [
          'Lonely']),
         State.State('Lonely', self.enterLonely, self.exitLonely, [
          'Chatty',
          'Walk']),
         State.State('Chatty', self.enterChatty, self.exitChatty, [
          'Lonely',
          'Walk']),
         State.State('Walk', self.enterWalk, self.exitWalk, [
          'Lonely',
          'Chatty'])], 'Off', 'Off')
        self.fsm.enterInitialState()
        self.dale = None
        self.handleHolidays()
        return

    def delete(self):
        self.fsm.requestFinalState()
        DistributedCCharBaseAI.DistributedCCharBaseAI.delete(self)
        self.lonelyDoneEvent = None
        self.lonely = None
        self.chattyDoneEvent = None
        self.chatty = None
        self.walkDoneEvent = None
        self.walk = None
        return

    def generate(self):
        DistributedCCharBaseAI.DistributedCCharBaseAI.generate(self)
        name = self.getName()
        self.lonelyDoneEvent = self.taskName(name + '-lonely-done')
        self.lonely = CharStateDatasAI.CharLonelyStateAI(self.lonelyDoneEvent, self)
        self.chattyDoneEvent = self.taskName(name + '-chatty-done')
        self.chatty = CharStateDatasAI.ChipChattyStateAI(self.chattyDoneEvent, self)
        self.walkDoneEvent = self.taskName(name + '-walk-done')
        self.walk = CharStateDatasAI.CharWalkStateAI(self.walkDoneEvent, self)

    def walkSpeed(self):
        return ToontownGlobals.ChipSpeed

    def start(self):
        self.fsm.request('Lonely')

    def _DistributedChipAI__decideNextState(self, doneStatus):
        if doneStatus['state'] == 'lonely' and doneStatus['status'] == 'done':
            self.fsm.request('Walk')
        elif doneStatus['state'] == 'chatty' and doneStatus['status'] == 'done':
            self.fsm.request('Walk')
        elif doneStatus['state'] == 'walk' and doneStatus['status'] == 'done':
            if len(self.nearbyAvatars) > 0:
                self.fsm.request('Chatty')
            else:
                self.fsm.request('Lonely')

    def enterOff(self):
        pass

    def exitOff(self):
        DistributedCCharBaseAI.DistributedCCharBaseAI.exitOff(self)

    def enterLonely(self):
        self.lonely.enter()
        self.acceptOnce(self.lonelyDoneEvent, self.__decideNextState)
        if self.dale:
            self.dale.chipEnteringState(self.fsm.getCurrentState().getName())

    def exitLonely(self):
        self.ignore(self.lonelyDoneEvent)
        self.lonely.exit()
        if self.dale:
            self.dale.chipLeavingState(self.fsm.getCurrentState().getName())

    def _DistributedChipAI__goForAWalk(self, task):
        self.notify.debug('going for a walk')
        self.fsm.request('Walk')
        return Task.done

    def enterChatty(self):
        self.chatty.enter()
        self.acceptOnce(self.chattyDoneEvent, self.__decideNextState)
        if self.dale:
            self.dale.chipEnteringState(self.fsm.getCurrentState().getName())

    def exitChatty(self):
        self.ignore(self.chattyDoneEvent)
        self.chatty.exit()
        if self.dale:
            self.dale.chipLeavingState(self.fsm.getCurrentState().getName())

    def enterWalk(self):
        self.notify.debug('going for a walk')
        self.walk.enter()
        self.acceptOnce(self.walkDoneEvent, self.__decideNextState)
        if self.dale:
            self.dale.chipEnteringState(self.fsm.getCurrentState().getName())

    def exitWalk(self):
        self.ignore(self.walkDoneEvent)
        self.walk.exit()
        if self.dale:
            self.dale.chipLeavingState(self.fsm.getCurrentState().getName())

    def avatarEnterNextState(self):
        if len(self.nearbyAvatars) == 1:
            if self.fsm.getCurrentState().getName() != 'Walk':
                self.fsm.request('Chatty')
            else:
                self.notify.debug('avatarEnterNextState: in walk state')
        else:
            self.notify.debug('avatarEnterNextState: num avatars: ' + str(len(self.nearbyAvatars)))

    def avatarExitNextState(self):
        if len(self.nearbyAvatars) == 0:
            if self.fsm.getCurrentState().getName() != 'Walk':
                self.fsm.request('Lonely')

    def setDaleId(self, daleId):
        self.daleId = daleId
        self.dale = self.air.doId2do.get(daleId)
        self.chatty.setDaleId(self.daleId)