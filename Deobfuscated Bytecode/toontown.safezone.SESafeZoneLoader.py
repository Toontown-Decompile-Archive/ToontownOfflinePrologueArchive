# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.safezone.SESafeZoneLoader
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
import SafeZoneLoader, SEPlayground

class SESafeZoneLoader(SafeZoneLoader.SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = SEPlayground.SEPlayground
        self.musicFile = 'phase_14/audio/bgm/SE_nbrhood.ogg'
        self.activityMusicFile = 'phase_14/audio/bgm/SE_SZ.ogg'
        self.dnaFile = 'phase_14/dna/sewer_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_14/dna/storage_SE.pdna'

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.setupCage()

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        self.cageModel.removeNode()
        del self.cageModel

    def enter(self, requestStatus):
        SafeZoneLoader.SafeZoneLoader.enter(self, requestStatus)

    def exit(self):
        SafeZoneLoader.SafeZoneLoader.exit(self)

    def setupCage(self):
        self.cageModel = loader.loadModel('phase_14/models/props/outpost_cage')
        self.cageModel.reparentTo(self.geom)
        self.cageModel.setPos(0, 2.5, 0)