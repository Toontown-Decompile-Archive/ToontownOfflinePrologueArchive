# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.uberdog.SpeedchatRelay
# Compiled at: 2014-04-30 09:53:54
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from direct.directnotify.DirectNotifyGlobal import directNotify
from otp.otpbase import OTPGlobals
from otp.uberdog import SpeedchatRelayGlobals

class SpeedchatRelay(DistributedObjectGlobal):

    def __init__(self, cr):
        DistributedObjectGlobal.__init__(self, cr)

    def sendSpeedchat(self, receiverId, messageIndex):
        self.sendSpeedchatToRelay(receiverId, SpeedchatRelayGlobals.NORMAL, [messageIndex])

    def sendSpeedchatCustom(self, receiverId, messageIndex):
        self.sendSpeedchatToRelay(receiverId, SpeedchatRelayGlobals.CUSTOM, [messageIndex])

    def sendSpeedchatEmote(self, receiverId, messageIndex):
        self.sendSpeedchatToRelay(receiverId, SpeedchatRelayGlobals.EMOTE, [messageIndex])

    def sendSpeedchatToRelay(self, receiverId, speedchatType, parameters):
        self.sendUpdate('forwardSpeedchat', [receiverId,
         speedchatType,
         parameters,
         base.cr.accountDetailRecord.playerAccountId,
         base.cr.accountDetailRecord.playerName + ' RHFM',
         0])