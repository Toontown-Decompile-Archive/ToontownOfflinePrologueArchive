# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.cogdominium.DistributedCogdoBarrelAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
import CogdoBarrelRoomConsts, random

class DistributedCogdoBarrelAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCogdoBarrelAI')

    def __init__(self, air, index):
        DistributedObjectAI.__init__(self, air)
        self.index = index
        self.state = CogdoBarrelRoomConsts.StateAvailable
        self.brLaff = 0

    def requestGrab(self):
        toonup = CogdoBarrelRoomConsts.ToonUp
        if self.state == CogdoBarrelRoomConsts.StateAvailable:
            self.state = CogdoBarrelRoomConsts.StateUsed
            self.sendUpdate('setState', [CogdoBarrelRoomConsts.StateUsed])
            self.sendUpdate('setGrab', [self.air.getAvatarIdFromSender()])
            self.brLaff = random.randint(toonup[0], toonup[1])
            self.recieveToonUp()

    def getIndex(self):
        return self.index

    def getState(self):
        return self.state

    def recieveToonUp(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            return
        av.toonUp(self.brLaff)