# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.ToonBlitzGlobals
# Compiled at: 2014-04-30 09:53:54
from toontown.toonbase import ToontownGlobals
from pandac.PandaModules import BitMask32
ShowScoresDuration = 4.0
EndlessGame = config.GetBool('endless-2d-game', 0)
ScoreToJellyBeansMultiplier = 5
ScoreGainPerTreasure = 1
ToonStartingPosition = (-39, 0, 13.59)
CameraStartingPosition = (-28, -53, 17.3, 0, 0, 0)
GameDuration = {ToontownGlobals.ToontownCentral: 150, ToontownGlobals.DonaldsDock: 145, 
   ToontownGlobals.DaisyGardens: 140, 
   ToontownGlobals.MinniesMelodyland: 135, 
   ToontownGlobals.TheBrrrgh: 130, 
   ToontownGlobals.DonaldsDreamland: 125}
BaseBonusOnCompletion = {ToontownGlobals.ToontownCentral: 15, ToontownGlobals.DonaldsDock: 17, 
   ToontownGlobals.DaisyGardens: 19, 
   ToontownGlobals.MinniesMelodyland: 21, 
   ToontownGlobals.TheBrrrgh: 23, 
   ToontownGlobals.DonaldsDreamland: 25}
BonusPerSecondLeft = 0.8
ScoreLossPerEnemyCollision = {ToontownGlobals.ToontownCentral: -1, ToontownGlobals.DonaldsDock: -1, 
   ToontownGlobals.DaisyGardens: -1, 
   ToontownGlobals.MinniesMelodyland: -1, 
   ToontownGlobals.TheBrrrgh: -1, 
   ToontownGlobals.DonaldsDreamland: -1}
ScoreLossPerFallDown = {ToontownGlobals.ToontownCentral: 0, ToontownGlobals.DonaldsDock: 0, 
   ToontownGlobals.DaisyGardens: 0, 
   ToontownGlobals.MinniesMelodyland: 0, 
   ToontownGlobals.TheBrrrgh: 0, 
   ToontownGlobals.DonaldsDreamland: 0}
ScoreLossPerStomperSquish = {ToontownGlobals.ToontownCentral: -1, ToontownGlobals.DonaldsDock: -1, 
   ToontownGlobals.DaisyGardens: -1, 
   ToontownGlobals.MinniesMelodyland: -1, 
   ToontownGlobals.TheBrrrgh: -1, 
   ToontownGlobals.DonaldsDreamland: -1}
SectionWeights = {ToontownGlobals.ToontownCentral: ((0, 25),
                                   (1, 25),
                                   (2, 25),
                                   (3, 15),
                                   (4, 10),
                                   (5, 0)), 
   ToontownGlobals.DonaldsDock: (
                               (0, 15),
                               (1, 25),
                               (2, 25),
                               (3, 15),
                               (4, 10),
                               (5, 10)), 
   ToontownGlobals.DaisyGardens: (
                                (0, 15),
                                (1, 15),
                                (2, 25),
                                (3, 25),
                                (4, 10),
                                (5, 10)), 
   ToontownGlobals.MinniesMelodyland: (
                                     (0, 10),
                                     (1, 10),
                                     (2, 25),
                                     (3, 25),
                                     (4, 15),
                                     (5, 15)), 
   ToontownGlobals.TheBrrrgh: (
                             (0, 10),
                             (1, 10),
                             (2, 15),
                             (3, 25),
                             (4, 25),
                             (5, 15)), 
   ToontownGlobals.DonaldsDreamland: (
                                    (0, 10),
                                    (1, 10),
                                    (2, 15),
                                    (3, 15),
                                    (4, 25),
                                    (5, 25))}
NumSections = {ToontownGlobals.ToontownCentral: 5, ToontownGlobals.DonaldsDock: 5, 
   ToontownGlobals.DaisyGardens: 5, 
   ToontownGlobals.MinniesMelodyland: 5, 
   ToontownGlobals.TheBrrrgh: 5, 
   ToontownGlobals.DonaldsDreamland: 5}
PercentMaxEnemies = {ToontownGlobals.ToontownCentral: 50, ToontownGlobals.DonaldsDock: 60, 
   ToontownGlobals.DaisyGardens: 70, 
   ToontownGlobals.MinniesMelodyland: 80, 
   ToontownGlobals.TheBrrrgh: 90, 
   ToontownGlobals.DonaldsDreamland: 100}
PercentMaxTreasures = {ToontownGlobals.ToontownCentral: 100, ToontownGlobals.DonaldsDock: 100, 
   ToontownGlobals.DaisyGardens: 100, 
   ToontownGlobals.MinniesMelodyland: 100, 
   ToontownGlobals.TheBrrrgh: 100, 
   ToontownGlobals.DonaldsDreamland: 100}
PercentMaxSpawnPoints = {ToontownGlobals.ToontownCentral: 100, ToontownGlobals.DonaldsDock: 90, 
   ToontownGlobals.DaisyGardens: 80, 
   ToontownGlobals.MinniesMelodyland: 70, 
   ToontownGlobals.TheBrrrgh: 60, 
   ToontownGlobals.DonaldsDreamland: 50}
PercentMaxStompers = {ToontownGlobals.ToontownCentral: 50, ToontownGlobals.DonaldsDock: 60, 
   ToontownGlobals.DaisyGardens: 70, 
   ToontownGlobals.MinniesMelodyland: 80, 
   ToontownGlobals.TheBrrrgh: 90, 
   ToontownGlobals.DonaldsDreamland: 100}
TreasureValueProbability = {1: 4, 2: 3, 
   3: 2, 
   4: 1}
BLOCK_H24 = 'BlockH24'
BLOCK_V24F = 'BlockV24F'
BLOCK_V24B = 'BlockV24B'
BLOCK_H12 = 'BlockH12'
BLOCK_V12F = 'BlockV12F'
BLOCK_V12B = 'BlockV12B'
BLOCK_H6 = 'BlockH6'
BLOCK_V6F = 'BlockV6F'
BLOCK_V6B = 'BlockV6B'
BLOCK_H3 = 'BlockH3'
BLOCK_V3F = 'BlockV3F'
BLOCK_V3B = 'BlockV3B'
BlockTypes = {BLOCK_H24: ('00',
             (0, 0, 0),
             (0, 0, 0),
             (1, 1, 1)), 
   BLOCK_V24F: (
              '00',
              (0, 0, 0),
              (0, 0, 270),
              (1, 1, 1)), 
   BLOCK_V24B: (
              '00',
              (0, 0, 0),
              (0, 0, 90),
              (1, 1, 1)), 
   BLOCK_H12: (
             '01',
             (0, 0, 0),
             (0, 0, 0),
             (1, 1, 1)), 
   BLOCK_V12F: (
              '01',
              (0, 0, 0),
              (0, 0, 270),
              (1, 1, 1)), 
   BLOCK_V12B: (
              '01',
              (0, 0, 0),
              (0, 0, 90),
              (1, 1, 1)), 
   BLOCK_H6: (
            '02',
            (0, 0, 0),
            (0, 0, 0),
            (1, 1, 1)), 
   BLOCK_V6F: (
             '02',
             (0, 0, 0),
             (0, 0, 270),
             (0.86, 1, 1)), 
   BLOCK_V6B: (
             '02',
             (0, 0, 0),
             (0, 0, 90),
             (0.86, 1, 1)), 
   BLOCK_H3: (
            '03',
            (0, 0, 0),
            (0, 0, 0),
            (1, 1, 1)), 
   BLOCK_V3F: (
             '03',
             (0, 0, 0),
             (0, 0, 270),
             (1, 1, 1)), 
   BLOCK_V3B: (
             '03',
             (0, 0, 0),
             (0, 0, 90),
             (1, 1, 1))}
BlocksList = []
SpawnPointList = []
DamagePerBullet = 25
EnemyBaseHealth = 25
EnemyHealthMultiplier = {'f': 1, 'p': 1, 
   'ym': 1, 
   'mm': 1, 
   'bf': 1, 
   'b': 1, 
   'dt': 1, 
   'sc': 1, 
   'pp': 1, 
   'tw': 1, 
   'cc': 1, 
   'tm': 1}
NumEnemies = 2
EnemyList = []
NumTreasures = 5
TreasureList = []
BlockListStart = [[BLOCK_H24, [(0, 0, 12)]]]
BlockListEnd = [[BLOCK_H24, [(0, 0, 12)]], [BLOCK_H24, [(24, 0, 12)]], [BLOCK_H24, [(48, 0, 12)]]]
SpawnPointListEnd = [[(45, 0, 16)]]
BlockList0 = [[BLOCK_H24, [(0, 0, 12)]],
 [
  BLOCK_H24, [(22.4, 0, 12)]],
 [
  BLOCK_H24, [(42.9, 0, 12)]],
 [
  BLOCK_H24, [(30, 0, 18.75)]],
 [
  BLOCK_H24, [(58, 0, 18.75)]],
 [
  BLOCK_H24, [(0, 0, 18.75)]]]
EnemyList0 = [['tm', [(35, 0, 12.65), (30, 0, 12.65), 2]], ['tm', [(24, 0, 12.65), (24, 0, 30.0), 2]]]
TreasureList0 = [[(16, 0, 16)],
 [
  (30, 0, 23)],
 [
  (40, 0, 23)],
 [
  (50, 0, 16)],
 [
  (50, 0, 23)]]
SpawnPointList0 = [[(9, 0, 16), (4, 0, 16)], [(80, 0, 16)]]
StomperTypes = {1: (1,
     2,
     [
      0, -4],
     [
      1, 6.75],
     3), 
   2: (
     1,
     5,
     [
      0.6, -0.34],
     [
      0.2, 1.5],
     2), 
   3: (
     1,
     2,
     [
      0, -9.85],
     [
      1, 15],
     5)}
BlockList1 = [[BLOCK_H12, [(0, 0, 12)]],
 [
  BLOCK_H12, [(16, 0, 18.75)]],
 [
  BLOCK_H12, [(36, 0, 12)]],
 [
  BLOCK_H12, [(64, 0, 12)]],
 [
  BLOCK_H24, [(19, 0, 5.25)]],
 [
  BLOCK_H24, [(43, 0, 5.25)]],
 [
  BLOCK_H24, [(67, 0, 5.25)]],
 [
  BLOCK_H12, [(82, 0, 18.75)]]]
TreasureList1 = [[(8, 0, 27.25)],
 [
  (36, 0, 27.25)],
 [
  (20, 0, 7.25)],
 [
  (32, 0, 7.25)],
 [
  (56, 0, 22.5)],
 [
  (56, 0, 7.25)],
 [
  (80, 0, 7.25)],
 [
  (90, 0, 7.25)],
 [
  (74, 0, 27.25)],
 [
  (102, 0, 27.25)]]
SpawnPointList1 = [[(2, 0, 16)], [(73, 0, 16)]]
EnemyList1 = [['f', [(20, 0, 6), (50, 0, 6), 3.5]],
 [
  'bf', [(50, 0, 6), (20, 0, 6), 3.5]],
 [
  'f', [(62, 0, 6), (90, 0, 6), 3.5]],
 [
  'bf', [(90, 0, 6), (62, 0, 6), 3.5]],
 [
  'dt', [(52, 0, 6), (52, 0, 28), 3.5]],
 [
  'b', [(60, 0, 28), (60, 0, 6), 3.5]]]
BlockList2 = [[BLOCK_H12, [(0, 0, 12)]],
 [
  BLOCK_H12, [(16, 0, 18.75)]],
 [
  BLOCK_H6, [(34, 0, 12)]],
 [
  BLOCK_H12, [(25, 0, 5.25)]],
 [
  BLOCK_H24, [(34, 0, 25.5)]],
 [
  BLOCK_H12, [(64, 0, 18.75)]],
 [
  BLOCK_H6, [(52, 0, 12)]],
 [
  BLOCK_H12, [(55, 0, 5.25)]],
 [
  BLOCK_H12, [(80, 0, 12), (100, 0, 12), 2.5]]]
TreasureList2 = [[(8, 0, 27.25)],
 [
  (26, 0, 7.25)],
 [
  (36, 0, 7.25)],
 [
  (26, 0, 34)],
 [
  (66, 0, 34)],
 [
  (42, 0, 23)],
 [
  (46, 0, 21)],
 [
  (50, 0, 23)],
 [
  (56, 0, 7.25)],
 [
  (66, 0, 7.25)],
 [
  (84, 0, 28)],
 [
  (20, 0, 14)],
 [
  (72, 0, 14)]]
SpawnPointList2 = [[(2, 0, 16)], [(72, 0, 22.75)]]
EnemyList2 = [['p', [(31, 0, 6), (31, 0, 31), 3.5]],
 [
  'ym', [(31, 0, 31), (31, 0, 6), 3.5]],
 [
  'bf', [(61, 0, 6), (61, 0, 31), 3.5]],
 [
  'b', [(61, 0, 31), (61, 0, 6), 3.5]],
 [
  'sc', [(35, 0, 26.25), (57, 0, 26.25), 3.5]],
 [
  'tw', [(57, 0, 26.25), (35, 0, 26.25), 3.5]]]
BlockList3 = [[BLOCK_H12, [(0, 0, 12)]],
 [
  BLOCK_H12, [(12, 0, 5.25), (36, 0, 25.5), 3]],
 [
  BLOCK_H12, [(48, 0, 25.5)]],
 [
  BLOCK_H12, [(60, 0, 25.5), (84, 0, 5.25), 3]],
 [
  BLOCK_H12, [(102, 0, 5.25)]],
 [
  BLOCK_H12, [(120, 0, 5.25), (138, 0, 5.25), 2.5]],
 [
  BLOCK_H12, [(156, 0, 5.25)]],
 [
  BLOCK_H12, [(174, 0, 5.25), (174, 0, 25.5), 2.5]]]
TreasureList3 = [[(28, 0, 32)],
 [
  (24, 0, 28)],
 [
  (20, 0, 24)],
 [
  (16, 0, 20)],
 [
  (80, 0, 32)],
 [
  (84, 0, 28)],
 [
  (88, 0, 24)],
 [
  (92, 0, 20)],
 [
  (48, 0, 34)],
 [
  (60, 0, 34)],
 [
  (125, 0, 15)],
 [
  (135, 0, 15)],
 [
  (145, 0, 15)],
 [
  (180, 0, 7.25)],
 [
  (168, 0, 34)],
 [
  (192, 0, 34)]]
SpawnPointList3 = [[(2, 0, 16)],
 [
  (56, 0, 29.5)],
 [
  (108, 0, 9.25)],
 [
  (162, 0, 9.25)]]
EnemyList3 = [['p', [(31, 0, 6), (31, 0, 31), 3.5]],
 [
  'ym', [(31, 0, 31), (31, 0, 6), 3.5]],
 [
  'bf', [(61, 0, 6), (61, 0, 31), 3.5]],
 [
  'b', [(61, 0, 31), (61, 0, 6), 3.5]],
 [
  'sc', [(35, 0, 26.25), (57, 0, 26.25), 3.5]],
 [
  'tw', [(57, 0, 26.25), (35, 0, 26.25), 3.5]]]
BlockList5 = [[BLOCK_H24, [(0, 0, 12)]],
 [
  BLOCK_H24, [(24, 0, 12)]],
 [
  BLOCK_H24, [(48, 0, 12)]],
 [
  BLOCK_H6, [(12, 0, 18.75)]],
 [
  BLOCK_H6, [(18, 0, 25.5)]],
 [
  BLOCK_H6, [(24, 0, 18.75)]],
 [
  BLOCK_H6, [(44, 0, 18.75)]],
 [
  BLOCK_H6, [(50, 0, 25.5)]],
 [
  BLOCK_H6, [(56, 0, 18.75)]]]
TreasureList5 = [[(15, 0, 20.75)],
 [
  (21, 0, 27.5)],
 [
  (27, 0, 20.75)],
 [
  (47, 0, 20.75)],
 [
  (53, 0, 27.5)],
 [
  (59, 0, 20.75)]]
SpawnPointList5 = [[(2, 0, 16)]]
BlockList6 = [[BLOCK_H24, [(0, 0, 12)]],
 [
  BLOCK_H24, [(0, 0, 5.25)]],
 [
  BLOCK_H24, [(24, 0, 5.25)]],
 [
  BLOCK_H24, [(48, 0, 5.25)]],
 [
  BLOCK_H12, [(72, 0, 5.25)]],
 [
  BLOCK_H12, [(30, 0, 12)]],
 [
  BLOCK_H12, [(48, 0, 12)]],
 [
  BLOCK_H24, [(66, 0, 12)]]]
TreasureList6 = [[(27, 0, 20.75)],
 [
  (45, 0, 20.75)],
 [
  (63, 0, 20.75)],
 [
  (3, 0, 7.25)],
 [
  (15, 0, 7.25)],
 [
  (36, 0, 7.25)],
 [
  (54, 0, 7.25)],
 [
  (70, 0, 7.25)],
 [
  (81, 0, 7.25)]]
SpawnPointList6 = [[(2, 0, 16)]]
BlockList7 = [[BLOCK_H12, [(0, 0, 12)]],
 [
  BLOCK_H12, [(10, 0, 18.75)]],
 [
  BLOCK_H12, [(20, 0, 25.5)]],
 [
  BLOCK_H12, [(30, 0, 18.75)]],
 [
  BLOCK_H24, [(40, 0, 12)]],
 [
  BLOCK_H24, [(14, 0, 5.25)]],
 [
  BLOCK_H3, [(11, 0, 5.25)]],
 [
  BLOCK_H3, [(38, 0, 5.25)]],
 [
  BLOCK_H12, [(62, 0, 18.75)]],
 [
  BLOCK_H12, [(72, 0, 12)]],
 [
  BLOCK_H12, [(82, 0, 5.25)]],
 [
  BLOCK_H12, [(92, 0, 12)]],
 [
  BLOCK_H12, [(102, 0, 18.75)]],
 [
  BLOCK_H12, [(112, 0, 12)]],
 [
  BLOCK_H24, [(76, 0, 25.5)]],
 [
  BLOCK_H3, [(73, 0, 25.5)]],
 [
  BLOCK_H3, [(100, 0, 25.5)]]]
TreasureList7 = [[(12, 0, 34)],
 [
  (26, 0, 34)],
 [
  (40, 0, 34)],
 [
  (26, 0, 23)],
 [
  (26, 0, 12)],
 [
  (13, 0, 7.25)],
 [
  (40, 0, 7.25)],
 [
  (88, 0, 34)],
 [
  (112, 0, 34)],
 [
  (64, 0, 34)],
 [
  (88, 0, 7.25)],
 [
  (88, 0, 23)]]
SpawnPointList7 = [[(2, 0, 16)]]
BlockList8 = [[BLOCK_H12, [(0, 0, 12)]],
 [
  BLOCK_H24, [(0, 0, 5.25)]],
 [
  BLOCK_H12, [(16, 0, 18.75)]],
 [
  BLOCK_H24, [(32, 0, 25.5)]],
 [
  BLOCK_H12, [(64, 0, 25.5)]],
 [
  BLOCK_H12, [(84, 0, 25.5)]],
 [
  BLOCK_H6, [(104, 0, 25.5)]],
 [
  BLOCK_H6, [(118, 0, 25.5)]],
 [
  BLOCK_H3, [(132, 0, 25.5)]],
 [
  BLOCK_H3, [(143, 0, 25.5)]],
 [
  BLOCK_H3, [(154, 0, 25.5)]],
 [
  BLOCK_H24, [(32, 0, 5.25)]],
 [
  BLOCK_H12, [(64, 0, 5.25)]],
 [
  BLOCK_H12, [(84, 0, 5.25)]],
 [
  BLOCK_H6, [(104, 0, 5.25)]],
 [
  BLOCK_H6, [(118, 0, 5.25)]],
 [
  BLOCK_H3, [(132, 0, 5.25)]],
 [
  BLOCK_H3, [(143, 0, 5.25)]],
 [
  BLOCK_H3, [(154, 0, 5.25)]],
 [
  BLOCK_H3, [(161, 0, 18.75)]],
 [
  BLOCK_H6, [(160, 0, 12)]]]
TreasureList8 = [[(1, 0, 7.25)],
 [
  (4, 0, 7.25)],
 [
  (26, 0, 34)],
 [
  (10, 0, 28)],
 [
  (154, 0, 20.75)],
 [
  (60, 0, 34)],
 [
  (80, 0, 34)],
 [
  (100, 0, 34)],
 [
  (114, 0, 34)],
 [
  (128, 0, 34)],
 [
  (139, 0, 34)],
 [
  (150, 0, 34)],
 [
  (60, 0, 13.75)],
 [
  (80, 0, 13.75)],
 [
  (100, 0, 13.75)],
 [
  (114, 0, 13.75)],
 [
  (128, 0, 13.75)],
 [
  (139, 0, 13.75)],
 [
  (150, 0, 13.75)]]
SpawnPointList8 = [[(2, 0, 16)], [(128, 0, 29.5), (121, 0, 29.5)], [(128, 0, 9.25), (121, 0, 9.25)]]
BlockList9 = [[BLOCK_H24, [(0, 0, 12)]],
 [
  BLOCK_H12, [(28, 0, 12), (50, 0, 12), 3]],
 [
  BLOCK_H12, [(66, 0, 12)]],
 [
  BLOCK_H12, [(82, 0, 12), (104, 0, 12), 3]],
 [
  BLOCK_H12, [(120, 0, 12)]],
 [
  BLOCK_H12, [(136, 0, 25.5), (136, 0, 5.25), 3]],
 [
  BLOCK_H12, [(152, 0, 25.5)]],
 [
  BLOCK_H12, [(152, 0, 5.25)]],
 [
  BLOCK_H12, [(168, 0, 25.5), (168, 0, 5.25), 3]],
 [
  BLOCK_H12, [(184, 0, 12)]]]
TreasureList9 = [[(36, 0, 23)],
 [
  (45, 0, 23)],
 [
  (54, 0, 23)],
 [
  (90, 0, 23)],
 [
  (99, 0, 23)],
 [
  (108, 0, 23)],
 [
  (142, 0, 35)],
 [
  (142, 0, 8)],
 [
  (130, 0, 30)],
 [
  (158, 0, 7.25)],
 [
  (158, 0, 27.5)],
 [
  (174, 0, 35)],
 [
  (174, 0, 8)],
 [
  (186, 0, 30)]]
SpawnPointList9 = [[(2, 0, 16)], [(126, 0, 16)]]
BlockList10 = [[BLOCK_H12, [(0, 0, 12)]],
 [
  BLOCK_H12, [(14, 0, 12), (40, 0, 12), 3.5]],
 [
  BLOCK_H6, [(40, 0, 25.5)]],
 [
  BLOCK_H6, [(40, 0, 5.25)]],
 [
  BLOCK_H12, [(54, 0, 32), (54, 0, -1.5), 3.5]],
 [
  BLOCK_H6, [(74, 0, 25.5)]],
 [
  BLOCK_H6, [(74, 0, 5.25)]],
 [
  BLOCK_H12, [(82, 0, 5.25), (114, 0, 5.25), 3.7]],
 [
  BLOCK_H6, [(130, 0, 5.25)]],
 [
  BLOCK_H6, [(130, 0, 25.5)]],
 [
  BLOCK_H12, [(144, 0, 32), (144, 0, -1.5), 3.5]],
 [
  BLOCK_H6, [(164, 0, 25.5)]],
 [
  BLOCK_H6, [(164, 0, 5.25)]],
 [
  BLOCK_H12, [(202, 0, 25.5), (172, 0, 25.5), 4]]]
TreasureList10 = [[(43, 0, 27.5)],
 [
  (43, 0, 7.25)],
 [
  (32, 0, 32)],
 [
  (77, 0, 27.5)],
 [
  (77, 0, 7.25)],
 [
  (88, 0, 32)],
 [
  (97, 0, 15)],
 [
  (105, 0, 15)],
 [
  (113, 0, 15)],
 [
  (133, 0, 27.5)],
 [
  (133, 0, 7.25)],
 [
  (122, 0, 32)],
 [
  (167, 0, 27.5)],
 [
  (167, 0, 7.25)],
 [
  (173, 0, 14)]]
SpawnPointList10 = [[(2, 0, 16)], [(133, 0, 9.25)], [(77, 0, 29.5)]]
BlockList11 = [[BLOCK_H24, [(0, 0, 12)]],
 [
  BLOCK_H24, [(24, 0, 12)]],
 [
  BLOCK_H24, [(24, 0, 18.75)]],
 [
  BLOCK_H24, [(48, 0, 12)]],
 [
  BLOCK_H6, [(12, 0, 25.5)]],
 [
  BLOCK_H6, [(54, 0, 25.5)]],
 [
  BLOCK_H24, [(72, 0, 5.25)]],
 [
  BLOCK_H12, [(78, 0, 18.75)]],
 [
  BLOCK_H24, [(96, 0, 12)]],
 [
  BLOCK_H24, [(120, 0, 18.75)]],
 [
  BLOCK_H6, [(110, 0, 25.5)]],
 [
  BLOCK_H6, [(148, 0, 25.5)]]]
TreasureList11 = [[(4, 0, 34)],
 [
  (26, 0, 34)],
 [
  (46, 0, 34)],
 [
  (68, 0, 34)],
 [
  (74, 0, 7.25)],
 [
  (94, 0, 7.25)],
 [
  (102, 0, 34)],
 [
  (124, 0, 34)],
 [
  (140, 0, 34)],
 [
  (162, 0, 34)]]
EnemyList11 = [['cc', [(26, 0, 12.75), (46, 0, 12.75), 3.5]], ['tm', [(74, 0, 6), (94, 0, 6), 3.5]], ['sc', [(122, 0, 19.5), (142, 0, 19.5), 3.5]]]
SpawnPointList11 = [[(2, 0, 16)], [(70, 0, 16)]]
BlockList12 = [[BLOCK_H24, [(0, 0, 12)]],
 [
  BLOCK_H24, [(9, 0, 5.25)]],
 [
  BLOCK_H24, [(33, 0, 5.25)]],
 [
  BLOCK_H24, [(32, 0, 12)]],
 [
  BLOCK_H24, [(56, 0, 12)]],
 [
  BLOCK_H24, [(80, 0, 12)]],
 [
  BLOCK_H12, [(60, 0, 18.75)]],
 [
  BLOCK_H24, [(88, 0, 25.5)]],
 [
  BLOCK_V12B, [(103.2, 0, 24.72)]]]
TreasureList12 = [[(12, 0, 7.25)],
 [
  (55, 0, 7.25)],
 [
  (52, 0, 7.25)],
 [
  (36, 0, 34)],
 [
  (64, 0, 34)],
 [
  (68, 0, 34)],
 [
  (100, 0, 14)],
 [
  (95, 0, 22)],
 [
  (90, 0, 14)]]
SpawnPointList12 = [[(2, 0, 16)]]
StomperList12 = [[1, (13, 0, 20.75), 2], [1, (50, 0, 20.75), 2], [1, (82, 0, 20.75), 1.5]]
BlockList13 = [[BLOCK_H24, [(0, 0, 12)]],
 [
  BLOCK_H24, [(24, 0, 12)]],
 [
  BLOCK_H12, [(48, 0, 12)]],
 [
  BLOCK_H24, [(22, 0, 25.5)]],
 [
  BLOCK_H24, [(64, 0, 18.75)]],
 [
  BLOCK_H24, [(96, 0, 18.75)]],
 [
  BLOCK_H24, [(126, 0, 12)]],
 [
  BLOCK_H24, [(150, 0, 12)]],
 [
  BLOCK_H24, [(174, 0, 12)]],
 [
  BLOCK_H24, [(148, 0, 25.5)]],
 [
  BLOCK_H6, [(190, 0, 18.75)]]]
TreasureList13 = [[(2, 0, 34)],
 [
  (66, 0, 34)],
 [
  (91, 0, 29)],
 [
  (12, 0, 23)],
 [
  (20, 0, 23)],
 [
  (48, 0, 23)],
 [
  (56, 0, 23)],
 [
  (72, 0, 29.75)],
 [
  (80, 0, 29.75)],
 [
  (104, 0, 29.75)],
 [
  (112, 0, 29.75)],
 [
  (138, 0, 23)],
 [
  (146, 0, 23)],
 [
  (174, 0, 23)],
 [
  (182, 0, 23)],
 [
  (128, 0, 34)],
 [
  (192, 0, 34)]]
SpawnPointList13 = [[(2, 0, 16)], [(67, 0, 22.75)], [(130, 0, 16)]]
EnemyList13 = [['cc', [(20, 0, 12.75), (48, 0, 12.75), 3.5]],
 [
  'cc', [(48, 0, 12.75), (20, 0, 12.75), 3.5]],
 [
  'sc', [(92, 0, 31), (92, 0, -1), 3.5]],
 [
  'sc', [(92, 0, -1), (92, 0, 31), 3.5]],
 [
  'cc', [(146, 0, 12.75), (174, 0, 12.75), 3.5]],
 [
  'cc', [(174, 0, 12.75), (146, 0, 12.75), 3.5]]]
StomperList13 = [[1, (16, 0, 20.75), 2],
 [
  1, (52, 0, 20.75), 2],
 [
  1, (76, 0, 27.5), 2],
 [
  1, (108, 0, 27.5), 2],
 [
  1, (142, 0, 20.75), 2],
 [
  1, (178, 0, 20.75), 2]]
BlockList4 = [[BLOCK_H12, [(0, 0, 12)]],
 [
  BLOCK_H24, [(0, 0, 0)]],
 [
  BLOCK_H24, [(0, 0, 0)]],
 [
  BLOCK_H24, [(0, 0, 0)]],
 [
  BLOCK_H24, [(0, 0, 0)]],
 [
  BLOCK_H24, [(0, 0, 0)]],
 [
  BLOCK_H12, [(0, 0, 0)]],
 [
  BLOCK_H12, [(0, 0, 0)]],
 [
  BLOCK_H12, [(0, 0, 0)]],
 [
  BLOCK_H12, [(0, 0, 0)]],
 [
  BLOCK_H12, [(0, 0, 0)]],
 [
  BLOCK_H12, [(0, 0, 0)]],
 [
  BLOCK_H12, [(0, 0, 0)]],
 [
  BLOCK_H6, [(0, 0, 0)]],
 [
  BLOCK_H6, [(0, 0, 0)]],
 [
  BLOCK_H6, [(0, 0, 0)]],
 [
  BLOCK_H6, [(0, 0, 0)]],
 [
  BLOCK_H6, [(0, 0, 0)]],
 [
  BLOCK_H6, [(0, 0, 0)]],
 [
  BLOCK_H6, [(0, 0, 0)]],
 [
  BLOCK_H6, [(0, 0, 0)]],
 [
  BLOCK_H6, [(0, 0, 0)]],
 [
  BLOCK_H3, [(0, 0, 0)]],
 [
  BLOCK_H3, [(0, 0, 0)]],
 [
  BLOCK_H3, [(0, 0, 0)]],
 [
  BLOCK_H3, [(0, 0, 0)]],
 [
  BLOCK_H3, [(0, 0, 0)]],
 [
  BLOCK_V12F, [(0, 0, 0)]],
 [
  BLOCK_V12F, [(0, 0, 0)]],
 [
  BLOCK_V12B, [(0, 0, 0)]],
 [
  BLOCK_V12B, [(0, 0, 0)]],
 [
  BLOCK_V6F, [(0, 0, 0)]],
 [
  BLOCK_V6F, [(0, 0, 0)]],
 [
  BLOCK_V6B, [(0, 0, 0)]],
 [
  BLOCK_V6B, [(0, 0, 0)]]]
TreasureList4 = [[(-3, 0, 25)],
 [
  (-3, 0, 25)],
 [
  (-3, 0, 25)],
 [
  (-3, 0, 25)],
 [
  (-3, 0, 25)]]
SpawnPointList4 = [[(9, 0, 16)]]
EnemyList4 = [['cc', [(26, 0, 12.75), (46, 0, 12.75), 3.5]], ['tm', [(74, 0, 6), (94, 0, 6), 3.5]], ['sc', [(122, 0, 19.5), (142, 0, 19.5), 3.5]]]
StomperList4 = [[1, (12, 0, 20.75), 2], [1, (50, 0, 20.75), 2], [1, (82, 0, 20.75), 2]]
SectionTypes = {'end': (0,
         24,
         BlockListEnd,
         None,
         None,
         SpawnPointListEnd,
         None, [], [],
         [
          1, 1], []), 
   1: (
     4,
     100,
     BlockList1,
     EnemyList1,
     TreasureList1,
     SpawnPointList1,
     None,
     [
      3, 6],
     [
      10, 10],
     [
      1, 2], []), 
   2: (
     4,
     118,
     BlockList2,
     EnemyList2,
     TreasureList2,
     SpawnPointList2,
     None,
     [
      3, 6],
     [
      13, 13],
     [
      1, 2], []), 
   3: (
     4,
     192,
     BlockList3,
     None,
     TreasureList3,
     SpawnPointList3,
     None, [],
     [
      16, 16],
     [
      1, 4], []), 
   5: (
     0,
     72,
     BlockList5,
     None,
     TreasureList5,
     SpawnPointList5,
     None, [],
     [
      6, 6],
     [
      1, 1], []), 
   6: (
     0,
     90,
     BlockList6,
     None,
     TreasureList6,
     SpawnPointList6,
     None, [],
     [
      9, 9],
     [
      1, 1], []), 
   7: (
     1,
     124,
     BlockList7,
     None,
     TreasureList7,
     SpawnPointList7,
     None, [],
     [
      12, 12],
     [
      1, 1], []), 
   8: (
     5,
     174,
     BlockList8,
     None,
     TreasureList8,
     SpawnPointList8,
     None, [],
     [
      19, 19],
     [
      1, 3], []), 
   9: (
     3,
     204,
     BlockList9,
     None,
     TreasureList9,
     SpawnPointList9,
     None, [],
     [
      14, 14],
     [
      1, 2], []), 
   10: (
      4,
      214,
      BlockList10,
      None,
      TreasureList10,
      SpawnPointList10,
      None, [],
      [
       15, 15],
      [
       1, 3], []), 
   11: (
      2,
      164,
      BlockList11,
      EnemyList11,
      TreasureList11,
      SpawnPointList11,
      None,
      [
       3, 3],
      [
       10, 10],
      [
       1, 2], []), 
   12: (
      3,
      120,
      BlockList12,
      None,
      TreasureList12,
      SpawnPointList12,
      StomperList12, [],
      [
       10, 10],
      [
       1, 1],
      [
       3, 3]), 
   13: (
      3,
      198,
      BlockList13,
      EnemyList13,
      TreasureList13,
      SpawnPointList13,
      StomperList13,
      [
       3, 6],
      [
       17, 17],
      [
       1, 3],
      [
       3, 6]), 
   4: (
     0,
     1000,
     BlockList4,
     None,
     TreasureList4,
     SpawnPointList4,
     None,
     [
      25, 25],
     [
      10, 10],
     [
      10, 10],
     [
      10, 10]), 
   0: (
     0,
     75,
     BlockList0,
     None,
     TreasureList0,
     SpawnPointList0,
     None,
     [
      2, 5],
     [
      5, 10],
     [
      2, 5], [])}
SectionsPool = [
 1, 
 2, 
 3, 
 5, 
 6, 
 7, 
 8, 
 9, 
 10, 
 11, 
 12, 
 13]