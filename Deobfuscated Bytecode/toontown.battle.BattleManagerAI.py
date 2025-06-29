# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.battle.BattleManagerAI
# Compiled at: 2014-04-30 09:53:54
import DistributedBattleAI
from direct.directnotify import DirectNotifyGlobal

class BattleManagerAI:
    notify = DirectNotifyGlobal.directNotify.newCategory('BattleManagerAI')

    def __init__(self, air):
        self.air = air
        self.cellId2battle = {}
        self.battleConstructor = DistributedBattleAI.DistributedBattleAI

    def cellHasBattle(self, cellId):
        return self.cellId2battle.has_key(cellId)

    def getBattle(self, cellId):
        if self.cellId2battle.has_key(cellId):
            return self.cellId2battle[cellId]
        else:
            return

    def newBattle(self, cellId, zoneId, pos, suit, toonId, finishCallback=None, maxSuits=4, interactivePropTrackBonus=-1):
        if self.cellId2battle.has_key(cellId):
            self.notify.info("A battle is already present in the suit's zone!")
            if not self.requestBattleAddSuit(cellId, suit):
                suit.flyAwayNow()
            battle = self.cellId2battle[cellId]
            battle.signupToon(toonId, pos[0], pos[1], pos[2])
        else:
            battle = self.battleConstructor(self.air, self, pos, suit, toonId, zoneId, finishCallback, maxSuits, interactivePropTrackBonus=interactivePropTrackBonus)
            battle.generateWithRequired(zoneId)
            battle.battleCellId = cellId
            self.cellId2battle[cellId] = battle
        return battle

    def requestBattleAddSuit(self, cellId, suit):
        return self.cellId2battle[cellId].suitRequestJoin(suit)

    def destroy(self, battle):
        cellId = battle.battleCellId
        self.notify.debug('BattleManager - destroying battle %d' % cellId)
        del self.cellId2battle[cellId]
        battle.requestDelete()