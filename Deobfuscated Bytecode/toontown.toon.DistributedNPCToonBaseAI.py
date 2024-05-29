# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.toon.DistributedNPCToonBaseAI
# Compiled at: 2014-04-30 09:53:54
from otp.ai.AIBaseGlobal import *
from pandac.PandaModules import *
import DistributedToonAI
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.distributed import ClockDelta
from toontown.toonbase import ToontownGlobals
import NPCToons
from direct.task import Task
from toontown.quest import Quests

class DistributedNPCToonBaseAI(DistributedToonAI.DistributedToonAI):

    def __init__(self, air, npcId, questCallback=None):
        DistributedToonAI.DistributedToonAI.__init__(self, air)
        self.air = air
        self.npcId = npcId
        self.busy = 0
        self.questCallback = questCallback
        self.givesQuests = 1

    def delete(self):
        taskMgr.remove(self.uniqueName('clearMovie'))
        DistributedToonAI.DistributedToonAI.delete(self)

    def _doPlayerEnter(self):
        pass

    def _doPlayerExit(self):
        pass

    def _announceArrival(self):
        pass

    def isPlayerControlled(self):
        return False

    def getHq(self):
        return 0

    def getTailor(self):
        return 0

    def getGivesQuests(self):
        return self.givesQuests

    def avatarEnter(self):
        pass

    def isBusy(self):
        return self.busy > 0

    def getNpcId(self):
        return self.npcId

    def freeAvatar(self, avId):
        self.sendUpdateToAvatarId(avId, 'freeAvatar', [])

    def setPositionIndex(self, posIndex):
        self.posIndex = posIndex

    def getPositionIndex(self):
        return self.posIndex