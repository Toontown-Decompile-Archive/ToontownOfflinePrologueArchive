# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.CogSuitManagerAI
# Compiled at: 2014-04-30 09:53:54
from otp.ai.AIBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
import random
from toontown.suit import SuitDNA
import CogDisguiseGlobals

class CogSuitManagerAI:
    notify = DirectNotifyGlobal.directNotify.newCategory('CogSuitManagerAI')

    def __init__(self, air):
        self.air = air

    def recoverPart(self, av, factoryType, suitTrack, zoneId, avList):
        partsRecovered = [
         0,
         0,
         0,
         0]
        part = av.giveGenericCogPart(factoryType, suitTrack)
        if part:
            partsRecovered[CogDisguiseGlobals.dept2deptIndex(suitTrack)] = part
            self.air.questManager.toonRecoveredCogSuitPart(av, zoneId, avList)
        return partsRecovered