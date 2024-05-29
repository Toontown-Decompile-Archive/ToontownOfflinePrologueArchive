# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.chat.TalkHandle
# Compiled at: 2014-04-30 09:53:54
from otp.avatar.AvatarHandle import AvatarHandle

class TalkHandle(AvatarHandle):

    def __init__(self, doId, message):
        self.avatarId = doId
        self.avatarName = None
        self.accountId = None
        self.accountName = None
        self.addMessageInfo(message)
        return

    def getName(self):
        return self.avatarName

    def isUnderstandable(self):
        return False

    def isOnline(self):
        return False

    def addMessageInfo(self, message):
        if self.avatarId == message.getSenderAvatarId():
            if not self.avatarName and message.getSenderAvatarName():
                self.avatarName = message.getSenderAvatarName()
            if not self.accountId and message.getSenderAccountId():
                self.accountId = message.getSenderAccountId()
            if not self.accountName and message.getSenderAccountName():
                self.accountName = message.getSenderAccountName()
        elif self.avatarId == message.getReceiverAvatarId():
            if not self.avatarName and message.getReceiverAvatarName():
                self.avatarName = message.getReceiverAvatarName()
            if not self.accountId and message.getReceiverAccountId():
                self.accountId = message.getReceiverAccountId()
            if not self.accountName and message.getReceiverAccountName():
                self.accountName = message.getReceiverAccountName()

    def setTalkWhisper(self, fromAV, fromAC, avatarName, chat, mods, flags):
        newText, scrubbed = localAvatar.scrubTalk(chat, mods)
        base.talkAssistant.receiveWhisperTalk(fromAV, avatarName, fromAC, None, self.avatarId, self.getName(), newText, scrubbed)
        return