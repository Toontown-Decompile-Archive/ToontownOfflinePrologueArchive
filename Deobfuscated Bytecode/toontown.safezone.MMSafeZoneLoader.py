# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.safezone.MMSafeZoneLoader
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
import SafeZoneLoader, MMPlayground
from toontown.toonbase import ToontownGlobals

class MMSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = MMPlayground.MMPlayground
        self.musicFile = 'phase_6/audio/bgm/MM_nbrhood.ogg'
        self.activityMusicFile = 'phase_6/audio/bgm/MM_SZ_activity.ogg'
        self.dnaFile = 'phase_6/dna/minnies_melody_land_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_6/dna/storage_MM_sz.pdna'

    def load(self):
        print 'loading MM safezone'
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.piano = self.geom.find('**/center_icon')
        if self.piano.isEmpty():
            self.notify.error('Piano not found')
        else:
            hq = self.geom.find('**/*toon_landmark_hqMM_DNARoot')
            hq.wrtReparentTo(self.piano)

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        del self.piano