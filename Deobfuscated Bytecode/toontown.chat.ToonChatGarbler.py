# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.chat.ToonChatGarbler
# Compiled at: 2014-04-30 09:53:54
import string, random
from toontown.toonbase import TTLocalizer
from otp.otpbase import OTPLocalizer
from otp.chat import ChatGarbler

class ToonChatGarbler(ChatGarbler.ChatGarbler):
    animalSounds = {'dog': TTLocalizer.ChatGarblerDog, 'cat': TTLocalizer.ChatGarblerCat, 
       'mouse': TTLocalizer.ChatGarblerMouse, 
       'horse': TTLocalizer.ChatGarblerHorse, 
       'rabbit': TTLocalizer.ChatGarblerRabbit, 
       'duck': TTLocalizer.ChatGarblerDuck, 
       'monkey': TTLocalizer.ChatGarblerMonkey, 
       'bear': TTLocalizer.ChatGarblerBear, 
       'pig': TTLocalizer.ChatGarblerPig, 
       'scrooge': TTLocalizer.ChatGarblerScrooge, 
       'default': OTPLocalizer.ChatGarblerDefault}

    def garble(self, toon, message):
        newMessage = ''
        animalType = toon.getStyle().getType()
        if ToonChatGarbler.animalSounds.has_key(animalType):
            wordlist = ToonChatGarbler.animalSounds[animalType]
        else:
            wordlist = ToonChatGarbler.animalSounds['default']
        numWords = random.randint(1, 7)
        for i in range(1, numWords + 1):
            wordIndex = random.randint(0, len(wordlist) - 1)
            newMessage = newMessage + wordlist[wordIndex]
            if i < numWords:
                newMessage = newMessage + ' '

        return newMessage

    def garbleSingle(self, toon, message):
        newMessage = ''
        animalType = toon.getStyle().getType()
        if ToonChatGarbler.animalSounds.has_key(animalType):
            wordlist = ToonChatGarbler.animalSounds[animalType]
        else:
            wordlist = ToonChatGarbler.animalSounds['default']
        numWords = 1
        for i in range(1, numWords + 1):
            wordIndex = random.randint(0, len(wordlist) - 1)
            newMessage = newMessage + wordlist[wordIndex]
            if i < numWords:
                newMessage = newMessage + ' '

        return newMessage