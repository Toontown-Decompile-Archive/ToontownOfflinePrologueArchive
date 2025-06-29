# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.safezone.GSSafeZoneLoader
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from pandac.PandaModules import *
from toontown.hood import ZoneUtil
from toontown.launcher import DownloadForceAcknowledge
from toontown.safezone.SafeZoneLoader import SafeZoneLoader
from toontown.safezone.GSPlayground import GSPlayground
from toontown.effects.CarSmoke import CarSmoke
from toontown.toonbase import ToontownGlobals
import random

class GSSafeZoneLoader(SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.musicFile = 'phase_6/audio/bgm/GS_SZ.ogg'
        self.activityMusicFile = 'phase_6/audio/bgm/GS_KartShop.ogg'
        self.dnaFile = 'phase_6/dna/goofy_speedway_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_6/dna/storage_GS_sz.pdna'
        del self.fsm
        self.fsm = ClassicFSM.ClassicFSM('SafeZoneLoader', [State.State('start', self.enterStart, self.exitStart, ['quietZone', 'playground', 'toonInterior']),
         State.State('playground', self.enterPlayground, self.exitPlayground, ['quietZone', 'racetrack']),
         State.State('toonInterior', self.enterToonInterior, self.exitToonInterior, ['quietZone']),
         State.State('quietZone', self.enterQuietZone, self.exitQuietZone, ['playground', 'toonInterior', 'racetrack']),
         State.State('racetrack', self.enterRacetrack, self.exitRacetrack, ['quietZone', 'playground']),
         State.State('final', self.enterFinal, self.exitFinal, ['start'])], 'start', 'final')
        self.smoke = None
        return

    def load(self):
        SafeZoneLoader.load(self)
        if base.cr.newsManager:
            holidayIds = base.cr.newsManager.getDecorationHolidayId()
            if ToontownGlobals.CRASHED_LEADERBOARD in holidayIds:
                self.startSmokeEffect()
        self.birdSound = map(base.loadSfx, ['phase_4/audio/sfx/SZ_TC_bird1.ogg', 'phase_4/audio/sfx/SZ_TC_bird2.ogg', 'phase_4/audio/sfx/SZ_TC_bird3.ogg'])

    def unload(self):
        del self.birdSound
        if self.smoke != None:
            self.stopSmokeEffect()
        SafeZoneLoader.unload(self)
        return

    def enterPlayground(self, requestStatus):
        self.playgroundClass = GSPlayground
        SafeZoneLoader.enterPlayground(self, requestStatus)

    def exitPlayground(self):
        taskMgr.remove('titleText')
        self.hood.hideTitleText()
        SafeZoneLoader.exitPlayground(self)
        self.playgroundClass = None
        return

    def handlePlaygroundDone(self):
        status = self.place.doneStatus
        if self.enteringARace(status) and status.get('shardId') == None:
            zoneId = status['zoneId']
            self.fsm.request('quietZone', [status])
        elif ZoneUtil.getBranchZone(status['zoneId']) == self.hood.hoodId and status['shardId'] == None:
            self.fsm.request('quietZone', [status])
        else:
            self.doneStatus = status
            messenger.send(self.doneEvent)
        return

    def enteringARace(self, status):
        if not status['where'] == 'racetrack':
            return 0
        else:
            if ZoneUtil.isDynamicZone(status['zoneId']):
                return status['hoodId'] == self.hood.hoodId
            return ZoneUtil.getHoodId(status['zoneId']) == self.hood.hoodId

    def enterRacetrack(self, requestStatus):
        self.trackId = requestStatus['trackId']
        self.accept('raceOver', self.handleRaceOver)
        self.accept('leavingRace', self.handleLeftRace)
        base.transitions.fadeOut(t=0)

    def exitRacetrack(self):
        del self.trackId

    def handleRaceOver(self):
        print 'you done!!'

    def handleLeftRace(self):
        req = {'loader': 'safeZoneLoader', 'where': 'playground', 
           'how': 'teleportIn', 
           'zoneId': 8000, 
           'hoodId': 8000, 
           'shardId': None}
        self.fsm.request('quietZone', [req])
        return

    def startSmokeEffect(self):
        if config.GetBool('want-crashedLeaderBoard-Smoke', 1):
            leaderBoard = self.geom.find('**/*crashed*')
            locator = leaderBoard.find('**/*locator_smoke*')
            if locator != None:
                self.smoke = CarSmoke(locator)
                self.smoke.start()
        return

    def stopSmokeEffect(self):
        if config.GetBool('want-crashedLeaderBoard-Smoke', 1):
            if self.smoke != None:
                self.smoke.stop()
                self.smoke.destroy()
                self.smoke = None
        return