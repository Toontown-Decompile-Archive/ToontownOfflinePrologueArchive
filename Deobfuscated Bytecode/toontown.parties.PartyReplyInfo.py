# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.parties.PartyReplyInfo
# Compiled at: 2014-04-30 09:53:54


class SingleReply:

    def __init__(self, inviteeId, status):
        self.inviteeId = inviteeId
        self.status = status


class PartyReplyInfoBase:

    def __init__(self, partyId, partyReplies):
        self.partyId = partyId
        self.replies = []
        for oneReply in partyReplies:
            self.replies.append(SingleReply(*oneReply))

    def __str__(self):
        string = 'partyId=%d ' % self.partyId
        for reply in self.replies:
            string += '(%d:%d) ' % (reply.inviteeId, reply.status)

        return string