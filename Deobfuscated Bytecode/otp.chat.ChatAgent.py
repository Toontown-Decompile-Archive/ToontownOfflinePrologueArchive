# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.chat.ChatAgent
# Compiled at: 2014-04-30 09:53:54
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from pandac.PandaModules import *
from otp.otpbase import OTPGlobals
from otp.ai.MagicWordGlobal import *

class ChatAgent(DistributedObjectGlobal):

    def __init__(self, cr):
        DistributedObjectGlobal.__init__(self, cr)
        self.chatMode = 0

    def delete(self):
        self.ignoreAll()
        self.cr.chatManager = None
        self.cr.chatAgent = None
        DistributedObjectGlobal.delete(self)
        return

    def adminChat(self, aboutId, message):
        self.notify.warning('Admin Chat(%s): %s' % (aboutId, message))
        messenger.send('adminChat', [aboutId, message])

    def sendChatMessage(self, message):
        self.sendUpdate('chatMessage', [message, self.chatMode])

    def sendWhisperMessage(self, receiverAvId, message):
        self.sendUpdate('whisperMessage', [receiverAvId, message])

    def sendSFWhisperMessage(self, receiverAvId, message):
        self.sendUpdate('sfWhisperMessage', [receiverAvId, message])


@magicWord(category=CATEGORY_MODERATION, types=[int])
def chatmode(mode=-1):
    mode2name = {0: 'user', 
       1: 'moderator', 
       2: 'administrator', 
       3: 'system administrator'}
    if base.cr.chatAgent is None:
        return 'No ChatAgent found.'
    else:
        if mode == -1:
            return 'You are currently talking in the %s chat mode.' % mode2name.get(base.cr.chatAgent.chatMode, 'N/A')
        if not 0 <= mode <= 3:
            return 'Invalid chat mode specified.'
        if mode == 3 and spellbook.getInvoker().getAdminAccess() < 500:
            return 'Chat mode 3 is reserved for system administrators.'
        if mode == 2 and spellbook.getInvoker().getAdminAccess() < 400:
            return 'Chat mode 2 is reserved for administrators.'
        if mode == 1 and spellbook.getInvoker().getAdminAccess() < 200:
            return 'Chat mode 1 is reserved for moderators.'
        base.cr.chatAgent.chatMode = mode
        return 'You are now talking in the %s chat mode.' % mode2name.get(mode, 'N/A')