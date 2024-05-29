# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.reborn.DistributedSafezoneInvasionRebornAI
# Compiled at: 2014-04-30 09:53:54
import random
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.fsm.FSM import FSM
from otp.ai.MagicWordGlobal import *
from toontown.election.DistributedInvasionSuitAI import DistributedInvasionSuitAI
from toontown.election.InvasionMasterAI import InvasionMasterAI
import SafezoneInvasionRebornGlobals, DistributedInterimElectionEventAI
from toontown.electionsuit import SuitTimings
from toontown.toonbase import ToontownBattleGlobals

class DistributedSafezoneInvasionRebornAI(DistributedObjectAI, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSafezoneInvasionRebornAI')

    def __init__(self, air, election):
        DistributedObjectAI.__init__(self, air)
        FSM.__init__(self, 'InvasionFSM')
        self.master = InvasionMasterAI(self)
        self.election = election
        self.waveNumber = 0
        self.spawnPoints = []
        self.suits = []
        self.toons = []
        self.sadToons = []
        self.lastWave = self.waveNumber == len(SafezoneInvasionRebornGlobals.SuitWaves) - 1
        self.invasionOn = False
        self.numberOfSuits = 0

    def announceGenerate(self):
        self.b_setInvasionStarted(True)
        self.demand('BeginWave', 0)
        for toon in self.air.doId2do.values():
            if toon.zoneId != self.zoneId:
                continue
            if toon.dclass != self.air.dclassesByName['DistributedToonAI']:
                continue
            self._handleToonEnter(toon)

        self.accept('toon-entered-%s' % self.zoneId, self._handleToonEnter)
        self.accept('toon-left-%s' % self.zoneId, self._handleToonExit)

    def b_setInvasionStarted(self, started):
        self.setInvasionStarted(started)
        self.d_setInvasionStarted(started)

    def setInvasionStarted(self, started):
        self.invasionOn = started

    def d_setInvasionStarted(self, started):
        self.sendUpdate('setInvasionStarted', [started])

    def getInvasionStarted(self):
        return self.invasionOn

    def delete(self):
        DistributedObjectAI.delete(self)
        self.demand('Off')
        self.ignoreAll()

    def enterBeginWave(self, waveNumber):
        self.waveNumber = waveNumber
        self.spawnPoints = range(len(SafezoneInvasionRebornGlobals.SuitSpawnPoints))
        suitsToCall = SafezoneInvasionRebornGlobals.SuitWaves[self.waveNumber]
        self.numberOfSuits = len(suitsToCall)
        delay = max(SafezoneInvasionRebornGlobals.WaveBeginningTime, SuitTimings.fromSky)
        spread = delay - SuitTimings.fromSky
        spreadPerSuit = spread / len(suitsToCall)
        self._waveBeginTasks = []
        for i, (suit, level) in enumerate(suitsToCall):
            self._waveBeginTasks.append(taskMgr.doMethodLater(i * spreadPerSuit, self.spawnOne, self.uniqueName('summon-suit-%s' % i), extraArgs=[
             suit, level]))

        self._waveBeginTasks.append(taskMgr.doMethodLater(delay, self.demand, self.uniqueName('begin-wave'), extraArgs=[
         'Wave']))

    def exitBeginWave(self):
        for task in self._waveBeginTasks:
            task.remove()

        self.spawnPoints = range(len(SafezoneInvasionRebornGlobals.SuitSpawnPoints))

    def enterWave(self):
        for suit in self.suits:
            suit.start()

        if self.lastWave:
            return
        if self.waveNumber not in SafezoneInvasionRebornGlobals.SuitIntermissionWaves and self.waveNumber not in SafezoneInvasionRebornGlobals.SuitWaitWaves:
            self.spawnPoints = range(len(SafezoneInvasionRebornGlobals.SuitSpawnPoints))
            self.demand('BeginWave', self.waveNumber + 1)
            self.lastWave = self.waveNumber == len(SafezoneInvasionRebornGlobals.SuitWaves) - 1
        if self.suits:
            self.suits[0].d_sayFaceoffTaunt()

    def exitWave(self):
        if self.waveNumber in SafezoneInvasionRebornGlobals.SuitIntermissionWaves or self.waveNumber in SafezoneInvasionRebornGlobals.SuitWaitWaves:
            self.__deleteSuits()

    def waveWon(self):
        if self.state != 'Wave':
            return
        if self.lastWave:
            self.demand('Finale')
        elif self.waveNumber in SafezoneInvasionRebornGlobals.SuitWaitWaves:
            self.demand('BeginWave', self.waveNumber + 1)
            self.lastWave = self.waveNumber == len(SafezoneInvasionRebornGlobals.SuitWaves) - 1
        else:
            self.demand('Intermission')

    def enterIntermission(self):
        self._delay = taskMgr.doMethodLater(SafezoneInvasionRebornGlobals.IntermissionTime, self.__endIntermission, self.uniqueName('intermission'))
        self.election.saySurleePhrase(random.choice[("You got them, but that's only one wave. We don't have time to mess around, here come some more!",
                                                     'Agh! More Cogs are flying in!',
                                                     'Yet more Cogs are coming in... Toons are dropping like flies...',
                                                     "We're losing Toons, but we must stay resolute. Fight for our town!")], 1, True)

    def __endIntermission(self, task):
        self.demand('BeginWave', self.waveNumber + 1)
        self.lastWave = self.waveNumber == len(SafezoneInvasionRebornGlobals.SuitWaves) - 1

    def exitIntermission(self):
        self._delay.remove()

    def enterFinale(self):
        self._delay = taskMgr.doMethodLater(3, self.spawnFinaleSuit, self.uniqueName('summon-finale-suit'))

    def spawnFinaleSuit(self, task):
        self.election.saySurleePhrase("Uh oh, they're sending in the boss!", 1, True)
        suit = DistributedInvasionSuitAI(self.air, self)
        suit.dna.newSuit('ls')
        suit.setSpawnPoint(101)
        suit.setLevel(4)
        suit.generateWithRequired(self.zoneId)
        suit.d_makeSkelecog()
        suit.b_setState('FlyDown')
        self.suits.append(suit)

    def setFinaleSuitStunned(self, hp, kill=False):
        if self.state == 'Finale' and kill:
            self.sendUpdate('stopMusic')
            for suit in self.suits:
                hp = min(hp, suit.currHP)
                suit.b_setHP(suit.currHP - hp)
                suit.b_setState('Stunned')

        elif self.state == 'Finale':
            for suit in self.suits:
                suit.takeDamage(hp)

    def winFinale(self):
        if self.state == 'Finale':
            for suit in self.suits:
                suit.b_setState('Explode')

    def exitFinale(self):
        self._delay.remove()

    def getToon(self, toonId):
        for toon in self.toons:
            if toon.doId == toonId:
                return toon

        return

    def _handleToonEnter(self, toon):
        if toon not in self.toons:
            self.toons.append(toon)
            self.acceptOnce(self.air.getAvatarExitEvent(toon.doId), self._handleToonExit, extraArgs=[
             toon])
            self.checkToonHp()
            toon.b_setHealthDisplay(2)

    def _handleToonExit(self, toon):
        if toon in self.toons:
            self.toons.remove(toon)
            self.ignore(self.air.getAvatarExitEvent(toon.doId))
        if toon in self.sadToons:
            self.sadToons.remove(toon)
            self.ignore(self.air.getAvatarExitEvent(toon.doId))
        toon.b_setHealthDisplay(0)

    def takeDamage(self, damage):
        avId = self.air.getAvatarIdFromSender()
        toon = self.air.doId2do.get(avId)
        if not toon:
            self.air.writeServerEvent('suspicious', avId, 'Nonexistent Toon tried to get hit!')
            return
        toonHp = toon.getHp()
        if damage > toonHp and toonHp > 0:
            toon.takeDamage(toonHp)
        else:
            toon.takeDamage(damage)
        self.checkToonHp()

    def pieHitToon(self, doId):
        avId = self.air.getAvatarIdFromSender()
        toon = self.air.doId2do.get(doId)
        if not toon:
            self.air.writeServerEvent('suspicious', avId, 'Hit a nonexistent Toon with a pie!')
            return
        from toontown.toon.DistributedToonAI import DistributedToonAI
        if not isinstance(toon, DistributedToonAI):
            self.air.writeServerEvent('suspicious', avId, 'Hit a non-Toon with a pie through healToon()!')
            return
        if toon.getHp() == -1:
            toon.setHp(0)
        toon.toonUp(SafezoneInvasionRebornGlobals.ToonHealAmount)
        self.checkToonHp()

    def checkToonHp(self):
        for toon in self.toons:
            if toon.getHp() < 0:
                if toon not in self.sadToons:
                    self.sadToons.append(toon)
                if toon in self.toons:
                    self.toons.remove(toon)

        for toon in self.sadToons:
            if toon.getHp() > 0:
                if toon in self.sadToons:
                    self.toons.append(toon)
                    self.sadToons.remove(toon)

    def spawnOne(self, suitType, levelOffset=0):
        if not self.spawnPoints:
            return
        pointId = random.choice(self.spawnPoints)
        self.spawnPoints.remove(pointId)
        suit = DistributedInvasionSuitAI(self.air, self)
        if suitType == 'vp':
            suit.dna.newBossCog('s')
            suit.generateWithRequired(self.zoneId)
        else:
            suit.dna.newSuit(suitType)
            suit.setSpawnPoint(pointId)
            suit.setLevel(levelOffset)
            suit.generateWithRequired(self.zoneId)
            whatKind = random.randrange(1, 6)
            if whatKind == 1:
                suit.d_makeSkelecog()
            elif whatKind == 2:
                suit.d_makeHolocog()
            elif whatKind == 3:
                suit.b_setSkeleRevives(1)
        suit.b_setState('FlyDown')
        self.suits.append(suit)

    def pieHitSuit(self, doId):
        avId = self.air.getAvatarIdFromSender()
        toon = self.air.doId2do.get(avId)
        if not toon:
            self.air.writeServerEvent('suspicious', avId, 'Nonexistent Toon tried to throw a pie!')
            return
        suit = self.air.doId2do.get(doId)
        if suit not in self.suits:
            return
        if toon.pieType == 7:
            suit.evidenceStun()
        else:
            pieDamageEntry = ToontownBattleGlobals.AvPropDamage[ToontownBattleGlobals.THROW_TRACK][toon.pieType]
            (pieDamage, pieGroupDamage), _ = pieDamageEntry
            suit.takeDamage(pieDamage)

    def __deleteSuits(self):
        for suit in self.suits:
            suit.requestDelete()

    def suitDied(self, suit):
        if self.state == 'Finale':
            self.suits.remove(suit)
            self.demand('Victory')
            return
        if suit not in self.suits:
            self.notify.warning('suitDied called twice for same suit!')
            return
        if self.waveNumber not in SafezoneInvasionRebornGlobals.SuitIntermissionWaves and self.numberOfSuits > 0:
            self.numberOfSuits = self.numberOfSuits - 1
            taskMgr.doMethodLater(1, self.spawnOne, self.uniqueName('summon-suit-%s' % self.numberOfSuits), extraArgs=[suit.getStyleName(), suit.getLevel()])
        self.suits.remove(suit)
        if not self.suits:
            self.waveWon()


@magicWord(category=CATEGORY_DEBUG, types=[str, str])
def szInvasionReborn(cmd, arg=''):
    if not simbase.config.GetBool('want-doomsday-reborn', False):
        return 'Doomsday is currently disabled.'
    else:
        if simbase.config.GetBool('want-doomsday', False):
            return 'The Election is active.'
        invasion = simbase.air.doFind('SafezoneInvasionReborn')
        if invasion is None and cmd != 'start':
            return 'No invasion has been created'
        if cmd == 'start':
            if invasion is None:
                election = simbase.air.doFind('InterimElectionEvent')
                if election is None:
                    return 'No election event.'
                invasion = DistributedSafezoneInvasionRebornAI(simbase.air, election)
                invasion.generateWithRequired(2000)
            else:
                return 'An invasion object already exists.'
        elif cmd == 'stop':
            invasion.b_setInvasionStarted(False)
            invasion.requestDelete()
        elif cmd == 'spawn':
            invasion.spawnOne(arg)
        elif cmd == 'wave':
            if arg == '5':
                return 'Skipping to wave 5 will cause an AI crash!'
            invasion.demand('BeginWave', int(arg))
        elif cmd == 'endWave':
            invasion.waveWon()
        elif cmd == 'stunFinaleSuit':
            invasion.setFinaleSuitStunned(200, True)
        elif cmd == 'winFinale':
            invasion.winFinale()
        return