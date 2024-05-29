# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.uberdog.DistributedDeliveryManager
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.distributed.DistributedObject import DistributedObject
from toontown.catalog import CatalogItemList
from toontown.catalog import CatalogItem

class DistributedDeliveryManager(DistributedObject):
    neverDisable = 1

    def sendHello(self, message):
        self.sendUpdate('hello', [message])

    def rejectHello(self, message):
        print 'rejected', message

    def helloResponse(self, message):
        print 'accepted', message

    def sendAck(self):
        self.sendUpdate('requestAck', [])

    def returnAck(self):
        messenger.send('DeliveryManagerAck')

    def test(self):
        print 'Distributed Delviery Manager Stub Test'