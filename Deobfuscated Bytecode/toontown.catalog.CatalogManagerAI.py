# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.catalog.CatalogManagerAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from CatalogGenerator import CatalogGenerator
from toontown.toonbase import ToontownGlobals
import time

class CatalogManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('CatalogManagerAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.catalogGenerator = CatalogGenerator()

    def startCatalog(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if av:
            self.deliverCatalogFor(av)

    def deliverCatalogFor(self, av):
        monthlyCatalog = self.catalogGenerator.generateMonthlyCatalog(av, time.time() / 60)
        newWeek = (av.catalogScheduleCurrentWeek + 1) % ToontownGlobals.CatalogNumWeeks
        weeklyCatalog = self.catalogGenerator.generateWeeklyCatalog(av, newWeek, monthlyCatalog)
        backCatalog = self.catalogGenerator.generateBackCatalog(av, newWeek, av.catalogScheduleCurrentWeek, monthlyCatalog)
        av.b_setCatalog(monthlyCatalog, weeklyCatalog, backCatalog)
        av.b_setCatalogSchedule(newWeek, int((time.time() + 604800) / 60))
        av.b_setCatalogNotify(ToontownGlobals.NewItems, av.mailboxNotify)

    def isItemReleased(self, accessory):
        return 1