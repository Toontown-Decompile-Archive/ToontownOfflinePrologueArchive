# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.fishing.DiagonalBingo
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from toontown.fishing import BingoGlobals
from toontown.fishing import BingoCardBase

class DiagonalBingo(BingoCardBase.BingoCardBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DiagonalBingo')

    def __init__(self, cardSize=BingoGlobals.CARD_SIZE, rowSize=BingoGlobals.CARD_ROWS, colSize=BingoGlobals.CARD_COLS):
        BingoCardBase.BingoCardBase.__init__(self, cardSize, rowSize, colSize)
        self.gameType = BingoGlobals.DIAGONAL_CARD
        self.fDiagResult = 0
        self.bDiagResult = 0

    def checkForWin(self, id):
        if self.fDiagCheck(id):
            self.fDiagResult = 1
        if self.bDiagCheck(id):
            self.bDiagResult = 1
        if self.fDiagResult and self.bDiagResult:
            return BingoGlobals.WIN
        return BingoGlobals.NO_UPDATE

    def checkForColor(self, id):
        return self.onFDiag(id) | self.onBDiag(id)

    def checkForBingo(self):
        id = self.cardSize / 2
        if self.checkForWin(id):
            return BingoGlobals.WIN
        return BingoGlobals.NO_UPDATE