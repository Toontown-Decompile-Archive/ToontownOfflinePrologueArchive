# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.toon.DistributedNPCKartClerkAI
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from DistributedNPCToonBaseAI import *
from toontown.toonbase import TTLocalizer
from direct.task import Task
from toontown.racing.KartShopGlobals import *
from toontown.racing.KartDNA import *

class DistributedNPCKartClerkAI(DistributedNPCToonBaseAI):

    def __init__(self, air, npcId):
        DistributedNPCToonBaseAI.__init__(self, air, npcId)
        self.givesQuests = 0
        self.busy = 0

    def delete(self):
        taskMgr.remove(self.uniqueName('clearMovie'))
        self.ignoreAll()
        DistributedNPCToonBaseAI.delete(self)

    def avatarEnter(self):
        avId = self.air.getAvatarIdFromSender()
        if not self.air.doId2do.has_key(avId):
            self.notify.warning('Avatar: %s not found' % avId)
            return
        if self.isBusy():
            self.freeAvatar(avId)
            return
        self.transactionType = ''
        av = self.air.doId2do[avId]
        self.busy = avId
        self.acceptOnce(self.air.getAvatarExitEvent(avId), self.__handleUnexpectedExit, extraArgs=[avId])
        flag = NPCToons.SELL_MOVIE_START
        self.d_setMovie(avId, flag)
        taskMgr.doMethodLater(KartShopGlobals.KARTCLERK_TIMER, self.sendTimeoutMovie, self.uniqueName('clearMovie'))
        DistributedNPCToonBaseAI.avatarEnter(self)

    def rejectAvatar(self, avId):
        self.notify.warning('rejectAvatar: should not be called by a kart clerk!')

    def d_setMovie(self, avId, flag, extraArgs=[]):
        self.sendUpdate('setMovie', [flag,
         self.npcId,
         avId,
         extraArgs,
         ClockDelta.globalClockDelta.getRealNetworkTime()])

    def sendTimeoutMovie(self, task):
        self.d_setMovie(self.busy, NPCToons.SELL_MOVIE_TIMEOUT)
        self.sendClearMovie(None)
        return Task.done

    def sendClearMovie(self, task):
        self.ignore(self.air.getAvatarExitEvent(self.busy))
        taskMgr.remove(self.uniqueName('clearMovie'))
        self.busy = 0
        self.d_setMovie(0, NPCToons.SELL_MOVIE_CLEAR)
        return Task.done

    def buyKart(self, whichKart):
        avId = self.air.getAvatarIdFromSender()
        if self.busy != avId:
            self.air.writeServerEvent('suspicious', avId=avId, issue='DistributedNPCKartClerkAI.buyKart busy with %s' % self.busy)
            self.notify.warning('somebody called buyKart that I was not busy with! avId: %s' % avId)
            return
        av = simbase.air.doId2do.get(avId)
        if av:
            movieType = NPCToons.SELL_MOVIE_COMPLETE
            extraArgs = []
            cost = getKartCost(whichKart)
            if cost == 'key error':
                self.air.writeServerEvent('suspicious', avId=avId, issue='Player trying to buy non-existant kart %s' % whichKart)
                self.notify.warning('somebody is trying to buy non-existant kart%s! avId: %s' % (whichKart, avId))
                return
            if cost > av.getTickets():
                self.air.writeServerEvent('suspicious', avId=avId, issue="DistributedNPCKartClerkAI.buyKart and toon doesn't have enough tickets!")
                self.notify.warning("somebody called buyKart and didn't have enough tickets to purchase! avId: %s" % avId)
                return
            av.b_setTickets(av.getTickets() - cost)
            self.air.writeServerEvent('kartingTicketsSpent', avId=avId, cost='%s' % cost)
            av.b_setKartBodyType(whichKart)
            self.air.writeServerEvent('kartingKartPurchased', avId=avId, kartType='%s' % whichKart)

    def buyAccessory(self, whichAcc):
        avId = self.air.getAvatarIdFromSender()
        av = simbase.air.doId2do.get(avId)
        if self.busy != avId:
            self.air.writeServerEvent('suspicious', avId=avId, issue='DistributedNPCKartClerkAI.buyAccessory busy with %s' % self.busy)
            self.notify.warning('somebody called buyAccessory that I was not busy with! avId: %s' % avId)
            return
        if len(av.getKartAccessoriesOwned()) >= KartShopGlobals.MAX_KART_ACC:
            self.air.writeServerEvent('suspicious', avId=avId, issue='DistributedNPCKartClerkAI.buyAcc and toon already has max number of accessories!')
            self.notify.warning('somebody called buyAcc and already has maximum allowed accessories! avId: %s' % avId)
            return
        av = simbase.air.doId2do.get(avId)
        if av:
            movieType = NPCToons.SELL_MOVIE_COMPLETE
            extraArgs = []
            cost = getAccCost(whichAcc)
            if cost > av.getTickets():
                self.air.writeServerEvent('suspicious', avId=avId, issue="DistributedNPCKartClerkAI.buyAcc and toon doesn't have enough tickets!")
                self.notify.warning("somebody called buyAcc and didn't have enough tickets to purchase! avId: %s" % avId)
                return
            av.b_setTickets(av.getTickets() - cost)
            self.air.writeServerEvent('kartingTicketsSpent', avId=avId, cost='%s' % cost)
            av.addOwnedAccessory(whichAcc)
            self.air.writeServerEvent('kartingAccessoryPurchased', avId=avId, accessory='%s' % whichAcc)
            av.updateKartDNAField(getAccessoryType(whichAcc), whichAcc)

    def transactionDone(self):
        avId = self.air.getAvatarIdFromSender()
        if self.busy != avId:
            self.air.writeServerEvent('suspicious', avId=avId, issue='DistributedNPCKartClerkAI.transactionDone busy with %s' % self.busy)
            self.notify.warning('somebody called transactionDone that I was not busy with! avId: %s' % avId)
            return
        else:
            av = simbase.air.doId2do.get(avId)
            if av:
                movieType = NPCToons.SELL_MOVIE_COMPLETE
                extraArgs = []
                self.d_setMovie(avId, movieType, extraArgs)
            self.sendClearMovie(None)
            return

    def __handleUnexpectedExit(self, avId):
        self.notify.warning('avatar:' + str(avId) + ' has exited unexpectedly')
        self.notify.warning('not busy with avId: %s, busy: %s ' % (avId, self.busy))
        taskMgr.remove(self.uniqueName('clearMovie'))
        self.sendClearMovie(None)
        return