# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.FactoryUtil
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.showbase import DirectObject
from direct.interval.IntervalGlobal import *
from toontown.toonbase import ToontownGlobals
import MovingPlatform
from direct.task.Task import Task
from toontown.suit import Suit
from toontown.suit import SuitDNA

class Ouch(DirectObject.DirectObject):

    def __init__(self, keyEvent, callback):
        DirectObject.DirectObject.__init__(self)
        self.accept(keyEvent, callback)

    def destroy(self):
        self.ignoreAll()


class CyclePlacer(DirectObject.DirectObject):

    def __init__(self, locations, keyEvent, startIndex=0):
        DirectObject.DirectObject.__init__(self)
        self.locations = locations
        self.index = startIndex
        self.accept(keyEvent, self.gotoNextLocation)

    def destroy(self):
        self.locations = None
        self.ignoreAll()
        return

    def gotoNextLocation(self):
        self.index = (self.index + 1) % len(self.locations)
        self.gotoLocation()

    def gotoLocation(self, index=None):
        if index is None:
            index = self.index
        pos, h = self.locations[index]
        base.localAvatar.reparentTo(render)
        base.localAvatar.setPos(*pos)
        base.localAvatar.setH(h)
        return


class ToonLifter(DirectObject.DirectObject):
    SerialNum = 0

    def __init__(self, keyDownEvent, speed=2):
        DirectObject.DirectObject.__init__(self)
        self.serialNum = ToonLifter.SerialNum
        ToonLifter.SerialNum += 1
        self.taskName = 'ToonLifter%s' % self.serialNum
        self.keyDownEvent = keyDownEvent
        self.keyUpEvent = self.keyDownEvent + '-up'
        self.speed = speed
        self.accept(self.keyDownEvent, self.startLifting)

    def destroy(self):
        self.ignoreAll()
        taskMgr.remove(self.taskName)

    def startLifting(self):

        def liftTask(task, self=self):
            base.localAvatar.setZ(base.localAvatar.getZ() + self.speed)
            return Task.cont

        def stopLifting(self=self):
            taskMgr.remove(self.taskName)
            self.ignore(self.keyUpEvent)
            self.accept(self.keyDownEvent, self.startLifting)

        self.ignore(self.keyDownEvent)
        self.accept(self.keyUpEvent, stopLifting)
        taskMgr.add(liftTask, self.taskName)