# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.rpc.AwardManagerConsts
# Compiled at: 2014-04-30 09:53:54
GiveAwardErrors = Enum('Success, WrongGender, NotGiftable, FullMailbox, FullAwardMailbox, AlreadyInMailbox, AlreadyInGiftQueue, AlreadyInOrderedQueue, AlreadyInCloset, AlreadyBeingWorn, AlreadyInAwardMailbox, AlreadyInThirtyMinuteQueue, AlreadyInMyPhrases, AlreadyKnowDoodleTraining, AlreadyRented, GenericAlreadyHaveError, UnknownError, UnknownToon, NonToon,')
GiveAwardErrorStrings = {GiveAwardErrors.Success: 'success', GiveAwardErrors.WrongGender: 'wrong gender', 
   GiveAwardErrors.NotGiftable: 'item is not giftable', 
   GiveAwardErrors.FullMailbox: 'mailbox is full', 
   GiveAwardErrors.FullAwardMailbox: 'award mailbox is full', 
   GiveAwardErrors.AlreadyInMailbox: 'award already in mailbox.', 
   GiveAwardErrors.AlreadyInGiftQueue: 'award already in gift queue.', 
   GiveAwardErrors.AlreadyInOrderedQueue: 'award already in ordered queue.', 
   GiveAwardErrors.AlreadyInCloset: 'award already in closet.', 
   GiveAwardErrors.AlreadyBeingWorn: 'award already being worn.', 
   GiveAwardErrors.AlreadyInAwardMailbox: 'award already in award mailbox', 
   GiveAwardErrors.AlreadyInThirtyMinuteQueue: 'award already in 30 minute queue', 
   GiveAwardErrors.AlreadyInMyPhrases: 'speed chat award already in my phrases', 
   GiveAwardErrors.AlreadyKnowDoodleTraining: 'doodle training award already known', 
   GiveAwardErrors.AlreadyRented: 'award is already rented', 
   GiveAwardErrors.GenericAlreadyHaveError: 'generic-already-have error', 
   GiveAwardErrors.UnknownError: 'unknown error', 
   GiveAwardErrors.UnknownToon: 'toon not in database', 
   GiveAwardErrors.NonToon: 'this is not a toon'}