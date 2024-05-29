# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.level.DistributedInteractiveEntityAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from otp.level.DistributedEntityAI import DistributedEntityAI

class DistributedInteractiveEntityAI(DistributedEntityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedInteractiveEntityAI')

    def setAvatarInteract(self, todo0):
        pass

    def requestInteract(self):
        pass

    def rejectInteract(self):
        pass

    def requestExit(self):
        pass

    def avatarExit(self, todo0):
        pass

    def setState(self, todo0, todo1):
        pass