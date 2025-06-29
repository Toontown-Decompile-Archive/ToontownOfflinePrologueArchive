# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.nametag.Nametag
# Compiled at: 2014-04-30 09:53:54
from NametagConstants import *
import NametagGlobals
from otp.margins.ClickablePopup import ClickablePopup
from otp.otpbase import OTPGlobals
from pandac.PandaModules import *

class Nametag(ClickablePopup):
    CName = 1
    CSpeech = 2
    CThought = 4
    NAME_PADDING = 0.2
    CHAT_ALPHA = 1.0
    DEFAULT_CHAT_WORDWRAP = 10.0
    IS_3D = False

    def __init__(self):
        if self.IS_3D:
            ClickablePopup.__init__(self, NametagGlobals.camera)
        else:
            ClickablePopup.__init__(self)
        self.contents = 0
        self.innerNP = NodePath.anyPath(self).attachNewNode('nametag_contents')
        self.wordWrap = 7.5
        self.chatWordWrap = None
        self.font = None
        self.speechFont = None
        self.name = ''
        self.displayName = ''
        self.qtColor = VBase4(1, 1, 1, 1)
        self.colorCode = CCNormal
        self.avatar = None
        self.icon = NodePath('icon')
        self.frame = (0, 0, 0, 0)
        self.nameFg = (0, 0, 0, 1)
        self.nameBg = (1, 1, 1, 1)
        self.chatFg = (0, 0, 0, 1)
        self.chatBg = (1, 1, 1, 1)
        self.chatString = ''
        self.chatFlags = 0
        return

    def destroy(self):
        ClickablePopup.destroy(self)

    def setContents(self, contents):
        self.contents = contents
        self.update()

    def setAvatar(self, avatar):
        self.avatar = avatar

    def setChatWordwrap(self, chatWordWrap):
        self.chatWordWrap = chatWordWrap

    def tick(self):
        pass

    def clickStateChanged(self):
        self.update()

    def getButton(self):
        cs = self.getClickState()
        if self.buttons is None:
            return
        else:
            if cs in self.buttons:
                return self.buttons[cs]
            else:
                return self.buttons.get(0)

            return

    def update(self):
        if self.colorCode in NAMETAG_COLORS:
            cc = self.colorCode
        else:
            cc = CCNormal
        self.nameFg, self.nameBg, self.chatFg, self.chatBg = NAMETAG_COLORS[cc][self.getClickState()]
        self.innerNP.node().removeAllChildren()
        if self.contents & self.CThought and self.chatFlags & CFThought:
            self.showThought()
        elif self.contents & self.CSpeech and self.chatFlags & CFSpeech:
            self.showSpeech()
        elif self.contents & self.CName and self.displayName:
            self.showName()

    def showBalloon(self, balloon, text):
        if not self.speechFont:
            return
        color = self.qtColor if self.chatFlags & CFQuicktalker else self.chatBg
        if color[3] > self.CHAT_ALPHA:
            color = (
             color[0], color[1], color[2], self.CHAT_ALPHA)
        reversed = self.IS_3D and self.chatFlags & CFReversed
        balloon, frame = balloon.generate(text, self.speechFont, textColor=self.chatFg, balloonColor=color, wordWrap=self.chatWordWrap or self.DEFAULT_CHAT_WORDWRAP, button=self.getButton(), reversed=reversed)
        balloon.reparentTo(self.innerNP)
        self.frame = frame

    def showThought(self):
        self.showBalloon(self.getThoughtBalloon(), self.chatString)

    def showSpeech(self):
        self.showBalloon(self.getSpeechBalloon(), self.chatString)

    def showName(self):
        if not self.font:
            return
        self.innerNP.attachNewNode(self.icon)
        t = self.innerNP.attachNewNode(TextNode('name'), 1)
        t.node().setFont(self.font)
        t.node().setAlign(TextNode.ACenter)
        t.node().setWordwrap(self.wordWrap)
        t.node().setText(self.displayName)
        t.setColor(self.nameFg)
        t.setTransparency(self.nameFg[3] < 1.0)
        width, height = t.node().getWidth(), t.node().getHeight()
        t.setY(-0.05)
        t.setAttrib(DepthWriteAttrib.make(0))
        t.setDepthOffset(1)
        panel = NametagGlobals.nametagCardModel.copyTo(self.innerNP, 0)
        panel.setPos((t.node().getLeft() + t.node().getRight()) / 2.0, 0, (t.node().getTop() + t.node().getBottom()) / 2.0)
        panel.setScale(width + self.NAME_PADDING, 1, height + self.NAME_PADDING)
        panel.setColor(self.nameBg)
        panel.setTransparency(self.nameBg[3] < 1.0)
        self.frame = (
         t.node().getLeft() - self.NAME_PADDING / 2.0,
         t.node().getRight() + self.NAME_PADDING / 2.0,
         t.node().getBottom() - self.NAME_PADDING / 2.0,
         t.node().getTop() + self.NAME_PADDING / 2.0)