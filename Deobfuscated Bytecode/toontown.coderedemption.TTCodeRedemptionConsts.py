# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coderedemption.TTCodeRedemptionConsts
# Compiled at: 2014-04-30 09:53:54
DefaultDbName = 'tt_code_redemption'
RedeemErrors = Enum('Success, CodeDoesntExist, CodeIsInactive, CodeAlreadyRedeemed, AwardCouldntBeGiven, TooManyAttempts, SystemUnavailable, ')
RedeemErrorStrings = {RedeemErrors.Success: 'Success', RedeemErrors.CodeDoesntExist: 'Invalid code', 
   RedeemErrors.CodeIsInactive: 'Code is inactive', 
   RedeemErrors.CodeAlreadyRedeemed: 'Code has already been redeemed', 
   RedeemErrors.AwardCouldntBeGiven: 'Award could not be given', 
   RedeemErrors.TooManyAttempts: 'Too many attempts, code ignored', 
   RedeemErrors.SystemUnavailable: 'Code redemption is currently unavailable'}
MaxCustomCodeLen = config.GetInt('tt-max-custom-code-len', 16)