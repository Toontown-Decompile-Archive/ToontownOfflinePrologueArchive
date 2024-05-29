# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.speedchat.TTSCPetTrickMenu
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from otp.speedchat.SCMenu import SCMenu
from otp.speedchat import SCMenuHolder
from otp.speedchat.SCStaticTextTerminal import SCStaticTextTerminal
from otp.otpbase import OTPLocalizer
from toontown.pets import PetTricks

class TTSCPetTrickMenu(SCMenu):
    notify = DirectNotifyGlobal.directNotify.newCategory('TTSCPetTrickMenu')

    def __init__(self):
        SCMenu.__init__(self)
        self.accept('petTrickPhrasesChanged', self.__phrasesChanged)
        self.__phrasesChanged()

    def destroy(self):
        self.ignore('petTrickPhrasesChanged')
        SCMenu.destroy(self)

    def __phrasesChanged(self, zoneId=0):
        self.clearMenu()
        try:
            lt = base.localAvatar
        except:
            return

        for trickId in lt.petTrickPhrases:
            if trickId not in PetTricks.TrickId2scIds:
                TTSCPetTrickMenu.notify.warning('unknown trick ID: %s' % trickId)
            else:
                for msg in PetTricks.TrickId2scIds[trickId]:
                    self.append(SCStaticTextTerminal(msg))