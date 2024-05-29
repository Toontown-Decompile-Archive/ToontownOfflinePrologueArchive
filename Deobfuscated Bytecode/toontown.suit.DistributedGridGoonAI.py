# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.suit.DistributedGridGoonAI
# Compiled at: 2014-04-30 09:53:54
from otp.ai.AIBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
from toontown.battle import SuitBattleGlobals
import DistributedGoonAI
from direct.task.Task import Task
from toontown.coghq import DistributedCrushableEntityAI
import random

class DistributedGridGoonAI(DistributedGoonAI.DistributedGoonAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedGridGoonAI')

    def __init__(self, level, entId):
        self.grid = None
        self.h = 0
        DistributedGoonAI.DistributedGoonAI.__init__(self, level, entId)
        return

    def generate(self):
        self.notify.debug('generate')
        DistributedCrushableEntityAI.DistributedCrushableEntityAI.generate(self)

    def initGridDependents(self):
        taskMgr.doMethodLater(2, self.goToNextPoint, self.taskName('walkTask'))

    def getPosition(self):
        if self.grid:
            return self.grid.getObjPos(self.entId)

    def getH(self):
        return self.h

    def goToNextPoint(self, task):
        if not self.grid:
            self.notify.warning("couldn't find grid, not starting")
            return
        if self.grid.checkMoveDir(self.entId, self.h):
            ptA = Point3(*self.getPosition())
            self.grid.doMoveDir(self.entId, self.h)
            ptB = Point3(*self.getPosition())
            self.sendUpdate('setPathPts', [ptA[0],
             ptA[1],
             ptA[2],
             ptB[0],
             ptB[1],
             ptB[2]])
            tPathSegment = Vec3(ptA - ptB).length() / self.velocity
        else:
            turn = int(random.randrange(1, 4) * 90)
            self.h = (self.h + turn) % 360
            tPathSegment = 0.1
        taskMgr.doMethodLater(tPathSegment, self.goToNextPoint, self.taskName('walkTask'))
        return Task.done