# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.safezone.DGSafeZoneLoader
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
import SafeZoneLoader, DGPlayground

class DGSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = DGPlayground.DGPlayground
        self.musicFile = 'phase_8/audio/bgm/DG_nbrhood.ogg'
        self.activityMusicFile = 'phase_8/audio/bgm/DG_SZ.ogg'
        self.dnaFile = 'phase_8/dna/daisys_garden_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_8/dna/storage_DG_sz.pdna'

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.bird1Sound = base.loadSfx('phase_8/audio/sfx/SZ_DG_bird_01.ogg')
        self.bird2Sound = base.loadSfx('phase_8/audio/sfx/SZ_DG_bird_02.ogg')
        self.bird3Sound = base.loadSfx('phase_8/audio/sfx/SZ_DG_bird_03.ogg')
        self.bird4Sound = base.loadSfx('phase_8/audio/sfx/SZ_DG_bird_04.ogg')

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        del self.bird1Sound
        del self.bird2Sound
        del self.bird3Sound
        del self.bird4Sound

    def enter(self, requestStatus):
        SafeZoneLoader.SafeZoneLoader.enter(self, requestStatus)

    def exit(self):
        SafeZoneLoader.SafeZoneLoader.exit(self)