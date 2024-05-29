# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.estate.DistributedBankMgrAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedBankMgrAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBankMgrAI')

    def transferMoney(self, avId, amount):
        av = self.air.doId2do.get(avId)
        if av:
            transactionAmount = amount
            jarMoney = av.getMoney()
            maxJarMoney = av.getMaxMoney()
            bankMoney = av.getBankMoney()
            maxBankMoney = av.getMaxBankMoney()
            transactionAmount = min(transactionAmount, jarMoney)
            transactionAmount = min(transactionAmount, maxBankMoney - bankMoney)
            transactionAmount = -min(-transactionAmount, maxJarMoney - jarMoney)
            transactionAmount = -min(-transactionAmount, bankMoney)
            newJarMoney = jarMoney - transactionAmount
            newBankMoney = bankMoney + transactionAmount
            if newJarMoney > maxJarMoney:
                return
            if newBankMoney > maxBankMoney:
                return
            av.b_setMoney(newJarMoney)
            av.b_setBankMoney(newBankMoney)