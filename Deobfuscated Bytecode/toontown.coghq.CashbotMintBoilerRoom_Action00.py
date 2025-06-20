# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.CashbotMintBoilerRoom_Action00
# Compiled at: 2014-04-30 09:53:54
from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr', 'name': 'LevelMgr', 'comment': '', 
          'parentEntId': 0, 
          'cogLevel': 0, 
          'farPlaneDistance': 1500, 
          'modelFilename': 'phase_10/models/cashbotHQ/ZONE08a', 
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
   10055: {'type': 'attribModifier', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10001, 
           'attribName': 'modelPath', 
           'recursive': 1, 
           'typeName': 'model', 
           'value': ''}, 
   10045: {'type': 'gagBarrel', 'name': 'gag', 
           'comment': '', 
           'parentEntId': 10002, 
           'pos': Point3(1.36976861954, 0.773027420044, 0.0), 
           'hpr': Vec3(51.1066703796, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'gagLevel': 5, 
           'gagLevelMax': 0, 
           'gagTrack': 'random', 
           'rewardPerGrab': 5, 
           'rewardPerGrabMax': 0}, 
   10047: {'type': 'gagBarrel', 'name': 'gag', 
           'comment': '', 
           'parentEntId': 10002, 
           'pos': Point3(0.137291625142, 2.83575630188, 0.0), 
           'hpr': Vec3(-210.47303772, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'gagLevel': 5, 
           'gagLevelMax': 0, 
           'gagTrack': 'random', 
           'rewardPerGrab': 5, 
           'rewardPerGrabMax': 0}, 
   10054: {'type': 'gagBarrel', 'name': 'gag', 
           'comment': '', 
           'parentEntId': 10002, 
           'pos': Point3(-2.34864091873, 2.16795802116, 0.0), 
           'hpr': Vec3(-141.715744019, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'gagLevel': 5, 
           'gagLevelMax': 0, 
           'gagTrack': 'random', 
           'rewardPerGrab': 5, 
           'rewardPerGrabMax': 0}, 
   10020: {'type': 'gear', 'name': 'upper', 
           'comment': '', 
           'parentEntId': 10044, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Point3(1.0, 1.0, 1.60000002384), 
           'degreesPerSec': -5.0, 
           'gearScale': 24.3, 
           'modelType': 'mint', 
           'orientation': 'horizontal', 
           'phaseShift': 0}, 
   10004: {'type': 'healBarrel', 'name': 'heal', 
           'comment': '', 
           'parentEntId': 10002, 
           'pos': Point3(0.0, -0.748414576054, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'rewardPerGrab': 6, 
           'rewardPerGrabMax': 8}, 
   10005: {'type': 'healBarrel', 'name': 'heal', 
           'comment': '', 
           'parentEntId': 10002, 
           'pos': Point3(-2.20195555687, -0.384303599596, 0.0), 
           'hpr': Vec3(-64.4312591553, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'rewardPerGrab': 6, 
           'rewardPerGrabMax': 8}, 
   10037: {'type': 'healBarrel', 'name': 'atTheEnd', 
           'comment': '', 
           'parentEntId': 10028, 
           'pos': Point3(64.282081604, 42.8509597778, 0.0), 
           'hpr': Vec3(274.906707764, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'rewardPerGrab': 5, 
           'rewardPerGrabMax': 0}, 
   10010: {'type': 'mintShelf', 'name': 'shelf0', 
           'comment': '', 
           'parentEntId': 10023, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1, 
           'mintId': 12700}, 
   10021: {'type': 'mintShelf', 'name': 'copy of shelf0', 
           'comment': '', 
           'parentEntId': 10023, 
           'pos': Point3(-13.4654359818, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Point3(1.0, 1.0, 1.0), 
           'mintId': 12500}, 
   10022: {'type': 'mintShelf', 'name': 'copy of shelf0 (2)', 
           'comment': '', 
           'parentEntId': 10023, 
           'pos': Point3(-26.8826961517, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'mintId': 12500}, 
   10025: {'type': 'mintShelf', 'name': 'shelf0', 
           'comment': '', 
           'parentEntId': 10024, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1, 
           'mintId': 12500}, 
   10026: {'type': 'mintShelf', 'name': 'copy of shelf0', 
           'comment': '', 
           'parentEntId': 10024, 
           'pos': Point3(-13.4654359818, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'mintId': 12500}, 
   10027: {'type': 'mintShelf', 'name': 'copy of shelf0 (2)', 
           'comment': '', 
           'parentEntId': 10024, 
           'pos': Point3(-26.8826961517, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'mintId': 12500}, 
   10000: {'type': 'model', 'name': 'crate', 
           'comment': '', 
           'parentEntId': 10009, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10007: {'type': 'model', 'name': 'upper', 
           'comment': '', 
           'parentEntId': 10059, 
           'pos': Point3(0.0, 2.0, 5.5), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1, 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10008: {'type': 'model', 'name': 'crate', 
           'comment': '', 
           'parentEntId': 10009, 
           'pos': Point3(0.0, -5.79679441452, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10012: {'type': 'model', 'name': 'copy of crate', 
           'comment': '', 
           'parentEntId': 10011, 
           'pos': Point3(0.0, -5.79679441452, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10013: {'type': 'model', 'name': 'copy of crate (2)', 
           'comment': '', 
           'parentEntId': 10011, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10014: {'type': 'model', 'name': 'copy of crate (2)', 
           'comment': '', 
           'parentEntId': 10011, 
           'pos': Point3(-5.65285158157, -11.6494598389, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10015: {'type': 'model', 'name': 'copy of crate (2)', 
           'comment': '', 
           'parentEntId': 10011, 
           'pos': Point3(-5.80570077896, -5.79679441452, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10016: {'type': 'model', 'name': 'copy of crate (3)', 
           'comment': '', 
           'parentEntId': 10011, 
           'pos': Point3(-3.93829965591, -17.6477527618, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10018: {'type': 'model', 'name': 'copy of upper', 
           'comment': '', 
           'parentEntId': 10059, 
           'pos': Point3(0.0, -3.83362102509, 5.5), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10019: {'type': 'model', 'name': 'copy of upper (2)', 
           'comment': '', 
           'parentEntId': 10059, 
           'pos': Point3(0.0, -9.69304847717, 5.5), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10030: {'type': 'model', 'name': 'lastCrateStack', 
           'comment': '', 
           'parentEntId': 10029, 
           'pos': Point3(47.9848709106, 27.71052742, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10031: {'type': 'model', 'name': 'upper', 
           'comment': '', 
           'parentEntId': 10030, 
           'pos': Point3(0.0, 0.0, 5.5), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1, 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10033: {'type': 'model', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10032, 
           'pos': Point3(-41.8699073792, -36.9582328796, 0.0), 
           'hpr': Point3(180.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/pipes_D1'}, 
   10034: {'type': 'model', 'name': 'crateStack', 
           'comment': '', 
           'parentEntId': 10029, 
           'pos': Point3(47.9848709106, -3.09666919708, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10035: {'type': 'model', 'name': 'upper', 
           'comment': '', 
           'parentEntId': 10034, 
           'pos': Point3(0.0, 0.0, 5.5), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1, 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10036: {'type': 'model', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10032, 
           'pos': Point3(0.0, -41.4516029358, 30.2685108185), 
           'hpr': Vec3(180.0, 0.0, 180.0), 
           'scale': Vec3(0.850346446037, 0.850346446037, 0.850346446037), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/pipes_C'}, 
   10041: {'type': 'model', 'name': 'crateStack', 
           'comment': '', 
           'parentEntId': 10040, 
           'pos': Point3(36.5904769897, -31.6758518219, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10042: {'type': 'model', 'name': 'upper', 
           'comment': '', 
           'parentEntId': 10041, 
           'pos': Point3(0.0, 0.0, 5.5), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1, 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10043: {'type': 'model', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10032, 
           'pos': Point3(19.5017147064, 84.0786056519, 10.0058736801), 
           'hpr': Vec3(171.253845215, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/boiler_B1'}, 
   10048: {'type': 'model', 'name': 'crate', 
           'comment': '', 
           'parentEntId': 10046, 
           'pos': Point3(0.0, 0.0, 8.25758934021), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Point3(1.29999995232, 1.29999995232, 1.64999997616), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10050: {'type': 'model', 'name': 'support', 
           'comment': '', 
           'parentEntId': 10046, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1, 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/gears_C2'}, 
   10052: {'type': 'model', 'name': 'crate', 
           'comment': '', 
           'parentEntId': 10051, 
           'pos': Point3(0.0, 0.0, 8.25758934021), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Point3(1.29999995232, 1.29999995232, 1.64999997616), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10053: {'type': 'model', 'name': 'support', 
           'comment': '', 
           'parentEntId': 10051, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1, 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/gears_C2'}, 
   10056: {'type': 'model', 'name': 'collision', 
           'comment': '', 
           'parentEntId': 10002, 
           'pos': Point3(-0.62570387125, 0.824797034264, 0.0), 
           'hpr': Vec3(318.366455078, 0.0, 0.0), 
           'scale': Vec3(0.644617915154, 0.639999985695, 1.28725671768), 
           'collisionsOnly': 1, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/CBMetalCrate'}, 
   10057: {'type': 'model', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10044, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(11.0614013672, 11.0614013672, 11.0614013672), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/RoundShadow'}, 
   10058: {'type': 'model', 'name': 'shelf', 
           'comment': '', 
           'parentEntId': 10028, 
           'pos': Point3(62.9968643188, 21.712474823, 0.0), 
           'hpr': Vec3(270.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/shelf_A1'}, 
   10062: {'type': 'model', 'name': 'copy of upper', 
           'comment': '', 
           'parentEntId': 10061, 
           'pos': Point3(0.0, -3.83362102509, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10063: {'type': 'model', 'name': 'copy of upper (2)', 
           'comment': '', 
           'parentEntId': 10061, 
           'pos': Point3(0.0, -9.69304847717, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10064: {'type': 'model', 'name': 'upper', 
           'comment': '', 
           'parentEntId': 10061, 
           'pos': Point3(0.0, 2.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1, 
           'collisionsOnly': 0, 
           'flattenType': 'light', 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2'}, 
   10001: {'type': 'nodepath', 'name': 'crates', 
           'comment': '', 
           'parentEntId': 10028, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.29999995232, 1.29999995232, 1.64892423153)}, 
   10002: {'type': 'nodepath', 'name': 'rewardBarrels', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(-0.719733536243, 56.9690589905, 10.0021047592), 
           'hpr': Vec3(61.6992454529, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0)}, 
   10003: {'type': 'nodepath', 'name': 'upperWall', 
           'comment': 'TODO: replace with lines of shelves', 
           'parentEntId': 0, 
           'pos': Point3(-20.3202514648, 52.6549415588, 9.9087305069), 
           'hpr': Vec3(270.0, 0.0, 0.0), 
           'scale': Vec3(1.11429846287, 1.11429846287, 1.11429846287)}, 
   10009: {'type': 'nodepath', 'name': 'toGear0', 
           'comment': '', 
           'parentEntId': 10001, 
           'pos': Point3(-26.5593318939, 31.8559513092, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0)}, 
   10011: {'type': 'nodepath', 'name': 'toGear1', 
           'comment': '', 
           'parentEntId': 10001, 
           'pos': Point3(-25.88397789, 13.6748971939, 0.0), 
           'hpr': Vec3(41.6335411072, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0)}, 
   10023: {'type': 'nodepath', 'name': 'leftWall', 
           'comment': '', 
           'parentEntId': 10003, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1}, 
   10024: {'type': 'nodepath', 'name': 'rightWall', 
           'comment': '', 
           'parentEntId': 10003, 
           'pos': Point3(-26.7111759186, 6.85981559753, 0.0), 
           'hpr': Point3(180.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0)}, 
   10028: {'type': 'nodepath', 'name': 'lowerPuzzle', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(0.0, 0.0, 0.0500000007451), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1}, 
   10029: {'type': 'nodepath', 'name': 'entranceWall', 
           'comment': '', 
           'parentEntId': 10001, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1}, 
   10032: {'type': 'nodepath', 'name': 'props', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1}, 
   10038: {'type': 'nodepath', 'name': 'archStompers', 
           'comment': '', 
           'parentEntId': 10028, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1}, 
   10040: {'type': 'nodepath', 'name': 'backWall', 
           'comment': '', 
           'parentEntId': 10001, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1}, 
   10044: {'type': 'nodepath', 'name': 'gear', 
           'comment': '', 
           'parentEntId': 10028, 
           'pos': Point3(11.8500003815, -11.3800001144, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1}, 
   10046: {'type': 'nodepath', 'name': 'supportedCrateBackWall', 
           'comment': '', 
           'parentEntId': 10028, 
           'pos': Point3(34.904460907, -34.058883667, -1.51686680317), 
           'hpr': Vec3(63.4349479675, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0)}, 
   10051: {'type': 'nodepath', 'name': 'supportedCrateEntrance', 
           'comment': '', 
           'parentEntId': 10028, 
           'pos': Point3(50.5076904298, 7.75915336609, 0.35789707303), 
           'hpr': Point3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0)}, 
   10059: {'type': 'nodepath', 'name': 'largeStack', 
           'comment': '', 
           'parentEntId': 10029, 
           'pos': Point3(47.9799995422, -16.9799995422, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1}, 
   10061: {'type': 'nodepath', 'name': 'lower', 
           'comment': '', 
           'parentEntId': 10059, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1}, 
   10049: {'type': 'stomper', 'name': 'second', 
           'comment': '', 
           'parentEntId': 10038, 
           'pos': Point3(62.3684997559, -19.4456634521, 18.1217155457), 
           'hpr': Point3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'animateShadow': 1, 
           'crushCellId': None, 
           'damage': 8, 
           'headScale': Point3(3.79999995232, 4.30000019073, 3.79999995232), 
           'modelPath': 0, 
           'motion': 3, 
           'period': 3.0, 
           'phaseShift': 0.34, 
           'range': 7.0, 
           'removeCamBarrierCollisions': 0, 
           'removeHeadFloor': 1, 
           'shaftScale': Point3(1.71000003815, 2.78999996185, 1.71000003815), 
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