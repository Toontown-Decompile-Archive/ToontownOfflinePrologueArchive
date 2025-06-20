# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.building.DistributedAnimDoor
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import NodePath, VBase3
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import Parallel, Sequence, Wait, HprInterval, LerpHprInterval, SoundInterval
from toontown.building import DistributedDoor
from toontown.building import DoorTypes

class DistributedAnimDoor(DistributedDoor.DistributedDoor):

    def __init__(self, cr):
        DistributedDoor.DistributedDoor.__init__(self, cr)
        base.animDoor = self

    def getBuilding(self):
        if not self.__dict__.has_key('building'):
            if self.doorType == DoorTypes.EXT_ANIM_STANDARD:
                searchStr = '**/??' + str(self.block) + ':animated_building_*_DNARoot;+s'
                self.notify.debug('searchStr=%s' % searchStr)
                self.building = self.cr.playGame.hood.loader.geom.find(searchStr)
            else:
                self.notify.error('DistributedAnimDoor.getBuiding with doorType=%s' % self.doorType)
        return self.building

    def getDoorNodePath(self):
        if self.doorType == DoorTypes.EXT_ANIM_STANDARD:
            if hasattr(self, 'tempDoorNodePath'):
                return self.tempDoorNodePath
            building = self.getBuilding()
            doorNP = building.find('**/door_origin')
            self.notify.debug('creating doorOrigin at %s %s' % (str(doorNP.getPos()), str(doorNP.getHpr())))
            otherNP = NodePath('doorOrigin')
            otherNP.setPos(doorNP.getPos())
            otherNP.setHpr(doorNP.getHpr())
            otherNP.reparentTo(doorNP.getParent())
            self.tempDoorNodePath = otherNP
        else:
            self.notify.error('DistributedAnimDoor.getDoorNodePath with doorType=%s' % self.doorType)
        return otherNP

    def setTriggerName(self):
        if self.doorType == DoorTypes.EXT_ANIM_STANDARD:
            building = self.getBuilding()
            if not building.isEmpty():
                doorTrigger = building.find('**/door_0_door_trigger')
                if not doorTrigger.isEmpty():
                    doorTrigger.node().setName(self.getTriggerName())
            else:
                self.notify.warning('setTriggerName failed no building')
        else:
            self.notify.error('setTriggerName doorTYpe=%s' % self.doorType)

    def getAnimBuilding(self):
        if not self.__dict__.has_key('animBuilding'):
            if self.doorType == DoorTypes.EXT_ANIM_STANDARD:
                bldg = self.getBuilding()
                key = bldg.getParent().getParent()
                animPropList = self.cr.playGame.hood.loader.animPropDict.get(key)
                if animPropList:
                    for prop in animPropList:
                        if bldg == prop.getActor().getParent():
                            self.animBuilding = prop
                            break

                else:
                    self.notify.error('could not find' + str(key))
            else:
                self.notify.error('No such door type as ' + str(self.doorType))
        return self.animBuilding

    def getBuildingActor(self):
        result = self.getAnimBuilding().getActor()
        return result

    def enterOpening(self, ts):
        bldgActor = self.getBuildingActor()
        rightDoor = bldgActor.controlJoint(None, 'modelRoot', 'def_right_door')
        if rightDoor.isEmpty():
            self.notify.warning('enterOpening(): did not find rightDoor')
            return
        else:
            otherNP = self.getDoorNodePath()
            trackName = 'doorOpen-%d' % self.doId
            if self.rightSwing:
                h = 100
            else:
                h = -100
            self.finishDoorTrack()
            self.doorTrack = Parallel(SoundInterval(self.openSfx, node=rightDoor), Sequence(HprInterval(rightDoor, VBase3(0, 0, 0)), Wait(0.4), LerpHprInterval(nodePath=rightDoor, duration=0.6, hpr=VBase3(h, 0, 0), startHpr=VBase3(0, 0, 0), blendType='easeInOut')), name=trackName)
            self.doorTrack.start(ts)
            return

    def enterClosing(self, ts):
        bldgActor = self.getBuildingActor()
        rightDoor = bldgActor.controlJoint(None, 'modelRoot', 'def_right_door')
        if rightDoor.isEmpty():
            self.notify.warning('enterClosing(): did not find rightDoor')
            return
        else:
            otherNP = self.getDoorNodePath()
            trackName = 'doorClose-%d' % self.doId
            if self.rightSwing:
                h = 100
            else:
                h = -100
            self.finishDoorTrack()
            self.doorTrack = Sequence(LerpHprInterval(nodePath=rightDoor, duration=1.0, hpr=VBase3(0, 0, 0), startHpr=VBase3(h, 0, 0), blendType='easeInOut'), SoundInterval(self.closeSfx, node=rightDoor), name=trackName)
            self.doorTrack.start(ts)
            if hasattr(self, 'done'):
                request = self.getRequestStatus()
                messenger.send('doorDoneEvent', [request])
            return

    def exitDoorEnterOpening(self, ts):
        bldgActor = self.getBuildingActor()
        leftDoor = bldgActor.controlJoint(None, 'modelRoot', 'def_left_door')
        if self.leftSwing:
            h = -100
        else:
            h = 100
        if not leftDoor.isEmpty():
            otherNP = self.getDoorNodePath()
            trackName = 'doorDoorExitTrack-%d' % self.doId
            self.finishDoorExitTrack()
            self.doorExitTrack = Parallel(SoundInterval(self.openSfx, node=leftDoor), Sequence(LerpHprInterval(nodePath=leftDoor, duration=0.6, hpr=VBase3(h, 0, 0), startHpr=VBase3(0, 0, 0), blendType='easeInOut')), name=trackName)
            self.doorExitTrack.start(ts)
        else:
            self.notify.warning('exitDoorEnterOpening(): did not find leftDoor')
        return

    def exitDoorEnterClosing(self, ts):
        bldgActor = self.getBuildingActor()
        leftDoor = bldgActor.controlJoint(None, 'modelRoot', 'def_left_door')
        if self.leftSwing:
            h = -100
        else:
            h = 100
        if not leftDoor.isEmpty():
            otherNP = self.getDoorNodePath()
            trackName = 'doorExitTrack-%d' % self.doId
            self.finishDoorExitTrack()
            self.doorExitTrack = Sequence(LerpHprInterval(nodePath=leftDoor, duration=1.0, hpr=VBase3(0, 0, 0), startHpr=VBase3(h, 0, 0), blendType='easeInOut'), SoundInterval(self.closeSfx, node=leftDoor), name=trackName)
            self.doorExitTrack.start(ts)
        return