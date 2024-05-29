# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.MinigameGlobals
# Compiled at: 2014-04-30 09:53:54
from direct.showbase import PythonUtil
from toontown.toonbase import ToontownGlobals
from toontown.hood import ZoneUtil
from random import choice
latencyTolerance = 10.0
MaxLoadTime = 40.0
rulesDuration = 16
JellybeanTrolleyHolidayScoreMultiplier = 2
DifficultyOverrideMult = int(65536)

def QuantizeDifficultyOverride(diffOverride):
    return int(round(diffOverride * DifficultyOverrideMult)) / float(DifficultyOverrideMult)


NoDifficultyOverride = 2147483647
NoTrolleyZoneOverride = -1
SafeZones = [ToontownGlobals.ToontownCentral,
 ToontownGlobals.DonaldsDock,
 ToontownGlobals.DaisyGardens,
 ToontownGlobals.MinniesMelodyland,
 ToontownGlobals.TheBrrrgh,
 ToontownGlobals.DonaldsDreamland]

def getDifficulty(trolleyZone):
    hoodZone = getSafezoneId(trolleyZone)
    return float(SafeZones.index(hoodZone)) / (len(SafeZones) - 1)


def getSafezoneId(trolleyZone):
    return ZoneUtil.getCanonicalHoodId(trolleyZone)


def getScoreMult(trolleyZone):
    szId = getSafezoneId(trolleyZone)
    multiplier = PythonUtil.lerp(1.0, 1.5, float(SafeZones.index(szId)) / (len(SafeZones) - 1))
    return multiplier


SuitSerialMessages = [
 'DS-DEBUG1: Suit Serial #0043 -- METHOD', 
 'DS-DEBUG1: Suit Serial #0052 -- USED', 
 'DS-DEBUG1: Suit Serial #0045 -- IS', 
 'DS-DEBUG1: Suit Serial #0041 -- THE', 
 'DS-DEBUG1: Suit Serial #0054 -- SAME', 
 'DS-DEBUG1: Suit Serial #0049 -- AS', 
 'DS-DEBUG1: Suit Serial #004E -- LAST', 
 'DS-DEBUG1: Suit Serial #0047 -- TIME', 
 'DS-DEBUG2: Suit Serial #0045 -- ALL', 
 'DS-DEBUG2: Suit Serial #0051 -- RECORDS', 
 'DS-DEBUG2: Suit Serial #0055 -- EXPUNGED', 
 'DS-DEBUG2: Suit Serial #0049 -- FURTHER', 
 'DS-DEBUG2: Suit Serial #004D -- INVESTIGATION', 
 'DS-DEBUG2: Suit Serial #0045 -- WILL', 
 'DS-DEBUG2: Suit Serial #004E -- BE', 
 'DS-DEBUG2: Suit Serial #0054 -- NECESSARY']

def generateDebugARGPhrase():
    phrase = choice(SuitSerialMessages)
    base.localAvatar.setSystemMessage(0, phrase)