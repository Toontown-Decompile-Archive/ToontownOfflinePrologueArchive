# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.parties.DistributedPartyAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from PartyGlobals import *
import PartyUtils, time
from toontown.parties.DistributedPartyJukeboxActivityAI import DistributedPartyJukeboxActivityAI
from toontown.parties.DistributedPartyDanceActivityAI import DistributedPartyDanceActivityAI
from toontown.parties.DistributedPartyJukebox40ActivityAI import DistributedPartyJukebox40ActivityAI
from toontown.parties.DistributedPartyDance20ActivityAI import DistributedPartyDance20ActivityAI
from toontown.parties.DistributedPartyCogActivityAI import DistributedPartyCogActivityAI
from toontown.parties.DistributedPartyTrampolineActivityAI import DistributedPartyTrampolineActivityAI
from toontown.parties.DistributedPartyVictoryTrampolineActivityAI import DistributedPartyVictoryTrampolineActivityAI
from toontown.parties.DistributedPartyCatchActivityAI import DistributedPartyCatchActivityAI
from toontown.parties.DistributedPartyTugOfWarActivityAI import DistributedPartyTugOfWarActivityAI
from toontown.parties.DistributedPartyCannonActivityAI import DistributedPartyCannonActivityAI
from toontown.parties.DistributedPartyCannonAI import DistributedPartyCannonAI
from toontown.parties.DistributedPartyFireworksActivityAI import DistributedPartyFireworksActivityAI

class DistributedPartyAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPartyAI')

    def __init__(self, air, hostId, zoneId, info):
        DistributedObjectAI.__init__(self, air)
        self.hostId = hostId
        self.zoneId = zoneId
        self.info = info
        PARTY_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
        self.startedAt = time.strftime(PARTY_TIME_FORMAT)
        self.partyState = 0
        self.avIdsAtParty = []
        for activity in self.info['activities']:
            if activity[0] == ActivityIds.PartyClock:
                self.partyClockInfo = (
                 activity[1], activity[2], activity[3])

        self.hostName = ''
        host = self.air.doId2do.get(self.hostId, None)
        if host:
            self.hostName = host.getName()
        self.activities = []
        self.cannonActivity = None
        return

    def generate(self):
        DistributedObjectAI.generate(self)
        actId2Class = {ActivityIds.PartyJukebox: DistributedPartyJukeboxActivityAI, 
           ActivityIds.PartyTrampoline: DistributedPartyTrampolineActivityAI, 
           ActivityIds.PartyVictoryTrampoline: DistributedPartyVictoryTrampolineActivityAI, 
           ActivityIds.PartyCatch: DistributedPartyCatchActivityAI, 
           ActivityIds.PartyDance: DistributedPartyDanceActivityAI, 
           ActivityIds.PartyTugOfWar: DistributedPartyTugOfWarActivityAI, 
           ActivityIds.PartyFireworks: DistributedPartyFireworksActivityAI, 
           ActivityIds.PartyJukebox40: DistributedPartyJukebox40ActivityAI, 
           ActivityIds.PartyDance20: DistributedPartyDance20ActivityAI, 
           ActivityIds.PartyCog: DistributedPartyCogActivityAI}
        for activity in self.info['activities']:
            actId = activity[0]
            if actId in actId2Class:
                act = actId2Class[actId](self.air, self.doId, activity)
                act.generateWithRequired(self.zoneId)
                self.activities.append(act)
            elif actId == ActivityIds.PartyCannon:
                if not self.cannonActivity:
                    self.cannonActivity = DistributedPartyCannonActivityAI(self.air, self.doId, activity)
                    self.cannonActivity.generateWithRequired(self.zoneId)
                act = DistributedPartyCannonAI(self.air)
                act.setActivityDoId(self.cannonActivity.doId)
                x, y, h = activity[1:]
                x = PartyUtils.convertDistanceFromPartyGrid(x, 0)
                y = PartyUtils.convertDistanceFromPartyGrid(y, 1)
                h *= PartyGridHeadingConverter
                act.setPosHpr(x, y, 0, h, 0, 0)
                act.generateWithRequired(self.zoneId)
                self.activities.append(act)

    def delete(self):
        for act in self.activities:
            act.requestDelete()

        if self.cannonActivity:
            self.cannonActivity.requestDelete()
        DistributedObjectAI.delete(self)

    def getPartyClockInfo(self):
        return self.partyClockInfo

    def getInviteeIds(self):
        return self.info.get('inviteeIds', [])

    def getPartyState(self):
        return self.partyState

    def b_setPartyState(self, partyState):
        self.partyState = partyState
        self.sendUpdate('setPartyState', [partyState])

    def _formatParty(self, partyDict, status=PartyStatus.Started):
        start = partyDict['start']
        end = partyDict['end']
        return [partyDict['partyId'],
         partyDict['hostId'],
         start.year,
         start.month,
         start.day,
         start.hour,
         start.minute,
         end.year,
         end.month,
         end.day,
         end.hour,
         end.minute,
         partyDict['isPrivate'],
         partyDict['inviteTheme'],
         partyDict['activities'],
         partyDict['decorations'],
         status]

    def getPartyInfoTuple(self):
        return self._formatParty(self.info)

    def getAvIdsAtParty(self):
        return self.avIdsAtParty

    def getPartyStartedTime(self):
        return self.startedAt

    def getHostName(self):
        return self.hostName

    def enteredParty(self):
        avId = self.air.getAvatarIdFromSender()
        if avId not in self.avIdsAtParty:
            self.air.globalPartyMgr.d_toonJoinedParty(self.info.get('partyId', 0), avId)
            self.avIdsAtParty.append(avId)

    def _removeAvatar(self, avId):
        if avId in self.avIdsAtParty:
            self.notify.info('Removing av from party...')
            self.air.globalPartyMgr.d_toonLeftParty(self.info.get('partyId', 0), avId)
            self.avIdsAtParty.remove(avId)