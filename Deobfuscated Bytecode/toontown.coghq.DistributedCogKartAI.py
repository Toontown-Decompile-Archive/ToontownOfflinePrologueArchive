# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.DistributedCogKartAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from toontown.safezone import DistributedGolfKartAI
from toontown.building import DistributedElevatorExtAI
from toontown.building import ElevatorConstants
from toontown.toonbase import ToontownGlobals

class DistributedCogKartAI(DistributedElevatorExtAI.DistributedElevatorExtAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCogKartAI')

    def __init__(self, air, index, x, y, z, h, p, r, bldg, minLaff):
        self.posHpr = (
         x, y, z, h, p, r)
        DistributedElevatorExtAI.DistributedElevatorExtAI.__init__(self, air, bldg, minLaff=minLaff)
        self.type = ElevatorConstants.ELEVATOR_COUNTRY_CLUB
        self.courseIndex = index
        if self.courseIndex == 0:
            self.countryClubId = ToontownGlobals.BossbotCountryClubIntA
        elif self.courseIndex == 1:
            self.countryClubId = ToontownGlobals.BossbotCountryClubIntB
        elif self.courseIndex == 2:
            self.countryClubId = ToontownGlobals.BossbotCountryClubIntC
        else:
            self.countryClubId = 12500

    def getPosHpr(self):
        return self.posHpr

    def elevatorClosed(self):
        numPlayers = self.countFullSeats()
        if numPlayers > 0:
            players = []
            for i in self.seats:
                if i not in (None, 0):
                    players.append(i)

            countryClubZone = self.bldg.createCountryClub(self.countryClubId, players)
            for seatIndex in range(len(self.seats)):
                avId = self.seats[seatIndex]
                if avId:
                    self.sendUpdateToAvatarId(avId, 'setCountryClubInteriorZone', [countryClubZone])
                    self.clearFullNow(seatIndex)

        else:
            self.notify.warning('The elevator left, but was empty.')
        self.fsm.request('closed')
        return

    def sendAvatarsToDestination(self, avIdList):
        if len(avIdList) > 0:
            countryClubZone = self.bldg.createCountryClub(self.countryClubId, avIdList)
            for avId in avIdList:
                if avId:
                    self.sendUpdateToAvatarId(avId, 'setCountryClubInteriorZoneForce', [countryClubZone])

    def getCountryClubId(self):
        return self.countryClubId

    def enterClosed(self):
        DistributedElevatorExtAI.DistributedElevatorExtAI.enterClosed(self)
        self.fsm.request('opening')