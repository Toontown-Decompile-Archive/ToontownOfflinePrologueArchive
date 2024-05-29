# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.cogdominium.CogdoFlyingUtil
# Compiled at: 2014-04-30 09:53:54
from otp.otpbase import OTPGlobals
from CogdoFlyingShadowPlacer import CogdoFlyingShadowPlacer

def loadMockup(fileName, dmodelsAlt='coffin'):
    try:
        model = loader.loadModel(fileName)
    except IOError:
        model = loader.loadModel('phase_4/models/props/%s' % dmodelsAlt)

    return model


def swapAvatarShadowPlacer(avatar, name):
    avatar.setActiveShadow(0)
    avatar.deleteDropShadow()
    avatar.initializeDropShadow()
    if avatar.shadowPlacer:
        avatar.shadowPlacer.delete()
        avatar.shadowPlacer = None
    shadowPlacer = CogdoFlyingShadowPlacer(base.shadowTrav, avatar.dropShadow, OTPGlobals.WallBitmask, OTPGlobals.FloorBitmask, name)
    avatar.shadowPlacer = shadowPlacer
    avatar.setActiveShadow(0)
    avatar.setActiveShadow(1)
    return