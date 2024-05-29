# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.cogdominium.CogdoFlyingInputManager
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import CollisionSphere, CollisionNode, BitMask32, CollisionHandlerEvent, CollisionRay
from toontown.minigame import ArrowKeys

class CogdoFlyingInputManager:

    def __init__(self):
        self.arrowKeys = ArrowKeys.ArrowKeys()
        self.arrowKeys.disable()

    def enable(self):
        self.arrowKeys.setPressHandlers([self.__upArrowPressed,
         self.__downArrowPressed,
         self.__leftArrowPressed,
         self.__rightArrowPressed,
         self.__controlPressed])
        self.arrowKeys.enable()

    def disable(self):
        self.arrowKeys.clearPressHandlers()
        self.arrowKeys.disable()

    def destroy(self):
        self.disable()
        self.arrowKeys.destroy()
        self.arrowKeys = None
        self.refuelLerp = None
        return

    def __upArrowPressed(self):
        pass

    def __downArrowPressed(self):
        pass

    def __leftArrowPressed(self):
        pass

    def __rightArrowPressed(self):
        pass

    def __controlPressed(self):
        pass