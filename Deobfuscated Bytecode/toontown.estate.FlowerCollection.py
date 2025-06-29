# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.estate.FlowerCollection
# Compiled at: 2014-04-30 09:53:54
import GardenGlobals
from direct.directnotify import DirectNotifyGlobal
import FlowerBase

class FlowerCollection:
    notify = DirectNotifyGlobal.directNotify.newCategory('FlowerCollection')

    def __init__(self):
        self.flowerlist = []

    def __len__(self):
        return len(self.flowerlist)

    def getFlower(self):
        return self.flowerlist

    def makeFromNetLists(self, speciesList, varietyList):
        self.flowerlist = []
        for species, variety in zip(speciesList, varietyList):
            self.flowerlist.append(FlowerBase.FlowerBase(species, variety))

    def getNetLists(self):
        speciesList = []
        varietyList = []
        for flower in self.flowerlist:
            speciesList.append(flower.getSpecies())
            varietyList.append(flower.getVariety())

        return [speciesList, varietyList]

    def hasFlower(self, species, variety):
        for flower in self.flowerlist:
            if flower.getSpecies() == species and flower.getVariety() == variety:
                return 1

        return 0

    def hasSpecies(self, species):
        for flower in self.flowerlist:
            if flower.getSpecies() == species:
                return 1

        return 0

    def getInitialVariety(self, species):
        retVal = 100000
        for flower in self.flowerlist:
            if flower.getSpecies() == species:
                if flower.getVariety() < retVal:
                    retVal = flower.getVariety()

        if retVal == 100000:
            retVal = 0
        return retVal

    def __collect(self, newFlower, updateCollection):
        for flower in self.flowerlist:
            if flower.getVariety() == newFlower.getVariety() and flower.getSpecies() == newFlower.getSpecies():
                return GardenGlobals.COLLECT_NO_UPDATE

        if updateCollection:
            self.flowerlist.append(newFlower)
        return GardenGlobals.COLLECT_NEW_ENTRY

    def collectFlower(self, newFlower):
        return self.__collect(newFlower, updateCollection=1)

    def __str__(self):
        numFlower = len(self.flowerlist)
        txt = 'Flower Collection (%s flowers):' % numFlower
        for flower in self.flowerlist:
            txt += '\n' + str(flower)

        return txt