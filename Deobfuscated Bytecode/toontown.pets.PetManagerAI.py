# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.pets.PetManagerAI
# Compiled at: 2014-04-30 09:53:54
from toontown.pets import PetTraits
from toontown.pets import PetUtil
from toontown.hood import ZoneUtil
from toontown.pets import PetNameGenerator
import random, time
from toontown.toon.DistributedToonAI import dna

class PetCreator:

    def __init__(self, air, avId, petSeed, nameIndex, gender, zoneId):
        name, dna, traitSeed = PetUtil.getPetInfoFromSeed(petSeed, zoneId)
        self.air = air
        self.avId = avId
        self.petSeed = petSeed
        self.traitSeed = traitSeed
        self.nameIndex = nameIndex
        self.dna = dna
        self.zoneId = ZoneUtil.getCanonicalSafeZoneId(zoneId)
        self.traits = PetTraits.PetTraits(traitSeed=traitSeed, safeZoneId=zoneId)
        self.gender = gender
        self.petId = None
        self.name = None
        return

    def _handleCreate(self, doId):
        self.petId = doId
        av = self.air.doId2do[self.avId]
        av.b_setPetId(self.petId)
        self.air.writeServerEvent('purchased-pet', avId=self.avId, petId=self.petId)

    def createPet(self):
        self.nameGen = PetNameGenerator.PetNameGenerator()
        self.name = self.nameGen.getName(self.nameIndex)
        self.air.dbInterface.createObject(self.air.dbId, self.air.dclassesByName['DistributedPetAI'], {'setOwnerId': [
                        self.avId], 
           'setPetName': [
                        self.name], 
           'setTraitSeed': [
                          self.traitSeed], 
           'setSafeZone': [
                         self.zoneId], 
           'setForgetfulness': [
                              0], 
           'setBoredomThreshold': [
                                 0], 
           'setRestlessnessThreshold': [
                                      0], 
           'setPlayfulnessThreshold': [
                                     0], 
           'setLonelinessThreshold': [
                                    0], 
           'setSadnessThreshold': [
                                 0], 
           'setFatigueThreshold': [
                                 0], 
           'setHungerThreshold': [
                                0], 
           'setExcitementThreshold': [
                                    0], 
           'setAngerThreshold': [
                               0], 
           'setSurpriseThreshold': [
                                  0], 
           'setAffectionThreshold': [
                                   0], 
           'setHead': [
                     self.dna[0]], 
           'setEars': [
                     self.dna[1]], 
           'setNose': [
                     self.dna[2]], 
           'setTail': [
                     self.dna[3]], 
           'setBodyTexture': [
                            self.dna[4]], 
           'setColor': [
                      self.dna[5]], 
           'setColorScale': [
                           self.dna[6]], 
           'setEyeColor': [
                         self.dna[7]], 
           'setGender': [
                       self.dna[8]], 
           'setLastSeenTimestamp': [
                                  0], 
           'setExcitement': [
                           0], 
           'setBoredom': [
                        0], 
           'setRestlessness': [
                             0], 
           'setPlayfulness': [
                            0], 
           'setLoneliness': [
                           0], 
           'setSadness': [
                        0], 
           'setAffection': [
                          0], 
           'setHunger': [
                       0], 
           'setAnger': [
                      0], 
           'setTrickAptitudes': [
                               [
                                0, 
                                0, 0, 0, 0, 
                                0, 0]]}, self._handleCreate)


class PetManagerAI:

    def __init__(self, air):
        self.air = air

    def getAvailablePets(self, numPets=5):
        return random.sample(xrange(256), numPets)

    def createNewPetFromSeed(self, avId, petSeeds, nameIndex, gender, safeZoneId):
        creator = PetCreator(self.air, avId, petSeeds, nameIndex, gender, safeZoneId)
        creator.createPet()

    def deleteToonsPet(self, avId):
        av = self.air.doId2do[avId]
        pet = av.getPetId()
        if pet:
            if pet in self.air.doId2do:
                self.air.doId2do[pet].requestDelete()
        av.b_setPetId(0)
        self.air.writeServerEvent('returned-pet', avId=avId, pet=pet)