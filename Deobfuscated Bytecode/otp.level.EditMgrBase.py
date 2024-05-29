# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.level.EditMgrBase
# Compiled at: 2014-04-30 09:53:54
import Entity
from direct.directnotify import DirectNotifyGlobal

class EditMgrBase(Entity.Entity):
    notify = DirectNotifyGlobal.directNotify.newCategory('EditMgr')

    def __init__(self, level, entId):
        Entity.Entity.__init__(self, level, entId)

    def destroy(self):
        Entity.Entity.destroy(self)
        self.ignoreAll()

    if __dev__:

        def setInsertEntity(self, data):
            self.level.setEntityCreatorUsername(data['entId'], data['username'])
            self.level.levelSpec.insertEntity(data['entId'], data['entType'], data['parentEntId'])
            self.level.levelSpec.doSetAttrib(self.entId, 'insertEntity', None)
            return

        def setRemoveEntity(self, data):
            self.level.levelSpec.removeEntity(data['entId'])
            self.level.levelSpec.doSetAttrib(self.entId, 'removeEntity', None)
            return