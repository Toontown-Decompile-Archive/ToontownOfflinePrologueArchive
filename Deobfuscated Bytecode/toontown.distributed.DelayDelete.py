# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.distributed.DelayDelete
# Compiled at: 2014-04-30 09:53:54


class DelayDelete:

    def __init__(self, distObj, name):
        self._distObj = distObj
        self._name = name
        self._token = self._distObj.acquireDelayDelete(name)

    def getObject(self):
        return self._distObj

    def getName(self):
        return self._name

    def destroy(self):
        token = self._token
        del self._token
        self._distObj.releaseDelayDelete(token)
        del self._distObj
        del self._name


def cleanupDelayDeletes(interval):
    if hasattr(interval, 'delayDelete'):
        delayDelete = interval.delayDelete
        del interval.delayDelete
        if type(delayDelete) == type([]):
            for i in delayDelete:
                i.destroy()

        else:
            delayDelete.destroy()
    if hasattr(interval, 'delayDeletes'):
        delayDeletes = interval.delayDeletes
        del interval.delayDeletes
        if type(delayDeletes) == type([]):
            for i in delayDeletes:
                i.destroy()

        else:
            delayDeletes.destroy()