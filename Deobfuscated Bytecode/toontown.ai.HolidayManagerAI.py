# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.ai.HolidayManagerAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.ClockDelta import *
from direct.task import Task
from otp.ai.MagicWordGlobal import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase.HolidayData import ONCELY_HOLIDAYS, WEEKLY_HOLIDAYS, YEARLY_HOLIDAYS
from toontown.parties import PartyGlobals
from toontown.effects.DistributedFireworkShowAI import DistributedFireworkShowAI
from toontown.effects import FireworkShows
from toontown.suit import SuitDNA
import random, time

class HolidayManagerAI():
    notify = directNotify.newCategory('HolidayManagerAI')

    def __init__(self, air):
        self.air = air
        self.currentHolidays = []
        self.setup()

    def setup(self):
        holidays = config.GetString('active-holidays', '')
        if holidays != '':
            for holiday in holidays.split(','):
                holiday = int(holiday)
                self.currentHolidays.append(holiday)

            self.air.newsManager.setHolidayIdList([self.currentHolidays])
        if config.GetBool('want-hourly-fireworks', False) or self.isHolidayRunning(ToontownGlobals.JULY4_FIREWORKS) or self.isHolidayRunning(ToontownGlobals.NEWYEARS_FIREWORKS) or self.isHolidayRunning(ToontownGlobals.OCTOBER31_FIREWORKS) or self.isHolidayRunning(ToontownGlobals.NOVEMBER19_FIREWORKS) or self.isHolidayRunning(ToontownGlobals.FEBRUARY14_FIREWORKS) or self.isHolidayRunning(ToontownGlobals.JULY14_FIREWORKS) or self.isHolidayRunning(ToontownGlobals.COMBO_FIREWORKS):
            self.__startFireworksTick()

    def __startFireworksTick(self):
        ts = time.time()
        nextHour = 3600 - ts % 3600
        taskMgr.doMethodLater(nextHour, self.__fireworksTick, 'hourly-fireworks')

    def __fireworksTick(self, task):
        task.delayTime = 3600
        showName = config.GetString('hourly-fireworks-type', 'july4')
        if self.isHolidayRunning(ToontownGlobals.JULY4_FIREWORKS):
            showType = ToontownGlobals.JULY4_FIREWORKS
        else:
            if self.isHolidayRunning(ToontownGlobals.NEWYEARS_FIREWORKS):
                showType = ToontownGlobals.NEWYEARS_FIREWORKS
            else:
                if self.isHolidayRunning(ToontownGlobals.JULY14_FIREWORKS) or self.isHolidayRunning(ToontownGlobals.OCTOBER31_FIREWORKS) or self.isHolidayRunning(ToontownGlobals.NOVEMBER19_FIREWORKS) or self.isHolidayRunning(ToontownGlobals.FEBRUARY14_FIREWORKS):
                    showType = PartyGlobals.FireworkShows.Summer
                else:
                    if self.isHolidayRunning(ToontownGlobals.COMBO_FIREWORKS):
                        shows = [
                         ToontownGlobals.JULY4_FIREWORKS, ToontownGlobals.NEWYEARS_FIREWORKS, PartyGlobals.FireworkShows.Summer]
                        showType = random.choice(shows)
                    else:
                        if showName == 'july4':
                            showType = ToontownGlobals.JULY4_FIREWORKS
                        else:
                            if showName == 'newyears':
                                showType = ToontownGlobals.NEWYEARS_FIREWORKS
                            else:
                                if showName == 'summer':
                                    showType = PartyGlobals.FireworkShows.Summer
                                elif showName == 'random':
                                    shows = [
                                     ToontownGlobals.JULY4_FIREWORKS, ToontownGlobals.NEWYEARS_FIREWORKS, PartyGlobals.FireworkShows.Summer]
                                    showType = random.choice(shows)
                                else:
                                    raise AttributeError('%s is an invalid firework type' % showName)
                                    return
            numShows = len(FireworkShows.shows.get(showType, []))
            showIndex = random.randint(0, numShows - 1)
            for hood in self.air.hoods:
                if hood.HOOD == ToontownGlobals.GolfZone:
                    continue
                fireworksShow = DistributedFireworkShowAI(self.air)
                fireworksShow.generateWithRequired(hood.HOOD)
                fireworksShow.b_startShow(showType, showIndex, globalClockDelta.getRealNetworkTime())

        return task.again

    def isHolidayRunning(self, holidayId):
        if holidayId in self.currentHolidays:
            return True

    def isInvasionHolidayRunning(self):
        if ToontownGlobals.SKELECOG_INVASION in self.currentHolidays or ToontownGlobals.MR_HOLLYWOOD_INVASION in self.currentHolidays or ToontownGlobals.MARCH_INVASION in self.currentHolidays:
            return True
        if ToontownGlobals.DECEMBER_INVASION in self.currentHolidays or ToontownGlobals.MR_HOLLYWOOD_INVASION in self.currentHolidays or ToontownGlobals.MARCH_INVASION in self.currentHolidays:
            return True
        for holiday in xrange(33, 49):
            if holiday in self.currentHolidays:
                return True

        if ToontownGlobals.BEAN_COUNTER_INVASION in self.currentHolidays or ToontownGlobals.DOUBLE_TALKER_INVASION in self.currentHolidays or ToontownGlobals.DOWNSIZER_INVASION in self.currentHolidays:
            return True
        for holiday in xrange(72, 93):
            if holiday in self.currentHolidays:
                return True

        if ToontownGlobals.SELLBOT_INVASION in self.currentHolidays or ToontownGlobals.SELLBOT_INVASION_MOVER_AND_SHAKER in self.currentHolidays or ToontownGlobals.IDES_OF_MARCH in self.currentHolidays:
            return True
        if ToontownGlobals.PRE_JULY_4_DOWNSIZER_INVASION in self.currentHolidays or ToontownGlobals.PRE_JULY_4_BIGWIG_INVASION in self.currentHolidays:
            return True

    def whosInvading(self):
        if ToontownGlobals.SKELECOG_INVASION in self.currentHolidays:
            return (random.choice(SuitDNA.suitHeadTypes), 1)
        if ToontownGlobals.MR_HOLLYWOOD_INVASION in self.currentHolidays:
            return ('mh', 0)
        if ToontownGlobals.MARCH_INVASION in self.currentHolidays or ToontownGlobals.IDES_OF_MARCH in self.currentHolidays:
            return ('bs', 0)
        if ToontownGlobals.DECEMBER_INVASION in self.currentHolidays:
            return ('cc', 2)
        if ToontownGlobals.MR_HOLLYWOOD_INVASION in self.currentHolidays:
            return ('mh', 0)
        if ToontownGlobals.SELLBOT_SURPRISE_1 in self.currentHolidays:
            return ('cc', 0)
        if ToontownGlobals.SELLBOT_SURPRISE_2 in self.currentHolidays or ToontownGlobals.NAME_DROPPER_INVASION in self.currentHolidays:
            return ('nd', 0)
        if ToontownGlobals.SELLBOT_SURPRISE_3 in self.currentHolidays or ToontownGlobals.TWOFACES_INVASION in self.currentHolidays:
            return ('tf', 0)
        if ToontownGlobals.SELLBOT_SURPRISE_4 in self.currentHolidays:
            return ('mh', 0)
        if ToontownGlobals.CASHBOT_CONUNDRUM_1 in self.currentHolidays or ToontownGlobals.TIGHTWAD_INVASION in self.currentHolidays:
            return ('tw', 0)
        if ToontownGlobals.CASHBOT_CONUNDRUM_2 in self.currentHolidays:
            return ('bc', 0)
        if ToontownGlobals.CASHBOT_CONUNDRUM_3 in self.currentHolidays or ToontownGlobals.LOANSHARK_INVASION in self.currentHolidays:
            return ('ls', 0)
        if ToontownGlobals.CASHBOT_CONUNDRUM_4 in self.currentHolidays or ToontownGlobals.ROBBER_BARON_INVASION in self.currentHolidays:
            return ('rb', 0)
        if ToontownGlobals.LAWBOT_GAMBIT_1 in self.currentHolidays or ToontownGlobals.AMBULANCE_CHASER_INVASION in self.currentHolidays:
            return ('ac', 0)
        if ToontownGlobals.LAWBOT_GAMBIT_2 in self.currentHolidays:
            return ('bs', 0)
        if ToontownGlobals.LAWBOT_GAMBIT_3 in self.currentHolidays or ToontownGlobals.SPINDOCTOR_INVASION in self.currentHolidays:
            return ('sd', 0)
        if ToontownGlobals.LAWBOT_GAMBIT_4 in self.currentHolidays or ToontownGlobals.LEGAL_EAGLE_INVASION in self.currentHolidays:
            return ('le', 0)
        if ToontownGlobals.TROUBLE_BOSSBOTS_1 in self.currentHolidays:
            return ('p', 0)
        if ToontownGlobals.TROUBLE_BOSSBOTS_2 in self.currentHolidays or ToontownGlobals.YES_MAN_INVASION in self.currentHolidays:
            return ('ym', 0)
        if ToontownGlobals.TROUBLE_BOSSBOTS_3 in self.currentHolidays or ToontownGlobals.MICROMANAGER_INVASION in self.currentHolidays:
            return ('mm', 0)
        if ToontownGlobals.TROUBLE_BOSSBOTS_4 in self.currentHolidays or ToontownGlobals.BIG_CHEESE_INVASION in self.currentHolidays:
            return ('tbc', 0)
        if ToontownGlobals.BEAN_COUNTER_INVASION in self.currentHolidays:
            return ('bc', 0)
        if ToontownGlobals.DOUBLE_TALKER_INVASION in self.currentHolidays or ToontownGlobals.DOUBLETALKER_INVASION in self.currentHolidays:
            return ('dt', 0)
        if ToontownGlobals.DOWNSIZER_INVASION in self.currentHolidays or ToontownGlobals.DOWN_SIZER_INVASION in self.currentHolidays or ToontownGlobals.PRE_JULY_4_DOWNSIZER_INVASION in self.currentHolidays:
            return ('ds', 0)
        if ToontownGlobals.TELEMARKETER_INVASION in self.currentHolidays:
            return ('tm', 0)
        if ToontownGlobals.HEADHUNTER_INVASION in self.currentHolidays:
            return ('hh', 0)
        if ToontownGlobals.MONEYBAGS_INVASION in self.currentHolidays:
            return ('mb', 0)
        if ToontownGlobals.MINGLER_INVASION in self.currentHolidays:
            return ('m', 0)
        if ToontownGlobals.CORPORATE_RAIDER_INVASION in self.currentHolidays:
            return ('cr', 0)
        if ToontownGlobals.BIG_WIG_INVASION in self.currentHolidays or ToontownGlobals.PRE_JULY_4_BIGWIG_INVASION in self.currentHolidays:
            return ('bw', 0)
        if ToontownGlobals.MOVER_AND_SHAKER_INVASION in self.currentHolidays:
            return ('ms', 0)
        if ToontownGlobals.PENNY_PINCHER_INVASION in self.currentHolidays:
            return ('pp', 0)
        if ToontownGlobals.NUMBER_CRUNCHER_INVASION in self.currentHolidays:
            return ('nc', 0)
        if ToontownGlobals.SELLBOT_INVASION in self.currentHolidays:
            return (SuitDNA.getRandomSuitByDept('s'), 0)
        if ToontownGlobals.SELLBOT_INVASION_MOVER_AND_SHAKER in self.currentHolidays:
            return ('ms', 0)

    def yearlyHolidayTask(self, task=None):
        for holiday in YEARLY_HOLIDAYS:
            holidayId = holiday[0]
            now = datetime.now()
            startDate = datetime(now.year, *holiday[1])
            endDate = datetime(now.year, *holiday[2])
            if startDate < now < endDate and holidayId not in self.currentHolidays:
                self.appendHoliday(holidayId)
                self.startHoliday(holidayId)
            elif endDate < now and holidayId in self.currentHolidays:
                self.removeHoliday(holidayId)
                self.endHoliday(holidayId)

        taskMgr.doMethodLater(STANDARD_INTERVAL, self.yearlyHolidayTask, 'yearlyHolidayTask')

    def weeklyHolidayTask(self, task=None):
        for holiday in WEEKLY_HOLIDAYS:
            holidayId = holiday[0]
            startDay = holiday[1]
            if startDay == date.today().weekday() and holidayId not in self.currentHolidays:
                self.appendHoliday(holidayId)
                self.startHoliday(holidayId)
            elif holidayId in self.currentHolidays:
                self.removeHoliday(holidayId)
                self.endHoliday(holidayId)

        taskMgr.doMethodLater(STANDARD_INTERVALL, self.weeklyHolidayTask, 'weeklyHolidayTask')

    def oncelyHolidayTask(self, task=None):
        for holiday in ONCELY_HOLIDAYS:
            holidayId = holiday[0]
            now = datetime.now()
            startDate = datetime(now.year, *holiday[1])
            endDate = datetime(now.year, *holiday[2])
            if startDay == date.today().weekday() and holidayId not in self.currentHolidays:
                self.appendHoliday(holidayId)
                self.startHoliday(holidayId)
                if holidayId in self.currentHolidays:
                    self.removeHoliday(holidayId)
                    self.endHoliday(holidayId)

        taskMgr.doMethodLater(STANDARD_INTERVALL, self.oncelyHolidayTask, 'oncelyHolidayTask')

    def appendHoliday(self, holidayId):
        if holidayId not in self.currentHolidays:
            self.currentHolidays.append(holidayId)
            self.air.newsManager.setHolidayIdList([self.currentHolidays])
            return True

    def removeHoliday(self, holidayId):
        if holidayId in self.currentHolidays:
            self.currentHolidays.remove(holidayId)
            self.air.newsManager.setHolidayIdList([self.currentHolidays])
            return True


@magicWord(category=CATEGORY_SYSADMIN, types=[int])
def startHoliday(holidayId):
    if simbase.air.holidayManager.appendHoliday(holidayId) == True:
        return 'Started Holiday %s' % holidayId
    return 'Holiday %s is already running' % holidayId


@magicWord(category=CATEGORY_SYSADMIN, types=[int])
def endHoliday(holidayId):
    if simbase.air.holidayManager.removeHoliday(holidayId) == True:
        return 'Ended Holiday %s' % holidayId
    return 'Holiday %s already ended' % holidayId