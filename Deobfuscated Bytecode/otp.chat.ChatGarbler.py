# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.chat.ChatGarbler
# Compiled at: 2014-04-30 09:53:54
import string, random
from otp.otpbase import OTPLocalizer

class ChatGarbler:

    def garble(self, avatar, message):
        newMessage = ''
        numWords = random.randint(1, 7)
        wordlist = OTPLocalizer.ChatGarblerDefault
        for i in range(1, numWords + 1):
            wordIndex = random.randint(0, len(wordlist) - 1)
            newMessage = newMessage + wordlist[wordIndex]
            if i < numWords:
                newMessage = newMessage + ' '

        return newMessage

    def garbleSingle(self, avatar, message):
        newMessage = ''
        numWords = 1
        wordlist = OTPLocalizer.ChatGarblerDefault
        for i in range(1, numWords + 1):
            wordIndex = random.randint(0, len(wordlist) - 1)
            newMessage = newMessage + wordlist[wordIndex]
            if i < numWords:
                newMessage = newMessage + ' '

        return newMessage