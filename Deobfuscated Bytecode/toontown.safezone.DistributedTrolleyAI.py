# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.safezone.DistributedTrolleyAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import *
from direct.fsm.FSM import FSM
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from TrolleyConstants import *
from toontown.minigame.MinigameCreatorAI import *
from toontown.quest import Quests
from otp.ai.MagicWordGlobal import *
doesntWantTrolleyTracks = {}

class DistributedTrolleyAI(DistributedObjectAI, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTrolleyAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        FSM.__init__(self, 'DistributedTrolleyAI')
        self.trolleyCountdownTime = config.GetFloat('trolley-countdown-time', TROLLEY_COUNTDOWN_TIME)
        self.slots = [
         None, None, None, None]
        self.boardable = False
        return

    def announceGenerate(self):
        self.b_setState('WaitEmpty')

    def setState(self, state):
        self.request(state)

    def d_setState(self, state):
        state = state[:1].lower() + state[1:]
        self.sendUpdate('setState', [state, globalClockDelta.getRealNetworkTime()])

    def b_setState(self, state):
        self.setState(state)
        self.d_setState(state)

    def enterWaitEmpty(self):
        self.boardable = True

    def exitWaitEmpty(self):
        self.boardable = False

    def enterWaitCountdown(self):
        self.boardable = True
        self.departureTask = taskMgr.doMethodLater(self.trolleyCountdownTime, self.__depart, 'trolleyDepartureTask')

    def __depart(self, task):
        self.b_setState('Leaving')
        return task.done

    def exitWaitCountdown(self):
        taskMgr.remove(self.departureTask)
        self.boardable = False

    def enterLeaving(self):
        self.leavingTask = taskMgr.doMethodLater(TROLLEY_EXIT_TIME, self.__activateMinigame, 'trolleyLeaveTask')

    def isNewbie(self, avId):
        toon = self.air.doId2do.get(avId)
        if not toon:
            return False
        return Quests.avatarHasTrolleyQuest(toon)

    def __activateMinigame(self, task):
        players = [ player for player in self.slots if player is not None ]
        if players:
            newbieIds = []
            for avId in players:
                if self.isNewbie(avId):
                    newbieIds.append(avId)
                mg = createMinigame(self.air, players, self.zoneId, newbieIds=newbieIds)

            for player in players:
                self.sendUpdateToAvatarId(player, 'setMinigameZone', [mg['minigameZone'], mg['minigameId']])
                self.removeFromTrolley(player)

        self.b_setState('Entering')
        return task.done

    def exitLeaving(self):
        taskMgr.remove(self.leavingTask)

    def enterEntering(self):
        self.enteringTask = taskMgr.doMethodLater(TROLLEY_ENTER_TIME, self.__doneEntering, 'trolleyEnterTask')

    def __doneEntering(self, task):
        self.b_setState('WaitEmpty')
        return task.done

    def exitEntering(self):
        taskMgr.remove(self.enteringTask)

    def getBoardingSlot(self):
        if not self.boardable:
            return -1
        else:
            if None not in self.slots:
                return -1
            return self.slots.index(None)

    def requestBoard(self):
        avId = self.air.getAvatarIdFromSender()
        if avId in self.slots:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Toon requested to board a trolley twice!')
            self.sendUpdateToAvatarId(avId, 'rejectBoard', [avId])
            return
        slot = self.getBoardingSlot()
        if slot == -1:
            self.sendUpdateToAvatarId(avId, 'rejectBoard', [avId])
            return
        self.acceptOnce(self.air.getAvatarExitEvent(avId), self.removeFromTrolley, extraArgs=[avId])
        self.sendUpdate('emptySlot%d' % slot, [0, globalClockDelta.getRealNetworkTime()])
        self.sendUpdate('fillSlot%d' % slot, [avId])
        self.slots[slot] = avId
        if self.state == 'WaitEmpty':
            self.b_setState('WaitCountdown')

    def requestExit(self):
        avId = self.air.getAvatarIdFromSender()
        if avId not in self.slots:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Toon requested to exit a trolley they are not on!')
            return
        if not self.boardable:
            return
        self.removeFromTrolley(avId, True)

    def removeFromTrolley(self, avId, hopOff=False):
        if avId not in self.slots:
            return
        else:
            self.ignore(self.air.getAvatarExitEvent(avId))
            slot = self.slots.index(avId)
            self.sendUpdate('fillSlot%d' % slot, [0])
            if hopOff:
                self.sendUpdate('emptySlot%d' % slot, [avId, globalClockDelta.getRealNetworkTime()])
            self.sendUpdate('emptySlot%d' % slot, [0, globalClockDelta.getRealNetworkTime()])
            self.slots[slot] = None
            if self.state == 'WaitCountdown' and self.slots.count(None) == 4:
                self.b_setState('WaitEmpty')
            return


@magicWord(category=CATEGORY_OVERRIDE, types=[str])
def travel(target='self'):
    if target == 'everyone':
        if 'everyone' in doesntWantTrolleyTracks:
            del doesntWantTrolleyTracks['everyone']
            return 'Re-enabled Trolley Tracks in the current district.'
        else:
            doesntWantTrolleyTracks['everyone'] = True
            return 'Disabled Trolley Tracks in the current district.'

    else:
        if spellbook.getTarget().doId in doesntWantTrolleyTracks:
            del doesntWantTrolleyTracks[spellbook.getTarget().doId]
            return 'Re-enabled Trolley Tracks.'
        else:
            doesntWantTrolleyTracks[spellbook.getTarget().doId] = True
            return 'Disabled Trolley Tracks.'