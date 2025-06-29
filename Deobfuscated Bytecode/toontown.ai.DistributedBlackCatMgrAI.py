# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.ai.DistributedBlackCatMgrAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.toon.ToonDNA import ToonDNA

class DistributedBlackCatMgrAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBlackCatMgrAI')

    def requestBlackCatTransformation(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            return
        if av.dna.getAnimal() == 'cat' and av.dna.headColor != 26:
            newDNA = ToonDNA()
            newDNA.makeFromNetString(av.getDNAString())
            newDNA.headColor = 26
            newDNA.armColor = 26
            newDNA.legColor = 26
            taskMgr.doMethodLater(1.0, (lambda task: av.b_setDNAString(newDNA.makeNetString())), 'transform-%d' % avId)
            self.sendUpdate('doBlackCatTransformation', [avId])