# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.ai.ToontownAIMsgTypes
# Compiled at: 2014-04-30 09:53:54
from otp.ai.AIMsgTypes import *
TTAIMsgName2Id = {'DBSERVER_GET_ESTATE': 1040, 'DBSERVER_GET_ESTATE_RESP': 1041, 'PARTY_MANAGER_UD_TO_ALL_AI': 1042, 
   'IN_GAME_NEWS_MANAGER_UD_TO_ALL_AI': 1043, 
   'WHITELIST_MANAGER_UD_TO_ALL_AI': 1044}
TTAIMsgId2Names = invertDictLossless(TTAIMsgName2Id)
for name, value in TTAIMsgName2Id.items():
    exec '%s = %s' % (name, value)

del name
del value
DBSERVER_PET_OBJECT_TYPE = 5