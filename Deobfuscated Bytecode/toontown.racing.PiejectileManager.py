# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.racing.PiejectileManager
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from pandac.PandaModules import *
from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import *
from toontown.battle.BattleProps import *
from toontown.racing import Piejectile

class PiejectileManager(DirectObject):
    pieCounter = 0

    def __init__(self):
        self.piejectileList = []

    def delete(self):
        for piejectile in self.piejectileList:
            self.__removePiejectile(piejectile)

    def addPiejectile(self, sourceId, targetId=0, type=0):
        name = 'PiejectileManager Pie %s' % PiejectileManager.pieCounter
        pie = Piejectile.Piejectile(sourceId, targetId, type, name)
        self.piejectileList.append(pie)
        PiejectileManager.pieCounter += 1

    def __removePiejectile(self, piejectile):
        self.piejectileList.remove(piejectile)
        piejectile.delete()
        piejectile = None
        return