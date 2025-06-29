# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.DistributedMazeGameAI
# Compiled at: 2014-04-30 09:53:54
from DistributedMinigameAI import *
from direct.fsm import ClassicFSM, State
from direct.fsm import State
import PatternGameGlobals
from direct.task.Task import Task
import MazeGameGlobals, MazeData

class DistributedMazeGameAI(DistributedMinigameAI):

    def __init__(self, air, minigameId):
        try:
            self.DistributedMinigameTemplateAI_initialized
        except:
            self.DistributedMinigameTemplateAI_initialized = 1
            DistributedMinigameAI.__init__(self, air, minigameId)
            self.gameFSM = ClassicFSM.ClassicFSM('DistributedMazeGameAI', [State.State('inactive', self.enterInactive, self.exitInactive, ['play']),
             State.State('play', self.enterPlay, self.exitPlay, ['waitShowScores', 'cleanup']),
             State.State('waitShowScores', self.enterWaitShowScores, self.exitWaitShowScores, ['cleanup']),
             State.State('cleanup', self.enterCleanup, self.exitCleanup, ['inactive'])], 'inactive', 'inactive')
            self.addChildGameFSM(self.gameFSM)

    def delete(self):
        self.notify.debug('delete')
        del self.gameFSM
        DistributedMinigameAI.delete(self)

    def setGameReady(self):
        self.notify.debug('setGameReady')
        DistributedMinigameAI.setGameReady(self)
        mazeName = MazeGameGlobals.getMazeName(self.doId, self.numPlayers, MazeData.mazeNames)
        mData = MazeData.mazeData[mazeName]
        self.numTreasures = len(mData['treasurePosList'])
        self.numTreasuresTaken = 0
        self.takenTable = [0] * self.numTreasures
        for avId in self.scoreDict.keys():
            self.scoreDict[avId] = 0

    def setGameStart(self, timestamp):
        self.notify.debug('setGameStart')
        DistributedMinigameAI.setGameStart(self, timestamp)
        self.gameFSM.request('play')

    def setGameAbort(self):
        self.notify.debug('setGameAbort')
        if self.gameFSM.getCurrentState():
            self.gameFSM.request('cleanup')
        DistributedMinigameAI.setGameAbort(self)

    def gameOver(self):
        self.notify.debug('gameOver')
        self.gameFSM.request('cleanup')
        DistributedMinigameAI.gameOver(self)

    def enterInactive(self):
        self.notify.debug('enterInactive')

    def exitInactive(self):
        pass

    def getTimeBase(self):
        return self.__timeBase

    def enterPlay(self):
        self.notify.debug('enterPlay')
        taskMgr.doMethodLater(MazeGameGlobals.GAME_DURATION, self.timerExpired, self.taskName('gameTimer'))

    def exitPlay(self):
        taskMgr.remove(self.taskName('gameTimer'))

    def claimTreasure(self, treasureNum):
        if self.gameFSM.getCurrentState() is None or self.gameFSM.getCurrentState().getName() != 'play':
            return
        avId = self.air.getAvatarIdFromSender()
        if not self.scoreDict.has_key(avId):
            self.notify.warning('PROBLEM: avatar %s called claimTreasure(%s) but he is not in the scoreDict: %s. avIdList is: %s' % (avId,
             treasureNum,
             self.scoreDict,
             self.avIdList))
            return
        else:
            if treasureNum < 0 or treasureNum >= self.numTreasures:
                self.air.writeServerEvent('warning', avId=avId, issue='MazeGameAI.claimTreasure treasureNum out of range, was %s' % treasureNum)
                return
            if self.takenTable[treasureNum]:
                return
            self.takenTable[treasureNum] = 1
            avId = self.air.getAvatarIdFromSender()
            self.sendUpdate('setTreasureGrabbed', [avId, treasureNum])
            self.scoreDict[avId] += 1
            self.numTreasuresTaken += 1
            if self.numTreasuresTaken >= self.numTreasures:
                self.logAllPerfect()
                self.sendUpdate('allTreasuresTaken', [])
                if not MazeGameGlobals.ENDLESS_GAME:
                    self.gameFSM.request('waitShowScores')
            return

    def timerExpired(self, task):
        self.notify.debug('timer expired')
        if not MazeGameGlobals.ENDLESS_GAME:
            self.gameFSM.request('waitShowScores')
        return Task.done

    def enterWaitShowScores(self):
        self.notify.debug('enterWaitShowScores')
        taskMgr.doMethodLater(MazeGameGlobals.SHOWSCORES_DURATION, self.__doneShowingScores, self.taskName('waitShowScores'))

    def __doneShowingScores(self, task):
        self.notify.debug('doneShowingScores')
        for key in self.scoreDict.keys():
            self.scoreDict[key] = max(1, self.scoreDict[key] / 12)

        if self.numTreasuresTaken >= self.numTreasures:
            for key in self.scoreDict.keys():
                self.scoreDict[key] += 8

        self.gameOver()
        return Task.done

    def exitWaitShowScores(self):
        taskMgr.remove(self.taskName('waitShowScores'))

    def enterCleanup(self):
        self.notify.debug('enterCleanup')
        del self.takenTable
        self.gameFSM.request('inactive')

    def exitCleanup(self):
        pass