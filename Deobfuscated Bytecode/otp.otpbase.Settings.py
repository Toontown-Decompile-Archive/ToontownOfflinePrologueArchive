# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.otpbase.Settings
# Compiled at: 2014-04-30 09:53:54
import json

class Settings:

    def __init__(self):
        self.fileName = 'settings.json'
        try:
            with open(self.fileName, 'r') as (file):
                self.settings = json.load(file)
        except:
            self.settings = {}

    def updateSetting(self, type, attribute, value):
        with open(self.fileName, 'w+') as (file):
            if not self.settings.get(type):
                self.settings[type] = {}
            self.settings[type][attribute] = value
            json.dump(self.settings, file)

    def getOption(self, type, attribute, default):
        return self.settings.get(type, {}).get(attribute, default)

    def getString(self, type, attribute, default=''):
        value = self.getOption(type, attribute, default)
        if isinstance(value, basestring):
            return value
        else:
            return default

    def getInt(self, type, attribute, default=0):
        value = self.getOption(type, attribute, default)
        if isinstance(value, (int, long)):
            return int(value)
        else:
            return default

    def getBool(self, type, attribute, default=False):
        value = self.getOption(type, attribute, default)
        if isinstance(value, bool):
            return value
        else:
            return default

    def getList(self, type, attribute, default=[], expectedLength=2):
        value = self.getOption(type, attribute, default)
        if isinstance(value, list) and len(value) == expectedLength:
            return value
        else:
            return default