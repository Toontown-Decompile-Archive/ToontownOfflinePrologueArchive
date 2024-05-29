# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.distributed.TelemetryLimited
# Compiled at: 2014-04-30 09:53:54


class TelemetryLimited:
    Sng = SerialNumGen()

    def __init__(self):
        self._telemetryLimiterId = self.Sng.next()
        self._limits = set()

    def getTelemetryLimiterId(self):
        return self._telemetryLimiterId

    def addTelemetryLimit(self, limit):
        self._limits.add(limit)

    def removeTelemetryLimit(self, limit):
        if limit in self._limits:
            self._limits.remove(limit)

    def enforceTelemetryLimits(self):
        for limit in self._limits:
            limit(self)