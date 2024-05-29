# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.catalog.CatalogAnimatedFurnitureItem
# Compiled at: 2014-04-30 09:53:54
from CatalogFurnitureItem import *
FTAnimRate = 6
AnimatedFurnitureItemKeys = (10020, 270, 990, 460, 470, 480, 490, 491, 492)

class CatalogAnimatedFurnitureItem(CatalogFurnitureItem):

    def loadModel(self):
        model = CatalogFurnitureItem.loadModel(self)
        self.setAnimRate(model, self.getAnimRate())
        return model

    def getAnimRate(self):
        item = FurnitureTypes[self.furnitureType]
        if FTAnimRate < len(item):
            animRate = item[FTAnimRate]
            if not animRate == None:
                return item[FTAnimRate]
            return 1
        else:
            return 1
        return

    def setAnimRate(self, model, rate):
        seqNodes = model.findAllMatches('**/seqNode*')
        for seqNode in seqNodes:
            seqNode.node().setPlayRate(rate)