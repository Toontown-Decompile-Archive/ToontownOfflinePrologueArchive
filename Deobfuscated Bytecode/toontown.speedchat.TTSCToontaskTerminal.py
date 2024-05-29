# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.speedchat.TTSCToontaskTerminal
# Compiled at: 2014-04-30 09:53:54
from otp.speedchat.SCTerminal import *
from toontown.quest import Quests
from toontown.toon import NPCToons
TTSCToontaskMsgEvent = 'SCToontaskMsg'

def decodeTTSCToontaskMsg(taskId, toNpcId, toonProgress, msgIndex):
    q = Quests.getQuest(taskId)
    if q is None:
        return
    else:
        name = NPCToons.getNPCName(toNpcId)
        if name is None:
            return
        msgs = q.getSCStrings(toNpcId, toonProgress)
        if type(msgs) != type([]):
            msgs = [
             msgs]
        if msgIndex >= len(msgs):
            return
        return msgs[msgIndex]


class TTSCToontaskTerminal(SCTerminal):

    def __init__(self, msg, taskId, toNpcId, toonProgress, msgIndex):
        SCTerminal.__init__(self)
        self.msg = msg
        self.taskId = taskId
        self.toNpcId = toNpcId
        self.toonProgress = toonProgress
        self.msgIndex = msgIndex

    def getDisplayText(self):
        return self.msg

    def handleSelect(self):
        SCTerminal.handleSelect(self)
        messenger.send(self.getEventName(TTSCToontaskMsgEvent), [self.taskId,
         self.toNpcId,
         self.toonProgress,
         self.msgIndex])