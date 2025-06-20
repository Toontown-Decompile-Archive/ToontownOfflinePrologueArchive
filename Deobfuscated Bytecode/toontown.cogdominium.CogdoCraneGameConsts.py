# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.cogdominium.CogdoCraneGameConsts
# Compiled at: 2014-04-30 09:53:54
from direct.fsm.StatePush import StateVar
from otp.level.EntityStateVarSet import EntityStateVarSet
from toontown.cogdominium.CogdoEntityTypes import CogdoCraneGameSettings, CogdoCraneCogSettings
Settings = EntityStateVarSet(CogdoCraneGameSettings)
CogSettings = EntityStateVarSet(CogdoCraneCogSettings)
CranePosHprs = [(13.4, -136.6, 6, -45, 0, 0),
 (13.4, -91.4, 6, -135, 0, 0),
 (58.6, -91.4, 6, 135, 0, 0),
 (58.6, -136.6, 6, 45, 0, 0)]
MoneyBagPosHprs = [
 [-6.799999999999997, 
  -128.3, 
  0, 
  -90, 
  0, 
  0],
 [
  -6.900000000000006, 
  -101.69999999999999, 
  0, 
  -90, 
  0, 
  0],
 [
  81.69999999999999, 
  -125.39999999999998, 
  0, 
  90, 
  0, 
  0],
 [
  81.5, 
  -101.39999999999998, 
  0, 
  90, 
  0, 
  0],
 [
  23.799999999999997, 
  -158.10000000000002, 
  0, 
  0, 
  0, 
  0],
 [
  49.900000000000006, 
  -158.10000000000002, 
  0, 
  0, 
  0, 
  0],
 [
  23.0, 
  -73.69999999999999, 
  0, 
  180, 
  0, 
  0],
 [
  50.19999999999999, 
  -73.69999999999999, 
  0, 
  180, 
  0, 
  0]]
for i in xrange(len(MoneyBagPosHprs)):
    MoneyBagPosHprs[i][2] += 6