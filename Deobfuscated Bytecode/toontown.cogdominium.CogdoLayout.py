# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.cogdominium.CogdoLayout
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal

class CogdoLayout:
    notify = DirectNotifyGlobal.directNotify.newCategory('CogdoLayout')

    def __init__(self, numFloors):
        self._numFloors = numFloors

    def getNumGameFloors(self):
        return self._numFloors

    def hasBossBattle(self):
        return self._numFloors >= 1

    def getNumFloors(self):
        if self.hasBossBattle():
            return self._numFloors + 1
        else:
            return self._numFloors

    def getBossBattleFloor(self):
        if not self.hasBossBattle():
            self.notify.error('getBossBattleFloor(): cogdo has no boss battle')
        return self.getNumFloors() - 1