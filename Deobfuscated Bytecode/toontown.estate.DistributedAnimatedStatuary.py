# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.estate.DistributedAnimatedStatuary
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import NodePath
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.estate import DistributedStatuary
from toontown.estate import GardenGlobals
from direct.actor import Actor

class DistributedAnimatedStatuary(DistributedStatuary.DistributedStatuary):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedAnimatedStatuary')

    def __init__(self, cr):
        self.notify.debug('constructing DistributedAnimatedStatuary')
        DistributedStatuary.DistributedStatuary.__init__(self, cr)

    def loadModel(self):
        self.rotateNode = self.plantPath.attachNewNode('rotate')
        self.model = Actor.Actor()
        animPath = self.modelPath + self.anims[1]
        self.model.loadModel(self.modelPath + self.anims[0])
        self.model.loadAnims(dict([[self.anims[1], animPath]]))
        colNode = self.model.find('**/+CollisionNode')
        if self.typeIndex == 234:
            colNode.setScale(0.5)
        if not colNode.isEmpty():
            score, multiplier = ToontownGlobals.PinballScoring[ToontownGlobals.PinballStatuary]
            if self.pinballScore:
                score = self.pinballScore[0]
                multiplier = self.pinballScore[1]
            scoreNodePath = NodePath('statuary-%d-%d' % (score, multiplier))
            colNode.setName('statuaryCol')
            scoreNodePath.reparentTo(colNode.getParent())
            colNode.reparentTo(scoreNodePath)
        self.model.setScale(self.worldScale)
        self.model.reparentTo(self.rotateNode)
        self.model.loop(self.anims[1])

    def setTypeIndex(self, typeIndex):
        DistributedStatuary.DistributedStatuary.setTypeIndex(self, typeIndex)
        self.anims = GardenGlobals.PlantAttributes[typeIndex]['anims']

    def setupShadow(self):
        if self.typeIndex == 234:
            pass
        else:
            DistributedStatuary.DistributedStatuary.setupShadow()