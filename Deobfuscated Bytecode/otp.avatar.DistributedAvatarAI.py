# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.avatar.DistributedAvatarAI
# Compiled at: 2014-04-30 09:53:54
from otp.otpbase import OTPGlobals
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.distributed import DistributedNodeAI
from direct.task import Task

class DistributedAvatarAI(DistributedNodeAI.DistributedNodeAI):

    def __init__(self, air):
        DistributedNodeAI.DistributedNodeAI.__init__(self, air)
        self.hp = 0
        self.maxHp = 0

    def b_setName(self, name):
        self.setName(name)
        self.d_setName(name)

    def d_setName(self, name):
        self.sendUpdate('setName', [name])

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def b_setMaxHp(self, maxHp):
        self.d_setMaxHp(maxHp)
        self.setMaxHp(maxHp)

    def d_setMaxHp(self, maxHp):
        self.sendUpdate('setMaxHp', [maxHp])

    def setMaxHp(self, maxHp):
        self.maxHp = maxHp

    def getMaxHp(self):
        return self.maxHp

    def b_setHp(self, hp):
        self.d_setHp(hp)
        self.setHp(hp)

    def d_setHp(self, hp):
        self.sendUpdate('setHp', [hp])

    def setHp(self, hp):
        self.hp = hp

    def getHp(self):
        return self.hp

    def b_setLocationName(self, locationName):
        self.d_setLocationName(locationName)
        self.setLocationName(locationName)

    def d_setLocationName(self, locationName):
        pass

    def setLocationName(self, locationName):
        self.locationName = locationName

    def getLocationName(self):
        return self.locationName

    def b_setActivity(self, activity):
        self.d_setActivity(activity)
        self.setActivity(activity)

    def d_setActivity(self, activity):
        pass

    def setActivity(self, activity):
        self.activity = activity

    def getActivity(self):
        return self.activity

    def toonUp(self, num):
        if self.hp >= self.maxHp:
            return
        self.hp = min(self.hp + num, self.maxHp)
        self.b_setHp(self.hp)

    def getRadius(self):
        return OTPGlobals.AvatarDefaultRadius

    def checkAvOnShard(self, avId):
        senderId = self.air.getAvatarIdFromSender()
        onShard = False
        if simbase.air.doId2do.get(avId):
            onShard = True
        self.sendUpdateToAvatarId(senderId, 'confirmAvOnShard', [avId, onShard])