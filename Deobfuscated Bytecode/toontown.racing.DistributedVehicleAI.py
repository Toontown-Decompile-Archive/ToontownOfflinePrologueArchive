# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.racing.DistributedVehicleAI
# Compiled at: 2014-04-30 09:53:54
from otp.ai.AIBase import *
from toontown.toonbase.ToontownGlobals import *
from toontown.racing.KartDNA import *
from direct.distributed.ClockDelta import *
from direct.distributed import DistributedSmoothNodeAI
from direct.fsm import FSM
from direct.task import Task
from direct.distributed.PyDatagram import *

class DistributedVehicleAI(DistributedSmoothNodeAI.DistributedSmoothNodeAI, FSM.FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedVehicleAI')

    def __init__(self, air, avId):
        self.ownerId = avId
        DistributedSmoothNodeAI.DistributedSmoothNodeAI.__init__(self, air)
        FSM.FSM.__init__(self, 'DistributedVehicleAI')
        self.driverId = 0
        self.kartDNA = [-1] * getNumFields()
        self.__initDNA()
        self.request('Off')

    def generate(self):
        DistributedSmoothNodeAI.DistributedSmoothNodeAI.generate(self)

    def delete(self):
        DistributedSmoothNodeAI.DistributedSmoothNodeAI.delete(self)

    def __initDNA(self):
        owner = self.air.doId2do.get(self.ownerId)
        if owner:
            self.kartDNA[KartDNA.bodyType] = owner.getKartBodyType()
            self.kartDNA[KartDNA.bodyColor] = owner.getKartBodyColor()
            self.kartDNA[KartDNA.accColor] = owner.getKartAccessoryColor()
            self.kartDNA[KartDNA.ebType] = owner.getKartEngineBlockType()
            self.kartDNA[KartDNA.spType] = owner.getKartSpoilerType()
            self.kartDNA[KartDNA.fwwType] = owner.getKartFrontWheelWellType()
            self.kartDNA[KartDNA.bwwType] = owner.getKartBackWheelWellType()
            self.kartDNA[KartDNA.rimsType] = owner.getKartRimType()
            self.kartDNA[KartDNA.decalType] = owner.getKartDecalType()
        else:
            self.notify.warning('__initDNA - OWNER %s OF KART NOT FOUND!' % self.ownerId)

    def d_setState(self, state, avId):
        self.sendUpdate('setState', [state, avId])

    def requestControl(self):
        avId = self.air.getAvatarIdFromSender()
        if self.driverId == 0:
            self.request('Controlled', avId)

    def requestParked(self):
        avId = self.air.getAvatarIdFromSender()
        if avId == self.driverId:
            self.request('Parked')

    def start(self):
        self.request('Parked')

    def enterOff(self):
        return

    def exitOff(self):
        return

    def enterParked(self):
        self.driverId = 0
        self.d_setState('P', 0)
        return

    def exitParked(self):
        return

    def enterControlled(self, avId):
        self.driverId = avId
        fieldList = ['setComponentL', 
         'setComponentX', 
         'setComponentY', 
         'setComponentZ', 
         'setComponentH', 
         'setComponentP', 
         'setComponentR', 
         'setComponentT', 
         'setSmStop', 
         'setSmH', 
         'setSmZ', 
         'setSmXY', 
         'setSmXZ', 
         'setSmPos', 
         'setSmHpr', 
         'setSmXYH', 
         'setSmXYZH', 
         'setSmPosHpr', 
         'setSmPosHprL', 
         'clearSmoothing', 
         'suggestResync', 
         'returnResync']
        self.air.setAllowClientSend(avId, self, fieldNameList=fieldList)
        self.d_setState('C', self.driverId)

    def exitControlled(self):
        pass

    def handleUnexpectedExit(self):
        self.notify.warning('toon: %d exited unexpectedly, resetting vehicle %d' % (self.driverId, self.doId))
        self.request('Parked')
        self.requestDelete()

    def getBodyType(self):
        return self.kartDNA[KartDNA.bodyType]

    def getBodyColor(self):
        return self.kartDNA[KartDNA.bodyColor]

    def getAccessoryColor(self):
        return self.kartDNA[KartDNA.accColor]

    def getEngineBlockType(self):
        return self.kartDNA[KartDNA.ebType]

    def getSpoilerType(self):
        return self.kartDNA[KartDNA.spType]

    def getFrontWheelWellType(self):
        return self.kartDNA[KartDNA.fwwType]

    def getBackWheelWellType(self):
        return self.kartDNA[KartDNA.bwwType]

    def getRimType(self):
        return self.kartDNA[KartDNA.rimsType]

    def getDecalType(self):
        return self.kartDNA[KartDNA.decalType]

    def getOwner(self):
        return self.ownerId