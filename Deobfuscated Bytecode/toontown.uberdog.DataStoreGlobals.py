# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.uberdog.DataStoreGlobals
# Compiled at: 2014-04-30 09:53:54
from toontown.uberdog.ScavengerHuntDataStore import *
from toontown.uberdog.DataStore import *
SH = 1
GEN = 2
TYPES = {SH: (ScavengerHuntDataStore,), GEN: (
       DataStore,)}

def getStoreClass(type):
    storeClass = TYPES.get(type, None)
    if storeClass:
        return storeClass[0]
    else:
        return