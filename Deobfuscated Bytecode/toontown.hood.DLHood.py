# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.hood.DLHood
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
import ToonHood
from toontown.town import DLTownLoader
from toontown.safezone import DLSafeZoneLoader
from toontown.toonbase.ToontownGlobals import *

class DLHood(ToonHood.ToonHood):

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        ToonHood.ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = DonaldsDreamland
        self.townLoaderClass = DLTownLoader.DLTownLoader
        self.safeZoneLoaderClass = DLSafeZoneLoader.DLSafeZoneLoader
        self.storageDNAFile = 'phase_8/dna/storage_DL.pdna'
        self.holidayStorageDNADict = {WINTER_DECORATIONS: ['phase_8/dna/winter_storage_DL.pdna'], WACKY_WINTER_DECORATIONS: [
                                    'phase_8/dna/winter_storage_DL.pdna'], 
           HALLOWEEN_PROPS: [
                           'phase_8/dna/halloween_props_storage_DL.pdna'], 
           SPOOKY_PROPS: [
                        'phase_8/dna/halloween_props_storage_DL.pdna']}
        self.skyFile = 'phase_8/models/props/DL_sky'
        self.titleColor = (1.0, 0.9, 0.5, 1.0)

    def load(self):
        ToonHood.ToonHood.load(self)
        self.parentFSM.getStateNamed('DLHood').addChild(self.fsm)

    def unload(self):
        self.parentFSM.getStateNamed('DLHood').removeChild(self.fsm)
        ToonHood.ToonHood.unload(self)

    def enter(self, *args):
        ToonHood.ToonHood.enter(self, *args)

    def exit(self):
        ToonHood.ToonHood.exit(self)