# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.DistributedBarrelBaseAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from otp.level import DistributedEntityAI
from direct.task import Task
from toontown.coghq import BarrelBase

class DistributedBarrelBaseAI(DistributedEntityAI.DistributedEntityAI, BarrelBase.BarrelBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBarrelBaseAI')

    def __init__(self, level, entId):
        self.rewardPerGrabMax = 0
        DistributedEntityAI.DistributedEntityAI.__init__(self, level, entId)
        self.usedAvIds = []

    def delete(self):
        taskMgr.remove(self.taskName('resetGags'))
        del self.usedAvIds
        del self.pos
        DistributedEntityAI.DistributedEntityAI.delete(self)

    def requestGrab(self):
        avId = self.air.getAvatarIdFromSender()
        self.notify.debug('requestGrab %s' % avId)
        if avId not in self.usedAvIds:
            self.usedAvIds.append(avId)
            self.d_setGrab(avId)
        else:
            self.sendUpdate('setReject')

    def d_setGrab(self, avId):
        self.sendUpdate('setGrab', [avId])