# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.TempMinigameAI
# Compiled at: 2014-04-30 09:53:54
from toontown.toonbase import ToontownGlobals
ALLOW_TEMP_MINIGAMES = config.GetBool('allow-temp-minigames', False)
TEMP_MG_ID_COUNTER = ToontownGlobals.TravelGameId - 1
TempMgCtors = {}

def _printMessage(message):
    print '\n\n!!!', message, '\n\n'


def _registerTempMinigame(name, Class, id, minPlayers=1, maxPlayers=4):
    if not ALLOW_TEMP_MINIGAMES:
        _printMessage('registerTempMinigame WARNING: allow-temp-minigames config is set to false, but we are trying to register temp minigame ' + name)
        import traceback
        traceback.print_stack()
        return
    ToontownGlobals.MinigameIDs += (id,)
    ToontownGlobals.MinigameNames[name] = id
    TempMgCtors[id] = Class
    for i in range(minPlayers, maxPlayers):
        ToontownGlobals.MinigamePlayerMatrix[i] += (id,)

    _printMessage('registerTempMinigame: ' + name)


if ALLOW_TEMP_MINIGAMES:
    pass