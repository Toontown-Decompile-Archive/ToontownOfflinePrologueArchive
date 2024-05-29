# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.racing.DistributedKartPad
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObject import DistributedObject

class DistributedKartPad(DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedKartPad')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        self.startingBlocks = []

    def delete(self):
        del self.startingBlocks
        DistributedObject.delete(self)

    def setArea(self, area):
        self.area = area

    def getArea(self):
        return self.area

    def addStartingBlock(self, block):
        self.startingBlocks.append(block)
        self.notify.debug('KartPad %s has added starting block %s' % (self.doId, block.doId))