# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.suit.DistributedTutorialSuitAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from toontown.suit.DistributedSuitBaseAI import DistributedSuitBaseAI
from toontown.tutorial.DistributedBattleTutorialAI import DistributedBattleTutorialAI
from panda3d.core import *
import SuitDNA

class FakeBattleManager:

    def __init__(self, avId):
        self.avId = avId

    def destroy(self, battle):
        if battle.suitsKilledThisBattle:
            if self.avId in simbase.air.tutorialManager.avId2fsm.keys():
                simbase.air.tutorialManager.avId2fsm[self.avId].demand('HQ')
        battle.requestDelete()


class DistributedTutorialSuitAI(DistributedSuitBaseAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTutorialSuitAI')

    def __init__(self, air):
        DistributedSuitBaseAI.__init__(self, air, None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('f')
        self.dna = suitDNA
        self.setLevel(1)
        return

    def destroy(self):
        del self.dna

    def requestBattle(self, x, y, z, h, p, r):
        self.confrontPosHpr = (
         LPoint3f(x, y, z), LPoint3f(h, p, r))
        avId = self.air.getAvatarIdFromSender()
        battle = DistributedBattleTutorialAI(self.air, FakeBattleManager(avId), LPoint3f(x, y, z), self, avId, 20001, maxSuits=1, tutorialFlag=1)
        battle.generateWithRequired(self.zoneId)
        battle.battleCellId = 0

    def getConfrontPosHpr(self):
        return self.confrontPosHpr