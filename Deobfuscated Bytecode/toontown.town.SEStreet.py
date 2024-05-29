# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.town.SEStreet
# Compiled at: 2014-04-30 09:53:54
from direct.interval.IntervalGlobal import *
from toontown.toonbase import ToontownGlobals
import Street

class SEStreet(Street.Street):

    def __init__(self, loader, parentFSM, doneEvent):
        Street.Street.__init__(self, loader, parentFSM, doneEvent)
        self.ladderColExists = False
        self.climbSeq = None
        return

    def load(self):
        Street.Street.load(self)
        tunnel = self.loader.geom.find('**/linktunnel_se_14000_DNARoot')
        if tunnel:
            tunnel.removeNode()
        sewer6 = self.loader.geom.find('**/suit_sewer_6_DNARoot')
        if sewer6:
            ladderCol = sewer6.find('**/14100')
            ladderCol.setName('LadderUp')
        else:
            ladderCol = None
        if ladderCol:
            self.accept('enterLadderUp', self.__touchedLadder)
            self.ladderColExists = True
        return

    def __touchedLadder(self, entry):
        sfxClimb = loader.loadSfx('phase_14/audio/sfx/sewer_ladder_climb.ogg')
        self.climbSeq = Sequence(Func(base.localAvatar.setImmortalMode, 1), Func(base.camera.wrtReparentTo, render), Func(base.localAvatar.stopUpdateSmartCamera), Func(base.localAvatar.shutdownSmartCamera), Func(base.camera.setPosHpr, 860.181, 100.567, 2.5, -45.106, 25, 0), Func(base.transitions.letterboxOn), Func(aspect2d.hide), Func(base.localAvatar.disableAvatarControls), Func(base.localAvatar.collisionsOff), Func(base.localAvatar.setPosHpr, 887.181, 129.567, 6.492, -27.106, 0, 0), Func(base.localAvatar.loop, 'climb', toFrame=75, fromFrame=0), Wait(0.3), Func(base.playSfx, sfxClimb), Wait(2.3), Func(base.transitions.fadeOut), Wait(1.0), Func(base.localAvatar.attachCamera), Func(base.localAvatar.initializeSmartCamera), Func(base.localAvatar.startUpdateSmartCamera), Func(base.localAvatar.collisionsOn), Func(base.localAvatar.enableAvatarControls), Func(base.transitions.letterboxOff), Func(aspect2d.show), Func(self.teleportToCNC))
        self.climbSeq.start()

    def teleportToCNC(self):
        try:
            base.cr.playGame.getPlace().handleBookCloseTeleport(ToontownGlobals.CogNationCentral, ToontownGlobals.CogNationCentral)
        except:
            pass

    def unload(self):
        Street.Street.unload(self)
        self.ignore('enterLadderUp')
        base.localAvatar.setImmortalMode(0)
        self.ladderColExists = False
        del self.ladderColExists
        if self.climbSeq:
            self.climbSeq.finish()
        self.climbSeq = None
        del self.climbSeq
        return

    def enterTunnelIn(self, requestStatus):
        self.enterZone(requestStatus['zoneId'])
        self.battlePlace.enterTunnelInSewer(self, requestStatus)