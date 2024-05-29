# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.hood.HoodUtil
# Compiled at: 2014-04-30 09:53:54
from toontown.toonbase import ToontownGlobals

def calcPropType(node):
    propType = ToontownGlobals.AnimPropTypes.Unknown
    fullString = str(node)
    if 'hydrant' in fullString:
        propType = ToontownGlobals.AnimPropTypes.Hydrant
    elif 'trashcan' in fullString:
        propType = ToontownGlobals.AnimPropTypes.Trashcan
    elif 'mailbox' in fullString:
        propType = ToontownGlobals.AnimPropTypes.Mailbox
    return propType