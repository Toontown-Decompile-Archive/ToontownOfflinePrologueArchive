# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.toon.DistributedNPCClerkAI
# Compiled at: 2014-04-30 09:53:54
from direct.task.Task import Task
from pandac.PandaModules import *
from DistributedNPCToonBaseAI import *

class DistributedNPCClerkAI(DistributedNPCToonBaseAI):

    def __init__(self, air, npcId):
        DistributedNPCToonBaseAI.__init__(self, air, npcId)
        self.timedOut = 0

    def delete(self):
        taskMgr.remove(self.uniqueName('clearMovie'))
        self.ignoreAll()
        DistributedNPCToonBaseAI.delete(self)

    def avatarEnter(self):
        avId = self.air.getAvatarIdFromSender()
        DistributedNPCToonBaseAI.avatarEnter(self)
        av = self.air.doId2do.get(avId)
        if av is None:
            self.notify.warning('toon isnt there! toon: %s' % avId)
            return
        else:
            self.acceptOnce(self.air.getAvatarExitEvent(avId), self.__handleUnexpectedExit, extraArgs=[avId])
            if self.isBusy():
                self.freeAvatar(avId)
                return
            if av.getMoney():
                self.sendStartMovie(avId)
            else:
                self.sendNoMoneyMovie(avId)
            return

    def sendStartMovie(self, avId):
        self.busy = avId
        self.sendUpdate('setMovie', [NPCToons.PURCHASE_MOVIE_START,
         self.npcId,
         avId,
         ClockDelta.globalClockDelta.getRealNetworkTime()])
        taskMgr.doMethodLater(NPCToons.CLERK_COUNTDOWN_TIME, self.sendTimeoutMovie, self.uniqueName('clearMovie'))

    def sendNoMoneyMovie(self, avId):
        self.busy = avId
        self.sendUpdate('setMovie', [NPCToons.PURCHASE_MOVIE_NO_MONEY,
         self.npcId,
         avId,
         ClockDelta.globalClockDelta.getRealNetworkTime()])
        self.sendClearMovie(None)
        return

    def sendTimeoutMovie(self, task):
        self.timedOut = 1
        self.sendUpdate('setMovie', [NPCToons.PURCHASE_MOVIE_TIMEOUT,
         self.npcId,
         self.busy,
         ClockDelta.globalClockDelta.getRealNetworkTime()])
        self.sendClearMovie(None)
        return Task.done

    def sendClearMovie(self, task):
        self.ignore(self.air.getAvatarExitEvent(self.busy))
        self.busy = 0
        self.timedOut = 0
        self.sendUpdate('setMovie', [NPCToons.PURCHASE_MOVIE_CLEAR,
         self.npcId,
         0,
         ClockDelta.globalClockDelta.getRealNetworkTime()])
        return Task.done

    def completePurchase(self, avId):
        self.busy = avId
        self.sendUpdate('setMovie', [NPCToons.PURCHASE_MOVIE_COMPLETE,
         self.npcId,
         avId,
         ClockDelta.globalClockDelta.getRealNetworkTime()])
        self.sendClearMovie(None)
        return

    def setInventory(self, blob, newMoney, done):
        avId = self.air.getAvatarIdFromSender()
        if self.busy != avId:
            if self.busy != 0:
                self.air.writeServerEvent('suspicious', avId=avId, issue='DistributedNPCClerkAI.setInventory busy with %s' % self.busy)
                self.notify.warning('setInventory from unknown avId: %s busy: %s' % (avId, self.busy))
            return
        if self.air.doId2do.has_key(avId):
            av = self.air.doId2do[avId]
            newInventory = av.inventory.makeFromNetString(blob)
            currentMoney = av.getMoney()
            if av.inventory.validatePurchase(newInventory, currentMoney, newMoney):
                av.setMoney(newMoney)
                if done:
                    av.d_setInventory(av.inventory.makeNetString())
                    av.d_setMoney(newMoney)
            else:
                self.air.writeServerEvent('suspicious', avId=avId, issue='DistributedNPCClerkAI.setInventory invalid purchase')
                self.notify.warning('Avatar ' + str(avId) + ' attempted an invalid purchase.')
                av.d_setInventory(av.inventory.makeNetString())
                av.d_setMoney(av.getMoney())
        if self.timedOut:
            return
        if done:
            taskMgr.remove(self.uniqueName('clearMovie'))
            self.completePurchase(avId)

    def __handleUnexpectedExit(self, avId):
        self.notify.warning('avatar:' + str(avId) + ' has exited unexpectedly')
        self.sendTimeoutMovie(None)
        return