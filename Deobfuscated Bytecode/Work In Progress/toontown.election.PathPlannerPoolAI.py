# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.election.PathPlannerPoolAI
# Compiled at: 2014-04-30 09:53:54
import subprocess, os, atexit, thread
from panda3d.core import *

class PlanD:

    def __init__(self, pool):
        self.pool = pool
        pathPath = os.path.join(os.path.dirname(__file__), 'pathd.py')
        if not config.GetBool('want-doomsday', False) and os.name == 'nt':
            return
        else:
            self.sp = subprocess.Popen(pathPath, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            atexit.register(self.sp.kill)
            self.callback = None
            self.pool.addWorker(self)
            return

    def plan(self, callback, navFrom, navTo, radius):
        self.callback = callback
        params = (
         tuple(navFrom), tuple(navTo), radius)
        self.sp.stdin.write('%r\n' % (params,))
        self.sp.stdin.flush()
        thread.start_new_thread(self.__read, ())

    def __read(self):
        line = self.sp.stdout.readline()
        taskMgr.doMethodLater(0.1, self.__handle, 'inject-%d' % id(self), extraArgs=[
         line])

    def __handle(self, line):
        x = eval(line)
        if self.callback:
            self.callback(x)
        self.callback = None
        self.pool.addWorker(self)
        return


class PlanJob:

    def __init__(self, callback, navFrom, navTo, radius):
        self.callback = callback
        self.navFrom = navFrom
        self.navTo = navTo
        self.radius = radius

    def assign(self, pland):
        pland.plan(self.callback, self.navFrom, self.navTo, self.radius)


class PlannerPool:

    def __init__(self, workerCount):
        self.workers = []
        self.jobs = []
        for x in xrange(workerCount):
            PlanD(self)

    def addWorker(self, worker):
        self.workers.append(worker)
        self.__flushQueues()

    def addJob(self, job):
        self.jobs.append(job)
        self.__flushQueues()

    def __flushQueues(self):
        while self.workers and self.jobs:
            worker = self.workers.pop(0)
            job = self.jobs.pop(0)
            job.assign(worker)

    def plan(self, callback, navFrom, navTo, radius):
        job = PlanJob(callback, navFrom, navTo, radius)
        self.addJob(job)


pool = PlannerPool(simbase.config.GetInt('doomsday-threads', 0))