# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.chat.ChatInputTyped
# Compiled at: 2014-04-30 09:53:54
from direct.showbase import DirectObject
from otp.otpbase import OTPGlobals
import sys
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from otp.otpbase import OTPLocalizer

class ChatInputTyped(DirectObject.DirectObject):
    ExecNamespace = None

    def __init__(self, mainEntry=0):
        self.whisperName = None
        self.whisperId = None
        self.toPlayer = 0
        self.mainEntry = mainEntry
        wantHistory = 0
        if __dev__:
            wantHistory = 1
        self.wantHistory = config.GetBool('want-chat-history', wantHistory)
        self.history = ['']
        self.historySize = config.GetInt('chat-history-size', 10)
        self.historyIndex = 0
        return

    def typeCallback(self, extraArgs):
        self.activate()

    def delete(self):
        self.ignore('arrow_up-up')
        self.ignore('arrow_down-up')
        self.chatFrame.destroy()
        del self.chatFrame
        del self.chatButton
        del self.cancelButton
        del self.chatEntry
        del self.whisperLabel
        del self.chatMgr

    def show(self, whisperId=None, toPlayer=0):
        self.toPlayer = toPlayer
        self.whisperId = whisperId
        self.whisperName = None
        if self.whisperId:
            self.whisperName = base.talkAssistant.findName(whisperId, toPlayer)
            if hasattr(self, 'whisperPos'):
                self.chatFrame.setPos(self.whisperPos)
            self.whisperLabel['text'] = OTPLocalizer.ChatInputWhisperLabel % self.whisperName
            self.whisperLabel.show()
        else:
            if hasattr(self, 'normalPos'):
                self.chatFrame.setPos(self.normalPos)
            self.whisperLabel.hide()
        self.chatEntry['focus'] = 1
        self.chatEntry.set('')
        self.chatFrame.show()
        self.chatEntry.show()
        self.cancelButton.show()
        self.typedChatButton.hide()
        self.typedChatBar.hide()
        if self.wantHistory:
            self.accept('arrow_up-up', self.getPrevHistory)
            self.accept('arrow_down-up', self.getNextHistory)
        return

    def hide(self):
        self.chatEntry.set('')
        self.chatEntry['focus'] = 0
        self.chatFrame.hide()
        self.chatEntry.hide()
        self.cancelButton.hide()
        self.typedChatButton.show()
        self.typedChatBar.show()
        self.ignore('arrow_up-up')
        self.ignore('arrow_down-up')

    def activate(self):
        self.chatEntry.set('')
        self.chatEntry['focus'] = 1
        self.chatFrame.show()
        self.chatEntry.show()
        self.cancelButton.show()
        self.typedChatButton.hide()
        self.typedChatBar.hide()
        if self.whisperId:
            print 'have id'
            if self.toPlayer:
                if not base.talkAssistant.checkWhisperTypedChatPlayer(self.whisperId):
                    messenger.send('Chat-Failed player typed chat test')
                    self.deactivate()
            elif not base.talkAssistant.checkWhisperTypedChatAvatar(self.whisperId):
                messenger.send('Chat-Failed avatar typed chat test')
                self.deactivate()
        elif not base.talkAssistant.checkOpenTypedChat():
            messenger.send('Chat-Failed open typed chat test')
            self.deactivate()

    def deactivate(self):
        self.chatEntry.set('')
        self.chatEntry['focus'] = 0
        self.chatFrame.show()
        self.chatEntry.hide()
        self.cancelButton.hide()
        self.typedChatButton.show()
        self.typedChatBar.show()

    def sendChat(self, text):
        self.deactivate()
        if text:
            if self.toPlayer:
                if self.whisperId:
                    pass
            elif self.whisperId:
                pass
            else:
                if config.GetBool('exec-chat', 0) and text[0] == '>':
                    text = self.__execMessage(text[1:])
                    base.localAvatar.setChatAbsolute(text, CFSpeech | CFTimeout)
                    return
                base.talkAssistant.sendOpenTalk(text)
            if self.wantHistory:
                self.addToHistory(text)
        self.chatEntry.set('')

    def chatOverflow(self, overflowText):
        self.sendChat(self.chatEntry.get())

    def __execMessage(self, message):
        if not ChatInputTyped.ExecNamespace:
            ChatInputTyped.ExecNamespace = {}
            exec 'from pandac.PandaModules import *' in globals(), self.ExecNamespace
            self.importExecNamespace()
        try:
            return str(eval(message, globals(), ChatInputTyped.ExecNamespace))
        except SyntaxError:
            try:
                exec message in globals(), ChatInputTyped.ExecNamespace
                return 'ok'
            except:
                exception = sys.exc_info()[0]
                extraInfo = sys.exc_info()[1]
                if extraInfo:
                    return str(extraInfo)
                return str(exception)

        except:
            exception = sys.exc_info()[0]
            extraInfo = sys.exc_info()[1]
            if extraInfo:
                return str(extraInfo)
            return str(exception)

    def cancelButtonPressed(self):
        self.chatEntry.set('')
        self.deactivate()

    def chatButtonPressed(self):
        self.sendChat(self.chatEntry.get())

    def importExecNamespace(self):
        pass

    def addToHistory(self, text):
        self.history = [
         text] + self.history[:self.historySize - 1]
        self.historyIndex = 0

    def getPrevHistory(self):
        self.chatEntry.set(self.history[self.historyIndex])
        self.historyIndex += 1
        self.historyIndex %= len(self.history)

    def getNextHistory(self):
        self.chatEntry.set(self.history[self.historyIndex])
        self.historyIndex -= 1
        self.historyIndex %= len(self.history)