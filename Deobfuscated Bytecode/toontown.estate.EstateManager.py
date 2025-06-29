# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.estate.EstateManager
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from toontown.toonbase import ToontownGlobals
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
import random
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from toontown.toonbase import TTLocalizer
import HouseGlobals, Estate

class EstateManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('EstateManager')
    neverDisable = 1

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.availableZones = 0
        self.popupInfo = None
        return

    def disable(self):
        self.notify.debug("i'm disabling EstateManager rightnow.")
        self.ignore('getLocalEstateZone')
        self.ignoreAll()
        if self.popupInfo:
            self.popupInfo.destroy()
            self.popupInfo = None
        DistributedObject.DistributedObject.disable(self)
        return

    def allocateMyEstateZone(self):
        self.getLocalEstateZone(base.localAvatar.getDoId())

    def getLocalEstateZone(self, avId):
        self.sendUpdate('getEstateZone', [avId])

    def setEstateZone(self, ownerId, zoneId):
        self.notify.debug('setEstateZone(%s, %s)' % (ownerId, zoneId))
        messenger.send('setLocalEstateZone', [ownerId, zoneId])

    def generate(self):
        self.notify.debug('BASE: generate')
        DistributedObject.DistributedObject.generate(self)
        base.cr.estateMgr = self
        self.accept('getLocalEstateZone', self.getLocalEstateZone)
        self.announceGenerateName = self.uniqueName('generate')

    def setAvHouseId(self, avId, houseIds):
        self.notify.debug('setAvHouseId %d' % base.localAvatar.doId)
        for av in base.cr.avList:
            if av.id == avId:
                houseId = houseIds[av.position]
                ownerAv = base.cr.doId2do.get(avId)
                if ownerAv:
                    ownerAv.b_setHouseId(houseId)
                return

    def sendAvToPlayground(self, avId, retCode):
        self.notify.debug('sendAvToPlayground: %d' % avId)
        messenger.send('kickToPlayground', [retCode])

    def leaveEstate(self):
        if self.isDisabled():
            self.notify.warning('EstateManager disabled; unable to leave estate.')
            return
        self.sendUpdate('exitEstate')

    def removeFriend(self, ownerId, avId):
        self.notify.debug('removeFriend ownerId = %s, avId = %s' % (ownerId, avId))
        self.sendUpdate('removeFriend', [ownerId, avId])

    def startAprilFools(self):
        if isinstance(base.cr.playGame.getPlace(), Estate.Estate):
            base.cr.playGame.getPlace().startAprilFoolsControls()

    def stopAprilFools(self):
        if isinstance(base.cr.playGame.getPlace(), Estate.Estate):
            base.cr.playGame.getPlace().stopAprilFoolsControls()