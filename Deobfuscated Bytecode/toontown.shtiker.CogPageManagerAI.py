# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.shtiker.CogPageManagerAI
# Compiled at: 2014-04-30 09:53:54
from toontown.suit import SuitDNA
from toontown.shtiker.CogPageGlobals import *

class CogPageManagerAI:

    def toonEncounteredCogs(self, toon, encounteredCogs, zoneId):
        cogs = toon.cogs
        for cog in encounteredCogs:
            if toon.getDoId() in cog['activeToons']:
                cogIndex = SuitDNA.suitHeadTypes.index(cog['type'])
                if cogs[cogIndex] == COG_UNSEEN:
                    cogs[cogIndex] = COG_BATTLED

        toon.b_setCogStatus(cogs)

    def toonKilledCogs(self, toon, killedCogs, zoneId):
        cogCounts = toon.cogCounts
        cogs = toon.cogs
        for cog in killedCogs:
            if cog['isSkelecog'] or cog['isVP'] or cog['isCFO']:
                continue
            if toon.getDoId() in cog['activeToons']:
                deptIndex = SuitDNA.suitDepts.index(cog['track'])
                if toon.buildingRadar[deptIndex - 1] == 1:
                    continue
                cogIndex = SuitDNA.suitHeadTypes.index(cog['type'])
                buildingQuota = COG_QUOTAS[1][cogIndex % SuitDNA.suitsPerDept]
                cogQuota = COG_QUOTAS[0][cogIndex % SuitDNA.suitsPerDept]
                if cogCounts[cogIndex] >= buildingQuota:
                    continue
                cogCounts[cogIndex] += 1
                if cogCounts[cogIndex] < cogQuota:
                    cogs[cogIndex] = COG_DEFEATED
                else:
                    if cogQuota <= cogCounts[cogIndex] < buildingQuota:
                        cogs[cogIndex] = COG_COMPLETE1
                    else:
                        cogs[cogIndex] = COG_COMPLETE2

        toon.b_setCogCount(cogCounts)
        toon.b_setCogStatus(cogs)
        newCogRadar = toon.cogRadar
        newBuildingRadar = toon.buildingRadar
        for dept in range(len(SuitDNA.suitDepts) - 1):
            if newBuildingRadar[dept] == 1:
                continue
            cogRadar = 1
            buildingRadar = 1
            for cog in range(SuitDNA.suitsPerDept):
                status = toon.cogs[dept * SuitDNA.suitsPerDept + cog]
                if status != COG_COMPLETE2:
                    buildingRadar = 0
                    if status != COG_COMPLETE1:
                        cogRadar = 0

            newCogRadar[dept] = cogRadar
            newBuildingRadar[dept] = buildingRadar

        toon.b_setCogRadar(newCogRadar)
        toon.b_setBuildingRadar(newBuildingRadar)