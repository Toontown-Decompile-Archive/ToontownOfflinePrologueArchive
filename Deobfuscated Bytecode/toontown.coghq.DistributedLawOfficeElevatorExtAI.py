# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.DistributedLawOfficeElevatorExtAI
# Compiled at: 2014-04-30 09:53:54
from otp.ai.AIBase import *
from toontown.toonbase import ToontownGlobals
from direct.distributed.ClockDelta import *
from toontown.building.ElevatorConstants import *
from toontown.building import DistributedElevatorExtAI
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.task import Task

class DistributedLawOfficeElevatorExtAI(DistributedElevatorExtAI.DistributedElevatorExtAI):

    def __init__(self, air, bldg, lawOfficeId, entranceId, antiShuffle=0, minLaff=0):
        DistributedElevatorExtAI.DistributedElevatorExtAI.__init__(self, air, bldg, antiShuffle=antiShuffle, minLaff=minLaff)
        self.lawOfficeId = lawOfficeId
        self.entranceId = entranceId

    def getEntranceId(self):
        return self.entranceId

    def elevatorClosed(self):
        numPlayers = self.countFullSeats()
        if numPlayers > 0:
            players = []
            for i in self.seats:
                if i not in (None, 0):
                    players.append(i)

            lawOfficeZone = self.bldg.createLawOffice(self.lawOfficeId, self.entranceId, players)
            for seatIndex in range(len(self.seats)):
                avId = self.seats[seatIndex]
                if avId:
                    self.sendUpdateToAvatarId(avId, 'setLawOfficeInteriorZone', [lawOfficeZone])
                    self.clearFullNow(seatIndex)

        else:
            self.notify.warning('The elevator left, but was empty.')
        self.fsm.request('closed')
        return

    def enterClosed(self):
        DistributedElevatorExtAI.DistributedElevatorExtAI.enterClosed(self)
        self.fsm.request('opening')

    def sendAvatarsToDestination(self, avIdList):
        if len(avIdList) > 0:
            officeZone = self.bldg.createLawOffice(self.lawOfficeId, self.entranceId, avIdList)
            for avId in avIdList:
                if avId:
                    self.sendUpdateToAvatarId(avId, 'setLawOfficeInteriorZoneForce', [officeZone])