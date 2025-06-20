# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.char.CharDNA
# Compiled at: 2014-04-30 09:53:54
import random
from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import *
import random
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from otp.avatar import AvatarDNA
notify = directNotify.newCategory('CharDNA')
charTypes = ['mk', 
 'vmk', 
 'mn', 
 'wmn', 
 'g', 
 'sg', 
 'd', 
 'fd', 
 'dw', 
 'p', 
 'wp', 
 'cl', 
 'dd', 
 'shdd', 
 'ch', 
 'da', 
 'pch', 
 'jda']

class CharDNA(AvatarDNA.AvatarDNA):

    def __init__(self, str=None, type=None, dna=None, r=None, b=None, g=None):
        if str != None:
            self.makeFromNetString(str)
        elif type != None:
            if type == 'c':
                self.newChar(dna)
        else:
            self.type = 'u'
        return

    def __str__(self):
        if self.type == 'c':
            return 'type = char, name = %s' % self.name
        else:
            return 'type undefined'

    def makeNetString(self):
        dg = PyDatagram()
        dg.addFixedString(self.type, 1)
        if self.type == 'c':
            dg.addFixedString(self.name, 2)
        elif self.type == 'u':
            notify.error('undefined avatar')
        else:
            notify.error('unknown avatar type: ', self.type)
        return dg.getMessage()

    def makeFromNetString(self, string):
        dg = PyDatagram(string)
        dgi = PyDatagramIterator(dg)
        self.type = dgi.getFixedString(1)
        if self.type == 'c':
            self.name = sgi.getFixedString(2)
        else:
            notify.error('unknown avatar type: ', self.type)
        return

    def __defaultChar(self):
        self.type = 'c'
        self.name = charTypes[0]

    def newChar(self, name=None):
        if name == None:
            self.__defaultChar()
        else:
            self.type = 'c'
            if name in charTypes:
                self.name = name
            else:
                notify.error('unknown avatar type: %s' % name)
        return

    def getType(self):
        if self.type == 'c':
            type = self.getCharName()
        else:
            notify.error('Invalid DNA type: ', self.type)
        return type

    def getCharName(self):
        if self.name == 'mk':
            return 'mickey'
        if self.name == 'vmk':
            return 'vampire_mickey'
        if self.name == 'mn':
            return 'minnie'
        if self.name == 'wmn':
            return 'witch_minnie'
        if self.name == 'g':
            return 'goofy'
        if self.name == 'sg':
            return 'super_goofy'
        if self.name == 'd':
            return 'donald'
        if self.name == 'dw':
            return 'donald-wheel'
        if self.name == 'fd':
            return 'franken_donald'
        if self.name == 'dd':
            return 'daisy'
        if self.name == 'shdd':
            return 'sockHop_daisy'
        if self.name == 'p':
            return 'pluto'
        if self.name == 'wp':
            return 'western_pluto'
        if self.name == 'cl':
            return 'clarabelle'
        if self.name == 'ch':
            return 'chip'
        if self.name == 'da':
            return 'dale'
        if self.name == 'pch':
            return 'police_chip'
        if self.name == 'jda':
            return 'jailbird_dale'
        notify.error('unknown char type: ', self.name)