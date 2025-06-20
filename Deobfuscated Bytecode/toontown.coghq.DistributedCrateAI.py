# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.DistributedCrateAI
# Compiled at: 2014-04-30 09:53:54
from CrateGlobals import *
from direct.directnotify import DirectNotifyGlobal
import DistributedCrushableEntityAI
from direct.task import Task
import CrateGlobals

class DistributedCrateAI(DistributedCrushableEntityAI.DistributedCrushableEntityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCrateAI')

    def __init__(self, level, entId):
        DistributedCrushableEntityAI.DistributedCrushableEntityAI.__init__(self, level, entId)
        self.grid = None
        self.avId = 0
        self.tPowerUp = 0
        self.width = 2
        return

    def generate(self):
        DistributedCrushableEntityAI.DistributedCrushableEntityAI.generate(self)

    def delete(self):
        taskMgr.remove(self.taskName('sendPush'))
        DistributedCrushableEntityAI.DistributedCrushableEntityAI.delete(self)

    def requestPush(self, side):
        self.notify.debug('requestPush')
        avId = self.air.getAvatarIdFromSender()
        if side not in (0, 1, 2, 3):
            self.air.writeServerEvent('suspicious', avId=avId, issue='DistributedCrateAI.requestPush given invalid side arg')
            return
        if not self.avId and self.grid.checkPush(self.entId, side):
            self.avId = avId
            self.side = side
            self.acceptOnce(self.air.getAvatarExitEvent(avId), self.__handleUnexpectedExit, extraArgs=[avId])
            taskMgr.remove(self.taskName('sendPush'))
            taskMgr.doMethodLater(self.tPowerUp, self.sendPushTask, self.taskName('sendPush'))
        else:
            self.sendUpdateToAvatarId(avId, 'setReject', [])

    def setDone(self):
        self.notify.debug('setDone')
        avId = self.air.getAvatarIdFromSender()
        if avId == self.avId:
            taskMgr.remove(self.taskName('sendPush'))
            self.avId = 0

    def sendPushTask(self, task):
        self.notify.debug('sendPushTask')
        oldPos = self.grid.getObjPos(self.entId)
        if self.grid.doPush(self.entId, self.side):
            newPos = self.grid.getObjPos(self.entId)
            self.sendUpdate('setMoveTo', [self.avId,
             oldPos[0],
             oldPos[1],
             oldPos[2],
             newPos[0],
             newPos[1],
             newPos[2]])
            taskMgr.doMethodLater(CrateGlobals.T_PUSH + CrateGlobals.T_PAUSE, self.sendPushTask, self.taskName('sendPush'))
        else:
            taskMgr.remove(self.taskName('sendPush'))
            self.sendUpdateToAvatarId(self.avId, 'setReject', [])
            self.avId = 0
        return Task.done

    def updateGrid(self):
        pass

    def doCrush(self, crusherId, axis):
        DistributedCrushableEntityAI.DistributedCrushableEntityAI.doCrush(self, crusherId, axis)

    def setGridId(self, gridId):
        self.gridId = gridId
        grid = self.level.entities.get(gridId, None)
        if grid:
            self.grid = grid
            self.grid.addObjectByPos(self.entId, self.pos, width=2)
            self.b_setPosition(self.getPosition())
        return

    def __handleUnexpectedExit(self, avId):
        self.notify.warning('avatar:' + str(avId) + ' has exited unexpectedly')
        if self.avId == avId:
            self.avId = 0