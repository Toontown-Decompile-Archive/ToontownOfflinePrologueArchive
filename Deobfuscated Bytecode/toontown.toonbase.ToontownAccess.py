# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.toonbase.ToontownAccess
# Compiled at: 2014-04-30 09:53:54
from direct.task import Task
from toontown.hood import ZoneUtil
from toontown.toonbase import ToontownGlobals

class ToontownAccess:

    def __init__(self):
        self.startupModules = []

    def initModuleInfo(self):
        self.startupModules = self.getModuleList()
        taskMgr.doMethodLater(300, self.checkModuleInfo, 'moduleListTask')

    def delete(self):
        taskMgr.remove('moduleListTask')
        del self.startupModules

    def checkModuleInfo(self, task):
        currentModuleList = self.getModuleList()
        newModules = []
        for module in currentModuleList:
            if module not in self.startupModules:
                self.startupModules.insert(0, module)
                newModules.insert(0, module)

        self.sendUpdate('setModuleInfo', [newModules])
        return task.again

    def getModuleList(self):
        return []

    def sendUpdate(self, fieldName, args=[], sendToId=None):
        if base.cr and hasattr(base, 'localAvatar'):
            dg = base.localAvatar.dclass.clientFormatUpdate(fieldName, sendToId or base.localAvatar.doId, args)
            base.cr.send(dg)

    def canAccess(self, zoneId=None):
        if base.cr.isPaid():
            return True
        allowed = False
        allowedZones = [ToontownGlobals.ToontownCentral,
         ToontownGlobals.MyEstate,
         ToontownGlobals.GoofySpeedway,
         ToontownGlobals.OldDaisyGardens,
         ToontownGlobals.ScroogeBank,
         ToontownGlobals.Tutorial]
        specialZones = [ToontownGlobals.SellbotLobby]
        if hasattr(base.cr, 'newsManager') and base.cr.newsManager:
            holidayIds = base.cr.newsManager.getHolidayIdList()
            if ToontownGlobals.SELLBOT_NERF_HOLIDAY in holidayIds:
                specialZones.append(ToontownGlobals.SellbotHQ)
        place = base.cr.playGame.getPlace()
        if zoneId:
            myHoodId = ZoneUtil.getCanonicalHoodId(zoneId)
        else:
            myHoodId = ZoneUtil.getCanonicalHoodId(place.zoneId)
        if hasattr(place, 'id'):
            myHoodId = place.id
        if myHoodId in allowedZones:
            allowed = True
        elif zoneId and zoneId in specialZones:
            allowed = True
        return allowed