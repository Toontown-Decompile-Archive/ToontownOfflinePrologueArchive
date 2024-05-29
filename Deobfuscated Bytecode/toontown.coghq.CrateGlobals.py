# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.CrateGlobals
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
CRATE_CLEAR = 0
CRATE_POWERUP = 1
CRATE_PUSH = 2
CrateNormals = [Vec3(1, 0, 0),
 Vec3(-1, 0, 0),
 Vec3(0, 1, 0),
 Vec3(0, -1, 0)]
CrateHprs = [Vec3(90, 0, 0),
 Vec3(270, 0, 0),
 Vec3(180, 0, 0),
 Vec3(0, 0, 0)]
T_PUSH = 1.5
T_PAUSE = 0.1
TorsoToOffset = {'ss': 0.17, 'ms': 0.18, 
   'ls': 0.75, 
   'sd': 0.17, 
   'md': 0.18, 
   'ld': 0.75, 
   's': 0.17, 
   'm': 0.18, 
   'l': 0.75}