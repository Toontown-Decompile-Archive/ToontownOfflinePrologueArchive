# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.shtiker.NewbiePurchaseManager
# Compiled at: 2014-04-30 09:53:54
import PurchaseManager
from toontown.quest import QuestParser
from toontown.toon import NPCToons

class NewbiePurchaseManager(PurchaseManager.PurchaseManager):

    def setOwnedNewbieId(self, ownedNewbieId):
        self.ownedNewbieId = ownedNewbieId

    def calcHasLocalToon(self):
        return base.localAvatar.doId == self.ownedNewbieId

    def announceGenerate(self):
        PurchaseManager.PurchaseManager.announceGenerate(self)
        if self.hasLocalToon:
            self.npc = NPCToons.createLocalNPC(2011)
            self.npc.addActive()

            def getDoId():
                return 0

            self.npc.getDoId = getDoId

            def acquireDelayDelete(name):
                return serialNum()

            self.npc.acquireDelayDelete = acquireDelayDelete

            def releaseDelayDelete(token):
                pass

            self.npc.releaseDelayDelete = releaseDelayDelete

            def uniqueName(string):
                return string

            self.npc.uniqueName = uniqueName
            self.accept('gagScreenIsUp', self.playMovie)
            self.purchase = base.cr.playGame.hood.purchase
            self.purchase.enterTutorialMode(self.ownedNewbieId)

    def disable(self):
        PurchaseManager.PurchaseManager.disable(self)
        if hasattr(self, 'movie'):
            self.npc.removeActive()
            self.npc.delete()
            del self.npc
            del self.movie

    def playMovie(self):
        self.movie = QuestParser.NPCMoviePlayer('gag_intro', base.localAvatar, self.npc)
        self.movie.setVar('backToPlaygroundButton', self.purchase.backToPlayground)
        self.movie.setVar('playAgainButton', self.purchase.playAgain)
        self.movie.setVar('purchaseBg', self.purchase.bg)
        self.movie.play()