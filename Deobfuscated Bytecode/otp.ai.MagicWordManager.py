# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.ai.MagicWordManager
# Compiled at: 2014-04-30 09:53:54
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from otp.ai.MagicWordGlobal import *
from otp.nametag.NametagConstants import *
lastClickedNametag = None

class MagicWordManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('MagicWordManager')
    neverDisable = 1

    def generate(self):
        DistributedObject.DistributedObject.generate(self)
        self.accept('magicWord', self.handleMagicWord)

    def disable(self):
        self.ignore('magicWord')
        DistributedObject.DistributedObject.disable(self)

    def handleMagicWord(self, magicWord):
        if not self.cr.wantMagicWords:
            return
        else:
            if magicWord.startswith('~~'):
                if lastClickedNametag == None:
                    target = base.localAvatar
                else:
                    target = lastClickedNametag
                magicWord = magicWord[2:]
            if magicWord.startswith('~'):
                target = base.localAvatar
                magicWord = magicWord[1:]
            targetId = target.doId
            if target == base.localAvatar:
                response = spellbook.process(base.localAvatar, target, magicWord)
                if response[1]:
                    if response[0]:
                        self.sendMagicWordResponse(response[0])
                    self.sendUpdate('sendMagicWord', [magicWord, targetId, False])
                    return
            self.sendUpdate('sendMagicWord', [magicWord, targetId, True])
            return

    def sendMagicWordResponse(self, response):
        self.notify.info(response)
        base.localAvatar.setSystemMessage(0, 'Spellbook: ' + str(response))