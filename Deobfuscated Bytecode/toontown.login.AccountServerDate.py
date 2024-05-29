# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.login.AccountServerDate
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from otp.login.HTTPUtil import *
from direct.directnotify import DirectNotifyGlobal
from otp.login import TTAccount
import DateObject, TTDateObject, time

class AccountServerDate:
    notify = DirectNotifyGlobal.directNotify.newCategory('AccountServerDate')

    def __init__(self):
        self.__grabbed = 0

    def getServer(self):
        return TTAccount.getAccountServer().cStr()

    def grabDate(self, force=0):
        if self.__grabbed and not force:
            self.notify.debug('using cached account server date')
            return
        if base.cr.accountOldAuth or config.GetBool('use-local-date', 0):
            self.__useLocalClock()
            return
        url = URLSpec(self.getServer())
        url.setPath('/getDate.php')
        self.notify.debug('grabbing account server date from %s' % url.cStr())
        response = getHTTPResponse(url, http)
        if response[0] != 'ACCOUNT SERVER DATE':
            self.notify.debug('invalid response header')
            raise UnexpectedResponse, 'unexpected response, response=%s' % response
        try:
            epoch = int(response[1])
        except ValueError as e:
            self.notify.debug(str(e))
            raise UnexpectedResponse, 'unexpected response, response=%s' % response

        timeTuple = time.gmtime(epoch)
        self.year = timeTuple[0]
        self.month = timeTuple[1]
        self.day = timeTuple[2]
        base.cr.dateObject = TTDateObject.TTDateObject(self)
        self.__grabbed = 1

    def __useLocalClock(self):
        self.month = base.cr.dateObject.getMonth()
        self.year = base.cr.dateObject.getYear()
        self.day = base.cr.dateObject.getDay()

    def getMonth(self):
        return self.month

    def getYear(self):
        return self.year

    def getDay(self):
        return self.day