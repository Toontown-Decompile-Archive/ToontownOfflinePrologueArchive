# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.PromotionManagerAI
# Compiled at: 2014-04-30 09:53:54
from otp.ai.AIBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
import random
from toontown.suit import SuitDNA
import CogDisguiseGlobals
from toontown.toonbase.ToontownBattleGlobals import getInvasionMultiplier
MeritMultiplier = 0.5

class PromotionManagerAI:
    notify = DirectNotifyGlobal.directNotify.newCategory('PromotionManagerAI')

    def __init__(self, air):
        self.air = air

    def getPercentChance(self):
        return 100.0

    def recoverMerits(self, av, cogList, zoneId, multiplier=1, extraMerits=None):
        avId = av.getDoId()
        meritsRecovered = [0, 
         0, 
         0, 
         0, 
         0]
        if extraMerits is None:
            extraMerits = [
             0, 
             0, 
             0, 
             0, 
             0]
        if self.air.suitInvasionManager.getInvading():
            multiplier *= getInvasionMultiplier()
        for i in range(len(extraMerits)):
            if CogDisguiseGlobals.isSuitComplete(av.getCogParts(), i):
                meritsRecovered[i] += extraMerits[i]
                self.notify.debug('recoverMerits: extra merits = %s' % extraMerits[i])

        self.notify.debug('recoverMerits: multiplier = %s' % multiplier)
        for cogDict in cogList:
            dept = SuitDNA.suitDepts.index(cogDict['track'])
            if avId in cogDict['activeToons']:
                if CogDisguiseGlobals.isSuitComplete(av.getCogParts(), SuitDNA.suitDepts.index(cogDict['track'])):
                    self.notify.debug('recoverMerits: checking against cogDict: %s' % cogDict)
                    rand = random.random() * 100
                    if rand <= self.getPercentChance() and not cogDict['isVirtual']:
                        merits = cogDict['level'] * MeritMultiplier
                        merits = int(round(merits))
                        if cogDict['hasRevives']:
                            merits *= 2
                        merits = merits * multiplier
                        merits = int(round(merits))
                        meritsRecovered[dept] += merits
                        self.notify.debug('recoverMerits: merits = %s' % merits)
                    else:
                        self.notify.debug('recoverMerits: virtual cog!')

        if meritsRecovered != [0, 
         0, 
         0, 
         0, 
         0]:
            actualCounted = [
             0, 
             0, 
             0, 
             0, 
             0]
            merits = av.getCogMerits()
            for i in range(len(meritsRecovered)):
                max = CogDisguiseGlobals.getTotalMerits(av, i)
                if max:
                    if merits[i] + meritsRecovered[i] <= max:
                        actualCounted[i] = meritsRecovered[i]
                        merits[i] += meritsRecovered[i]
                    else:
                        actualCounted[i] = max - merits[i]
                        merits[i] = max
                    av.b_setCogMerits(merits)

            if reduce((lambda x, y: x + y), actualCounted):
                self.air.writeServerEvent('merits', avId=avId, bossbot=actualCounted[0], lawbot=actualCounted[1], cashbot=actualCounted[2], sellbot=actualCounted[3])
                self.notify.debug('recoverMerits: av %s recovered merits %s' % (avId, actualCounted))
        return meritsRecovered