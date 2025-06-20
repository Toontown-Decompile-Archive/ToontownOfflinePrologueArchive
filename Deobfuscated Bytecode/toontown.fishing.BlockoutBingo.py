# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.fishing.BlockoutBingo
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from toontown.fishing import BingoGlobals
from toontown.fishing import BingoCardBase

class BlockoutBingo(BingoCardBase.BingoCardBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('BlockoutBingo')

    def __init__(self, cardSize=BingoGlobals.CARD_SIZE, rowSize=BingoGlobals.CARD_ROWS, colSize=BingoGlobals.CARD_COLS):
        BingoCardBase.BingoCardBase.__init__(self, cardSize, rowSize, colSize)
        self.gameType = BingoGlobals.BLOCKOUT_CARD

    def checkForWin(self, id=0):
        for i in xrange(self.rowSize):
            if not self.rowCheck(i):
                return BingoGlobals.NO_UPDATE

        return BingoGlobals.WIN

    def checkForColor(self, id):
        return 1

    def checkForBingo(self):
        if self.checkForWin():
            return BingoGlobals.WIN
        return BingoGlobals.NO_UPDATE