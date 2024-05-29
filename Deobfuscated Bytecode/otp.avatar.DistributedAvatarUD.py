# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.avatar.DistributedAvatarUD
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class DistributedAvatarUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedAvatarUD')

    def setName(self, todo0):
        pass

    def friendsNotify(self, todo0, todo1):
        pass

    def checkAvOnShard(self, todo0):
        pass

    def confirmAvOnShard(self, todo0, todo1):
        pass