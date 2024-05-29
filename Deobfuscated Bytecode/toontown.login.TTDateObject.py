# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.login.TTDateObject
# Compiled at: 2014-04-30 09:53:54
import DateObject

class TTDateObject(DateObject.DateObject):

    def __init__(self, accountServerDate):
        self.accountServerDate = accountServerDate

    def getYear(self):
        return self.accountServerDate.getYear()

    def getMonth(self):
        return self.accountServerDate.getMonth()

    def getDay(self):
        return self.accountServerDate.getDay()

    def getDetailedAge(self, dobMonth, dobYear, dobDay=None, curMonth=None, curYear=None, curDay=None):
        return DateObject.DateObject.getDetailedAge(self, dobMonth, dobYear, dobDay, curMonth=self.getMonth(), curYear=self.getYear(), curDay=self.getDay())

    def getAge(self, dobMonth, dobYear, dobDay=None, curMonth=None, curYear=None, curDay=None):
        return TTDateObject.getDetailedAge(self, dobMonth, dobYear, dobDay=dobDay, curMonth=curMonth, curYear=curYear, curDay=curDay)[0]