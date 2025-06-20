# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.effects.RocketExplosion
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.particles import ParticleEffect
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import *
from toontown.battle import BattleParticles

class RocketExplosion(NodePath):

    def __init__(self, parent, smokeParent):
        NodePath.__init__(self)
        notify = DirectNotifyGlobal.directNotify.newCategory('RocketExplosionParticles')
        self.effectNode = parent.attachNewNode('RocketExplosion')
        self.effectNode.setBin('fixed', 1)
        self.effectNode.setDepthWrite(1)
        self.smokeEffectNode = smokeParent.attachNewNode('RocketSmoke')
        self.smokeEffectNode.setBin('fixed', 1)
        self.smokeEffectNode.setDepthWrite(0)
        self.effect = BattleParticles.loadParticleFile('tt_p_efx_rocketLaunchFire.ptf')
        self.smokeEffect = BattleParticles.loadParticleFile('tt_p_efx_rocketLaunchSmoke.ptf')
        ren = self.effect.getParticlesNamed('particles-1').getRenderer()
        ren.setTextureFromNode('phase_4/models/props/tt_m_efx_fireball', '**/*')
        ren = self.smokeEffect.getParticlesNamed('particles-1').getRenderer()
        ren.setTextureFromNode('phase_4/models/props/tt_m_efx_smoke', '**/*')
        self.endSeq = None
        self.cleanupCompleted = 0
        return

    def start(self):
        self.effect.start(parent=self.effectNode)
        self.smokeEffect.start(parent=self.smokeEffectNode)

    def stop(self):
        try:
            self.effect.disable()
            self.smokeEffect.disable()
        except AttributeError:
            pass

    def end(self):
        self.endSeq = Sequence(LerpColorScaleInterval(self.smokeEffectNode, 2.0, Vec4(1, 1, 1, 0)), Func(self.destroy))
        self.endSeq.start()

    def destroy(self):
        if self.endSeq:
            self.endSeq.pause()
            self.endSeq = None
        self.stop()
        if not self.cleanupCompleted:
            self.effect.cleanup()
            self.smokeEffect.cleanup()
            self.effectNode.removeNode()
            self.smokeEffectNode.removeNode()
            del self.effect
            del self.smokeEffect
            del self.effectNode
            del self.smokeEffectNode
            self.cleanupCompleted = 1
        return