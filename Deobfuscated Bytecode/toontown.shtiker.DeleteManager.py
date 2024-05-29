# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.shtiker.DeleteManager
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal

class DeleteManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DeleteManager')
    neverDisable = 1

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    def generate(self):
        DistributedObject.DistributedObject.generate(self)
        self.accept('deleteItems', self.d_setInventory)

    def disable(self):
        self.ignore('deleteItems')
        DistributedObject.DistributedObject.disable(self)

    def d_setInventory(self, newInventoryString):
        self.sendUpdate('setInventory', [newInventoryString])