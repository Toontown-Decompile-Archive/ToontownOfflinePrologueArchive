# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.dna.DNAParser
# Compiled at: 2014-04-30 09:53:54
from libpandadna import *

def loadDNAFile(dnaStorage, file):
    print 'Reading DNA file...', file
    dnaLoader = DNALoader()
    fileu = '/' + file
    node = dnaLoader.loadDNAFile(dnaStorage, fileu)
    if node.node().getNumChildren() > 0:
        return node.node()


def loadDNAFileAI(dnaStorage, file):
    dnaLoader = DNALoader()
    fileu = '/' + file
    data = dnaLoader.loadDNAFileAI(dnaStorage, fileu)
    return data


def setupDoor(a, b, c, d, e, f):
    try:
        e = int(str(e).split('_')[0])
    except:
        print 'setupDoor: error parsing', e
        e = 9999

    DNADoor.setupDoor(a, b, c, d, e, f)