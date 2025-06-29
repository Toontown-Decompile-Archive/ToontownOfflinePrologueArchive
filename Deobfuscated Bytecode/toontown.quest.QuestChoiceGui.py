# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.quest.QuestChoiceGui
# Compiled at: 2014-04-30 09:53:54
from direct.gui.DirectGui import *
from pandac.PandaModules import *
import QuestPoster
from toontown.toonbase import ToontownTimer
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from direct.directnotify import DirectNotifyGlobal

class QuestChoiceGui(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('QuestChoiceGui')

    def __init__(self):
        DirectFrame.__init__(self, relief=None, parent=base.a2dLeftCenter, geom=DGG.getDefaultDialogGeom(), geom_color=Vec4(0.8, 0.6, 0.4, 1), geom_scale=(1.85,
                                                                                                                                                           1,
                                                                                                                                                           0.9), geom_hpr=(0,
                                                                                                                                                                           0,
                                                                                                                                                                           -90), pos=(0.5,
                                                                                                                                                                                      0,
                                                                                                                                                                                      0))
        self.initialiseoptions(QuestChoiceGui)
        self.questChoicePosters = []
        guiButton = loader.loadModel('phase_3/models/gui/quit_button')
        self.cancelButton = DirectButton(parent=self, relief=None, image=(guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale=(0.7,
                                                                                                                                                                                             1,
                                                                                                                                                                                             1), text=TTLocalizer.QuestChoiceGuiCancel, text_scale=0.06, text_pos=(0,
                                                                                                                                                                                                                                                                   -0.02), command=self.chooseQuest, extraArgs=[0])
        guiButton.removeNode()
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.reparentTo(self)
        self.timer.setScale(0.3)
        base.setCellsAvailable(base.leftCells, 0)
        base.setCellsAvailable([base.bottomCells[0], base.bottomCells[1]], 0)
        return

    def setQuests(self, quests, fromNpcId, timeout):
        for i in range(0, len(quests), 3):
            questId, rewardId, toNpcId = quests[i:i + 3]
            qp = QuestPoster.QuestPoster()
            qp.reparentTo(self)
            qp.showChoicePoster(questId, fromNpcId, toNpcId, rewardId, self.chooseQuest)
            self.questChoicePosters.append(qp)

        if len(quests) == 3:
            self['geom_scale'] = (1, 1, 0.9)
            self.questChoicePosters[0].setPos(0, 0, 0.1)
            self.cancelButton.setPos(0.15, 0, -0.375)
            self.timer.setPos(-0.2, 0, -0.35)
        elif len(quests) == 6:
            self['geom_scale'] = (1.5, 1, 0.9)
            self.questChoicePosters[0].setPos(0, 0, -0.2)
            self.questChoicePosters[1].setPos(0, 0, 0.4)
            self.cancelButton.setPos(0.15, 0, -0.625)
            self.timer.setPos(-0.2, 0, -0.6)
        elif len(quests) == 9:
            self['geom_scale'] = (1.85, 1, 0.9)
            map((lambda x: x.setScale(0.95)), self.questChoicePosters)
            self.questChoicePosters[0].setPos(0, 0, -0.4)
            self.questChoicePosters[1].setPos(0, 0, 0.125)
            self.questChoicePosters[2].setPos(0, 0, 0.65)
            self.cancelButton.setPos(0.15, 0, -0.8)
            self.timer.setPos(-0.2, 0, -0.775)
        self.timer.countdown(timeout, self.timeout)

    def chooseQuest(self, questId):
        if questId != 0:
            if config.GetBool('want-qa-regression', 0):
                self.notify.info('QA-REGRESSION: CREATEATASK: Create A Task.')
        base.setCellsAvailable(base.leftCells, 1)
        base.setCellsAvailable([base.bottomCells[0], base.bottomCells[1]], 1)
        self.timer.stop()
        messenger.send('chooseQuest', [questId])

    def timeout(self):
        messenger.send('chooseQuest', [0])