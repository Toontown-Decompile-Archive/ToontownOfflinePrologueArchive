# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: build.NiraiStart
# Compiled at: 2014-04-30 09:53:54
from panda3d.core import *
import __builtin__, os, aes, niraidata
prc = niraidata.CONFIG
iv, key, prc = prc[:16], prc[16:32], prc[32:]
prc = aes.decrypt(prc, key, iv)
for line in prc.split('\n'):
    line = line.strip()
    if line:
        loadPrcFileData('nirai config', line)

del prc
del iv
del key
__builtin__.dcStream = StringStream()
dc = niraidata.DC
iv, key, dc = dc[:16], dc[16:32], dc[32:]
dc = aes.decrypt(dc, key, iv)
dcStream.setData(dc)
del dc
del iv
del key

def getValue(key, default=None):
    return os.environ.get(key, default)


if getValue('IS_UD') == 'TRUE':
    import toontown.uberdog.ServiceStart
elif getValue('IS_AI') == 'TRUE':
    import toontown.ai.ServiceStart
else:
    import toontown.toonbase.ToontownStart