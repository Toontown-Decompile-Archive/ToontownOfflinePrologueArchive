# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.shtiker.WordPage
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer
import ShtikerPage

class WordPage(ShtikerPage.ShtikerPage):
    notify = DirectNotifyGlobal.directNotify.newCategory('WordPage')

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.textRolloverColor = Vec4(1, 1, 0, 1)
        self.textDownColor = Vec4(0.5, 0.9, 1, 1)
        self.textDisabledColor = Vec4(0.4, 0.8, 0.4, 1)

    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        self.title = DirectLabel(parent=self, relief=None, text=TTLocalizer.WordPageTitle, text_scale=0.12, textMayChange=0, pos=(0,
                                                                                                                                  0,
                                                                                                                                  0.6))
        self.helpText = DirectLabel(parent=self, relief=None, text=TTLocalizer.WordPageHelp, text_scale=0.06, text_wordwrap=12, text_align=TextNode.ALeft, textMayChange=1, pos=(0.058,
                                                                                                                                                                                 0,
                                                                                                                                                                                 0.403))
        self.word1Desc = DirectLabel(parent=hidden, relief=None, text=TTLocalizer.MagicWordMaxDesc, text_align=TextNode.ALeft, text_scale=0.06, text_wordwrap=12, pos=(0.058,
                                                                                                                                                                       0,
                                                                                                                                                                       0))
        self.word1 = DirectButton(parent=self, relief=None, text=TTLocalizer.MagicWordMax, text_align=TextNode.ALeft, text_scale=0.05, text1_bg=self.textDownColor, text2_bg=self.textRolloverColor, text3_fg=self.textDisabledColor, textMayChange=0, command=self.showWordInfo, extraArgs=[0, self.word1Desc])
        self.word2Desc = DirectLabel(parent=hidden, relief=None, text=TTLocalizer.MagicWordTpDesc, text_align=TextNode.ALeft, text_scale=0.06, text_wordwrap=12, pos=(0.058,
                                                                                                                                                                      0,
                                                                                                                                                                      0))
        self.word2 = DirectButton(parent=self, relief=None, text=TTLocalizer.MagicWordTp, text_align=TextNode.ALeft, text_scale=0.05, text1_bg=self.textDownColor, text2_bg=self.textRolloverColor, text3_fg=self.textDisabledColor, textMayChange=0, command=self.showWordInfo, extraArgs=[1, self.word2Desc])
        self.word3Desc = DirectLabel(parent=hidden, relief=None, text=TTLocalizer.MagicWordMaxHpDesc, text_align=TextNode.ALeft, text_scale=0.06, text_wordwrap=12, pos=(0.058,
                                                                                                                                                                         0,
                                                                                                                                                                         0))
        self.word3 = DirectButton(parent=self, relief=None, text=TTLocalizer.MagicWordMaxHp, text_align=TextNode.ALeft, text_scale=0.05, text1_bg=self.textDownColor, text2_bg=self.textRolloverColor, text3_fg=self.textDisabledColor, textMayChange=0, command=self.showWordInfo, extraArgs=[2, self.word3Desc])
        self.word4Desc = DirectLabel(parent=hidden, relief=None, text=TTLocalizer.MagicWordHpDesc, text_align=TextNode.ALeft, text_scale=0.06, text_wordwrap=12, pos=(0.058,
                                                                                                                                                                      0,
                                                                                                                                                                      0))
        self.word4 = DirectButton(parent=self, relief=None, text=TTLocalizer.MagicWordHp, text_align=TextNode.ALeft, text_scale=0.05, text1_bg=self.textDownColor, text2_bg=self.textRolloverColor, text3_fg=self.textDisabledColor, textMayChange=0, command=self.showWordInfo, extraArgs=[3, self.word4Desc])
        self.word5Desc = DirectLabel(parent=hidden, relief=None, text=TTLocalizer.MagicWordFiresDesc, text_align=TextNode.ALeft, text_scale=0.06, text_wordwrap=12, pos=(0.058,
                                                                                                                                                                         0,
                                                                                                                                                                         0))
        self.word5 = DirectButton(parent=self, relief=None, text=TTLocalizer.MagicWordFires, text_align=TextNode.ALeft, text_scale=0.05, text1_bg=self.textDownColor, text2_bg=self.textRolloverColor, text3_fg=self.textDisabledColor, textMayChange=0, command=self.showWordInfo, extraArgs=[4, self.word5Desc])
        self.word6Desc = DirectLabel(parent=hidden, relief=None, text=TTLocalizer.MagicWordRebornDesc, text_align=TextNode.ALeft, text_scale=0.06, text_wordwrap=12, pos=(0.058,
                                                                                                                                                                          0,
                                                                                                                                                                          0))
        self.word6 = DirectButton(parent=self, relief=None, text=TTLocalizer.MagicWordReborn, text_align=TextNode.ALeft, text_scale=0.05, text1_bg=self.textDownColor, text2_bg=self.textRolloverColor, text3_fg=self.textDisabledColor, textMayChange=0, command=self.showWordInfo, extraArgs=[5, self.word6Desc])
        self.word7Desc = DirectLabel(parent=hidden, relief=None, text=TTLocalizer.MagicWordSewerDesc, text_align=TextNode.ALeft, text_scale=0.06, text_wordwrap=12, pos=(0.058,
                                                                                                                                                                         0,
                                                                                                                                                                         0))
        self.word7 = DirectButton(parent=self, relief=None, text=TTLocalizer.MagicWordSewer, text_align=TextNode.ALeft, text_scale=0.05, text1_bg=self.textDownColor, text2_bg=self.textRolloverColor, text3_fg=self.textDisabledColor, textMayChange=0, command=self.showWordInfo, extraArgs=[6, self.word7Desc])
        self.word8Desc = DirectLabel(parent=hidden, relief=None, text=TTLocalizer.MagicWordObstacleCourseDesc, text_align=TextNode.ALeft, text_scale=0.06, text_wordwrap=12, pos=(0.058,
                                                                                                                                                                                  0,
                                                                                                                                                                                  0))
        self.word8 = DirectButton(parent=self, relief=None, text=TTLocalizer.MagicWordObstacleCourse, text_align=TextNode.ALeft, text_scale=0.05, text1_bg=self.textDownColor, text2_bg=self.textRolloverColor, text3_fg=self.textDisabledColor, textMayChange=0, command=self.showWordInfo, extraArgs=[7, self.word8Desc])
        self.word9Desc = DirectLabel(parent=hidden, relief=None, text=TTLocalizer.MagicWordTreesDesc, text_align=TextNode.ALeft, text_scale=0.06, text_wordwrap=12, pos=(0.058,
                                                                                                                                                                         0,
                                                                                                                                                                         0))
        self.word9 = DirectButton(parent=self, relief=None, text=TTLocalizer.MagicWordTrees, text_align=TextNode.ALeft, text_scale=0.05, text1_bg=self.textDownColor, text2_bg=self.textRolloverColor, text3_fg=self.textDisabledColor, textMayChange=0, command=self.showWordInfo, extraArgs=[8, self.word9Desc])
        self.word10Desc = DirectLabel(parent=hidden, relief=None, text=TTLocalizer.MagicWordHarvestDesc, text_align=TextNode.ALeft, text_scale=0.06, text_wordwrap=12, pos=(0.058,
                                                                                                                                                                            0,
                                                                                                                                                                            0))
        self.word10 = DirectButton(parent=self, relief=None, text=TTLocalizer.MagicWordHarvest, text_align=TextNode.ALeft, text_scale=0.05, text1_bg=self.textDownColor, text2_bg=self.textRolloverColor, text3_fg=self.textDisabledColor, textMayChange=0, command=self.showWordInfo, extraArgs=[9, self.word10Desc])
        self.word11Desc = DirectLabel(parent=hidden, relief=None, text=TTLocalizer.MagicWordStartHolidayDesc, text_align=TextNode.ALeft, text_scale=0.06, text_wordwrap=12, pos=(0.058,
                                                                                                                                                                                 0,
                                                                                                                                                                                 0))
        self.word11 = DirectButton(parent=self, relief=None, text=TTLocalizer.MagicWordStartHoliday, text_align=TextNode.ALeft, text_scale=0.05, text1_bg=self.textDownColor, text2_bg=self.textRolloverColor, text3_fg=self.textDisabledColor, textMayChange=0, command=self.showWordInfo, extraArgs=[10, self.word11Desc])
        self.word12Desc = DirectLabel(parent=hidden, relief=None, text=TTLocalizer.MagicWordEndHolidayDesc, text_align=TextNode.ALeft, text_scale=0.06, text_wordwrap=12, pos=(0.058,
                                                                                                                                                                               0,
                                                                                                                                                                               0))
        self.word12 = DirectButton(parent=self, relief=None, text=TTLocalizer.MagicWordEndHoliday, text_align=TextNode.ALeft, text_scale=0.05, text1_bg=self.textDownColor, text2_bg=self.textRolloverColor, text3_fg=self.textDisabledColor, textMayChange=0, command=self.showWordInfo, extraArgs=[11, self.word12Desc])
        self.word13Desc = DirectLabel(parent=hidden, relief=None, text=TTLocalizer.MagicWordElectionDesc, text_align=TextNode.ALeft, text_scale=0.06, text_wordwrap=12, pos=(0.058,
                                                                                                                                                                             0,
                                                                                                                                                                             0))
        self.word13 = DirectButton(parent=self, relief=None, text=TTLocalizer.MagicWordElection, text_align=TextNode.ALeft, text_scale=0.05, text1_bg=self.textDownColor, text2_bg=self.textRolloverColor, text3_fg=self.textDisabledColor, textMayChange=0, command=self.showWordInfo, extraArgs=[12, self.word13Desc])
        self.word14Desc = DirectLabel(parent=hidden, relief=None, text=TTLocalizer.MagicWordHouseTypeDesc, text_align=TextNode.ALeft, text_scale=0.06, text_wordwrap=12, pos=(0.058,
                                                                                                                                                                              0,
                                                                                                                                                                              0))
        self.word14 = DirectButton(parent=self, relief=None, text=TTLocalizer.MagicWordHouseType, text_align=TextNode.ALeft, text_scale=0.05, text1_bg=self.textDownColor, text2_bg=self.textRolloverColor, text3_fg=self.textDisabledColor, textMayChange=0, command=self.showWordInfo, extraArgs=[13, self.word14Desc])
        self.word15Desc = DirectLabel(parent=hidden, relief=None, text=TTLocalizer.MagicWordGiveFishDesc, text_align=TextNode.ALeft, text_scale=0.06, text_wordwrap=12, pos=(0.058,
                                                                                                                                                                             0,
                                                                                                                                                                             0))
        self.word15 = DirectButton(parent=self, relief=None, text=TTLocalizer.MagicWordGiveFish, text_align=TextNode.ALeft, text_scale=0.05, text1_bg=self.textDownColor, text2_bg=self.textRolloverColor, text3_fg=self.textDisabledColor, textMayChange=0, command=self.showWordInfo, extraArgs=[14, self.word15Desc])
        self.word16Desc = DirectLabel(parent=hidden, relief=None, text=TTLocalizer.MagicWordRemoveFishRequestDesc, text_align=TextNode.ALeft, text_scale=0.06, text_wordwrap=12, pos=(0.058,
                                                                                                                                                                                      0,
                                                                                                                                                                                      0))
        self.word16 = DirectButton(parent=self, relief=None, text=TTLocalizer.MagicWordRemoveFishRequest, text_align=TextNode.ALeft, text_scale=0.05, text1_bg=self.textDownColor, text2_bg=self.textRolloverColor, text3_fg=self.textDisabledColor, textMayChange=0, command=self.showWordInfo, extraArgs=[15, self.word16Desc])
        self.words = [self.word1, self.word2, self.word3, self.word4, self.word5, self.word6, self.word7, self.word8, self.word9, self.word10, self.word11, self.word12, self.word13, self.word14, self.word15, self.word16]
        self.descriptions = [self.word1Desc, self.word2Desc, self.word3Desc, self.word4Desc, self.word5Desc, self.word6Desc, self.word7Desc, self.word8Desc, self.word9Desc, self.word10Desc, self.word11Desc, self.word12Desc, self.word13Desc, self.word14Desc, self.word15Desc, self.word16Desc]
        gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        self.scrollList = DirectScrolledList(parent=self, relief=None, forceHeight=0.07, pos=(-0.5,
                                                                                              0,
                                                                                              0), incButton_image=(gui.find('**/FndsLst_ScrollUp'),
         gui.find('**/FndsLst_ScrollDN'),
         gui.find('**/FndsLst_ScrollUp_Rllvr'),
         gui.find('**/FndsLst_ScrollUp')), incButton_relief=None, incButton_scale=(1.3,
                                                                                   1.3,
                                                                                   -1.3), incButton_pos=(0.08,
                                                                                                         0,
                                                                                                         -0.6), incButton_image3_color=Vec4(1, 1, 1, 0.2), decButton_image=(gui.find('**/FndsLst_ScrollUp'),
         gui.find('**/FndsLst_ScrollDN'),
         gui.find('**/FndsLst_ScrollUp_Rllvr'),
         gui.find('**/FndsLst_ScrollUp')), decButton_relief=None, decButton_scale=(1.3,
                                                                                   1.3,
                                                                                   1.3), decButton_pos=(0.08,
                                                                                                        0,
                                                                                                        0.52), decButton_image3_color=Vec4(1, 1, 1, 0.2), itemFrame_pos=(-0.237,
                                                                                                                                                                         0,
                                                                                                                                                                         0.41), itemFrame_scale=1.0, itemFrame_relief=DGG.SUNKEN, itemFrame_frameSize=(-0.05,
                                                                                                                                                                                                                                                       0.66,
                                                                                                                                                                                                                                                       -0.98,
                                                                                                                                                                                                                                                       0.07), itemFrame_frameColor=(0.85,
                                                                                                                                                                                                                                                                                    0.95,
                                                                                                                                                                                                                                                                                    1,
                                                                                                                                                                                                                                                                                    1), itemFrame_borderWidth=(0.01,
                                                                                                                                                                                                                                                                                                               0.01), numItemsVisible=14, items=[self.word1, self.word2, self.word3, self.word4, self.word5, self.word6, self.word7, self.word8, self.word9, self.word10, self.word11, self.word12, self.word13, self.word14, self.word15, self.word16])
        gui.removeNode()
        return

    def unload(self):
        ShtikerPage.ShtikerPage.unload(self)
        del self.title
        del self.helpText
        del self.word1Desc
        del self.word1
        del self.word2Desc
        del self.word2
        del self.word3Desc
        del self.word3
        del self.word4Desc
        del self.word4
        del self.word5Desc
        del self.word5
        del self.word6Desc
        del self.word6
        del self.word7Desc
        del self.word7
        del self.word8Desc
        del self.word8
        del self.word9Desc
        del self.word9
        del self.word10Desc
        del self.word10
        del self.word11Desc
        del self.word11
        del self.word12Desc
        del self.word12
        del self.word13Desc
        del self.word13
        del self.word14Desc
        del self.word14
        del self.word15Desc
        del self.word15
        del self.word16Desc
        del self.word16
        del self.words
        del self.descriptions
        self.scrollList.destroy()
        del self.scrollList

    def showWordInfo(self, wordNum, desc):
        for word in self.words:
            if word['state'] != DGG.NORMAL:
                word['state'] = DGG.NORMAL

        for description in self.descriptions:
            if description.getParent() != hidden:
                description.reparentTo(hidden)

        wordName = self.words[wordNum]
        wordName['state'] = DGG.DISABLED
        desc.reparentTo(self)