# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.parties.DistributedPartyJukeboxActivityBaseAI
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from toontown.parties.DistributedPartyActivityAI import DistributedPartyActivityAI
from direct.task import Task
import PartyGlobals

class DistributedPartyJukeboxActivityBaseAI(DistributedPartyActivityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPartyJukeboxActivityBaseAI')

    def __init__(self, air, parent, activityTuple):
        DistributedPartyActivityAI.__init__(self, air, parent, activityTuple)
        self.music = PartyGlobals.PhaseToMusicData40
        self.queue = []
        self.owners = []
        self.currentToon = 0
        self.playing = False
        self.paused = False
        self.accept('fireworksStarted%i' % self.getPartyDoId(), self.handleFireworksStart)
        self.accept('fireworksFinished%i' % self.getPartyDoId(), self.handleFireworksEnd)

    def delete(self):
        taskMgr.remove('playSong%d' % self.doId)
        DistributedPartyActivityAI.delete(self)

    def setNextSong(self, song):
        avId = self.air.getAvatarIdFromSender()
        phase = self.music.get(song[0])
        if avId != self.currentToon:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Toon tried to set song without using the jukebox!')
        if not phase:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Toon supplied invalid phase for song!')
            return
        if not phase.has_key(song[1]):
            self.air.writeServerEvent('suspicious', avId=avId, issue='Toon supplied invalid song name!')
            return
        if avId in self.owners:
            self.queue[self.owners.index(avId)] = song
        else:
            self.queue.append(song)
            self.owners.append(avId)
        for toon in self.toonsPlaying:
            self.sendUpdateToAvatarId(toon, 'setSongInQueue', [song])

        if self.paused:
            return
        if not self.playing:
            self.d_setSongPlaying([0, ''], 0)
            taskMgr.remove('playSong%d' % self.doId)
            self.__startPlaying()

    def __startPlaying(self):
        if self.paused:
            return
        if len(self.queue) == 0:
            self.d_setSongPlaying([13, 'party_original_theme.ogg'], 0)
            self.playing = False
            taskMgr.doMethodLater(56, self.__pause, 'playSong%d' % self.doId, extraArgs=[])
            return
        self.playing = True
        details = self.queue.pop(0)
        owner = self.owners.pop(0)
        songInfo = self.music[details[0]][details[1]]
        self.d_setSongPlaying(details, owner)
        taskMgr.doMethodLater(songInfo[1] * PartyGlobals.getMusicRepeatTimes(songInfo[1]), self.__pause, 'playSong%d' % self.doId, extraArgs=[])

    def __pause(self):
        self.d_setSongPlaying([0, ''], 0)
        taskMgr.doMethodLater(PartyGlobals.MUSIC_GAP, self.__startPlaying, 'playSong%d' % self.doId, extraArgs=[])

    def toonJoinRequest(self):
        avId = self.air.getAvatarIdFromSender()
        if self.currentToon:
            self.sendUpdateToAvatarId(avId, 'joinRequestDenied', [1])
            return
        self.currentToon = avId
        taskMgr.doMethodLater(PartyGlobals.JUKEBOX_TIMEOUT, self.__removeToon, 'removeToon%d', extraArgs=[])
        self.toonsPlaying.append(avId)
        self.updateToonsPlaying()

    def toonExitRequest(self):
        pass

    def toonExitDemand(self):
        avId = self.air.getAvatarIdFromSender()
        if avId != self.currentToon:
            return
        taskMgr.remove('removeToon%d' % self.doId)
        self.currentToon = 0
        self.toonsPlaying.remove(avId)
        self.updateToonsPlaying()

    def __removeToon(self):
        if not self.currentToon:
            return
        self.toonsPlaying.remove(self.currentToon)
        self.updateToonsPlaying()
        self.currentToon = 0

    def d_setSongPlaying(self, details, owner):
        self.sendUpdate('setSongPlaying', [details, owner])

    def queuedSongsRequest(self):
        avId = self.air.getAvatarIdFromSender()
        if avId in self.owners:
            index = self.owners.index(avId)
        else:
            index = -1
        self.sendUpdateToAvatarId(avId, 'queuedSongsResponse', [self.queue, index])

    def moveHostSongToTopRequest(self):
        avId = self.air.getAvatarIdFromSender()
        if avId != self.currentToon:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Toon tried to set song without using the jukebox!')
        host = self.air.doId2do[self.parent].hostId
        if avId != host:
            self.air.writeServerEvent('suspicious', avId=avId, issue="Toon tried to move the host's song to the top!")
            return
        if host not in self.owners:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Host tried to move non-existent song to the top of the queue!')
            return
        index = self.owners.index(host)
        self.owners.remove(host)
        song = self.queue.pop(index)
        self.owners.insert(0, host)
        self.queue.insert(0, song)
        for toon in self.toonsPlaying:
            self.sendUpdateToAvatarId(toon, 'moveHostSongToTop', [])

    def handleFireworksStart(self):
        taskMgr.remove('playSong%d' % self.doId)
        self.paused = True
        self.d_setSongPlaying([0, ''], 0)

    def handleFireworksEnd(self):
        self.paused = False
        self.__startPlaying()