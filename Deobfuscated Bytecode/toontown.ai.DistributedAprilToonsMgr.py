# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.ai.DistributedAprilToonsMgr
# Compiled at: 2014-04-30 09:53:54
from direct.distributed.DistributedObject import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase.AprilToonsGlobals import *
from toontown.toonbase import ToontownGlobals

class DistributedAprilToonsMgr(DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('AprilToonsMgr')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        cr.aprilToonsMgr = self
        self.events = []

    def announceGenerate(self):
        DistributedObject.announceGenerate(self)
        self.d_requestEventsList()

    def d_requestEventsList(self):
        self.notify.debug('Requesting events list from AI.')
        self.sendUpdate('requestEventsList', [])

    def requestEventsListResp(self, eventIds):
        self.events = eventIds
        self.checkActiveEvents()

    def isEventActive(self, eventId):
        if not base.cr.config.GetBool('want-april-toons', False):
            return False
        return eventId in self.events

    def setEventActive(self, eventId, active):
        if active and eventId not in self.events:
            self.events.append(eventId)
        elif not active and eventId in self.events:
            del self.events[eventId]

    def checkActiveEvents(self):
        if self.isEventActive(EventGlobalGravity):
            base.localAvatar.controlManager.currentControls.setGravity(ToontownGlobals.GravityValue * 0.75)