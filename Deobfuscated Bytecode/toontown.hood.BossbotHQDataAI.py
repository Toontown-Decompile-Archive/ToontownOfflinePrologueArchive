# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.hood.BossbotHQDataAI
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import Point3
from direct.directnotify import DirectNotifyGlobal
import HoodDataAI
from toontown.toonbase import ToontownGlobals
from toontown.coghq import DistributedCogHQDoorAI
from toontown.building import DistributedDoorAI
from toontown.building import DoorTypes
from toontown.coghq import LobbyManagerAI
from toontown.building import DistributedBossElevatorAI
from toontown.suit import DistributedBossbotBossAI
from toontown.building import DistributedBBElevatorAI
from toontown.building import DistributedBoardingPartyAI
from toontown.building import FADoorCodes
from toontown.coghq import DistributedCogKartAI

class BossbotHQDataAI(HoodDataAI.HoodDataAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('CogHoodAI')

    def __init__(self, air, zoneId=None):
        self.notify.debug('__init__: zoneId:%s' % zoneId)
        hoodId = ToontownGlobals.BossbotHQ
        if zoneId == None:
            zoneId = hoodId
        self.cogKarts = []
        HoodDataAI.HoodDataAI.__init__(self, air, zoneId, hoodId)
        return

    def startup(self):
        self.notify.info('Creating zone... Bossbot HQ')
        HoodDataAI.HoodDataAI.startup(self)

        def makeOfficeElevator(index, antiShuffle=0, minLaff=0):
            destZone = (ToontownGlobals.LawbotStageIntA,
             ToontownGlobals.LawbotStageIntB,
             ToontownGlobals.LawbotStageIntC,
             ToontownGlobals.LawbotStageIntD)[index]
            elev = DistributedLawOfficeElevatorExtAI.DistributedLawOfficeElevatorExtAI(self.air, self.air.lawMgr, destZone, index, antiShuffle=0, minLaff=minLaff)
            elev.generateWithRequired(ToontownGlobals.LawbotOfficeExt)
            self.addDistObj(elev)

        self.lobbyMgr = LobbyManagerAI.LobbyManagerAI(self.air, DistributedBossbotBossAI.DistributedBossbotBossAI)
        self.lobbyMgr.generateWithRequired(ToontownGlobals.BossbotLobby)
        self.addDistObj(self.lobbyMgr)
        self.lobbyElevator = DistributedBBElevatorAI.DistributedBBElevatorAI(self.air, self.lobbyMgr, ToontownGlobals.BossbotLobby, antiShuffle=1)
        self.lobbyElevator.generateWithRequired(ToontownGlobals.BossbotLobby)
        self.addDistObj(self.lobbyElevator)
        if simbase.config.GetBool('want-boarding-groups', 1):
            self.boardingParty = DistributedBoardingPartyAI.DistributedBoardingPartyAI(self.air, [self.lobbyElevator.doId], 8)
            self.boardingParty.generateWithRequired(ToontownGlobals.BossbotLobby)

        def makeDoor(destinationZone, intDoorIndex, extDoorIndex, lock=0):
            intDoor = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 0, DoorTypes.INT_COGHQ, self.canonicalHoodId, doorIndex=intDoorIndex, lockValue=lock)
            intDoor.zoneId = destinationZone
            extDoor = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 0, DoorTypes.EXT_COGHQ, destinationZone, doorIndex=extDoorIndex, lockValue=lock)
            extDoor.setOtherDoor(intDoor)
            intDoor.setOtherDoor(extDoor)
            intDoor.generateWithRequired(destinationZone)
            intDoor.sendUpdate('setDoorIndex', [intDoor.getDoorIndex()])
            self.addDistObj(intDoor)
            extDoor.generateWithRequired(self.canonicalHoodId)
            extDoor.sendUpdate('setDoorIndex', [extDoor.getDoorIndex()])
            self.addDistObj(extDoor)

        makeDoor(ToontownGlobals.BossbotLobby, 0, 0, FADoorCodes.BB_DISGUISE_INCOMPLETE)
        kartIdList = self.createCogKarts()
        if simbase.config.GetBool('want-boarding-groups', 1):
            self.courseBoardingParty = DistributedBoardingPartyAI.DistributedBoardingPartyAI(self.air, kartIdList, 4)
            self.courseBoardingParty.generateWithRequired(self.zoneId)

    def createCogKarts(self):
        posList = ((154.762, 37.169, 0), (141.403, -81.887, 0), (-48.44, 15.308, 0))
        hprList = ((110.815, 0, 0), (61.231, 0, 0), (-105.481, 0, 0))
        mins = ToontownGlobals.FactoryLaffMinimums[3]
        kartIdList = []
        for cogCourse in xrange(len(posList)):
            pos = posList[cogCourse]
            hpr = hprList[cogCourse]
            cogKart = DistributedCogKartAI.DistributedCogKartAI(self.air, cogCourse, pos[0], pos[1], pos[2], hpr[0], hpr[1], hpr[2], self.air.countryClubMgr, minLaff=mins[cogCourse])
            cogKart.generateWithRequired(self.zoneId)
            self.cogKarts.append(cogKart)
            kartIdList.append(cogKart.doId)

        return kartIdList