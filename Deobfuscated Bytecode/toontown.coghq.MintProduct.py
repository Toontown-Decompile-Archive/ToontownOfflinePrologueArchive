# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.MintProduct
# Compiled at: 2014-04-30 09:53:54
from toontown.toonbase.ToontownGlobals import *
from otp.level import BasicEntities

class MintProduct(BasicEntities.NodePathEntity):
    Models = {CashbotMintIntA: 'phase_10/models/cashbotHQ/MoneyBag', CashbotMintIntB: 'phase_10/models/cashbotHQ/MoneyStackPallet', 
       CashbotMintIntC: 'phase_10/models/cashbotHQ/GoldBarStack'}
    Scales = {CashbotMintIntA: 0.98, CashbotMintIntB: 0.38, 
       CashbotMintIntC: 0.6}

    def __init__(self, level, entId):
        BasicEntities.NodePathEntity.__init__(self, level, entId)
        self.model = None
        self.mintId = self.level.mintId
        self.loadModel()
        return

    def destroy(self):
        if self.model:
            self.model.removeNode()
            del self.model
        BasicEntities.NodePathEntity.destroy(self)

    def loadModel(self):
        if self.model:
            self.model.removeNode()
            self.model = None
        self.model = loader.loadModel(self.Models[self.mintId])
        self.model.setScale(self.Scales[self.mintId])
        self.model.flattenStrong()
        if self.model:
            self.model.reparentTo(self)
        return

    if __dev__:

        def setMintId(self, mintId):
            self.mintId = mintId
            self.loadModel()