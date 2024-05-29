# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.credits.OfflineCredits
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from toontown.toonbase import ToontownGlobals

def doFade(fade, elements):
    if fade == 'in':
        for node in elements:
            Sequence(node.colorScaleInterval(0.5, (1, 1, 1, 1))).start()

    elif fade == 'out':
        for node in elements:
            Sequence(node.colorScaleInterval(0.5, (1, 1, 1, 0))).start()

    elif fade == 'hide':
        for node in elements:
            node.setColorScale(1, 1, 1, 0)


class Logano:

    def __init__(self, preload=False):
        self.sceneRoot = None
        self.preload = preload
        return

    def load(self):
        self.sceneRoot = NodePath('Logano')
        base.setBackgroundColor(0, 0, 0, 1)
        self.title = OnscreenText(text='Logano', pos=(0.6, 0.15, 0.0), scale=0.15, fg=(1,
                                                                                       1,
                                                                                       1,
                                                                                       1), font=ToontownGlobals.getSignFont(), align=TextNode.ACenter)
        self.description = OnscreenText(text='Professional Procrastinator\nFormer Lead Developer\nFormer Project Manager', pos=(0.25,
                                                                                                                                0.05,
                                                                                                                                0.0), scale=0.06, fg=(1,
                                                                                                                                                      1,
                                                                                                                                                      1,
                                                                                                                                                      1), font=ToontownGlobals.getMinnieFont(), align=TextNode.ALeft)
        self.image = OnscreenImage(image='phase_4/maps/news/logano.jpg', pos=(-0.5,
                                                                              0.0,
                                                                              0.0), scale=(0.5,
                                                                                           0.3,
                                                                                           0.3))
        self.elements = [self.title, self.description, self.image]
        for node in self.elements:
            node.setTransparency(1)
            if self.preload:
                node.setColorScale(1, 1, 1, 0)

    def makeInterval(self):
        return Sequence(ParentInterval(self.sceneRoot, render), Wait(3), Func(doFade, 'out', self.elements), Wait(0.5), ParentInterval(self.sceneRoot, hidden))

    def unload(self):
        self.sceneRoot.removeNode()
        self.title.removeNode()
        self.description.removeNode()
        self.image.removeNode()


class Credits:

    def __init__(self, name, description, image, side='left', number=1, name2=None, description2=None, image2=None, special=None):
        self.sceneRoot = None
        self.twoSlides = None
        self.toonName = name
        self.toonDescription = description
        self.toonImage = image
        self.side = side
        self.special = special
        if number > 1:
            self.toon2Name = name2
            self.toon2Description = description2
            self.toon2Image = image2
            self.twoSlides = True
        return

    def load(self):
        self.sceneRoot = NodePath(self.toonName.replace(' ', '').replace('', ''))
        base.setBackgroundColor(0, 0, 0, 1)
        if self.twoSlides:
            if self.side == 'left':
                titlePos = (0.1, 0.5, 0.0)
                descriptionPos = (0.2, 0.4, 0.0)
                imagePos = (-0.55, 0.0, 0.4)
                textAlignment = TextNode.ALeft
                title2Pos = (-0.1, -0.35, 0.0)
                description2Pos = (-0.1, -0.45, 0.0)
                image2Pos = (0.55, 0.0, -0.4)
                text2Alignment = TextNode.ARight
            else:
                titlePos = (-0.1, 0.5, 0.0)
                descriptionPos = (-0.1, 0.4, 0.0)
                imagePos = (0.55, 0.0, 0.4)
                textAlignment = TextNode.ARight
                title2Pos = (0.1, -0.35, 0.0)
                description2Pos = (0.25, -0.45, 0.0)
                image2Pos = (-0.55, 0.0, -0.4)
                text2Alignment = TextNode.ALeft
        else:
            if self.side == 'left':
                titlePos = (0.1, 0.15, 0.0)
                descriptionPos = (0.2, 0.05, 0.0)
                imagePos = (-0.5, 0.0, 0.0)
                textAlignment = TextNode.ALeft
            else:
                titlePos = (-0.1, 0.1, 0.0)
                descriptionPos = (-0.11, 0.0, 0.0)
                imagePos = (0.5, 0.0, 0.0)
                textAlignment = TextNode.ARight
            self.title = OnscreenText(text=self.toonName, pos=titlePos, scale=0.15, fg=(1,
                                                                                        1,
                                                                                        1,
                                                                                        1), font=ToontownGlobals.getSignFont(), align=textAlignment)
            self.description = OnscreenText(text=self.toonDescription, pos=descriptionPos, scale=0.06, fg=(1,
                                                                                                           1,
                                                                                                           1,
                                                                                                           1), font=ToontownGlobals.getMinnieFont(), align=textAlignment)
            self.image = OnscreenImage(image='phase_4/maps/news/%s' % self.toonImage, pos=imagePos, scale=(0.5,
                                                                                                           0.3,
                                                                                                           0.3))
            self.elements = [self.title, self.description, self.image]
            if self.twoSlides:
                self.title2 = OnscreenText(text=self.toon2Name, pos=title2Pos, scale=0.15, fg=(1,
                                                                                               1,
                                                                                               1,
                                                                                               1), font=ToontownGlobals.getSignFont(), align=text2Alignment)
                self.description2 = OnscreenText(text=self.toon2Description, pos=description2Pos, scale=0.06, fg=(1,
                                                                                                                  1,
                                                                                                                  1,
                                                                                                                  1), font=ToontownGlobals.getMinnieFont(), align=text2Alignment)
                self.image2 = OnscreenImage(image='phase_4/maps/news/%s' % self.toon2Image, pos=image2Pos, scale=(0.5,
                                                                                                                  0.3,
                                                                                                                  0.3))
                self.elements.extend([self.title2, self.description2, self.image2])
            for node in self.elements:
                node.setTransparency(1)
                node.setColorScale(1, 1, 1, 0)

    def makeInterval(self):
        if self.special == 'final':
            return Sequence(ParentInterval(self.sceneRoot, render), Func(doFade, 'in', self.elements), Wait(3), Func(doFade, 'hide', self.elements), ParentInterval(self.sceneRoot, hidden))
        else:
            return Sequence(ParentInterval(self.sceneRoot, render), Func(doFade, 'in', self.elements), Wait(3.5), Func(doFade, 'out', self.elements), Wait(0.5), ParentInterval(self.sceneRoot, hidden))

    def unload(self):
        self.sceneRoot.removeNode()
        self.title.removeNode()
        self.description.removeNode()
        self.image.removeNode()
        self.elements = None
        self.toonName = None
        self.toonDescription = None
        self.toonImage = None
        self.side = None
        return


CreditsScenes = [
 Logano(),
 Credits('B.D. Pinkermash', 'Nerd\nSecondary Developer', 'sparky.png', 'left', 2, 'Ned', 'Certified House Sitter\nDeveloper', 'nedpls.png'),
 Credits('Sparkpin', 'Election Encoder\nNot a Donkey\nAssistant Developer', 'sparkpin.png', 'right', 2, 'Super Tricky', 'Fishing Specialist\nDeveloper', 'supertricky.png'),
 Credits('Giggletwist', 'Infinite Creativity\nDeveloper', 'giggletwist.png', 'right', 2, 'QED', 'Contributor of many\nMagic Words!', 'qed.png'),
 Credits('Sweet Ratt', 'Actually Sour\nField Office Model Repairman', 'sweetratt.png', 'right', 2, 'S.P. MacSpeed', 'Field Officer\nTTH Developer', 'sillypeppymacspeed.png'),
 Credits('Loblao', 'Factory Night Guard\nTTH Developer', 'loblao.png', 'left', 2, 'Yorke', 'Minty Fresh\nDoomsday Orchestrator', 'yorke.jpg'),
 Credits('Bear E. Funny', 'Laughter Master\nCage Constructor\nCog ID-er', 'bear3funny.png', 'left', 2, 'Odie', 'Kicked off the Table\nRadar Manager\nSewer Architect', 'jaquanza.jpg'),
 Credits('Rocky Reborn', 'Strong Soldier\nDoomsday Designer', 'strongsoldier.jpg', 'left'),
 Credits('Disney Online', 'The owners and creators\nof Toontown.', '11-20-13_donald.jpg', 'left', 2, 'VR Studio', 'For developing Toontown Online.', '11-15-13_grey.jpg'),
 Credits('TTR Team', 'For reviving Toontown\nand allowing us to\ncontinue forward!', 'toontownrewritten.png', 'left')]
FakeRockyCredit = Credits('Odie', 'Kicked off the Table\nRadar Manager', 'jaquanza.jpg', 'left', 2, 'Rocky Reborn', 'Strong Soldier\nSpeech Writer', 'strongsoldier.jpg')