# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.speedchat.SCObject
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.showbase.DirectObject import DirectObject

class SCObject(DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('SpeedChat')

    def __init__(self):
        self.settingsRef = None
        self.__visible = 0
        self.__dirty = 1
        return

    def destroy(self):
        self.ignoreAll()
        if self.isVisible():
            self.exitVisible()

    def enterVisible(self):
        self.__visible = 1

    def exitVisible(self):
        self.__visible = 0

    def isVisible(self):
        return self.__visible

    def invalidate(self):
        self.__dirty = 1

    def isDirty(self):
        return self.__dirty

    def validate(self):
        self.__dirty = 0

    def finalize(self):
        pass

    def getEventName(self, name):
        return '%s%s' % (self.settingsRef.eventPrefix, name)

    def getColorScheme(self):
        return self.settingsRef.colorScheme

    def isWhispering(self):
        return self.settingsRef.whisperMode

    def getSubmenuOverlap(self):
        return self.settingsRef.submenuOverlap

    def getTopLevelOverlap(self):
        if self.settingsRef.topLevelOverlap is None:
            return self.getSubmenuOverlap()
        else:
            return self.settingsRef.topLevelOverlap
            return

    def privSetSettingsRef(self, settingsRef):
        self.settingsRef = settingsRef

    def privAdoptSCObject(self, scObj):
        scObj.privSetSettingsRef(self.settingsRef)

    def invalidateAll(self):
        self.invalidate()

    def finalizeAll(self):
        self.finalize()