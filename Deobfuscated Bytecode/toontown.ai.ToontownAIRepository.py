# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.ai.ToontownAIRepository
# Compiled at: 2014-04-30 09:53:54
import toontown.minigame.MinigameCreatorAI
from toontown.distributed.ToontownDistrictAI import ToontownDistrictAI
from toontown.distributed.ToontownDistrictStatsAI import ToontownDistrictStatsAI
from toontown.distributed.ShardStatus import ShardStatusSender
from otp.ai.TimeManagerAI import TimeManagerAI
from otp.ai.MagicWordManagerAI import MagicWordManagerAI
from toontown.ai.HolidayManagerAI import HolidayManagerAI
from toontown.ai.NewsManagerAI import NewsManagerAI
from toontown.ai.FishManagerAI import FishManagerAI
from toontown.distributed.ToontownInternalRepository import ToontownInternalRepository
from toontown.toon import NPCToons
from toontown.hood import TTHoodDataAI, DDHoodDataAI, DGHoodDataAI, BRHoodDataAI, MMHoodDataAI, DLHoodDataAI, OZHoodDataAI, GSHoodDataAI, GZHoodDataAI, SBHoodDataAI, ODGHoodDataAI, ZoneUtil
from toontown.hood import CSHoodDataAI, CashbotHQDataAI, LawbotHQDataAI, BossbotHQDataAI
from toontown.toonbase import ToontownGlobals
from direct.distributed.PyDatagram import *
from otp.ai.AIZoneData import *
from toontown.dna.DNAParser import *
import time
if config.GetBool('want-code-redemption', True):
    from toontown.coderedemption.TTCodeRedemptionMgrAI import TTCodeRedemptionMgrAI
from otp.friends.FriendManagerAI import FriendManagerAI
if config.GetBool('want-estates', True):
    from toontown.estate.EstateManagerAI import EstateManagerAI
if config.GetBool('want-parties', True):
    from toontown.uberdog.DistributedPartyManagerAI import DistributedPartyManagerAI
    from otp.distributed.OtpDoGlobals import *
from direct.task import Task
from toontown.toonbase import ToontownGlobals
from toontown.effects.DistributedFireworkShowAI import DistributedFireworkShowAI
from toontown.effects import FireworkShows
from direct.distributed.ClockDelta import *
from toontown.parties import PartyGlobals
from toontown.quest.QuestManagerAI import QuestManagerAI
from toontown.building.DistributedTrophyMgrAI import DistributedTrophyMgrAI
from toontown.shtiker.CogPageManagerAI import CogPageManagerAI
from toontown.coghq.FactoryManagerAI import FactoryManagerAI
from toontown.coghq.MintManagerAI import MintManagerAI
from toontown.coghq.LawOfficeManagerAI import LawOfficeManagerAI
from toontown.coghq.PromotionManagerAI import PromotionManagerAI
from toontown.coghq.CogSuitManagerAI import CogSuitManagerAI
from toontown.coghq.CountryClubManagerAI import CountryClubManagerAI
from toontown.suit.SuitInvasionManagerAI import SuitInvasionManagerAI
from toontown.tutorial.TutorialManagerAI import TutorialManagerAI
from toontown.catalog.CatalogManagerAI import CatalogManagerAI
if config.GetBool('want-pets', True):
    from toontown.pets.PetManagerAI import PetManagerAI
from otp.ai.MagicWordGlobal import *
import otp.ai.DiagnosticMagicWords
hoods = (
 TTHoodDataAI.TTHoodDataAI, DDHoodDataAI.DDHoodDataAI, DGHoodDataAI.DGHoodDataAI,
 BRHoodDataAI.BRHoodDataAI, MMHoodDataAI.MMHoodDataAI, DLHoodDataAI.DLHoodDataAI,
 GSHoodDataAI.GSHoodDataAI, OZHoodDataAI.OZHoodDataAI, GZHoodDataAI.GZHoodDataAI,
 SBHoodDataAI.SBHoodDataAI, ODGHoodDataAI.ODGHoodDataAI,
 CSHoodDataAI.CSHoodDataAI, CashbotHQDataAI.CashbotHQDataAI,
 LawbotHQDataAI.LawbotHQDataAI, BossbotHQDataAI.BossbotHQDataAI)

class ToontownAIRepository(ToontownInternalRepository):

    def __init__(self, baseChannel, serverId, districtName):
        ToontownInternalRepository.__init__(self, baseChannel, serverId, dcSuffix='AI')
        self.districtName = districtName
        self.zoneAllocator = UniqueIdAllocator(ToontownGlobals.DynamicZonesBegin, ToontownGlobals.DynamicZonesEnd)
        self.zoneId2owner = {}
        NPCToons.generateZone2NpcDict()
        self.hoods = []
        self._dnaStoreMap = {}
        self.zoneDataStore = AIZoneDataStore()
        self.useAllMinigames = self.config.GetBool('want-all-minigames', False)
        self.doLiveUpdates = self.config.GetBool('want-live-updates', True)
        self.fishManager = FishManagerAI()
        self.questManager = QuestManagerAI(self)
        self.cogPageManager = CogPageManagerAI()
        self.factoryMgr = FactoryManagerAI(self)
        self.mintMgr = MintManagerAI(self)
        self.lawOfficeMgr = LawOfficeManagerAI(self)
        self.countryClubMgr = CountryClubManagerAI(self)
        self.promotionMgr = PromotionManagerAI(self)
        self.cogSuitMgr = CogSuitManagerAI(self)
        self.wantCogdominiums = self.config.GetBool('want-cogdominums', False)
        self.statusSender = ShardStatusSender(self)
        self.buildingManagers = {}
        self.suitPlanners = {}

    def getTrackClsends(self):
        return False

    def handleConnected(self):
        ToontownInternalRepository.handleConnected(self)
        self.districtId = self.allocateChannel()
        self.notify.info('Creating district (%d)...' % self.districtId)
        self.distributedDistrict = ToontownDistrictAI(self)
        self.distributedDistrict.setName(self.districtName)
        self.distributedDistrict.generateWithRequiredAndId(self.districtId, self.getGameDoId(), 2)
        self.notify.info('Claiming ownership of district (%d)...' % self.districtId)
        dg = PyDatagram()
        dg.addServerHeader(self.districtId, self.ourChannel, STATESERVER_OBJECT_SET_AI)
        dg.addChannel(self.ourChannel)
        self.send(dg)
        self.notify.info('Creating global objects...')
        self.createGlobals()
        self.notify.info('Creating zones (Playgrounds and Cog HQs)...')
        self.createZones()

    def districtReady(self):
        for sp in self.suitPlanners.values():
            sp.assignInitialSuitBuildings()

        self.statusSender.start()
        self.notify.info('Making district available...')
        self.distributedDistrict.b_setAvailable(1)
        self.notify.info('District is now ready. Have fun in Toontown!')

    def incrementPopulation(self):
        self.districtStats.b_setAvatarCount(self.districtStats.getAvatarCount() + 1)
        self.statusSender.sendStatus()

    def decrementPopulation(self):
        self.districtStats.b_setAvatarCount(self.districtStats.getAvatarCount() - 1)
        self.statusSender.sendStatus()

    def allocateZone(self, owner=None):
        zoneId = self.zoneAllocator.allocate()
        if owner:
            self.zoneId2owner[zoneId] = owner
        return zoneId

    def deallocateZone(self, zone):
        if self.zoneId2owner.get(zone):
            del self.zoneId2owner[zone]
        self.zoneAllocator.free(zone)

    def getZoneDataStore(self):
        return self.zoneDataStore

    def getAvatarExitEvent(self, avId):
        return 'distObjDelete-%d' % avId

    def createGlobals(self):
        self.districtStats = ToontownDistrictStatsAI(self)
        self.districtStats.settoontownDistrictId(self.districtId)
        self.districtStats.generateWithRequiredAndId(self.allocateChannel(), self.getGameDoId(), 3)
        self.notify.info('Created district stats AI (%d).' % self.districtStats.doId)
        self.timeManager = TimeManagerAI(self)
        self.timeManager.generateWithRequired(2)
        self.newsManager = NewsManagerAI(self)
        self.newsManager.generateWithRequired(2)
        self.holidayManager = HolidayManagerAI(self)
        self.suitInvasionManager = SuitInvasionManagerAI(self)
        self.magicWordManager = MagicWordManagerAI(self)
        self.magicWordManager.generateWithRequired(2)
        self.friendManager = FriendManagerAI(self)
        self.friendManager.generateWithRequired(2)
        if config.GetBool('want-code-redemption', True):
            self.codeRedemptionMgr = TTCodeRedemptionMgrAI(self)
            self.codeRedemptionMgr.generateWithRequired(2)
        if config.GetBool('want-parties', True):
            self.partyManager = DistributedPartyManagerAI(self)
            self.partyManager.generateWithRequired(2)
            self.globalPartyMgr = self.generateGlobalObject(OTP_DO_ID_GLOBAL_PARTY_MANAGER, 'GlobalPartyManager')
        if config.GetBool('want-estates', True):
            self.estateManager = EstateManagerAI(self)
            self.estateManager.generateWithRequired(2)
        self.trophyMgr = DistributedTrophyMgrAI(self)
        self.trophyMgr.generateWithRequired(2)
        if config.GetBool('want-pets', True):
            self.petMgr = PetManagerAI(self)
        self.tutorialManager = TutorialManagerAI(self)
        self.tutorialManager.generateWithRequired(2)
        self.catalogManager = CatalogManagerAI(self)
        self.catalogManager.generateWithRequired(2)

    def createZones(self):
        self.zoneTable = {1000: (
                (1000, 1, 0), (1100, 1, 1), (1200, 1, 1), (1300, 1, 1)), 
           2000: (
                (2000, 1, 0), (2100, 1, 1), (2200, 1, 1), (2300, 1, 1)), 
           3000: (
                (3000, 1, 0), (3100, 1, 1), (3200, 1, 1), (3300, 1, 1)), 
           4000: (
                (4000, 1, 0), (4100, 1, 1), (4200, 1, 1), (4300, 1, 1)), 
           5000: (
                (5000, 1, 0), (5100, 1, 1), (5200, 1, 1), (5300, 1, 1)), 
           9000: (
                (9000, 1, 0), (9100, 1, 1), (9200, 1, 1)), 
           6000: ((6000, 1, 0), ), 
           8000: ((8000, 1, 0), ), 
           10000: (), 
           11000: (
                 (11000, 1, 0), (11200, 1, 0)), 
           12000: ((12000, 1, 0), ), 
           13000: ((13000, 1, 0), ), 
           17000: ((17000, 1, 0), ), 
           21000: (
                 (21000, 1, 0), (21300, 1, 0)), 
           1002000: ()}
        self.__nextHood(0)

    def __nextHood(self, hoodIndex):
        if hoodIndex >= len(hoods):
            self.districtReady()
            return Task.done
        self.hoods.append(hoods[hoodIndex](self))
        self.upkeepConnection()
        taskMgr.doMethodLater(0, ToontownAIRepository.__nextHood, 'nextHood', [self, hoodIndex + 1])
        return Task.done

    def dnaStoreMap(self, zone):
        dnaStore = self._dnaStoreMap.get(zone)
        if not dnaStore:
            dnaStore = DNAStorage()
            self.loadDNAFileAI(dnaStore, self.genDNAFileName(zone))
            self._dnaStoreMap[zone] = dnaStore
        return dnaStore

    def genDNAFileName(self, zoneId):
        zoneId = ZoneUtil.getCanonicalZoneId(zoneId)
        hoodId = ZoneUtil.getCanonicalHoodId(zoneId)
        hood = ToontownGlobals.dnaMap[hoodId]
        if hoodId == zoneId:
            zoneId = 'sz'
            phase = ToontownGlobals.phaseMap[hoodId]
        else:
            phase = ToontownGlobals.streetPhaseMap[hoodId]
        return 'phase_%s/dna/%s_%s.pdna' % (phase, hood, zoneId)

    def loadDNAFileAI(self, dnastore, filename):
        return loadDNAFileAI(dnastore, filename)

    def upkeepConnection(self):
        self.readerPollUntilEmpty(None)
        return