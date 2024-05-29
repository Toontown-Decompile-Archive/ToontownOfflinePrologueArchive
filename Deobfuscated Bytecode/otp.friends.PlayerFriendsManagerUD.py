# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.friends.PlayerFriendsManagerUD
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class PlayerFriendsManagerUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('PlayerFriendsManagerUD')

    def requestInvite(self, todo0, todo1, todo2):
        pass

    def invitationFrom(self, todo0, todo1):
        pass

    def retractInvite(self, todo0):
        pass

    def invitationResponse(self, todo0, todo1, todo2):
        pass

    def requestDecline(self, todo0, todo1):
        pass

    def requestDeclineWithReason(self, todo0, todo1, todo2):
        pass

    def requestRemove(self, todo0, todo1):
        pass

    def secretResponse(self, todo0):
        pass

    def rejectSecret(self, todo0):
        pass

    def rejectUseSecret(self, todo0):
        pass

    def updatePlayerFriend(self, todo0, todo1, todo2):
        pass

    def removePlayerFriend(self, todo0):
        pass