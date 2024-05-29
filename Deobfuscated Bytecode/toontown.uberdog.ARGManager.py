# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.uberdog.ARGManager
# Compiled at: 2014-04-30 09:53:54
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from toontown.toonbase import ToontownGlobals
from otp.speedchat import SpeedChatGlobals
from direct.directnotify.DirectNotifyGlobal import directNotify
from toontown.hood import ZoneUtil
from pandac.PandaModules import Vec3
from otp.margins import WhisperPopup
Hood2Details = {2665: [
        (6, 7, 9), 1150, 2665], 
   1832: [
        (6, 7, 9), 1150, 1832], 
   5502: [
        (6, 7, 9), 1150, 5502], 
   4612: [
        (6, 7, 9), 1150, 4612], 
   3636: [
        (6, 7, 9), 1150, 3636], 
   9705: [
        (6, 7, 9), 1150, 9705], 
   3823: [
        (6, 7, 9), 1150, 3823]}
Interior2Messages = {2665: [
        'Keep them far out of sight.', "The mine should do. Nobody can get to there. Alec's too afraid to pilot the balloon there."], 
   1832: [
        'If they do attack, we need the silliness levels to increase about one-hundred-fold.', 'Get everyone to fight Cogs, throw parties... maybe even convince those guys at your other project to do something extravagant.'], 
   5502: [
        'Those Cogs are strong. So, so strong.', 'Walt knows what kind of chaos can ensue if the other Cogs accept their "merger proposal".'], 
   4612: [
        'They might feel brave enough to build...', "Well, something big. I won't concern you with the specifics. Just the nature of Surlees."], 
   3636: [
        'If you absolutely must, you need to counteract this construction.', 'The most obvious way would be to build something of your own.'], 
   9705: [
        'The construction tools of Toontown have been lost to time.', 'But us great scientists... perhaps we can figure something out.'], 
   3823: [
        'Most importantly, train everyone. The Hac--', "Hmm? What's this? Who are you? What are you d--"]}

class ARGManager(DistributedObjectGlobal):
    notify = directNotify.newCategory('ARGManager')

    def __init__(self, cr):
        DistributedObjectGlobal.__init__(self, cr)
        self.setupPortableHoleEvent()

    def disable(self):
        self.cleanupPortableHoleEvent()
        DistributedObjectGlobal.disable(self)

    def delete(self):
        self.cleanupPortableHoleEvent()
        DistributedObjectGlobal.delete(self)

    def setupPortableHoleEvent(self):

        def phraseSaid(phraseId):
            position, speedchatIndex, destination = Hood2Details.get(base.cr.playGame.getPlace().getZoneId(), [None, None, None])
            if not position or not speedchatIndex or not destination:
                return
            if speedchatIndex != phraseId:
                return
            else:
                msgBefore, msgAfter = Interior2Messages.get(destination, [None, None])
                if not msgBefore:
                    self.notify.warning('Interior %d has no message definitions!' % destination)
                    return
                taskMgr.doMethodLater(2, base.localAvatar.setSystemMessage, self.uniqueName('arg-before-msg'), extraArgs=[0, msgBefore])
                taskMgr.doMethodLater(7, base.localAvatar.setSystemMessage, self.uniqueName('arg-after-msg'), extraArgs=[0, msgAfter])
                if destination == 3823:
                    taskMgr.doMethodLater(15, base.localAvatar.setSystemMessage, self.uniqueName('arg-after-after-msg'), extraArgs=[0, ':toonsafe: ALERT: TOON \'Doctor "Glasses" Surlee\' WAS KIDNAPPED BY COG \'Script Kiddie\'. CALLING POLICE...'])
                    taskMgr.doMethodLater(25, base.localAvatar.setSystemMessage, self.uniqueName('arg-after-after-msg'), extraArgs=[0, 'Professor Flake: Hmm. I don\'t know what a "Hac" is... but we appear to have some BIG trouble on the line.', WhisperPopup.WTEmote])
                return

        self.accept(SpeedChatGlobals.SCStaticTextMsgEvent, phraseSaid)

    def cleanupPortableHoleEvent(self):
        self.ignore(SpeedChatGlobals.SCStaticTextMsgEvent)