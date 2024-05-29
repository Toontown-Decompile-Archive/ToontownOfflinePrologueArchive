# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.parties.GlobalPartyManagerAI
# Compiled at: 2014-04-30 09:53:54
from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI
from direct.distributed.PyDatagram import *
from direct.directnotify.DirectNotifyGlobal import directNotify

class GlobalPartyManagerAI(DistributedObjectGlobalAI):
    notify = directNotify.newCategory('GlobalPartyManagerAI')

    def announceGenerate(self):
        DistributedObjectGlobalAI.announceGenerate(self)
        self.sendUpdate('partyManagerAIHello', [simbase.air.partyManager.doId])

    def sendAddParty(self, avId, partyId, start, end, isPrivate, inviteTheme, activities, decorations, inviteeIds):
        self.sendUpdate('addParty', [avId, partyId, start, end, isPrivate, inviteTheme, activities, decorations, 
         inviteeIds])

    def queryPartyForHost(self, hostId):
        self.sendUpdate('queryParty', [hostId])

    def d_partyStarted(self, partyId, shardId, zoneId, hostName):
        self.sendUpdate('partyHasStarted', [partyId, shardId, zoneId, hostName])

    def partyStarted(self, partyId, shardId, zoneId, hostName):
        pass

    def d_partyDone(self, partyId):
        self.sendUpdate('partyDone', [partyId])

    def partyDone(self, partyId):
        pass

    def d_toonJoinedParty(self, partyId, avId):
        self.sendUpdate('toonJoinedParty', [partyId, avId])

    def toonJoinedParty(self, partyId, avId):
        pass

    def d_toonLeftParty(self, partyId, avId):
        self.sendUpdate('toonLeftParty', [partyId, avId])

    def toonLeftParty(self, partyId, avId):
        pass

    def d_requestPartySlot(self, partyId, avId, gateId):
        self.sendUpdate('requestPartySlot', [partyId, avId, gateId])

    def requestPartySlot(self, partyId, avId, gateId):
        pass

    def d_allocIds(self, numIds):
        self.sendUpdate('allocIds', [numIds])

    def allocIds(self, numIds):
        pass