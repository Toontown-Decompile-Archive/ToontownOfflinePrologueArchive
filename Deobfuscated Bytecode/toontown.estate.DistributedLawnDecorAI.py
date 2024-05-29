# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.estate.DistributedLawnDecorAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedNodeAI import DistributedNodeAI

class DistributedLawnDecorAI(DistributedNodeAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedLawnDecorAI')

    def __init__(self, mgr):
        self.mgr = mgr
        DistributedNodeAI.__init__(self, self.mgr.air)
        self.plot = 0
        self.ownerIndex = 0

    def setPlot(self, plot):
        self.plot = plot

    def getPlot(self):
        return self.plot

    def getHeading(self):
        return self.getH()

    def getPosition(self):
        return self.getPos()

    def setOwnerIndex(self, ownerIndex):
        self.ownerIndex = ownerIndex
        self.ownerDoId = self.mgr.gardenMgr.mgr.toons[ownerIndex]
        self.owner = self.air.doId2do.get(self.ownerDoId)

    def getOwnerIndex(self):
        return self.ownerIndex

    def d_setMovie(self, mode, avId=None):
        if avId is None:
            avId = self.air.getAvatarIdFromSender()
        self.sendUpdate('setMovie', [mode, avId])
        return

    def d_interactionDenied(self):
        self.sendUpdate('interactionDenied', [self.air.getAvatarIdFromSender()])