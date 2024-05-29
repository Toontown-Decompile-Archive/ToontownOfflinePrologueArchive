# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.shtiker.NPCFriendPage
# Compiled at: 2014-04-30 09:53:54
import ShtikerPage
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from toontown.toon import NPCFriendPanel
from toontown.toonbase import TTLocalizer

class NPCFriendPage(ShtikerPage.ShtikerPage):

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)

    def load(self):
        self.title = DirectLabel(parent=self, relief=None, text=TTLocalizer.NPCFriendPageTitle, text_scale=0.12, textMayChange=0, pos=(0,
                                                                                                                                       0,
                                                                                                                                       0.6))
        self.friendPanel = NPCFriendPanel.NPCFriendPanel(parent=self)
        self.friendPanel.setScale(0.1225)
        self.friendPanel.setZ(-0.03)
        return

    def unload(self):
        ShtikerPage.ShtikerPage.unload(self)
        del self.title
        del self.friendPanel

    def updatePage(self):
        self.friendPanel.update(base.localAvatar.NPCFriendsDict, fCallable=0)

    def enter(self):
        self.updatePage()
        ShtikerPage.ShtikerPage.enter(self)

    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)