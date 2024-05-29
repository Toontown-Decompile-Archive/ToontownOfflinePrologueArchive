# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.town.ODGStreet
# Compiled at: 2014-04-30 09:53:54
import Street
from direct.interval.IntervalGlobal import *
from direct.interval.LerpInterval import LerpFunctionInterval
from toontown.toonbase.ToontownGlobals import *
from pandac.PandaModules import *

class ODGStreet(Street.Street):

    def __init__(self, loader, parentFSM, doneEvent):
        Street.Street.__init__(self, loader, parentFSM, doneEvent)
        self.laffMeter = base.localAvatar.laffMeter
        self.book = base.localAvatar.book.bookOpenButton
        self.book2 = base.localAvatar.book.bookCloseButton

    def load(self):
        Street.Street.load(self)
        pro3EvSeq = Sequence(Wait(3), Func(NodePath(self.book).hide), Func(NodePath(self.laffMeter).hide), Func(base.localAvatar.disableSleeping), Func(base.localAvatar.obscureFriendsListButton, 1), Func(base.localAvatar.hideClarabelleGui), Func(base.localAvatar.chatMgr.obscure, 1, 1), Func(localAvatar.sendUpdate, 'startPro3Ev', []))
        pro3EvSeq.start()

    def unload(self):
        Street.Street.unload(self)