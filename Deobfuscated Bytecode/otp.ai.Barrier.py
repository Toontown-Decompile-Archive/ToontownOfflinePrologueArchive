# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.ai.Barrier
# Compiled at: 2014-04-30 09:53:54
from otp.ai.AIBase import *
from direct.task import Task
from direct.showbase import DirectObject
import random

class Barrier(DirectObject.DirectObject):
    notify = directNotify.newCategory('Barrier')

    def __init__(self, name, uniqueName, avIdList, timeout, clearedFunc=None, timeoutFunc=None, doneFunc=None):
        self.name = name
        self.uniqueName = uniqueName + '-Barrier'
        self.avIdList = avIdList[:]
        self.pendingAvatars = self.avIdList[:]
        self.timeout = timeout
        self.clearedFunc = clearedFunc
        self.timeoutFunc = timeoutFunc
        self.doneFunc = doneFunc
        if len(self.pendingAvatars) == 0:
            self.notify.debug('%s: barrier with empty list' % self.uniqueName)
            self.active = 0
            if self.clearedFunc:
                self.clearedFunc()
            if self.doneFunc:
                self.doneFunc(self.avIdList)
            return
        self.taskName = self.uniqueName + '-Timeout'
        origTaskName = self.taskName
        while taskMgr.hasTaskNamed(self.taskName):
            self.taskName = origTaskName + '-' + str(random.randint(0, 10000))

        taskMgr.doMethodLater(self.timeout, self.__timerExpired, self.taskName)
        for avId in self.avIdList:
            event = simbase.air.getAvatarExitEvent(avId)
            self.acceptOnce(event, self.__handleUnexpectedExit, extraArgs=[avId])

        self.notify.debug('%s: expecting responses from %s within %s seconds' % (self.uniqueName, self.avIdList, self.timeout))
        self.active = 1

    def cleanup(self):
        if self.active:
            taskMgr.remove(self.taskName)
            self.active = 0
        self.ignoreAll()

    def clear(self, avId):
        if avId not in self.pendingAvatars:
            self.notify.warning('%s: tried to clear %s, who was not listed.' % (self.uniqueName, avId))
            return
        self.notify.debug('%s: clearing avatar %s' % (self.uniqueName, avId))
        self.pendingAvatars.remove(avId)
        if len(self.pendingAvatars) == 0:
            self.notify.debug('%s: barrier cleared by %s' % (self.uniqueName, self.avIdList))
            self.cleanup()
            if self.clearedFunc:
                self.clearedFunc()
            if self.doneFunc:
                self.doneFunc(self.avIdList)

    def isActive(self):
        return self.active

    def getPendingAvatars(self):
        return self.pendingAvatars[:]

    def __timerExpired(self, task):
        self.notify.warning('%s: timeout expired; responses not received from %s' % (self.uniqueName, self.pendingAvatars))
        self.cleanup()
        if self.timeoutFunc:
            self.timeoutFunc(self.pendingAvatars[:])
        if self.doneFunc:
            clearedAvIds = self.avIdList[:]
            for avId in self.pendingAvatars:
                clearedAvIds.remove(avId)

            self.doneFunc(clearedAvIds)
        return Task.done

    def __handleUnexpectedExit(self, avId):
        if avId not in self.avIdList:
            return
        self.avIdList.remove(avId)
        if avId in self.pendingAvatars:
            self.clear(avId)