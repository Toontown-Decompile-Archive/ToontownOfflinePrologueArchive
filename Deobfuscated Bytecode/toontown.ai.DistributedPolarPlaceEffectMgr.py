# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.ai.DistributedPolarPlaceEffectMgr
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from direct.interval.IntervalGlobal import *
from otp.speedchat import SpeedChatGlobals
from toontown.toonbase import TTLocalizer

class DistributedPolarPlaceEffectMgr(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPolarPlaceEffectMgr')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        DistributedPolarPlaceEffectMgr.notify.debug('announceGenerate')
        self.accept(SpeedChatGlobals.SCStaticTextMsgEvent, self.phraseSaid)

    def phraseSaid(self, phraseId):
        helpPhrase = 103
        if phraseId == helpPhrase:
            self.addPolarPlaceEffect()

    def delete(self):
        self.ignore(SpeedChatGlobals.SCStaticTextMsgEvent)
        DistributedObject.DistributedObject.delete(self)

    def addPolarPlaceEffect(self):
        DistributedPolarPlaceEffectMgr.notify.debug('addResitanceEffect')
        av = base.localAvatar
        self.sendUpdate('addPolarPlaceEffect', [])
        msgTrack = Sequence(Func(av.setSystemMessage, 0, TTLocalizer.PolarPlaceEffect1), Wait(2), Func(av.setSystemMessage, 0, TTLocalizer.PolarPlaceEffect2), Wait(4), Func(av.setSystemMessage, 0, TTLocalizer.PolarPlaceEffect3))
        msgTrack.start()