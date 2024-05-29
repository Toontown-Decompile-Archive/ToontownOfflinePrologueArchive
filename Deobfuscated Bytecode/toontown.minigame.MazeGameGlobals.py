# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.MazeGameGlobals
# Compiled at: 2014-04-30 09:53:54
from direct.showbase import RandomNumGen

def getMazeName(gameDoId, numPlayers, mazeNames):
    try:
        return forcedMaze
    except:
        names = mazeNames[numPlayers - 1]
        return names[RandomNumGen.randHash(gameDoId) % len(names)]


ENDLESS_GAME = config.GetBool('endless-maze-game', 0)
GAME_DURATION = 60.0
SHOWSCORES_DURATION = 2.0
SUIT_TIC_FREQ = int(256)
WALK_SAME_DIRECTION_PROB = 4
WALK_TURN_AROUND_PROB = 30
SUIT_START_POSITIONS = ((0.25, 0.25),
 (0.75, 0.75),
 (0.25, 0.75),
 (0.75, 0.25),
 (0.2, 0.5),
 (0.8, 0.5),
 (0.5, 0.2),
 (0.5, 0.8),
 (0.33, 0.0),
 (0.66, 0.0),
 (0.33, 1.0),
 (0.66, 1.0),
 (0.0, 0.33),
 (0.0, 0.66),
 (1.0, 0.33),
 (1.0, 0.66))