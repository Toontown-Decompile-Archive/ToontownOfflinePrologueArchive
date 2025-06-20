# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.distributed.ToontownDistrictStats
# Compiled at: 2014-04-30 09:53:54
from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from direct.task import Task
from direct.distributed import DoInterestManager
from otp.distributed.OtpDoGlobals import *
_ToonTownDistrictStatInterest = None
_ToonTownDistrictStatInterestComplete = 0
_trashObject = DirectObject.DirectObject()

def EventName():
    return 'ShardPopulationSet'


def isOpen():
    global _ToonTownDistrictStatInterest
    return _ToonTownDistrictStatInterest is not None


def isComplete():
    global _ToonTownDistrictStatInterestComplete
    return _ToonTownDistrictStatInterestComplete


def open(event=None):
    global _ToonTownDistrictStatInterest
    global _trashObject
    if not isOpen():

        def _CompleteProc(event):
            global _ToonTownDistrictStatInterestComplete
            _ToonTownDistrictStatInterestComplete = 1
            if event is not None:
                messenger.send(event)
            return

        _trashObject.acceptOnce(EventName(), _CompleteProc)
        _ToonTownDistrictStatInterest = base.cr.addInterest(OTP_DO_ID_TOONTOWN, OTP_ZONE_ID_DISTRICTS_STATS, EventName(), EventName())
    elif isComplete():
        messenger.send(EventName())


def refresh(event=None):
    global _ToonTownDistrictStatInterest
    if isOpen():
        if isComplete():
            messenger.send(EventName())
            if event is not none:
                messenger.send(event)
    else:

        def _CompleteProc(event):
            global _ToonTownDistrictStatInterestComplete
            _ToonTownDistrictStatInterestComplete = 1
            if event is not None:
                messenger.send(event)
            close()
            return

        _trashObject.acceptOnce(EventName(), _CompleteProc, [event])
        _ToonTownDistrictStatInterest = base.cr.addInterest(OTP_DO_ID_TOONTOWN, OTP_ZONE_ID_DISTRICTS_STATS, EventName(), EventName())


def close():
    global _ToonTownDistrictStatInterest
    global _ToonTownDistrictStatInterestComplete
    if isOpen():
        _ToonTownDistrictStatInterestComplete = 0
        base.cr.removeInterest(_ToonTownDistrictStatInterest, None)
        _ToonTownDistrictStatInterest = None
    return


class ToontownDistrictStats(DistributedObject.DistributedObject):
    neverDisable = 1

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.toontownDistrictId = 0

    def settoontownDistrictId(self, value):
        self.toontownDistrictId = value

    def setAvatarCount(self, avatarCount):
        if self.cr.activeDistrictMap.has_key(self.toontownDistrictId):
            self.cr.activeDistrictMap[self.toontownDistrictId].avatarCount = avatarCount

    def setNewAvatarCount(self, newAvatarCount):
        if self.cr.activeDistrictMap.has_key(self.toontownDistrictId):
            self.cr.activeDistrictMap[self.toontownDistrictId].newAvatarCount = newAvatarCount

    def setStats(self, avatarCount, newAvatarCount):
        self.setAvatarCount(avatarCount)
        self.setNewAvatarCount(newAvatarCount)