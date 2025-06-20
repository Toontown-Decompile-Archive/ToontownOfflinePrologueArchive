# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.estate.DistributedBankAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from toontown.estate.DistributedFurnitureItemAI import DistributedFurnitureItemAI
from direct.distributed.ClockDelta import *
import BankGlobals

class DistributedBankAI(DistributedFurnitureItemAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBankAI')

    def __init__(self, air, furnitureMgr, item):
        DistributedFurnitureItemAI.__init__(self, air, furnitureMgr, item)
        self.avId = None
        self.movie = BankGlobals.BANK_MOVIE_CLEAR
        return

    def avatarEnter(self):
        avId = self.air.getAvatarIdFromSender()
        if not self.avId:
            if not self.furnitureMgr.ownerId:
                self.b_setMovie(BankGlobals.BANK_MOVIE_NO_OWNER, avId, globalClockDelta.getRealNetworkTime())
                return
            else:
                if self.furnitureMgr.ownerId != avId:
                    self.b_setMovie(BankGlobals.BANK_MOVIE_NOT_OWNER, avId, globalClockDelta.getRealNetworkTime())
                    return
                self.avId = avId
                self.b_setMovie(BankGlobals.BANK_MOVIE_GUI, avId, globalClockDelta.getRealNetworkTime())
                return

        else:
            if avId == self.avId:
                self.air.writeServerEvent('suspicious', avId=avId, issue='Tried to use bank while already using it!')
            self.sendUpdateToAvatarId(avId, 'freeAvatar', [])

    def freeAvatar(self):
        pass

    def setMovie(self, mode, avId, time):
        self.movie = mode
        if self.movie != BankGlobals.BANK_MOVIE_CLEAR:
            taskMgr.doMethodLater(2.0, self.clearMovie, 'clear-movie-%d' % self.getDoId())

    def clearMovie(self, task):
        self.b_setMovie(BankGlobals.BANK_MOVIE_CLEAR, 0, globalClockDelta.getRealNetworkTime())

    def b_setMovie(self, mode, avId, time):
        self.setMovie(mode, avId, time)
        self.d_setMovie(mode, avId, time)

    def d_setMovie(self, mode, avId, time):
        self.sendUpdate('setMovie', [mode, avId, time])

    def transferMoney(self, amount):
        avId = self.air.getAvatarIdFromSender()
        if avId != self.avId:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Tried to transfer money while not using a bank!')
            return
        else:
            av = self.air.doId2do.get(avId)
            if not av:
                self.air.writeServerEvent('suspicious', avId=avId, issue='Tried to transfer money while not on the AI!')
                return
            if amount == 0:
                self.b_setMovie(BankGlobals.BANK_MOVIE_NO_OP, avId, globalClockDelta.getRealNetworkTime())
            elif amount > 0:
                self.b_setMovie(BankGlobals.BANK_MOVIE_DEPOSIT, avId, globalClockDelta.getRealNetworkTime())
                if av.money < amount:
                    self.air.writeServerEvent('suspicious', avId=avId, issue='Toon tried to deposit more money than they have!')
                else:
                    av.b_setMoney(av.money - amount)
                    av.b_setBankMoney(av.bankMoney + amount)
            else:
                self.b_setMovie(BankGlobals.BANK_MOVIE_WITHDRAW, avId, globalClockDelta.getRealNetworkTime())
                if av.bankMoney + amount < 0:
                    self.air.writeServerEvent('suspicious', avId=avId, issue='Toon tried to withdraw more money than they have!')
                else:
                    av.b_setMoney(av.money - amount)
                    av.b_setBankMoney(av.bankMoney + amount)
            self.avId = None
            return