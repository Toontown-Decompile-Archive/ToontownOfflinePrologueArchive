# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.safezone.DistributedDGFlowerAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedDGFlowerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedDGFlowerAI')
    BASE_HEIGHT = 2.0
    MAX_HEIGHT = 10.0
    HEIGHT_PER_AV = 0.5

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.avatars = set()
        self.height = 2.0

    def avatarEnter(self):
        avId = self.air.getAvatarIdFromSender()
        self.avatars.add(avId)
        self.acceptOnce(self.air.getAvatarExitEvent(avId), self.handleAvatarLeave, extraArgs=[avId])
        self.adjustHeight()

    def avatarExit(self):
        avId = self.air.getAvatarIdFromSender()
        self.handleAvatarLeave(avId)

    def handleAvatarLeave(self, avId):
        self.ignore(self.air.getAvatarExitEvent(avId))
        if avId in self.avatars:
            self.avatars.remove(avId)
        self.adjustHeight()

    def adjustHeight(self):
        height = self.BASE_HEIGHT + self.HEIGHT_PER_AV * len(self.avatars)
        height = min(height, self.MAX_HEIGHT)
        self.b_setHeight(height)

    def setHeight(self, height):
        self.height = height

    def d_setHeight(self, height):
        self.sendUpdate('setHeight', [height])

    def b_setHeight(self, height):
        self.setHeight(height)
        self.d_setHeight(height)

    def getHeight(self):
        return self.height