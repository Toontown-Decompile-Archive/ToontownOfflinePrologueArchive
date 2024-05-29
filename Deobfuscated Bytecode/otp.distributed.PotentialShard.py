# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.distributed.PotentialShard
# Compiled at: 2014-04-30 09:53:54


class PotentialShard:

    def __init__(self, id):
        self.id = id
        self.name = None
        self.population = 0
        self.welcomeValleyPopulation = 0
        self.active = 1
        self.available = 1
        return