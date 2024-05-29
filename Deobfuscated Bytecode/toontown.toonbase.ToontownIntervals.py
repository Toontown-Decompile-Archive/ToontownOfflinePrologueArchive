# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.toonbase.ToontownIntervals
# Compiled at: 2014-04-30 09:53:54
from direct.interval.MetaInterval import Sequence
from direct.interval.FunctionInterval import Wait, Func
PULSE_GUI_DURATION = 0.2
PULSE_GUI_CHANGE = 0.333

def cleanup(name):
    taskMgr.remove(name)


def start(ival):
    cleanup(ival.getName())
    ival.start()
    return ival


def loop(ival):
    cleanup(ival.getName())
    ival.loop()
    return ival


def getPulseLargerIval(np, name, duration=PULSE_GUI_DURATION, scale=1):
    return getPulseIval(np, name, 1 + PULSE_GUI_CHANGE, duration=duration, scale=scale)


def getPulseSmallerIval(np, name, duration=PULSE_GUI_DURATION, scale=1):
    return getPulseIval(np, name, 1 - PULSE_GUI_CHANGE, duration=duration, scale=scale)


def getPulseIval(np, name, change, duration=PULSE_GUI_CHANGE, scale=1):
    return Sequence(np.scaleInterval(duration, scale * change, blendType='easeOut'), np.scaleInterval(duration, scale, blendType='easeIn'), name=name, autoFinish=1)


def getPresentGuiIval(np, name, waitDuration=0.5, moveDuration=1.0, parent=aspect2d, startPos=(0, 0, 0)):
    endPos = np.getPos()
    np.setPos(parent, startPos[0], startPos[1], startPos[2])
    return Sequence(Func(np.show), getPulseLargerIval(np, '', scale=np.getScale()), Wait(waitDuration), np.posInterval(moveDuration, endPos, blendType='easeInOut'), name=name, autoFinish=1)