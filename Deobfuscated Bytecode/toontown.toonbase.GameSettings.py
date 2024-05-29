# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.toonbase.GameSettings
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from pandac.PandaModules import loadPrcFileData
from otp.otpbase.Settings import Settings

class GameSettings:
    notify = DirectNotifyGlobal.directNotify.newCategory('GameSettings')

    def __init__(self):
        self.settings = Settings()
        self.loadFromSettings()

    def loadFromSettings(self):
        electionEvent = self.settings.getBool('game', 'elections', False)
        loadPrcFileData('toonBase Settings Election Active', 'want-doomsday %s' % electionEvent)
        if electionEvent:
            loadPrcFileData('toonBase Settings Election Active', 'want-prologue #f')
        self.settings.updateSetting('game', 'elections', electionEvent)
        self.electionEvent = electionEvent
        retroMode = self.settings.getBool('game', 'retro', False)
        loadPrcFileData('toonBase Settings TTO Map Hover', 'want-map-hover %s' % retroMode)
        loadPrcFileData('toonBase Settings TTO Loading Screen', 'want-tto-loading-screen %s' % retroMode)
        loadPrcFileData('toonBase Settings TTO Localizers', 'want-tto-text %s' % retroMode)
        loadPrcFileData('toonBase Settings TTO Theme Song', 'want-tto-theme %s' % retroMode)
        loadPrcFileData('toonBase Settings TTO Catalog Screen', 'want-tto-catalog %s' % retroMode)
        loadPrcFileData('toonBase Settings TTO Fireworks', 'want-old-fireworks %s' % retroMode)
        loadPrcFileData('toonBase Settings TTO Run Sound', 'want-tto-runsound %s' % retroMode)
        loadPrcFileData('toonBase Settings TTO Nametag Colors', 'want-tto-tags %s' % retroMode)
        self.settings.updateSetting('game', 'retro', retroMode)
        self.retroMode = retroMode
        aspect = self.settings.getBool('game', 'stretched-screen', False)
        loadPrcFileData('toonBase Settings Aspect Ratio', 'aspect-ratio 1.33' if aspect else '0')
        self.settings.updateSetting('game', 'stretched-screen', aspect)
        self.aspect = aspect
        randomInvasions = self.settings.getBool('game', 'random-invasions', True)
        loadPrcFileData('toonBase Settings Random Invasions', 'want-random-invasions %s' % randomInvasions)
        self.settings.updateSetting('game', 'random-invasions', randomInvasions)
        self.randomInvasions = randomInvasions
        nerfs = self.settings.getBool('game', 'nerfs', True)
        loadPrcFileData('toonBase Settings Nerfs', 'want-nerfs %s' % nerfs)
        self.settings.updateSetting('game', 'nerfs', nerfs)
        self.nerfs = nerfs
        software = self.settings.getBool('game', 'software-render', False)
        loadPrcFileData('toonBase Settings Software Rendering', 'framebuffer-hardware %s' % (not software))
        loadPrcFileData('toonBase Settings Software Rendering', 'framebuffer-software %s' % software)
        self.settings.updateSetting('game', 'software-render', software)
        self.software = software
        oeuf = self.settings.getBool('game', 'oeuf', False)
        loadPrcFileData('toonBase Settings oeuf', 'check-language %s' % oeuf)
        loadPrcFileData('toonBase Settings oeuf', 'language french' if oeuf else 'english')
        self.settings.updateSetting('game', 'oeuf', oeuf)
        self.oeuf = oeuf