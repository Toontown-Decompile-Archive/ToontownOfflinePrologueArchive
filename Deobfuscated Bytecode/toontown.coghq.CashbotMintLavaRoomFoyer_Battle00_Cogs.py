# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.CashbotMintLavaRoomFoyer_Battle00_Cogs
# Compiled at: 2014-04-30 09:53:54
from SpecImports import *
from toontown.toonbase import ToontownGlobals
CogParent = 10000
BattleParent = 10005
BattleCellId = 0
BattleCells = {BattleCellId: {'parentEntId': BattleParent, 'pos': Point3(0, 0, 0)}}
CogData = [
 {'parentEntId': CogParent, 'boss': 0, 
    'level': ToontownGlobals.CashbotMintSkelecogLevel, 
    'battleCell': BattleCellId, 
    'pos': Point3(-6, 0, 0), 
    'h': 180, 
    'behavior': 'stand', 
    'path': None, 
    'skeleton': 1},
 {'parentEntId': CogParent, 'boss': 0, 
    'level': ToontownGlobals.CashbotMintSkelecogLevel, 
    'battleCell': BattleCellId, 
    'pos': Point3(-2, 0, 0), 
    'h': 180, 
    'behavior': 'stand', 
    'path': None, 
    'skeleton': 1},
 {'parentEntId': CogParent, 'boss': 0, 
    'level': ToontownGlobals.CashbotMintSkelecogLevel, 
    'battleCell': BattleCellId, 
    'pos': Point3(2, 0, 0), 
    'h': 180, 
    'behavior': 'stand', 
    'path': None, 
    'skeleton': 1},
 {'parentEntId': CogParent, 'boss': 0, 
    'level': ToontownGlobals.CashbotMintSkelecogLevel, 
    'battleCell': BattleCellId, 
    'pos': Point3(6, 0, 0), 
    'h': 180, 
    'behavior': 'stand', 
    'path': None, 
    'skeleton': 1}]
ReserveCogData = []