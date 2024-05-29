# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.TwoDEnemyMgr
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
from direct.showbase.DirectObject import DirectObject
from toontown.minigame import ToonBlitzGlobals
from toontown.minigame import TwoDEnemy

class TwoDEnemyMgr(DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('TwoDEnemyMgr')

    def __init__(self, section, enemyList):
        self.section = section
        self.enemyList = enemyList
        self.load()

    def destroy(self):
        self.section = None
        while len(self.enemies):
            enemy = self.enemies[0]
            enemy.destroy()
            self.enemies.remove(enemy)

        self.enemies = None
        return

    def load(self):
        if len(self.enemyList):
            self.enemiesNP = NodePath('Enemies')
            self.enemiesNP.reparentTo(self.section.sectionNP)
        self.enemies = []
        for index in xrange(len(self.enemyList)):
            enemyId = self.section.getSectionizedId(index)
            suitAttribs = self.enemyList[index]
            newEnemy = TwoDEnemy.TwoDEnemy(self, enemyId, suitAttribs)
            newEnemy.suit.reparentTo(self.enemiesNP)
            self.enemies.append(newEnemy)

    def enterPlay(self, elapsedTime):
        for enemy in self.enemies:
            enemy.start(elapsedTime)

    def exitPlay(self):
        pass

    def enterPause(self):
        for enemy in self.enemies:
            enemy.enterPause()

    def exitPause(self):
        for enemy in self.enemies:
            enemy.exitPause()