# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.effects.Ripples
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from toontown.battle.BattleProps import globalPropPool

class Ripples(NodePath):
    rippleCount = 0

    def __init__(self, parent=hidden):
        NodePath.__init__(self)
        self.assign(globalPropPool.getProp('ripples'))
        self.reparentTo(parent)
        self.getChild(0).setZ(0.1)
        self.seqNode = self.find('**/+SequenceNode').node()
        self.seqNode.setPlayRate(0)
        self.track = None
        self.trackId = Ripples.rippleCount
        Ripples.rippleCount += 1
        self.setBin('fixed', 100, 1)
        self.hide()
        return

    def createTrack(self, rate=1):
        tflipDuration = self.seqNode.getNumChildren() / (float(rate) * 24)
        self.track = Sequence(Func(self.show), Func(self.seqNode.play, 0, self.seqNode.getNumFrames() - 1), Func(self.seqNode.setPlayRate, rate), Wait(tflipDuration), Func(self.seqNode.setPlayRate, 0), Func(self.hide), name='ripples-track-%d' % self.trackId)

    def play(self, rate=1):
        self.stop()
        self.createTrack(rate)
        self.track.start()

    def loop(self, rate=1):
        self.stop()
        self.createTrack(rate)
        self.track.loop()

    def stop(self):
        if self.track:
            self.track.finish()

    def destroy(self):
        self.stop()
        self.track = None
        del self.seqNode
        self.removeNode()
        return