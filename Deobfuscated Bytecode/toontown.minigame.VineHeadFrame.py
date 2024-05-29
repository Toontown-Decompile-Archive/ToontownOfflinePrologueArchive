# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.VineHeadFrame
# Compiled at: 2014-04-30 09:53:54
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from toontown.toonbase import ToontownGlobals
from toontown.toon import ToonHead

class VineHeadFrame(DirectFrame):

    def __init__(self, av=None, color=Vec4(1, 1, 1, 1), *args, **kwargs):
        self.panelGeom = DGG.getDefaultDialogGeom()
        opts = {'relief': None, 'geom': self.panelGeom, 
           'geom_scale': (0.5, 1, 0.5), 
           'pos': (0, 0, 0)}
        opts.update(kwargs)
        apply(DirectFrame.__init__, (self,) + args, opts)
        self.initialiseoptions(VineHeadFrame)
        if av:
            self.setAv(av)
        self.setScale(0.1)
        self.setTransparency(0)
        return

    def setAv(self, av):
        self.head = self.stateNodePath[0].attachNewNode('head', 20)
        self.head.setPosHprScale(0, -0.5, -0.09, 180.0, 0.0, 0.0, 0.2, 0.2, 0.2)
        self.headModel = ToonHead.ToonHead()
        self.headModel.setupHead(av.style, forGui=1)
        self.headModel.reparentTo(self.head)

    def destroy(self):
        self.headModel.delete()
        del self.headModel
        self.head.removeNode()
        del self.head
        DirectFrame.destroy(self)