# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.LevelBattleManagerAI
# Compiled at: 2014-04-30 09:53:54
from toontown.battle import BattleManagerAI
from direct.directnotify import DirectNotifyGlobal
from toontown.coghq import BattleExperienceAggregatorAI

class LevelBattleManagerAI(BattleManagerAI.BattleManagerAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('LevelBattleManagerAI')

    def __init__(self, air, level, battleCtor, battleExpAggreg=None):
        BattleManagerAI.BattleManagerAI.__init__(self, air)
        self.battleCtor = battleCtor
        self.level = level
        self.battleBlockers = {}
        if battleExpAggreg is None:
            battleExpAggreg = BattleExperienceAggregatorAI.BattleExperienceAggregatorAI()
        self.battleExpAggreg = battleExpAggreg
        return

    def destroyBattleMgr(self):
        battles = self.cellId2battle.values()
        for battle in battles:
            self.destroy(battle)

        for cellId, battleBlocker in self.battleBlockers.items():
            if battleBlocker is not None:
                battleBlocker.deactivate()

        del self.battleBlockers
        del self.cellId2battle
        del self.battleExpAggreg
        return

    def newBattle(self, cellId, zoneId, pos, suit, toonId, roundCallback=None, finishCallback=None, maxSuits=4):
        battle = self.cellId2battle.get(cellId, None)
        if battle != None:
            self.notify.debug('battle already created by battle blocker, add toon %d' % toonId)
            battle.signupToon(toonId, pos[0], pos[1], pos[2])
            return battle
        else:
            battle = self.battleCtor(self.air, self, pos, suit, toonId, zoneId, self.level, cellId, roundCallback, finishCallback, maxSuits)
            self.battleExpAggreg.attachToBattle(battle)
            battle.battleCalc.setSkillCreditMultiplier(self.level.getBattleCreditMultiplier())
            battle.addToon(toonId)
            battle.generateWithRequired(zoneId)
            self.cellId2battle[cellId] = battle
            return battle

    def addBattleBlocker(self, blocker, cellId):
        self.battleBlockers[cellId] = blocker
        messenger.send(self.level.planner.getBattleBlockerEvent(cellId))