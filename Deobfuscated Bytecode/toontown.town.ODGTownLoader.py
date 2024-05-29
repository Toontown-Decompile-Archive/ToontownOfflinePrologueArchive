# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.town.ODGTownLoader
# Compiled at: 2014-04-30 09:53:54
import TownLoader, ODGStreet
from toontown.suit import Suit

class ODGTownLoader(TownLoader.TownLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        TownLoader.TownLoader.__init__(self, hood, parentFSM, doneEvent)
        self.streetClass = ODGStreet.ODGStreet
        self.musicFile = 'phase_8/audio/bgm/DG_SZ.ogg'
        self.activityMusicFile = 'phase_8/audio/sfx/Silent_sound.ogg'
        self.townStorageDNAFile = 'phase_8/dna/storage_ODG_town.pdna'

    def load(self, zoneId):
        TownLoader.TownLoader.load(self, zoneId)
        Suit.loadSuits(3)
        dnaFile = 'phase_8/dna/old_daisys_garden_' + str(self.canonicalBranchZone) + '.pdna'
        self.createHood(dnaFile)
        if hasattr(self, 'loader'):
            tunnel = self.loader.geom.find('**/prop_safe_zone_tunnel_dummy')
            if tunnel:
                tunnel.reparentTo(hidden)

    def unload(self):
        Suit.unloadSuits(3)
        TownLoader.TownLoader.unload(self)