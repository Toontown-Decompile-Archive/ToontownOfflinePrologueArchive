# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.shtiker.ShtikerPage
# Compiled at: 2014-04-30 09:53:54
import ShtikerBook
from direct.fsm import StateData
from direct.gui.DirectGui import *
from pandac.PandaModules import *

class ShtikerPage(DirectFrame, StateData.StateData):

    def __init__(self):
        DirectFrame.__init__(self, relief=None, sortOrder=DGG.BACKGROUND_SORT_INDEX)
        self.initialiseoptions(ShtikerPage)
        StateData.StateData.__init__(self, 'shtiker-page-done')
        self.book = None
        self.hide()
        return

    def load(self):
        pass

    def unload(self):
        self.ignoreAll()
        del self.book

    def enter(self):
        self.show()

    def exit(self):
        self.hide()

    def setBook(self, book):
        self.book = book

    def setPageName(self, pageName):
        self.pageName = pageName

    def makePageWhite(self, item):
        white = Vec4(1, 1, 1, 1)
        self.book['image_color'] = white
        self.book.nextArrow['image_color'] = white
        self.book.prevArrow['image_color'] = white

    def makePageRed(self, item):
        red = Vec4(1, 0.5, 0.5, 1)
        self.book['image_color'] = red
        self.book.nextArrow['image_color'] = red
        self.book.prevArrow['image_color'] = red