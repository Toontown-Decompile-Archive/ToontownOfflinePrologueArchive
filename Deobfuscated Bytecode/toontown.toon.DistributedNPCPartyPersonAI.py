# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.toon.DistributedNPCPartyPersonAI
# Compiled at: 2014-04-30 09:53:54
from DistributedNPCToonBaseAI import DistributedNPCToonBaseAI
from toontown.toonbase import TTLocalizer
from direct.task import Task
from toontown.toonbase import ToontownGlobals
from toontown.toon import NPCToons
from direct.distributed import ClockDelta
from toontown.parties import PartyGlobals

class DistributedNPCPartyPersonAI(DistributedNPCToonBaseAI):

    def __init__(self, air, npcId):
        DistributedNPCToonBaseAI.__init__(self, air, npcId)
        self.givesQuests = 0
        self.busy = 0

    def delete(self):
        taskMgr.remove(self.uniqueName('clearMovie'))
        self.ignoreAll()
        DistributedNPCToonBaseAI.delete(self)

    def avatarEnter(self):
        avId = self.air.getAvatarIdFromSender()
        if not self.air.doId2do.has_key(avId):
            self.notify.warning('Avatar: %s not found' % avId)
            return
        else:
            if self.isBusy():
                self.freeAvatar(avId)
                return
            av = self.air.doId2do[avId]
            self.busy = avId
            self.acceptOnce(self.air.getAvatarExitEvent(avId), self.__handleUnexpectedExit, extraArgs=[avId])
            parties = av.hostedParties
            if not self.air.partyManager.canBuyParties():
                flag = NPCToons.PARTY_MOVIE_COMINGSOON
                self.d_setMovie(avId, flag)
                self.sendClearMovie(None)
            elif av.getTotalMoney() < PartyGlobals.MinimumPartyCost:
                flag = NPCToons.PARTY_MOVIE_MINCOST
                self.d_setMovie(avId, flag)
                self.sendClearMovie(None)
            elif av.canPlanParty():
                flag = NPCToons.PARTY_MOVIE_START
                self.d_setMovie(avId, flag)
                taskMgr.doMethodLater(30.0, self.sendTimeoutMovie, self.uniqueName('clearMovie'))
            else:
                flag = NPCToons.PARTY_MOVIE_ALREADYHOSTING
                self.d_setMovie(avId, flag)
                self.sendClearMovie(None)
            DistributedNPCToonBaseAI.avatarEnter(self)
            return

    def rejectAvatar(self, avId):
        self.notify.warning('rejectAvatar: should not be called by a party person!')

    def d_setMovie(self, avId, flag, extraArgs=[]):
        self.sendUpdate('setMovie', [flag,
         self.npcId,
         avId,
         extraArgs,
         ClockDelta.globalClockDelta.getRealNetworkTime()])

    def sendTimeoutMovie(self, task):
        self.d_setMovie(self.busy, NPCToons.PARTY_MOVIE_TIMEOUT)
        self.sendClearMovie(None)
        return Task.done

    def sendClearMovie(self, task):
        self.ignore(self.air.getAvatarExitEvent(self.busy))
        taskMgr.remove(self.uniqueName('clearMovie'))
        self.busy = 0
        self.d_setMovie(0, NPCToons.PARTY_MOVIE_CLEAR)
        return Task.done

    def answer(self, wantsToPlan):
        avId = self.air.getAvatarIdFromSender()
        if self.busy != avId:
            self.air.writeServerEvent('suspicious', avId=avId, issue='DistributedNPCPartyPersonAI.answer busy with %s' % self.busy)
            self.notify.warning('somebody called setMovieDone that I was not busy with! avId: %s' % avId)
            return
        else:
            if wantsToPlan:
                av = simbase.air.doId2do.get(avId)
                if av:
                    if av.getGameAccess() != ToontownGlobals.AccessFull:
                        self.air.writeServerEvent('suspicious', avId=avId, issue='DistributedNPCPartyPersonAI.free player tried to host party.')
                        flag = NPCToons.PARTY_MOVIE_ONLYPAID
                        self.d_setMovie(avId, flag)
                    else:
                        zoneId = self.air.allocateZone(owner=self)
                        hoodId = ToontownGlobals.PartyHood
                        self.d_setMovie(avId, NPCToons.PARTY_MOVIE_COMPLETE, [hoodId, zoneId])
            else:
                av = simbase.air.doId2do.get(avId)
                if av:
                    self.d_setMovie(avId, NPCToons.PARTY_MOVIE_MAYBENEXTTIME)
            self.sendClearMovie(None)
            return

    def __handleUnexpectedExit(self, avId):
        self.notify.warning('avatar:' + str(avId) + ' has exited unexpectedly')
        self.notify.warning('not busy with avId: %s, busy: %s ' % (avId, self.busy))
        taskMgr.remove(self.uniqueName('clearMovie'))
        self.sendClearMovie(None)
        return