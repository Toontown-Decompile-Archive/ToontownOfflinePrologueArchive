# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.level.EditMgrAI
# Compiled at: 2014-04-30 09:53:54
import EditMgrBase
if __dev__:
    from direct.showbase.PythonUtil import list2dict
    import EditorGlobals

class EditMgrAI(EditMgrBase.EditMgrBase):
    if __dev__:

        def setRequestNewEntity(self, data):
            spec = self.level.levelSpec
            entIds = spec.getAllEntIds()
            entIdDict = list2dict(entIds)
            allocRange = EditorGlobals.getEntIdAllocRange()
            if not hasattr(self, 'lastAllocatedEntId'):
                self.lastAllocatedEntId = allocRange[0]
            idChosen = 0
            while not idChosen:
                for id in xrange(self.lastAllocatedEntId, allocRange[1]):
                    print id
                    if id not in entIdDict:
                        idChosen = 1
                        break
                else:
                    if self.lastAllocatedEntId != allocRange[0]:
                        self.lastAllocatedEntId = allocRange[0]
                    else:
                        self.notify.error('out of entIds')

            data.update({'entId': id})
            self.lastAllocatedEntId = id
            self.level.setAttribChange(self.entId, 'insertEntity', data)
            self.level.levelSpec.doSetAttrib(self.entId, 'requestNewEntity', None)
            return

        def getSpecSaveEvent(self):
            return 'requestSave-%s' % self.level.levelId

        def setRequestSave(self, data):
            messenger.send(self.getSpecSaveEvent())
            self.level.levelSpec.doSetAttrib(self.entId, 'requestSave', None)
            return