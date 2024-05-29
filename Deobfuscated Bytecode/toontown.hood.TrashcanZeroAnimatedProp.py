# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.hood.TrashcanZeroAnimatedProp
# Compiled at: 2014-04-30 09:53:54
from toontown.hood import ZeroAnimatedProp
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal

class TrashcanZeroAnimatedProp(ZeroAnimatedProp.ZeroAnimatedProp):
    notify = DirectNotifyGlobal.directNotify.newCategory('TrashcanZeroAnimatedProp')
    PauseTimeMult = config.GetFloat('zero-pause-mult', 1.0)
    PhaseInfo = {0: ('tt_a_ara_dga_trashcan_firstMoveLidFlip1', 40 * PauseTimeMult), 1: (
         'tt_a_ara_dga_trashcan_firstMoveStruggle', 20 * PauseTimeMult), 
       2: (
         'tt_a_ara_dga_trashcan_firstMoveLidFlip2', 10 * PauseTimeMult), 
       3: (
         'tt_a_ara_dga_trashcan_firstMoveJump', 8 * PauseTimeMult), 
       4: (
         'tt_a_ara_dga_trashcan_firstMoveLidFlip3', 6 * PauseTimeMult), 
       5: (
         'tt_a_ara_dga_trashcan_firstMoveJumpHit', 4 * PauseTimeMult), 
       6: (
         'tt_a_ara_dga_trashcan_firstMoveJumpJuggle', 2 * PauseTimeMult)}

    def __init__(self, node):
        ZeroAnimatedProp.ZeroAnimatedProp.__init__(self, node, 'trashcan', self.PhaseInfo, ToontownGlobals.TRASHCAN_ZERO_HOLIDAY)