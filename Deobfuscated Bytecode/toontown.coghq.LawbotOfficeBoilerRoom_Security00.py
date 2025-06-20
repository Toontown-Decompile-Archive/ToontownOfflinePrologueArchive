# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.LawbotOfficeBoilerRoom_Security00
# Compiled at: 2014-04-30 09:53:54
from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr', 'name': 'LevelMgr', 'comment': '', 
          'parentEntId': 0, 
          'cogLevel': 0, 
          'farPlaneDistance': 1500, 
          'modelFilename': 'phase_11/models/lawbotHQ/LB_Zone08a', 
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
   100014: {'type': 'gagBarrel', 'name': '<unnamed>', 
            'comment': '', 
            'parentEntId': 0, 
            'pos': Point3(-25.1777, 5.83836, 0.03), 
            'hpr': Vec3(92.8624, 0, 0), 
            'scale': Vec3(1, 1, 1), 
            'gagLevel': 5, 
            'gagLevelMax': 5, 
            'gagTrack': 'random', 
            'rewardPerGrab': 3, 
            'rewardPerGrabMax': 0}, 
   100035: {'type': 'gagBarrel', 'name': 'copy of <unnamed>', 
            'comment': '', 
            'parentEntId': 0, 
            'pos': Point3(16.7354, -42.9601, 0.03), 
            'hpr': Vec3(151.049, 0, 0), 
            'scale': Vec3(1, 1, 1), 
            'gagLevel': 5, 
            'gagLevelMax': 5, 
            'gagTrack': 'random', 
            'rewardPerGrab': 3, 
            'rewardPerGrabMax': 0}, 
   100013: {'type': 'healBarrel', 'name': '<unnamed>', 
            'comment': '', 
            'parentEntId': 100012, 
            'pos': Point3(0, 0, 0.591849), 
            'hpr': Vec3(147.995, 0, 0), 
            'scale': Vec3(1, 1, 1), 
            'rewardPerGrab': 15, 
            'rewardPerGrabMax': 0}, 
   100016: {'type': 'model', 'name': '<unnamed>', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(1.77609, -41.5342, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1.5, 1.5, 1.5), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_deskA'}, 
   100018: {'type': 'model', 'name': 'copy of <unnamed>', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(27.5451, -41.4709, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1.5, 1.5, 1.5), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_deskA'}, 
   100019: {'type': 'model', 'name': 'copy of <unnamed> (2)', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(36.4846, -38.3301, 0), 
            'hpr': Vec3(270.526, 0, 0), 
            'scale': Vec3(1.5, 1.5, 1.5), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_deskA'}, 
   100020: {'type': 'model', 'name': 'copy of <unnamed> (3)', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(10.7887, -37.8558, 0), 
            'hpr': Vec3(270.526, 0, 0), 
            'scale': Vec3(1.5, 1.5, 1.5), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_deskA'}, 
   100022: {'type': 'model', 'name': 'copy of <unnamed>', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(32.4792, -42.2737, 4.71821), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1.6, 1.6, 1.6), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_torch_lampA'}, 
   100023: {'type': 'model', 'name': 'copy of <unnamed> (2)', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(5.52344, -42.2737, 4.71821), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1.6, 1.6, 1.6), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_torch_lampA'}, 
   100024: {'type': 'model', 'name': 'copy of <unnamed> (2)', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(-39.2286, -39.5741, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1, 1, 1), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBoxX2'}, 
   100025: {'type': 'model', 'name': 'copy of <unnamed> (2)', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(-62.8751, -40.0794, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(8, 8, 8), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_pottedplantA'}, 
   100026: {'type': 'model', 'name': 'copy of <unnamed> (3)', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(-39.2286, -33.027, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1, 1, 1), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox'}, 
   100027: {'type': 'model', 'name': 'copy of <unnamed> (4)', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(-31.2652, -39.7321, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1, 1, 1), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox'}, 
   100028: {'type': 'model', 'name': 'copy of <unnamed> (5)', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(-22.0578, -39.3922, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1, 1, 1), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox'}, 
   100029: {'type': 'model', 'name': 'copy of <unnamed>', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(1.77609, -21.8266, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1.5, 1.5, 1.5), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_deskA'}, 
   100030: {'type': 'model', 'name': 'copy of <unnamed> (4)', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(10.7887, -18.0704, 0), 
            'hpr': Vec3(270.526, 0, 0), 
            'scale': Vec3(1.5, 1.5, 1.5), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_deskA'}, 
   100031: {'type': 'model', 'name': 'copy of <unnamed> (3)', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(36.6874, -16.1212, 0), 
            'hpr': Vec3(270.526, 0, 0), 
            'scale': Vec3(1.5, 1.5, 1.5), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_deskA'}, 
   100032: {'type': 'model', 'name': 'copy of <unnamed> (2)', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(27.5451, -20.5329, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1.5, 1.5, 1.5), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_deskA'}, 
   100033: {'type': 'model', 'name': 'copy of <unnamed> (3)', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(5.52344, -22.4424, 4.71821), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1.6, 1.6, 1.6), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_torch_lampA'}, 
   100034: {'type': 'model', 'name': 'copy of <unnamed> (4)', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(32.445, -22.0763, 4.71821), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1.6, 1.6, 1.6), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_torch_lampA'}, 
   100036: {'type': 'model', 'name': 'copy of <unnamed> (5)', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(15.0906, 40.376, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1, 1, 1), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox'}, 
   100037: {'type': 'model', 'name': 'copy of <unnamed> (6)', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(23.8805, 40.376, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1, 1, 1), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox'}, 
   100038: {'type': 'model', 'name': 'copy of <unnamed> (7)', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(31.7416, 40.376, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1, 1, 1), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox'}, 
   100039: {'type': 'model', 'name': 'copy of <unnamed> (8)', 
            'comment': '', 
            'parentEntId': 100015, 
            'pos': Point3(31.7416, 33.2113, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1, 1, 1), 
            'collisionsOnly': 0, 
            'flattenType': 'light', 
            'loadType': 'loadModel', 
            'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBoxX2'}, 
   100003: {'type': 'nodepath', 'name': 'light target 2', 
            'comment': '', 
            'parentEntId': 0, 
            'pos': Point3(-46.465, -27.1019, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1, 1, 1)}, 
   100004: {'type': 'nodepath', 'name': 'light target1', 
            'comment': '', 
            'parentEntId': 0, 
            'pos': Point3(45.4612, -33.6397, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1, 1, 1)}, 
   100006: {'type': 'nodepath', 'name': 'copy of light target 2', 
            'comment': '', 
            'parentEntId': 0, 
            'pos': Point3(-46.465, 31.2292, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1, 1, 1)}, 
   100007: {'type': 'nodepath', 'name': 'copy of light target1', 
            'comment': '', 
            'parentEntId': 0, 
            'pos': Point3(22.3708, 14.195, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1, 1, 1)}, 
   100008: {'type': 'nodepath', 'name': 'stompergroup', 
            'comment': '', 
            'parentEntId': 0, 
            'pos': Point3(-45.2964, 0, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1, 1, 1)}, 
   100015: {'type': 'nodepath', 'name': 'props', 
            'comment': '', 
            'parentEntId': 0, 
            'pos': Point3(0, 0, 0.05), 
            'hpr': Vec3(0, 0, 0), 
            'scale': 1}, 
   100011: {'type': 'platform', 'name': '<unnamed>', 
            'comment': '', 
            'parentEntId': 100008, 
            'pos': Point3(-8.92462, 5.26364, 19.9994), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1, 1, 1), 
            'floorName': 'platformcollision', 
            'modelPath': 'phase_9/models/cogHQ/platform1', 
            'modelScale': Vec3(1, 1, 1), 
            'motion': 'noBlend', 
            'offset': Point3(-10, 0, 0), 
            'period': 8.0, 
            'phaseShift': 0.0, 
            'waitPercent': 0.1}, 
   100012: {'type': 'platform', 'name': '<unnamed>', 
            'comment': '', 
            'parentEntId': 100008, 
            'pos': Point3(-18.1468, -5.11, 20), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1, 1, 1), 
            'floorName': 'platformcollision', 
            'modelPath': 'phase_9/models/cogHQ/platform1', 
            'modelScale': Vec3(1, 1, 1), 
            'motion': 'noBlend', 
            'offset': Point3(0, 0, 0), 
            'period': 2, 
            'phaseShift': 0.0, 
            'waitPercent': 0.1}, 
   100002: {'type': 'securityCamera', 'name': '<unnamed>', 
            'comment': '', 
            'parentEntId': 0, 
            'pos': Point3(-5.84843, -50.8043, 0.1), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1, 1, 1), 
            'accel': 5.0, 
            'damPow': 10, 
            'hideModel': 0, 
            'maxVel': 15.0, 
            'modelPath': 0, 
            'projector': Point3(6, 6, 25), 
            'radius': 10.0, 
            'switchId': 0, 
            'trackTarget1': 100004, 
            'trackTarget2': 100003, 
            'trackTarget3': 0}, 
   100005: {'type': 'securityCamera', 'name': 'copy of <unnamed>', 
            'comment': '', 
            'parentEntId': 0, 
            'pos': Point3(-5.38565, 34.1311, 0.1), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1, 1, 1), 
            'accel': 5.0, 
            'damPow': 8, 
            'hideModel': 0, 
            'maxVel': 15.0, 
            'modelPath': 0, 
            'projector': Point3(6, 6, 25), 
            'radius': 10.0, 
            'switchId': 0, 
            'trackTarget1': 100006, 
            'trackTarget2': 100007, 
            'trackTarget3': 0}, 
   100000: {'type': 'stomper', 'name': '<unnamed>', 
            'comment': '', 
            'parentEntId': 100008, 
            'pos': Point3(5, 5, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': 1, 
            'animateShadow': 1, 
            'cogStyle': 1, 
            'crushCellId': None, 
            'damage': 10, 
            'headScale': Point3(8, 4, 8), 
            'modelPath': 0, 
            'motion': 4, 
            'period': 2.0, 
            'phaseShift': 0.0, 
            'range': 18.0, 
            'removeCamBarrierCollisions': 0, 
            'removeHeadFloor': 0, 
            'shaftScale': Point3(0.5, 10, 0.5), 
            'soundLen': 0, 
            'soundOn': 1, 
            'soundPath': 0, 
            'style': 'vertical', 
            'switchId': 0, 
            'wantShadow': 1, 
            'wantSmoke': 1, 
            'zOffset': 0}, 
   100001: {'type': 'stomper', 'name': 'copy of <unnamed>', 
            'comment': '', 
            'parentEntId': 100008, 
            'pos': Point3(34.0608, 5, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1, 1, 1), 
            'animateShadow': 1, 
            'cogStyle': 1, 
            'crushCellId': None, 
            'damage': 10, 
            'headScale': Point3(8, 4, 8), 
            'modelPath': 0, 
            'motion': 4, 
            'period': 2.0, 
            'phaseShift': 0.75, 
            'range': 12.0, 
            'removeCamBarrierCollisions': 0, 
            'removeHeadFloor': 0, 
            'shaftScale': Point3(0.5, 10, 0.5), 
            'soundLen': 0, 
            'soundOn': 1, 
            'soundPath': 0, 
            'style': 'vertical', 
            'switchId': 0, 
            'wantShadow': 1, 
            'wantSmoke': 1, 
            'zOffset': 0}, 
   100009: {'type': 'stomper', 'name': 'copy of <unnamed>', 
            'comment': '', 
            'parentEntId': 100008, 
            'pos': Point3(19.6858, 21.6045, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1, 1, 1), 
            'animateShadow': 1, 
            'cogStyle': 1, 
            'crushCellId': None, 
            'damage': 10, 
            'headScale': Point3(8, 4, 8), 
            'modelPath': 0, 
            'motion': 4, 
            'period': 2.0, 
            'phaseShift': 0.5, 
            'range': 12.0, 
            'removeCamBarrierCollisions': 0, 
            'removeHeadFloor': 0, 
            'shaftScale': Point3(0.5, 10, 0.5), 
            'soundLen': 0, 
            'soundOn': 1, 
            'soundPath': 0, 
            'style': 'vertical', 
            'switchId': 0, 
            'wantShadow': 1, 
            'wantSmoke': 1, 
            'zOffset': 0}, 
   100010: {'type': 'stomper', 'name': 'copy of <unnamed> (2)', 
            'comment': '', 
            'parentEntId': 100008, 
            'pos': Point3(19.6858, -11.5601, 0), 
            'hpr': Vec3(0, 0, 0), 
            'scale': Vec3(1, 1, 1), 
            'animateShadow': 1, 
            'cogStyle': 1, 
            'crushCellId': None, 
            'damage': 10, 
            'headScale': Point3(8, 4, 8), 
            'modelPath': 0, 
            'motion': 4, 
            'period': 2.0, 
            'phaseShift': 0.25, 
            'range': 12.0, 
            'removeCamBarrierCollisions': 0, 
            'removeHeadFloor': 0, 
            'shaftScale': Point3(0.5, 10, 0.5), 
            'soundLen': 0, 
            'soundOn': 1, 
            'soundPath': 0, 
            'style': 'vertical', 
            'switchId': 0, 
            'wantShadow': 1, 
            'wantSmoke': 1, 
            'zOffset': 0}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities, 'scenarios': [
               Scenario0]}