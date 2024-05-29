# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.election.InvasionMasterAI
# Compiled at: 2014-04-30 09:53:54
import random

class InvasionMasterAI:
    UNREACHABLE_TIMEOUT = 30.0

    def __init__(self, invasion):
        self.invasion = invasion
        self._unreachables = {}

    def getAttackableToons(self):
        result = []
        for toon in self.invasion.toons:
            if toon.ghostMode:
                continue
            unreachableTimestamp = self._unreachables.get(toon.doId)
            if unreachableTimestamp and unreachableTimestamp > globalClock.getFrameTime():
                continue
            result.append(toon)

        return result

    def requestOrders(self, brain):
        attackables = self.getAttackableToons()
        if attackables:
            toonId = random.choice(attackables).doId
            brain.demand('Attack', toonId)
        else:
            brain.demand('AskAgain')

    def toonUnreachable(self, toonId):
        self._unreachables[toonId] = globalClock.getFrameTime() + self.UNREACHABLE_TIMEOUT