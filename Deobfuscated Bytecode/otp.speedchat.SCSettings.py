# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.speedchat.SCSettings
# Compiled at: 2014-04-30 09:53:54
from SCColorScheme import SCColorScheme
from otp.otpbase import OTPLocalizer

class SCSettings:

    def __init__(self, eventPrefix, whisperMode=0, colorScheme=None, submenuOverlap=OTPLocalizer.SCOsubmenuOverlap, topLevelOverlap=None):
        self.eventPrefix = eventPrefix
        self.whisperMode = whisperMode
        if colorScheme is None:
            colorScheme = SCColorScheme()
        self.colorScheme = colorScheme
        self.submenuOverlap = submenuOverlap
        self.topLevelOverlap = topLevelOverlap
        return