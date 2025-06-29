# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.safezone.DistributedFishingSpotAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.fishing import FishGlobals
from toontown.fishing.FishBase import FishBase
from direct.task import Task
from toontown.toonbase import ToontownGlobals

class DistributedFishingSpotAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFishingSpotAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.avId = None
        self.pondDoId = None
        self.posHpr = [None, None, None, None, None, None]
        self.cast = False
        self.lastFish = [None, None, None, None]
        return

    def generate(self):
        DistributedObjectAI.generate(self)
        pond = self.air.doId2do[self.pondDoId]
        pond.addSpot(self)

    def setPondDoId(self, pondDoId):
        self.pondDoId = pondDoId

    def getPondDoId(self):
        return self.pondDoId

    def setPosHpr(self, x, y, z, h, p, r):
        self.posHpr = [
         x, y, z, h, p, r]

    def getPosHpr(self):
        return self.posHpr

    def requestEnter(self):
        avId = self.air.getAvatarIdFromSender()
        if self.avId != None:
            if self.avId == avId:
                self.air.writeServerEvent('suspicious', avId=avId, issue='Toon requested to enter a pier twice!')
            self.sendUpdateToAvatarId(avId, 'rejectEnter', [])
            return
        else:
            self.acceptOnce(self.air.getAvatarExitEvent(avId), self.removeFromPier)
            self.b_setOccupied(avId)
            self.d_setMovie(FishGlobals.EnterMovie, 0, 0, 0, 0, 0, 0)
            taskMgr.remove('cancelAnimation%d' % self.doId)
            taskMgr.doMethodLater(2, DistributedFishingSpotAI.cancelAnimation, 'cancelAnimation%d' % self.doId, [self])
            taskMgr.remove('timeOut%d' % self.doId)
            taskMgr.doMethodLater(45, DistributedFishingSpotAI.removeFromPierWithAnim, 'timeOut%d' % self.doId, [self])
            self.lastFish = [None, None, None]
            self.cast = False
            if self.air.doId2do[self.pondDoId].bingoMgr and self.air.doId2do[self.pondDoId].bingoMgr.state != 'Off':
                self.air.doId2do[self.pondDoId].bingoMgr.activateBingoForPlayer(avId)
            return

    def rejectEnter(self):
        pass

    def requestExit(self):
        avId = self.air.getAvatarIdFromSender()
        if self.avId != avId:
            self.air.writeServerEvent('suspicious', avId=avId, issue="Toon requested to exit a pier they're not on!")
            return
        self.ignore(self.air.getAvatarExitEvent(avId))
        self.removeFromPierWithAnim()

    def setOccupied(self, avId):
        self.avId = avId

    def d_setOccupied(self, avId):
        self.sendUpdate('setOccupied', [avId])

    def b_setOccupied(self, avId):
        self.setOccupied(avId)
        self.d_setOccupied(avId)

    def doCast(self, p, h):
        avId = self.air.getAvatarIdFromSender()
        if self.avId != avId:
            self.air.writeServerEvent('suspicious', avId=avId, issue="Toon tried to cast from a pier they're not on!")
            return
        av = self.air.doId2do.get(avId)
        if not av:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Toon tried to cast while not on district!')
            return
        money = av.getMoney()
        cost = FishGlobals.getCastCost(av.getFishingRod())
        if money < cost:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Toon tried to cast without enough jellybeans!')
            return
        if len(av.fishTank) >= av.getMaxFishTank():
            self.air.writeServerEvent('suspicious', avId=avId, issue='Toon tried to cast with too many fish!')
            return
        av.takeMoney(cost, False)
        self.d_setMovie(FishGlobals.CastMovie, 0, 0, 0, 0, p, h)
        taskMgr.remove('cancelAnimation%d' % self.doId)
        taskMgr.doMethodLater(2, DistributedFishingSpotAI.cancelAnimation, 'cancelAnimation%d' % self.doId, [self])
        taskMgr.remove('timeOut%d' % self.doId)
        taskMgr.doMethodLater(45, DistributedFishingSpotAI.removeFromPierWithAnim, 'timeOut%d' % self.doId, [self])
        self.cast = True

    def sellFish(self):
        avId = self.air.getAvatarIdFromSender()
        if self.avId != avId:
            self.air.writeServerEvent('suspicious', avId=avId, issue="Toon tried to sell fish at a pier they're not using!")
            return
        if self.air.doId2do[pondDoId].getArea() != ToontownGlobals.MyEstate:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Toon tried to sell fish at a pier not in their estate!')
        av = self.air.doId2do.get(avId)
        if not av:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Toon tried to sell fish while not on district!')
            return
        result = self.air.fishManager.creditFishTank(av)
        totalFish = len(av.fishCollection)
        self.sendUpdateToAvatarId(avId, 'sellFishComplete', [result, totalFish])
        taskMgr.remove('timeOut%d' % self.doId)
        taskMgr.doMethodLater(45, DistributedFishingSpotAI.removeFromPierWithAnim, 'timeOut%d' % self.doId, [self])

    def sellFishComplete(self, todo0, todo1):
        pass

    def setMovie(self, todo0, todo1, todo2, todo3, todo4, todo5, todo6):
        pass

    def d_setMovie(self, mode, code, genus, species, weight, p, h):
        self.sendUpdate('setMovie', [mode, code, genus, species, weight, p, h])

    def removeFromPier(self):
        taskMgr.remove('timeOut%d' % self.doId)
        self.cancelAnimation()
        self.d_setOccupied(0)
        self.avId = None
        return

    def removeFromPierWithAnim(self):
        taskMgr.remove('cancelAnimation%d' % self.doId)
        self.d_setMovie(FishGlobals.ExitMovie, 0, 0, 0, 0, 0, 0)
        taskMgr.doMethodLater(1, DistributedFishingSpotAI.removeFromPier, 'remove%d' % self.doId, [self])

    def rewardIfValid(self, target):
        if not self.cast:
            self.air.writeServerEvent('suspicious', avId=self.avId, issue='Toon tried to fish without casting!')
            return
        av = self.air.doId2do[self.avId]
        catch = self.air.fishManager.generateCatch(av, self.air.doId2do[self.pondDoId].getArea())
        self.lastFish = catch
        self.d_setMovie(FishGlobals.PullInMovie, catch[0], catch[1], catch[2], catch[3], 0, 0)
        self.cast = False

    def cancelAnimation(self):
        self.d_setMovie(FishGlobals.NoMovie, 0, 0, 0, 0, 0, 0)