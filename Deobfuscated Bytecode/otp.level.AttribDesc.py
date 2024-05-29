# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.level.AttribDesc
# Compiled at: 2014-04-30 09:53:54


class AttribDesc:

    def __init__(self, name, default, datatype='string', params={}):
        self.name = name
        self.default = default
        self.datatype = datatype
        self.params = params

    def getName(self):
        return self.name

    def getDefaultValue(self):
        return self.default

    def getDatatype(self):
        return self.datatype

    def getParams(self):
        return self.params

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'AttribDesc(%s, %s, %s, %s)' % (repr(self.name),
         repr(self.default),
         repr(self.datatype),
         repr(self.params))