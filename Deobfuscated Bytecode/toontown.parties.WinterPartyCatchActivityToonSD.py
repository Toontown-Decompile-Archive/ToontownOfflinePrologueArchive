# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.parties.WinterPartyCatchActivityToonSD
# Compiled at: 2014-04-30 09:53:54
import PartyCatchActivityToonSD
from pandac.PandaModules import Vec4
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import Sequence, Parallel, Wait, Func
from direct.interval.IntervalGlobal import LerpColorScaleInterval
from direct.interval.IntervalGlobal import WaitInterval, ActorInterval, FunctionInterval
from direct.fsm import ClassicFSM, State

class WinterPartyCatchActivityToonSD(PartyCatchActivityToonSD.PartyCatchActivityToonSD):
    notify = DirectNotifyGlobal.directNotify.newCategory('PartyCatchActivityToonSD')

    def __init__(self, avId, activity):
        WinterPartyCatchActivityToonSD.notify.debug('init : avId = %s, activity = %s ' % (avId, activity))
        PartyCatchActivityToonSD.PartyCatchActivityToonSD.__init__(self, avId, activity)

    def enterEatFruit(self, fruitModel, handNode):
        self.notify.debug('enterEatFruit')
        if self.isLocal:
            self.activity.orthoWalk.start()
        self.setAnimState('Catching', 1.0)
        self.fruitModel = fruitModel
        renderScale = fruitModel.getScale(render)
        fruitModel.reparentTo(handNode)
        fruitModel.setScale(render, renderScale)
        fruitModel.setTransparency(1)
        duration = self.toon.getDuration('catch-eatneutral')
        self.eatIval = Sequence(Parallel(WaitInterval(duration), Sequence(LerpColorScaleInterval(fruitModel, duration / 2.0, Vec4(1.0, 1.0, 1.0, 0.0)))), Func(self.fsm.request, 'normal'), name=self.toon.uniqueName('eatingIval'))
        self.eatIval.start()

    def exitEatFruit(self):
        self.eatIval.pause()
        del self.eatIval
        self.fruitModel.reparentTo(hidden)
        self.fruitModel.removeNode()
        del self.fruitModel
        self.setAnimState('off', 1.0)
        if self.isLocal:
            self.activity.orthoWalk.stop()