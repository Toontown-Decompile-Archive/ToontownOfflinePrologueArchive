# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.parties.DistributedPartyDanceActivityBaseAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from toontown.parties.DistributedPartyActivityAI import DistributedPartyActivityAI
from direct.distributed.ClockDelta import *
import PartyGlobals

class DistributedPartyDanceActivityBaseAI(DistributedPartyActivityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPartyDanceActivityBaseAI')

    def __init__(self, air, parent, activityTuple):
        DistributedPartyActivityAI.__init__(self, air, parent, activityTuple)
        self.toons = []
        self.headings = []

    def generate(self):
        DistributedPartyActivityAI.generate(self)
        self.sendUpdate('setState', ['Active', globalClockDelta.getRealNetworkTime()])

    def updateDancingToon(self, state, anim):
        avId = self.air.getAvatarIdFromSender()
        if avId not in self.toons:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Toon tried to update their state while not dancing!')
            return
        self.sendUpdate('setDancingToonState', [avId, state, anim])

    def toonJoinRequest(self):
        avId = self.air.getAvatarIdFromSender()
        if avId in self.toons:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Toon tried to enter dance activity twice!')
            return
        av = self.air.doId2do.get(avId)
        if not av:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Toon tried to interact with a party activity from a different district!')
            return
        self.toons.append(avId)
        self.headings.append(av.getH())
        self.sendUpdate('setToonsPlaying', [self.toons, self.headings])

    def toonExitRequest(self):
        avId = self.air.getAvatarIdFromSender()
        if avId not in self.toons:
            self.air.writeServerEvent('suspicious', avId=avId, issue="Toon tried to exit a dance floor they're not on!")
            return
        index = self.toons.index(avId)
        self.toons.remove(avId)
        self.headings.pop(index)
        self.sendUpdate('setToonsPlaying', [self.toons, self.headings])