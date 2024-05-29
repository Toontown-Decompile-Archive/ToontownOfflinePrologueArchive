# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.chat.TTSCWhiteListTerminal
# Compiled at: 2014-04-30 09:53:54
from otp.speedchat.SCTerminal import SCTerminal
from otp.otpbase.OTPLocalizer import SpeedChatStaticText
SCStaticTextMsgEvent = 'SCStaticTextMsg'

def decodeSCStaticTextMsg(textId):
    return SpeedChatStaticText.get(textId, None)


class TTSCWhiteListTerminal(SCTerminal):

    def __init__(self, textId, parentMenu=None):
        SCTerminal.__init__(self)
        self.parentClass = parentMenu
        self.textId = textId
        self.text = SpeedChatStaticText[self.textId]
        print 'SpeedText %s %s' % (self.textId, self.text)

    def handleSelect(self):
        SCTerminal.handleSelect(self)
        if not self.parentClass.whisperAvatarId:
            base.localAvatar.chatMgr.fsm.request('whiteListOpenChat')
        elif self.parentClass.toPlayer:
            base.localAvatar.chatMgr.fsm.request('whiteListPlayerChat', [self.parentClass.whisperAvatarId])
        else:
            base.localAvatar.chatMgr.fsm.request('whiteListAvatarChat', [self.parentClass.whisperAvatarId])