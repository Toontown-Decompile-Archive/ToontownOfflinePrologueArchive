# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.parties.InviteInfo
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.parties.PartyGlobals import InviteStatus
from toontown.toonbase import TTLocalizer

class InviteInfoBase:

    def __init__(self, inviteKey, partyId, status):
        self.inviteKey = inviteKey
        self.partyId = partyId
        self.status = status

    def __str__(self):
        string = 'inviteKey=%d ' % self.inviteKey
        string += 'partyId=%d ' % self.partyId
        string += 'status=%s' % InviteStatus.getString(self.status)
        return string

    def __repr__(self):
        return self.__str__()


class InviteInfo(InviteInfoBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('InviteInfo')

    def __init__(self, inviteKey, partyId, status):
        InviteInfoBase.__init__(self, inviteKey, partyId, status)

    def acceptItem(self, mailbox, acceptingIndex, callback):
        InviteInfo.notify.debug('acceptItem')
        mailbox.acceptInvite(self, acceptingIndex, callback)

    def discardItem(self, mailbox, acceptingIndex, callback):
        InviteInfo.notify.debug('discardItem')
        mailbox.rejectInvite(self, acceptingIndex, callback)

    def getAcceptItemErrorText(self, retcode):
        InviteInfo.notify.debug('getAcceptItemErrorText')
        if retcode == ToontownGlobals.P_InvalidIndex:
            return TTLocalizer.InviteAcceptInvalidError
        else:
            if retcode == ToontownGlobals.P_ItemAvailable:
                return TTLocalizer.InviteAcceptAllOk
            return TTLocalizer.CatalogAcceptGeneralError % retcode

    def getDiscardItemErrorText(self, retcode):
        InviteInfo.notify.debug('getDiscardItemErrorText')
        if retcode == ToontownGlobals.P_InvalidIndex:
            return TTLocalizer.InviteAcceptInvalidError
        else:
            if retcode == ToontownGlobals.P_ItemAvailable:
                return TTLocalizer.InviteRejectAllOk
            return TTLocalizer.CatalogAcceptGeneralError % retcode

    def output(self, store=-1):
        return 'InviteInfo %s' % str(self)