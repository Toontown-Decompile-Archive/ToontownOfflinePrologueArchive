# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.pets.PetHandle
# Compiled at: 2014-04-30 09:53:54
from toontown.toonbase import ToontownGlobals
from toontown.pets import PetMood, PetTraits, PetDetail

class PetHandle:

    def __init__(self, avatar):
        self.doId = avatar.doId
        self.name = avatar.name
        self.style = avatar.style
        self.ownerId = avatar.ownerId
        self.bFake = False
        self.cr = avatar.cr
        self.traits = PetTraits.PetTraits(avatar.traitSeed, avatar.safeZone, traitValueList=avatar.traitList)
        self._grabMood(avatar)

    def _grabMood(self, avatar):
        self.mood = avatar.lastKnownMood.makeCopy()
        self.mood.setPet(self)
        self.lastKnownMood = self.mood.makeCopy()
        self.setLastSeenTimestamp(avatar.lastSeenTimestamp)
        self.updateOfflineMood()

    def getDoId(self):
        return self.doId

    def getOwnerId(self):
        return self.ownerId

    def isPet(self):
        return True

    def getName(self):
        return self.name

    def getDNA(self):
        return self.style

    def getFont(self):
        return ToontownGlobals.getToonFont()

    def setLastSeenTimestamp(self, timestamp):
        self.lastSeenTimestamp = timestamp

    def getTimeSinceLastSeen(self):
        t = self.cr.getServerTimeOfDay() - self.lastSeenTimestamp
        return max(0.0, t)

    def updateOfflineMood(self):
        self.mood.driftMood(dt=self.getTimeSinceLastSeen(), curMood=self.lastKnownMood)

    def getDominantMood(self):
        if not hasattr(self, 'mood'):
            return PetMood.PetMood.Neutral
        return self.mood.getDominantMood()

    def uniqueName(self, idString):
        return idString + '-' + str(self.getDoId())

    def updateMoodFromServer(self, callWhenDone=None):

        def handleGotDetails(avatar, callWhenDone=callWhenDone):
            avatar.announceGenerate()
            self._grabMood(avatar)
            if callWhenDone:
                callWhenDone()

        PetDetail.PetDetail(self.doId, handleGotDetails)