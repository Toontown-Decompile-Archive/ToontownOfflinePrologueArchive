# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.hood.CSHoodDataAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
import HoodDataAI, ZoneUtil
from toontown.toonbase import ToontownGlobals
from toontown.coghq import DistributedFactoryElevatorExtAI
from toontown.coghq import DistributedCogHQDoorAI
from toontown.building import DoorTypes
from toontown.coghq import LobbyManagerAI
from toontown.building import DistributedBossElevatorAI
from toontown.suit import DistributedSellbotBossAI
from toontown.building import DistributedBoardingPartyAI
from toontown.suit import DistributedSuitPlannerAI

class CSHoodDataAI(HoodDataAI.HoodDataAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('CogHoodAI')

    def __init__(self, air, zoneId=None):
        hoodId = ToontownGlobals.SellbotHQ
        if zoneId == None:
            zoneId = hoodId
        HoodDataAI.HoodDataAI.__init__(self, air, zoneId, hoodId)
        return

    def startup(self):
        self.notify.info('Creating zone... Sellbot HQ')
        HoodDataAI.HoodDataAI.startup(self)
        mins = ToontownGlobals.FactoryLaffMinimums[0]
        self.testElev0 = DistributedFactoryElevatorExtAI.DistributedFactoryElevatorExtAI(self.air, self.air.factoryMgr, ToontownGlobals.SellbotFactoryInt, 0, antiShuffle=0, minLaff=mins[0])
        self.testElev0.generateWithRequired(ToontownGlobals.SellbotFactoryExt)
        self.addDistObj(self.testElev0)
        self.testElev1 = DistributedFactoryElevatorExtAI.DistributedFactoryElevatorExtAI(self.air, self.air.factoryMgr, ToontownGlobals.SellbotFactoryInt, 1, antiShuffle=0, minLaff=mins[1])
        self.testElev1.generateWithRequired(ToontownGlobals.SellbotFactoryExt)
        self.addDistObj(self.testElev1)
        self.lobbyMgr = LobbyManagerAI.LobbyManagerAI(self.air, DistributedSellbotBossAI.DistributedSellbotBossAI)
        self.lobbyMgr.generateWithRequired(ToontownGlobals.SellbotLobby)
        self.addDistObj(self.lobbyMgr)
        self.lobbyElevator = DistributedBossElevatorAI.DistributedBossElevatorAI(self.air, self.lobbyMgr, ToontownGlobals.SellbotLobby, antiShuffle=1)
        self.lobbyElevator.generateWithRequired(ToontownGlobals.SellbotLobby)
        self.addDistObj(self.lobbyElevator)
        if simbase.config.GetBool('want-boarding-groups', 1):
            self.boardingParty = DistributedBoardingPartyAI.DistributedBoardingPartyAI(self.air, [self.lobbyElevator.doId], 8)
            self.boardingParty.generateWithRequired(ToontownGlobals.SellbotLobby)
        factoryIdList = [
         self.testElev0.doId, self.testElev1.doId]
        if simbase.config.GetBool('want-boarding-groups', 1):
            self.factoryBoardingParty = DistributedBoardingPartyAI.DistributedBoardingPartyAI(self.air, factoryIdList, 4)
            self.factoryBoardingParty.generateWithRequired(ToontownGlobals.SellbotFactoryExt)
        destinationZone = ToontownGlobals.SellbotLobby
        extDoor0 = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 0, DoorTypes.EXT_COGHQ, destinationZone, doorIndex=0)
        extDoor1 = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 1, DoorTypes.EXT_COGHQ, destinationZone, doorIndex=1)
        extDoor2 = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 2, DoorTypes.EXT_COGHQ, destinationZone, doorIndex=2)
        extDoor3 = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 3, DoorTypes.EXT_COGHQ, destinationZone, doorIndex=3)
        extDoorList = [extDoor0,
         extDoor1,
         extDoor2,
         extDoor3]
        for sp in self.suitPlanners:
            if sp.zoneId == ToontownGlobals.SellbotHQ:
                sp.cogHQDoors = extDoorList

        intDoor0 = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 0, DoorTypes.INT_COGHQ, ToontownGlobals.SellbotHQ, doorIndex=0)
        intDoor0.setOtherDoor(extDoor0)
        intDoor0.zoneId = ToontownGlobals.SellbotLobby
        for extDoor in extDoorList:
            extDoor.setOtherDoor(intDoor0)
            extDoor.zoneId = ToontownGlobals.SellbotHQ
            extDoor.generateWithRequired(ToontownGlobals.SellbotHQ)
            extDoor.sendUpdate('setDoorIndex', [extDoor.getDoorIndex()])
            self.addDistObj(extDoor)

        intDoor0.generateWithRequired(ToontownGlobals.SellbotLobby)
        intDoor0.sendUpdate('setDoorIndex', [intDoor0.getDoorIndex()])
        self.addDistObj(intDoor0)
        if simbase.config.GetBool('want-suit-planners', 1):
            self.createPlanner(ToontownGlobals.SellbotHQ, extDoorList)
            self.createPlanner(ToontownGlobals.SellbotFactoryExt)

    def createPlanner(self, zoneId, cogHQDoors=[]):
        zoneId = ZoneUtil.getTrueZoneId(zoneId, self.zoneId)
        sp = DistributedSuitPlannerAI.DistributedSuitPlannerAI(self.air, zoneId)
        sp.cogHQDoors = cogHQDoors
        sp.generateWithRequired(zoneId)
        sp.d_setZoneId(zoneId)
        sp.initTasks()
        self.air.suitPlanners[zoneId] = sp
        self.notify.debug('Created new SuitPlanner at %s' % zoneId)