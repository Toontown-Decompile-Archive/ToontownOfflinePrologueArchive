# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.cogdominium.CogdoInterior
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import ModelPool, TexturePool
from direct.task.Task import Task
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from toontown.hood import Place
from toontown.toonbase.ToonBaseGlobal import *
from toontown.town import TownBattle
from toontown.suit import Suit
from toontown.building import Elevator
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToontownBattleGlobals

class CogdoInterior(Place.Place):
    notify = DirectNotifyGlobal.directNotify.newCategory('CogdoInterior')

    def __init__(self, loader, parentFSM, doneEvent):
        Place.Place.__init__(self, loader, doneEvent)
        self.fsm = ClassicFSM.ClassicFSM('CogdoInterior', [State.State('entrance', self.enterEntrance, self.exitEntrance, ['Game', 'walk']),
         State.State('Elevator', self.enterElevator, self.exitElevator, ['Game',
          'battle',
          'walk',
          'crane']),
         State.State('Game', self.enterGame, self.exitGame, ['battle',
          'died',
          'crane',
          'walk']),
         State.State('battle', self.enterBattle, self.exitBattle, ['walk', 'died']),
         State.State('crane', self.enterCrane, self.exitCrane, ['walk', 
          'battle', 
          'finalBattle', 
          'died', 
          'ouch', 
          'squished']),
         State.State('walk', self.enterWalk, self.exitWalk, ['stickerBook', 
          'stopped', 
          'battle', 
          'sit', 
          'died', 
          'teleportOut', 
          'Elevator', 
          'crane', 
          'DFA', 
          'trialerFA']),
         State.State('sit', self.enterSit, self.exitSit, ['walk']),
         State.State('stickerBook', self.enterStickerBook, self.exitStickerBook, ['walk', 
          'stopped', 
          'sit', 
          'died', 
          'DFA', 
          'trialerFA', 
          'teleportOut', 
          'Elevator']),
         State.State('trialerFA', self.enterTrialerFA, self.exitTrialerFA, ['trialerFAReject', 'DFA']),
         State.State('trialerFAReject', self.enterTrialerFAReject, self.exitTrialerFAReject, ['walk']),
         State.State('DFA', self.enterDFA, self.exitDFA, ['DFAReject', 'teleportOut']),
         State.State('DFAReject', self.enterDFAReject, self.exitDFAReject, ['walk']),
         State.State('teleportIn', self.enterTeleportIn, self.exitTeleportIn, ['walk']),
         State.State('teleportOut', self.enterTeleportOut, self.exitTeleportOut, ['teleportIn']),
         State.State('stopped', self.enterStopped, self.exitStopped, ['walk', 'elevatorOut', 'battle']),
         State.State('died', self.enterDied, self.exitDied, []),
         State.State('elevatorOut', self.enterElevatorOut, self.exitElevatorOut, [])], 'entrance', 'elevatorOut')
        self.parentFSM = parentFSM
        self.elevatorDoneEvent = 'elevatorDoneSI'
        self.currentFloor = 0

    def enter(self, requestStatus):
        self.fsm.enterInitialState()
        self.zoneId = requestStatus['zoneId']
        self.accept('DSIDoneEvent', self.handleDSIDoneEvent)

    def exit(self):
        self.ignoreAll()

    def load(self):
        Place.Place.load(self)
        self.parentFSM.getStateNamed('cogdoInterior').addChild(self.fsm)
        self.townBattle = TownBattle.TownBattle('town-battle-done')
        self.townBattle.load()
        for i in range(1, 3):
            Suit.loadSuits(i)

    def unload(self):
        Place.Place.unload(self)
        self.parentFSM.getStateNamed('cogdoInterior').removeChild(self.fsm)
        del self.parentFSM
        del self.fsm
        self.ignoreAll()
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()
        self.townBattle.unload()
        self.townBattle.cleanup()
        del self.townBattle
        for i in range(1, 3):
            Suit.unloadSuits(i)

    def setState(self, state, battleEvent=None):
        if battleEvent:
            self.fsm.request(state, [battleEvent])
        else:
            self.fsm.request(state)

    def getZoneId(self):
        return self.zoneId

    def enterZone(self, zoneId):
        pass

    def isPeriodTimerEffective(self):
        return 0

    def handleDSIDoneEvent(self, requestStatus):
        self.doneStatus = requestStatus
        messenger.send(self.doneEvent)

    def doRequestLeave(self, requestStatus):
        self.fsm.request('trialerFA', [requestStatus])

    def enterEntrance(self):
        pass

    def exitEntrance(self):
        pass

    def enterElevator(self, distElevator):
        self.accept(self.elevatorDoneEvent, self.handleElevatorDone)
        self.elevator = Elevator.Elevator(self.fsm.getStateNamed('Elevator'), self.elevatorDoneEvent, distElevator)
        self.elevator.load()
        self.elevator.enter()
        base.localAvatar.cantLeaveGame = 1

    def exitElevator(self):
        base.localAvatar.cantLeaveGame = 0
        self.ignore(self.elevatorDoneEvent)
        self.elevator.unload()
        self.elevator.exit()
        del self.elevator
        return

    def detectedElevatorCollision(self, distElevator):
        self.fsm.request('Elevator', [distElevator])
        return

    def handleElevatorDone(self, doneStatus):
        self.notify.debug('handling elevator done event')
        where = doneStatus['where']
        if where == 'reject':
            if hasattr(base.localAvatar, 'elevatorNotifier') and base.localAvatar.elevatorNotifier.isNotifierOpen():
                pass
            else:
                self.fsm.request('walk')
        elif where == 'exit':
            self.fsm.request('walk')
        elif where == 'cogdoInterior':
            pass
        else:
            self.notify.error('Unknown mode: ' + where + ' in handleElevatorDone')

    def enterGame(self):
        base.localAvatar.setTeleportAvailable(0)
        base.localAvatar.laffMeter.start()

    def exitGame(self):
        base.localAvatar.laffMeter.stop()

    def enterBattle(self, event):
        mult = ToontownBattleGlobals.getCreditMultiplier(self.currentFloor)
        self.townBattle.enter(event, self.fsm.getStateNamed('battle'), bldg=1, creditMultiplier=mult)
        base.localAvatar.b_setAnimState('off', 1)
        base.localAvatar.cantLeaveGame = 1

    def exitBattle(self):
        self.townBattle.exit()
        base.localAvatar.cantLeaveGame = 0

    def enterCrane(self):
        base.localAvatar.setTeleportAvailable(0)
        base.localAvatar.laffMeter.start()
        base.localAvatar.collisionsOn()

    def exitCrane(self):
        base.localAvatar.collisionsOff()
        base.localAvatar.laffMeter.stop()

    def enterWalk(self, teleportIn=0):
        Place.Place.enterWalk(self, teleportIn)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)

    def enterStickerBook(self, page=None):
        Place.Place.enterStickerBook(self, page)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)

    def enterSit(self):
        Place.Place.enterSit(self)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)

    def enterTeleportIn(self, requestStatus):
        base.localAvatar.setPosHpr(2.5, 11.5, ToontownGlobals.FloorOffset, 45.0, 0.0, 0.0)
        Place.Place.enterTeleportIn(self, requestStatus)

    def enterTeleportOut(self, requestStatus):
        Place.Place.enterTeleportOut(self, requestStatus, self.__teleportOutDone)

    def __teleportOutDone(self, requestStatus):
        hoodId = requestStatus['hoodId']
        if hoodId == ToontownGlobals.MyEstate:
            self.getEstateZoneAndGoHome(requestStatus)
        else:
            messenger.send('localToonLeft')
            self.doneStatus = requestStatus
            messenger.send(self.doneEvent)

    def exitTeleportOut(self):
        Place.Place.exitTeleportOut(self)

    def goHomeFailed(self, task):
        self.notifyUserGoHomeFailed()
        self.ignore('setLocalEstateZone')
        self.doneStatus['avId'] = -1
        self.doneStatus['zoneId'] = self.getZoneId()
        self.fsm.request('teleportIn', [self.doneStatus])
        return Task.done

    def enterElevatorOut(self):
        return

    def __elevatorOutDone(self, requestStatus):
        self.doneStatus = requestStatus
        messenger.send(self.doneEvent)

    def exitElevatorOut(self):
        return