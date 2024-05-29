# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.nametag.NametagGlobals
# Compiled at: 2014-04-30 09:53:54
camera = None

def setCamera(cam):
    global camera
    camera = cam


arrowModel = None

def setArrowModel(am):
    global arrowModel
    arrowModel = am


nametagCardModel = None
nametagCardDimensions = None

def setNametagCard(model, dimensions):
    global nametagCardDimensions
    global nametagCardModel
    nametagCardModel = model
    nametagCardDimensions = dimensions


mouseWatcher = None

def setMouseWatcher(mw):
    global mouseWatcher
    mouseWatcher = mw


speechBalloon3d = None

def setSpeechBalloon3d(sb3d):
    global speechBalloon3d
    speechBalloon3d = sb3d


thoughtBalloon3d = None

def setThoughtBalloon3d(tb3d):
    global thoughtBalloon3d
    thoughtBalloon3d = tb3d


speechBalloon2d = None

def setSpeechBalloon2d(sb2d):
    global speechBalloon2d
    speechBalloon2d = sb2d


thoughtBalloon2d = None

def setThoughtBalloon2d(tb2d):
    global thoughtBalloon2d
    thoughtBalloon2d = tb2d


pageButtons = {}

def setPageButton(state, model):
    pageButtons[state] = model


quitButtons = {}

def setQuitButton(state, model):
    quitButtons[state] = model


rolloverSound = None

def setRolloverSound(ros):
    global rolloverSound
    rolloverSound = ros


clickSound = None

def setClickSound(cs):
    global clickSound
    clickSound = cs


toon = None

def setToon(t):
    global toon
    toon = t


masterArrowsOn = 0

def setMasterArrowsOn(mao):
    global masterArrowsOn
    masterArrowsOn = mao


masterNametagsActive = 0

def setMasterNametagsActive(mna):
    global masterNametagsActive
    masterNametagsActive = mna


min2dAlpha = 0.0

def setMin2dAlpha(m2a):
    global min2dAlpha
    min2dAlpha = m2a


def getMin2dAlpha():
    return min2dAlpha


max2dAlpha = 0.0

def setMax2dAlpha(m2a):
    global max2dAlpha
    max2dAlpha = m2a


def getMax2dAlpha():
    return max2dAlpha


onscreenChatForced = 0

def setOnscreenChatForced(ocf):
    global onscreenChatForced
    onscreenChatForced = ocf


def setGlobalNametagScale(s):
    pass