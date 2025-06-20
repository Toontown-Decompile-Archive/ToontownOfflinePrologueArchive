# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.DistributedCashbotBossSafeAI
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from toontown.toonbase import ToontownGlobals
from otp.otpbase import OTPGlobals
import DistributedCashbotBossObjectAI

class DistributedCashbotBossSafeAI(DistributedCashbotBossObjectAI.DistributedCashbotBossObjectAI):
    wantsWatchDrift = 0

    def __init__(self, air, boss, index):
        DistributedCashbotBossObjectAI.DistributedCashbotBossObjectAI.__init__(self, air, boss)
        self.index = index
        self.avoidHelmet = 0
        cn = CollisionNode('sphere')
        cs = CollisionSphere(0, 0, 0, 6)
        cn.addSolid(cs)
        self.attachNewNode(cn)

    def resetToInitialPosition(self):
        posHpr = ToontownGlobals.CashbotBossSafePosHprs[self.index]
        self.setPosHpr(*posHpr)

    def getIndex(self):
        return self.index

    def hitBoss(self, impact):
        avId = self.air.getAvatarIdFromSender()
        self.validate(avId, impact <= 1.0, 'invalid hitBoss impact %s' % impact)
        if avId not in self.boss.involvedToons:
            return
        else:
            if self.state != 'Dropped' and self.state != 'Grabbed':
                return
            if self.avoidHelmet or self == self.boss.heldObject:
                return
            if self.boss.heldObject == None:
                if self.boss.attackCode == ToontownGlobals.BossCogDizzy:
                    damage = int(impact * 50)
                    self.boss.recordHit(max(damage, 2))
                elif self.boss.acceptHelmetFrom(avId):
                    self.demand('Grabbed', self.boss.doId, self.boss.doId)
                    self.boss.heldObject = self
            elif impact >= ToontownGlobals.CashbotBossSafeKnockImpact:
                self.boss.heldObject.demand('Dropped', avId, self.boss.doId)
                self.boss.heldObject.avoidHelmet = 1
                self.boss.heldObject = None
                self.avoidHelmet = 1
                self.boss.waitForNextHelmet()
            return

    def requestInitial(self):
        avId = self.air.getAvatarIdFromSender()
        if avId == self.avId:
            self.demand('Initial')

    def enterGrabbed(self, avId, craneId):
        DistributedCashbotBossObjectAI.DistributedCashbotBossObjectAI.enterGrabbed(self, avId, craneId)
        self.avoidHelmet = 0

    def enterInitial(self):
        self.avoidHelmet = 0
        self.resetToInitialPosition()
        if self.index == 0:
            self.stash()
        self.d_setObjectState('I', 0, 0)

    def exitInitial(self):
        if self.index == 0:
            self.unstash()

    def enterFree(self):
        DistributedCashbotBossObjectAI.DistributedCashbotBossObjectAI.enterFree(self)
        self.avoidHelmet = 0