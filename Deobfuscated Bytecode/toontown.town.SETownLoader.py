# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.town.SETownLoader
# Compiled at: 2014-04-30 09:53:54
import TownLoader, SEStreet
from toontown.suit import Suit

class SETownLoader(TownLoader.TownLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        TownLoader.TownLoader.__init__(self, hood, parentFSM, doneEvent)
        self.streetClass = SEStreet.SEStreet
        self.musicFile = 'phase_14/audio/bgm/SE_SZ.ogg'
        self.activityMusicFile = 'phase_14/audio/bgm/SE_SZ.ogg'
        self.townStorageDNAFile = 'phase_14/dna/storage_SE.pdna'

    def load(self, zoneId):
        TownLoader.TownLoader.load(self, zoneId)
        Suit.loadSuits(3)
        dnaFile = 'phase_14/dna/sewer_' + str(self.canonicalBranchZone) + '.pdna'
        self.createHood(dnaFile)

    def unload(self):
        Suit.unloadSuits(3)
        TownLoader.TownLoader.unload(self)