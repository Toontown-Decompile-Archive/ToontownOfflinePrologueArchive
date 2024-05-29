# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.PlatformEntity
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from otp.level import BasicEntities
import MovingPlatform

class PlatformEntity(BasicEntities.NodePathEntity):

    def __init__(self, level, entId):
        BasicEntities.NodePathEntity.__init__(self, level, entId)
        self.start()

    def destroy(self):
        self.stop()
        BasicEntities.NodePathEntity.destroy(self)

    def start(self):
        model = loader.loadModel(self.modelPath)
        if model is None:
            return
        else:
            if len(self.floorName) == 0:
                return
            model.setScale(self.modelScale)
            model.flattenMedium()
            self.platform = MovingPlatform.MovingPlatform()
            self.platform.setupCopyModel(self.getParentToken(), model, self.floorName)
            self.platform.reparentTo(self)
            startPos = Point3(0, 0, 0)
            endPos = self.offset
            distance = Vec3(self.offset).length()
            waitDur = self.period * self.waitPercent
            moveDur = self.period - waitDur
            self.moveIval = Sequence(WaitInterval(waitDur * 0.5), LerpPosInterval(self.platform, moveDur * 0.5, endPos, startPos=startPos, name='platformOut%s' % self.entId, blendType=self.motion, fluid=1), WaitInterval(waitDur * 0.5), LerpPosInterval(self.platform, moveDur * 0.5, startPos, startPos=endPos, name='platformBack%s' % self.entId, blendType=self.motion, fluid=1), name=self.getUniqueName('platformIval'))
            self.moveIval.loop()
            self.moveIval.setT(globalClock.getFrameTime() - self.level.startTime + self.period * self.phaseShift)
            return

    def stop(self):
        if hasattr(self, 'moveIval'):
            self.moveIval.pause()
            del self.moveIval
        if hasattr(self, 'platform'):
            self.platform.destroy()
            del self.platform

    if __dev__:

        def attribChanged(self, *args):
            self.stop()
            self.start()