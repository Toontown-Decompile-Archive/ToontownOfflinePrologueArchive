# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.speedchat.TTSCPromotionalMenu
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from otp.speedchat.SCMenu import SCMenu
from otp.speedchat import SCMenuHolder
from otp.speedchat.SCStaticTextTerminal import SCStaticTextTerminal
from otp.otpbase import OTPLocalizer
from toontown.toonbase import ToontownGlobals
holidayId2menuInfo = {ToontownGlobals.ELECTION_PROMOTION: (OTPLocalizer.SCMenuElection,
                                      [10000, 10001,
                                       10006,
                                       10007])}

class TTSCPromotionalMenu(SCMenu):
    notify = DirectNotifyGlobal.directNotify.newCategory('TTSCPromotionalMenu')

    def __init__(self):
        SCMenu.__init__(self)
        base.TTSCPromotionalMenu = self
        self.curHolidayId = None
        self.clearMenu()
        return

    def destroy(self):
        del base.TTSCPromotionalMenu
        SCMenu.destroy(self)

    def startHoliday(self, holidayId):
        if self.curHolidayId is not None:
            TTSCPromotionalMenu.notify.warning('overriding existing holidayId %s with %s' % (self.curHolidayId, holidayId))
        self.curHolidayId = holidayId
        title, structure = holidayId2menuInfo[holidayId]
        self.rebuildFromStructure(structure, title=title)
        return

    def endHoliday(self, holidayId):
        if holidayId != self.curHolidayId:
            TTSCPromotionalMenu.notify.warning('unexpected holidayId: %s' % holidayId)
            return
        else:
            self.curHolidayId = None
            self.clearMenu()
            return