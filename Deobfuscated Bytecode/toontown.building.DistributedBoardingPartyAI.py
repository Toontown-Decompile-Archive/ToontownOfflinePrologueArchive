# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.building.DistributedBoardingPartyAI
# Compiled at: 2014-04-30 09:53:54
from otp.otpbase import OTPGlobals
from otp.ai.AIBase import *
from toontown.toonbase import ToontownGlobals
from direct.distributed.ClockDelta import *
from ElevatorConstants import *
from direct.distributed import DistributedObjectAI
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from direct.task import Task
from direct.directnotify import DirectNotifyGlobal
from toontown.building import BoardingPartyBase
GROUPMEMBER = 0
GROUPINVITE = 1

class DistributedBoardingPartyAI(DistributedObjectAI.DistributedObjectAI, BoardingPartyBase.BoardingPartyBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBoardingPartyAI')

    def __init__(self, air, elevatorList, maxSize=4):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        BoardingPartyBase.BoardingPartyBase.__init__(self)
        self.setGroupSize(maxSize)
        self.elevatorIdList = elevatorList
        self.visibleZones = []

    def delete(self):
        self.cleanup()
        DistributedObjectAI.DistributedObjectAI.delete(self)

    def generate(self):
        DistributedObjectAI.DistributedObjectAI.generate(self)
        for elevatorId in self.elevatorIdList:
            elevator = simbase.air.doId2do.get(elevatorId)
            elevator.setBoardingParty(self)

    def cleanup(self):
        BoardingPartyBase.BoardingPartyBase.cleanup(self)
        del self.elevatorIdList
        del self.visibleZones

    def getElevatorIdList(self):
        return self.elevatorIdList

    def setElevatorIdList(self, elevatorIdList):
        self.elevatorIdList = elevatorIdList

    def addWacthAvStatus(self, avId):
        self.acceptOnce(self.air.getAvatarExitEvent(avId), self.handleAvatarDisco, extraArgs=[avId])
        self.accept(self.staticGetLogicalZoneChangeEvent(avId), self.handleAvatarZoneChange, extraArgs=[avId])
        messageToonAdded = 'Battle adding toon %s' % avId
        self.accept(messageToonAdded, self.handleToonJoinedBattle)
        messageToonReleased = 'Battle releasing toon %s' % avId
        self.accept(messageToonReleased, self.handleToonLeftBattle)

    def handleToonJoinedBattle(self, avId):
        self.notify.debug('handleToonJoinedBattle %s' % avId)

    def handleToonLeftBattle(self, avId):
        self.notify.debug('handleToonLeftBattle %s' % avId)

    def removeWacthAvStatus(self, avId):
        self.ignore(self.air.getAvatarExitEvent(avId))
        self.ignore(self.staticGetLogicalZoneChangeEvent(avId))

    def requestInvite(self, inviteeId):
        self.notify.debug('requestInvite %s' % inviteeId)
        inviterId = self.air.getAvatarIdFromSender()
        invitee = simbase.air.doId2do.get(inviteeId)
        if invitee and invitee.battleId != 0:
            reason = BoardingPartyBase.BOARDCODE_BATTLE
            self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviteeId, reason, 0])
            self.sendUpdateToAvatarId(inviteeId, 'postMessageInvitationFailed', [inviterId])
            return
        if self.hasActiveGroup(inviteeId):
            reason = BoardingPartyBase.BOARDCODE_DIFF_GROUP
            self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviteeId, reason, 0])
            self.sendUpdateToAvatarId(inviteeId, 'postMessageInvitationFailed', [inviterId])
            return
        if self.hasPendingInvite(inviteeId):
            reason = BoardingPartyBase.BOARDCODE_PENDING_INVITE
            self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviteeId, reason, 0])
            self.sendUpdateToAvatarId(inviteeId, 'postMessageInvitationFailed', [inviterId])
            return
        if self.__isInElevator(inviteeId):
            reason = BoardingPartyBase.BOARDCODE_IN_ELEVATOR
            self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviteeId, reason, 0])
            self.sendUpdateToAvatarId(inviteeId, 'postMessageInvitationFailed', [inviterId])
            return
        inviteeOkay = self.checkBoard(inviteeId, self.elevatorIdList[0])
        reason = 0
        if inviteeOkay == REJECT_NOTPAID:
            reason = BoardingPartyBase.BOARDCODE_NOT_PAID
            self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviteeId, reason, 0])
            return
        if len(self.elevatorIdList) == 1:
            if inviteeOkay:
                if inviteeOkay == REJECT_MINLAFF:
                    reason = BoardingPartyBase.BOARDCODE_MINLAFF
                elif inviteeOkay == REJECT_PROMOTION:
                    reason = BoardingPartyBase.BOARDCODE_PROMOTION
                self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviteeId, reason, self.elevatorIdList[0]])
                return
            inviterOkay = self.checkBoard(inviterId, self.elevatorIdList[0])
            if inviterOkay:
                if inviterOkay == REJECT_MINLAFF:
                    reason = BoardingPartyBase.BOARDCODE_MINLAFF
                elif inviterOkay == REJECT_PROMOTION:
                    reason = BoardingPartyBase.BOARDCODE_PROMOTION
                self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviterId, reason, self.elevatorIdList[0]])
                return
        if self.avIdDict.has_key(inviterId):
            self.notify.debug('old group')
            leaderId = self.avIdDict[inviterId]
            groupList = self.groupListDict.get(leaderId)
            if groupList:
                self.notify.debug('got group list')
                if inviterId == leaderId:
                    if inviteeId in groupList[2]:
                        groupList[2].remove(inviteeId)
                if len(self.getGroupMemberList(leaderId)) >= self.maxSize:
                    self.sendUpdate('postSizeReject', [leaderId, inviterId, inviteeId])
                else:
                    if inviterId not in groupList[1] and inviterId not in groupList[2]:
                        if inviteeId not in groupList[1]:
                            groupList[1].append(inviteeId)
                        self.groupListDict[leaderId] = groupList
                        if self.avIdDict.has_key(inviteeId):
                            self.notify.warning('inviter %s tried to invite %s who already exists in the avIdDict.' % (inviterId, inviteeId))
                            self.air.writeServerEvent('suspicious', avId=inviterId, issue='tried to invite %s who already exists in the avIdDict.' % inviteeId)
                        self.avIdDict[inviteeId] = leaderId
                        self.sendUpdateToAvatarId(inviteeId, 'postInvite', [leaderId, inviterId])
                        for memberId in groupList[0]:
                            if not memberId == inviterId:
                                self.sendUpdateToAvatarId(memberId, 'postMessageInvited', [inviteeId, inviterId])

                    elif inviterId in groupList[2]:
                        self.sendUpdate('postKickReject', [leaderId, inviterId, inviteeId])
        else:
            if self.avIdDict.has_key(inviteeId):
                self.notify.warning('inviter %s tried to invite %s who already exists in avIdDict.' % (inviterId, inviteeId))
                self.air.writeServerEvent('suspicious', avId=inviterId, issue='tried to invite %s who already exists in the avIdDict.' % inviteeId)
            self.notify.debug('new group')
            leaderId = inviterId
            self.avIdDict[inviterId] = inviterId
            self.avIdDict[inviteeId] = inviterId
            self.groupListDict[leaderId] = [[leaderId], [inviteeId], []]
            self.addWacthAvStatus(leaderId)
            self.sendUpdateToAvatarId(inviteeId, 'postInvite', [leaderId, inviterId])

    def requestCancelInvite(self, inviteeId):
        inviterId = self.air.getAvatarIdFromSender()
        if self.avIdDict.has_key(inviterId):
            leaderId = self.avIdDict[inviterId]
            groupList = self.groupListDict.get(leaderId)
            if groupList:
                self.removeFromGroup(leaderId, inviteeId)
                self.sendUpdateToAvatarId(inviteeId, 'postInviteCanceled', [])

    def requestAcceptInvite(self, leaderId, inviterId):
        inviteeId = self.air.getAvatarIdFromSender()
        self.notify.debug('requestAcceptInvite leader%s inviter%s invitee%s' % (leaderId, inviterId, inviteeId))
        if self.avIdDict.has_key(inviteeId):
            if self.hasActiveGroup(inviteeId):
                self.sendUpdateToAvatarId(inviteeId, 'postAlreadyInGroup', [])
                return
            if not self.avIdDict.has_key(leaderId) or not self.isInGroup(inviteeId, leaderId):
                self.sendUpdateToAvatarId(inviteeId, 'postSomethingMissing', [])
                return
            memberList = self.getGroupMemberList(leaderId)
            if self.avIdDict[inviteeId]:
                if self.avIdDict[inviteeId] == leaderId:
                    if inviteeId in memberList:
                        self.notify.debug('invitee already in group, aborting requestAcceptInvite')
                        return
                else:
                    self.air.writeServerEvent('suspicious', avId=inviteeId, issue="accepted a second invite from %s, in %s's group, while he was in alredy in %s's group." % (inviterId, leaderId, self.avIdDict[inviteeId]))
                    self.removeFromGroup(self.avIdDict[inviteeId], inviteeId, post=0)
            if len(memberList) >= self.maxSize:
                self.removeFromGroup(leaderId, inviteeId)
                self.sendUpdateToAvatarId(inviterId, 'postMessageAcceptanceFailed', [inviteeId, BoardingPartyBase.INVITE_ACCEPT_FAIL_GROUP_FULL])
                self.sendUpdateToAvatarId(inviteeId, 'postGroupAlreadyFull', [])
                return
            self.sendUpdateToAvatarId(inviterId, 'postInviteAccepted', [inviteeId])
            self.addToGroup(leaderId, inviteeId)
        else:
            self.air.writeServerEvent('suspicious', avId=inviteeId, issue="was invited to %s's group by %s, but the invitee didn't have an entry in the avIdDict." % (leaderId, inviterId))

    def requestRejectInvite(self, leaderId, inviterId):
        inviteeId = self.air.getAvatarIdFromSender()
        self.removeFromGroup(leaderId, inviteeId)
        self.sendUpdateToAvatarId(inviterId, 'postInviteDelcined', [inviteeId])

    def requestKick(self, kickId):
        leaderId = self.air.getAvatarIdFromSender()
        if self.avIdDict.has_key(kickId):
            if self.avIdDict[kickId] == leaderId:
                self.removeFromGroup(leaderId, kickId, kick=1)
                self.sendUpdateToAvatarId(kickId, 'postKick', [leaderId])

    def requestLeave(self, leaderId):
        memberId = self.air.getAvatarIdFromSender()
        if self.avIdDict.has_key(memberId):
            if leaderId == self.avIdDict[memberId]:
                self.removeFromGroup(leaderId, memberId)

    def checkBoard(self, avId, elevatorId):
        elevator = simbase.air.doId2do.get(elevatorId)
        avatar = simbase.air.doId2do.get(avId)
        if avatar:
            if not avatar.getGameAccess() == OTPGlobals.AccessFull:
                return REJECT_NOTPAID
            if elevator:
                return elevator.checkBoard(avatar)
        return REJECT_BOARDINGPARTY

    def testBoard(self, leaderId, elevatorId, needSpace=0):
        elevator = None
        boardOkay = BoardingPartyBase.BOARDCODE_MISSING
        avatarsFailingRequirements = []
        avatarsInBattle = []
        if elevatorId in self.elevatorIdList:
            elevator = simbase.air.doId2do.get(elevatorId)
        if elevator:
            if self.avIdDict.has_key(leaderId):
                if leaderId == self.avIdDict[leaderId]:
                    boardOkay = BoardingPartyBase.BOARDCODE_OKAY
                    for avId in self.getGroupMemberList(leaderId):
                        avatar = simbase.air.doId2do.get(avId)
                        if avatar:
                            if elevator.checkBoard(avatar) != 0:
                                if elevator.checkBoard(avatar) == REJECT_MINLAFF:
                                    boardOkay = BoardingPartyBase.BOARDCODE_MINLAFF
                                elif elevator.checkBoard(avatar) == REJECT_PROMOTION:
                                    boardOkay = BoardingPartyBase.BOARDCODE_PROMOTION
                                avatarsFailingRequirements.append(avId)
                            elif avatar.battleId != 0:
                                boardOkay = BoardingPartyBase.BOARDCODE_BATTLE
                                avatarsInBattle.append(avId)

                    groupSize = len(self.getGroupMemberList(leaderId))
                    if groupSize > self.maxSize:
                        boardOkay = BoardingPartyBase.BOARDCODE_SPACE
                    if needSpace:
                        if groupSize > elevator.countOpenSeats():
                            boardOkay = BoardingPartyBase.BOARDCODE_SPACE
        if boardOkay != BoardingPartyBase.BOARDCODE_OKAY:
            self.notify.debug('Something is wrong with the group board request')
            if boardOkay == BoardingPartyBase.BOARDCODE_MINLAFF:
                self.notify.debug('An avatar did not meet the elevator laff requirements')
            if boardOkay == BoardingPartyBase.BOARDCODE_PROMOTION:
                self.notify.debug('An avatar did not meet the elevator promotion requirements')
            elif boardOkay == BoardingPartyBase.BOARDCODE_BATTLE:
                self.notify.debug('An avatar is in battle')
        return (
         boardOkay, avatarsFailingRequirements, avatarsInBattle)

    def requestBoard(self, elevatorId):
        wantDisableGoButton = False
        leaderId = self.air.getAvatarIdFromSender()
        elevator = None
        if elevatorId in self.elevatorIdList:
            elevator = simbase.air.doId2do.get(elevatorId)
        if elevator:
            if self.avIdDict.has_key(leaderId):
                if leaderId == self.avIdDict[leaderId]:
                    group = self.groupListDict.get(leaderId)
                    if group:
                        boardOkay, avatarsFailingRequirements, avatarsInBattle = self.testBoard(leaderId, elevatorId, needSpace=1)
                        if boardOkay == BoardingPartyBase.BOARDCODE_OKAY:
                            leader = simbase.air.doId2do.get(leaderId)
                            if leader:
                                elevator.partyAvatarBoard(leader)
                                wantDisableGoButton = True
                            for avId in group[0]:
                                if not avId == leaderId:
                                    avatar = simbase.air.doId2do.get(avId)
                                    if avatar:
                                        elevator.partyAvatarBoard(avatar, wantBoardingShow=1)

                            self.air.writeServerEvent('boarding_elevator', zoneId=self.zoneId, elevatorId=elevatorId, group=group[0])
                        else:
                            self.sendUpdateToAvatarId(leaderId, 'postRejectBoard', [elevatorId, boardOkay, avatarsFailingRequirements, avatarsInBattle])
                            return
        if not wantDisableGoButton:
            self.sendUpdateToAvatarId(leaderId, 'postRejectBoard', [elevatorId, BoardingPartyBase.BOARDCODE_MISSING, [], []])
        return

    def testGoButtonRequirements(self, leaderId, elevatorId):
        if self.avIdDict.has_key(leaderId):
            if leaderId == self.avIdDict[leaderId]:
                if elevatorId in self.elevatorIdList:
                    elevator = simbase.air.doId2do.get(elevatorId)
                    if elevator:
                        boardOkay, avatarsFailingRequirements, avatarsInBattle = self.testBoard(leaderId, elevatorId, needSpace=0)
                        if boardOkay == BoardingPartyBase.BOARDCODE_OKAY:
                            avList = self.getGroupMemberList(leaderId)
                            if 0 in avList:
                                avList.remove(0)
                            if leaderId not in elevator.seats:
                                return True
                            self.notify.warning('avId: %s has hacked his/her client.' % leaderId)
                            self.air.writeServerEvent('suspicious', avId=leaderId, issue='pressed the GO Button while inside the elevator.')
                        else:
                            self.sendUpdateToAvatarId(leaderId, 'rejectGoToRequest', [elevatorId, boardOkay, avatarsFailingRequirements, avatarsInBattle])
        return False

    def requestGoToFirstTime(self, elevatorId):
        callerId = self.air.getAvatarIdFromSender()
        if self.testGoButtonRequirements(callerId, elevatorId):
            self.sendUpdateToAvatarId(callerId, 'acceptGoToFirstTime', [elevatorId])

    def requestGoToSecondTime(self, elevatorId):
        callerId = self.air.getAvatarIdFromSender()
        avList = self.getGroupMemberList(callerId)
        if self.testGoButtonRequirements(callerId, elevatorId):
            for avId in avList:
                self.sendUpdateToAvatarId(avId, 'acceptGoToSecondTime', [elevatorId])

            THREE_SECONDS = 3.0
            taskMgr.doMethodLater(THREE_SECONDS, self.sendAvatarsToDestinationTask, self.uniqueName('sendAvatarsToDestinationTask'), extraArgs=[elevatorId, avList], appendTask=True)

    def sendAvatarsToDestinationTask(self, elevatorId, avList, task):
        self.notify.debug('entering sendAvatarsToDestinationTask')
        if len(avList):
            if elevatorId in self.elevatorIdList:
                elevator = simbase.air.doId2do.get(elevatorId)
                if elevator:
                    self.notify.warning('Sending avatars %s' % avList)
                    boardOkay, avatarsFailingRequirements, avatarsInBattle = self.testBoard(avList[0], elevatorId, needSpace=0)
                    if not boardOkay == BoardingPartyBase.BOARDCODE_OKAY:
                        for avId in avatarsFailingRequirements:
                            self.air.writeServerEvent('suspicious', avId=avId, issue='failed requirements after the second go button request.')

                        for avId in avatarsInBattle:
                            self.air.writeServerEvent('suspicious', avId=avId, issue='joined battle after the second go button request.')

                    self.air.writeServerEvent('boarding_go', zoneId=self.zoneId, elevatorId=elevatorId, group=avList)
                    elevator.sendAvatarsToDestination(avList)
        return Task.done

    def handleAvatarDisco(self, avId):
        self.notify.debug('handleAvatarDisco %s' % avId)
        if self.avIdDict.has_key(avId):
            leaderId = self.avIdDict[avId]
            self.removeFromGroup(leaderId, avId)

    def handleAvatarZoneChange(self, avId, zoneNew, zoneOld):
        self.notify.debug('handleAvatarZoneChange %s new-%s old-%s bp-%s' % (avId, zoneNew, zoneOld, self.zoneId))
        if zoneNew in self.visibleZones:
            self.toonInZone(avId)
        elif self.avIdDict.has_key(avId):
            leaderId = self.avIdDict[avId]
            self.removeFromGroup(leaderId, avId)

    def toonInZone(self, avId):
        if self.avIdDict.has_key(avId):
            leaderId = self.avIdDict[avId]
            group = self.groupListDict.get(leaderId)
            if leaderId and group:
                self.notify.debug('Calling postGroupInfo from toonInZone')

    def addToGroup(self, leaderId, inviteeId, post=1):
        group = self.groupListDict.get(leaderId)
        if group:
            self.avIdDict[inviteeId] = leaderId
            if inviteeId in group[1]:
                group[1].remove(inviteeId)
            if inviteeId not in group[0]:
                group[0].append(inviteeId)
            self.groupListDict[leaderId] = group
            if post:
                self.notify.debug('Calling postGroupInfo from addToGroup')
                self.sendUpdate('postGroupInfo', [leaderId, group[0], group[1], group[2]])
            self.addWacthAvStatus(inviteeId)
        else:
            self.sendUpdate('postGroupDissolve', [leaderId, leaderId, [], 0])

    def removeFromGroup(self, leaderId, memberId, kick=0, post=1):
        self.notify.debug('removeFromGroup leaderId %s memberId %s' % (leaderId, memberId))
        self.notify.debug('Groups %s' % self.groupListDict)
        self.notify.debug('avDict %s' % self.avIdDict)
        if not self.avIdDict.has_key(leaderId):
            self.sendUpdate('postGroupDissolve', [memberId, leaderId, [], kick])
            if self.avIdDict.has_key(memberId):
                self.avIdDict.pop(memberId)
            return
        self.removeWacthAvStatus(memberId)
        group = self.groupListDict.get(leaderId)
        if group:
            if memberId in group[0]:
                group[0].remove(memberId)
            if memberId in group[1]:
                group[1].remove(memberId)
            if memberId in group[2]:
                group[2].remove(memberId)
            if kick:
                group[2].append(memberId)
        else:
            return
        if memberId == leaderId or len(group[0]) < 2:
            if self.avIdDict.has_key(leaderId):
                self.avIdDict.pop(leaderId)
                for inviteeId in group[1]:
                    if self.avIdDict.has_key(inviteeId):
                        self.avIdDict.pop(inviteeId)
                        self.sendUpdateToAvatarId(inviteeId, 'postInviteCanceled', [])

            dgroup = self.groupListDict.pop(leaderId)
            for dMemberId in dgroup[0]:
                if self.avIdDict.has_key(dMemberId):
                    self.avIdDict.pop(dMemberId)

            self.notify.debug('postGroupDissolve')
            dgroup[0].insert(0, memberId)
            self.sendUpdate('postGroupDissolve', [memberId,
             leaderId,
             dgroup[0],
             kick])
        else:
            self.groupListDict[leaderId] = group
            if post:
                self.notify.debug('Calling postGroupInfo from removeFromGroup')
                self.sendUpdate('postGroupInfo', [leaderId, group[0], group[1], group[2]])
        if self.avIdDict.has_key(memberId):
            self.avIdDict.pop(memberId)
        self.notify.debug('Remove from group END')
        self.notify.debug('Groups %s' % self.groupListDict)
        self.notify.debug('avDict %s' % self.avIdDict)

    def informDestinationInfo(self, offset):
        leaderId = self.air.getAvatarIdFromSender()
        if offset > len(self.elevatorIdList):
            self.air.writeServerEvent('suspicious', avId=leaderId, issue='has requested to go to %s elevator which does not exist' % offset)
            return
        memberList = self.getGroupMemberList(leaderId)
        for avId in memberList:
            if avId != leaderId:
                self.sendUpdateToAvatarId(avId, 'postDestinationInfo', [offset])

    def __isInElevator(self, avId):
        inElevator = False
        for elevatorId in self.elevatorIdList:
            elevator = simbase.air.doId2do.get(elevatorId)
            if elevator:
                if avId in elevator.seats:
                    inElevator = True

        return inElevator