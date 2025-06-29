# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.suit.DistributedSuitPlanner
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.distributed import DistributedObject
import SuitPlannerBase
from toontown.toonbase import ToontownGlobals
from otp.ai.MagicWordGlobal import *
from toontown.dna import *

class DistributedSuitPlanner(DistributedObject.DistributedObject, SuitPlannerBase.SuitPlannerBase):

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        SuitPlannerBase.SuitPlannerBase.__init__(self)
        self.suitList = []
        self.buildingList = [0,
         0,
         0,
         0]
        self.pathViz = None
        return

    def generate(self):
        self.accept('suitShowPaths', self.showPaths)
        self.accept('suitHidePaths', self.hidePaths)
        self.notify.info('DistributedSuitPlanner %d: generating' % self.getDoId())
        DistributedObject.DistributedObject.generate(self)
        base.cr.currSuitPlanner = self

    def disable(self):
        self.ignore('suitShowPaths')
        self.ignore('suitHidePaths')
        self.notify.info('DistributedSuitPlanner %d: disabling' % self.getDoId())
        self.hidePaths()
        DistributedObject.DistributedObject.disable(self)
        base.cr.currSuitPlanner = None
        return

    def d_suitListQuery(self):
        self.sendUpdate('suitListQuery')

    def suitListResponse(self, suitList):
        self.suitList = suitList
        messenger.send('suitListResponse')

    def d_buildingListQuery(self):
        self.sendUpdate('buildingListQuery')

    def buildingListResponse(self, buildingList):
        self.buildingList = buildingList
        messenger.send('buildingListResponse')

    def hidePaths(self):
        if self.pathViz:
            self.pathViz.detachNode()
            self.pathViz = None
        return

    def showPaths(self):
        self.hidePaths()
        vizNode = GeomNode(self.uniqueName('PathViz'))
        lines = LineSegs()
        self.pathViz = render.attachNewNode(vizNode)
        points = self.frontdoorPointList + self.sidedoorPointList + self.cogHQDoorPointList + self.streetPointList
        while len(points) > 0:
            self.__doShowPoints(vizNode, lines, None, points)

        cnode = CollisionNode('battleCells')
        cnode.setCollideMask(BitMask32.allOff())
        for zoneId, cellPos in self.battlePosDict.items():
            cnode.addSolid(CollisionSphere(cellPos, 9))
            text = '%s' % zoneId
            self.__makePathVizText(text, cellPos[0], cellPos[1], cellPos[2] + 9, (1,
                                                                                  1,
                                                                                  1,
                                                                                  1))

        self.pathViz.attachNewNode(cnode).show()
        return

    def __doShowPoints(self, vizNode, lines, p, points):
        if p == None:
            pi = len(points) - 1
            if pi < 0:
                return
            p = points[pi]
            del points[pi]
        else:
            if p not in points:
                return
            pi = points.index(p)
            del points[pi]
        text = '%s' % p.getIndex()
        pos = p.getPos()
        if p.getPointType() == DNAStoreSuitPoint.FRONTDOORPOINT:
            color = (1, 0, 0, 1)
        else:
            if p.getPointType() == DNAStoreSuitPoint.SIDEDOORPOINT:
                color = (0, 0, 1, 1)
            else:
                color = (0, 1, 0, 1)
            self.__makePathVizText(text, pos[0], pos[1], pos[2], color)
            adjacent = self.dnaStore.generateData().getAdjacentPoints(p)
            numPoints = adjacent.getNumPoints()
            for i in range(numPoints):
                q = adjacent.getPoint(i)
                pp = p.getPos()
                qp = q.getPos()
                v = Vec3(qp - pp)
                v.normalize()
                c = v.cross(Vec3.up())
                p1a = pp + v * 2 + c * 0.5
                p1b = pp + v * 3
                p1c = pp + v * 2 - c * 0.5
                lines.reset()
                lines.moveTo(pp)
                lines.drawTo(qp)
                lines.moveTo(p1a)
                lines.drawTo(p1b)
                lines.drawTo(p1c)
                lines.create(vizNode, 0)
                self.__doShowPoints(vizNode, lines, q, points)

        return

    def __makePathVizText(self, text, x, y, z, color):
        if not hasattr(self, 'debugTextNode'):
            self.debugTextNode = TextNode('debugTextNode')
            self.debugTextNode.setAlign(TextNode.ACenter)
            self.debugTextNode.setFont(ToontownGlobals.getSignFont())
        self.debugTextNode.setTextColor(*color)
        self.debugTextNode.setText(text)
        np = self.pathViz.attachNewNode(self.debugTextNode.generate())
        np.setPos(x, y, z + 1)
        np.setScale(1.0)
        np.setBillboardPointEye(2)
        np.node().setAttrib(TransparencyAttrib.make(TransparencyAttrib.MDual), 2)


@magicWord(category=CATEGORY_GRAPHICAL)
def spShow():
    messenger.send('suitShowPaths')


@magicWord(category=CATEGORY_GRAPHICAL)
def spHide():
    messenger.send('suitHidePaths')