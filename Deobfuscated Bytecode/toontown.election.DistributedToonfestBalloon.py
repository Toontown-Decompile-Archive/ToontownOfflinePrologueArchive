# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.election.DistributedToonfestBalloon
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from otp.nametag.NametagConstants import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from direct.distributed.DistributedObject import DistributedObject
from direct.fsm.FSM import FSM
from toontown.toon import NPCToons
from toontown.toonbase import ToontownGlobals
from direct.task import Task
from random import choice
import ToonfestBalloonGlobals

class DistributedToonfestBalloon(DistributedObject, FSM):

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        FSM.__init__(self, 'ToonfestBalloonFSM')
        self.avId = 0
        self.flightPathIndex = 0
        self.electionsOn = config.GetBool('want-doomsday-reborn', False) or config.GetBool('want-doomsday', False) or config.GetBool('want-interim-election-buildup', False) or config.GetBool('want-election-buildup', False)
        self.balloon = loader.loadModel('phase_6/models/events/tf_balloon')
        self.balloon.reparentTo(base.render)
        self.balloon.setPos(*ToonfestBalloonGlobals.BalloonBasePosition)
        self.balloon.setH(250)
        self.balloon.setScale(ToonfestBalloonGlobals.BalloonScale)
        self.cr.parentMgr.registerParent(ToontownGlobals.SPToonfestBalloon, self.balloon)
        cs = CollisionSphere(0, 0, 0, 9)
        cs.setTangible(False)
        self.collisionNP = self.balloon.find('**/basket_wall_collision')
        self.collisionNP.node().addSolid(cs)
        self.alec = None
        if not self.electionsOn:
            self.alec = NPCToons.createLocalNPC(2022)
            self.alec.setPos(0.7, 0.7, 0.4)
            self.alec.setH(150)
            self.alec.setScale(1 / ToonfestBalloonGlobals.BalloonScale)
            self.alec.initializeBodyCollisions('toon')
            self.alec.setPickable(0)
            self.alec.addActive()
            self.alec.startBlink()
            self.alec.loop('neutral')
        self.flightPaths = ToonfestBalloonGlobals.generateFlightPaths(self)
        self.toonFlightPaths = ToonfestBalloonGlobals.generateToonFlightPaths(self)
        self.speechSequence = ToonfestBalloonGlobals.generateSpeechSequence(self)
        return

    def delete(self):
        self.demand('Off')
        self.ignore('enter' + self.collisionNP.node().getName())
        self.cr.parentMgr.unregisterParent(ToontownGlobals.SPToonfestBalloon)
        self.balloon.removeNode()
        if self.alec:
            self.alec.delete()
        DistributedObject.delete(self)

    def setState(self, state, timestamp, avId):
        if avId != self.avId:
            self.avId = avId
        self.demand(state, globalClockDelta.localElapsedTime(timestamp))

    def enterWaiting(self, offset):
        self.alec.reparentTo(self.balloon)
        self.alec.setPos(0.7, 0.7, 0.4)
        self.alec.setH(150)
        self.alec.setScale(1 / ToonfestBalloonGlobals.BalloonScale)
        self.accept('enter' + self.collisionNP.node().getName(), self.__handleToonEnter)
        self.balloonIdle = Sequence(Wait(0.3), self.balloon.posInterval(3, (274, -263,
                                                                            26)), Wait(0.3), self.balloon.posInterval(3, (274,
                                                                                                                          -263,
                                                                                                                          25)))
        self.balloonIdle.loop()
        self.balloonIdle.setT(offset)

    def enterNotReady(self, offset):
        if not self.electionsOn:
            self.alec.reparentTo(render)
            self.alec.setPos(255, -259, 22.366)
            self.alec.setH(80)
            self.alec.setScale(1)
        self.accept('enter' + self.collisionNP.node().getName(), self.__handleToonEnterNotReady)
        self.balloonIdle = Sequence(Wait(0.3), self.balloon.posInterval(3, (274, -263,
                                                                            26)), Wait(0.3), self.balloon.posInterval(3, (274,
                                                                                                                          -263,
                                                                                                                          25)))
        self.balloonIdle.loop()
        self.balloonIdle.setT(offset)

    def __handleToonEnter(self, collEntry):
        if self.avId != 0:
            return
        if self.state != 'Waiting':
            return
        self.sendUpdate('requestEnter', [])

    def __handleToonEnterNotReady(self, collEntry):
        if not self.electionsOn:
            if self.alec.nametag.getChat() == '':
                self.alec.setChatAbsolute('Hey there! Come back later for a ride to the top of the tower!', CFSpeech | CFTimeout)

    def exitWaiting(self):
        self.balloonIdle.finish()
        self.ignore('enter' + self.collisionNP.node().getName())

    def exitNotReady(self):
        self.balloonIdle.finish()

    def enterOccupied(self, offset):
        if self.avId == base.localAvatar.doId:
            base.localAvatar.disableAvatarControls()
            self.hopOnAnim = Sequence(Parallel(Func(base.localAvatar.b_setParent, ToontownGlobals.SPToonfestBalloon), Func(base.localAvatar.b_setAnimState, 'jump', 1.0)), base.localAvatar.posInterval(0.6, (0,
                                                                                                                                                                                                              0,
                                                                                                                                                                                                              2)), base.localAvatar.posInterval(0.4, (0,
                                                                                                                                                                                                                                                      0,
                                                                                                                                                                                                                                                      0.7)), Func(base.localAvatar.enableAvatarControls), Parallel(Func(base.localAvatar.b_setParent, ToontownGlobals.SPRender)))
            self.hopOnAnim.start()
        try:
            self.speechSequence = self.speechSequence
            self.speechSequence.start()
            self.speechSequence.setT(offset)
        except Exception as e:
            self.notify.debug('Exception: %s' % e)

    def exitOccupied(self):
        try:
            self.hopOnAnim.finish()
        except Exception as e:
            self.notify.debug('Exception: %s' % e)

    def setFlightPath(self, flightPathIndex):
        self.flightPathIndex = flightPathIndex

    def enterStartRide(self, offset):
        try:
            self.rideSequence = self.flightPaths[self.flightPathIndex]
            self.rideSequence.start()
            self.rideSequence.setT(offset)
        except Exception as e:
            self.notify.debug('Exception: %s' % e)

        if self.avId == base.localAvatar.doId:
            try:
                self.toonRideSequence = self.toonFlightPaths[self.flightPathIndex]
                self.toonRideSequence.start()
                self.toonRideSequence.setT(offset)
            except Exception as e:
                self.notify.debug('Exception: %s' % e)

    def exitStartRide(self):
        try:
            self.rideSequence.finish()
            self.speechSequence.finish()
        except Exception as e:
            self.notify.debug('Exception: %s' % e)

    def enterRideOver(self, offset):
        if self.avId == base.localAvatar.doId:
            base.localAvatar.disableAvatarControls()
            self.hopOffAnim = Sequence(Parallel(Func(base.localAvatar.b_setParent, ToontownGlobals.SPRender), Func(base.localAvatar.b_setAnimState, 'jump', 1.0)), Wait(0.3), base.localAvatar.hprInterval(0.4, (-24,
                                                                                                                                                                                                                 0,
                                                                                                                                                                                                                 0)), base.localAvatar.posInterval(0.3, (197,
                                                                                                                                                                                                                                                         -133,
                                                                                                                                                                                                                                                         209)), base.localAvatar.posInterval(0.7, (209,
                                                                                                                                                                                                                                                                                                   -112,
                                                                                                                                                                                                                                                                                                   204.936)), Wait(0.3), Func(base.localAvatar.b_setAnimState, 'neutral'), Wait(0.3), Func(base.localAvatar.enableAvatarControls), Wait(5), self.balloon.posHprInterval(15.0, Point3(274, -263, 26), (0,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      0,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      0)), self.balloon.posHprInterval(0.1, Point3(274, -263, 25), (0,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    0,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    0)))
            self.hopOffAnim.start()