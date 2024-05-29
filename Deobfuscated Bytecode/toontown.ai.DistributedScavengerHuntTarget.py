# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.ai.DistributedScavengerHuntTarget
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from otp.speedchat import SpeedChatGlobals

class DistributedScavengerHuntTarget(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedScavengerHuntTarget')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    def setupListenerDetails(self):
        self.triggered = False
        self.triggerDelay = 15
        self.accept(SpeedChatGlobals.SCCustomMsgEvent, self.phraseSaid)

    def phraseSaid(self, phraseId):
        self.notify.debug('Checking if phrase was said')
        helpPhrase = 10003

        def reset():
            self.triggered = False

        if phraseId == helpPhrase and not self.triggered:
            self.triggered = True
            self.attemptScavengerHunt()
            taskMgr.doMethodLater(self.triggerDelay, reset, 'ScavengerHunt-phrase-reset', extraArgs=[])

    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        DistributedScavengerHuntTarget.notify.debug('announceGenerate')
        self.setupListenerDetails()

    def delete(self):
        self.ignoreAll()
        taskMgr.remove('ScavengerHunt-phrase-reset')
        DistributedObject.DistributedObject.delete(self)

    def attemptScavengerHunt(self):
        DistributedScavengerHuntTarget.notify.debug('attempScavengerHunt')
        self.sendUpdate('attemptScavengerHunt', [])