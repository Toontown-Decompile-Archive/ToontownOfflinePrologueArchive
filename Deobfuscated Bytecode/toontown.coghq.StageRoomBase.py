# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.StageRoomBase
# Compiled at: 2014-04-30 09:53:54
from toontown.toonbase import ToontownGlobals

class StageRoomBase:

    def __init__(self):
        pass

    def setStageId(self, stageId):
        self.stageId = stageId
        self.cogTrack = ToontownGlobals.cogHQZoneId2dept(stageId)

    def setRoomId(self, roomId):
        self.roomId = roomId

    def getCogTrack(self):
        return self.cogTrack

    if __dev__:

        def getEntityTypeReg(self):
            import FactoryEntityTypes
            from otp.level import EntityTypeRegistry
            typeReg = EntityTypeRegistry.EntityTypeRegistry(FactoryEntityTypes)
            return typeReg