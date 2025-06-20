# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.ai.HolidayDecorator
# Compiled at: 2014-04-30 09:53:54
from toontown.toonbase import ToontownGlobals
from direct.interval.IntervalGlobal import Parallel, Sequence, Func, Wait
from pandac.PandaModules import Vec4, TransformState, NodePath, TransparencyAttrib

class HolidayDecorator:

    def __init__(self):
        self.dnaStore = base.cr.playGame.dnaStore
        self.swapIval = None
        return

    def exit(self):
        if self.swapIval is not None and self.swapIval.isPlaying():
            self.swapIval.finish()
        return

    def decorate(self):
        self.updateHoodDNAStore()
        self.swapIval = self.getSwapVisibleIval()
        if self.swapIval:
            self.swapIval.start()

    def undecorate(self):
        holidayIds = base.cr.newsManager.getDecorationHolidayId()
        if len(holidayIds) > 0:
            self.decorate()
            return
        storageFile = base.cr.playGame.hood.storageDNAFile
        if storageFile:
            pass
        self.swapIval = self.getSwapVisibleIval()
        if self.swapIval:
            self.swapIval.start()

    def updateHoodDNAStore(self):
        hood = base.cr.playGame.hood
        holidayIds = base.cr.newsManager.getDecorationHolidayId()
        for holiday in holidayIds:
            for storageFile in hood.holidayStorageDNADict.get(holiday, []):
                pass

    def getSwapVisibleIval(self, wait=5.0, tFadeOut=3.0, tFadeIn=3.0):
        loader = base.cr.playGame.hood.loader
        npl = render.findAllMatches('**/=DNARoot=holiday_prop;+s')
        p = Parallel()
        for i in range(npl.getNumPaths()):
            np = npl.getPath(i)
            np.setTransparency(TransparencyAttrib.MDual, 1)
            if not np.hasTag('DNACode'):
                continue
            dnaCode = np.getTag('DNACode')
            dnaNode = self.dnaStore.findNode(dnaCode)
            if dnaNode.isEmpty():
                continue
            newNP = dnaNode.copyTo(np.getParent())
            newNP.setTag('DNARoot', 'holiday_prop')
            newNP.setTag('DNACode', dnaCode)
            newNP.setColorScale(1, 1, 1, 0)
            newNP.setTransparency(TransparencyAttrib.MDual, 1)
            if np.hasTag('transformIndex'):
                index = int(np.getTag('transformIndex'))
                transform = loader.holidayPropTransforms.get(index, TransformState.makeIdentity())
                newNP.setTransform(NodePath(), transform)
                newNP.setTag('transformIndex', `index`)
            s = Sequence(Wait(wait), np.colorScaleInterval(tFadeOut, Vec4(1, 1, 1, 0), startColorScale=Vec4(1, 1, 1, 1), blendType='easeInOut'), Func(np.detachNode), Func(np.clearTransparency), newNP.colorScaleInterval(tFadeOut, Vec4(1, 1, 1, 1), startColorScale=Vec4(1, 1, 1, 0), blendType='easeInOut'), Func(newNP.clearTransparency), Func(newNP.clearColorScale))
            p.append(s)

        return p