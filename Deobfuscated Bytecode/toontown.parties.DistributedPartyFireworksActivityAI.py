# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.parties.DistributedPartyFireworksActivityAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import globalClockDelta
from direct.fsm.FSM import FSM
from direct.task import Task
from toontown.parties.DistributedPartyActivityAI import DistributedPartyActivityAI
from toontown.effects import FireworkShows
import PartyGlobals, random

class DistributedPartyFireworksActivityAI(DistributedPartyActivityAI, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPartyFireworksActivityAI')

    def __init__(self, air, parent, activityTuple):
        DistributedPartyActivityAI.__init__(self, air, parent, activityTuple)
        FSM.__init__(self, 'DistributedPartyActivityAI')
        self.state = 'Idle'

    def getEventId(self):
        return PartyGlobals.FireworkShows.Summer

    def getShowStyle(self):
        return random.randint(0, len(FireworkShows.shows[PartyGlobals.FireworkShows.Summer]) - 1)

    def getSongId(self):
        return random.randint(0, 1)

    def toonJoinRequest(self):
        avId = self.air.getAvatarIdFromSender()
        host = self.air.doId2do[self.parent].hostId
        if avId == host and self.state == 'Idle':
            self.request('Active')
            taskMgr.doMethodLater(FireworkShows.getShowDuration(self.getEventId(), self.getShowStyle()) + PartyGlobals.FireworksPostLaunchDelay, self.showEnded, 'disablePartyFireworks%i' % self.doId, [])
            return
        self.sendUpdateToAvatarId(avId, 'joinRequestDenied', [1])

    def showEnded(self):
        self.request('Disabled')

    def enterActive(self):
        self.sendUpdate('setState', ['Active', globalClockDelta.getRealNetworkTime()])
        messenger.send('fireworksStarted%i' % self.getPartyDoId())

    def enterIdle(self):
        self.sendUpdate('setState', ['Idle', globalClockDelta.getRealNetworkTime()])

    def enterDisabled(self):
        self.sendUpdate('setState', ['Disabled', globalClockDelta.getRealNetworkTime()])
        messenger.send('fireworksFinished%i' % self.getPartyDoId())