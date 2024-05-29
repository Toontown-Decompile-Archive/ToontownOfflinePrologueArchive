# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.ai.DistributedOldmanTipMgr
# Compiled at: 2014-04-30 09:53:54
import random
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from direct.interval.IntervalGlobal import *
from otp.speedchat import SpeedChatGlobals
from toontown.toonbase import TTLocalizer, ToontownGlobals
from toontown.reborn.InterimElectionGlobals import *

class DistributedOldmanTipMgr(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedOldmanTipMgr')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        DistributedOldmanTipMgr.notify.debug('announceGenerate')
        self.accept(SpeedChatGlobals.SCStaticTextMsgEvent, self.phraseSaid)

    def phraseSaid(self, phraseId):
        helpPhrase = 1400
        if phraseId == helpPhrase and (config.GetBool('want-doomsday-reborn', False) or config.GetBool('want-interim-election-buildup', False)):
            self.sayPhrase()

    def delete(self):
        self.ignore(SpeedChatGlobals.SCStaticTextMsgEvent)
        DistributedObject.DistributedObject.delete(self)

    def sayPhrase(self):
        DistributedOldmanTipMgr.notify.debug('addResitanceEffect')
        av = base.localAvatar
        msgTrack = Sequence(Func(av.setSystemMessage, 0, oldmanTipsIntro), Wait(2), Func(av.setSystemMessage, 0, "Lil' Oldman: " + random.choice(toonTips)))
        msgTrack.start()