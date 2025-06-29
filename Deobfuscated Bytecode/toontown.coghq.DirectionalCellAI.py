# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.DirectionalCellAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
import ActiveCellAI, CrateGlobals
from direct.task import Task

class DirectionalCellAI(ActiveCellAI.ActiveCellAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DirectionalCellAI')

    def __init__(self, level, entId):
        self.dir = [
         0, 0]
        ActiveCellAI.ActiveCellAI.__init__(self, level, entId)
        self.moveTrack = None
        return

    def delete(self):
        if self.moveTrack:
            self.moveTrack.pause()
            del self.moveTrack
            self.moveTrack = None
        taskMgr.remove(self.taskName('moveTask'))
        return

    def setState(self, state, objId=None):
        ActiveCellAI.ActiveCellAI.setState(self, state, objId)
        self.startMoveTask()

    def taskName(self, name):
        return self.level.taskName(name) + '-' + str(self.entId)

    def startMoveTask(self):
        taskMgr.remove(self.taskName('moveTask'))
        taskMgr.doMethodLater(CrateGlobals.T_PUSH + CrateGlobals.T_PAUSE, self.moveTask, self.taskName('moveTask'))

    def moveTask(self, task):
        oldPos = self.grid.getObjPos(self.occupantId)
        if self.grid.doMove(self.occupantId, self.dir[0], self.dir[1]):
            newPos = self.grid.getObjPos(self.occupantId)
            crate = simbase.air.doId2do.get(self.occupantId)
            if crate:
                crate.sendUpdate('setMoveTo', [oldPos[0],
                 oldPos[1],
                 oldPos[2],
                 newPos[0],
                 newPos[1],
                 newPos[2]])
        return Task.done