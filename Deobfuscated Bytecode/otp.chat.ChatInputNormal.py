# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.chat.ChatInputNormal
# Compiled at: 2014-04-30 09:53:54
from direct.showbase import DirectObject
from otp.otpbase import OTPGlobals
import sys
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from otp.otpbase import OTPLocalizer

class ChatInputNormal(DirectObject.DirectObject):
    ExecNamespace = None

    def __init__(self, chatMgr):
        self.chatMgr = chatMgr
        self.normalPos = Vec3(-1.083, 0, 0.804)
        self.whisperPos = Vec3(0.0, 0, 0.71)
        self.whisperAvatarName = None
        self.whisperAvatarId = None
        self.toPlayer = 0
        wantHistory = 0
        if __dev__:
            wantHistory = 1
        self.wantHistory = config.GetBool('want-chat-history', wantHistory)
        self.history = ['']
        self.historySize = config.GetInt('chat-history-size', 10)
        self.historyIndex = 0
        return

    def typeCallback(self, extraArgs):
        messenger.send('enterNormalChat')

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

    def activateByData(self, whisperAvatarId=None, toPlayer=0):
        self.toPlayer = toPlayer
        self.whisperAvatarId = whisperAvatarId
        if self.whisperAvatarId:
            self.whisperAvatarName = base.talkAssistant.findName(self.whisperAvatarId, self.toPlayer)
            self.chatFrame.setPos(self.whisperPos)
            self.whisperLabel['text'] = OTPLocalizer.ChatInputWhisperLabel % self.whisperAvatarName
            self.whisperLabel.show()
        else:
            self.chatFrame.setPos(self.normalPos)
            self.whisperLabel.hide()
        self.chatEntry['focus'] = 1
        self.chatFrame.show()
        if self.wantHistory:
            self.accept('arrow_up-up', self.getPrevHistory)
            self.accept('arrow_down-up', self.getNextHistory)
        return True

    def deactivate(self):
        self.chatEntry.set('')
        self.chatEntry['focus'] = 0
        self.chatFrame.hide()
        self.whisperLabel.hide()
        base.win.closeIme()
        self.ignore('arrow_up-up')
        self.ignore('arrow_down-up')

    def checkForOverRide(self):
        return False

    def sendChat(self, text):
        if self.checkForOverRide():
            self.chatEntry.enterText('')
            return
        else:
            self.deactivate()
            self.chatMgr.fsm.request('mainMenu')
            if text:
                if self.toPlayer:
                    if self.whisperAvatarId:
                        self.whisperAvatarName = None
                        self.whisperAvatarId = None
                        self.toPlayer = 0
                else:
                    if self.whisperAvatarId:
                        self.chatMgr.sendWhisperString(text, self.whisperAvatarId)
                        self.whisperAvatarName = None
                        self.whisperAvatarId = None
                    else:
                        if self.chatMgr.execChat:
                            if text[0] == '>':
                                text = self.__execMessage(text[1:])
                                base.localAvatar.setChatAbsolute(text, CFSpeech | CFTimeout)
                                return
                        base.talkAssistant.sendOpenTalk(text)
                        if self.wantHistory:
                            self.addToHistory(text)
            return

    def chatOverflow(self, overflowText):
        self.sendChat(self.chatEntry.get())

    def __execMessage(self, message):
        if not ChatInputNormal.ExecNamespace:
            ChatInputNormal.ExecNamespace = {}
            exec 'from pandac.PandaModules import *' in globals(), self.ExecNamespace
            self.importExecNamespace()
        try:
            return str(eval(message, globals(), ChatInputNormal.ExecNamespace))
        except SyntaxError:
            try:
                exec message in globals(), ChatInputNormal.ExecNamespace
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
        self.chatMgr.fsm.request('mainMenu')

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

    def setPos(self, posX, posY=None, posZ=None):
        if posX and posY and posZ:
            self.chatFrame.setPos(posX, posY, posZ)
        else:
            self.chatFrame.setPos(posX)