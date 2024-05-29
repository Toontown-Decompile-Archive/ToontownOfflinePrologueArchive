# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.reborn.DistributedPrologue3Event
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from direct.distributed.DistributedObject import DistributedObject
from direct.fsm.FSM import FSM
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from toontown.toon import NPCToons
from otp.margins.WhisperPopup import *

class DistributedPrologue3Event(DistributedObject, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPrologue3Event')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        FSM.__init__(self, 'Prologue3EventFSM')
        self.cr.prologue3Event = self
        self.laffMeter = base.localAvatar.laffMeter
        self.book = base.localAvatar.book.bookOpenButton
        self.book2 = base.localAvatar.book.bookCloseButton

    def enterOff(self, offset):
        pass

    def exitOff(self):
        pass

    def __cleanupNPCs(self):
        pass

    def delete(self):
        self.demand('Off', 0.0)
        self.ignore('entercnode')
        self.__cleanupNPCs()
        DistributedObject.delete(self)

    def enterIdle(self, offset):
        pass

    def exitIdle(self):
        pass

    def enterEvent(self, offset):
        base.localAvatar.disableSleeping()
        base.localAvatar.invPage.ignoreOnscreenHooks()
        base.localAvatar.questPage.ignoreOnscreenHooks()
        self.eventInterval = Sequence(Wait(2), Func(NodePath(self.book).hide), Func(NodePath(self.laffMeter).hide), Func(base.localAvatar.obscureFriendsListButton, 1), Func(base.localAvatar.hideClarabelleGui), Func(base.localAvatar.invPage.ignoreOnscreenHooks), Func(base.localAvatar.questPage.ignoreOnscreenHooks))
        self.eventInterval.start()
        self.eventInterval.setT(offset)

    def exitEvent(self):
        self.eventInterval.finish()

    def enterEventTwo(self, offset):
        pass

    def exitEventTwo(self):
        pass

    def setState(self, state, timestamp):
        self.request(state, globalClockDelta.localElapsedTime(timestamp))