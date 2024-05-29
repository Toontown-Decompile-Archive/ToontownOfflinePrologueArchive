# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.suit.SuitInvasionManagerAI
# Compiled at: 2014-04-30 09:53:54
import SuitDNA
from otp.ai.MagicWordGlobal import *
from direct.task import Task
from toontown.toonbase import ToontownGlobals
from random import random, randint, choice
import datetime
from direct.directnotify import DirectNotifyGlobal

class SuitInvasionManagerAI:
    notify = DirectNotifyGlobal.directNotify.newCategory('SuitInvasionManagerAI')

    def __init__(self, air):
        self.air = air
        self.invading = 0
        self.specialSuit = 0
        self.suitName = None
        self.numSuits = 0
        self.spawnedSuits = 0
        self.specialSuit = False
        if config.GetBool('want-mega-invasions', False) or self.air.holidayManager.isInvasionHolidayRunning():
            self.randomInvasionProbability = config.GetFloat('mega-invasion-probability', 0.4)
            self.specialSuit = choice([0, 0, 0, 1, 2])
            self.megaInvasionCog = config.GetString('mega-invasion-cog-type', '')
            if not self.megaInvasionCog:
                invasionTuple = self.air.holidayManager.whosInvading()
                self.megaInvasionCog = invasionTuple[0]
                self.specialSuit = invasionTuple[1]
                if not self.megaInvasionCog:
                    raise AttributeError('No mega invasion cog specified, but mega invasions are on!')
            if self.megaInvasionCog not in SuitDNA.suitHeadTypes:
                raise AttributeError('Invalid cog type specified for mega invasion!')
            taskMgr.doMethodLater(randint(1800, 5400), self.__randomInvasionTick, 'random-invasion-tick')
        elif config.GetBool('want-random-invasions', True):
            self.randomInvasionProbability = config.GetFloat('random-invasion-probability', 0.3)
            taskMgr.doMethodLater(randint(1800, 5400), self.__randomInvasionTick, 'random-invasion-tick')
        return

    def __randomInvasionTick(self, task=None):
        task.delayTime = randint(1800, 5400)
        if self.getInvading():
            self.notify.debug('Invasion tested but already running invasion!')
            return task.again
        if random() <= self.randomInvasionProbability:
            self.notify.debug('Invasion probability hit! Starting invasion.')
            if config.GetBool('want-mega-invasions', False) and random() <= self.randomInvasionProbability or simbase.air.holidayManager.isInvasionHolidayRunning() and random() <= self.randomInvasionProbability:
                suitName = self.megaInvasionCog
                numSuits = randint(2000, 15000)
            else:
                suitName = choice(SuitDNA.suitHeadTypes[:32])
                numSuits = randint(1500, 5000)
                self.specialSuit = False
            self.startInvasion(suitName, numSuits, self.specialSuit)
        return task.again

    def getInvading(self):
        return self.invading

    def stopInvasion(self, task=None):
        if not self.getInvading():
            return False
        else:
            self.air.newsManager.sendUpdate('setInvasionStatus', [
             ToontownGlobals.SuitInvasionEnd, self.suitName,
             self.numSuits, self.specialSuit])
            if task is not None:
                task.remove()
            else:
                taskMgr.remove('invasion-timeout')
            self.specialSuit = 0
            self.numSuits = 0
            self.spawnedSuits = 0
            self.invading = 0
            self.suitName = None
            self.__spAllCogsSupaFly()
            return

    def __checkInvasionOver(self):
        if self.spawnedSuits >= self.numSuits:
            self.stopInvasion()

    def getInvadingCog(self):
        self.spawnedSuits += 1
        self.__checkInvasionOver()
        return (self.suitName, self.specialSuit)

    def __spAllCogsSupaFly(self):
        for sp in self.air.suitPlanners.values():
            sp.flySuits()

    def startInvasion(self, suitName='f', numSuits=1000, specialSuit=0):
        if self.getInvading():
            return False
        self.invading = True
        self.spawnedSuits = 0
        self.suitName = suitName
        self.numSuits = numSuits
        self.specialSuit = specialSuit
        self.air.newsManager.sendUpdate('setInvasionStatus', [
         ToontownGlobals.SuitInvasionBegin, self.suitName,
         self.numSuits, self.specialSuit])
        timePerCog = config.GetFloat('invasion-time-per-cog', 1.5)
        taskMgr.doMethodLater(timePerCog * numSuits, self.stopInvasion, 'invasion-timeout')
        self.__spAllCogsSupaFly()
        return True


@magicWord(types=[str, str, int, int], category=CATEGORY_OVERRIDE)
def invasion(cmd, name='f', num=1000, specialSuit=0):
    invMgr = simbase.air.suitInvasionManager
    if cmd == 'start':
        if invMgr.getInvading():
            return 'There is already an invasion on the current AI!'
        if name not in SuitDNA.suitHeadTypes:
            return 'This cog does not exist!'
        invMgr.startInvasion(name, num, specialSuit)
    elif cmd == 'stop':
        if not invMgr.getInvading():
            return 'There is no invasion on the current AI!'
        invMgr.stopInvasion()
    else:
        return "You didn't enter a valid command! Commands are ~invasion start or stop."