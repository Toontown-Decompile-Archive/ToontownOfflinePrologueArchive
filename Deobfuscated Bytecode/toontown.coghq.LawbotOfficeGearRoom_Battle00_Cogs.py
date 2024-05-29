# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.LawbotOfficeGearRoom_Battle00_Cogs
# Compiled at: 2014-04-30 09:53:54
from SpecImports import *
from toontown.toonbase import ToontownGlobals
CogParent = 10000
BattlePlace1 = 10000
BattleCellId = 0
BattleCells = {BattleCellId: {'parentEntId': BattlePlace1, 'pos': Point3(0, 0, 0)}}
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
    'skeleton': 1}]
ReserveCogData = []