# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.LawbotCogHQLoader
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
import CogHQLoader
from toontown.toonbase import ToontownGlobals
from direct.gui import DirectGui
from toontown.toonbase import TTLocalizer
from toontown.toon import Toon
from direct.fsm import State
import StageInterior, LawbotHQExterior, LawbotHQBossBattle, LawbotOfficeExterior
aspectSF = 0.7227

class LawbotCogHQLoader(CogHQLoader.CogHQLoader):
    notify = DirectNotifyGlobal.directNotify.newCategory('LawbotCogHQLoader')

    def __init__(self, hood, parentFSMState, doneEvent):
        CogHQLoader.CogHQLoader.__init__(self, hood, parentFSMState, doneEvent)
        self.fsm.addState(State.State('stageInterior', self.enterStageInterior, self.exitStageInterior, ['quietZone', 'cogHQExterior']))
        self.fsm.addState(State.State('factoryExterior', self.enterFactoryExterior, self.exitFactoryExterior, ['quietZone', 'cogHQExterior']))
        for stateName in ['start', 'cogHQExterior', 'quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('stageInterior')

        for stateName in ['quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('factoryExterior')

        self.musicFile = 'phase_11/audio/bgm/LB_courtyard.ogg'
        self.cogHQExteriorModelPath = 'phase_11/models/lawbotHQ/LawbotPlaza'
        self.factoryExteriorModelPath = 'phase_11/models/lawbotHQ/LB_DA_Lobby'
        self.cogHQLobbyModelPath = 'phase_11/models/lawbotHQ/LB_CH_Lobby'
        self.geom = None
        self.factGeom = None
        self.interests = []
        return

    def load(self, zoneId):
        CogHQLoader.CogHQLoader.load(self, zoneId)
        Toon.loadSellbotHQAnims()

    def unloadPlaceGeom(self):
        if self.geom:
            self.geom.removeNode()
            self.geom = None
        CogHQLoader.CogHQLoader.unloadPlaceGeom(self)
        return

    def __handleInterests(self, zoneId):
        taskMgr.doMethodLater(0.1, (lambda t: self.__handleInterestsTask(zoneId, t)), 'lawbotHQ-handleInterests')

    def __handleInterestsTask(self, zoneId, task):
        if zoneId == ToontownGlobals.LawbotHQ:
            for i in range(1, 13):
                self.interests.append(base.cr.addInterest(localAvatar.defaultShard, 13000 + i, 'lawbotHq-%d' % i))

        else:
            for i in self.interests:
                base.cr.removeInterest(i)

            self.interests = []
        return task.done

    def loadPlaceGeom(self, zoneId):
        self.notify.info('loadPlaceGeom: %s' % zoneId)
        zoneId = zoneId - zoneId % 100
        self.__handleInterests(zoneId)
        self.notify.debug('zoneId = %d ToontownGlobals.LawbotHQ=%d' % (zoneId, ToontownGlobals.LawbotHQ))
        if zoneId == ToontownGlobals.LawbotHQ:
            self.geom = loader.loadModel(self.cogHQExteriorModelPath)
            ug = self.geom.find('**/underground')
            ug.setBin('ground', -10)
            brLinkTunnel = self.geom.find('**/TunnelEntrance1')
            brLinkTunnel.setName('linktunnel_br_3326_DNARoot')
        elif zoneId == ToontownGlobals.LawbotOfficeExt:
            self.geom = loader.loadModel(self.factoryExteriorModelPath)
            ug = self.geom.find('**/underground')
            ug.setBin('ground', -10)
        elif zoneId == ToontownGlobals.LawbotLobby:
            if config.GetBool('want-qa-regression', 0):
                self.notify.info('QA-REGRESSION: COGHQ: Visit LawbotLobby')
            self.notify.debug('cogHQLobbyModelPath = %s' % self.cogHQLobbyModelPath)
            self.geom = loader.loadModel(self.cogHQLobbyModelPath)
            ug = self.geom.find('**/underground')
            ug.setBin('ground', -10)
        else:
            self.notify.warning('loadPlaceGeom: unclassified zone %s' % zoneId)
        CogHQLoader.CogHQLoader.loadPlaceGeom(self, zoneId)

    def unload(self):
        CogHQLoader.CogHQLoader.unload(self)
        self.__handleInterests(0)
        Toon.unloadSellbotHQAnims()

    def enterStageInterior(self, requestStatus):
        self.placeClass = StageInterior.StageInterior
        self.stageId = requestStatus['stageId']
        self.enterPlace(requestStatus)

    def exitStageInterior(self):
        self.exitPlace()
        self.placeClass = None
        return

    def getExteriorPlaceClass(self):
        self.notify.debug('getExteriorPlaceClass')
        return LawbotHQExterior.LawbotHQExterior

    def getBossPlaceClass(self):
        self.notify.debug('getBossPlaceClass')
        return LawbotHQBossBattle.LawbotHQBossBattle

    def enterFactoryExterior(self, requestStatus):
        self.placeClass = LawbotOfficeExterior.LawbotOfficeExterior
        self.enterPlace(requestStatus)
        self.hood.spawnTitleText(requestStatus['zoneId'])

    def exitFactoryExterior(self):
        taskMgr.remove('titleText')
        self.hood.hideTitleText()
        self.exitPlace()
        self.placeClass = None
        return

    def enterCogHQBossBattle(self, requestStatus):
        self.notify.debug('LawbotCogHQLoader.enterCogHQBossBattle')
        CogHQLoader.CogHQLoader.enterCogHQBossBattle(self, requestStatus)
        base.cr.forbidCheesyEffects(1)

    def exitCogHQBossBattle(self):
        self.notify.debug('LawbotCogHQLoader.exitCogHQBossBattle')
        CogHQLoader.CogHQLoader.exitCogHQBossBattle(self)
        base.cr.forbidCheesyEffects(0)