# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.suit.DistributedGridGoon
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from toontown.battle.BattleProps import *
from direct.directnotify import DirectNotifyGlobal
import DistributedGoon
from toontown.toonbase import ToontownGlobals
from toontown.coghq import MovingPlatform

class DistributedGridGoon(DistributedGoon.DistributedGoon):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedGoon')

    def __init__(self, cr, type='sg'):
        try:
            self.DistributedGridGoon_initialized
        except:
            self.DistributedGridGoon_initialized = 1
            DistributedGoon.DistributedGoon.__init__(self, cr, type)

    def generate(self):
        DistributedGoon.DistributedGoon.generate(self)
        self.ignore(self.uniqueName('wallHit'))
        self.mazeWalkTrack = None
        return

    def delete(self):
        if self.mazeWalkTrack:
            self.mazeWalkTrack.pause()
            del self.mazeWalkTrack
        DistributedGoon.DistributedGoon.delete(self)

    def setH(self, h):
        self.h = h

    def setPathPts(self, xi, yi, zi, xf, yf, zf):
        self.notify.debug('setPathPts')
        if self.mazeWalkTrack:
            self.mazeWalkTrack.pause()
            del self.mazeWalkTrack
            self.mazeWalkTrack = None
        curPos = Point3(xi, yi, zi)
        nextPos = Point3(xf, yf, zf)
        distance = Vec3(curPos - nextPos).length()
        duration = distance / self.velocity
        self.mazeWalkTrack = Sequence(Func(self.headsUp, nextPos[0], nextPos[1], nextPos[2]), LerpPosInterval(self, duration=duration, pos=nextPos, startPos=curPos), name=self.uniqueName('mazeWalkTrack'))
        self.mazeWalkTrack.start()
        return

    def enterWalk(self, avId=None, ts=0):
        pass

    def exitWalk(self):
        pass