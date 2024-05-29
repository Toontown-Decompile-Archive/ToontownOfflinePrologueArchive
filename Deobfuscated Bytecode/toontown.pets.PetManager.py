# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.pets.PetManager
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from toontown.toonbase import ToontownGlobals
from direct.task import Task

def acquirePetManager():
    if not hasattr(base, 'petManager'):
        PetManager()
    base.petManager.incRefCount()


def releasePetManager():
    base.petManager.decRefCount()


class PetManager:
    CollTaskName = 'petFloorCollisions'

    def __init__(self):
        base.petManager = self
        self.refCount = 0
        self.cTrav = CollisionTraverser('petFloorCollisions')
        taskMgr.add(self._doCollisions, PetManager.CollTaskName, priority=ToontownGlobals.PetFloorCollPriority)

    def _destroy(self):
        taskMgr.remove(PetManager.CollTaskName)
        del self.cTrav

    def _doCollisions(self, task):
        self.cTrav.traverse(render)
        return Task.cont

    def incRefCount(self):
        self.refCount += 1

    def decRefCount(self):
        self.refCount -= 1
        if self.refCount == 0:
            self._destroy()
            del base.petManager