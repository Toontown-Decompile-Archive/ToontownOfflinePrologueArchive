# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.level.EntityCreator
# Compiled at: 2014-04-30 09:53:54
import CutScene, EntityCreatorBase, BasicEntities
from direct.directnotify import DirectNotifyGlobal
import EditMgr, EntrancePoint, LevelMgr, LogicGate, ZoneEntity, ModelEntity, PathEntity, VisibilityExtender, PropSpinner, AmbientSound, LocatorEntity, CollisionSolidEntity

def nothing(*args):
    return 'nothing'


def nonlocal(*args):
    return 'nonlocal'


class EntityCreator(EntityCreatorBase.EntityCreatorBase):

    def __init__(self, level):
        EntityCreatorBase.EntityCreatorBase.__init__(self, level)
        self.level = level
        self.privRegisterTypes({'attribModifier': nothing, 'ambientSound': AmbientSound.AmbientSound, 
           'collisionSolid': CollisionSolidEntity.CollisionSolidEntity, 
           'cutScene': CutScene.CutScene, 
           'editMgr': EditMgr.EditMgr, 
           'entityGroup': nothing, 
           'entrancePoint': EntrancePoint.EntrancePoint, 
           'levelMgr': LevelMgr.LevelMgr, 
           'locator': LocatorEntity.LocatorEntity, 
           'logicGate': LogicGate.LogicGate, 
           'model': ModelEntity.ModelEntity, 
           'nodepath': BasicEntities.NodePathEntity, 
           'path': PathEntity.PathEntity, 
           'propSpinner': PropSpinner.PropSpinner, 
           'visibilityExtender': VisibilityExtender.VisibilityExtender, 
           'zone': ZoneEntity.ZoneEntity})

    def doCreateEntity(self, ctor, entId):
        return ctor(self.level, entId)