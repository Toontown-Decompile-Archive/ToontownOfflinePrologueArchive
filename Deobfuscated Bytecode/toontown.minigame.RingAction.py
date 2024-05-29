# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.RingAction
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
import RingTrack

class RingAction:
    notify = DirectNotifyGlobal.directNotify.newCategory('RingAction')

    def __init__(self):
        pass

    def eval(self, t):
        return (0, 0)


class RingActionStaticPos(RingAction):

    def __init__(self, pos):
        RingAction.__init__(self)
        self.__pos = pos

    def eval(self, t):
        return self.__pos


class RingActionFunction(RingAction):

    def __init__(self, func, args):
        RingAction.__init__(self)
        self.__func = func
        self.__args = args

    def eval(self, t):
        return self.__func(t, *self.__args)


class RingActionRingTrack(RingAction):

    def __init__(self, ringTrack):
        RingAction.__init__(self)
        self.__track = ringTrack

    def eval(self, t):
        return self.__track.eval(t)