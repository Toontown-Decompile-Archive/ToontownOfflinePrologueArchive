# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.parties.SimpleMailBase
# Compiled at: 2014-04-30 09:53:54


class SimpleMailBase:

    def __init__(self, msgId, senderId, year, month, day, body):
        self.msgId = msgId
        self.senderId = senderId
        self.year = year
        self.month = month
        self.day = day
        self.body = body

    def __str__(self):
        string = 'msgId=%d ' % self.msgId
        string += 'senderId=%d ' % self.senderId
        string += 'sent=%s-%s-%s ' % (self.year, self.month, self.day)
        string += 'body=%s' % self.body
        return string