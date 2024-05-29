# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.election.DistributedToonfestCogAI
# Compiled at: 2014-04-30 09:53:54
from direct.interval.IntervalGlobal import *
from direct.fsm.FSM import FSM
from otp.ai.MagicWordGlobal import *
from toontown.election.DistributedHotAirBalloonAI import DistributedHotAirBalloonAI
from DistributedElectionCameraManagerAI import DistributedElectionCameraManagerAI
from DistributedSafezoneInvasionAI import DistributedSafezoneInvasionAI
from DistributedInvasionSuitAI import DistributedInvasionSuitAI
from InvasionMasterAI import InvasionMasterAI
from toontown.toonbase import ToontownGlobals
import SafezoneInvasionGlobals, ElectionGlobals, random
from otp.distributed.OtpDoGlobals import *
from direct.task import Task
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from toontown.election import *

class DistributedToonfestCogAI(DistributedObjectAI, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedToonfestTowerAI')

    def __init__(self, air, operation='SpeedUp'):
        DistributedObjectAI.__init__(self, air)
        FSM.__init__(self, 'ToonfestCogFSM')
        self.air = air
        self.validOperations = ['SpeedUp', 'SlowDown', 'Reverse']
        if operation in self.validOperations:
            self.operation = operation
        else:
            print 'DistributedToonfestCogAI: Operation %s is not a valid operation.' % operation
            self.operation = 'SpeedUp'

    def enterOff(self):
        self.requestDelete()

    def setPos(self, x, y, z):
        self.sendUpdate('setPosThroughAI', [x, y, z])

    def setId(self, id):
        self.sendUpdate('setIdThroughAI', [id])

    def enterDown(self):
        pass

    def enterUp(self):
        pass

    def updateTower(self):
        if not isinstance(self.air.toonfestTower, DistributedToonfestTowerAI) or not self.air.toonfestTower:
            print 'DistributedToonfestCogAI: ERROR! Could not find the ToonFest Tower.'
        else:
            base = random.randrange(0, 3)
            self.air.toonfestTower.updateTower(self.operation, base)
            print 'DistributedToonfestCogAI: Told Tower to ' + self.operation + ' base number ' + str(base + 1)