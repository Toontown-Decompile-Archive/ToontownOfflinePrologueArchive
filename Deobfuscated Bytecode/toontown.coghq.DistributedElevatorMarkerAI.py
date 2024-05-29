# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.DistributedElevatorMarkerAI
# Compiled at: 2014-04-30 09:53:54
from otp.ai.AIBase import *
from direct.interval.IntervalGlobal import *
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import ClockDelta
from direct.task import Task
from otp.level import DistributedEntityAI
from otp.level import BasicEntities
from direct.directnotify import DirectNotifyGlobal

class DistributedElevatorMarkerAI(DistributedEntityAI.DistributedEntityAI, NodePath, BasicEntities.NodePathAttribs):

    def __init__(self, level, entId):
        DistributedEntityAI.DistributedEntityAI.__init__(self, level, entId)
        node = hidden.attachNewNode('DistributedElevatorMarkerAI')
        NodePath.__init__(self, node)

    def generate(self):
        DistributedEntityAI.DistributedEntityAI.generate(self)
        self.setPos(self.pos)
        self.setHpr(self.hpr)

    def delete(self):
        self.ignoreAll()
        DistributedEntityAI.DistributedEntityAI.delete(self)

    def destroy(self):
        self.notify.info('destroy entity(elevatorMaker) %s' % self.entId)
        DistributedEntityAI.DistributedEntityAI.destroy(self)