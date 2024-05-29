# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.MintProductPallet
# Compiled at: 2014-04-30 09:53:54
from toontown.toonbase.ToontownGlobals import *
from toontown.coghq import MintProduct

class MintProductPallet(MintProduct.MintProduct):
    Models = {CashbotMintIntA: 'phase_10/models/cashbotHQ/DoubleCoinStack', CashbotMintIntB: 'phase_10/models/cogHQ/DoubleMoneyStack', 
       CashbotMintIntC: 'phase_10/models/cashbotHQ/DoubleGoldStack'}
    Scales = {CashbotMintIntA: 1.0, CashbotMintIntB: 1.0, 
       CashbotMintIntC: 1.0}