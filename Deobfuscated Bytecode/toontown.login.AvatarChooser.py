# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.login.AvatarChooser
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from toontown.toonbase import ToontownGlobals
import AvatarChoice
from direct.fsm import StateData
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from toontown.launcher import DownloadForceAcknowledge
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer
from toontown.toonbase import DisplayOptions
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import *
from toontown.toon import ToonDNA
import random
MAX_AVATARS = 6
POSITIONS = (Vec3(-0.840167, 0, 0.359333),
 Vec3(0.00933349, 0, 0.306533),
 Vec3(0.862, 0, 0.3293),
 Vec3(-0.863554, 0, -0.445659),
 Vec3(0.00999999, 0, -0.5181),
 Vec3(0.864907, 0, -0.445659))
COLORS = (Vec4(0.917, 0.164, 0.164, 1),
 Vec4(0.152, 0.75, 0.258, 1),
 Vec4(0.598, 0.402, 0.875, 1),
 Vec4(0.133, 0.59, 0.977, 1),
 Vec4(0.895, 0.348, 0.602, 1),
 Vec4(0.977, 0.816, 0.133, 1))
chooser_notify = DirectNotifyGlobal.directNotify.newCategory('AvatarChooser')

class AvatarChooser(StateData.StateData):

    def __init__(self, avatarList, parentFSM, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.choice = None
        self.avatarList = avatarList
        self.displayOptions = None
        self.fsm = ClassicFSM.ClassicFSM('AvatarChooser', [State.State('Choose', self.enterChoose, self.exitChoose, ['CheckDownload']), State.State('CheckDownload', self.enterCheckDownload, self.exitCheckDownload, ['Choose'])], 'Choose', 'Choose')
        self.fsm.enterInitialState()
        self.parentFSM = parentFSM
        self.parentFSM.getCurrentState().addChild(self.fsm)
        base.cr.choseScrooge = False
        self.scroogeExists = False
        self.choseScrooge = False
        return

    def enter(self):
        self.notify.info('AvatarChooser.enter')
        if not self.displayOptions:
            self.displayOptions = DisplayOptions.DisplayOptions()
        self.notify.info('calling self.displayOptions.restrictToEmbedded(False)')
        if base.appRunner:
            self.displayOptions.loadFromSettings()
            self.displayOptions.restrictToEmbedded(False)
        if self.isLoaded == 0:
            self.load()
        base.disableMouse()
        self.title.reparentTo(aspect2d)
        self.quitButton.show()
        if config.GetBool('want-prologue', False):
            self.prologueButton.show()
        if base.cr.loginInterface.supportsRelogin():
            self.logoutButton.show()
        self.pickAToonBG.setBin('background', 1)
        self.pickAToonBG.reparentTo(aspect2d)
        base.setBackgroundColor(Vec4(0.145, 0.368, 0.78, 1))
        choice = config.GetInt('auto-avatar-choice', -1)
        for panel in self.panelList:
            panel.show()
            self.accept(panel.doneEvent, self.__handlePanelDone)
            if panel.position == choice and panel.mode == AvatarChoice.AvatarChoice.MODE_CHOOSE:
                self.__handlePanelDone('chose', panelChoice=choice)

    def exit(self):
        if self.isLoaded == 0:
            return
        else:
            for panel in self.panelList:
                panel.hide()

            self.ignoreAll()
            self.title.reparentTo(hidden)
            self.quitButton.hide()
            self.prologueButton.hide()
            self.logoutButton.hide()
            self.pickAToonBG.reparentTo(hidden)
            base.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)
            return

    def load(self, isPaid):
        if self.isLoaded == 1:
            return
        else:
            self.isPaid = isPaid
            gui = loader.loadModel('phase_3/models/gui/pick_a_toon_gui')
            gui2 = loader.loadModel('phase_3/models/gui/quit_button')
            newGui = loader.loadModel('phase_3/models/gui/tt_m_gui_pat_mainGui')
            self.pickAToonBG = newGui.find('**/tt_t_gui_pat_background')
            self.pickAToonBG.reparentTo(hidden)
            self.pickAToonBG.setPos(0.0, 2.73, 0.0)
            self.pickAToonBG.setScale(1, 1, 1)
            self.title = OnscreenText(TTLocalizer.AvatarChooserPickAToon, scale=TTLocalizer.ACtitle, parent=hidden, font=ToontownGlobals.getSignFont(), fg=(1,
                                                                                                                                                            0.9,
                                                                                                                                                            0.1,
                                                                                                                                                            1), pos=(0.0,
                                                                                                                                                                     0.82))
            quitHover = gui.find('**/QuitBtn_RLVR')
            self.quitButton = DirectButton(image=(quitHover, quitHover, quitHover), relief=None, text=TTLocalizer.AvatarChooserQuit, text_font=ToontownGlobals.getSignFont(), text_fg=(0.977,
                                                                                                                                                                                       0.816,
                                                                                                                                                                                       0.133,
                                                                                                                                                                                       1), text_pos=TTLocalizer.ACquitButtonPos, text_scale=TTLocalizer.ACquitButton, image_scale=1, image1_scale=1.05, image2_scale=1.05, scale=1.05, pos=(-0.253,
                                                                                                                                                                                                                                                                                                                                            0,
                                                                                                                                                                                                                                                                                                                                            0.093), command=self.__handleQuit)
            self.quitButton.flattenMedium()
            self.quitButton.reparentTo(base.a2dBottomRight)
            self.prologueButton = DirectButton(image=(quitHover, quitHover, quitHover), relief=None, text=TTLocalizer.AvatarChooserPrologue, text_font=ToontownGlobals.getSignFont(), text_fg=(0.977,
                                                                                                                                                                                               0.816,
                                                                                                                                                                                               0.133,
                                                                                                                                                                                               1), text_pos=TTLocalizer.ACprologueButtonPos, text_scale=TTLocalizer.ACprologueButton, image_scale=1, image1_scale=1.05, image2_scale=1.05, scale=1.05, pos=(-0.725,
                                                                                                                                                                                                                                                                                                                                                            0,
                                                                                                                                                                                                                                                                                                                                                            0.093), command=self.__handlePrologue)
            self.prologueButton.flattenMedium()
            self.prologueButton.reparentTo(base.a2dBottomRight)
            self.prologueButton.hide()
            self.logoutButton = DirectButton(relief=None, image=(quitHover, quitHover, quitHover), text=TTLocalizer.OptionsPageLogout, text_font=ToontownGlobals.getSignFont(), text_fg=(0.977,
                                                                                                                                                                                         0.816,
                                                                                                                                                                                         0.133,
                                                                                                                                                                                         1), text_scale=TTLocalizer.AClogoutButton, text_pos=(0,
                                                                                                                                                                                                                                              -0.035), pos=(0.163,
                                                                                                                                                                                                                                                            0,
                                                                                                                                                                                                                                                            0.086), image_scale=1.15, image1_scale=1.15, image2_scale=1.18, scale=0.5, command=self.__handleLogoutWithoutConfirm)
            self.logoutButton.reparentTo(base.a2dBottomLeft)
            self.logoutButton.flattenMedium()
            self.logoutButton.hide()
            gui.removeNode()
            gui2.removeNode()
            newGui.removeNode()
            self.panelList = []
            used_position_indexs = []
            for av in self.avatarList:
                if av.position != 6:
                    if base.cr.isPaid():
                        okToLockout = 0
                    else:
                        okToLockout = 1
                    panel = AvatarChoice.AvatarChoice(av, position=av.position, paid=isPaid, okToLockout=okToLockout)
                    panel.setPos(POSITIONS[av.position])
                    used_position_indexs.append(av.position)
                    self.panelList.append(panel)

            for panelNum in range(0, MAX_AVATARS):
                if panelNum not in used_position_indexs:
                    panel = AvatarChoice.AvatarChoice(position=panelNum, paid=isPaid)
                    panel.setPos(POSITIONS[panelNum])
                    self.panelList.append(panel)

            if len(self.avatarList) > 0:
                self.initLookAtInfo()
            self.isLoaded = 1
            return

    def getLookAtPosition(self, toonHead, toonidx):
        lookAtChoice = random.random()
        if len(self.used_panel_indexs) == 1:
            lookFwdPercent = 0.33
            lookAtOthersPercent = 0
        else:
            lookFwdPercent = 0.2
            if len(self.used_panel_indexs) == 2:
                lookAtOthersPercent = 0.4
            else:
                lookAtOthersPercent = 0.65
        lookRandomPercent = 1.0 - lookFwdPercent - lookAtOthersPercent
        if lookAtChoice < lookFwdPercent:
            self.IsLookingAt[toonidx] = 'f'
            return Vec3(0, 1.5, 0)
        else:
            if lookAtChoice < lookRandomPercent + lookFwdPercent or len(self.used_panel_indexs) == 1:
                self.IsLookingAt[toonidx] = 'r'
                return toonHead.getRandomForwardLookAtPoint()
            else:
                other_toon_idxs = []
                for i in range(len(self.IsLookingAt)):
                    if self.IsLookingAt[i] == toonidx:
                        other_toon_idxs.append(i)

                if len(other_toon_idxs) == 1:
                    IgnoreStarersPercent = 0.4
                else:
                    IgnoreStarersPercent = 0.2
                NoticeStarersPercent = 0.5
                bStareTargetTurnsToMe = 0
                if len(other_toon_idxs) == 0 or random.random() < IgnoreStarersPercent:
                    other_toon_idxs = []
                    for i in self.used_panel_indexs:
                        if i != toonidx:
                            other_toon_idxs.append(i)

                    if random.random() < NoticeStarersPercent:
                        bStareTargetTurnsToMe = 1
                if len(other_toon_idxs) == 0:
                    return toonHead.getRandomForwardLookAtPoint()
                lookingAtIdx = random.choice(other_toon_idxs)
                if bStareTargetTurnsToMe:
                    self.IsLookingAt[lookingAtIdx] = toonidx
                    otherToonHead = None
                    for panel in self.panelList:
                        if panel.position == lookingAtIdx:
                            otherToonHead = panel.headModel

                    otherToonHead.doLookAroundToStareAt(otherToonHead, self.getLookAtToPosVec(lookingAtIdx, toonidx))
                self.IsLookingAt[toonidx] = lookingAtIdx
                return self.getLookAtToPosVec(toonidx, lookingAtIdx)

            return

    def getLookAtToPosVec(self, fromIdx, toIdx):
        x = -(POSITIONS[toIdx][0] - POSITIONS[fromIdx][0])
        y = POSITIONS[toIdx][1] - POSITIONS[fromIdx][1]
        z = POSITIONS[toIdx][2] - POSITIONS[fromIdx][2]
        return Vec3(x, y, z)

    def initLookAtInfo(self):
        self.used_panel_indexs = []
        for panel in self.panelList:
            if panel.dna != None:
                self.used_panel_indexs.append(panel.position)

        if len(self.used_panel_indexs) == 0:
            return
        else:
            self.IsLookingAt = []
            for i in range(MAX_AVATARS):
                self.IsLookingAt.append('f')

            for panel in self.panelList:
                if panel.dna != None:
                    panel.headModel.setLookAtPositionCallbackArgs((self, panel.headModel, panel.position))

            return

    def unload(self):
        if self.isLoaded == 0:
            return
        else:
            cleanupDialog('globalDialog')
            for panel in self.panelList:
                panel.destroy()

            del self.panelList
            self.title.removeNode()
            del self.title
            self.quitButton.destroy()
            del self.quitButton
            self.prologueButton.destroy()
            del self.prologueButton
            self.logoutButton.destroy()
            del self.logoutButton
            self.pickAToonBG.removeNode()
            del self.pickAToonBG
            del self.avatarList
            self.parentFSM.getCurrentState().removeChild(self.fsm)
            del self.parentFSM
            del self.fsm
            self.ignoreAll()
            self.isLoaded = 0
            ModelPool.garbageCollect()
            TexturePool.garbageCollect()
            base.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)
            return

    def __handlePanelDone(self, panelDoneStatus, panelChoice=0):
        self.doneStatus = {}
        self.doneStatus['mode'] = panelDoneStatus
        self.choice = panelChoice
        if panelDoneStatus == 'chose':
            self.__handleChoice()
        elif panelDoneStatus == 'nameIt':
            self.__handleCreate()
        elif panelDoneStatus == 'delete':
            self.__handleDelete()
        elif panelDoneStatus == 'create':
            self.__handleCreate()

    def getChoice(self):
        return self.choice

    def __handleChoice(self):
        self.fsm.request('CheckDownload')

    def __handleCreate(self):
        base.transitions.fadeOut(finishIval=EventInterval(self.doneEvent, [self.doneStatus]))

    def __handleDelete(self):
        messenger.send(self.doneEvent, [self.doneStatus])

    def __handleQuit(self):
        cleanupDialog('globalDialog')
        self.doneStatus = {'mode': 'exit'}
        messenger.send(self.doneEvent, [self.doneStatus])

    def __handlePrologue(self):
        base.cr.choseScrooge = True
        for av in self.avatarList:
            if av.position == 6:
                self.scroogeExists = True

        if self.scroogeExists == True:
            self.__handlePanelDone('chose', panelChoice=6)
        else:
            self.choseScrooge = True
            base.cr.skipTutorialRequest = True
            dna = ToonDNA.ToonDNA()
            dna.newToonFromProperties('oll', 'ls', 'l', 'm', 0, 0, 9, 0, 165, 27, 152, 27, 68, 27)
            dna.makeFromNetString(dna.makeNetString())
            self.scroogeSeq = Sequence(Func(base.transitions.fadeOut), Func(base.cr.csm.sendCreateAvatar, dna, '', 6), Wait(1), Func(base.cr.loginFSM.request, 'waitForAvatarList'), Wait(1), Func(self.__handleScroogeEnter))
            self.scroogeSeq.start()

    def enterChoose(self):
        pass

    def exitChoose(self):
        pass

    def enterCheckDownload(self):
        self.accept('downloadAck-response', self.__handleDownloadAck)
        self.downloadAck = DownloadForceAcknowledge.DownloadForceAcknowledge('downloadAck-response')
        self.downloadAck.enter(4)

    def exitCheckDownload(self):
        self.downloadAck.exit()
        self.downloadAck = None
        self.ignore('downloadAck-response')
        return

    def __handleDownloadAck(self, doneStatus):
        if doneStatus['mode'] == 'complete':
            if self.choseScrooge == True:
                messenger.send(self.doneEvent, [self.doneStatus])
            else:
                base.transitions.fadeOut(finishIval=EventInterval(self.doneEvent, [self.doneStatus]))
        else:
            self.fsm.request('Choose')

    def __handleLogoutWithoutConfirm(self):
        base.cr.loginFSM.request('login')

    def __handleScroogeEnter(self):
        if not hasattr(self, 'fsm'):
            self.fsm = ClassicFSM.ClassicFSM('AvatarChooser', [State.State('Choose', self.enterChoose, self.exitChoose, ['CheckDownload']), State.State('CheckDownload', self.enterCheckDownload, self.exitCheckDownload, ['Choose'])], 'Choose', 'Choose')
            self.fsm.enterInitialState()
        base.cr.choseScrooge = True
        self.__handlePanelDone('chose', panelChoice=6)