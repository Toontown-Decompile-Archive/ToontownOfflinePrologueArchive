# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.ActiveCellAI
# Compiled at: 2014-04-30 09:53:54
from otp.level import DistributedEntityAI
from direct.directnotify import DirectNotifyGlobal

class ActiveCellAI(DistributedEntityAI.DistributedEntityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('ActiveCellAI')

    def __init__(self, level, entId):
        self.state = 0
        self.grid = None
        self.occupantIds = []
        DistributedEntityAI.DistributedEntityAI.__init__(self, level, entId)

        def setGrid(gridId=self.gridId, self=self):
            self.grid = self.level.entities.get(gridId, None)
            if self.grid:
                self.grid.addActiveCell(self)
                return 1
            else:
                return 0

        if not setGrid():
            self.accept(self.level.getEntityCreateEvent(self.gridId), setGrid)
        return

    def generate(self):
        DistributedEntityAI.DistributedEntityAI.generate(self)

    def delete(self):
        self.notify.debug('delete')
        self.ignoreAll()
        DistributedEntityAI.DistributedEntityAI.delete(self)

    def getState(self):
        return self.state

    def b_setState(self, state, objId=None):
        self.setState(state, objId)
        self.d_setState(state, objId)

    def d_setState(self, state, objId=None):
        if not objId:
            objId = 0
        self.sendUpdate('setState', [state, objId])

    def setState(self, state, objId=None):
        self.state = state
        if state:
            self.occupantIds.append(objId)
        else:
            try:
                self.occupantIds.remove(objId)
            except:
                self.notify.warning("couldn't remove %s from active cell" % objId)

    def getRowCol(self):
        return [
         self.row, self.col]