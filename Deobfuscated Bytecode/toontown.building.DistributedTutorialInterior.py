# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.building.DistributedTutorialInterior
# Compiled at: 2014-04-30 09:53:54
from toontown.toonbase.ToonBaseGlobal import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from toontown.toonbase import ToontownGlobals
from toontown.toon import NPCToons
import ToonInterior
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
import random, ToonInteriorColors
from toontown.hood import ZoneUtil
from toontown.char import Char
from toontown.suit import SuitDNA
from toontown.suit import Suit
from toontown.quest import QuestParser
from toontown.dna.DNAParser import *
from otp.nametag.NametagConstants import *

class DistributedTutorialInterior(DistributedObject.DistributedObject):

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    def generate(self):
        DistributedObject.DistributedObject.generate(self)

    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        self.setup()

    def disable(self):
        self.interior.removeNode()
        del self.interior
        self.street.removeNode()
        del self.street
        self.sky.removeNode()
        del self.sky
        self.suitWalkTrack.finish()
        del self.suitWalkTrack
        self.suit.delete()
        del self.suit
        self.surlee.delete()
        del self.surlee
        self.ignore('enterTutorialInterior')
        DistributedObject.DistributedObject.disable(self)

    def delete(self):
        DistributedObject.DistributedObject.delete(self)

    def randomDNAItem(self, category, findFunc):
        codeCount = self.dnaStore.getNumCatalogCodes(category)
        index = self.randomGenerator.randint(0, codeCount - 1)
        code = self.dnaStore.getCatalogCode(category, index)
        return findFunc(code)

    def replaceRandomInModel(self, model):
        baseTag = 'random_'
        npc = model.findAllMatches('**/' + baseTag + '???_*')
        for i in range(npc.getNumPaths()):
            np = npc.getPath(i)
            name = np.getName()
            b = len(baseTag)
            category = name[b + 4:]
            key1 = name[b]
            key2 = name[b + 1]
            if key1 == 'm':
                model = self.randomDNAItem(category, self.dnaStore.findNode)
                newNP = model.copyTo(np)
                c = render.findAllMatches('**/collision')
                c.stash()
                if key2 == 'r':
                    self.replaceRandomInModel(newNP)
            elif key1 == 't':
                texture = self.randomDNAItem(category, self.dnaStore.findTexture)
                np.setTexture(texture, 100)
                newNP = np
            if key2 == 'c':
                if category == 'TI_wallpaper' or category == 'TI_wallpaper_border':
                    self.randomGenerator.seed(self.zoneId)
                    newNP.setColorScale(self.randomGenerator.choice(self.colors[category]))
                else:
                    newNP.setColorScale(self.randomGenerator.choice(self.colors[category]))

    def setup(self):
        self.dnaStore = base.cr.playGame.dnaStore
        self.randomGenerator = random.Random()
        self.randomGenerator.seed(self.zoneId)
        self.interior = loader.loadModel('phase_3.5/models/modules/toon_interior_tutorial')
        self.interior.reparentTo(render)
        dnaStore = DNAStorage()
        node = loader.loadDNAFile(self.cr.playGame.hood.dnaStore, 'phase_3.5/dna/tutorial_street.pdna')
        self.street = render.attachNewNode(node)
        self.street.flattenMedium()
        self.street.setPosHpr(-17, 42, -0.5, 180, 0, 0)
        self.street.find('**/tb2:toon_landmark_TT_A1_DNARoot').stash()
        self.street.find('**/tb1:toon_landmark_hqTT_DNARoot/**/door_flat_0').stash()
        self.street.findAllMatches('**/+CollisionNode').stash()
        self.skyFile = 'phase_3.5/models/props/TT_sky'
        self.sky = loader.loadModel(self.skyFile)
        self.sky.setScale(0.8)
        self.sky.reparentTo(render)
        self.sky.setDepthTest(0)
        self.sky.setDepthWrite(0)
        self.sky.setBin('background', 100)
        self.sky.find('**/Sky').reparentTo(self.sky, -1)
        self.surlee = NPCToons.createLocalNPC(2019)
        self.surlee.useLOD(1000)
        self.surlee.setPosHpr(10, 24, 0, -10, 0, 0)
        self.surlee.setH(110)
        self.surlee.head = self.surlee.find('**/__Actor_head')
        self.surlee.initializeBodyCollisions('toon')
        self.surlee.reparentTo(render)
        self.surlee.show()
        self.surlee.addActive()
        self.surlee.startBlink()
        hoodId = ZoneUtil.getCanonicalHoodId(self.zoneId)
        self.colors = ToonInteriorColors.colors[hoodId]
        self.replaceRandomInModel(self.interior)
        doorModelName = 'door_double_round_ul'
        if doorModelName[-1:] == 'r':
            doorModelName = doorModelName[:-1] + 'l'
        else:
            doorModelName = doorModelName[:-1] + 'r'
        door = self.dnaStore.findNode(doorModelName)
        door_origin = render.find('**/door_origin;+s')
        doorNP = door.copyTo(door_origin)
        door_origin.setScale(0.8, 0.8, 0.8)
        door_origin.setPos(door_origin, 0, -0.025, 0)
        color = self.randomGenerator.choice(self.colors['TI_door'])
        DNADoor.setupDoor(doorNP, self.interior, door_origin, self.dnaStore, int(self.block), color)
        doorFrame = doorNP.find('door_*_flat')
        doorFrame.wrtReparentTo(self.interior)
        doorFrame.setColor(color)
        del self.colors
        del self.dnaStore
        del self.randomGenerator
        self.interior.flattenMedium()
        self.createSuit()
        base.localAvatar.setPosHpr(0, 9, 0, -10, 0, 0)
        place = base.cr.playGame.getPlace()
        if place and hasattr(place, 'fsm') and place.fsm.getCurrentState().getName():
            self.notify.info('Tutorial loaded: Ready.')
        else:
            self.notify.info('Tutorial movie: Waiting for place=%s, has fsm=%s' % (place, hasattr(place, 'fsm')))
            if hasattr(place, 'fsm'):
                self.notify.info('Tutorial movie: place state=%s' % place.fsm.getCurrentState().getName())
            self.acceptOnce('enterTutorialInterior')
        self.surleeIntroInterval = Sequence(Func(self.surlee.setChatAbsolute, "Tom, nobody else can know about this. It's extremely important that you--", CFSpeech | CFTimeout), Wait(7), Func(self.surlee.loop, 'walk'), Func(self.surlee.setChatAbsolute, 'Oh, hello there! Looks like we have a new Toon in town.', CFSpeech | CFTimeout), self.surlee.posHprInterval(1, (10,
                                                                                                                                                                                                                                                                                                                                                                              24,
                                                                                                                                                                                                                                                                                                                                                                              0), (150,
                                                                                                                                                                                                                                                                                                                                                                                   0,
                                                                                                                                                                                                                                                                                                                                                                                   0)), Func(self.surlee.loop, 'neutral'), Wait(6), Func(self.surlee.setChatAbsolute, 'Hey, who let you in here anyways?', CFSpeech | CFTimeout), Wait(5), Func(self.surlee.setChatAbsolute, 'Well no matter. Welcome to Toontown!', CFSpeech | CFTimeout), Wait(6), Func(self.surlee.setChatAbsolute, 'Hey Tom, how about you introduce this fine Toon to our town.', CFSpeech | CFTimeout), Wait(6), Func(self.surlee.setChatAbsolute, 'Go talk to Tutorial Tom! Use the arrow keys to move.', CFSpeech | CFTimeout), Wait(6), Func(self.surlee.setChatAbsolute, "While you do that, I'll be observing Tom's performance. Don't mind me!", CFSpeech | CFTimeout), Wait(2), Func(self.surlee.loop, 'walk'), self.surlee.posHprInterval(1, (10,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            24,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            0), (95,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 0,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 0)), Func(self.surlee.loop, 'neutral'))
        self.surleeIntroInterval.start()

    def createSuit(self):
        self.suit = Suit.Suit()
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('f')
        self.suit.setDNA(suitDNA)
        self.suit.loop('neutral')
        self.suit.setPosHpr(-20, 8, 0, 0, 0, 0)
        self.suit.reparentTo(self.interior)
        self.suitWalkTrack = Sequence(self.suit.hprInterval(0.1, Vec3(0, 0, 0)), Func(self.suit.loop, 'walk'), self.suit.posInterval(2, Point3(-20, 20, 0)), Func(self.suit.loop, 'neutral'), Wait(1.0), self.suit.hprInterval(0.1, Vec3(180, 0, 0)), Func(self.suit.loop, 'walk'), self.suit.posInterval(2, Point3(-20, 10, 0)), Func(self.suit.loop, 'neutral'), Wait(1.0))
        self.suitWalkTrack.loop()

    def setZoneIdAndBlock(self, zoneId, block):
        self.zoneId = zoneId
        self.block = block

    def setTutorialNpcId(self, npcId):
        self.npcId = npcId