# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.PairingGameGlobals
# Compiled at: 2014-04-30 09:53:54
import PlayingCardDeck
EasiestGameDuration = 120
HardestGameDuration = 90
EndlessGame = config.GetBool('endless-pairing-game', 0)
MaxRankIndexUsed = [7, 
 7, 
 7, 
 8, 
 9]

def createDeck(deckSeed, numPlayers):
    deck = PlayingCardDeck.PlayingCardDeck()
    deck.shuffleWithSeed(deckSeed)
    deck.removeRanksAbove(MaxRankIndexUsed[numPlayers])
    return deck


def calcGameDuration(difficulty):
    difference = EasiestGameDuration - HardestGameDuration
    adjust = difference * difficulty
    retval = EasiestGameDuration - adjust
    return retval


def calcLowFlipModifier(matches, flips):
    idealFlips = round(matches * 2 * 1.6)
    if idealFlips < 2:
        idealFlips = 2
    maxFlipsForBonus = idealFlips * 2
    retval = 0
    if flips < idealFlips:
        retval = 1
    elif maxFlipsForBonus < flips:
        retval = 0
    else:
        divisor = maxFlipsForBonus - idealFlips
        difference = maxFlipsForBonus - flips
        retval = float(difference) / divisor
    return retval