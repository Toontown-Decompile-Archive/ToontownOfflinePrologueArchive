# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.SellbotCogHQLoader
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
import CogHQLoader
from toontown.toonbase import ToontownGlobals
from direct.gui import DirectGui
from toontown.toonbase import TTLocalizer
from toontown.toon import Toon
from direct.fsm import State
import FactoryExterior, FactoryInterior, SellbotHQExterior, SellbotHQBossBattle
from pandac.PandaModules import DecalEffect
aspectSF = 0.7227

class SellbotCogHQLoader(CogHQLoader.CogHQLoader):
    notify = DirectNotifyGlobal.directNotify.newCategory('SellbotCogHQLoader')

    def __init__(self, hood, parentFSMState, doneEvent):
        CogHQLoader.CogHQLoader.__init__(self, hood, parentFSMState, doneEvent)
        self.fsm.addState(State.State('factoryExterior', self.enterFactoryExterior, self.exitFactoryExterior, ['quietZone', 'factoryInterior', 'cogHQExterior']))
        for stateName in ['start', 'cogHQExterior', 'quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('factoryExterior')

        self.fsm.addState(State.State('factoryInterior', self.enterFactoryInterior, self.exitFactoryInterior, ['quietZone', 'factoryExterior']))
        for stateName in ['quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('factoryInterior')

        self.musicFile = 'phase_9/audio/bgm/encntr_suit_HQ_nbrhood.ogg'
        self.cogHQExteriorModelPath = 'phase_9/models/cogHQ/SellbotHQExterior'
        self.cogHQLobbyModelPath = 'phase_9/models/cogHQ/SellbotHQLobby'
        self.factoryExteriorModelPath = 'phase_9/models/cogHQ/SellbotFactoryExterior'
        self.geom = None
        self.factGeom = None
        self.interests = {'sz': [], 'factExt': []}
        return

    def __handleInterests(self, zoneId):
        taskMgr.doMethodLater(0.1, (lambda t: self.__handleInterestsTask(zoneId, t)), 'sellbotHQ-handleInterests')

    def __handleInterestsTask(self, zoneId, task):
        if zoneId == ToontownGlobals.SellbotHQ:
            for i in range(1, 12) + [50, 51, 52, 99]:
                self.interests['sz'].append(base.cr.addInterest(localAvatar.defaultShard, 11000 + i, 'sellbotHq-%d' % i))

        else:
            for i in self.interests['sz']:
                base.cr.removeInterest(i)

            self.interests['sz'] = []
        if zoneId == ToontownGlobals.SellbotFactoryExt:
            for i in range(1, 14) + range(51, 64):
                self.interests['factExt'].append(base.cr.addInterest(localAvatar.defaultShard, 11200 + i, 'sellbotHq-factExt-%d' % i))

        else:
            for i in self.interests['factExt']:
                base.cr.removeInterest(i)

            self.interests['factExt'] = []
        return task.done

    def load(self, zoneId):
        CogHQLoader.CogHQLoader.load(self, zoneId)
        Toon.loadSellbotHQAnims()

    def unloadPlaceGeom(self):
        if self.geom:
            self.geom.removeNode()
            self.geom = None
        if self.factGeom:
            self.factGeom.removeNode()
            self.factGeom = None
        CogHQLoader.CogHQLoader.unloadPlaceGeom(self)
        return

    def loadPlaceGeom(self, zoneId):
        self.notify.info('loadPlaceGeom: %s' % zoneId)
        zoneId = zoneId - zoneId % 100
        self.__handleInterests(zoneId)
        if zoneId == ToontownGlobals.SellbotHQ:
            self.geom = loader.loadModel(self.cogHQExteriorModelPath)
            dgLinkTunnel = self.geom.find('**/Tunnel1')
            dgLinkTunnel.setName('linktunnel_dg_5316_DNARoot')
            factoryLinkTunnel = self.geom.find('**/Tunnel2')
            factoryLinkTunnel.setName('linktunnel_sellhq_11200_DNARoot')
            cogSignModel = loader.loadModel('phase_4/models/props/sign_sellBotHeadHQ')
            cogSign = cogSignModel.find('**/sign_sellBotHeadHQ')
            cogSignSF = 23
            dgSign = cogSign.copyTo(dgLinkTunnel)
            dgSign.setPosHprScale(0.0, -291.5, 29, 180.0, 0.0, 0.0, cogSignSF, cogSignSF, cogSignSF * aspectSF)
            dgSign.node().setEffect(DecalEffect.make())
            dgText = DirectGui.OnscreenText(text=TTLocalizer.DaisyGardens[-1], font=ToontownGlobals.getSuitFont(), pos=(0,
                                                                                                                        -0.3), scale=TTLocalizer.SCHQLdgText, mayChange=False, parent=dgSign)
            dgText.setDepthWrite(0)
            factorySign = cogSign.copyTo(factoryLinkTunnel)
            factorySign.setPosHprScale(148.625, -155, 27, -90.0, 0.0, 0.0, cogSignSF, cogSignSF, cogSignSF * aspectSF)
            factorySign.node().setEffect(DecalEffect.make())
            factoryTypeText = DirectGui.OnscreenText(text=TTLocalizer.Sellbot, font=ToontownGlobals.getSuitFont(), pos=TTLocalizer.SellbotFactoryPosPart1, scale=TTLocalizer.SellbotFactoryScalePart1, mayChange=False, parent=factorySign)
            factoryTypeText.setDepthWrite(0)
            factoryText = DirectGui.OnscreenText(text=TTLocalizer.Factory, font=ToontownGlobals.getSuitFont(), pos=TTLocalizer.SellbotFactoryPosPart2, scale=TTLocalizer.SellbotFactoryScalePart2, mayChange=False, parent=factorySign)
            factoryText.setDepthWrite(0)
            doors = self.geom.find('**/doors')
            door0 = doors.find('**/door_0')
            door1 = doors.find('**/door_1')
            door2 = doors.find('**/door_2')
            door3 = doors.find('**/door_3')
            index = 0
            for door in [door0,
             door1,
             door2,
             door3]:
                doorFrame = door.find('**/doorDoubleFlat/+GeomNode')
                door.find('**/doorFrameHoleLeft').wrtReparentTo(doorFrame)
                door.find('**/doorFrameHoleRight').wrtReparentTo(doorFrame)
                doorFrame.node().setEffect(DecalEffect.make())
                index += 1

            if self.factGeom:
                self.factGeom.removeNode()
            self.factGeom = loader.loadModel(self.factoryExteriorModelPath)
            self.factGeom.setPos(504.997, -200, -24)
            self.factGeom.setHpr(-90, 0, 0)
            self.factGeom.setScale(0.859913)
            self.factGeom.find('**/tunnel_group2').removeNode()
        elif zoneId == ToontownGlobals.SellbotFactoryExt:
            self.geom = loader.loadModel(self.factoryExteriorModelPath)
            factoryLinkTunnel = self.geom.find('**/tunnel_group2')
            factoryLinkTunnel.setName('linktunnel_sellhq_11000_DNARoot')
            factoryLinkTunnel.find('**/tunnel_sphere').setName('tunnel_trigger')
            cogSignModel = loader.loadModel('phase_4/models/props/sign_sellBotHeadHQ')
            cogSign = cogSignModel.find('**/sign_sellBotHeadHQ')
            cogSignSF = 23
            elevatorSignSF = 15
            hqSign = cogSign.copyTo(factoryLinkTunnel)
            hqSign.setPosHprScale(0.0, -353, 27.5, -180.0, 0.0, 0.0, cogSignSF, cogSignSF, cogSignSF * aspectSF)
            hqSign.node().setEffect(DecalEffect.make())
            hqTypeText = DirectGui.OnscreenText(text=TTLocalizer.Sellbot, font=ToontownGlobals.getSuitFont(), pos=(0,
                                                                                                                   -0.25), scale=0.075, mayChange=False, parent=hqSign)
            hqTypeText.setDepthWrite(0)
            hqText = DirectGui.OnscreenText(text=TTLocalizer.Headquarters, font=ToontownGlobals.getSuitFont(), pos=(0,
                                                                                                                    -0.34), scale=0.1, mayChange=False, parent=hqSign)
            hqText.setDepthWrite(0)
            frontDoor = self.geom.find('**/doorway1')
            fdSign = cogSign.copyTo(frontDoor)
            fdSign.setPosHprScale(62.74, -87.99, 17.26, 2.72, 0.0, 0.0, elevatorSignSF, elevatorSignSF, elevatorSignSF * aspectSF)
            fdSign.node().setEffect(DecalEffect.make())
            fdTypeText = DirectGui.OnscreenText(text=TTLocalizer.Factory, font=ToontownGlobals.getSuitFont(), pos=(0,
                                                                                                                   -0.25), scale=TTLocalizer.SCHQLfdTypeText, mayChange=False, parent=fdSign)
            fdTypeText.setDepthWrite(0)
            fdText = DirectGui.OnscreenText(text=TTLocalizer.SellbotFrontEntrance, font=ToontownGlobals.getSuitFont(), pos=(0,
                                                                                                                            -0.34), scale=TTLocalizer.SCHQLdgText, mayChange=False, parent=fdSign)
            fdText.setDepthWrite(0)
            sideDoor = self.geom.find('**/doorway2')
            sdSign = cogSign.copyTo(sideDoor)
            sdSign.setPosHprScale(-164.78, 26.28, 17.25, -89.89, 0.0, 0.0, elevatorSignSF, elevatorSignSF, elevatorSignSF * aspectSF)
            sdSign.node().setEffect(DecalEffect.make())
            sdTypeText = DirectGui.OnscreenText(text=TTLocalizer.Factory, font=ToontownGlobals.getSuitFont(), pos=(0,
                                                                                                                   -0.25), scale=0.075, mayChange=False, parent=sdSign)
            sdTypeText.setDepthWrite(0)
            sdText = DirectGui.OnscreenText(text=TTLocalizer.SellbotSideEntrance, font=ToontownGlobals.getSuitFont(), pos=(0,
                                                                                                                           -0.34), scale=0.1, mayChange=False, parent=sdSign)
            sdText.setDepthWrite(0)
            self.factGeom = loader.loadModel(self.cogHQExteriorModelPath)
            self.factGeom.setPos(-175, -615, 0)
            self.factGeom.setHpr(90, 0, 0)
            self.factGeom.find('**/Terrain').removeNode()
            self.factGeom.find('**/Props').removeNode()
            self.factGeom.find('**/Tunnels').removeNode()
        elif zoneId == ToontownGlobals.SellbotLobby:
            if config.GetBool('want-qa-regression', 0):
                self.notify.info('QA-REGRESSION: COGHQ: Visit SellbotLobby')
            self.geom = loader.loadModel(self.cogHQLobbyModelPath)
            front = self.geom.find('**/frontWall')
            front.node().setEffect(DecalEffect.make())
            door = self.geom.find('**/door_0')
            parent = door.getParent()
            door.wrtReparentTo(front)
            doorFrame = door.find('**/doorDoubleFlat/+GeomNode')
            door.find('**/doorFrameHoleLeft').wrtReparentTo(doorFrame)
            door.find('**/doorFrameHoleRight').wrtReparentTo(doorFrame)
            doorFrame.node().setEffect(DecalEffect.make())
            door.find('**/leftDoor').wrtReparentTo(parent)
            door.find('**/rightDoor').wrtReparentTo(parent)
        else:
            self.notify.warning('loadPlaceGeom: unclassified zone %s' % zoneId)
        CogHQLoader.CogHQLoader.loadPlaceGeom(self, zoneId)

    def unload(self):
        CogHQLoader.CogHQLoader.unload(self)
        self.__handleInterests(0)
        Toon.unloadSellbotHQAnims()

    def enterFactoryExterior(self, requestStatus):
        self.placeClass = FactoryExterior.FactoryExterior
        self.enterPlace(requestStatus)
        self.hood.spawnTitleText(requestStatus['zoneId'])

    def exitFactoryExterior(self):
        taskMgr.remove('titleText')
        self.hood.hideTitleText()
        self.exitPlace()
        self.placeClass = None
        return

    def enterFactoryInterior(self, requestStatus):
        self.placeClass = FactoryInterior.FactoryInterior
        self.enterPlace(requestStatus)

    def exitFactoryInterior(self):
        self.exitPlace()
        self.placeClass = None
        return

    def getExteriorPlaceClass(self):
        return SellbotHQExterior.SellbotHQExterior

    def getBossPlaceClass(self):
        return SellbotHQBossBattle.SellbotHQBossBattle