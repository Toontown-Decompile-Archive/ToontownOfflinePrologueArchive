# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.parties.DistributedPartyCannonActivityAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from toontown.parties.DistributedPartyActivityAI import DistributedPartyActivityAI
from toontown.toonbase import TTLocalizer
import PartyGlobals

class DistributedPartyCannonActivityAI(DistributedPartyActivityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPartyCannonActivityAI')

    def __init__(self, air, parent, activityTuple):
        DistributedPartyActivityAI.__init__(self, air, parent, activityTuple)
        self.cloudColors = {}
        self.cloudsHit = {}

    def setMovie(self, todo0, todo1):
        pass

    def setLanded(self, toonId):
        avId = self.air.getAvatarIdFromSender()
        if avId != toonId:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Toon tried to land someone else!')
            return
        else:
            if avId not in self.toonsPlaying:
                self.air.writeServerEvent('suspicious', avId=avId, issue='Toon tried to land while not playing the cannon activity!')
                return
            self.toonsPlaying.remove(avId)
            reward = self.cloudsHit[avId] * PartyGlobals.CannonJellyBeanReward
            if reward > PartyGlobals.CannonMaxTotalReward:
                reward = PartyGlobals.CannonMaxTotalReward
            av = self.air.doId2do.get(avId, None)
            if not av:
                self.air.writeServerEvent('suspicious', avId=avId, issue='Toon tried to award beans while not in district!')
                return
            if reward > 0:
                self.sendUpdateToAvatarId(avId, 'showJellybeanReward', [reward, av.getMoney(), TTLocalizer.PartyCannonResults % (reward, self.cloudsHit[avId])])
                av.addMoney(reward)
            self.sendUpdate('setMovie', [PartyGlobals.CANNON_MOVIE_LANDED, avId])
            del self.cloudsHit[avId]
            return

    def b_setCannonWillFire(self, cannonId, rot, angle, toonId):
        self.toonsPlaying.append(toonId)
        self.cloudsHit[toonId] = 0
        self.sendUpdate('setCannonWillFire', [cannonId, rot, angle])

    def cloudsColorRequest(self):
        avId = self.air.getAvatarIdFromSender()
        self.sendUpdateToAvatarId(avId, 'cloudsColorResponse', [self.cloudColors.values()])

    def requestCloudHit(self, cloudId, r, g, b):
        avId = self.air.getAvatarIdFromSender()
        if avId not in self.toonsPlaying:
            self.air.writeServerEvent('suspicious', avId=avId, issue="Toon tried to hit cloud in cannon activity they're not using!")
            return
        self.cloudColors[cloudId] = [cloudId, r, g, b]
        self.sendUpdate('setCloudHit', [cloudId, r, g, b])
        self.cloudsHit[avId] += 1

    def setToonTrajectoryAi(self, launchTime, x, y, z, h, p, r, vx, vy, vz):
        self.sendUpdate('setToonTrajectory', [self.air.getAvatarIdFromSender(), launchTime, x, y, z, h, p, r, vx, vy, vz])

    def setToonTrajectory(self, todo0, todo1, todo2, todo3, todo4, todo5, todo6, todo7, todo8, todo9, todo10):
        pass

    def updateToonTrajectoryStartVelAi(self, vx, vy, vz):
        avId = self.air.getAvatarIdFromSender()
        self.sendUpdate('updateToonTrajectoryStartVel', [avId, vx, vy, vz])

    def updateToonTrajectoryStartVel(self, todo0, todo1, todo2, todo3):
        pass