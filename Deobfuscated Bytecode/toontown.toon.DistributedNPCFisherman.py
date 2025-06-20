# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.toon.DistributedNPCFisherman
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.interval.LerpInterval import LerpPosHprInterval
from otp.nametag.NametagConstants import *
from DistributedNPCToonBase import *
from direct.gui.DirectGui import *
from pandac.PandaModules import *
import NPCToons
from toontown.toonbase import TTLocalizer
from toontown.fishing import FishSellGUI
from direct.task.Task import Task
import time

class DistributedNPCFisherman(DistributedNPCToonBase):

    def __init__(self, cr):
        DistributedNPCToonBase.__init__(self, cr)
        self.isLocalToon = 0
        self.av = None
        self.button = None
        self.popupInfo = None
        self.fishGui = None
        self.nextCollision = 0
        return

    def disable(self):
        self.ignoreAll()
        taskMgr.remove(self.uniqueName('popupFishGUI'))
        taskMgr.remove(self.uniqueName('lerpCamera'))
        if self.popupInfo:
            self.popupInfo.destroy()
            self.popupInfo = None
        if self.fishGui:
            self.fishGui.destroy()
            self.fishGui = None
        self.av = None
        if self.isLocalToon:
            base.localAvatar.posCamera(0, 0)
        DistributedNPCToonBase.disable(self)
        return

    def generate(self):
        DistributedNPCToonBase.generate(self)
        self.fishGuiDoneEvent = 'fishGuiDone'

    def announceGenerate(self):
        DistributedNPCToonBase.announceGenerate(self)

    def initToonState(self):
        self.setAnimState('neutral', 1.05, None, None)
        npcOrigin = self.cr.playGame.hood.loader.geom.find('**/npc_fisherman_origin_%s;+s' % self.posIndex)
        print 'fisherman origin: ', npcOrigin
        if not npcOrigin.isEmpty():
            self.reparentTo(npcOrigin)
            self.clearMat()
        else:
            self.notify.warning('announceGenerate: Could not find npc_fisherman_origin_' + str(self.posIndex))
        return

    def getCollSphereRadius(self):
        return 1.0

    def handleCollisionSphereEnter(self, collEntry):
        self.currentTime = time.time()
        if self.nextCollision > self.currentTime:
            self.nextCollision = self.currentTime + 2
        else:
            base.cr.playGame.getPlace().fsm.request('purchase')
            self.sendUpdate('avatarEnter', [])
            self.nextCollision = self.currentTime + 2

    def __handleUnexpectedExit(self):
        self.notify.warning('unexpected exit')
        self.av = None
        return

    def setupAvatars(self, av):
        self.ignoreAvatars()
        av.stopLookAround()
        av.lerpLookAt(Point3(-0.5, 4, 0), time=0.5)
        self.stopLookAround()
        self.lerpLookAt(Point3(av.getPos(self)), time=0.5)

    def resetFisherman(self):
        self.ignoreAll()
        taskMgr.remove(self.uniqueName('popupFishGUI'))
        taskMgr.remove(self.uniqueName('lerpCamera'))
        if self.fishGui:
            self.fishGui.destroy()
            self.fishGui = None
        self.show()
        self.startLookAround()
        self.detectAvatars()
        self.clearMat()
        if self.isLocalToon:
            self.freeAvatar()
        return Task.done

    def setMovie(self, mode, npcId, avId, extraArgs, timestamp):
        timeStamp = ClockDelta.globalClockDelta.localElapsedTime(timestamp)
        self.remain = NPCToons.CLERK_COUNTDOWN_TIME - timeStamp
        self.npcId = npcId
        self.isLocalToon = avId == base.localAvatar.doId
        if mode == NPCToons.SELL_MOVIE_CLEAR:
            return
        else:
            if mode == NPCToons.SELL_MOVIE_TIMEOUT:
                taskMgr.remove(self.uniqueName('lerpCamera'))
                if self.isLocalToon:
                    self.ignore(self.fishGuiDoneEvent)
                    if self.popupInfo:
                        self.popupInfo.reparentTo(hidden)
                    if self.fishGui:
                        self.fishGui.destroy()
                        self.fishGui = None
                self.setChatAbsolute(TTLocalizer.STOREOWNER_TOOKTOOLONG, CFSpeech | CFTimeout)
                self.resetFisherman()
            elif mode == NPCToons.SELL_MOVIE_START:
                self.av = base.cr.doId2do.get(avId)
                if self.av is None:
                    self.notify.warning('Avatar %d not found in doId' % avId)
                    return
                self.accept(self.av.uniqueName('disable'), self.__handleUnexpectedExit)
                self.setupAvatars(self.av)
                if self.isLocalToon:
                    camera.wrtReparentTo(render)
                    quat = Quat()
                    quat.setHpr((-150, -2, 0))
                    camera.posQuatInterval(1, Point3(-5, 9, base.localAvatar.getHeight() - 0.5), quat, other=self, blendType='easeOut').start()
                if self.isLocalToon:
                    taskMgr.doMethodLater(1.0, self.popupFishGUI, self.uniqueName('popupFishGUI'))
            elif mode == NPCToons.SELL_MOVIE_COMPLETE:
                chatStr = TTLocalizer.STOREOWNER_THANKSFISH
                self.setChatAbsolute(chatStr, CFSpeech | CFTimeout)
                self.resetFisherman()
            elif mode == NPCToons.SELL_MOVIE_TROPHY:
                self.av = base.cr.doId2do.get(avId)
                if self.av is None:
                    self.notify.warning('Avatar %d not found in doId' % avId)
                    return
                numFish, totalNumFish = extraArgs
                self.setChatAbsolute(TTLocalizer.STOREOWNER_TROPHY % (numFish, totalNumFish), CFSpeech | CFTimeout)
                self.resetFisherman()
            elif mode == NPCToons.SELL_MOVIE_NOFISH:
                chatStr = TTLocalizer.STOREOWNER_NOFISH
                self.setChatAbsolute(chatStr, CFSpeech | CFTimeout)
                self.resetFisherman()
            elif mode == NPCToons.SELL_MOVIE_NO_MONEY:
                self.notify.warning('SELL_MOVIE_NO_MONEY should not be called')
                self.resetFisherman()
            return

    def __handleSaleDone(self, sell):
        self.ignore(self.fishGuiDoneEvent)
        self.sendUpdate('completeSale', [sell])
        self.fishGui.destroy()
        self.fishGui = None
        return

    def popupFishGUI(self, task):
        self.setChatAbsolute('', CFSpeech)
        self.acceptOnce(self.fishGuiDoneEvent, self.__handleSaleDone)
        self.fishGui = FishSellGUI.FishSellGUI(self.fishGuiDoneEvent)