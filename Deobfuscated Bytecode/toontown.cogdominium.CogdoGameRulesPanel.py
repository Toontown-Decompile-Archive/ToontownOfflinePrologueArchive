# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.cogdominium.CogdoGameRulesPanel
# Compiled at: 2014-04-30 09:53:54
from direct.task import Task
from direct.fsm import StateData
from toontown.toonbase.ToontownGlobals import *
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from toontown.toonbase import ToontownTimer
from toontown.toonbase import TTLocalizer
from toontown.minigame import MinigameGlobals

class CogdoGameRulesPanel(StateData.StateData):
    hiddenNode = NodePath('hiddenNode')

    def __init__(self, panelName, gameTitle, instructions, doneEvent, timeout=MinigameGlobals.rulesDuration):
        StateData.StateData.__init__(self, doneEvent)
        self.gameTitle = gameTitle
        self.instructions = instructions
        self.TIMEOUT = timeout

    def load(self):
        minigameGui = loader.loadModel('phase_5/models/cogdominium/tt_m_gui_csa_flyThru')
        self.bg = minigameGui.find('**/background')
        self.chatBubble = minigameGui.find('**/chatBubble')
        self.chatBubble.setScale(6.5, 6.5, 7.3)
        self.chatBubble.setPos(0.32, 0, -0.78)
        self.bg.setScale(5.2)
        self.bg.setPos(0.14, 0, -0.6667)
        self.bg.reparentTo(aspect2d)
        self.chatBubble.reparentTo(aspect2d)
        self.frame = DirectFrame(geom=self.bg, relief=None, pos=(0.2, 0, -0.6667))
        self.gameTitleText = DirectLabel(parent=self.frame, text=self.gameTitle, scale=TTLocalizer.CRPgameTitleText, text_align=TextNode.ACenter, text_font=getSignFont(), text_fg=(1.0,
                                                                                                                                                                                    0.33,
                                                                                                                                                                                    0.33,
                                                                                                                                                                                    1.0), pos=TTLocalizer.CRPgameTitleTextPos, relief=None)
        self.instructionsText = DirectLabel(parent=self.frame, text=self.instructions, scale=TTLocalizer.MRPinstructionsText, text_align=TextNode.ACenter, text_wordwrap=TTLocalizer.MRPinstructionsTextWordwrap, pos=TTLocalizer.MRPinstructionsTextPos, relief=None)
        self.playButton = DirectButton(parent=self.frame, relief=None, geom=(minigameGui.find('**/buttonUp'), minigameGui.find('**/buttonDown'), minigameGui.find('**/buttonHover')), pos=(0.74,
                                                                                                                                                                                           0,
                                                                                                                                                                                           0.1), scale=(4.2,
                                                                                                                                                                                                        5,
                                                                                                                                                                                                        5), command=self.playCallback)
        minigameGui.removeNode()
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.reparentTo(base.a2dTopRight)
        self.timer.setScale(0.4)
        self.timer.setPos(-0.155, 0, -0.155)
        self.frame.hide()
        return

    def unload(self):
        self.frame.destroy()
        self.timer.destroy()
        del self.frame
        del self.gameTitleText
        del self.instructionsText
        self.playButton.destroy()
        del self.playButton
        del self.timer
        self.bg.reparentTo(self.hiddenNode)
        del self.bg
        self.chatBubble.reparentTo(self.hiddenNode)
        del self.chatBubble

    def enter(self):
        self.frame.show()
        self.timer.countdown(self.TIMEOUT, self.playCallback)
        self.accept('enter', self.playCallback)

    def exit(self):
        self.frame.hide()
        self.timer.stop()
        self.ignore('enter')
        self.bg.hide()
        self.chatBubble.hide()

    def playCallback(self):
        messenger.send(self.doneEvent)