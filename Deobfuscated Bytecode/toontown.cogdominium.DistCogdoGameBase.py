# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.cogdominium.DistCogdoGameBase
# Compiled at: 2014-04-30 09:53:54


class DistCogdoGameBase:

    def local2GameTime(self, timestamp):
        return timestamp - self._startTime

    def game2LocalTime(self, timestamp):
        return timestamp + self._startTime

    def getCurrentGameTime(self):
        return self.local2GameTime(globalClock.getFrameTime())