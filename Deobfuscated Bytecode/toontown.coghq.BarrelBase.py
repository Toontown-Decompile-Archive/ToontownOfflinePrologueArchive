# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.BarrelBase
# Compiled at: 2014-04-30 09:53:54
import random

class BarrelBase:

    def getRng(self):
        return random.Random(self.entId * self.level.doId)

    def getRewardPerGrab(self):
        if not hasattr(self, '_reward'):
            if self.rewardPerGrabMax > self.rewardPerGrab:
                self._reward = self.getRng().randrange(self.rewardPerGrab, self.rewardPerGrabMax + 1)
            else:
                self._reward = self.rewardPerGrab
        return self._reward

    def getGagLevel(self):
        if not hasattr(self, '_gagLevel'):
            if self.gagLevelMax > self.gagLevel:
                self._gagLevel = self.getRng().randrange(self.gagLevel, self.gagLevelMax + 1)
            else:
                self._gagLevel = self.gagLevel
        return self._gagLevel

    def getGagTrack(self):
        if not hasattr(self, '_gagTrack'):
            if self.gagTrack == 'random':
                tracks = (0, 1, 2, 3, 4, 4, 5, 5, 6)
                self._gagTrack = self.getRng().choice(tracks)
            else:
                self._gagTrack = self.gagTrack
        return self._gagTrack

    if __dev__:

        def setRewardPerGrab(self, rewardPerGrab):
            if hasattr(self, '_reward'):
                del self._reward
            self.rewardPerGrab = rewardPerGrab

        def setRewardPerGrabMax(self, rewardPerGrabMax):
            if hasattr(self, '_reward'):
                del self._reward
            self.rewardPerGrabMax = rewardPerGrabMax

        def setGagLevel(self, gagLevel):
            if hasattr(self, '_gagLevel'):
                del self._gagLevel
            self.gagLevel = gagLevel

        def setGagLevelMax(self, gagLevelMax):
            if hasattr(self, '_gagLevel'):
                del self._gagLevel
            self.gagLevelMax = gagLevelMax

        def setGagTrack(self, gagTrack):
            if hasattr(self, '_gagTrack'):
                del self._gagTrack
            self.gagTrack = gagTrack