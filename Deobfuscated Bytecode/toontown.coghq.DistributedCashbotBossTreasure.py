# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.DistributedCashbotBossTreasure
# Compiled at: 2014-04-30 09:53:54
from toontown.safezone import DistributedTreasure
from toontown.toonbase import ToontownGlobals
from direct.interval.IntervalGlobal import *
from pandac.PandaModules import Point3
Models = {ToontownGlobals.ToontownCentral: 'phase_4/models/props/icecream', ToontownGlobals.DonaldsDock: 'phase_6/models/props/starfish_treasure', ToontownGlobals.TheBrrrgh: 'phase_8/models/props/snowflake_treasure', 
   ToontownGlobals.MinniesMelodyland: 'phase_6/models/props/music_treasure', 
   ToontownGlobals.DaisyGardens: 'phase_8/models/props/flower_treasure', 
   ToontownGlobals.DonaldsDreamland: 'phase_8/models/props/zzz_treasure'}

class DistributedCashbotBossTreasure(DistributedTreasure.DistributedTreasure):
    pass