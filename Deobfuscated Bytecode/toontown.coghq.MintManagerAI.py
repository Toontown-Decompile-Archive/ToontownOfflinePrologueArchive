# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.MintManagerAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
import DistributedMintAI
from toontown.toonbase import ToontownGlobals
from toontown.coghq import MintLayout
from direct.showbase import DirectObject
import random

class MintManagerAI(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('MintManagerAI')
    mintId = None

    def __init__(self, air):
        DirectObject.DirectObject.__init__(self)
        self.air = air

    def getDoId(self):
        return 0

    def createMint(self, mintId, players):
        for avId in players:
            if bboard.has('mintId-%s' % avId):
                mintId = bboard.get('mintId-%s' % avId)
                break

        numFloors = ToontownGlobals.MintNumFloors[mintId]
        floor = random.randrange(numFloors)
        for avId in players:
            if bboard.has('mintFloor-%s' % avId):
                floor = bboard.get('mintFloor-%s' % avId)
                floor = max(0, floor)
                floor = min(floor, numFloors - 1)
                break

        for avId in players:
            if bboard.has('mintRoom-%s' % avId):
                roomId = bboard.get('mintRoom-%s' % avId)
                for i in xrange(numFloors):
                    layout = MintLayout.MintLayout(mintId, i)
                    if roomId in layout.getRoomIds():
                        floor = i
                else:
                    from toontown.coghq import MintRoomSpecs
                    roomName = MintRoomSpecs.CashbotMintRoomId2RoomName[roomId]
                    MintManagerAI.notify.warning('room %s (%s) not found in any floor of mint %s' % (roomId, roomName, mintId))

        mintZone = self.air.allocateZone()
        mint = DistributedMintAI.DistributedMintAI(self.air, mintId, mintZone, floor, players)
        mint.generateWithRequired(mintZone)
        return mintZone