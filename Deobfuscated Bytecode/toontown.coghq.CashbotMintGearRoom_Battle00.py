# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.CashbotMintGearRoom_Battle00
# Compiled at: 2014-04-30 09:53:54
from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr', 'name': 'LevelMgr', 'comment': '', 
          'parentEntId': 0, 
          'cogLevel': 0, 
          'farPlaneDistance': 1500, 
          'modelFilename': 'phase_10/models/cashbotHQ/ZONE07a', 
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
   10001: {'type': 'battleBlocker', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(-27.3600006104, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'cellId': 0, 
           'radius': 10.0}, 
   10002: {'type': 'model', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10003, 
           'pos': Point3(57.0218696594, 3.79224324226, 0.0), 
           'hpr': Vec3(111.037513733, 0.0, 0.0), 
           'scale': Vec3(1.72596073151, 1.72596073151, 1.72596073151), 
           'collisionsOnly': 0, 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/boiler_B1'}, 
   10004: {'type': 'model', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10003, 
           'pos': Point3(-7.67323350906, -61.4041023254, 0.207314386964), 
           'hpr': Vec3(169.695159912, 0.0, 0.0), 
           'scale': Vec3(1.9143627882, 1.9143627882, 1.9143627882), 
           'collisionsOnly': 0, 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/boiler_A2'}, 
   10005: {'type': 'model', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10003, 
           'pos': Point3(-25.9598789215, 44.8260116577, 9.73551368713), 
           'hpr': Vec3(94.0856170654, 0.0, 0.0), 
           'scale': Vec3(1.53790044785, 1.53790044785, 1.53790044785), 
           'collisionsOnly': 0, 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/crates_F1'}, 
   10000: {'type': 'nodepath', 'name': 'cogs', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(-52.7907714844, 0.0, 0.0), 
           'hpr': Point3(270.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0)}, 
   10003: {'type': 'nodepath', 'name': 'props', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities, 'scenarios': [
               Scenario0]}