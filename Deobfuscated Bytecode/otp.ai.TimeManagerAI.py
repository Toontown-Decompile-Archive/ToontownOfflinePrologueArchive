# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.ai.TimeManagerAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.ClockDelta import globalClockDelta
import time

class TimeManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('TimeManagerAI')

    def requestServerTime(self, context):
        self.sendUpdateToAvatarId(self.air.getAvatarIdFromSender(), 'serverTime', [context,
         globalClockDelta.getRealNetworkTime(bits=32),
         int(time.time())])

    def setDisconnectReason(self, reason):
        avId = self.air.getAvatarIdFromSender()
        self.air.writeServerEvent('disconnect-reason', avId=avId, reason=reason)

    def setExceptionInfo(self, exception):
        avId = self.air.getAvatarIdFromSender()
        self.air.writeServerEvent('client-exception', avId=avId, exception=exception)

    def setSignature(self, todo0, todo1, todo2):
        pass

    def setFrameRate(self, todo0, todo1, todo2, todo3, todo4, todo5, todo6, todo7, todo8, todo9, todo10, todo11, todo12, todo13, todo14, todo15, todo16, todo17):
        pass

    def setCpuInfo(self, todo0, todo1):
        pass

    def checkForGarbageLeaks(self, todo0):
        pass

    def setNumAIGarbageLeaks(self, todo0):
        pass

    def setClientGarbageLeak(self, todo0, todo1):
        pass

    def checkAvOnDistrict(self, todo0, todo1):
        pass