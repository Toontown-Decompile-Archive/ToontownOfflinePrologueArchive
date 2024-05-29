# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.LawbotOfficeDiamondRoom_Trap00_Cogs
# Compiled at: 2014-04-30 09:53:54
from SpecImports import *
from toontown.toonbase import ToontownGlobals
CogParent = 100007
CogParent1 = 100009
BattlePlace1 = 100004
BattlePlace2 = 100005
BattleCellId = 0
BattleCellId1 = 1
BattleCells = {BattleCellId: {'parentEntId': BattlePlace1, 'pos': Point3(0, 0, 0)}, 
   BattleCellId1: {'parentEntId': BattlePlace2, 'pos': Point3(0, 0, 0)}}
CogData = [
 {'parentEntId': CogParent, 'boss': 0, 
    'level': ToontownGlobals.CashbotMintCogLevel, 
    'battleCell': BattleCellId, 
    'pos': Point3(-8, 4, 0), 
    'h': 180, 
    'behavior': 'stand', 
    'path': None, 
    'skeleton': 1},
 {'parentEntId': CogParent, 'boss': 0, 
    'level': ToontownGlobals.CashbotMintCogLevel + 1, 
    'battleCell': BattleCellId, 
    'pos': Point3(-3, 4, 0), 
    'h': 180, 
    'behavior': 'stand', 
    'path': None, 
    'skeleton': 1},
 {'parentEntId': CogParent, 'boss': 0, 
    'level': ToontownGlobals.CashbotMintCogLevel, 
    'battleCell': BattleCellId, 
    'pos': Point3(3, 4, 0), 
    'h': 180, 
    'behavior': 'stand', 
    'path': None, 
    'skeleton': 1},
 {'parentEntId': CogParent, 'boss': 0, 
    'level': ToontownGlobals.CashbotMintCogLevel + 1, 
    'battleCell': BattleCellId, 
    'pos': Point3(8, 4, 0), 
    'h': 180, 
    'behavior': 'stand', 
    'path': None, 
    'skeleton': 1},
 {'parentEntId': CogParent1, 'boss': 0, 
    'level': ToontownGlobals.CashbotMintCogLevel, 
    'battleCell': BattleCellId1, 
    'pos': Point3(-8, 4, 0), 
    'h': 180, 
    'behavior': 'stand', 
    'path': None, 
    'skeleton': 1},
 {'parentEntId': CogParent1, 'boss': 0, 
    'level': ToontownGlobals.CashbotMintCogLevel + 1, 
    'battleCell': BattleCellId1, 
    'pos': Point3(-3, 4, 0), 
    'h': 180, 
    'behavior': 'stand', 
    'path': None, 
    'skeleton': 1},
 {'parentEntId': CogParent1, 'boss': 0, 
    'level': ToontownGlobals.CashbotMintCogLevel, 
    'battleCell': BattleCellId1, 
    'pos': Point3(3, 4, 0), 
    'h': 180, 
    'behavior': 'stand', 
    'path': None, 
    'skeleton': 1},
 {'parentEntId': CogParent1, 'boss': 0, 
    'level': ToontownGlobals.CashbotMintCogLevel + 1, 
    'battleCell': BattleCellId1, 
    'pos': Point3(8, 4, 0), 
    'h': 180, 
    'behavior': 'stand', 
    'path': None, 
    'skeleton': 1}]
ReserveCogData = []