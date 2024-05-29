# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.reborn.DistributedCNCEvent
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from otp.nametag.NametagConstants import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from direct.distributed.DistributedObject import DistributedObject
from direct.fsm.FSM import FSM
from direct.actor import Actor
from direct.task import Task
from toontown.toon import NPCToons
from toontown.electionsuit import DistributedSuitBase, SuitDNA
from toontown.toonbase import ToontownGlobals
from toontown.battle import BattleProps
from otp.margins.WhisperPopup import *
import InterimElectionGlobals
from direct.directnotify import DirectNotifyGlobal
from random import choice
from direct.interval.LerpInterval import LerpFunctionInterval
from otp.speedchat import SpeedChatGlobals
import SafezoneInvasionRebornGlobals
from toontown.battle.BattleProps import *
from toontown.building.ElevatorUtils import *
from toontown.toonbase import TTLocalizer as TTL
from toontown.chat import ResistanceChat
from toontown.battle import MovieFire

class DistributedCNCEvent(DistributedObject, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCNCEvent')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        FSM.__init__(self, 'CNCEventFSM')
        self.cr.cncEvent = self
        self.rocky = NPCToons.createLocalNPC(14001)
        self.rocky.useLOD(1000)
        self.rocky.head = self.rocky.find('**/__Actor_head')
        self.rocky.initializeBodyCollisions('toon')
        self.rocky.setPosHpr(97.265, 11.262, 3.982, 142, 0, 0)
        self.surlee = NPCToons.createLocalNPC(2019)
        self.surlee.useLOD(1000)
        self.surlee.head = self.surlee.find('**/__Actor_head')
        self.surlee.initializeBodyCollisions('toon')
        self.surlee.setPosHpr(57.434, -18.041, 3.982, 0, 0, 0)
        self.ruth = NPCToons.createLocalNPC(14002)
        self.ruth.useLOD(1000)
        self.ruth.head = self.surlee.find('**/__Actor_head')
        self.ruth.initializeBodyCollisions('toon')
        self.ruth.setPosHpr(47.3, 21.1, 3.982, 222, 0, 0)
        self.reg = NPCToons.createLocalNPC(14003)
        self.reg.useLOD(1000)
        self.reg.head = self.surlee.find('**/__Actor_head')
        self.reg.initializeBodyCollisions('toon')
        self.reg.setPosHpr(78.358, -18.022, 3.982, 7.278, 0, 0)

    def enterOff(self, offset):
        pass

    def exitOff(self):
        pass

    def __cleanupNPCs(self):
        npcs = [
         self.rocky, self.surlee, self.ruth, self.reg]
        for npc in npcs:
            if npc:
                npc.removeActive()
                npc.hide()

    def delete(self):
        self.demand('Off', 0.0)
        self.ignore('entercnode')
        self.__cleanupNPCs()
        DistributedObject.delete(self)

    def enterIdle(self, offset):
        self.ruth.reparentTo(render)
        self.ruth.loop('neutral')
        self.ruth.addActive()
        self.surlee.reparentTo(render)
        self.surlee.loop('neutral')
        self.surlee.addActive()
        self.rocky.reparentTo(render)
        self.rocky.loop('neutral')
        self.rocky.addActive()
        self.reg.reparentTo(render)
        self.reg.loop('neutral')
        self.reg.addActive()
        self.eventInterval = Sequence(Wait(6), Func(self.surlee.setChatAbsolute, 'I wonder when these Toons will show up...', CFSpeech | CFTimeout), Func(self.surlee.loop, 'shrug'), Wait(2), Func(self.surlee.loop, 'neutral'), Wait(4), Func(self.reg.setChatAbsolute, "That Sewer wasn't too grimy to get through- I'm sure they'll make their way here fine!", CFSpeech | CFTimeout), Wait(9), Func(self.surlee.loop, 'walk'), self.surlee.hprInterval(2, (-60.2,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                0,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                0)), Func(self.surlee.loop, 'neutral'), Func(self.surlee.setChatAbsolute, 'Oh, there you Toons are! Nice to see you guys again.', CFSpeech | CFTimeout))
        self.eventInterval.loop()
        self.eventInterval.setT(offset)

    def exitIdle(self):
        self.eventInterval.finish()

    def enterEvent(self, offset):
        pass

    def exitEvent(self):
        pass

    def enterEventTwo(self, offset):
        pass

    def exitEventTwo(self):
        pass

    def setState(self, state, timestamp):
        self.request(state, globalClockDelta.localElapsedTime(timestamp))