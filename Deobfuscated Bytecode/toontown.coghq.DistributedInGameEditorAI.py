# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.DistributedInGameEditorAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObjectAI
from direct.directutil import DistributedLargeBlobSenderAI
from SpecImports import *

class DistributedInGameEditorAI(DistributedObjectAI.DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedInGameEditorAI')

    def __init__(self, air, level, editorAvId, editUsername):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.editorAvId = editorAvId
        self.editUsername = editUsername
        self.level = level
        self.levelDoId = self.level.getDoId()
        self.generateWithRequired(level.zoneId)

    def generate(self):
        self.notify.debug('generate')
        DistributedObjectAI.DistributedObjectAI.generate(self)
        simbase.levelEditor = self
        self.acceptOnce(self.air.getAvatarExitEvent(self.editorAvId), self.setFinished)
        self.accept(self.level.getAttribChangeEventName(), self.handleAttribChange)

    def delete(self):
        self.notify.debug('delete')
        messenger.send(self.getDoneEvent())
        DistributedObjectAI.DistributedObjectAI.delete(self)
        self.ignoreAll()

    def getDoneEvent(self):
        return self.uniqueName('levelEditorDone')

    def getEditorAvId(self):
        return self.editorAvId

    def getEditUsername(self):
        return self.editUsername

    def getLevelDoId(self):
        return self.levelDoId

    def requestCurrentLevelSpec(self):
        print 'requestCurrentLevelSpec'
        spec = self.level.levelSpec
        specStr = repr(spec)
        largeBlob = DistributedLargeBlobSenderAI.DistributedLargeBlobSenderAI(self.air, self.zoneId, self.editorAvId, specStr, useDisk=config.GetBool('spec-by-disk', 1))
        self.sendUpdateToAvatarId(self.editorAvId, 'setSpecSenderDoId', [largeBlob.doId])

    def setEdit(self, entId, attribName, valueStr, username):
        self.level.setAttribChange(entId, attribName, eval(valueStr), username)

    def handleAttribChange(self, entId, attrib, value, username):
        self.sendUpdateToAvatarId(self.editorAvId, 'setAttribChange', [entId,
         attrib,
         repr(value),
         username])

    def setFinished(self):
        self.requestDelete()