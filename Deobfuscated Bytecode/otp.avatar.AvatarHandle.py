# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.avatar.AvatarHandle
# Compiled at: 2014-04-30 09:53:54


class AvatarHandle:
    dclassName = 'AvatarHandle'

    def getName(self):
        if __dev__:
            pass
        return ''

    def isOnline(self):
        if __dev__:
            pass
        return False

    def isUnderstandable(self):
        if __dev__:
            pass
        return True

    def setTalkWhisper(self, fromAV, fromAC, avatarName, chat, mods, flags):
        newText, scrubbed = localAvatar.scrubTalk(chat, mods)
        base.talkAssistant.receiveWhisperTalk(fromAV, avatarName, fromAC, None, self.avatarId, self.getName(), newText, scrubbed)
        return