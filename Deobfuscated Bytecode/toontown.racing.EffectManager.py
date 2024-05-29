# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.racing.EffectManager
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from pandac.PandaModules import *
from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import *
from toontown.battle.BattleProps import *
from toontown.battle import MovieUtil

class EffectManager(DirectObject):

    def __init__(self):
        self.effectList = []

    def delete(self):
        for effect in effectList:
            self.__removeEffect(effect)

    def addSplatEffect(self, spawner, splatName='splat-creampie', time=1, size=6, parent=render):
        splat = globalPropPool.getProp(splatName)
        splatSeq = Sequence()
        splatType = globalPropPool.getPropType(splatName)
        splatShow = Func(self.__showProp, splat, size, parent, spawner.getPos(parent))
        splatAnim = ActorInterval(splat, splatName)
        splatHide = Func(MovieUtil.removeProp, splat)
        splatRemove = Func(self.__removeEffect, splatSeq)
        splatSeq.append(splatShow)
        splatSeq.append(splatAnim)
        splatSeq.append(splatHide)
        splatSeq.append(splatRemove)
        splatSeq.start()
        self.effectList.append(splatSeq)

    def __showProp(self, prop, size, parent, pos):
        prop.reparentTo(parent)
        prop.setScale(size)
        prop.setBillboardPointEye()
        prop.setPos(pos + Vec3(0, 0, size / 2))

    def __removeEffect(self, effect):
        if effect.isPlaying():
            effect.finish()
        self.effectList.remove(effect)
        effect = None
        return