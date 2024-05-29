# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.parties.ActivityBase
# Compiled at: 2014-04-30 09:53:54


class ActivityBase:

    def __init__(self, activityId, x, y, h):
        self.activityId = activityId
        self.x = x
        self.y = y
        self.h = h

    def __str__(self):
        string = '<ActivityBase activityId=%d, ' % self.activityId
        string += 'x=%d, y=%d, h=%d>' % (self.x, self.y, self.h)
        return string

    def __repr__(self):
        return self.__str__()