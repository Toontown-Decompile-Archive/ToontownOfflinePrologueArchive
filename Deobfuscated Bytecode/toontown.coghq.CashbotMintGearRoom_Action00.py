# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.CashbotMintGearRoom_Action00
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
   10007: {'type': 'attribModifier', 'name': 'goonStrength', 
           'comment': '', 
           'parentEntId': 0, 
           'attribName': 'strength', 
           'recursive': 1, 
           'typeName': 'goon', 
           'value': '10'}, 
   10002: {'type': 'goon', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10001, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1.5, 
           'attackRadius': 15, 
           'crushCellId': None, 
           'goonType': 'pg', 
           'gridId': None, 
           'hFov': 70, 
           'strength': 10, 
           'velocity': 4.0}, 
   10004: {'type': 'goon', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10003, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1.5, 
           'attackRadius': 15, 
           'crushCellId': None, 
           'goonType': 'pg', 
           'gridId': None, 
           'hFov': 70, 
           'strength': 10, 
           'velocity': 4}, 
   10006: {'type': 'goon', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10005, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1.5, 
           'attackRadius': 15, 
           'crushCellId': None, 
           'goonType': 'pg', 
           'gridId': None, 
           'hFov': 70, 
           'strength': 10, 
           'velocity': 4}, 
   10009: {'type': 'goon', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10008, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1.5, 
           'attackRadius': 15, 
           'crushCellId': None, 
           'goonType': 'pg', 
           'gridId': None, 
           'hFov': 70, 
           'strength': 10, 
           'velocity': 4}, 
   10011: {'type': 'healBarrel', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10012, 
           'pos': Point3(2.15899157524, 2.29615116119, 5.45938539505), 
           'hpr': Vec3(331.109100342, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'rewardPerGrab': 8, 
           'rewardPerGrabMax': 0}, 
   10012: {'type': 'model', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10010, 
           'pos': Point3(20.9361133575, 13.8672618866, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(0.920000016689, 0.920000016689, 0.920000016689), 
           'collisionsOnly': 0, 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/CBMetalCrate'}, 
   10013: {'type': 'model', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10000, 
           'pos': Point3(57.0218696594, 5.15023899078, 0.0), 
           'hpr': Vec3(270.0, 0.0, 0.0), 
           'scale': Vec3(0.660517215729, 0.660517215729, 0.660517215729), 
           'collisionsOnly': 0, 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/pipes_C'}, 
   10015: {'type': 'model', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10000, 
           'pos': Point3(-25.9598789215, 59.4411621094, 9.73551368713), 
           'hpr': Vec3(274.089996338, 0.0, 0.0), 
           'scale': Vec3(1.53790044785, 1.53790044785, 1.53790044785), 
           'collisionsOnly': 0, 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/crates_F1'}, 
   10016: {'type': 'model', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10000, 
           'pos': Point3(33.3394889832, -18.3643035889, 0.0), 
           'hpr': Vec3(180.0, 0.0, 0.0), 
           'scale': Vec3(0.660000026226, 0.660000026226, 0.660000026226), 
           'collisionsOnly': 0, 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/pipes_D1'}, 
   10017: {'type': 'model', 'name': 'copy of <unnamed>', 
           'comment': '', 
           'parentEntId': 10018, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Point3(169.699996948, 0.0, 0.0), 
           'scale': Vec3(0.902469694614, 0.902469694614, 0.902469694614), 
           'collisionsOnly': 0, 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/pipes_D4'}, 
   10020: {'type': 'model', 'name': 'copy of <unnamed> (2)', 
           'comment': '', 
           'parentEntId': 10018, 
           'pos': Point3(-12.071434021, 0.0, 0.0), 
           'hpr': Vec3(288.434936523, 0.0, 0.0), 
           'scale': Vec3(0.902469694614, 0.902469694614, 0.902469694614), 
           'collisionsOnly': 0, 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/pipes_D4'}, 
   10022: {'type': 'model', 'name': '<unnamed>', 
           'comment': '', 
           'parentEntId': 10021, 
           'pos': Point3(-5.97179174423, -60.3133621216, 0.0), 
           'hpr': Vec3(180.0, 0.0, 0.0), 
           'scale': Vec3(0.869391143322, 0.869391143322, 0.869391143322), 
           'collisionsOnly': 0, 
           'loadType': 'loadModel', 
           'modelPath': 'phase_10/models/cashbotHQ/pipes_C'}, 
   10000: {'type': 'nodepath', 'name': 'props', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1}, 
   10010: {'type': 'nodepath', 'name': 'healPuzzle', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(43.1796302795, 0.0, 0.0), 
           'hpr': Point3(-90.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0)}, 
   10018: {'type': 'nodepath', 'name': 'rightVertPipes', 
           'comment': '', 
           'parentEntId': 10021, 
           'pos': Point3(-16.4536571503, -45.3981781006, -8.39999961853), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Point3(0.649999976158, 0.649999976158, 1.55999994278)}, 
   10021: {'type': 'nodepath', 'name': 'rightPipes', 
           'comment': '', 
           'parentEntId': 10000, 
           'pos': Point3(0.0, 0.0, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': 1}, 
   10001: {'type': 'path', 'name': 'nearPace', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(-59.7391967773, 0.0, 0.0), 
           'hpr': Point3(90.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'pathIndex': 3, 
           'pathScale': 1.0}, 
   10003: {'type': 'path', 'name': 'bowtie', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(-40.0336875916, 0.0, 0.0), 
           'hpr': Point3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'pathIndex': 2, 
           'pathScale': 1.0}, 
   10005: {'type': 'path', 'name': 'bridgePace', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(-8.80618190765, -1.5122487545, 0.0), 
           'hpr': Vec3(0.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'pathIndex': 3, 
           'pathScale': 1.0}, 
   10008: {'type': 'path', 'name': 'farPace', 
           'comment': '', 
           'parentEntId': 0, 
           'pos': Point3(7.5265827179, 7.56240034103, 0.0), 
           'hpr': Vec3(90.0, 0.0, 0.0), 
           'scale': Vec3(1.0, 1.0, 1.0), 
           'pathIndex': 3, 
           'pathScale': 1.0}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities, 'scenarios': [
               Scenario0]}