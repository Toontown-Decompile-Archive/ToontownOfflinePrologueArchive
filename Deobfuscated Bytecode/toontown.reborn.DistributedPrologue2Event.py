# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.reborn.DistributedPrologue2Event
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from direct.distributed.DistributedObject import DistributedObject
from direct.fsm.FSM import FSM
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from toontown.toon import NPCToons
from otp.margins.WhisperPopup import *

class DistributedPrologue2Event(DistributedObject, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPrologue2Event')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        FSM.__init__(self, 'Prologue2EventFSM')
        self.cr.prologue2Event = self
        self.laffMeter = base.localAvatar.laffMeter
        self.book = base.localAvatar.book.bookOpenButton
        self.book2 = base.localAvatar.book.bookCloseButton
        self.rocky = NPCToons.createLocalNPC(14011)
        self.rocky.useLOD(1000)
        self.rocky.head = self.rocky.find('**/__Actor_head')
        self.rocky.initializeBodyCollisions('toon')
        self.rocky.setPosHpr(-53.317, 229.216, 10.015, -518, 0, 0)
        self.rocky.reparentTo(render)
        self.rocky.loop('neutral')
        self.rocky.addActive()
        self.logano = NPCToons.createLocalNPC(14006)
        self.logano.useLOD(1000)
        self.logano.head = self.logano.find('**/__Actor_head')
        self.logano.initializeBodyCollisions('toon')
        self.logano.setPosHpr(17.805, 25.009, 0.025, -102, 0, 0)
        self.logano.reparentTo(render)
        self.logano.loop('neutral')
        self.logano.addActive()
        self.sparky = NPCToons.createLocalNPC(14007)
        self.sparky.useLOD(1000)
        self.sparky.head = self.sparky.find('**/__Actor_head')
        self.sparky.initializeBodyCollisions('toon')
        self.sparky.setPosHpr(-62, 213.407, 10.015, -422, 0, 0)
        self.sparky.reparentTo(render)
        self.sparky.loop('neutral')
        self.sparky.addActive()
        self.weird = NPCToons.createLocalNPC(14008)
        self.weird.useLOD(1000)
        self.weird.head = self.weird.find('**/__Actor_head')
        self.weird.initializeBodyCollisions('toon')
        self.weird.setPosHpr(-41.676, 229.239, 10.015, -602, 0, 0)
        self.weird.reparentTo(render)
        self.weird.loop('neutral')
        self.weird.addActive()
        self.ned = NPCToons.createLocalNPC(14009)
        self.ned.useLOD(1000)
        self.ned.head = self.ned.find('**/__Actor_head')
        self.ned.initializeBodyCollisions('toon')
        self.ned.setPosHpr(64.153, 74.389, 0.025, 87.9, 0, 0)
        self.ned.reparentTo(render)
        self.ned.loop('neutral')
        self.ned.addActive()
        self.supertricky = NPCToons.createLocalNPC(14010)
        self.supertricky.useLOD(1000)
        self.supertricky.head = self.supertricky.find('**/__Actor_head')
        self.supertricky.initializeBodyCollisions('toon')
        self.supertricky.setPosHpr(55.043, 158.484, 10.025, -15, 0, 0)
        self.supertricky.reparentTo(render)
        self.supertricky.loop('neutral')
        self.supertricky.addActive()
        self.jaquanza = NPCToons.createLocalNPC(14012)
        self.jaquanza.useLOD(1000)
        self.jaquanza.head = self.jaquanza.find('**/__Actor_head')
        self.jaquanza.initializeBodyCollisions('toon')
        self.jaquanza.setPosHpr(78.257, 165.554, 10.125, 44.5, 0, 0)
        self.jaquanza.reparentTo(render)
        self.jaquanza.loop('neutral')
        self.jaquanza.addActive()
        self.zzandrew = NPCToons.createLocalNPC(14013)
        self.zzandrew.useLOD(1000)
        self.zzandrew.head = self.zzandrew.find('**/__Actor_head')
        self.zzandrew.initializeBodyCollisions('toon')
        self.zzandrew.setPosHpr(37.952, 208.329, 10.026, 106, 0, 0)
        self.zzandrew.reparentTo(render)
        self.zzandrew.loop('neutral')
        self.zzandrew.addActive()
        self.patrick = NPCToons.createLocalNPC(14014)
        self.patrick.useLOD(1000)
        self.patrick.head = self.patrick.find('**/__Actor_head')
        self.patrick.initializeBodyCollisions('toon')
        self.patrick.setPosHpr(-78.568, 163.722, 10.025, -415, 0, 0)
        self.patrick.reparentTo(render)
        self.patrick.loop('neutral')
        self.patrick.addActive()

    def enterOff(self, offset):
        pass

    def exitOff(self):
        pass

    def __cleanupNPCs(self):
        npcs = [
         self.rocky, self.logano, self.sparky, self.weird, self.ned, self.zzandrew, self.jaquanza, self.supertricky, self.patrick]
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
        pass

    def exitIdle(self):
        pass

    def enterEvent(self, offset):
        base.localAvatar.disableSleeping()
        base.localAvatar.invPage.ignoreOnscreenHooks()
        base.localAvatar.questPage.ignoreOnscreenHooks()
        self.hideTunnel()
        self.zzandrewWalkInterval = Sequence(Func(self.zzandrew.loop, 'walk'), self.zzandrew.posHprInterval(4, (15.188,
                                                                                                                204.227,
                                                                                                                10.026), (88,
                                                                                                                          0,
                                                                                                                          0)), self.zzandrew.posHprInterval(7, (-39.275,
                                                                                                                                                                205.043,
                                                                                                                                                                10.025), (88,
                                                                                                                                                                          0,
                                                                                                                                                                          0)), self.zzandrew.posHprInterval(1, (-39.275,
                                                                                                                                                                                                                205.043,
                                                                                                                                                                                                                10.025), (28,
                                                                                                                                                                                                                          0,
                                                                                                                                                                                                                          0)), self.zzandrew.posHprInterval(3, (-44.788,
                                                                                                                                                                                                                                                                214.04,
                                                                                                                                                                                                                                                                10.025), (43.3,
                                                                                                                                                                                                                                                                          0,
                                                                                                                                                                                                                                                                          0)), Func(self.zzandrew.loop, 'neutral'))
        self.zzandrewWalk2Interval = Sequence(Func(self.zzandrew.loop, 'walk'), self.zzandrew.posHprInterval(1, (-39.275,
                                                                                                                 205.043,
                                                                                                                 10.025), (28,
                                                                                                                           0,
                                                                                                                           0)), self.zzandrew.posHprInterval(7, (-39.275,
                                                                                                                                                                 205.043,
                                                                                                                                                                 10.025), (88,
                                                                                                                                                                           0,
                                                                                                                                                                           0)), self.zzandrew.posHprInterval(4, (15.188,
                                                                                                                                                                                                                 204.227,
                                                                                                                                                                                                                 10.026), (88,
                                                                                                                                                                                                                           0,
                                                                                                                                                                                                                           0)), self.zzandrew.posHprInterval(3, (37.952,
                                                                                                                                                                                                                                                                 208.329,
                                                                                                                                                                                                                                                                 10.026), (106,
                                                                                                                                                                                                                                                                           0,
                                                                                                                                                                                                                                                                           0)), Func(self.zzandrew.loop, 'neutral'))
        self.eventInterval = Sequence(Wait(2), Func(NodePath(self.book).hide), Func(NodePath(self.laffMeter).hide), Func(base.localAvatar.obscureFriendsListButton, 1), Func(base.localAvatar.hideClarabelleGui), Func(base.localAvatar.invPage.ignoreOnscreenHooks), Func(base.localAvatar.questPage.ignoreOnscreenHooks), Wait(3), Func(base.localAvatar.displayTalk, 'If I recall correctly, that there lab is located on Oak Street.'), Wait(4), Func(base.localAvatar.displayTalk, 'This here place needs some renovations. A nice fishing pond at this pool would do just nicely, and make my Pet Shop business an extra buck!'))
        self.eventInterval2 = Sequence(Wait(3), Func(self.sparky.setChatAbsolute, 'I sure love boeats.', CFSpeech | CFTimeout), Wait(7), Func(self.sparky.setChatAbsolute, 'Gayyyyygs.', CFSpeech | CFTimeout), Wait(7), Func(self.sparky.setChatAbsolute, 'Cawwwwwwgs.', CFSpeech | CFTimeout), Wait(7), Func(self.sparky.setChatAbsolute, 'Wow. These guys are silent.', CFThought | CFTimeout), Wait(7), Func(self.sparky.setChatAbsolute, "Hey guys. Wanna hear something these younglings call a, 'joke'?", CFSpeech | CFTimeout), Wait(7), Func(self.rocky.setChatAbsolute, 'No.', CFSpeech | CFTimeout), Func(self.weird.setChatAbsolute, 'No.', CFSpeech | CFTimeout), Wait(3), Func(self.sparky.setChatAbsolute, 'Wow, okay then. Sheesh.', CFSpeech | CFTimeout), Wait(5))
        self.eventInterval3 = Sequence(Wait(2), Func(self.patrick.setChatAbsolute, "Man, I wonder when I'll be able to push that new Funny Farm update.", CFThought | CFTimeout), Wait(5), Func(self.patrick.setChatAbsolute, 'I worked really hard on the new tutorial too...', CFThought | CFTimeout), Wait(4), Func(self.patrick.setChatAbsolute, "It's not much, but I hope people appreicate it for what it's worth.", CFThought | CFTimeout), Wait(6), Func(self.patrick.setChatAbsolute, "Oh, I can't forget that trolley games now work also!", CFThought | CFTimeout), Wait(4), Func(self.patrick.setChatAbsolute, "Don't get me started on that new title screen. That's prob-", CFThought | CFTimeout), Wait(5), Func(self.patrick.setChatAbsolute, 'AAAAAAA!', CFSpeech | CFTimeout), Wait(3), Func(self.patrick.setChatAbsolute, 'Why did I just scream out loud?! Anyway, what was I talking about again...?', CFThought | CFTimeout), Wait(5))
        self.eventInterval4 = Sequence(Wait(2), Func(self.logano.setChatAbsolute, 'I sure do love me some Undertally.', CFSpeech | CFTimeout), Wait(4), Func(self.logano.setChatAbsolute, 'aaa', CFSpeech | CFTimeout), Wait(3.5), Func(self.logano.setChatAbsolute, 'aaa underwater habitat', CFSpeech | CFTimeout), Wait(3.5), Func(self.logano.setChatAbsolute, 'aaa sharks', CFSpeech | CFTimeout), Wait(3.5), Func(self.logano.setChatAbsolute, 'aaa indentation errors', CFSpeech | CFTimeout), Wait(8))
        self.eventInterval5 = Sequence(Func(self.eventInterval2.start), Wait(2), Func(self.zzandrew.setChatAbsolute, "Doot Doot I'm a flinger.", CFSpeech | CFTimeout), Wait(4), Func(self.zzandrew.setChatAbsolute, "In all seriousness though, I gotta stop modelin' in Panda3D.", CFThought | CFTimeout), Wait(5), Func(self.zzandrew.setChatAbsolute, 'But dang has my music improved ever since Toontown Universe!', CFThought | CFTimeout), Wait(5), Func(self.zzandrew.setChatAbsolute, 'Oh snap, I forgot: Officer Shroder is visiting my Estate today!', CFSpeech | CFTimeout), Wait(5), Func(self.zzandrew.setChatAbsolute, 'I better get my monitor and chair ready so I look good.', CFSpeech | CFTimeout), Wait(1), Func(self.zzandrewWalkInterval.start), Wait(16), Func(self.zzandrew.setChatAbsolute, 'Do any of you know where the ZZ Train is?', CFSpeech | CFTimeout), Wait(5), Func(self.zzandrew.setChatAbsolute, 'Welp. Better luck next time I suppose.', CFSpeech | CFTimeout), Wait(5), Func(self.zzandrewWalk2Interval.start), Wait(16))
        self.eventInterval3.loop()
        self.eventInterval3.setT(offset)
        self.eventInterval4.loop()
        self.eventInterval4.setT(offset)
        self.eventInterval5.loop()
        self.eventInterval5.setT(offset)
        self.eventInterval.start()
        self.eventInterval.setT(offset)

    def exitEvent(self):
        self.eventInterval2.finish()
        self.eventInterval3.finish()
        self.eventInterval4.finish()
        self.eventInterval5.finish()
        self.eventInterval.finish()
        self.zzandrewWalkInterval.finish()
        self.zzandrewWalk2Interval.finish()

    def enterEventTwo(self, offset):
        pass

    def exitEventTwo(self):
        pass

    def setState(self, state, timestamp):
        self.request(state, globalClockDelta.localElapsedTime(timestamp))

    def hideTunnel(self):
        self.geom = base.cr.playGame.hood.loader.geom
        tunnel = self.geom.find('**/linktunnel_sb_1002000_DNARoot')
        if tunnel:
            tunnel.reparentTo(hidden)
        dummyTunnel = self.geom.find('**/prop_safe_zone_tunnel_dummy')
        if dummyTunnel:
            dummyTunnel.reparentTo(self.geom)