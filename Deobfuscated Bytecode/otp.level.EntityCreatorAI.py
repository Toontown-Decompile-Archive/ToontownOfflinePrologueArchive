# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.level.EntityCreatorAI
# Compiled at: 2014-04-30 09:53:54
import EntityCreatorBase, LogicGate, EditMgrAI, LevelMgrAI, ZoneEntityAI
from direct.showbase.PythonUtil import Functor

def createDistributedEntity(AIclass, level, entId, zoneId):
    ent = AIclass(level, entId)
    ent.generateWithRequired(zoneId)
    return ent


def createLocalEntity(AIclass, level, entId, zoneId):
    ent = AIclass(level, entId)
    return ent


def nothing(*args):
    return 'nothing'


class EntityCreatorAI(EntityCreatorBase.EntityCreatorBase):

    def __init__(self, level):
        EntityCreatorBase.EntityCreatorBase.__init__(self, level)
        cLE = createLocalEntity
        self.privRegisterTypes({'attribModifier': nothing, 'ambientSound': nothing, 
           'collisionSolid': nothing, 
           'cutScene': nothing, 
           'editMgr': Functor(cLE, EditMgrAI.EditMgrAI), 
           'entityGroup': nothing, 
           'entrancePoint': nothing, 
           'levelMgr': Functor(cLE, LevelMgrAI.LevelMgrAI), 
           'locator': nothing, 
           'logicGate': Functor(cLE, LogicGate.LogicGate), 
           'model': nothing, 
           'nodepath': nothing, 
           'path': nothing, 
           'propSpinner': nothing, 
           'visibilityExtender': nothing, 
           'zone': Functor(cLE, ZoneEntityAI.ZoneEntityAI)})

    def doCreateEntity(self, ctor, entId):
        zoneId = self.level.getEntityZoneId(entId)
        self.notify.debug('creating entity %s in zone %s' % (entId, zoneId))
        return ctor(self.level, entId, zoneId)