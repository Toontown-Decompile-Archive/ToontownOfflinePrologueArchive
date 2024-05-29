# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.level.AmbientSound
# Compiled at: 2014-04-30 09:53:54
from direct.interval.IntervalGlobal import *
import BasicEntities, random

class AmbientSound(BasicEntities.NodePathEntity):

    def __init__(self, level, entId):
        BasicEntities.NodePathEntity.__init__(self, level, entId)
        self.initSound()

    def destroy(self):
        self.destroySound()
        BasicEntities.NodePathEntity.destroy(self)

    def initSound(self):
        if not self.enabled:
            return
        else:
            if self.soundPath == '':
                return
            self.sound = base.loadSfx(self.soundPath)
            if self.sound is None:
                return
            self.soundIval = SoundInterval(self.sound, node=self, volume=self.volume)
            self.soundIval.loop()
            self.soundIval.setT(random.random() * self.sound.length())
            return

    def destroySound(self):
        if hasattr(self, 'soundIval'):
            self.soundIval.pause()
            del self.soundIval
        if hasattr(self, 'sound'):
            del self.sound

    if __dev__:

        def attribChanged(self, *args):
            self.destroySound()
            self.initSound()