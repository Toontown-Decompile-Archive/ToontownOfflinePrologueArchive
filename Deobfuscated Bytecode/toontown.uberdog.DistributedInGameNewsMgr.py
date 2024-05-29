# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.uberdog.DistributedInGameNewsMgr
# Compiled at: 2014-04-30 09:53:54
import socket, datetime, os
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from direct.distributed.DistributedObject import DistributedObject
from toontown.toonbase import ToontownGlobals
from toontown.uberdog import InGameNewsResponses

class DistributedInGameNewsMgr(DistributedObject):
    notify = directNotify.newCategory('InGameNewsMgr')
    neverDisable = 1

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        base.cr.inGameNewsMgr = self

    def delete(self):
        DistributedObject.delete(self)
        self.cr.inGameNewsMgr = None
        return

    def disable(self):
        self.notify.debug("i'm disabling InGameNewsMgr  rightnow.")
        DistributedObject.disable(self)

    def generate(self):
        self.notify.debug('BASE: generate')
        DistributedObject.generate(self)

    def setLatestIssueStr(self, issueStr):
        self.latestIssueStr = issueStr
        self.latestIssue = base.cr.toontownTimeManager.convertUtcStrToToontownTime(issueStr)
        messenger.send('newIssueOut')
        self.notify.info('latestIssue=%s' % self.latestIssue)

    def getLatestIssueStr(self):
        pass

    def getLatestIssue(self):
        return self.latestIssue