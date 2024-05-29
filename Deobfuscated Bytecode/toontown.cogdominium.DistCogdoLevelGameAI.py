# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.cogdominium.DistCogdoLevelGameAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from toontown.cogdominium.DistCogdoGameAI import DistCogdoGameAI
from otp.level.DistributedLevelAI import DistributedLevelAI

class DistCogdoLevelGameAI(DistCogdoGameAI, DistributedLevelAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistCogdoLevelGameAI')