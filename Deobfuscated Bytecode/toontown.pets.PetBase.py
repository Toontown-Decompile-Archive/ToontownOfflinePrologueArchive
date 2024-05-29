# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.pets.PetBase
# Compiled at: 2014-04-30 09:53:54
from toontown.pets.PetConstants import AnimMoods
from toontown.pets import PetMood

class PetBase:

    def getSetterName(self, valueName, prefix='set'):
        return '%s%s%s' % (prefix, valueName[0].upper(), valueName[1:])

    def getAnimMood(self):
        if self.mood.getDominantMood() in PetMood.PetMood.ExcitedMoods:
            return AnimMoods.EXCITED
        else:
            if self.mood.getDominantMood() in PetMood.PetMood.UnhappyMoods:
                return AnimMoods.SAD
            return AnimMoods.NEUTRAL

    def isExcited(self):
        return self.getAnimMood() == AnimMoods.EXCITED

    def isSad(self):
        return self.getAnimMood() == AnimMoods.SAD