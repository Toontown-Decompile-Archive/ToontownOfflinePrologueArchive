# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.level.VisibilityBlocker
# Compiled at: 2014-04-30 09:53:54
import Entity

class VisibilityBlocker:

    def __init__(self):
        self.__nextSetZoneDoneEvent = None
        return

    def destroy(self):
        self.cancelUnblockVis()

    def requestUnblockVis(self):
        if self.__nextSetZoneDoneEvent is None:
            self.__nextSetZoneDoneEvent = self.level.cr.getNextSetZoneDoneEvent()
            self.acceptOnce(self.__nextSetZoneDoneEvent, self.okToUnblockVis)
            self.level.forceSetZoneThisFrame()
        return

    def cancelUnblockVis(self):
        if self.__nextSetZoneDoneEvent is not None:
            self.ignore(self.__nextSetZoneDoneEvent)
            self.__nextSetZoneDoneEvent = None
        return

    def isWaitingForUnblockVis(self):
        return self.__nextSetZoneDoneEvent is not None

    def okToUnblockVis(self):
        self.cancelUnblockVis()