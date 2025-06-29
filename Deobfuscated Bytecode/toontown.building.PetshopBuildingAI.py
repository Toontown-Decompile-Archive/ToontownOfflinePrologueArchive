# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.building.PetshopBuildingAI
# Compiled at: 2014-04-30 09:53:54
import DistributedDoorAI, DistributedPetshopInteriorAI, DoorTypes
from pandac.PandaModules import *
from toontown.hood import ZoneUtil
from toontown.pets import DistributedPetAI, PetTraits, PetUtil
from toontown.toon import NPCToons
from toontown.toonbase import ToontownGlobals

class PetshopBuildingAI:

    def __init__(self, air, exteriorZone, interiorZone, blockNumber):
        self.air = air
        self.exteriorZone = exteriorZone
        self.interiorZone = interiorZone
        self.setup(blockNumber)

    def cleanup(self):
        for npc in self.npcs:
            npc.requestDelete()

        del self.npcs
        self.door.requestDelete()
        del self.door
        self.insideDoor.requestDelete()
        del self.insideDoor
        self.interior.requestDelete()
        del self.interior

    def setup(self, blockNumber):
        self.interior = DistributedPetshopInteriorAI.DistributedPetshopInteriorAI(blockNumber, self.air, self.interiorZone)
        self.interior.generateWithRequired(self.interiorZone)
        self.npcs = NPCToons.createNpcsInZone(self.air, self.interiorZone)
        door = DistributedDoorAI.DistributedDoorAI(self.air, blockNumber, DoorTypes.EXT_STANDARD)
        insideDoor = DistributedDoorAI.DistributedDoorAI(self.air, blockNumber, DoorTypes.INT_STANDARD)
        door.setOtherDoor(insideDoor)
        insideDoor.setOtherDoor(door)
        door.zoneId = self.exteriorZone
        insideDoor.zoneId = self.interiorZone
        door.generateWithRequired(self.exteriorZone)
        insideDoor.generateWithRequired(self.interiorZone)
        self.door = door
        self.insideDoor = insideDoor

    def createPet(self, ownerId, seed):
        zoneId = self.interiorZone
        safeZoneId = ZoneUtil.getCanonicalSafeZoneId(zoneId)
        name, dna, traitSeed = PetUtil.getPetInfoFromSeed(seed, safeZoneId)
        pet = DistributedPetAI.DistributedPetAI(self.air, dna=dna)
        pet.setOwnerId(ownerId)
        pet.setPetName(name)
        pet.traits = PetTraits.PetTraits(traitSeed=traitSeed, safeZoneId=safeZoneId)
        pet.generateWithRequired(zoneId)
        pet.setPos(0, 0, 0)
        pet.b_setParent(ToontownGlobals.SPRender)