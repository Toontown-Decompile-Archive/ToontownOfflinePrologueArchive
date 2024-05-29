# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.speedchat.SpeedChat
# Compiled at: 2014-04-30 09:53:54
from direct.showbase.PythonUtil import boolEqual
from SpeedChatTypes import *
from SCSettings import SCSettings
from SCTerminal import SCWhisperModeChangeEvent
from otp.otpbase import OTPLocalizer

class SpeedChat(SCMenu):

    def __init__(self, name='', structure=None, backgroundModelName=None, guiModelName=None):
        SCMenu.BackgroundModelName = backgroundModelName
        SCMenu.GuiModelName = guiModelName
        SCMenu.__init__(self)
        self.name = name
        self.settings = SCSettings(eventPrefix=self.name)
        self.privSetSettingsRef(self.settings)
        if structure is not None:
            self.rebuildFromStructure(structure)
        self._lastTransform = None
        return

    def destroy(self):
        if self.isVisible():
            self.exitVisible()
        self._lastTransform = None
        SCMenu.destroy(self)
        return

    def __str__(self):
        return "%s: '%s'" % (self.__class__.__name__, self.name)

    def enter(self):
        self._detectTransformChange()
        self.enterVisible()

    def exit(self):
        self.exitVisible()

    def _detectTransformChange(self):
        newTransform = self.getTransform(aspect2d)
        if self._lastTransform is not None:
            if newTransform != self._lastTransform:
                self.invalidateAll()
        self._lastTransform = newTransform
        return

    def setWhisperMode(self, whisperMode):
        if not boolEqual(self.settings.whisperMode, whisperMode):
            self.settings.whisperMode = whisperMode
            messenger.send(self.getEventName(SCWhisperModeChangeEvent), [whisperMode])

    def setColorScheme(self, colorScheme):
        self.settings.colorScheme = colorScheme
        self.invalidateAll()

    def setSubmenuOverlap(self, submenuOverlap):
        self.settings.submenuOverlap = submenuOverlap
        self.invalidateAll()

    def setTopLevelOverlap(self, topLevelOverlap):
        self.settings.topLevelOverlap = topLevelOverlap
        self.invalidateAll()

    def finalizeAll(self):
        self.notify.debug('finalizing entire SpeedChat tree')
        self._detectTransformChange()
        SCMenu.finalizeAll(self)