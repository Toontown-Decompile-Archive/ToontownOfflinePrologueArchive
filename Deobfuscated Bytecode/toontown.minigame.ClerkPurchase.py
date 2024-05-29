# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.ClerkPurchase
# Compiled at: 2014-04-30 09:53:54
from PurchaseBase import *
from toontown.toonbase import ToontownTimer
COUNT_UP_RATE = 0.15
DELAY_BEFORE_COUNT_UP = 1.25
DELAY_AFTER_COUNT_UP = 1.75
COUNT_DOWN_RATE = 0.075
DELAY_AFTER_COUNT_DOWN = 0.0
DELAY_AFTER_CELEBRATE = 3.0

class ClerkPurchase(PurchaseBase):
    activateMode = 'storePurchase'

    def __init__(self, toon, remain, doneEvent):
        PurchaseBase.__init__(self, toon, doneEvent)
        self.remain = remain

    def load(self):
        purchaseModels = loader.loadModel('phase_4/models/gui/gag_shop_purchase_gui')
        PurchaseBase.load(self, purchaseModels)
        self.backToPlayground = DirectButton(parent=self.frame, relief=None, scale=1.04, pos=(0.71,
                                                                                              0,
                                                                                              -0.045), image=(purchaseModels.find('**/PurchScrn_BTN_UP'), purchaseModels.find('**/PurchScrn_BTN_DN'), purchaseModels.find('**/PurchScrn_BTN_RLVR')), text=TTLocalizer.GagShopDoneShopping, text_fg=(0,
                                                                                                                                                                                                                                                                                                    0.1,
                                                                                                                                                                                                                                                                                                    0.7,
                                                                                                                                                                                                                                                                                                    1), text_scale=0.05, text_pos=(0,
                                                                                                                                                                                                                                                                                                                                   0.015,
                                                                                                                                                                                                                                                                                                                                   0), command=self.__handleBackToPlayground)
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.reparentTo(self.frame)
        self.timer.posInTopRightCorner()
        purchaseModels.removeNode()
        return

    def unload(self):
        self.timer.destroy()
        PurchaseBase.unload(self)
        del self.backToPlayground
        del self.timer

    def __handleBackToPlayground(self):
        self.toon.inventory.reparentTo(hidden)
        self.toon.inventory.hide()
        self.handleDone(0)

    def __timerExpired(self):
        self.handleDone(0)

    def enterPurchase(self):
        PurchaseBase.enterPurchase(self)
        self.backToPlayground.reparentTo(self.toon.inventory.storePurchaseFrame)
        self.pointDisplay.reparentTo(self.toon.inventory.storePurchaseFrame)
        self.statusLabel.reparentTo(self.toon.inventory.storePurchaseFrame)
        self.timer.countdown(self.remain, self.__timerExpired)

    def exitPurchase(self):
        PurchaseBase.exitPurchase(self)
        self.backToPlayground.reparentTo(self.frame)
        self.pointDisplay.reparentTo(self.frame)
        self.statusLabel.reparentTo(self.frame)
        self.ignore('purchaseStateChange')