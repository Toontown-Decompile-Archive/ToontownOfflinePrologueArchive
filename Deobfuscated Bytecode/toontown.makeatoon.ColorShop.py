# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.makeatoon.ColorShop
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from toontown.toon import ToonDNA
from direct.fsm import StateData
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from MakeAToonGlobals import *
from toontown.toonbase import TTLocalizer
import ShuffleButton
from random import random, choice
from direct.directnotify import DirectNotifyGlobal

class ColorShop(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('ColorShop')

    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.toon = None
        return

    def getGenderColorList(self, dna):
        if self.dna.getGender() == 'm':
            return ToonDNA.defaultBoyColorList
        else:
            return ToonDNA.defaultGirlColorList

    def enter(self, toon, shopsVisited=[]):
        base.disableMouse()
        self.toon = toon
        self.dna = toon.getStyle()
        colorList = self.getGenderColorList(self.dna)
        try:
            self.headChoice = colorList.index(self.dna.headColor)
            self.armChoice = colorList.index(self.dna.armColor)
            self.legChoice = colorList.index(self.dna.legColor)
            self.gloveChoice = colorList.index(self.dna.legColor)
        except:
            self.headChoice = choice(colorList)
            self.armChoice = choice(colorList)
            self.legChoice = choice(colorList)
            self.gloveChoice = choice(colorList)
            self.__swapHeadColor(0)
            self.__swapArmColor(0)
            self.__swapLegColor(0)
            self.__swapGloveColor(0)

        self.startColor = 0
        self.acceptOnce('last', self.__handleBackward)
        self.acceptOnce('next', self.__handleForward)
        choicePool = [colorList, colorList, colorList]
        self.shuffleButton.setChoicePool(choicePool)
        self.accept(self.shuffleFetchMsg, self.changeColor)
        self.acceptOnce('MAT-newToonCreated', self.shuffleButton.cleanHistory)

    def showButtons(self):
        self.parentFrame.show()

    def hideButtons(self):
        self.parentFrame.hide()

    def exit(self):
        self.ignore('last')
        self.ignore('next')
        self.ignore('enter')
        self.ignore(self.shuffleFetchMsg)
        try:
            del self.toon
        except:
            print 'ColorShop: toon not found'

        self.hideButtons()

    def load(self):
        self.gui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui')
        guiRArrowUp = self.gui.find('**/tt_t_gui_mat_arrowUp')
        guiRArrowRollover = self.gui.find('**/tt_t_gui_mat_arrowUp')
        guiRArrowDown = self.gui.find('**/tt_t_gui_mat_arrowDown')
        guiRArrowDisabled = self.gui.find('**/tt_t_gui_mat_arrowDisabled')
        shuffleFrame = self.gui.find('**/tt_t_gui_mat_shuffleFrame')
        shuffleArrowUp = self.gui.find('**/tt_t_gui_mat_shuffleArrowUp')
        shuffleArrowDown = self.gui.find('**/tt_t_gui_mat_shuffleArrowDown')
        shuffleArrowRollover = self.gui.find('**/tt_t_gui_mat_shuffleArrowUp')
        shuffleArrowDisabled = self.gui.find('**/tt_t_gui_mat_shuffleArrowDisabled')
        self.parentFrame = DirectFrame(relief=DGG.RAISED, pos=(0.98, 0, 0.416), frameColor=(1,
                                                                                            0,
                                                                                            0,
                                                                                            0))
        self.parentFrame.setPos(-0.354, 0, -0.585)
        self.parentFrame.reparentTo(base.a2dTopRight)
        self.toonFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=halfButtonInvertScale, relief=None, pos=(0,
                                                                                                                                       0,
                                                                                                                                       -0.0025), hpr=(0,
                                                                                                                                                      0,
                                                                                                                                                      0), scale=1.3, frameColor=(1,
                                                                                                                                                                                 1,
                                                                                                                                                                                 1,
                                                                                                                                                                                 1), text=TTLocalizer.ColorShopToon, text_scale=TTLocalizer.CStoonFrame, text_pos=(-0.001,
                                                                                                                                                                                                                                                                   -0.015), text_fg=(1,
                                                                                                                                                                                                                                                                                     1,
                                                                                                                                                                                                                                                                                     1,
                                                                                                                                                                                                                                                                                     1))
        self.allLButton = DirectButton(parent=self.toonFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2,
                                                                                                                                        0,
                                                                                                                                        0), command=self.__swapAllColor, extraArgs=[-1])
        self.allRButton = DirectButton(parent=self.toonFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2,
                                                                                                                                                          0,
                                                                                                                                                          0), command=self.__swapAllColor, extraArgs=[1])
        self.headFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=halfButtonInvertScale, relief=None, pos=(0,
                                                                                                                                       0,
                                                                                                                                       -0.22), hpr=(0,
                                                                                                                                                    0,
                                                                                                                                                    -2), scale=0.9, frameColor=(1,
                                                                                                                                                                                1,
                                                                                                                                                                                1,
                                                                                                                                                                                1), text=TTLocalizer.ColorShopHead, text_scale=0.0625, text_pos=(-0.001,
                                                                                                                                                                                                                                                 -0.015), text_fg=(1,
                                                                                                                                                                                                                                                                   1,
                                                                                                                                                                                                                                                                   1,
                                                                                                                                                                                                                                                                   1))
        self.headLButton = DirectButton(parent=self.headFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2,
                                                                                                                                        0,
                                                                                                                                        0), command=self.__swapHeadColor, extraArgs=[-1])
        self.headRButton = DirectButton(parent=self.headFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2,
                                                                                                                                                          0,
                                                                                                                                                          0), command=self.__swapHeadColor, extraArgs=[1])
        self.bodyFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=halfButtonScale, relief=None, pos=(0,
                                                                                                                                 0,
                                                                                                                                 -0.42), hpr=(0,
                                                                                                                                              0,
                                                                                                                                              2), scale=0.9, frameColor=(1,
                                                                                                                                                                         1,
                                                                                                                                                                         1,
                                                                                                                                                                         1), text=TTLocalizer.ColorShopBody, text_scale=0.0625, text_pos=(-0.001,
                                                                                                                                                                                                                                          -0.015), text_fg=(1,
                                                                                                                                                                                                                                                            1,
                                                                                                                                                                                                                                                            1,
                                                                                                                                                                                                                                                            1))
        self.armLButton = DirectButton(parent=self.bodyFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2,
                                                                                                                                        0,
                                                                                                                                        0), command=self.__swapArmColor, extraArgs=[-1])
        self.armRButton = DirectButton(parent=self.bodyFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2,
                                                                                                                                                          0,
                                                                                                                                                          0), command=self.__swapArmColor, extraArgs=[1])
        self.legsFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=halfButtonInvertScale, relief=None, pos=(0,
                                                                                                                                       0,
                                                                                                                                       -0.62), hpr=(0,
                                                                                                                                                    0,
                                                                                                                                                    3), scale=0.9, frameColor=(1,
                                                                                                                                                                               1,
                                                                                                                                                                               1,
                                                                                                                                                                               1), text=TTLocalizer.ColorShopLegs, text_scale=0.0625, text_pos=(-0.001,
                                                                                                                                                                                                                                                -0.015), text_fg=(1,
                                                                                                                                                                                                                                                                  1,
                                                                                                                                                                                                                                                                  1,
                                                                                                                                                                                                                                                                  1))
        self.legLButton = DirectButton(parent=self.legsFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2,
                                                                                                                                        0,
                                                                                                                                        0), command=self.__swapLegColor, extraArgs=[-1])
        self.legRButton = DirectButton(parent=self.legsFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2,
                                                                                                                                                          0,
                                                                                                                                                          0), command=self.__swapLegColor, extraArgs=[1])
        self.glovesFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=halfButtonInvertScale, relief=None, pos=(0,
                                                                                                                                         0,
                                                                                                                                         -0.82), hpr=(0,
                                                                                                                                                      0,
                                                                                                                                                      3), scale=0.9, frameColor=(1,
                                                                                                                                                                                 1,
                                                                                                                                                                                 1,
                                                                                                                                                                                 1), text=TTLocalizer.ColorShopGloves, text_scale=0.0625, text_pos=(-0.001,
                                                                                                                                                                                                                                                    -0.015), text_fg=(1,
                                                                                                                                                                                                                                                                      1,
                                                                                                                                                                                                                                                                      1,
                                                                                                                                                                                                                                                                      1))
        self.gloveLButton = DirectButton(parent=self.glovesFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2,
                                                                                                                                        0,
                                                                                                                                        0), command=self.__swapGloveColor, extraArgs=[-1])
        self.gloveRButton = DirectButton(parent=self.glovesFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2,
                                                                                                                                                          0,
                                                                                                                                                          0), command=self.__swapGloveColor, extraArgs=[1])
        self.parentFrame.hide()
        self.shuffleFetchMsg = 'ColorShopShuffle'
        self.shuffleButton = ShuffleButton.ShuffleButton(self, self.shuffleFetchMsg)
        return

    def unload(self):
        self.gui.removeNode()
        del self.gui
        self.parentFrame.destroy()
        self.toonFrame.destroy()
        self.headFrame.destroy()
        self.bodyFrame.destroy()
        self.legsFrame.destroy()
        self.glovesFrame.destroy()
        self.headLButton.destroy()
        self.headRButton.destroy()
        self.armLButton.destroy()
        self.armRButton.destroy()
        self.legLButton.destroy()
        self.legRButton.destroy()
        self.gloveLButton.destroy()
        self.gloveRButton.destroy()
        self.allLButton.destroy()
        self.allRButton.destroy()
        del self.parentFrame
        del self.toonFrame
        del self.headFrame
        del self.bodyFrame
        del self.legsFrame
        del self.glovesFrame
        del self.headLButton
        del self.headRButton
        del self.armLButton
        del self.armRButton
        del self.legLButton
        del self.legRButton
        del self.gloveLButton
        del self.gloveRButton
        del self.allLButton
        del self.allRButton
        self.shuffleButton.unload()
        self.ignore('MAT-newToonCreated')

    def __swapAllColor(self, offset):
        colorList = self.getGenderColorList(self.dna)
        length = len(colorList)
        choice = (self.headChoice + offset) % length
        self.__updateScrollButtons(choice, length, self.allLButton, self.allRButton)
        self.__swapHeadColor(offset)
        oldArmColorIndex = colorList.index(self.toon.style.armColor)
        oldLegColorIndex = colorList.index(self.toon.style.legColor)
        self.__swapArmColor(choice - oldArmColorIndex)
        self.__swapLegColor(choice - oldLegColorIndex)

    def __swapHeadColor(self, offset):
        colorList = self.getGenderColorList(self.dna)
        length = len(colorList)
        self.headChoice = (self.headChoice + offset) % length
        self.__updateScrollButtons(self.headChoice, length, self.headLButton, self.headRButton)
        newColor = colorList[self.headChoice]
        self.dna.headColor = newColor
        self.toon.swapToonColor(self.dna)

    def __swapArmColor(self, offset):
        colorList = self.getGenderColorList(self.dna)
        length = len(colorList)
        self.armChoice = (self.armChoice + offset) % length
        self.__updateScrollButtons(self.armChoice, length, self.armLButton, self.armRButton)
        newColor = colorList[self.armChoice]
        self.dna.armColor = newColor
        self.toon.swapToonColor(self.dna)

    def __swapLegColor(self, offset):
        colorList = self.getGenderColorList(self.dna)
        length = len(colorList)
        self.legChoice = (self.legChoice + offset) % length
        self.__updateScrollButtons(self.legChoice, length, self.legLButton, self.legRButton)
        newColor = colorList[self.legChoice]
        self.dna.legColor = newColor
        self.toon.swapToonColor(self.dna)

    def __swapGloveColor(self, offset):
        colorList = self.getGenderColorList(self.dna)
        length = len(colorList)
        self.gloveChoice = (self.gloveChoice + offset) % length
        self.__updateScrollButtons(self.gloveChoice, length, self.gloveLButton, self.gloveRButton)
        newColor = colorList[self.gloveChoice]
        self.dna.gloveColor = newColor
        self.toon.swapToonColor(self.dna)

    def __updateScrollButtons(self, choice, length, lButton, rButton):
        if choice == (self.startColor - 1) % length:
            rButton['state'] = DGG.DISABLED
        else:
            rButton['state'] = DGG.NORMAL
        if choice == self.startColor % length:
            lButton['state'] = DGG.DISABLED
        else:
            lButton['state'] = DGG.NORMAL

    def __handleForward(self):
        self.doneStatus = 'next'
        messenger.send(self.doneEvent)

    def __handleBackward(self):
        self.doneStatus = 'last'
        messenger.send(self.doneEvent)

    def changeColor(self):
        self.notify.debug('Entering changeColor')
        colorList = self.getGenderColorList(self.dna)
        newChoice = self.shuffleButton.getCurrChoice()
        newHeadColorIndex = colorList.index(newChoice[0])
        newArmColorIndex = colorList.index(newChoice[1])
        newLegColorIndex = colorList.index(newChoice[2])
        oldHeadColorIndex = colorList.index(self.toon.style.headColor)
        oldArmColorIndex = colorList.index(self.toon.style.armColor)
        oldLegColorIndex = colorList.index(self.toon.style.legColor)
        self.__swapHeadColor(newHeadColorIndex - oldHeadColorIndex)
        if config.GetBool('want-shuffle-colors', 1) and random() <= 0.4:
            self.__swapArmColor(newArmColorIndex - oldArmColorIndex)
            self.__swapLegColor(newLegColorIndex - oldLegColorIndex)
        else:
            self.__swapArmColor(newHeadColorIndex - oldArmColorIndex)
            self.__swapLegColor(newHeadColorIndex - oldLegColorIndex)

    def getCurrToonSetting(self):
        return [self.dna.headColor, self.dna.armColor, self.dna.legColor, self.dna.gloveColor]