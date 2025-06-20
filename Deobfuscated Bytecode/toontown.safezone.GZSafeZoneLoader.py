# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.safezone.GZSafeZoneLoader
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.gui import DirectGui
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from pandac.PandaModules import *
from toontown.hood import ZoneUtil
from toontown.launcher import DownloadForceAcknowledge
from toontown.safezone.SafeZoneLoader import SafeZoneLoader
from toontown.safezone.GZPlayground import GZPlayground
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
import random

class GZSafeZoneLoader(SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.musicFile = 'phase_6/audio/bgm/GZ_SZ.ogg'
        self.activityMusicFile = 'phase_6/audio/bgm/GS_KartShop.ogg'
        self.dnaFile = 'phase_6/dna/golf_zone_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_6/dna/storage_GZ_sz.pdna'
        del self.fsm
        self.fsm = ClassicFSM.ClassicFSM('SafeZoneLoader', [State.State('start', self.enterStart, self.exitStart, ['quietZone', 'playground', 'toonInterior']),
         State.State('playground', self.enterPlayground, self.exitPlayground, ['quietZone', 'golfcourse']),
         State.State('toonInterior', self.enterToonInterior, self.exitToonInterior, ['quietZone']),
         State.State('quietZone', self.enterQuietZone, self.exitQuietZone, ['playground', 'toonInterior', 'golfcourse']),
         State.State('golfcourse', self.enterGolfCourse, self.exitGolfCourse, ['quietZone', 'playground']),
         State.State('final', self.enterFinal, self.exitFinal, ['start'])], 'start', 'final')

    def load(self):
        SafeZoneLoader.load(self)
        self.birdSound = map(base.loadSfx, ['phase_4/audio/sfx/SZ_TC_bird1.ogg', 'phase_4/audio/sfx/SZ_TC_bird2.ogg', 'phase_4/audio/sfx/SZ_TC_bird3.ogg'])

    def unload(self):
        del self.birdSound
        SafeZoneLoader.unload(self)

    def enterPlayground(self, requestStatus):
        self.playgroundClass = GZPlayground
        SafeZoneLoader.enterPlayground(self, requestStatus)
        top = self.geom.find('**/linktunnel_bosshq_10000_DNARoot')
        sign = top.find('**/Sign_5')
        sign.node().setEffect(DecalEffect.make())
        locator = top.find('**/sign_origin')
        signText = DirectGui.OnscreenText(text=TextEncoder.upper(TTLocalizer.BossbotHQ[-1]), font=ToontownGlobals.getSuitFont(), scale=TTLocalizer.GZSZLsignText, fg=(0,
                                                                                                                                                                      0,
                                                                                                                                                                      0,
                                                                                                                                                                      1), mayChange=False, parent=sign)
        signText.setPosHpr(locator, 0, 0, -0.3, 0, 0, 0)
        signText.setDepthWrite(0)

    def exitPlayground(self):
        taskMgr.remove('titleText')
        self.hood.hideTitleText()
        SafeZoneLoader.exitPlayground(self)
        self.playgroundClass = None
        return

    def handlePlaygroundDone(self):
        status = self.place.doneStatus
        if self.enteringAGolfCourse(status) and status.get('shardId') == None:
            zoneId = status['zoneId']
            self.fsm.request('quietZone', [status])
        elif ZoneUtil.getBranchZone(status['zoneId']) == self.hood.hoodId and status['shardId'] == None:
            self.fsm.request('quietZone', [status])
        else:
            self.doneStatus = status
            messenger.send(self.doneEvent)
        return

    def enteringARace(self, status):
        if not status['where'] == 'golfcourse':
            return 0
        else:
            if ZoneUtil.isDynamicZone(status['zoneId']):
                return status['hoodId'] == self.hood.hoodId
            return ZoneUtil.getHoodId(status['zoneId']) == self.hood.hoodId

    def enteringAGolfCourse(self, status):
        if not status['where'] == 'golfcourse':
            return 0
        else:
            if ZoneUtil.isDynamicZone(status['zoneId']):
                return status['hoodId'] == self.hood.hoodId
            return ZoneUtil.getHoodId(status['zoneId']) == self.hood.hoodId

    def enterGolfCourse(self, requestStatus):
        if requestStatus.has_key('curseId'):
            self.golfCourseId = requestStatus['courseId']
        else:
            self.golfCourseId = 0
        self.accept('raceOver', self.handleRaceOver)
        self.accept('leavingGolf', self.handleLeftGolf)
        base.transitions.irisOut(t=0.2)

    def exitGolfCourse(self):
        del self.golfCourseId

    def handleRaceOver(self):
        print 'you done!!'

    def handleLeftGolf(self):
        req = {'loader': 'safeZoneLoader', 'where': 'playground', 
           'how': 'teleportIn', 
           'zoneId': 17000, 
           'hoodId': 17000, 
           'shardId': None}
        self.fsm.request('quietZone', [req])
        return