# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.InGameEditorElements
# Compiled at: 2014-04-30 09:53:54
from direct.showbase import DirectObject

class InGameEditorElement(DirectObject.DirectObject):
    elementId = 0

    def __init__(self, children=[]):
        self.elementId = InGameEditorElement.elementId
        InGameEditorElement.elementId += 1
        self.setChildren(children)
        self.feName = self.getTypeName()

    def getName(self):
        return self.feName

    def setNewName(self, newName):
        self.feName = newName

    def getTypeName(self):
        return 'Level Element'

    def id(self):
        return self.elementId

    def getChildren(self):
        return self.children

    def setChildren(self, children):
        self.children = list(children)

    def addChild(self, child):
        self.children.append(child)

    def removeChild(self, child):
        self.children.remove(child)

    def getNumChildren(self):
        return len(self.children)