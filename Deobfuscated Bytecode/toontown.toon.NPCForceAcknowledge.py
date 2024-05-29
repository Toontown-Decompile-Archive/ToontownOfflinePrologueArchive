# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.toon.NPCForceAcknowledge
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from toontown.toontowngui import TTDialog
from toontown.toonbase import TTLocalizer
from direct.gui import DirectLabel
from toontown.quest import Quests

class NPCForceAcknowledge:

    def __init__(self, doneEvent):
        self.doneEvent = doneEvent
        self.dialog = None
        return

    def enter(self):
        doneStatus = {}
        questHistory = base.localAvatar.getQuestHistory()
        imgScale = 0.5
        if questHistory != [] and questHistory != [1000] and questHistory != [101, 110]:
            doneStatus['mode'] = 'complete'
            messenger.send(self.doneEvent, [doneStatus])
        elif len(base.localAvatar.quests) > 1 or len(base.localAvatar.quests) == 0:
            doneStatus['mode'] = 'complete'
            messenger.send(self.doneEvent, [doneStatus])
        elif base.localAvatar.quests[0][0] != Quests.TROLLEY_QUEST_ID:
            doneStatus['mode'] = 'complete'
            messenger.send(self.doneEvent, [doneStatus])
        else:
            base.localAvatar.b_setAnimState('neutral', 1)
            doneStatus['mode'] = 'incomplete'
            self.doneStatus = doneStatus
            imageModel = loader.loadModel('phase_4/models/gui/tfa_images')
            if Quests.avatarHasTrolleyQuest(base.localAvatar):
                if base.localAvatar.quests[0][4] != 0:
                    imgNodePath = imageModel.find('**/hq-dialog-image')
                    imgPos = (0, 0, -0.02)
                    msg = TTLocalizer.NPCForceAcknowledgeMessage2
                else:
                    imgNodePath = imageModel.find('**/trolley-dialog-image')
                    imgPos = (0, 0, 0.04)
                    msg = TTLocalizer.NPCForceAcknowledgeMessage
            self.dialog = TTDialog.TTDialog(text=msg, command=self.handleOk, style=TTDialog.Acknowledge)
            imgLabel = DirectLabel.DirectLabel(parent=self.dialog, relief=None, pos=imgPos, scale=TTLocalizer.NPCFimgLabel, image=imgNodePath, image_scale=imgScale)
        return

    def exit(self):
        if self.dialog:
            self.dialog.cleanup()
            self.dialog = None
        return

    def handleOk(self, value):
        messenger.send(self.doneEvent, [self.doneStatus])