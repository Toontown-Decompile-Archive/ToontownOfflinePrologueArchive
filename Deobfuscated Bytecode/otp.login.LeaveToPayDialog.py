# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.login.LeaveToPayDialog
# Compiled at: 2014-04-30 09:53:54
from otp.otpbase import OTPGlobals
from otp.otpbase import OTPLauncherGlobals
from otp.otpbase import OTPLocalizer
from direct.gui.DirectGui import *
from pandac.PandaModules import *
import os

class LeaveToPayDialog:

    def __init__(self, paidUser, destructorHook=None, doneFunc=None):
        self.destructorHook = destructorHook
        self.dialog = None
        self.cancelHandler = self.__handleLeaveToPayCancel
        self.paidUser = paidUser
        self.doneFunc = doneFunc
        return

    def setOK(self, handler):
        self.okHandler = handler

    def setCancel(self, handler):
        self.cancelHandler = handler

    def show(self):
        if self.paidUser:
            if base.cr.productName in ('DisneyOnline-AP', 'DisneyOnline-UK', 'JP',
                                       'FR'):
                directFrameText = OTPLocalizer.LeaveToEnableChatUK
                directButtonYesText = OTPLocalizer.LeaveToEnableChatUKYes
            else:
                directFrameText = OTPLocalizer.LeaveToSetParentPassword
                directButtonYesText = OTPLocalizer.LeaveToSetParentPasswordYes
        else:
            directFrameText = OTPLocalizer.LeaveToPay
            directButtonYesText = OTPLocalizer.LeaveToPayYes
        if self.dialog == None:
            buttons = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
            okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
            cancelButtonImage = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr'))
            self.dialog = DirectFrame(parent=aspect2dp, pos=(0.0, 0.0, 0.0), relief=None, image=DGG.getDefaultDialogGeom(), image_color=OTPGlobals.GlobalDialogColor, image_scale=(0.9,
                                                                                                                                                                                   1.0,
                                                                                                                                                                                   0.5), text=directFrameText, text_align=TextNode.ALeft, text_wordwrap=14, text_scale=OTPLocalizer.LTPDdirectFrameText, text_pos=(-0.4,
                                                                                                                                                                                                                                                                                                                   0.15), textMayChange=0)
            DirectButton(self.dialog, image=okButtonImage, relief=None, text=directButtonYesText, text_scale=OTPLocalizer.LTPDdirectButtonYesText, text_pos=(0.0,
                                                                                                                                                             -0.1), textMayChange=0, pos=(0.0,
                                                                                                                                                                                          0.0,
                                                                                                                                                                                          -0.1), command=self.cancelHandler)
            buttons.removeNode()
        self.dialog.show()
        return

    def hide(self):
        self.dialog.hide()

    def destroy(self):
        if self.destructorHook:
            self.destructorHook()
        if self.dialog:
            self.dialog.hide()
            self.dialog.destroy()
        self.destructorHook
        self.dialog = None
        self.okHandler = None
        self.cancelHandler = None
        return

    def removed(self):
        if hasattr(self, 'dialog') and self.dialog:
            return self.dialog.removed()
        else:
            return 1

    def __handleLeaveToPayCancel(self):
        if self.doneFunc:
            self.doneFunc()
        self.destroy()