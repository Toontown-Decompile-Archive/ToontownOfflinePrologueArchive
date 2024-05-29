# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.dna.DNASpawnerAI
# Compiled at: 2014-04-30 09:53:54
from DNAParser import DNAStorage
from toontown.racing.DistributedRacePadAI import DistributedRacePadAI
from toontown.racing.DistributedViewPadAI import DistributedViewPadAI
from toontown.racing.DistributedStartingBlockAI import DistributedStartingBlockAI, DistributedViewingBlockAI
from toontown.racing import RaceGlobals
from toontown.safezone import DistributedPicnicBasketAI, DistributedPicnicTableAI, DistributedGolfKartAI
from toontown.fishing.DistributedFishingPondAI import DistributedFishingPondAI
from toontown.fishing.DistributedFishingTargetAI import DistributedFishingTargetAI
from toontown.fishing.DistributedPondBingoManagerAI import DistributedPondBingoManagerAI
from toontown.fishing import FishingTargetGlobals
from toontown.safezone.DistributedFishingSpotAI import DistributedFishingSpotAI
from toontown.toon import NPCToons
from toontown.safezone.DistributedPartyGateAI import DistributedPartyGateAI
from toontown.toonbase import ToontownGlobals
from DNAParser import *

class DNASpawnerAI:

    def spawnObjects(self, filename, baseZone):
        dnaStore = DNAStorage()
        dnaData = simbase.air.loadDNAFileAI(dnaStore, filename)
        self._createObjects(dnaData, baseZone)

    def _createObjects(self, group, zone):
        if group.getName()[:13] == 'fishing_pond_':
            pondZones = {1100: 1129, 
               1200: 1236, 
               1300: 1330, 
               2100: 2156, 
               2200: 2236, 
               2300: 2341, 
               3100: 3136, 
               3200: 3236, 
               3300: 3329, 
               4100: 4148, 
               4200: 4240, 
               4300: 4345, 
               5100: 5139, 
               5200: 5245, 
               5300: 5318, 
               9100: 9153, 
               9200: 9255}
            pondZone = pondZones.get(zone, zone)
            pondIndex = int(group.getName()[13:])
            pond = DistributedFishingPondAI(simbase.air)
            pond.setArea(zone)
            pond.generateWithRequired(pondZone)
            bingoManager = DistributedPondBingoManagerAI(simbase.air)
            bingoManager.setPondDoId(pond.getDoId())
            bingoManager.generateWithRequired(pondZone)
            bingoManager.createGame()
            pond.bingoMgr = bingoManager
            simbase.air.fishManager.ponds[zone] = pond
            for i in range(FishingTargetGlobals.getNumTargets(zone)):
                target = DistributedFishingTargetAI(simbase.air)
                target.setPondDoId(pond.getDoId())
                target.generateWithRequired(pondZone)

            for i in range(group.getNumChildren()):
                posSpot = group.at(i)
                if posSpot.getName()[:13] == 'fishing_spot_':
                    spot = DistributedFishingSpotAI(simbase.air)
                    spot.setPondDoId(pond.getDoId())
                    x, y, z = posSpot.getPos()
                    h, p, r = posSpot.getHpr()
                    spot.setPosHpr(x, y, z, h, p, r)
                    spot.generateWithRequired(pondZone)

            NPCToons.createNpcsInZone(simbase.air, pondZone)
        else:
            if group.getName()[:10] == 'racing_pad':
                index, dest = group.getName()[11:].split('_', 2)
                index = int(index)
                pad = DistributedRacePadAI(simbase.air)
                pad.setArea(zone)
                pad.nameType = dest
                pad.index = index
                nri = RaceGlobals.getNextRaceInfo(-1, dest, index)
                pad.setTrackInfo([nri[0], nri[1]])
                pad.generateWithRequired(zone)
                for i in range(group.getNumChildren()):
                    posSpot = group.at(i)
                    if posSpot.getName()[:14] == 'starting_block':
                        spotIndex = int(posSpot.getName()[15:])
                        x, y, z = posSpot.getPos()
                        h, p, r = posSpot.getHpr()
                        startingBlock = DistributedStartingBlockAI(simbase.air)
                        startingBlock.setPosHpr(x, y, z, h, p, r)
                        startingBlock.setPadDoId(pad.getDoId())
                        startingBlock.setPadLocationId(index)
                        startingBlock.generateWithRequired(zone)
                        pad.addStartingBlock(startingBlock)

            elif group.getName()[:11] == 'viewing_pad':
                pad = DistributedViewPadAI(simbase.air)
                pad.setArea(zone)
                pad.generateWithRequired(zone)
                for i in range(group.getNumChildren()):
                    posSpot = group.at(i)
                    if posSpot.getName()[:14] == 'starting_block':
                        spotIndex = int(posSpot.getName()[15:])
                        x, y, z = posSpot.getPos()
                        h, p, r = posSpot.getHpr()
                        startingBlock = DistributedViewingBlockAI(simbase.air)
                        startingBlock.setPosHpr(x, y, z, h, p, r)
                        startingBlock.setPadDoId(pad.getDoId())
                        startingBlock.setPadLocationId(0)
                        startingBlock.generateWithRequired(zone)
                        pad.addStartingBlock(startingBlock)

            elif group.getName()[:13] == 'picnic_table_':
                pos = group.getPos()
                hpr = group.getHpr()
                nameInfo = group.getName().split('_')
                picnicTable = DistributedPicnicBasketAI.DistributedPicnicBasketAI(simbase.air, nameInfo[2], pos[0], pos[1], pos[2], hpr[0], hpr[1], hpr[2])
                picnicTable.generateWithRequired(zone)
                picnicTable.start()
            elif group.getName() == 'prop_game_table_DNARoot' and config.GetBool('want-picnic-games', True):
                pos = group.getPos()
                hpr = group.getHpr()
                nameInfo = group.getName().split('_')
                tableIndex = int(group.getParent().getName().split('_')[-1])
                picnicTable = DistributedPicnicTableAI.DistributedPicnicTableAI(simbase.air, zone, nameInfo[2], pos[0], pos[1], pos[2], hpr[0], hpr[1], hpr[2])
                picnicTable.setTableIndex(tableIndex)
                picnicTable.generateOtpObject(simbase.air.districtId, zone, ['setX', 'setY', 'setZ', 'setH', 'setP', 'setR'])
            elif group.getName()[:9] == 'golf_kart' and config.GetBool('want-golf-karts', True):
                info = group.getName()[10:].split('_')
                golfCourse = int(info[0])
                kartId = info[1]
                for i in range(group.getNumChildren()):
                    prop = group.at(i)
                    if prop.getName()[:15] == 'starting_block_':
                        pos, hpr = prop.getPos(), prop.getHpr()

                kart = DistributedGolfKartAI.DistributedGolfKartAI(simbase.air, golfCourse, pos[0], pos[1], pos[2], hpr[0], hpr[1], hpr[2])
                kart.generateWithRequired(zone)
                kart.sendUpdate('setGolfCourse', [golfCourse])
                kart.sendUpdate('setPosHpr', [pos[0], pos[1], pos[2], hpr[0], hpr[1], hpr[2]])
                color = kart.getColor()
                kart.sendUpdate('setColor', [color[0], color[1], color[2]])
                kart.start()
            if group.getName()[:15] == 'prop_party_gate' and config.GetBool('want-parties', True):
                gate = DistributedPartyGateAI(simbase.air)
                gate.setArea(zone)
                gate.generateWithRequired(zone)
            for i in range(group.getNumChildren()):
                child = group.at(i)
                self._createObjects(child, zone)