# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.racing.DistributedViewPad
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import *
from direct.task import Task
from pandac.PandaModules import *
from toontown.racing.DistributedKartPad import DistributedKartPad
from toontown.racing.KartShopGlobals import KartGlobals

class DistributedViewPad(DistributedKartPad):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedViewPad')
    id = 0

    def __init__(self, cr):
        DistributedKartPad.__init__(self, cr)
        self.id = DistributedViewPad.id
        DistributedViewPad.id += 1

    def setLastEntered(self, timeStamp):
        self.timeStamp = timeStamp

    def getTimestamp(self, avId):
        return self.timeStamp

    def addStartingBlock(self, block):
        block.cameraPos = Point3(0, 23, 7)
        block.cameraHpr = Point3(180, -10, 0)
        DistributedKartPad.addStartingBlock(self, block)