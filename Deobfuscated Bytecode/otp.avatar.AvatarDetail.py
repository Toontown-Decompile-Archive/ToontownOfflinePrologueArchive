# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.avatar.AvatarDetail
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify.DirectNotifyGlobal import directNotify
from otp.avatar import Avatar

class AvatarDetail:
    notify = directNotify.newCategory('AvatarDetail')

    def __init__(self, doId, callWhenDone):
        self.id = doId
        self.callWhenDone = callWhenDone
        self.enterQuery()

    def isReady(self):
        return true

    def getId(self):
        return self.id

    def enterQuery(self):
        self.avatar = base.cr.doId2do.get(self.id)
        if self.avatar != None and not self.avatar.ghostMode:
            self.createdAvatar = 0
            dclass = self.getDClass()
            self.__handleResponse(True, self.avatar, dclass)
        else:
            self.avatar = self.createHolder()
            self.createdAvatar = 1
            self.avatar.doId = self.id
            dclass = self.getDClass()
            base.cr.getAvatarDetails(self.avatar, self.__handleResponse, dclass)
        return

    def exitQuery(self):
        return true

    def createHolder(self):
        pass

    def getDClass(self):
        pass

    def __handleResponse(self, gotData, avatar, dclass):
        if avatar != self.avatar:
            self.notify.warning('Ignoring unexpected request for avatar %s' % avatar.doId)
            return
        else:
            if gotData:
                self.callWhenDone(self.avatar)
                del self.callWhenDone
            else:
                self.callWhenDone(None)
                del self.callWhenDone
            return