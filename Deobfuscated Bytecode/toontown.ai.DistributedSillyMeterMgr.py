# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.ai.DistributedSillyMeterMgr
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from toontown.ai import DistributedPhaseEventMgr
import time

class DistributedSillyMeterMgr(DistributedPhaseEventMgr.DistributedPhaseEventMgr):
    neverDisable = 1
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSillyMeterMgr')

    def __init__(self, cr):
        DistributedPhaseEventMgr.DistributedPhaseEventMgr.__init__(self, cr)
        cr.SillyMeterMgr = self

    def announceGenerate(self):
        DistributedPhaseEventMgr.DistributedPhaseEventMgr.announceGenerate(self)
        messenger.send('SillyMeterIsRunning', [self.isRunning])

    def delete(self):
        self.notify.debug('deleting SillyMetermgr')
        messenger.send('SillyMeterIsRunning', [False])
        DistributedPhaseEventMgr.DistributedPhaseEventMgr.delete(self)
        if hasattr(self.cr, 'SillyMeterMgr'):
            del self.cr.SillyMeterMgr

    def setCurPhase(self, newPhase):
        DistributedPhaseEventMgr.DistributedPhaseEventMgr.setCurPhase(self, newPhase)
        messenger.send('SillyMeterPhase', [newPhase])

    def setIsRunning(self, isRunning):
        DistributedPhaseEventMgr.DistributedPhaseEventMgr.setIsRunning(self, isRunning)
        messenger.send('SillyMeterIsRunning', [isRunning])

    def getCurPhaseDuration(self):
        if len(self.holidayDates) > 0:
            startHolidayDate = self.holidayDates[self.curPhase]
            if self.curPhase + 1 >= len(self.holidayDates):
                self.notify.error('No end date for phase %' % self.curPhase)
                return -1
            endHolidayDate = self.holidayDates[self.curPhase + 1]
            startHolidayTime = time.mktime(startHolidayDate.timetuple())
            endHolidayTime = time.mktime(endHolidayDate.timetuple())
            holidayDuration = endHolidayTime - startHolidayTime
            if holidayDuration < 0:
                self.notify.error('Duration not set for phase %' % self.curPhase)
                return -1
            return holidayDuration
        else:
            self.notify.warning('Phase dates not yet known')
            return -1

    def getCurPhaseStartDate(self):
        if len(self.holidayDates) > 0:
            return self.holidayDates[self.curPhase]