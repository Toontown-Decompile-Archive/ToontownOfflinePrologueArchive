# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.BossbotCountryClubEntrance_Action00
# Compiled at: 2014-04-30 09:53:54
from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr', 'name': 'LevelMgr', 'comment': '', 
          'parentEntId': 0, 
          'cogLevel': 0, 
          'farPlaneDistance': 1500, 
          'modelFilename': 'phase_12/models/bossbotHQ/BossbotEntranceRoom', 
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
   10000: {'type': 'entrancePoint', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(0, 6, 0), 
           'hpr': Vec3(0, 0, 0), 
           'scale': 1, 
           'entranceId': 0, 
           'radius': 15, 
           'theta': 20}, 
   10002: {'type': 'nodepath', 'name': 'props', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(0, 0, 0), 
           'hpr': Vec3(0, 0, 0), 
           'scale': 1}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities, 'scenarios': [
               Scenario0]}