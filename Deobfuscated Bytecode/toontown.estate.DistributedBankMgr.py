# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.estate.DistributedBankMgr
# Compiled at: 2014-04-30 09:53:54
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer

class DistributedBankMgr(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBankMgr')
    neverDisable = 1

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    def generate(self):
        if base.cr.bankManager != None:
            base.cr.bankManager.delete()
        base.cr.bankManager = self
        DistributedObject.DistributedObject.generate(self)
        return

    def disable(self):
        base.cr.bankManager = None
        DistributedObject.DistributedObject.disable(self)
        return

    def delete(self):
        base.cr.bankManager = None
        DistributedObject.DistributedObject.delete(self)
        return

    def d_transferMoney(self, amount):
        self.sendUpdate('transferMoney', [amount])