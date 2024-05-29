# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.otpbase.BackupManager
# Compiled at: 2014-04-30 09:53:54
import json, os

class BackupManager:

    def __init__(self, filepath='backups/', extension='.json'):
        self.filepath = filepath
        self.extension = extension

    def getFileName(self, category, info):
        filename = os.path.join(self.filepath, category) + '/'
        for i in info:
            filename += str(i) + '_'

        return filename[:-1] + self.extension

    def load(self, category, info, default=None):
        filename = self.getFileName(category, info)
        if not os.path.exists(filename):
            return default
        with open(filename, 'r') as (f):
            return json.load(f)

    def save(self, category, info, data):
        filepath = os.path.join(self.filepath, category)
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        filename = self.getFileName(category, info)
        with open(filename, 'w') as (f):
            json.dump(data, f)