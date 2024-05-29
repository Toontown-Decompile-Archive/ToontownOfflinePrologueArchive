# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.toon.DistributedNPCFreeGagsAI
# Compiled at: 2014-04-30 09:53:54
from direct.task.Task import Task
from pandac.PandaModules import *
from DistributedNPCToonBaseAI import *
from toontown.quest import Quests
from random import randrange

class DistributedNPCFreeGagsAI(DistributedNPCToonBaseAI):

    def __init__(self, air, npcId, questCallback=None, hq=0):
        DistributedNPCToonBaseAI.__init__(self, air, npcId, questCallback)
        self.air = air

    def avatarEnter(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        self.notify.debug('avatar enter ' + str(avId))
        av.inventory.NPCMaxOutInv(targetTrack=-1, maxLevelIndex=6)
        av.b_setInventory(av.inventory.makeNetString())
        self.sendUpdate('gaveGags', [self.npcId, avId, randrange(4)])