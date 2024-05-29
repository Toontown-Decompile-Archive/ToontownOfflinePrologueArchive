# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.suit.SellbotBossGlobals
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
try:
    from toontown.coghq.DistributedHealBarrelAI import DistributedHealBarrelAI
    from toontown.coghq.DistributedGagBarrelAI import DistributedGagBarrelAI
except ImportError:
    DistributedHealBarrelAI = None
    DistributedGagBarrelAI = None

PieToonup = 1
PieToonupNerfed = 2
PieDamageMult = 1.0
PieDamageMultNerfed = 2.0
AttackMult = 1.0
AttackMultNerfed = 0.5
HitCountDamage = 35
HitCountDamageNerfed = 50
BarrelDefs = {8000: {'type': DistributedHealBarrelAI, 'pos': Point3(15, 23, 0), 
          'hpr': Vec3(-45, 0, 0), 
          'rewardPerGrab': 50, 
          'rewardPerGrabMax': 0}, 
   8001: {'type': DistributedGagBarrelAI, 'pos': Point3(15, -23, 0), 
          'hpr': Vec3(-135, 0, 0), 
          'gagLevel': 3, 
          'gagLevelMax': 0, 
          'gagTrack': 3, 
          'rewardPerGrab': 10, 
          'rewardPerGrabMax': 0}, 
   8002: {'type': DistributedGagBarrelAI, 'pos': Point3(21, 20, 0), 
          'hpr': Vec3(-45, 0, 0), 
          'gagLevel': 3, 
          'gagLevelMax': 0, 
          'gagTrack': 4, 
          'rewardPerGrab': 10, 
          'rewardPerGrabMax': 0}, 
   8003: {'type': DistributedGagBarrelAI, 'pos': Point3(21, -20, 0), 
          'hpr': Vec3(-135, 0, 0), 
          'gagLevel': 3, 
          'gagLevelMax': 0, 
          'gagTrack': 5, 
          'rewardPerGrab': 10, 
          'rewardPerGrabMax': 0}}

def setBarrelAttr(barrel, entId):
    for defAttr, defValue in BarrelDefs[entId].iteritems():
        setattr(barrel, defAttr, defValue)


BarrelsStartPos = (0, -36, -8)
BarrelsFinalPos = (0, -36, 0)