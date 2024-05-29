# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.effects.DistributedFireworkShowAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.ClockDelta import *
from direct.task import Task
from otp.ai.MagicWordGlobal import *
from toontown.toonbase import ToontownGlobals
from toontown.parties import PartyGlobals
import FireworkShows, random, time

class DistributedFireworkShowAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFireworkShowAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.air = air

    def startShow(self, eventId, style, timeStamp):
        taskMgr.doMethodLater(FireworkShows.getShowDuration(eventId, style), self.requestDelete, 'delete%i' % self.doId, [])

    def d_startShow(self, eventId, style, timeStamp):
        self.sendUpdate('startShow', [eventId, style, random.randint(0, 1), timeStamp])

    def b_startShow(self, eventId, style, timeStamp):
        self.startShow(eventId, style, timeStamp)
        self.d_startShow(eventId, style, timeStamp)

    def requestFirework(self, todo0, todo1, todo2, todo3, todo4, todo5):
        pass

    def shootFirework(self, todo0, todo1, todo2, todo3, todo4, todo5):
        pass


@magicWord(category=CATEGORY_OVERRIDE, types=[str])
def fireworks(showName='july4'):
    if showName == 'july4':
        showType = ToontownGlobals.JULY4_FIREWORKS
    else:
        if showName == 'newyears':
            showType = ToontownGlobals.NEWYEARS_FIREWORKS
        elif showName == 'summer':
            showType = PartyGlobals.FireworkShows.Summer
        else:
            return 'Invalid firework show type!'
        numShows = len(FireworkShows.shows.get(showType, []))
        showIndex = random.randint(0, numShows - 1)
        for hood in simbase.air.hoods:
            if hood.HOOD == ToontownGlobals.GolfZone:
                continue
            fireworksShow = DistributedFireworkShowAI(simbase.air)
            fireworksShow.generateWithRequired(hood.HOOD)
            fireworksShow.b_startShow(showType, showIndex, globalClockDelta.getRealNetworkTime())

    return 'Started fireworks in all playgrounds!'