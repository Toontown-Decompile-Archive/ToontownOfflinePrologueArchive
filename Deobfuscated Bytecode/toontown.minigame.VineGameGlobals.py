# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.VineGameGlobals
# Compiled at: 2014-04-30 09:53:54
from toontown.toonbase import ToontownGlobals
from pandac.PandaModules import BitMask32
NumVines = 20
GameDuration = 70
ShowScoresDuration = 4.0
VineStartingT = 0.25
VineFellDownT = 0.1
EndlessGame = False
BonusPerSecondLeft = 0.4
JumpTimeBuffer = 0.5
SpiderBitmask = ToontownGlobals.CatchGameBitmask
TreasureBitmask = ToontownGlobals.PieBitmask
VineXIncrement = 30
VineHeight = 30
BatMaxHeight = 28
BatMinHeight = 10
RadarCameraBitmask = BitMask32.bit(3)
CourseSections = (
 (
  (20, 30, 4, 0),
  (19, 39, 3.1, 0),
  (18, 41, 4, 0),
  (19, 38, 3.2, 0),
  (20, 30, 6, 0)),
 (
  (20, 30, 3, 0),
  (18, 40, 4.1, 0),
  (19, 31, 5.1, 0),
  (18, 41, 4.2, 0),
  (20, 30, 5, 0)),
 (
  (20, 30, 3, 0),
  (15, 39, 4.1, 0),
  (19, 29, 5, 0),
  (16, 38, 4.2, 0),
  (20, 30, 5, 0)),
 (
  (20, 30, 3, 0),
  (18, 36, 4.1, 0),
  (19, 30, 5, 9),
  (18, 38, 4.2, 0),
  (20, 30, 5, 0)),
 (
  (20, 30, 3, 0),
  (18, 15, 4.1, 0),
  (19, 30, 5, 11),
  (18, 16, 4.2, 0),
  (20, 30, 5, 0)),
 (
  (20, 30, 3, 0),
  (18, 11, 4.1, 0),
  (15, 12, 5, 0),
  (18, 16, 4.2, 0),
  (20, 30, 5, 0)),
 (
  (20, 30, 3, 0),
  (15, 39, 4.1, 13),
  (19, 29, 5, 0),
  (16, 38, 4.2, 0),
  (20, 30, 5, 0)),
 (
  (20, 30, 3, 0),
  (18, 26, 4.1, 9),
  (19, 30, 5, 0),
  (18, 28, 4.2, 12),
  (20, 30, 5, 0)),
 (
  (20, 30, 3, 0),
  (15, 26, 4.1, 9),
  (19, 30, 5, 0),
  (15, 28, 4.2, 12),
  (20, 30, 5, 0)),
 (
  (15, 50, 4, 0),
  (15, 40, 4.1, 0),
  (19, 40, 5, 0),
  (19, 28, 4.2, 0),
  (20, 30, 5, 0)))
CourseWeights = {ToontownGlobals.ToontownCentral: ((0, 25),
                                   (1, 25),
                                   (2, 25),
                                   (3, 25)), 
   ToontownGlobals.DonaldsDock: (
                               (1, 25),
                               (2, 25),
                               (3, 25),
                               (4, 25)), 
   ToontownGlobals.DaisyGardens: (
                                (2, 25),
                                (3, 25),
                                (4, 25),
                                (5, 25)), 
   ToontownGlobals.MinniesMelodyland: (
                                     (3, 25),
                                     (4, 25),
                                     (5, 25),
                                     (6, 25)), 
   ToontownGlobals.TheBrrrgh: (
                             (4, 25),
                             (5, 25),
                             (6, 25),
                             (7, 25)), 
   ToontownGlobals.DonaldsDreamland: (
                                    (4, 20),
                                    (5, 20),
                                    (6, 20),
                                    (7, 20),
                                    (8, 20))}
BaseBonusOnEndVine = {ToontownGlobals.ToontownCentral: 4, ToontownGlobals.DonaldsDock: 5, 
   ToontownGlobals.DaisyGardens: 6, 
   ToontownGlobals.MinniesMelodyland: 7, 
   ToontownGlobals.TheBrrrgh: 8, 
   ToontownGlobals.DonaldsDreamland: 9}
BatInfo = {ToontownGlobals.ToontownCentral: ((60, 0, 0.35), ), ToontownGlobals.DonaldsDock: (
                               (60, 0, 0.25), (30, 30)), 
   ToontownGlobals.DaisyGardens: (
                                (60, 0, 0.25), (15, 30)), 
   ToontownGlobals.MinniesMelodyland: (
                                     (60, 0, 0.25), (10, 25)), 
   ToontownGlobals.TheBrrrgh: (
                             (60, 0, 0.25), (30, 30), (30, 20)), 
   ToontownGlobals.DonaldsDreamland: (
                                    (60, 0, 0.25), (30, 30), (10, 20))}
SpiderLimits = {ToontownGlobals.ToontownCentral: 1, ToontownGlobals.DonaldsDock: 2, 
   ToontownGlobals.DaisyGardens: 2, 
   ToontownGlobals.MinniesMelodyland: 3, 
   ToontownGlobals.TheBrrrgh: 3, 
   ToontownGlobals.DonaldsDreamland: 4}

def getNumSpidersInSection(sectionIndex):
    if sectionIndex < 0 or sectionIndex >= len(CourseSections):
        return 0
    numSpiders = 0
    for vine in CourseSections[sectionIndex]:
        if vine[3]:
            numSpiders += 1

    return numSpiders