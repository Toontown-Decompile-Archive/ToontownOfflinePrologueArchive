# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.toontowngui.TTDialog
# Compiled at: 2014-04-30 09:53:54
from otp.otpgui.OTPDialog import *

class TTDialog(OTPDialog):

    def __init__(self, parent=None, style=NoButtons, **kw):
        self.path = 'phase_3/models/gui/dialog_box_buttons_gui'
        OTPDialog.__init__(self, parent, style, **kw)
        self.initialiseoptions(TTDialog)


class TTGlobalDialog(GlobalDialog):

    def __init__(self, message='', doneEvent=None, style=NoButtons, okButtonText=OTPLocalizer.DialogOK, cancelButtonText=OTPLocalizer.DialogCancel, **kw):
        self.path = 'phase_3/models/gui/dialog_box_buttons_gui'
        GlobalDialog.__init__(self, message, doneEvent, style, okButtonText, cancelButtonText, **kw)
        self.initialiseoptions(TTGlobalDialog)