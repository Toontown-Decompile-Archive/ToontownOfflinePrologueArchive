# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.level.EditorGlobals
# Compiled at: 2014-04-30 09:53:54
from direct.showbase.PythonUtil import uniqueElements
EditTargetPostName = 'inGameEditTarget'
EntIdRange = 10000
username2entIdBase = {'darren': 1 * EntIdRange, 'samir': 2 * EntIdRange, 
   'skyler': 3 * EntIdRange, 
   'joe': 4 * EntIdRange, 
   'DrEvil': 5 * EntIdRange, 
   'asad': 6 * EntIdRange, 
   'drose': 7 * EntIdRange, 
   'pappy': 8 * EntIdRange, 
   'patricia': 9 * EntIdRange, 
   'jloehrle': 10 * EntIdRange, 
   'rurbino': 11 * EntIdRange}
usernameConfigVar = 'level-edit-username'
undefinedUsername = 'UNDEFINED_USERNAME'
editUsername = config.GetString(usernameConfigVar, undefinedUsername)

def checkNotReadyToEdit():
    if editUsername == undefinedUsername:
        return "you must config '%s'; see %s.py" % (usernameConfigVar, __name__)
    else:
        if editUsername not in username2entIdBase:
            return "unknown editor username '%s'; see %s.py" % (editUsername, __name__)
        return


def assertReadyToEdit():
    msg = checkNotReadyToEdit()
    if msg is not None:
        pass
    return


def getEditUsername():
    return editUsername


def getEntIdAllocRange():
    baseId = username2entIdBase[editUsername]
    return [baseId, baseId + EntIdRange]