# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.CashbotMintOilRoom_Battle00
# Compiled at: 2014-04-30 09:53:54
from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr', 'name': 'LevelMgr', 'comment': '', 
          'parentEntId': 0, 
          'cogLevel': 0, 
          'farPlaneDistance': 1500, 
          'modelFilename': 'phase_10/models/cashbotHQ/ZONE22a', 
          'wantDoors': 1}, 
   1001: {'type': 'editMgr', 'name': 'EditMgr', 
          'parentEntId': 0, 
          'insertEntity': None, 
          'removeEntity': None, 
          'requestNewEntity': None, 
          'requestSave': None}, 
   0: {'type': 'zone', 'name': 'UberZone', 
       'comment': '', 
       'parentEntId': 0, 
       'scale': 1, 
       'description': '', 
       'visibility': []}, 
   10001: {'type': 'model', 'name': 'vaultDoor', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(7.2503657341, -35.8064537048, 0.0), 
           'hpr': Point3(180.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/VaultDoorCover'}, 
   10000: {'type': 'nodepath', 'name': 'cogs', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(180.0, 0.0, 0.0), 
           'scale': 1}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities, 'scenarios': [
               Scenario0]}