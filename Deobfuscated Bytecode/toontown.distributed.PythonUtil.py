# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.distributed.PythonUtil
# Compiled at: 2014-04-30 09:53:54
from panda3d.direct import get_config_showbase
import bisect, sys

class PriorityCallbacks:

    def __init__(self):
        self._callbacks = []

    def clear(self):
        while self._callbacks:
            self._callbacks.pop()

    def add(self, callback, priority=None):
        if priority is None:
            priority = 0
        item = (
         priority, callback)
        bisect.insort(self._callbacks, item)
        return item

    def remove(self, item):
        self._callbacks.pop(bisect.bisect_left(self._callbacks, item))

    def __call__(self):
        for priority, callback in self._callbacks:
            callback()


def clampScalar(value, a, b):
    if a < b:
        if value < a:
            return a
        else:
            if value > b:
                return b
            return value

    else:
        if value < b:
            return b
        else:
            if value > a:
                return a
            return value


def describeException(backTrace=4):

    def byteOffsetToLineno(code, byte):
        import array
        lnotab = array.array('B', code.co_lnotab)
        line = code.co_firstlineno
        for i in range(0, len(lnotab), 2):
            byte -= lnotab[i]
            if byte <= 0:
                return line
            line += lnotab[i + 1]

        return line

    infoArr = sys.exc_info()
    exception = infoArr[0]
    exceptionName = getattr(exception, '__name__', None)
    extraInfo = infoArr[1]
    trace = infoArr[2]
    stack = []
    while trace.tb_next:
        frame = trace.tb_frame
        module = frame.f_globals.get('__name__', None)
        lineno = byteOffsetToLineno(frame.f_code, frame.f_lasti)
        stack.append('%s:%s, ' % (module, lineno))
        trace = trace.tb_next

    frame = trace.tb_frame
    module = frame.f_globals.get('__name__', None)
    lineno = byteOffsetToLineno(frame.f_code, frame.f_lasti)
    stack.append('%s:%s, ' % (module, lineno))
    description = ''
    for i in range(len(stack) - 1, max(len(stack) - backTrace, 0) - 1, -1):
        description += stack[i]

    description += '%s: %s' % (exceptionName, extraInfo)
    return description


import __builtin__
__builtin__.describeException = describeException
__builtin__.config = get_config_showbase()