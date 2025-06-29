# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.MinigameCreatorAI
# Compiled at: 2014-04-30 09:53:54
import copy, random, time
from toontown.toonbase import ToontownGlobals
import DistributedMinigameTemplateAI, DistributedRaceGameAI, DistributedCannonGameAI, DistributedTagGameAI, DistributedPatternGameAI, DistributedRingGameAI, DistributedMazeGameAI, DistributedTugOfWarGameAI, DistributedCatchGameAI, DistributedDivingGameAI, DistributedTargetGameAI, DistributedPairingGameAI, DistributedPhotoGameAI, DistributedVineGameAI, DistributedIceGameAI, DistributedCogThiefGameAI, DistributedTwoDGameAI, DistributedTravelGameAI, TravelGameGlobals
from otp.ai.MagicWordGlobal import *
ALLOW_TEMP_MINIGAMES = config.GetBool('allow-temp-minigames', False)
if ALLOW_TEMP_MINIGAMES:
    from toontown.minigame.TempMinigameAI import *
simbase.forcedMinigameId = config.GetInt('minigame-id', 0)
RequestMinigame = {}
MinigameZoneRefs = {}

def createMinigame(air, playerArray, trolleyZone, minigameZone=None, previousGameId=ToontownGlobals.NoPreviousGameId, newbieIds=[], startingVotes=None, metagameRound=-1, desiredNextGame=None):
    if minigameZone == None:
        minigameZone = air.allocateZone(owner='MinigameCreatorAI')
    acquireMinigameZone(minigameZone)
    mgId = None
    mgDiff = None
    mgSzId = None
    for avId in playerArray:
        request = RequestMinigame.get(avId)
        if request != None:
            mgId, mgKeep, mgDiff, mgSzId = request
            if not mgKeep:
                del RequestMinigame[avId]
            break

    if mgId != None:
        pass
    else:
        if simbase.forcedMinigameId:
            mgId = simbase.forcedMinigameId
        else:
            randomList = list(copy.copy(ToontownGlobals.MinigamePlayerMatrix[len(playerArray)]))
            if simbase.air.useAllMinigames and len(playerArray) > 1:
                randomList = list(copy.copy(ToontownGlobals.MinigameIDs))
                for gameId in [ToontownGlobals.TravelGameId]:
                    if gameId in randomList:
                        randomList.remove(gameId)

            for gameId in [ToontownGlobals.TravelGameId]:
                if gameId in randomList:
                    randomList.remove(gameId)

            if previousGameId != ToontownGlobals.NoPreviousGameId:
                if randomList.count(previousGameId) != 0 and len(randomList) > 1:
                    randomList.remove(previousGameId)
            randomList = removeUnreleasedMinigames(randomList, True)
            mgId = random.choice(randomList)
            if metagameRound > -1:
                if metagameRound % 2 == 0:
                    mgId = ToontownGlobals.TravelGameId
                elif desiredNextGame:
                    mgId = desiredNextGame
            mgCtors = {ToontownGlobals.RaceGameId: DistributedRaceGameAI.DistributedRaceGameAI, ToontownGlobals.CannonGameId: DistributedCannonGameAI.DistributedCannonGameAI, 
               ToontownGlobals.TagGameId: DistributedTagGameAI.DistributedTagGameAI, 
               ToontownGlobals.PatternGameId: DistributedPatternGameAI.DistributedPatternGameAI, 
               ToontownGlobals.RingGameId: DistributedRingGameAI.DistributedRingGameAI, 
               ToontownGlobals.MazeGameId: DistributedMazeGameAI.DistributedMazeGameAI, 
               ToontownGlobals.TugOfWarGameId: DistributedTugOfWarGameAI.DistributedTugOfWarGameAI, 
               ToontownGlobals.CatchGameId: DistributedCatchGameAI.DistributedCatchGameAI, 
               ToontownGlobals.DivingGameId: DistributedDivingGameAI.DistributedDivingGameAI, 
               ToontownGlobals.TargetGameId: DistributedTargetGameAI.DistributedTargetGameAI, 
               ToontownGlobals.MinigameTemplateId: DistributedMinigameTemplateAI.DistributedMinigameTemplateAI, 
               ToontownGlobals.PairingGameId: DistributedPairingGameAI.DistributedPairingGameAI, 
               ToontownGlobals.VineGameId: DistributedVineGameAI.DistributedVineGameAI, 
               ToontownGlobals.IceGameId: DistributedIceGameAI.DistributedIceGameAI, 
               ToontownGlobals.CogThiefGameId: DistributedCogThiefGameAI.DistributedCogThiefGameAI, 
               ToontownGlobals.TwoDGameId: DistributedTwoDGameAI.DistributedTwoDGameAI, 
               ToontownGlobals.TravelGameId: DistributedTravelGameAI.DistributedTravelGameAI, 
               ToontownGlobals.PhotoGameId: DistributedPhotoGameAI.DistributedPhotoGameAI}
            if ALLOW_TEMP_MINIGAMES:
                from TempMinigameAI import TempMgCtors
                for key, value in TempMgCtors.items():
                    mgCtors[key] = value

            try:
                mg = mgCtors[mgId](air, mgId)
            except KeyError:
                raise Exception, 'unknown minigame ID: %s' % mgId

            mg.setExpectedAvatars(playerArray)
            mg.setNewbieIds(newbieIds)
            mg.setTrolleyZone(trolleyZone)
            mg.setDifficultyOverrides(mgDiff, mgSzId)
            if startingVotes == None:
                for avId in playerArray:
                    mg.setStartingVote(avId, TravelGameGlobals.DefaultStartingVotes)

            else:
                for index in range(len(startingVotes)):
                    avId = playerArray[index]
                    votes = startingVotes[index]
                    if votes < 0:
                        print 'createMinigame negative votes, avId=%s votes=%s' % (avId, votes)
                        votes = 0
                    mg.setStartingVote(avId, votes)

        mg.setMetagameRound(metagameRound)
        mg.generateWithRequired(minigameZone)
        toons = []
        for id in playerArray:
            toon = simbase.air.doId2do.get(id)
            if toon != None:
                toons.append(toon)

    retVal = {}
    retVal['minigameZone'] = minigameZone
    retVal['minigameId'] = mgId
    return retVal


def acquireMinigameZone(zoneId):
    if zoneId not in MinigameZoneRefs:
        MinigameZoneRefs[zoneId] = 0
    MinigameZoneRefs[zoneId] += 1


def releaseMinigameZone(zoneId):
    MinigameZoneRefs[zoneId] -= 1
    if MinigameZoneRefs[zoneId] <= 0:
        del MinigameZoneRefs[zoneId]
        simbase.air.deallocateZone(zoneId)


def removeUnreleasedMinigames(startList, increaseChanceOfNewGames=0):
    randomList = startList[:]
    for gameId in ToontownGlobals.MinigameReleaseDates:
        dateTuple = ToontownGlobals.MinigameReleaseDates[gameId]
        currentTime = time.time()
        releaseTime = time.mktime((dateTuple[0],
         dateTuple[1],
         dateTuple[2],
         0,
         0,
         0,
         0,
         0,
         -1))
        releaseTimePlus1Week = releaseTime + 604800
        if currentTime < releaseTime:
            if gameId in randomList:
                doRemove = True
                if gameId == ToontownGlobals.CogThiefGameId and simbase.air.config.GetBool('force-allow-thief-game', 0):
                    doRemove = False
                    if increaseChanceOfNewGames:
                        randomList += [gameId] * 4
                elif gameId == ToontownGlobals.IceGameId and simbase.air.config.GetBool('force-allow-ice-game', 0):
                    doRemove = False
                    if increaseChanceOfNewGames:
                        randomList += [gameId] * 4
                elif gameId == ToontownGlobals.TwoDGameId and simbase.air.config.GetBool('force-allow-2d-game', 0):
                    doRemove = False
                    if increaseChanceOfNewGames:
                        randomList += [gameId] * 4
                elif gameId == ToontownGlobals.PhotoGameId and simbase.air.config.GetBool('force-allow-photo-game', 0):
                    doRemove = False
                    if increaseChanceOfNewGames:
                        randomList += [gameId] * 4
                if doRemove:
                    randomList.remove(gameId)
        if releaseTime < currentTime and currentTime < releaseTimePlus1Week and gameId in randomList and increaseChanceOfNewGames:
            randomList += [gameId] * 4

    return randomList


@magicWord(category=CATEGORY_OVERRIDE, types=[str, int, int, int])
def requestMinigame(minigameName='remove', minigameKeep=False, minigameDiff=None, minigamePG=None):
    if minigameName == 'remove':
        if spellbook.getInvoker().doId in RequestMinigame:
            del RequestMinigame[spellbook.getInvoker().doId]
            return 'Deleted trolley game request.'
        else:
            return 'You had no trolley game requests!'

    else:
        RequestMinigame[spellbook.getTarget().doId] = (
         ToontownGlobals.MinigameNames[minigameName], minigameKeep, minigameDiff, minigamePG)
        return 'Your request for ' + minigameName + ' was added.'