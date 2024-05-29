# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.status.StatusDatabase
# Compiled at: 2014-04-30 09:53:54
import datetime, time
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from direct.directnotify.DirectNotifyGlobal import directNotify
from otp.otpbase import OTPLocalizer

class StatusDatabase(DistributedObjectGlobal):
    notify = directNotify.newCategory('StatusDatabase')

    def __init__(self, cr):
        DistributedObjectGlobal.__init__(self, cr)
        self.avatarData = {}
        self.avatarQueue = []
        self.avatarRequestTaskName = 'StatusDataBase_RequestAvatarLastOnline'
        self.avatarRetreiveTaskName = 'StatusDataBase_GetAvatarLastOnline'
        self.avatarDoneTaskName = 'StatusDataBase GotAvatarData'

    def requestOfflineAvatarStatus(self, avIds):
        self.notify.debugCall()
        self.sendUpdate('requestOfflineAvatarStatus', [avIds])

    def queueOfflineAvatarStatus(self, avIds):
        for avId in avIds:
            if avId not in self.avatarQueue:
                self.avatarQueue.append(avId)

        while taskMgr.hasTaskNamed(self.avatarRequestTaskName):
            taskMgr.remove(self.avatarRequestTaskName)

        task = taskMgr.doMethodLater(1.0, self.requestAvatarQueue, self.avatarRequestTaskName)

    def requestAvatarQueue(self, task):
        self.sendUpdate('requestOfflineAvatarStatus', [self.avatarQueue])
        self.avatarQueue = []

    def recvOfflineAvatarStatus(self, avId, lastOnline):
        self.notify.debugCall()
        self.notify.debug('Got an update for offline avatar %s who was last online %s' % (avId, self.lastOnlineString(lastOnline)))
        self.avatarData[avId] = lastOnline
        while taskMgr.hasTaskNamed(self.avatarRetreiveTaskName):
            taskMgr.remove(self.avatarRetreiveTaskName)

        task = taskMgr.doMethodLater(1.0, self.announceNewAvatarData, self.avatarRetreiveTaskName)

    def announceNewAvatarData(self, task):
        messenger.send(self.avatarDoneTaskName)

    def lastOnlineString(self, timestamp):
        if timestamp == 0:
            return ''
        now = datetime.datetime.utcnow()
        td = abs(now - datetime.datetime.fromtimestamp(timestamp))
        return OTPLocalizer.timeElapsedString(td)