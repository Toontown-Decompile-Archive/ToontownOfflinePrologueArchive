# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.racing.DistributedKartPadAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedKartPadAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedKartPadAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.air = air
        self.startingBlocks = []
        self.area = None
        return

    def setArea(self, area):
        self.area = area

    def d_setArea(self, area):
        self.sendUpdate('setArea', [area])

    def b_setArea(self, area):
        self.setArea(area)
        self.d_setArea(self, area)

    def getArea(self):
        return self.area

    def addStartingBlock(self, block):
        self.startingBlocks.append(block)

    def updateMovieState(self):
        pass

    def removeStartingBlock(self, block):
        if self.startingBlocks.count(block):
            self.startingBlocks.remove(block)