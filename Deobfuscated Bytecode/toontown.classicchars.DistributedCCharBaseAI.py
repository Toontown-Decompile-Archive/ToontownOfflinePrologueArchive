# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.classicchars.DistributedCCharBaseAI
# Compiled at: 2014-04-30 09:53:54
from otp.ai.AIBaseGlobal import *
from direct.distributed.ClockDelta import *
from otp.avatar import DistributedAvatarAI
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals

class DistributedCCharBaseAI(DistributedAvatarAI.DistributedAvatarAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCCharBaseAI')

    def __init__(self, air, name):
        DistributedAvatarAI.DistributedAvatarAI.__init__(self, air)
        self.setName(name)
        self.exitOff()
        self.transitionToCostume = 0
        self.diffPath = None
        return

    def delete(self):
        self.ignoreAll()
        DistributedAvatarAI.DistributedAvatarAI.delete(self)

    def exitOff(self):
        self.__initAttentionSpan()
        self.__clearNearbyAvatars()

    def avatarEnter(self):
        avId = self.air.getAvatarIdFromSender()
        self.notify.debug('adding avatar ' + str(avId) + ' to the nearby avatar list')
        if avId not in self.nearbyAvatars:
            self.nearbyAvatars.append(avId)
        else:
            self.air.writeServerEvent('suspicious', avId, 'CCharBase.avatarEnter')
            self.notify.warning('Avatar %s already in nearby avatars!' % avId)
        self.nearbyAvatarInfoDict[avId] = {}
        self.nearbyAvatarInfoDict[avId]['enterTime'] = globalClock.getRealTime()
        self.nearbyAvatarInfoDict[avId]['lastChatTime'] = 0
        self.sortNearbyAvatars()
        self.__interestingAvatarEventOccured()
        avExitEvent = self.air.getAvatarExitEvent(avId)
        self.acceptOnce(avExitEvent, self.__handleExitedAvatar, [
         avId])
        self.avatarEnterNextState()

    def avatarExit(self):
        avId = self.air.getAvatarIdFromSender()
        self.__doAvatarExit(avId)

    def _DistributedCCharBaseAI__doAvatarExit(self, avId):
        avId = self.air.getAvatarIdFromSender()
        self.notify.debug('removing avatar ' + str(avId) + ' from the nearby avatar list')
        if avId not in self.nearbyAvatars:
            self.notify.debug('avatar ' + str(avId) + ' not in the nearby avatar list')
        else:
            avExitEvent = self.air.getAvatarExitEvent(avId)
            self.ignore(avExitEvent)
            del self.nearbyAvatarInfoDict[avId]
            self.nearbyAvatars.remove(avId)
            self.avatarExitNextState()

    def avatarEnterNextState():
        pass

    def avatarExitNextState():
        pass

    def _DistributedCCharBaseAI__clearNearbyAvatars(self):
        self.nearbyAvatars = []
        self.nearbyAvatarInfoDict = {}

    def sortNearbyAvatars(self):

        def nAv_compare(a, b, nAvIDict=self.nearbyAvatarInfoDict):
            tsA = nAvIDict[a]['enterTime']
            tsB = nAvIDict[b]['enterTime']
            if tsA == tsB:
                return 0
            else:
                if tsA < tsB:
                    return -1
                return 1

        self.nearbyAvatars.sort(nAv_compare)

    def getNearbyAvatars(self):
        return self.nearbyAvatars

    def _DistributedCCharBaseAI__avatarSpoke(self, avId):
        now = globalClock.getRealTime()
        if self.nearbyAvatarInfoDict.has_key(avId):
            self.nearbyAvatarInfoDict[avId]['lastChatTime'] = now
            self.__interestingAvatarEventOccured()

    def _DistributedCCharBaseAI__initAttentionSpan(self):
        self.__avatarTimeoutBase = 0

    def _DistributedCCharBaseAI__interestingAvatarEventOccured(self, t=None):
        if t == None:
            t = globalClock.getRealTime()
        self.__avatarTimeoutBase = t
        return

    def lostInterest(self):
        now = globalClock.getRealTime()
        if now > self.__avatarTimeoutBase + 50.0:
            return 1
        return 0

    def _DistributedCCharBaseAI__handleExitedAvatar(self, avId):
        self.__doAvatarExit(avId)

    def setNearbyAvatarChat(self, msg):
        avId = self.air.getAvatarIdFromSender()
        self.notify.debug('setNearbyAvatarChat: avatar ' + str(avId) + ' said ' + str(msg))
        self.__avatarSpoke(avId)

    def setNearbyAvatarSC(self, msgIndex):
        avId = self.air.getAvatarIdFromSender()
        self.notify.debug('setNearbyAvatarSC: avatar %s said SpeedChat phrase %s' % (avId, msgIndex))
        self.__avatarSpoke(avId)

    def setNearbyAvatarSCCustom(self, msgIndex):
        avId = self.air.getAvatarIdFromSender()
        self.notify.debug('setNearbyAvatarSCCustom: avatar %s said custom SpeedChat phrase %s' % (avId, msgIndex))
        self.__avatarSpoke(avId)

    def setNearbyAvatarSCToontask(self, taskId, toNpcId, toonProgress, msgIndex):
        avId = self.air.getAvatarIdFromSender()
        self.notify.debug('setNearbyAvatarSCToontask: avatar %s said %s' % (avId, (taskId, toNpcId, toonProgress, msgIndex)))
        self.__avatarSpoke(avId)

    def getWalk(self):
        return ('', '', 0)

    def walkSpeed(self):
        return 0.1

    def handleHolidays(self):
        self.CCChatter = 0
        if hasattr(simbase.air, 'holidayManager'):
            if ToontownGlobals.CRASHED_LEADERBOARD in simbase.air.holidayManager.currentHolidays:
                self.CCChatter = ToontownGlobals.CRASHED_LEADERBOARD
            else:
                if ToontownGlobals.CIRCUIT_RACING_EVENT in simbase.air.holidayManager.currentHolidays:
                    self.CCChatter = ToontownGlobals.CIRCUIT_RACING_EVENT
                else:
                    if ToontownGlobals.WINTER_CAROLING in simbase.air.holidayManager.currentHolidays:
                        self.CCChatter = ToontownGlobals.WINTER_CAROLING
                    else:
                        if ToontownGlobals.WINTER_DECORATIONS in simbase.air.holidayManager.currentHolidays:
                            self.CCChatter = ToontownGlobals.WINTER_DECORATIONS
                        else:
                            if ToontownGlobals.VALENTINES_DAY in simbase.air.holidayManager.currentHolidays:
                                self.CCChatter = ToontownGlobals.VALENTINES_DAY
                            else:
                                if ToontownGlobals.APRIL_FOOLS_COSTUMES in simbase.air.holidayManager.currentHolidays:
                                    self.CCChatter = ToontownGlobals.APRIL_FOOLS_COSTUMES
                                else:
                                    if ToontownGlobals.SILLY_CHATTER_ONE in simbase.air.holidayManager.currentHolidays:
                                        self.CCChatter = ToontownGlobals.SILLY_CHATTER_ONE
                                    else:
                                        if ToontownGlobals.SILLY_CHATTER_TWO in simbase.air.holidayManager.currentHolidays:
                                            self.CCChatter = ToontownGlobals.SILLY_CHATTER_TWO
                                        else:
                                            if ToontownGlobals.SILLY_CHATTER_THREE in simbase.air.holidayManager.currentHolidays:
                                                self.CCChatter = ToontownGlobals.SILLY_CHATTER_THREE
                                            else:
                                                if ToontownGlobals.SILLY_CHATTER_FOUR in simbase.air.holidayManager.currentHolidays:
                                                    self.CCChatter = ToontownGlobals.SILLY_CHATTER_FOUR
                                                elif ToontownGlobals.SILLY_CHATTER_FIVE in simbase.air.holidayManager.currentHolidays:
                                                    self.CCChatter = ToontownGlobals.SILLY_CHATTER_FOUR

    def getCCLocation(self):
        return 0

    def getCCChatter(self):
        self.handleHolidays()
        return self.CCChatter

    def fadeAway(self):
        self.sendUpdate('fadeAway', [])

    def transitionCostume(self):
        self.transitionToCostume = 1