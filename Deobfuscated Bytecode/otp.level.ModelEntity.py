# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.level.ModelEntity
# Compiled at: 2014-04-30 09:53:54
from toontown.toonbase.ToontownGlobals import *
from direct.directnotify import DirectNotifyGlobal
import BasicEntities

class ModelEntity(BasicEntities.NodePathEntity):
    LoadFuncs = {'loadModel': loader.loadModel}

    def __init__(self, level, entId):
        self.collisionsOnly = False
        self.loadType = 'loadModel'
        self.flattenType = 'light'
        self.goonHatType = 'none'
        self.entInitialized = False
        BasicEntities.NodePathEntity.__init__(self, level, entId)
        self.entInitialized = True
        self.model = None
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
        if self.modelPath is None:
            return
        else:
            self.model = ModelEntity.LoadFuncs[self.loadType](self.modelPath)
            if self.model:
                self.model.reparentTo(self)
                if self.collisionsOnly:
                    if __dev__:
                        self.model.setTransparency(1)
                        self.model.setColorScale(1, 1, 1, 0.1)
                    else:
                        self.model.hide()
                else:
                    self.model.show()
                if self.modelPath in ('phase_9/models/cogHQ/woodCrateB', 'phase_9/models/cogHQ/metal_crateB',
                                      'phase_10/models/cashbotHQ/CBMetalCrate', 'phase_10/models/cogHQ/CBMetalCrate2',
                                      'phase_10/models/cashbotHQ/CBWoodCrate', 'phase_11/models/lawbotHQ/LB_metal_crate',
                                      'phase_11/models/lawbotHQ/LB_metal_crate2'):
                    cNode = self.find('**/wall')
                    cNode.setZ(cNode, -0.75)
                    colNode = self.find('**/collision')
                    floor = colNode.find('**/floor')
                    floor2 = floor.copyTo(colNode)
                    floor2.setZ(floor2, -0.75)
                if self.goonHatType is not 'none':
                    self.goonType = {'hardhat': 'pg', 'security': 'sg'}[self.goonHatType]
                    self.hat = self.model
                    if self.goonType == 'pg':
                        self.hat.find('**/security_hat').hide()
                    elif self.goonType == 'sg':
                        self.hat.find('**/hard_hat').hide()
                    del self.hat
                    del self.goonType
                if self.flattenType == 'light':
                    self.model.flattenLight()
                else:
                    if self.flattenType == 'medium':
                        self.model.flattenMedium()
                    elif self.flattenType == 'strong':
                        self.model.flattenStrong()
            return

    def setModelPath(self, path):
        self.modelPath = path
        self.loadModel()

    def setCollisionsOnly(self, collisionsOnly):
        self.collisionsOnly = collisionsOnly
        self.loadModel()

    def setGoonHatType(self, goonHatType):
        self.goonHatType = goonHatType
        self.loadModel()