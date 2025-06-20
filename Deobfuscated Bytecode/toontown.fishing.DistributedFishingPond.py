# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.fishing.DistributedFishingPond
# Compiled at: 2014-04-30 09:53:54
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
import FishGlobals
from toontown.fishing import DistributedPondBingoManager
from pandac.PandaModules import Vec3
from direct.task import Task

class DistributedFishingPond(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFishingPond')
    pollInterval = 0.5

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.notify.debug('init')
        self.targets = {}
        self.area = None
        self.localToonBobPos = None
        self.localToonSpot = None
        self.pondBingoMgr = None
        self.visitedSpots = {}
        return

    def disable(self):
        self.visitedSpots.clear()
        self.stopCheckingTargets()
        DistributedObject.DistributedObject.disable(self)

    def setArea(self, area):
        self.area = area

    def getArea(self):
        return self.area

    def addTarget(self, target):
        self.notify.debug('addTarget: %s' % target)
        self.targets[target.getDoId()] = target

    def removeTarget(self, target):
        self.notify.debug('removeTarget: %s' % target)
        del self.targets[target.getDoId()]

    def startCheckingTargets(self, spot, bobPos):
        self.notify.debug('startCheckingTargets')
        if base.wantBingo:
            pass
        self.localToonSpot = spot
        self.localToonBobPos = bobPos
        taskMgr.doMethodLater(self.pollInterval * 2, self.checkTargets, self.taskName('checkTargets'))

    def stopCheckingTargets(self):
        self.notify.debug('stopCheckingTargets')
        taskMgr.remove(self.taskName('checkTargets'))
        if not base.wantBingo:
            self.localToonSpot = None
        self.localToonBobPos = None
        return

    def checkTargets(self, task=None):
        self.notify.debug('checkTargets')
        if self.localToonSpot != None:
            for target in self.targets.values():
                targetPos = target.getPos(render)
                distVec = Vec3(targetPos - self.localToonBobPos)
                dist = distVec.length()
                if dist < target.getRadius():
                    self.notify.debug('checkTargets: hit target: %s' % target.getDoId())
                    self.d_hitTarget(target)
                    return Task.done

            taskMgr.doMethodLater(self.pollInterval, self.checkTargets, self.taskName('checkTargets'))
        else:
            self.notify.warning('localToonSpot became None while checking targets')
        return Task.done

    def d_hitTarget(self, target):
        self.localToonSpot.hitTarget()
        self.sendUpdate('hitTarget', [target.getDoId()])

    def setPondBingoManager(self, pondBingoMgr):
        self.pondBingoMgr = pondBingoMgr

    def removePondBingoManager(self):
        del self.pondBingoMgr
        self.pondBingoMgr = None
        return

    def getPondBingoManager(self):
        return self.pondBingoMgr

    def hasPondBingoManager(self):
        return (self.pondBingoMgr and [1] or [0])[0]

    def handleBingoCatch(self, catch):
        if self.pondBingoMgr:
            self.pondBingoMgr.setLastCatch(catch)

    def handleBingoBoot(self):
        if self.pondBingoMgr:
            self.pondBingoMgr.handleBoot()

    def cleanupBingoMgr(self):
        if self.pondBingoMgr:
            self.pondBingoMgr.cleanup()

    def setLocalToonSpot(self, spot=None):
        self.localToonSpot = spot
        if spot is not None and not self.visitedSpots.has_key(spot.getDoId()):
            self.visitedSpots[spot.getDoId()] = spot
        return

    def showBingoGui(self):
        if self.pondBingoMgr:
            self.pondBingoMgr.showCard()

    def getLocalToonSpot(self):
        return self.localToonSpot

    def resetSpotGui(self):
        for spot in self.visitedSpots.values():
            spot.resetCastGui()

    def setSpotGui(self):
        for spot in self.visitedSpots.values():
            spot.setCastGui()