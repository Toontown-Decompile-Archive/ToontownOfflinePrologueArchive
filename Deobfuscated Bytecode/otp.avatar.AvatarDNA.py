# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.avatar.AvatarDNA
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import *
import random
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
notify = directNotify.newCategory('AvatarDNA')

class AvatarDNA:

    def __str__(self):
        return 'avatar parent class: type undefined'

    def makeNetString(self):
        notify.error('called makeNetString on avatarDNA parent class')

    def printNetString(self):
        string = self.makeNetString()
        dg = PyDatagram(string)
        dg.dumpHex(ostream)

    def makeFromNetString(self, string):
        notify.error('called makeFromNetString on avatarDNA parent class')

    def getType(self):
        notify.error('Invalid DNA type: ', self.type)
        return type