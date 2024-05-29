# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.safezone.DistributedPartyGateAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.parties import PartyGlobals

class DistributedPartyGateAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPartyGateAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.area = None
        return

    def setArea(self, area):
        self.area = area

    def getArea(self):
        return self.area

    def getPartyList(self, avId):
        partyManager = simbase.air.partyManager
        self.sendUpdateToAvatarId(avId, 'listAllPublicParties', [partyManager.getPublicParties()])

    def partyChoiceRequest(self, avId, shardId, zoneId):
        party = None
        pid = 0
        for partyId in self.air.partyManager.pubPartyInfo:
            p = self.air.partyManager.pubPartyInfo[partyId]
            if p.get('shardId', 0) == shardId and p.get('zoneId', 0) == zoneId:
                party = p
                pid = partyId
                break

        if not party:
            self.sendUpdateToAvatarId(self.air.getAvatarIdFromSender(), 'partyRequestDenied', [PartyGlobals.PartyGateDenialReasons.Unavailable])
            return
        else:
            self.air.globalPartyMgr.d_requestPartySlot(pid, self.air.getAvatarIdFromSender(), self.doId)
            return