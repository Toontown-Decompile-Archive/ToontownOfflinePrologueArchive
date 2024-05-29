# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.safezone.TTSafeZoneLoader
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
import SafeZoneLoader, TTPlayground, random
from toontown.launcher import DownloadForceAcknowledge
from otp.nametag.NametagConstants import *

class TTSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = TTPlayground.TTPlayground
        self.musicFile = 'phase_4/audio/bgm/TC_nbrhood.ogg'
        self.activityMusicFile = 'phase_3.5/audio/bgm/TC_SZ_activity.ogg'
        self.dnaFile = 'phase_4/dna/toontown_central_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_4/dna/storage_TT_sz.pdna'

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.birdSound = map(base.loadSfx, ['phase_4/audio/sfx/SZ_TC_bird1.ogg', 'phase_4/audio/sfx/SZ_TC_bird2.ogg', 'phase_4/audio/sfx/SZ_TC_bird3.ogg'])
        if config.GetBool('want-doomsday-reborn', False):
            linkTunnels = self.geom.findAllMatches('**/linktunnel*')
            for tunnel in linkTunnels:
                tunnel.setName('defunct_tunnel')

            gazebo = self.geom.find('**/*gazebo*')
            gazebo.removeNode()
            floor = self.geom.find('**/mainFloor')
            floortex = self.geom.find('**/mainFloor').findTextureStage('*')
            tex = loader.loadTexture('phase_4/maps/site_plan_no_gazebo.jpg')
            floor.setTexture(floortex, tex, 1)

    def unload(self):
        del self.birdSound
        SafeZoneLoader.SafeZoneLoader.unload(self)

    def enter(self, requestStatus):
        SafeZoneLoader.SafeZoneLoader.enter(self, requestStatus)

    def exit(self):
        SafeZoneLoader.SafeZoneLoader.exit(self)