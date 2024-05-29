# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.estate.PlantTreeGUI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.showbase.ShowBase import *
from toontown.toonbase import TTLocalizer
import string
from direct.fsm import StateData
from toontown.toonbase.ToontownBattleGlobals import gagIsPaidOnly
from toontown.toontowngui.TeaserPanel import TeaserPanel

class PlantTreeGUI(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('PlantTreeGUI')

    def __init__(self, doneEvent):
        self.doneEvent = doneEvent
        self.oldActivateMode = base.localAvatar.inventory.activateMode
        self._teaserPanel = None
        base.localAvatar.inventory.setActivateMode('plantTree')
        base.localAvatar.inventory.show()
        self.accept('inventory-selection', self.__handleInventory)
        self.accept('inventory-pass', self.__handleCancel)
        return

    def destroy(self):
        self.ignore('inventory-selection')
        self.ignore('inventory-pass')
        base.localAvatar.inventory.setActivateMode(self.oldActivateMode)
        base.localAvatar.inventory.hide()
        if self._teaserPanel:
            self._teaserPanel.destroy()
            self._teaserPanel = None
        return

    def __handleInventory(self, track, level):
        if base.localAvatar.inventory.numItem(track, level) > 0:
            messenger.send(self.doneEvent, [True, track, level])
        else:
            self.notify.error("An item we don't have: track %s level %s was selected." % (track, level))

    def __handleCancel(self):
        messenger.send(self.doneEvent, [False, None, None])
        return