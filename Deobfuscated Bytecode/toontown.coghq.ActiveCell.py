# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.ActiveCell
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from otp.level import BasicEntities
from direct.directnotify import DirectNotifyGlobal

class ActiveCell(BasicEntities.DistributedNodePathEntity):
    notify = DirectNotifyGlobal.directNotify.newCategory('ActiveCell')

    def __init__(self, cr):
        BasicEntities.DistributedNodePathEntity.__init__(self, cr)
        self.occupantId = -1
        self.state = 0

    def announceGenerate(self):
        BasicEntities.DistributedNodePathEntity.announceGenerate(self)
        self.loadModel()

    def loadModel(self):
        if 0 and __debug__:
            grid = self.level.entities.get(self.gridId, None)
            if grid:
                pos = grid.getPos() + Vec3(self.col * grid.cellSize, self.row * grid.cellSize, 0)
                model = loader.loadModel('phase_5/models/modules/suit_walls')
                model.setScale(grid.cellSize, 1, grid.cellSize)
                model.setP(-90)
                model.flattenMedium()
                model.setZ(0.05)
                model.setColorScale(1, 0, 0, 0.5)
                model.copyTo(self)
                self.setPos(pos)
        return

    def setState(self, state, objId):
        self.state = state
        self.occupantId = objId

    if __dev__:

        def attribChanged(self, *args):
            model = self.find('*')
            if not model.isEmpty():
                model.removeNode()
            self.loadModel()