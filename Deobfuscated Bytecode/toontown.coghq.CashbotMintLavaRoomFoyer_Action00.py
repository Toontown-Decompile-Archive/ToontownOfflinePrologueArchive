# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.CashbotMintLavaRoomFoyer_Action00
# Compiled at: 2014-04-30 09:53:54
from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr', 'name': 'LevelMgr', 'comment': '', 
          'parentEntId': 0, 
          'cogLevel': 0, 
          'farPlaneDistance': 1500, 
          'modelFilename': 'phase_10/models/cashbotHQ/ZONE18a', 
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
   10009: {'type': 'attribModifier', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10008, 
           'attribName': 'modelPath', 
           'recursive': 1, 
           'typeName': 'model', 
           'value': ''}, 
   10017: {'type': 'attribModifier', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10008, 
           'attribName': 'scale', 
           'recursive': 1, 
           'typeName': 'model', 
           'value': 'Vec3(.955,1,1)'}, 
   10015: {'type': 'crate', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10014, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'scale': 0.92, 
           'crushCellId': None, 
           'gridId': 10014, 
           'modelType': 1, 
           'pushable': 1}, 
   10014: {'type': 'grid', 'name': 'crateGrid', 
           'comment': '', 
           'parentEntId': 10003, 
           'pos': Point3(-6.73230838776, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'cellSize': 3.0, 
           'numCol': 4, 
           'numRow': 2}, 
   10005: {'type': 'healBarrel', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(19.0611743927, -20.78266716, 0.0), 
           'hpr': Vec3(160.016891479, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'rewardPerGrab': 8, 
           'rewardPerGrabMax': 0}, 
   10001: {'type': 'model', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10000, 
           'pos': Point3(-7.89672088623, 21.0129165649, 0.0), 
           'hpr': Vec3(180.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/crates_F1'}, 
   10002: {'type': 'model', 'name': 'copy of <unnamed>', 
           'comment': '', 
           'parentEntId': 10000, 
           'pos': Point3(-17.8739471436, 16.2802295685, 0.0), 
           'hpr': Vec3(270.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/crates_E'}, 
   10006: {'type': 'model', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(20.9172992706, 20.2094459534, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/CBMetalCrate'}, 
   10007: {'type': 'model', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10000, 
           'pos': Point3(-18.3651504517, -19.2698841095, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/crates_C1'}, 
   10018: {'type': 'model', 'name': 'middle', 
           'comment': '', 
           'parentEntId': 10008, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(0.954999983311, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10019: {'type': 'model', 'name': 'copy of middle', 
           'comment': '', 
           'parentEntId': 10008, 
           'pos': Point3(-5.72357320786, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(0.954999983311, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10020: {'type': 'model', 'name': 'copy of middle', 
           'comment': '', 
           'parentEntId': 10008, 
           'pos': Point3(5.71999979019, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(0.954999983311, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10021: {'type': 'model', 'name': 'copy of middle', 
           'comment': '', 
           'parentEntId': 10008, 
           'pos': Point3(11.4399995804, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(0.954999983311, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10000: {'type': 'nodepath', 'name': 'props', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1}, 
   10003: {'type': 'nodepath', 'name': 'cratePuzzle', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Point3(0.0, 0.0, 0.0), 
           'scale': 1}, 
   10008: {'type': 'nodepath', 'name': 'wall', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(13.4399995804, 6.57999992371, 0.0), 
           'hpr': Point3(270.0, 0.0, 0.0), 
           'scale': Vec3(1.95812249184, 1.5, 1.79999995232)}, 
   10016: {'type': 'stomper', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10014, 
           'pos': Point3(-4.04936361313, 3.45528435707, 0.0), 
           'hpr': Point3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'crushCellId': None, 
           'damage': 6, 
           'headScale': Point3(4.0, 3.0, 4.0), 
           'modelPath': 0, 
           'motion': 3, 
           'period': 5.0, 
           'phaseShift': 0.0, 
           'range': 15.0, 
           'shaftScale': Point3(0.75, 10.0, 0.75), 
           'soundLen': 0, 
           'soundOn': 1, 
           'soundPath': 1, 
           'style': 'vertical', 
           'switchId': 0, 
           'wantShadow': 1, 
           'wantSmoke': 1, 
           'zOffset': 0}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities, 'scenarios': [
               Scenario0]}