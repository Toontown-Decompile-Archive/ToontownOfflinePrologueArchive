# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.ai.FishManagerAI
# Compiled at: 2014-04-30 09:53:54
from toontown.fishing import FishGlobals
from toontown.fishing.FishBase import FishBase
import random
from otp.ai.MagicWordGlobal import *
from toontown.toonbase import TTLocalizer

class FishManagerAI:

    def __init__(self):
        self.ponds = {}
        self.requestedFish = {}

    def creditFishTank(self, av):
        totalFish = len(av.fishCollection)
        trophies = int(totalFish / 10)
        curTrophies = len(av.fishingTrophies)
        av.addMoney(av.fishTank.getTotalValue())
        av.b_setFishTank([], [], [])
        if trophies > curTrophies:
            av.b_setMaxHp(av.getMaxHp() + trophies - curTrophies)
            av.toonUp(av.getMaxHp())
            av.b_setFishingTrophies(range(trophies))
            return True
        return False

    def generateCatch(self, av, zoneId):
        if len(av.fishTank) >= av.getMaxFishTank():
            return [FishGlobals.OverTankLimit, 0, 0, 0]
        else:
            caughtItem = simbase.air.questManager.toonFished(av, zoneId)
            if caughtItem:
                return [FishGlobals.QuestItem, caughtItem, 0, 0]
            rand = random.random() * 100.0
            for cutoff in FishGlobals.SortedProbabilityCutoffs:
                if rand <= cutoff:
                    itemType = FishGlobals.ProbabilityDict[cutoff]
                    break

            if av.doId in self.requestedFish:
                genus, species = self.requestedFish[av.doId]
                weight = FishGlobals.getRandomWeight(genus, species)
                fish = FishBase(genus, species, weight)
                fishType = av.fishCollection.collectFish(fish)
                if fishType == FishGlobals.COLLECT_NEW_ENTRY:
                    itemType = FishGlobals.FishItemNewEntry
                elif fishType == FishGlobals.COLLECT_NEW_RECORD:
                    itemType = FishGlobals.FishItemNewRecord
                else:
                    itemType = FishGlobals.FishItem
                netlist = av.fishCollection.getNetLists()
                av.d_setFishCollection(netlist[0], netlist[1], netlist[2])
                av.fishTank.addFish(fish)
                netlist = av.fishTank.getNetLists()
                av.d_setFishTank(netlist[0], netlist[1], netlist[2])
                del self.requestedFish[av.doId]
                return [
                 itemType, genus, species, weight]
            if itemType == FishGlobals.FishItem:
                success, genus, species, weight = FishGlobals.getRandomFishVitals(zoneId, av.getFishingRod())
                fish = FishBase(genus, species, weight)
                fishType = av.fishCollection.collectFish(fish)
                if fishType == FishGlobals.COLLECT_NEW_ENTRY:
                    itemType = FishGlobals.FishItemNewEntry
                elif fishType == FishGlobals.COLLECT_NEW_RECORD:
                    itemType = FishGlobals.FishItemNewRecord
                else:
                    itemType = FishGlobals.FishItem
                netlist = av.fishCollection.getNetLists()
                av.d_setFishCollection(netlist[0], netlist[1], netlist[2])
                av.fishTank.addFish(fish)
                netlist = av.fishTank.getNetLists()
                av.d_setFishTank(netlist[0], netlist[1], netlist[2])
                return [
                 itemType, genus, species, weight]
            if itemType == FishGlobals.BootItem:
                return [itemType, 0, 0, 0]
            money = FishGlobals.Rod2JellybeanDict[av.getFishingRod()]
            av.addMoney(money)
            return [itemType, money, 0, 0]


@magicWord(category=CATEGORY_OVERRIDE, types=[str])
def gibfish(fishName):
    for fishGenus in TTLocalizer.FishSpeciesNames:
        fishGenusSpeciesList = TTLocalizer.FishSpeciesNames[fishGenus]
        for speciesName in fishGenusSpeciesList:
            if fishName.lower() == speciesName.lower():
                simbase.air.fishManager.requestedFish[spellbook.getTarget().doId] = (
                 fishGenus, fishGenusSpeciesList.index(speciesName))
                return 'Request for the fish %s was saved for the avatar %s' % (speciesName, spellbook.getTarget().getName())

    return "Couldn't find the fish with the name %s!" % fishName


@magicWord(category=CATEGORY_OVERRIDE)
def nogibfish():
    if spellbook.getTarget().doId in simbase.air.fishManager.requestedFish:
        del simbase.air.fishManager.requestedFish[spellbook.getTarget().doId]
        return "Deleted %s's request for any fishes." % spellbook.getTarget().getName()
    return '%s has not requested any fish!' % spellbook.getTarget().getName()