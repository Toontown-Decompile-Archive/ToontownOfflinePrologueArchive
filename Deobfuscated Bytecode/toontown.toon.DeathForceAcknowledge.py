# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.toon.DeathForceAcknowledge
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from toontown.toontowngui import TTDialog
from toontown.toonbase import TTLocalizer
from direct.showbase import Transitions
from direct.gui.DirectGui import *
from pandac.PandaModules import *
import LaffMeter

class DeathForceAcknowledge:

    def __init__(self, doneEvent):
        fadeModel = loader.loadModel('phase_3/models/misc/fade')
        if fadeModel:
            self.fade = DirectFrame(parent=aspect2dp, relief=None, image=fadeModel, image_color=(0,
                                                                                                 0,
                                                                                                 0,
                                                                                                 0.4), image_scale=3.0, state=DGG.NORMAL)
            self.fade.reparentTo(render2d, FADE_SORT_INDEX)
            fadeModel.removeNode()
        else:
            print 'Problem loading fadeModel.'
            self.fade = None
        self.dialog = TTDialog.TTGlobalDialog(message=TTLocalizer.PlaygroundDeathAckMessage, doneEvent=doneEvent, style=TTDialog.Acknowledge, suppressKeys=True)
        self.dialog['text_pos'] = (-0.26, 0.1)
        scale = self.dialog.component('image0').getScale()
        scale.setX(scale[0] * 1.3)
        self.dialog.component('image0').setScale(scale)
        av = base.localAvatar
        self.laffMeter = LaffMeter.LaffMeter(av.style, av.hp, av.maxHp)
        self.laffMeter.reparentTo(self.dialog)
        if av.style.getAnimal() == 'monkey':
            self.laffMeter.setPos(-0.46, 0, -0.035)
            self.laffMeter.setScale(0.085)
        else:
            self.laffMeter.setPos(-0.48, 0, -0.035)
            self.laffMeter.setScale(0.1)
        self.laffMeter.start()
        self.dialog.show()
        return

    def cleanup(self):
        if self.fade:
            self.fade.destroy()
        if self.laffMeter:
            self.laffMeter.destroy()
            del self.laffMeter
        if self.dialog:
            self.dialog.cleanup()
            self.dialog = None
        return