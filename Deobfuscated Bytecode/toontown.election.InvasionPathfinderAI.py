# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.election.InvasionPathfinderAI
# Compiled at: 2014-04-30 09:53:54
import bisect, math
from pandac.PandaModules import *

class InvasionPathfinderAI:
    VERTEX_EXTRUSION = 0.15

    def __init__(self, polygons=None):
        self.borders = []
        self.vertices = []
        if polygons:
            for polygon in polygons:
                self.addPolygon(polygon)

            self.buildNeighbors()

    def addPolygon(self, points):
        newVertices = []
        for i, point in enumerate(points):
            prevPoint = points[i - 1]
            x, y = point
            x2, y2 = prevPoint
            self.borders.append((x2, y2, x, y))
            vertex = AStarVertex(Point2(x, y))
            self.vertices.append(vertex)
            newVertices.append(vertex)

        for i, vertex in enumerate(newVertices):
            prevVertex = newVertices[i - 1]
            nextVertex = newVertices[(i + 1) % len(newVertices)]
            vertex.setPolygonalNeighbors(prevVertex, nextVertex)
            vertex.extrudeVertex(self.VERTEX_EXTRUSION)
            if vertex.interiorAngle > 180:
                self.vertices.remove(vertex)

    def buildNeighbors(self):
        for vertex in self.vertices:
            vertex.resetNeighbors()

        for i, v1 in enumerate(self.vertices):
            for v2 in self.vertices[i + 1:]:
                self._considerLink(v1, v2)

    def planPath(self, fromPoint, toPoint, closeEnough=0):
        x1, y1 = fromPoint
        x2, y2 = toPoint
        if not self._testLineIntersections((x1, y1, x2, y2), self.borders):
            return [
             toPoint]
        else:
            fromVertex = AStarVertex(Point2(x1, y1))
            toVertex = AStarVertex(Point2(x2, y2))
            for vertex in self.vertices:
                self._considerLink(vertex, fromVertex)
                self._considerLink(vertex, toVertex)

            tempVertices = [fromVertex, toVertex]
            isApproximate = False
            try:
                if not toVertex.getNeighbors():
                    if closeEnough is 0:
                        return
                    isApproximate = True
                    closeEnoughSquared = closeEnough * closeEnough
                    for border in self.borders:
                        projected = self._projectPointToLine(toVertex.pos, border)
                        if projected is None:
                            continue
                        if (projected - toVertex.pos).lengthSquared() > closeEnoughSquared:
                            continue
                        projectionDirection = projected - toVertex.pos
                        projectionDirection.normalize()
                        projected += projectionDirection * self.VERTEX_EXTRUSION
                        projectedVertex = AStarVertex(projected)
                        projectedVertex.link(toVertex)
                        self._considerLink(fromVertex, projectedVertex)
                        for vertex in self.vertices:
                            self._considerLink(vertex, projectedVertex, False)

                        tempVertices.append(projectedVertex)

                astar = AStarSearch()
                result = astar.search(fromVertex, toVertex)
                if result:
                    if isApproximate:
                        result.pop(-1)
                    return [ vertex.pos for vertex in result ]
                return
            finally:
                for tempVertex in tempVertices:
                    tempVertex.unlinkAll()

            return

    def _considerLink(self, v1, v2, testAngles=True):
        if v1.isVertexPolygonalNeighbor(v2):
            v1.link(v2)
            return
        if testAngles:
            if v1.isVertexInsideAngle(v2) or v2.isVertexInsideAngle(v1):
                return
            if v1.isVertexInsideOpposite(v2) or v2.isVertexInsideOpposite(v1):
                return
        x1, y1 = v1.pos
        x2, y2 = v2.pos
        if self._testLineIntersections((x1, y1, x2, y2), self.borders):
            return
        v1.link(v2)

    def _makeLineMat(self, x1, y1, x2, y2):
        mat = Mat3(y2 - y1, x1 - x2, 0, x2 - x1, y2 - y1, 0, x1, y1, 1)
        if not mat.invertInPlace():
            return None
        else:
            return mat

    def _testLineIntersections(self, incident, lines):
        x1, y1, x2, y2 = incident
        mat = self._makeLineMat(x1, y1, x2, y2)
        if not mat:
            return False
        for x1, y1, x2, y2 in lines:
            x1, y1, _ = mat.xform(Point3(x1, y1, 1))
            x2, y2, _ = mat.xform(Point3(x2, y2, 1))
            if not (x1 < 0 and x2 > 0 or x1 > 0 and x2 < 0):
                continue
            m = (y2 - y1) / (x2 - x1)
            b = m * -x1 + y1
            epsilon = 0.001
            if 0.0 + epsilon < b < 1.0 - epsilon:
                return True

        return False

    def _projectPointToLine(self, point, line):
        x1, y1, x2, y2 = line
        x, y = point
        origin = Point2(x1, y1)
        vecLine = Point2(x2, y2) - origin
        vecPoint = Point2(x, y) - origin
        projectedPoint = vecPoint.project(vecLine)
        if projectedPoint.lengthSquared() > vecLine.lengthSquared():
            return None
        else:
            if projectedPoint.dot(vecLine) < 0:
                return None
            return origin + projectedPoint


class AStarVertex:

    def __init__(self, pos):
        self.pos = pos
        self.neighbors = []
        self.prevPolyNeighbor = None
        self.nextPolyNeighbor = None
        self.interiorAngle = None
        self.extrudeVector = None
        return

    def link(self, neighbor):
        self.__addNeighbor(neighbor)
        neighbor.__addNeighbor(self)

    def unlink(self, neighbor):
        self.__removeNeighbor(neighbor)
        neighbor.__removeNeighbor(self)

    def unlinkAll(self):
        neighbors = list(self.neighbors)
        for neighbor in neighbors:
            self.unlink(neighbor)

    def resetNeighbors(self):
        self.neighbors = []

    def __addNeighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

    def __removeNeighbor(self, neighbor):
        if neighbor in self.neighbors:
            self.neighbors.remove(neighbor)

    def setPolygonalNeighbors(self, prev, next):
        vecToPrev = prev.pos - self.pos
        vecToNext = next.pos - self.pos
        angle = vecToPrev.signedAngleDeg(vecToNext)
        angle %= 360
        self.prevPolyNeighbor = prev
        self.nextPolyNeighbor = next
        self.interiorAngle = angle
        prevAngle = Vec2(1, 0).signedAngleDeg(vecToPrev)
        extrudeAngle = prevAngle + self.interiorAngle / 2.0 + 180
        extrudeAngle *= math.pi / 180
        self.extrudeVector = Vec2(math.cos(extrudeAngle), math.sin(extrudeAngle))

    def isVertexInsideAngle(self, other):
        if self.prevPolyNeighbor is None or self.interiorAngle is None:
            return False
        vecToPrev = self.prevPolyNeighbor.pos - self.pos
        vecToOther = other.pos - self.pos
        angle = vecToPrev.signedAngleDeg(vecToOther)
        angle %= 360
        return angle < self.interiorAngle

    def isVertexInsideOpposite(self, other):
        if self.prevPolyNeighbor is None or self.interiorAngle is None:
            return False
        vecToPrev = self.prevPolyNeighbor.pos - self.pos
        vecToOther = other.pos - self.pos
        angle = vecToPrev.signedAngleDeg(vecToOther)
        angle -= 180
        angle %= 360
        return angle < self.interiorAngle

    def extrudeVertex(self, distance):
        if self.extrudeVector is None:
            return
        else:
            self.pos += self.extrudeVector * distance
            return

    def isVertexPolygonalNeighbor(self, other):
        return other in (self.prevPolyNeighbor, self.nextPolyNeighbor)

    def getNeighbors(self):
        return self.neighbors

    def getHeuristicTo(self, other):
        return (self.pos - other.pos).length()

    def getCostTo(self, other):
        return (self.pos - other.pos).length()


class AStarSearch:

    def __init__(self):
        self.openList = []
        self.closed = set()
        self.paths = {}
        self._toVertex = None
        return

    def search(self, fromVertex, toVertex):
        self.openList = [AStarPath(None, fromVertex, 0, 0)]
        self.closed = set()
        self.paths = {}
        self._toVertex = toVertex
        while self.openList and toVertex not in self.paths:
            self.__doIteration()

        path = self.paths.get(toVertex)
        if not path:
            return
        else:
            return self.__getVerticesToPath(path)

    def __doIteration--- This code section failed: ---

 L. 384         0  LOAD_FAST             0  'self'
                3  LOAD_ATTR             0  'openList'
                6  LOAD_ATTR             1  'pop'
                9  LOAD_CONST               0
               12  CALL_FUNCTION_1       1  None
               15  STORE_FAST            1  'path'

 L. 385        18  LOAD_FAST             1  'path'
               21  LOAD_ATTR             2  'vertex'
               24  STORE_FAST            2  'vertex'

 L. 386        27  LOAD_FAST             0  'self'
               30  LOAD_ATTR             3  'closed'
               33  LOAD_ATTR             4  'add'
               36  LOAD_FAST             2  'vertex'
               39  CALL_FUNCTION_1       1  None
               42  POP_TOP          

 L. 388        43  LOAD_FAST             2  'vertex'
               46  LOAD_ATTR             5  'getNeighbors'
               49  CALL_FUNCTION_0       0  None
               52  STORE_FAST            3  'neighbors'

 L. 389        55  SETUP_LOOP          200  'to 258'
               58  LOAD_FAST             3  'neighbors'
               61  GET_ITER         
               62  FOR_ITER            192  'to 257'
               65  STORE_FAST            4  'neighbor'

 L. 390        68  LOAD_FAST             4  'neighbor'
               71  LOAD_FAST             0  'self'
               74  LOAD_ATTR             3  'closed'
               77  COMPARE_OP            6  in
               80  POP_JUMP_IF_FALSE    89  'to 89'

 L. 392        83  CONTINUE             62  'to 62'
               86  JUMP_FORWARD          0  'to 89'
             89_0  COME_FROM            86  '86'

 L. 394        89  LOAD_FAST             2  'vertex'
               92  LOAD_ATTR             6  'getCostTo'
               95  LOAD_FAST             4  'neighbor'
               98  CALL_FUNCTION_1       1  None
              101  LOAD_FAST             1  'path'
              104  LOAD_ATTR             7  'totalCost'
              107  BINARY_ADD       
              108  STORE_FAST            5  'cost'

 L. 396       111  LOAD_FAST             4  'neighbor'
              114  LOAD_FAST             0  'self'
              117  LOAD_ATTR             8  'paths'
              120  COMPARE_OP            6  in
              123  POP_JUMP_IF_FALSE   189  'to 189'

 L. 400       126  LOAD_FAST             0  'self'
              129  LOAD_ATTR             8  'paths'
              132  LOAD_FAST             4  'neighbor'
              135  BINARY_SUBSCR    
              136  STORE_FAST            6  'neighborPath'

 L. 401       139  LOAD_FAST             5  'cost'
              142  LOAD_FAST             6  'neighborPath'
              145  LOAD_ATTR             7  'totalCost'
              148  COMPARE_OP            0  <
              151  POP_JUMP_IF_FALSE    62  'to 62'

 L. 403       154  LOAD_FAST             0  'self'
              157  LOAD_ATTR             0  'openList'
              160  LOAD_ATTR             9  'remove'
              163  LOAD_FAST             6  'neighborPath'
              166  CALL_FUNCTION_1       1  None
              169  POP_TOP          

 L. 404       170  LOAD_FAST             0  'self'
              173  LOAD_ATTR             8  'paths'
              176  LOAD_FAST             4  'neighbor'
              179  DELETE_SUBSCR    
              180  JUMP_ABSOLUTE       189  'to 189'

 L. 408       183  CONTINUE             62  'to 62'
              186  JUMP_FORWARD          0  'to 189'
            189_0  COME_FROM           186  '186'

 L. 410       189  LOAD_GLOBAL          10  'AStarPath'
              192  LOAD_FAST             1  'path'
              195  LOAD_FAST             4  'neighbor'
              198  LOAD_FAST             5  'cost'
              201  LOAD_FAST             4  'neighbor'
              204  LOAD_ATTR            11  'getHeuristicTo'
              207  LOAD_FAST             0  'self'
              210  LOAD_ATTR            12  '_toVertex'
              213  CALL_FUNCTION_1       1  None
              216  CALL_FUNCTION_4       4  None
              219  STORE_FAST            7  'newPath'

 L. 411       222  LOAD_FAST             7  'newPath'
              225  LOAD_FAST             0  'self'
              228  LOAD_ATTR             8  'paths'
              231  LOAD_FAST             4  'neighbor'
              234  STORE_SUBSCR     

 L. 412       235  LOAD_GLOBAL          13  'bisect'
              238  LOAD_ATTR            14  'insort'
              241  LOAD_FAST             0  'self'
              244  LOAD_ATTR             0  'openList'
              247  LOAD_FAST             7  'newPath'
              250  CALL_FUNCTION_2       2  None
              253  POP_TOP          
              254  JUMP_BACK            62  'to 62'
              257  POP_BLOCK        
            258_0  COME_FROM            55  '55'

Parse error at or near `JUMP_FORWARD' instruction at offset 186

    def __getVerticesToPath(self, path):
        result = []
        while path is not None:
            result.insert(0, path.vertex)
            path = path.parent

        return result


class AStarPath:

    def __init__(self, parent, vertex, cost, heuristic):
        self.parent = parent
        self.vertex = vertex
        self.heuristic = heuristic
        self.totalCost = cost

    def __cmp__(self, other):
        return cmp(self.totalCost + self.heuristic, other.totalCost + other.heuristic)