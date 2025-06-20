# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.fishing.DistributedFishingPondAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedFishingPondAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFishingPondAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.area = None
        self.targets = {}
        self.spots = {}
        self.bingoMgr = None
        return

    def hitTarget(self, target):
        avId = self.air.getAvatarIdFromSender()
        if self.targets.get(target) == None:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Toon tried to hit nonexistent fishing target!')
            return
        else:
            spot = self.hasToon(avId)
            if spot:
                spot.rewardIfValid(target)
                return
            self.air.writeServerEvent('suspicious', avId=avId, issue='Toon tried to catch fish while not fishing!')
            return

    def addTarget(self, target):
        self.targets[target.doId] = target

    def addSpot(self, spot):
        self.spots[spot.doId] = spot

    def setArea(self, area):
        self.area = area

    def getArea(self):
        return self.area

    def hasToon(self, avId):
        for spot in self.spots:
            if self.spots[spot].avId == avId:
                return self.spots[spot]