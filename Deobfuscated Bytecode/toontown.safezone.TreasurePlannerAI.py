# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.safezone.TreasurePlannerAI
# Compiled at: 2014-04-30 09:53:54
from direct.distributed.ClockDelta import *
from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal
from direct.task import Task
from DistributedTreasureAI import DistributedTreasureAI
import random

class TreasurePlannerAI(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('TreasurePlannerAI')

    def __init__(self, zoneId, treasureType, callback=None):
        self.zoneId = zoneId
        self.treasureType = treasureType
        self.callback = callback
        self.initSpawnPoints()
        self.treasures = []
        for spawnPoint in self.spawnPoints:
            self.treasures.append(None)

        self.deleteTaskNames = set()
        self.lastRequestId = None
        self.requestStartTime = None
        self.requestCount = None
        return

    def initSpawnPoints(self):
        self.spawnPoints = []
        return self.spawnPoints

    def numTreasures(self):
        counter = 0
        for treasure in self.treasures:
            if treasure:
                counter += 1

        return counter

    def countEmptySpawnPoints(self):
        counter = 0
        for treasure in self.treasures:
            if treasure == None:
                counter += 1

        return counter

    def nthEmptyIndex(self, n):
        emptyCounter = -1
        spawnPointCounter = -1
        while emptyCounter < n:
            spawnPointCounter += 1
            if self.treasures[spawnPointCounter] == None:
                emptyCounter += 1

        return spawnPointCounter

    def findIndexOfTreasureId(self, treasureId):
        counter = 0
        for treasure in self.treasures:
            if treasure == None:
                pass
            elif treasureId == treasure.getDoId():
                return counter
            counter += 1

        return

    def placeAllTreasures(self):
        index = 0
        for treasure in self.treasures:
            if not treasure:
                self.placeTreasure(index)
            index += 1

    def placeTreasure(self, index):
        spawnPoint = self.spawnPoints[index]
        treasure = DistributedTreasureAI(simbase.air, self, self.treasureType, spawnPoint[0], spawnPoint[1], spawnPoint[2])
        treasure.generateWithRequired(self.zoneId)
        self.treasures[index] = treasure

    def validAvatar(self, treasure, av):
        return treasure.validAvatar(av)

    def grabAttempt(self, avId, treasureId):
        if self.lastRequestId == avId:
            self.requestCount += 1
            now = globalClock.getFrameTime()
            elapsed = now - self.requestStartTime
            if elapsed > 10:
                self.requestCount = 1
                self.requestStartTime = now
            else:
                secondsPerGrab = elapsed / self.requestCount
                if self.requestCount >= 3 and secondsPerGrab <= 0.4:
                    simbase.air.writeServerEvent('suspicious', avId=avId, issue='TreasurePlannerAI.grabAttempt %s treasures in %s seconds' % (self.requestCount, elapsed))
        else:
            self.lastRequestId = avId
            self.requestCount = 1
            self.requestStartTime = globalClock.getFrameTime()
        index = self.findIndexOfTreasureId(treasureId)
        if index == None:
            pass
        else:
            av = simbase.air.doId2do.get(avId)
            if av == None:
                simbase.air.writeServerEvent('suspicious', avId=avId, issue='TreasurePlannerAI.grabAttempt unknown avatar')
                self.notify.warning('avid: %s does not exist' % avId)
            else:
                treasure = self.treasures[index]
                if self.validAvatar(treasure, av):
                    self.treasures[index] = None
                    if self.callback:
                        self.callback(avId)
                    treasure.d_setGrab(avId)
                    self.deleteTreasureSoon(treasure)
                else:
                    treasure.d_setReject()
        return

    def deleteTreasureSoon(self, treasure):
        taskName = treasure.uniqueName('deletingTreasure')
        taskMgr.doMethodLater(5, self.__deleteTreasureNow, taskName, extraArgs=(treasure, taskName))
        self.deleteTaskNames.add(taskName)

    def deleteAllTreasuresNow(self):
        for treasure in self.treasures:
            if treasure:
                treasure.requestDelete()

        for taskName in self.deleteTaskNames:
            tasks = taskMgr.getTasksNamed(taskName)
            if len(tasks):
                treasure = tasks[0].getArgs()[0]
                treasure.requestDelete()
                taskMgr.remove(taskName)

        self.deleteTaskNames = set()
        self.treasures = []
        for spawnPoint in self.spawnPoints:
            self.treasures.append(None)

        return

    def __deleteTreasureNow(self, treasure, taskName):
        treasure.requestDelete()
        self.deleteTaskNames.remove(taskName)