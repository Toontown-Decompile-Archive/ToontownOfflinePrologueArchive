# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.CogNationCentralCogHQLoader
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
import CogHQLoader
from toontown.toonbase import ToontownGlobals
from direct.gui import DirectGui
from toontown.toonbase import TTLocalizer
from toontown.toon import Toon
from direct.fsm import State
from direct.task import Task
import StageInterior, CogNationCentralExterior, CogNationCentralBossBattle, LawbotOfficeExterior
aspectSF = 0.7227

class CogNationCentralCogHQLoader(CogHQLoader.CogHQLoader):
    notify = DirectNotifyGlobal.directNotify.newCategory('CogNationCentralCogHQLoader')

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

        self.musicFile = 'phase_14/audio/bgm/CNC_SZ.ogg'
        self.musicLoopFile = 'phase_14/audio/bgm/CNC_SZ_loop.ogg'
        self.cogHQExteriorModelPath = 'phase_14/models/neighborhoods/toontown_central_takeover'
        self.factoryExteriorModelPath = 'phase_11/models/lawbotHQ/LB_DA_Lobby'
        self.cogHQLobbyModelPath = 'phase_11/models/lawbotHQ/LB_CH_Lobby'
        self.geom = None
        self.factGeom = None
        self.loopMusicTaskName = base.localAvatar.uniqueName('loopMusic')
        return

    def load(self, zoneId):
        CogHQLoader.CogHQLoader.load(self, zoneId)
        Toon.loadSellbotHQAnims()
        self.loopMusic = base.loadMusic(self.musicLoopFile)
        self.loopMusic.stop()
        self.music.play()
        taskMgr.doMethodLater(self.music.length(), self.switchMusic, self.loopMusicTaskName)

    def switchMusic(self, task):
        self.music.stop()
        base.playMusic(self.loopMusic, looping=1, volume=0.8)

    def unloadPlaceGeom(self):
        if self.geom:
            self.geom.removeNode()
            self.geom = None
        CogHQLoader.CogHQLoader.unloadPlaceGeom(self)
        return

    def loadPlaceGeom(self, zoneId):
        self.notify.info('loadPlaceGeom: %s' % zoneId)
        zoneId = zoneId - zoneId % 100
        self.notify.debug('zoneId = %d ToontownGlobals.CogNationCentral=%d' % (zoneId, ToontownGlobals.CogNationCentral))
        if zoneId == ToontownGlobals.CogNationCentral:
            self.geom = loader.loadModel(self.cogHQExteriorModelPath)
        elif zoneId == ToontownGlobals.CogNationCentralOfficeExt:
            self.geom = loader.loadModel(self.factoryExteriorModelPath)
        elif zoneId == ToontownGlobals.CogNationCentralLobby:
            if config.GetBool('want-qa-regression', 0):
                self.notify.info('QA-REGRESSION: COGHQ: Visit CogNationCentralLobby')
            self.notify.debug('cogHQLobbyModelPath = %s' % self.cogHQLobbyModelPath)
            self.geom = loader.loadModel(self.cogHQLobbyModelPath)
        else:
            self.notify.warning('loadPlaceGeom: unclassified zone %s' % zoneId)
        CogHQLoader.CogHQLoader.loadPlaceGeom(self, zoneId)

    def unload(self):
        CogHQLoader.CogHQLoader.unload(self)
        Toon.unloadSellbotHQAnims()
        taskMgr.remove(self.loopMusicTaskName)

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
        return CogNationCentralExterior.CogNationCentralExterior

    def getBossPlaceClass(self):
        self.notify.debug('getBossPlaceClass')
        return CogNationCentralBossBattle.CogNationCentralBossBattle

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
        self.notify.debug('CogNationCentralCogHQLoader.enterCogHQBossBattle')
        CogHQLoader.CogHQLoader.enterCogHQBossBattle(self, requestStatus)
        base.cr.forbidCheesyEffects(1)

    def exitCogHQBossBattle(self):
        self.notify.debug('CogNationCentralCogHQLoader.exitCogHQBossBattle')
        CogHQLoader.CogHQLoader.exitCogHQBossBattle(self)
        base.cr.forbidCheesyEffects(0)