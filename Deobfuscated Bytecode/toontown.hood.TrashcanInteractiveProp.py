# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.hood.TrashcanInteractiveProp
# Compiled at: 2014-04-30 09:53:54
from direct.actor import Actor
from direct.directnotify import DirectNotifyGlobal
from toontown.hood import InteractiveAnimatedProp
from toontown.hood import GenericAnimatedProp
from toontown.toonbase import ToontownGlobals, ToontownBattleGlobals, TTLocalizer

class TrashcanInteractiveProp(InteractiveAnimatedProp.InteractiveAnimatedProp):
    notify = DirectNotifyGlobal.directNotify.newCategory('TrashcanInteractiveProp')
    BattleCheerText = TTLocalizer.InteractivePropTrackBonusTerms[ToontownBattleGlobals.HEAL_TRACK]
    ZoneToIdles = {ToontownGlobals.ToontownCentral: (
                                       ('tt_a_ara_ttc_trashcan_idleTake2', 1, 1, None, 3, 10),
                                       ('tt_a_ara_ttc_trashcan_idleHiccup0', 1, 1, None, 3, 10),
                                       ('tt_a_ara_ttc_trashcan_idleLook1', 1, 1, None, 3, 10),
                                       ('tt_a_ara_ttc_trashcan_idleAwesome3', 1, 1, None, 3, 10)), 
       ToontownGlobals.DonaldsDock: (
                                   ('tt_a_ara_dod_trashcan_idleBounce2', 3, 10, 'tt_a_ara_dod_trashcan_idle0settle', 3,
 10),
                                   ('tt_a_ara_dod_trashcan_idle0', 1, 1, None, 3, 10),
                                   ('tt_a_ara_dod_trashcan_idle1', 1, 1, None, 3, 10),
                                   ('tt_a_ara_dod_trashcan_idleAwesome3', 1, 1, None, 3, 10)), 
       ToontownGlobals.DaisyGardens: (
                                    ('tt_a_ara_dga_trashcan_idleTake2', 1, 1, None, 3, 10),
                                    ('tt_a_ara_dga_trashcan_idleHiccup0', 1, 1, None, 3, 10),
                                    ('tt_a_ara_dga_trashcan_idleLook1', 1, 1, None, 3, 10),
                                    ('tt_a_ara_dga_trashcan_idleAwesome3', 1, 1, None, 3, 10)), 
       ToontownGlobals.MinniesMelodyland: (
                                         ('tt_a_ara_mml_trashcan_idleBounce0', 3, 10, 'tt_a_ara_mml_trashcan_idle0settle', 3,
 10),
                                         ('tt_a_ara_mml_trashcan_idleLook1', 1, 1, None, 3, 10),
                                         ('tt_a_ara_mml_trashcan_idleHelicopter2', 1, 1, None, 3, 10),
                                         ('tt_a_ara_mml_trashcan_idleAwesome3', 1, 1, None, 3, 10)), 
       ToontownGlobals.TheBrrrgh: (
                                 ('tt_a_ara_tbr_trashcan_idleShiver1', 1, 1, None, 3, 10),
                                 ('tt_a_ara_tbr_trashcan_idleSneeze2', 1, 1, None, 3, 10),
                                 ('tt_a_ara_tbr_trashcan_idle0', 1, 1, None, 3, 10),
                                 ('tt_a_ara_tbr_trashcan_idleAwesome3', 1, 1, None, 3, 10)), 
       ToontownGlobals.DonaldsDreamland: (
                                        ('tt_a_ara_ddl_trashcan_idleSleep0', 3, 10, None, 0, 0),
                                        ('tt_a_ara_ddl_trashcan_idleShake2', 1, 1, None, 0, 0),
                                        ('tt_a_ara_ddl_trashcan_idleSnore1', 1, 1, None, 0, 0),
                                        ('tt_a_ara_ddl_trashcan_idleAwesome3', 1, 1, None, 0, 0))}
    ZoneToIdleIntoFightAnims = {ToontownGlobals.ToontownCentral: 'tt_a_ara_ttc_trashcan_idleIntoFight', ToontownGlobals.DonaldsDock: 'tt_a_ara_dod_trashcan_idleIntoFight', 
       ToontownGlobals.DaisyGardens: 'tt_a_ara_dga_trashcan_idleIntoFight', 
       ToontownGlobals.MinniesMelodyland: 'tt_a_ara_mml_trashcan_idleIntoFight', 
       ToontownGlobals.TheBrrrgh: 'tt_a_ara_tbr_trashcan_idleIntoFight', 
       ToontownGlobals.DonaldsDreamland: 'tt_a_ara_ddl_trashcan_idleIntoFight'}
    ZoneToVictoryAnims = {ToontownGlobals.ToontownCentral: 'tt_a_ara_ttc_trashcan_victoryDance', ToontownGlobals.DonaldsDock: 'tt_a_ara_dod_trashcan_victoryDance', 
       ToontownGlobals.DaisyGardens: 'tt_a_ara_dga_trashcan_victoryDance', 
       ToontownGlobals.MinniesMelodyland: 'tt_a_ara_mml_trashcan_victoryDance', 
       ToontownGlobals.TheBrrrgh: 'tt_a_ara_tbr_trashcan_victoryDance', 
       ToontownGlobals.DonaldsDreamland: 'tt_a_ara_ddl_trashcan_victoryDance'}
    ZoneToSadAnims = {ToontownGlobals.ToontownCentral: 'tt_a_ara_ttc_trashcan_fightSad', ToontownGlobals.DonaldsDock: 'tt_a_ara_dod_trashcan_fightSad', 
       ToontownGlobals.DaisyGardens: 'tt_a_ara_dga_trashcan_fightSad', 
       ToontownGlobals.MinniesMelodyland: 'tt_a_ara_mml_trashcan_fightSad', 
       ToontownGlobals.TheBrrrgh: 'tt_a_ara_tbr_trashcan_fightSad', 
       ToontownGlobals.DonaldsDreamland: 'tt_a_ara_ddl_trashcan_fightSad'}
    ZoneToFightAnims = {ToontownGlobals.ToontownCentral: ('tt_a_ara_ttc_trashcan_fightBoost', 'tt_a_ara_ttc_trashcan_fightCheer', 'tt_a_ara_ttc_trashcan_fightIdle'), ToontownGlobals.DonaldsDock: ('tt_a_ara_dod_trashcan_fightBoost', 'tt_a_ara_dod_trashcan_fightCheer', 'tt_a_ara_dod_trashcan_fightIdle'), 
       ToontownGlobals.DaisyGardens: ('tt_a_ara_dga_trashcan_fightBoost', 'tt_a_ara_dga_trashcan_fightCheer', 'tt_a_ara_dga_trashcan_fightIdle'), 
       ToontownGlobals.MinniesMelodyland: ('tt_a_ara_mml_trashcan_fightBoost', 'tt_a_ara_mml_trashcan_fightCheer0', 'tt_a_ara_mml_trashcan_fightCheer1',
 'tt_a_ara_mml_trashcan_fightIdle'), 
       ToontownGlobals.TheBrrrgh: ('tt_a_ara_tbr_trashcan_fightBoost', 'tt_a_ara_tbr_trashcan_fightCheer', 'tt_a_ara_tbr_trashcan_fightIdle'), 
       ToontownGlobals.DonaldsDreamland: ('tt_a_ara_ddl_trashcan_fightBoost', 'tt_a_ara_ddl_trashcan_fightCheer', 'tt_a_ara_ddl_trashcan_fightIdle')}
    IdlePauseTime = config.GetFloat('prop-idle-pause-time', 0.0)

    def __init__(self, node):
        InteractiveAnimatedProp.InteractiveAnimatedProp.__init__(self, node, ToontownGlobals.TRASHCANS_BUFF_BATTLES)