# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.toon.DistributedNPCScientist
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from toontown.toonbase import TTLocalizer, ToontownGlobals
import DistributedNPCToonBase

class DistributedNPCScientist(DistributedNPCToonBase.DistributedNPCToonBase):

    def __init__(self, cr):
        DistributedNPCToonBase.DistributedNPCToonBase.__init__(self, cr)
        if base.cr.newsManager.isHolidayRunning(ToontownGlobals.SILLYMETER_HOLIDAY) or base.cr.newsManager.isHolidayRunning(ToontownGlobals.SILLYMETER_EXT_HOLIDAY):
            self.show()
        else:
            self.hide()
        self.accept('SillyMeterIsRunning', self.sillyMeterIsRunning)

    def disable(self):
        self.ignore('SillyMeterIsRunning')
        DistributedNPCToonBase.DistributedNPCToonBase.disable(self)

    def sillyMeterIsRunning(self, isRunning):
        if isRunning:
            self.show()
        else:
            self.hide()

    def getCollSphereRadius(self):
        return 2.5

    def initPos(self):
        self.setHpr(180, 0, 0)
        self.setScale(1.0)

    def handleCollisionSphereEnter(self, collEntry):
        self.nametag3d.setDepthTest(0)
        self.nametag3d.setBin('fixed', 0)

    def setChat(self, topic, partPos, partId, progress, flags):
        msg = TTLocalizer.toontownDialogues[topic][(partPos, partId)][progress]
        self.setChatMuted(msg, flags)

    def announceGenerate(self):
        DistributedNPCToonBase.DistributedNPCToonBase.announceGenerate(self)
        if base.cr.newsManager.isHolidayRunning(ToontownGlobals.SILLYMETER_HOLIDAY) or base.cr.newsManager.isHolidayRunning(ToontownGlobals.SILLYMETER_EXT_HOLIDAY):
            self.show()
        else:
            self.hide()

    def generateToon(self):
        self.setLODs()
        self.generateToonLegs()
        self.generateToonHead()
        self.generateToonTorso()
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.resetHeight()
        self.rightHands = []
        self.leftHands = []
        self.headParts = []
        self.hipsParts = []
        self.torsoParts = []
        self.legsParts = []
        self.__bookActors = []
        self.__holeActors = []
        self.setupToonNodes()
        if self.style.getTorsoSize() == 'short' and self.style.getAnimal() == 'duck':
            sillyReader = loader.loadModel('phase_4/models/props/tt_m_prp_acs_sillyReader')
            for rHand in self.getRightHands():
                placeholder = rHand.attachNewNode('SillyReader')
                sillyReader.instanceTo(placeholder)
                placeholder.setH(180)
                placeholder.setScale(render, 1.0)
                placeholder.setPos(0, 0, 0.1)

        elif self.style.getTorsoSize() == 'long' and self.style.getAnimal() == 'monkey' or self.style.getTorsoSize() == 'medium' and self.style.getAnimal() == 'horse':
            clipBoard = loader.loadModel('phase_4/models/props/tt_m_prp_acs_clipboard')
            for rHand in self.getRightHands():
                placeholder = rHand.attachNewNode('ClipBoard')
                clipBoard.instanceTo(placeholder)
                placeholder.setH(180)
                placeholder.setScale(render, 1.0)
                placeholder.setPos(0, 0, 0.1)

    def startLookAround(self):
        pass

    def scientistPlay(self):
        if self.style.getTorsoSize() == 'short' and self.style.getAnimal() == 'duck':
            sillyReaders = self.findAllMatches('**/SillyReader')
            for sillyReader in sillyReaders:
                if not sillyReader.isEmpty():
                    sillyReader.stash()
                sillyReader = None

        elif self.style.getTorsoSize() == 'long' and self.style.getAnimal() == 'monkey':
            clipBoards = self.findAllMatches('**/ClipBoard')
            for clipBoard in clipBoards:
                if not clipBoard.isEmpty():
                    clipBoard.stash()
                clipBoard = None

        return

    def showScientistProp(self):
        if self.style.getTorsoSize() == 'short' and self.style.getAnimal() == 'duck':
            sillyReaders = self.findAllMatches('**/SillyReader;+s')
            for sillyReader in sillyReaders:
                if not sillyReader.isEmpty():
                    sillyReader.unstash()
                sillyReader = None

        elif self.style.getTorsoSize() == 'long' and self.style.getAnimal() == 'monkey':
            clipBoards = self.findAllMatches('**/ClipBoard;+s')
            for clipBoard in clipBoards:
                if not clipBoard.isEmpty():
                    clipBoard.unstash()
                clipBoard = None

        return