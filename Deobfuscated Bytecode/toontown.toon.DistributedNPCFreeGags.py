# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.toon.DistributedNPCFreeGags
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from DistributedNPCToonBase import *
from toontown.quest import QuestParser
from toontown.quest import QuestChoiceGui
from toontown.quest import TrackChoiceGui
from toontown.toonbase import TTLocalizer
from toontown.hood import ZoneUtil
from toontown.toontowngui import TeaserPanel
from otp.nametag.NametagConstants import *

class DistributedNPCFreeGags(DistributedNPCToonBase):

    def __init__(self, cr):
        DistributedNPCToonBase.__init__(self, cr)
        self.restockSfx = loader.loadSfx('phase_9/audio/sfx/CHQ_SOS_pies_restock.ogg')

    def delayDelete(self):
        DistributedNPCToonBase.delayDelete(self)
        DistributedNPCToonBase.disable(self)

    def handleCollisionSphereEnter(self, collEntry):
        self.sendUpdate('avatarEnter', [])
        self.restockSfx.play()

    def gaveGags(self, npcId, avId, sbPhraseId):
        if avId in base.cr.doId2do:
            avName = base.cr.doId2do.get(avId).getName()
            chatPhrases = [
             'Get them Cogs, %s!' % avName,
             "You've got this, %s!" % avName,
             'Hey, %s, take some Gags!' % avName,
             'Got Gags? Now you do!']
            self.setChatAbsolute(chatPhrases[sbPhraseId], CFSpeech | CFTimeout)
        else:
            self.setChatAbsolute("Go get 'em!", CFSpeech | CFTimeout)