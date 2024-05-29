# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.uberdog.OtpAvatarManagerAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class OtpAvatarManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('OtpAvatarManagerAI')

    def online(self):
        pass

    def requestAvatarList(self, todo0):
        pass

    def rejectAvatarList(self, todo0):
        pass

    def avatarListResponse(self, todo0):
        pass

    def requestAvatarSlot(self, todo0, todo1, todo2):
        pass

    def rejectAvatarSlot(self, todo0, todo1, todo2):
        pass

    def avatarSlotResponse(self, todo0, todo1):
        pass

    def requestPlayAvatar(self, todo0, todo1, todo2):
        pass

    def rejectPlayAvatar(self, todo0, todo1):
        pass

    def playAvatarResponse(self, todo0, todo1, todo2, todo3):
        pass

    def rejectCreateAvatar(self, todo0):
        pass

    def createAvatarResponse(self, todo0, todo1, todo2, todo3):
        pass

    def requestRemoveAvatar(self, todo0, todo1, todo2, todo3):
        pass

    def rejectRemoveAvatar(self, todo0):
        pass

    def removeAvatarResponse(self, todo0, todo1):
        pass

    def requestShareAvatar(self, todo0, todo1, todo2, todo3):
        pass

    def rejectShareAvatar(self, todo0):
        pass

    def shareAvatarResponse(self, todo0, todo1, todo2):
        pass