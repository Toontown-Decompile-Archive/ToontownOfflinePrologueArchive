# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.RingTrackGroup
# Compiled at: 2014-04-30 09:53:54


class RingTrackGroup:

    def __init__(self, tracks, period, trackTOffsets=None, reverseFlag=0, tOffset=0.0):
        if trackTOffsets == None:
            trackTOffsets = [
             0] * len(tracks)
        self.tracks = tracks
        self.period = period
        self.trackTOffsets = trackTOffsets
        self.reverseFlag = reverseFlag
        self.tOffset = tOffset
        return