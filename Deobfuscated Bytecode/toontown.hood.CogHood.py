# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.hood.CogHood
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from direct.fsm import State
import Hood

class CogHood(Hood.Hood):
    notify = DirectNotifyGlobal.directNotify.newCategory('CogHood')

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        Hood.Hood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.fsm = ClassicFSM.ClassicFSM('Hood', [State.State('start', self.enterStart, self.exitStart, ['cogHQLoader']),
         State.State('cogHQLoader', self.enterCogHQLoader, self.exitCogHQLoader, ['quietZone', 'minigame']),
         State.State('minigame', self.enterCogHQLoader, self.exitCogHQLoader, ['quietZone', 'cogHQLoader']),
         State.State('quietZone', self.enterQuietZone, self.exitQuietZone, ['cogHQLoader']),
         State.State('final', self.enterFinal, self.exitFinal, [])], 'start', 'final')
        self.fsm.enterInitialState()
        self.visInterest = None
        return

    def load(self):
        Hood.Hood.load(self)
        skyInner = self.sky.find('**/InnerGroup')
        skyMiddle = self.sky.find('**/MiddleGroup')
        skyOuter = self.sky.find('**/OutterSky')
        if not skyOuter.isEmpty():
            skyOuter.setBin('background', 0)
        if not skyMiddle.isEmpty():
            skyMiddle.setDepthWrite(0)
            skyMiddle.setBin('background', 10)
        if not skyInner.isEmpty():
            skyInner.setDepthWrite(0)
            skyInner.setBin('background', 20)

    def unload(self):
        Hood.Hood.unload(self)

    def loadLoader(self, requestStatus):
        loaderName = requestStatus['loader']
        if loaderName == 'cogHQLoader':
            self.loader = self.cogHQLoaderClass(self, self.fsm.getStateNamed('cogHQLoader'), self.loaderDoneEvent)
            self.loader.load(requestStatus['zoneId'])

    def enterCogHQLoader(self, requestStatus):
        self.accept(self.loaderDoneEvent, self.handleCogHQLoaderDone)
        self.loader.enter(requestStatus)

    def exitCogHQLoader(self):
        self.ignore(self.loaderDoneEvent)
        self.loader.exit()
        self.loader.unload()
        del self.loader

    def handleCogHQLoaderDone(self):
        doneStatus = self.loader.getDoneStatus()
        if self.isSameHood(doneStatus):
            state = 'quietZone'
            if doneStatus.get('where') == 'minigame':
                state = 'final'
            self.fsm.request('quietZone', [doneStatus])
        else:
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)

    def enterMinigame(self, ignoredParameter=None):
        pass

    def exitMinigame(self):
        pass