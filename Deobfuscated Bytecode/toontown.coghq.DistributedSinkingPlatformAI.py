# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.DistributedSinkingPlatformAI
# Compiled at: 2014-04-30 09:53:54
from otp.ai.AIBase import *
from direct.directnotify import DirectNotifyGlobal
from otp.level import DistributedEntityAI
import SinkingPlatformGlobals

class DistributedSinkingPlatformAI(DistributedEntityAI.DistributedEntityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSinkingPlatformAI')

    def __init__(self, levelDoId, entId):
        DistributedEntityAI.DistributedEntityAI.__init__(self, levelDoId, entId)
        self.numStanding = 0

    def setOnOff(self, on, timestamp):
        avId = self.air.getAvatarIdFromSender()
        self.notify.debug('setOnOff %s' % on)
        if on:
            self.numStanding += 1
        else:
            self.numStanding -= 1
        self.notify.debug('numStanding = %s' % self.numStanding)
        if self.numStanding > 0:
            self.sendUpdate('setSinkMode', [avId, SinkingPlatformGlobals.SINKING, timestamp])
        else:
            self.sendUpdate('setSinkMode', [avId, SinkingPlatformGlobals.RISING, timestamp])