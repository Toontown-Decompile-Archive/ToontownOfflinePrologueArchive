# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.cogdominium.CogdoEntityTypes
# Compiled at: 2014-04-30 09:53:54
from otp.level.EntityTypes import *

class CogdoLevelMgr(LevelMgr):
    type = 'levelMgr'


class CogdoBoardroomGameSettings(Entity):
    type = 'cogdoBoardroomGameSettings'
    attribs = (('TimerScale', 1.0, 'float'), )


class CogdoCraneGameSettings(Entity):
    type = 'cogdoCraneGameSettings'
    attribs = (('GameDuration', 180.0, 'float'),
     ('EmptyFrictionCoef', 0.1, 'float'),
     ('Gravity', -32, 'int'),
     ('RopeLinkMass', 1.0, 'float'),
     ('MagnetMass', 1.0, 'float'),
     ('MoneyBagGrabHeight', -8.2, 'float'))


class CogdoCraneCogSettings(Entity):
    type = 'cogdoCraneCogSettings'
    attribs = (('CogSpawnPeriod', 10.0, 'float'),
     ('CogWalkSpeed', 2.0, 'float'),
     ('CogMachineInteractDuration', 2.0, 'float'),
     ('CogFlyAwayHeight', 50.0, 'float'),
     ('CogFlyAwayDuration', 4.0, 'float'))