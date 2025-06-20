# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.speedchat.SpeedChatGMHandler
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.showbase import DirectObject
from otp.otpbase import OTPLocalizer

class SpeedChatGMHandler(DirectObject.DirectObject):
    scStructure = None
    scList = {}

    def __init__(self):
        if SpeedChatGMHandler.scStructure is None:
            self.generateSCStructure()
        return

    def generateSCStructure(self):
        SpeedChatGMHandler.scStructure = [OTPLocalizer.PSCMenuGM]
        phraseCount = 0
        numGMCategories = config.GetInt('num-gm-categories', 0)
        for i in range(0, numGMCategories):
            categoryName = config.GetString('gm-category-%d' % i, '')
            if categoryName == '':
                continue
            categoryStructure = [
             categoryName]
            numCategoryPhrases = config.GetInt('gm-category-%d-phrases' % i, 0)
            for j in range(0, numCategoryPhrases):
                phrase = config.GetString('gm-category-%d-phrase-%d' % (i, j), '')
                if phrase != '':
                    idx = 'gm%d' % phraseCount
                    SpeedChatGMHandler.scList[idx] = phrase
                    categoryStructure.append(idx)
                    phraseCount += 1

            SpeedChatGMHandler.scStructure.append(categoryStructure)

        numGMPhrases = config.GetInt('num-gm-phrases', 0)
        for i in range(0, numGMPhrases):
            phrase = config.GetString('gm-phrase-%d' % i, '')
            if phrase != '':
                idx = 'gm%d' % phraseCount
                SpeedChatGMHandler.scList[idx] = phrase
                SpeedChatGMHandler.scStructure.append(idx)
                phraseCount += 1

    def getStructure(self):
        return SpeedChatGMHandler.scStructure

    def getPhrase(self, id):
        return SpeedChatGMHandler.scList[id]