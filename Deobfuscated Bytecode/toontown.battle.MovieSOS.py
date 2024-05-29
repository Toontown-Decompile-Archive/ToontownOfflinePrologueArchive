# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.battle.MovieSOS
# Compiled at: 2014-04-30 09:53:54
from direct.interval.IntervalGlobal import *
import MovieCamera
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer
from pandac.PandaModules import *
from otp.nametag.NametagConstants import *
from otp.nametag import NametagGlobals
notify = DirectNotifyGlobal.directNotify.newCategory('MovieSOS')

def doSOSs(calls):
    if len(calls) == 0:
        return (None, None)
    else:

        def callerFunc(toon, handle):
            toon.setChatAbsolute(TTLocalizer.MovieSOSCallHelp % handle.getName(), CFSpeech | CFTimeout)
            handle.d_battleSOS(base.localAvatar.doId)

        def calleeFunc(toon, handle):
            toon.setChatAbsolute(TTLocalizer.MovieSOSCallHelp % handle.getName(), CFSpeech | CFTimeout)

        def observerFunc(toon):
            toon.setChatAbsolute(TTLocalizer.MovieSOSObserverHelp, CFSpeech | CFTimeout)

        mtrack = Sequence()
        for c in calls:
            toon = c['toon']
            targetType = c['targetType']
            handle = c['target']
            mtrack.append(Wait(0.5))
            if targetType == 'observer':
                ival = Func(observerFunc, toon)
            elif targetType == 'caller':
                ival = Func(callerFunc, toon, handle)
            elif targetType == 'callee':
                ival = Func(calleeFunc, toon, handle)
            else:
                notify.error('invalid target type: %s' % targetType)
            mtrack.append(ival)
            mtrack.append(Wait(2.0))
            notify.debug('toon: %s calls for help' % toon.getName())

        camDuration = mtrack.getDuration()
        camTrack = MovieCamera.chooseSOSShot(toon, camDuration)
        return (mtrack, camTrack)