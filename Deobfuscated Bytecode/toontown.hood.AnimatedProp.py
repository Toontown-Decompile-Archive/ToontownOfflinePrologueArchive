# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.hood.AnimatedProp
# Compiled at: 2014-04-30 09:53:54
from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal

class AnimatedProp(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('AnimatedProp')

    def __init__(self, node):
        self.node = node

    def delete(self):
        pass

    def uniqueName(self, name):
        return name + '-' + str(self.node.this)

    def enter(self):
        self.notify.debug('enter')

    def exit(self):
        self.notify.debug('exit')