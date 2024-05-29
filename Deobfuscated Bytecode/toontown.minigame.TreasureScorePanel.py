# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.TreasureScorePanel
# Compiled at: 2014-04-30 09:53:54
from direct.showbase.ShowBaseGlobal import *
from toontown.toonbase.ToontownGlobals import *
from direct.gui.DirectGui import *
from toontown.toon import LaffMeter
from toontown.toonbase import TTLocalizer

class TreasureScorePanel(DirectFrame):

    def __init__(self):
        DirectFrame.__init__(self, relief=None, image_color=GlobalDialogColor, image_scale=(0.24,
                                                                                            1.0,
                                                                                            0.24), image_pos=(0.0,
                                                                                                              0.1,
                                                                                                              0.0))
        self.score = 0
        self.scoreText = DirectLabel(self, relief=None, text=str(self.score), text_scale=0.08, pos=(0.0,
                                                                                                    0.0,
                                                                                                    -0.09))
        self.nameText = DirectLabel(self, relief=None, text=TTLocalizer.DivingGameTreasuresRetrieved, text_scale=0.05, text_pos=(0.0,
                                                                                                                                 0.06), text_wordwrap=7.5, text_shadow=(1,
                                                                                                                                                                        1,
                                                                                                                                                                        1,
                                                                                                                                                                        1))
        self.show()
        return

    def cleanup(self):
        del self.scoreText
        del self.nameText
        self.destroy()

    def incrScore(self):
        self.score += 1
        self.scoreText['text'] = str(self.score)

    def makeTransparent(self, alpha):
        self.setTransparency(1)
        self.setColorScale(1, 1, 1, alpha)