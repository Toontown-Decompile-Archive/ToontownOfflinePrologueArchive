# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.electionsuit.DistributedSuitBaseAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from SuitBase import SuitBase
from SuitDNA import SuitDNA

class DistributedSuitBaseAI(DistributedObjectAI, SuitBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSuitBaseAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        SuitBase.__init__(self)
        self.dna = SuitDNA()
        self.name = ''
        self.skeleRevives = 0
        self.maxSkeleRevives = 0
        self.reviveFlag = 0

    def b_setHP(self, hp):
        self.d_setHP(hp)
        self.setHP(hp)

    def d_setHP(self, hp):
        self.sendUpdate('setHP', [hp])

    def setHP(self, hp):
        self.currHP = hp

    def getHP(self):
        return self.currHP

    def getLevelDist(self):
        return self.level

    def b_setSkeleRevives(self, num):
        if num == None:
            num = 0
        self.setSkeleRevives(num)
        self.d_setSkeleRevives(self.getSkeleRevives())
        return

    def d_setSkeleRevives(self, num):
        self.sendUpdate('setSkeleRevives', [num])

    def getSkeleRevives(self):
        return self.skeleRevives

    def setSkeleRevives(self, num):
        if num == None:
            num = 0
        self.skeleRevives = num
        if num > self.maxSkeleRevives:
            self.maxSkeleRevives = num
        return

    def getMaxSkeleRevives(self):
        return self.maxSkeleRevives

    def useSkeleRevive(self):
        self.skeleRevives -= 1
        self.currHP = self.maxHP
        self.reviveFlag = 1

    def reviveCheckAndClear(self):
        returnValue = 0
        if self.reviveFlag == 1:
            returnValue = 1
            self.reviveFlag = 0
        return returnValue

    def b_setDNAString(self, string):
        self.d_setDNAString(string)
        self.setDNAString(string)

    def d_setDNAString(self, string):
        self.sendUpdate('setDNAString', [string])

    def setDNAString(self, string):
        self.dna.makeFromNetString(string)

    def getDNAString(self):
        return self.dna.makeNetString()

    def setDisplayName(self, name):
        pass