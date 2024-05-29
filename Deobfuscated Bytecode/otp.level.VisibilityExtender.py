# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.level.VisibilityExtender
# Compiled at: 2014-04-30 09:53:54
import Entity

class VisibilityExtender(Entity.Entity):

    def __init__(self, level, entId):
        Entity.Entity.__init__(self, level, entId)
        self.initVisExt()

    def initVisExt(self):
        self.extended = 0
        self.zoneEntId = self.getZoneEntId()
        self.eventName = None
        if self.event is not None:
            self.eventName = self.getOutputEventName(self.event)
            self.accept(self.eventName, self.handleEvent)
        return

    def destroyVisExt(self):
        if self.eventName is not None:
            self.ignore(self.eventName)
        if self.extended:
            self.retract()
        return

    def handleEvent(self, doExtend):
        if doExtend:
            if not self.extended:
                self.extend()
        elif self.extended:
            self.retract()

    def extend(self):
        zoneEnt = self.level.getEntity(self.getZoneEntId())
        zoneEnt.incrementRefCounts(self.newZones)
        self.extended = 1
        self.level.handleVisChange()

    def retract(self):
        zoneEnt = self.level.getEntity(self.getZoneEntId())
        zoneEnt.decrementRefCounts(self.newZones)
        self.extended = 0
        self.level.handleVisChange()

    def destroy(self):
        self.destroyVisExt()
        Entity.Entity.destroy(self)

    if __dev__:

        def setNewZones(self, newZones):
            extended = self.extended
            self.destroyVisExt()
            self.newZones = newZones
            self.initVisExt()
            if extended:
                self.extend()

        def attribChanged(self, *args):
            extended = self.extended
            self.destroyVisExt()
            self.initVisExt()
            if extended:
                self.extend()