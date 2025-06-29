# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.PlayingCardDeck
# Compiled at: 2014-04-30 09:53:54
import random, PlayingCardGlobals
from toontown.minigame.PlayingCard import PlayingCardBase

class PlayingCardDeck:

    def __init__(self):
        self.shuffle()

    def shuffle(self):
        self.cards = range(0, PlayingCardGlobals.MaxSuit * PlayingCardGlobals.MaxRank)
        random.shuffle(self.cards)

    def shuffleWithSeed(self, seed):
        generator = random.Random()
        generator.seed(seed)
        self.cards = range(0, PlayingCardGlobals.MaxSuit * PlayingCardGlobals.MaxRank)
        generator.shuffle(self.cards)

    def dealCard(self):
        return self.cards.pop(0)

    def dealCards(self, num):
        cardList = []
        for i in range(num):
            cardList.append(self.cards.pop(0))

        return cardList

    def count(self):
        return len(self.cards)

    def removeRanksAbove(self, maxRankInDeck):
        done = False
        while not done:
            removedOne = False
            for cardValue in self.cards:
                tempCard = PlayingCardBase(cardValue)
                if tempCard.rank > maxRankInDeck:
                    self.cards.remove(cardValue)
                    removedOne = True

            if not removedOne:
                done = True