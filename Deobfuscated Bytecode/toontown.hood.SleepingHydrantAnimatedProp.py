# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.hood.SleepingHydrantAnimatedProp
# Compiled at: 2014-04-30 09:53:54
import AnimatedProp
from direct.interval.IntervalGlobal import *
from direct.task import Task
import math

class SleepingHydrantAnimatedProp(AnimatedProp.AnimatedProp):

    def __init__(self, node):
        AnimatedProp.AnimatedProp.__init__(self, node)
        self.task = None
        return

    def bobTask(self, task):
        self.node.setSz(1.0 + 0.08 * math.sin(task.time))
        return Task.cont

    def enter(self):
        AnimatedProp.AnimatedProp.enter(self)
        self.task = taskMgr.add(self.bobTask, self.uniqueName('bobTask'))

    def exit(self):
        AnimatedProp.AnimatedProp.exit(self)
        if self.task:
            taskMgr.remove(self.task)
            self.task = None
        return