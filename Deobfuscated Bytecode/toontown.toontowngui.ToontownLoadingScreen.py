# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.toontowngui.ToontownLoadingScreen
# Compiled at: 2014-04-30 09:53:54
from direct.gui.DirectGui import *
from panda3d.core import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
import random

class ToontownLoadingScreen:

    def __init__(self):
        self.__expectedCount = 0
        self.__count = 0
        self.gui = loader.loadModel('phase_3/models/gui/progress-background')
        self.tip = DirectLabel(guiId='ToontownLoadingScreenTip', parent=self.gui, relief=None, text='', text_scale=0.05, textMayChange=1, pos=(0.0,
                                                                                                                                               0.0,
                                                                                                                                               -0.95), text_fg=(0.4,
                                                                                                                                                                0.3,
                                                                                                                                                                0.2,
                                                                                                                                                                1), text_align=TextNode.ACenter)
        self.toon = DirectLabel(parent=self.gui, relief=None, pos=(0, 0, 0.8), text='', textMayChange=1, text_scale=0.17, text_fg=(0.952,
                                                                                                                                   0.631,
                                                                                                                                   0.007,
                                                                                                                                   1), text_align=TextNode.ACenter, text_font=ToontownGlobals.getSignFont())
        self.starring = DirectLabel(parent=self.gui, relief=None, pos=(0, 0, 0.7), text='', textMayChange=1, text_scale=0.1, text_fg=(0.968,
                                                                                                                                      0.917,
                                                                                                                                      0.131,
                                                                                                                                      1), text_align=TextNode.ACenter, text_font=ToontownGlobals.getSignFont())
        self.title = DirectLabel(guiId='ToontownLoadingScreenTitle', parent=self.gui, relief=None, pos=(0,
                                                                                                        0,
                                                                                                        -0.77), text='', textMayChange=1, text_scale=0.15, text_fg=(0.9,
                                                                                                                                                                    0.631,
                                                                                                                                                                    0.007,
                                                                                                                                                                    1), text_align=TextNode.ACenter, text_font=ToontownGlobals.getSignFont())
        self.waitBar = DirectWaitBar(guiId='ToontownLoadingScreenWaitBar', parent=self.gui, frameSize=(-1.06,
                                                                                                       1.06,
                                                                                                       -0.03,
                                                                                                       0.03), pos=(0,
                                                                                                                   0,
                                                                                                                   -0.85), text='')
        self.head = None
        if config.GetBool('want-placer-panel', False):
            self.gui.place()
        return

    def destroy(self):
        self.tip.destroy()
        self.toon.destroy()
        self.starring.destroy()
        self.title.destroy()
        self.waitBar.destroy()
        self.gui.removeNode()

    def getTip(self, tipCategory):
        return TTLocalizer.TipTitle + random.choice(TTLocalizer.TipDict.get(tipCategory))

    def resetBackground(self):
        base.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)

    def begin(self, range, label, gui, tipCategory):
        self.waitBar['range'] = range
        self.tip['text'] = self.getTip(tipCategory)
        self.title['text'] = label
        self.__count = 0
        self.__expectedCount = range
        if gui:
            base.setBackgroundColor(Vec4(0.952, 0.796, 0.317, 1))
            if base.localAvatarStyle:
                from toontown.toon import ToonHead
                self.toon['text'] = base.localAvatarName
                self.starring['text'] = TTLocalizer.StarringIn
                self.head = ToonHead.ToonHead()
                self.head.setupHead(base.localAvatarStyle, forGui=1)
                self.head.reparentTo(self.gui)
                self.head.fitAndCenterHead(1, forGui=1)
            self.gui.reparentTo(aspect2dp, NO_FADE_SORT_INDEX)
        else:
            self.waitBar.reparentTo(aspect2dp, NO_FADE_SORT_INDEX)
            self.title.reparentTo(aspect2dp, NO_FADE_SORT_INDEX)
            self.gui.reparentTo(hidden)
        self.waitBar.update(self.__count)

    def end(self):
        self.waitBar.finish()
        self.waitBar.reparentTo(self.gui)
        self.toon.reparentTo(self.gui)
        self.starring.reparentTo(self.gui)
        self.title.reparentTo(self.gui)
        self.gui.reparentTo(hidden)
        self.resetBackground()
        if self.head:
            self.head.delete()
            self.head = None
        return (
         self.__expectedCount, self.__count)

    def abort(self):
        self.gui.reparentTo(hidden)
        self.resetBackground()

    def tick(self):
        self.__count = self.__count + 1
        self.waitBar.update(self.__count)