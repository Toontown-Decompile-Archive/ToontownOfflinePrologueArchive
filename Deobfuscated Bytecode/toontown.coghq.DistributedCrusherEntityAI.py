# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.DistributedCrusherEntityAI
# Compiled at: 2014-04-30 09:53:54
from otp.level import DistributedEntityAI
from direct.directnotify import DirectNotifyGlobal

class DistributedCrusherEntityAI(DistributedEntityAI.DistributedEntityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCrusherEntityAI')

    def __init__(self, level, entId):
        self.isCrusher = 0
        self.crushCell = None
        DistributedEntityAI.DistributedEntityAI.__init__(self, level, entId)
        self.crushMsg = self.getUniqueName('crusherDoCrush')
        return

    def generate(self):
        DistributedEntityAI.DistributedEntityAI.generate(self)
        self.setActiveCrushCell()

    def delete(self):
        self.ignoreAll()
        DistributedEntityAI.DistributedEntityAI.delete(self)

    def destroy(self):
        self.notify.info('destroy entity %s' % self.entId)
        if self.crushCell != None:
            self.crushCell.unregisterCrusher(self.entId)
            self.crushCell = None
        DistributedEntityAI.DistributedEntityAI.destroy(self)
        return

    def setActiveCrushCell(self):
        self.notify.debug('setActiveCrushCell, entId: %d' % self.entId)
        if self.crushCellId != None:
            self.crushCell = self.level.entities.get(self.crushCellId, None)
            if self.crushCell == None:
                self.accept(self.level.getEntityCreateEvent(self.crushCellId), self.setActiveCrushCell)
            else:
                self.isCrusher = 1
                self.crushCell.registerCrusher(self.entId)
        return

    def sendCrushMsg(self, axis=0):
        if self.isCrusher:
            messenger.send(self.crushMsg, [self.entId, axis])

    def getPosition(self):
        if hasattr(self, 'pos'):
            return self.pos