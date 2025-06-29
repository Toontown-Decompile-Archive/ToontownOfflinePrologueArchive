# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.DistributedMinigamePhysicsWorld
# Compiled at: 2014-04-30 09:53:54
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from toontown.minigame import MinigamePhysicsWorldBase

class DistributedMinigamePhysicsWorld(DistributedObject.DistributedObject, MinigamePhysicsWorldBase.MinigamePhysicsWorldBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedMinigamePhysicsWorld')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        MinigamePhysicsWorldBase.MinigamePhysicsWorldBase.__init__(self, canRender=1)

    def delete(self):
        MinigamePhysicsWorldBase.MinigamePhysicsWorldBase.delete(self)
        DistributedObject.DistributedObject.delete(self)