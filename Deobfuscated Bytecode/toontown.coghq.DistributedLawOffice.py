# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.DistributedLawOffice
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from toontown.toonbase.ToontownGlobals import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
import random
from otp.level import DistributedLevel
from direct.directnotify import DirectNotifyGlobal
import LawOfficeBase, FactoryEntityCreator, FactorySpecs
from otp.level import LevelSpec
from otp.level import LevelConstants
from toontown.toonbase import TTLocalizer
from toontown.coghq import FactoryCameraViews
from direct.distributed.DistributedObject import DistributedObject
if __dev__:
    from otp.level import EditorGlobals

class DistributedLawOffice(DistributedObject, LawOfficeBase.LawOfficeBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedLawOffice')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        LawOfficeBase.LawOfficeBase.__init__(self)
        self.suitIds = []
        self.suits = []
        self.reserveSuits = []
        self.joiningReserves = []
        self.suitsInitialized = 0
        self.goonClipPlanes = {}
        self.level = None
        return

    def generate(self):
        self.notify.debug('generate')
        self.accept('lawOfficeFloorDone', self.handleFloorDone)

    def delete(self):
        base.localAvatar.chatMgr.chatInputSpeedChat.removeFactoryMenu()
        self.ignore('lawOfficeFloorDone')

    def setLawOfficeId(self, id):
        LawOfficeBase.LawOfficeBase.setLawOfficeId(self, id)

    def levelAnnounceGenerate(self):
        self.notify.debug('levelAnnounceGenerate')

    def handleSOSPanel(self, panel):
        avIds = []
        for avId in self.avIdList:
            if base.cr.doId2do.get(avId):
                avIds.append(avId)

        panel.setFactoryToonIdList(avIds)

    def handleFloorDone(self):
        self.sendUpdate('readyForNextFloor')

    def disable(self):
        self.notify.debug('disable')
        base.localAvatar.setCameraCollisionsCanMove(0)

    def getTaskZoneId(self):
        return self.lawOfficeId

    def startSignal(self):
        base.camera.setScale(base.localAvatar.getScale())
        localAvatar.setCameraFov(DefaultCameraFov)
        base.camera.clearMat()