# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.SellbotHQBossBattle
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from toontown.suit import DistributedSellbotBoss
from direct.directnotify import DirectNotifyGlobal
from toontown.coghq import CogHQBossBattle

class SellbotHQBossBattle(CogHQBossBattle.CogHQBossBattle):
    notify = DirectNotifyGlobal.directNotify.newCategory('SellbotHQBossBattle')

    def __init__(self, loader, parentFSM, doneEvent):
        CogHQBossBattle.CogHQBossBattle.__init__(self, loader, parentFSM, doneEvent)
        self.teleportInPosHpr = (0, 95, 18, 180, 0, 0)

    def load(self):
        CogHQBossBattle.CogHQBossBattle.load(self)

    def unload(self):
        CogHQBossBattle.CogHQBossBattle.unload(self)

    def enter(self, requestStatus):
        CogHQBossBattle.CogHQBossBattle.enter(self, requestStatus, DistributedSellbotBoss.OneBossCog)
        self.__setupHighSky()

    def exit(self):
        CogHQBossBattle.CogHQBossBattle.exit(self)
        self.__cleanupHighSky()

    def __setupHighSky(self):
        self.loader.hood.startSky()
        sky = self.loader.hood.sky
        sky.setH(150)
        sky.setZ(-100)

    def __cleanupHighSky(self):
        self.loader.hood.stopSky()
        sky = self.loader.hood.sky
        sky.setH(0)
        sky.setZ(0)