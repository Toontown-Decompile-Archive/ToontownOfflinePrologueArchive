# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.reborn.DistributedSafezoneInvasionReborn
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.distributed.DistributedObject import DistributedObject
from direct.interval.IntervalGlobal import *
from toontown.toonbase import ToontownGlobals
from otp.avatar import Emote
from toontown.toontowngui import TTDialog
import webbrowser, SafezoneInvasionRebornGlobals

class DistributedSafezoneInvasionReborn(DistributedObject):
    deferFor = 1

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        cr.invasion = self
        self.invasionOn = False
        self.accept('localPieSplat', self.__localPieSplat)
        self.accept('enterSuitAttack', self.__localToonHit)
        self.showFloor = base.render.find('**/ShowFloor')
        self.geom = base.cr.playGame.hood.loader.geom
        base.cr.playGame.hood.loader.music.stop()
        self.musicEnter = base.loadMusic(SafezoneInvasionRebornGlobals.InvasionMusicEnter)
        self.victoryMusic = base.loadMusic('phase_9/audio/bgm/CogHQ_finale.ogg')

    def delete(self):
        self.cr.invasion = None
        if self.invasionOn:
            del self.musicEnter
        DistributedObject.delete(self)
        self.ignoreAll()
        return

    def setInvasionStarted(self, started):
        if started and not self.invasionOn:
            base.playMusic(self.musicEnter, looping=1, volume=1.0)
        elif not started and self.invasionOn:
            self.endInvasion()
        else:
            return
        self.invasionOn = started

    def endInvasion(self):
        base.playMusic(self.victoryMusic, looping=0, volume=0.9)
        self.victoryIval = Sequence(Func(Emote.globalEmote.disableAll, base.localAvatar, 'dbattle, enterReward'), Func(base.localAvatar.disableAvatarControls), Func(base.localAvatar.b_setEmoteState, 6, 1.0), Wait(5.15), Func(Emote.globalEmote.releaseAll, base.localAvatar, 'dbattle, enterReward'), Func(base.localAvatar.enableAvatarControls))
        self.victoryIval.start()

    def startCogSky(self):
        self.fadeIn.start()
        self.cogSkyBegin.start()
        self.cogSkyBeginStage.start()

    def stopCogSky(self):
        if self.invasionOn:
            cogSkySequence = Sequence(Func(self.cogSkyEnd.start), Func(self.cogSkyEndStage.start), Func(self.fadeOut.start), Wait(7), Func(self.sky.removeNode))

    def stopMusic(self):
        self.musicEnter.stop()

    def showThanks(self):
        self.confirm = TTDialog.TTGlobalDialog(doneEvent='confirmDone', message=SafezoneInvasionRebornGlobals.Thanks, style=TTDialog.Acknowledge, suppressKeys=True)
        self.confirm.show()
        self.accept('confirmDone', self.handleConfirm)

    def handleConfirm(self):
        status = self.confirm.doneStatus
        self.ignore('confirmDone')
        self.confirm.cleanup()
        del self.confirm
        if status == 'ok':
            webbrowser.open('http://toontownrewritten.com')
            abort()

    def __localPieSplat(self, pieCode, entry):
        if pieCode == ToontownGlobals.PieCodeToon:
            avatarDoId = entry.getIntoNodePath().getNetTag('avatarDoId')
            if avatarDoId == '':
                self.notify.warning('Toon %s has no avatarDoId tag.' % repr(entry.getIntoNodePath()))
                return
            doId = int(avatarDoId)
            if doId != localAvatar.doId:
                self.d_pieHitToon(doId)
        elif pieCode == ToontownGlobals.PieCodeInvasionSuit:
            avatarDoId = entry.getIntoNodePath().getNetTag('avatarDoId')
            if avatarDoId == '':
                self.notify.warning('Suit %s has no avatarDoId tag.' % repr(entry.getIntoNodePath()))
                return
            doId = int(avatarDoId)
            if doId != localAvatar.doId:
                self.d_pieHitSuit(doId)

    def __localToonHit(self, entry):
        damage = int(entry.getIntoNode().getTag('damage'))
        self.d_takeDamage(damage)

    def d_pieHitToon(self, doId):
        self.sendUpdate('pieHitToon', [doId])

    def d_pieHitSuit(self, doId):
        self.sendUpdate('pieHitSuit', [doId])

    def d_takeDamage(self, damage):
        self.sendUpdate('takeDamage', [damage])