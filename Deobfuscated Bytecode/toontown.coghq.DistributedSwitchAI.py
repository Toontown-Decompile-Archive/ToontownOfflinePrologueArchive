# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.DistributedSwitchAI
# Compiled at: 2014-04-30 09:53:54
from direct.distributed.ClockDelta import *
from direct.directnotify import DirectNotifyGlobal
import DistributedSwitchBase
from direct.task import Task
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from otp.level import DistributedEntityAI

class DistributedSwitchAI(DistributedSwitchBase.DistributedSwitchBase, DistributedEntityAI.DistributedEntityAI):

    def __init__(self, level, entId, zoneId=None):
        DistributedEntityAI.DistributedEntityAI.__init__(self, level, entId)
        self.fsm = ClassicFSM.ClassicFSM('DistributedSwitch', [State.State('off', self.enterOff, self.exitOff, ['playing']), State.State('attract', self.enterAttract, self.exitAttract, ['playing']), State.State('playing', self.enterPlaying, self.exitPlaying, ['attract'])], 'off', 'off')
        self.fsm.enterInitialState()
        self.avatarId = 0
        self.doLaterTask = None
        if zoneId is not None:
            self.generateWithRequired(zoneId)
        return

    def setup(self):
        pass

    def takedown(self):
        pass

    setScale = DistributedSwitchBase.stubFunction

    def delete(self):
        if self.doLaterTask:
            self.doLaterTask.remove()
            self.doLaterTask = None
        del self.fsm
        DistributedEntityAI.DistributedEntityAI.delete(self)
        return

    def getAvatarInteract(self):
        return self.avatarId

    def getState(self):
        r = [
         self.fsm.getCurrentState().getName(), globalClockDelta.getRealNetworkTime()]
        return r

    def sendState(self):
        self.sendUpdate('setState', self.getState())

    def setIsOn(self, isOn):
        if self.isOn != isOn:
            self.isOn = isOn
            stateName = self.fsm.getCurrentState().getName()
            if isOn:
                if stateName != 'playing':
                    self.fsm.request('playing')
            elif stateName != 'attract':
                self.fsm.request('attract')
            messenger.send(self.getOutputEventName(), [isOn])

    def getIsOn(self):
        return self.isOn

    def getName(self):
        return 'switch-%s' % (self.entId,)

    def switchOffTask(self, task):
        self.setIsOn(0)
        self.fsm.request('attract')
        return Task.done

    def requestInteract(self):
        avatarId = self.air.getAvatarIdFromSender()
        stateName = self.fsm.getCurrentState().getName()
        if stateName != 'playing':
            self.sendUpdate('setAvatarInteract', [avatarId])
            self.avatarId = avatarId
            self.fsm.request('playing')
        else:
            self.sendUpdateToAvatarId(avatarId, 'rejectInteract', [])

    def requestExit(self):
        avatarId = self.air.getAvatarIdFromSender()
        if self.avatarId and avatarId == self.avatarId:
            stateName = self.fsm.getCurrentState().getName()
            if stateName == 'playing':
                self.sendUpdate('avatarExit', [avatarId])
                self.avatarId = None
                if self.isOn and self.secondsOn != -1.0 and self.secondsOn >= 0.0:
                    self.doLaterTask = taskMgr.doMethodLater(self.secondsOn, self.switchOffTask, self.uniqueName('switch-timer'))
        return

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterAttract(self):
        self.sendState()

    def exitAttract(self):
        pass

    def enterPlaying(self):
        self.sendState()
        self.setIsOn(1)

    def exitPlaying(self):
        if self.doLaterTask:
            self.doLaterTask.remove()
            self.doLaterTask = None
        return

    if __dev__:

        def attribChanged(self, attrib, value):
            self.takedown()
            self.setup()