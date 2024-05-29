# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.coghq.FactoryEntityCreator
# Compiled at: 2014-04-30 09:53:54
from otp.level import EntityCreator
import FactoryLevelMgr, PlatformEntity, ConveyorBelt, GearEntity, PaintMixer, GoonClipPlane, MintProduct, MintProductPallet, MintShelf, PathMasterEntity, RenderingEntity

class FactoryEntityCreator(EntityCreator.EntityCreator):

    def __init__(self, level):
        EntityCreator.EntityCreator.__init__(self, level)
        nothing = EntityCreator.nothing
        nonlocal = EntityCreator.nonlocal
        self.privRegisterTypes({'activeCell': nonlocal, 'crusherCell': nonlocal, 
           'battleBlocker': nonlocal, 
           'beanBarrel': nonlocal, 
           'button': nonlocal, 
           'conveyorBelt': ConveyorBelt.ConveyorBelt, 
           'crate': nonlocal, 
           'door': nonlocal, 
           'directionalCell': nonlocal, 
           'gagBarrel': nonlocal, 
           'gear': GearEntity.GearEntity, 
           'goon': nonlocal, 
           'gridGoon': nonlocal, 
           'golfGreenGame': nonlocal, 
           'goonClipPlane': GoonClipPlane.GoonClipPlane, 
           'grid': nonlocal, 
           'healBarrel': nonlocal, 
           'levelMgr': FactoryLevelMgr.FactoryLevelMgr, 
           'lift': nonlocal, 
           'mintProduct': MintProduct.MintProduct, 
           'mintProductPallet': MintProductPallet.MintProductPallet, 
           'mintShelf': MintShelf.MintShelf, 
           'mover': nonlocal, 
           'paintMixer': PaintMixer.PaintMixer, 
           'pathMaster': PathMasterEntity.PathMasterEntity, 
           'rendering': RenderingEntity.RenderingEntity, 
           'platform': PlatformEntity.PlatformEntity, 
           'sinkingPlatform': nonlocal, 
           'stomper': nonlocal, 
           'stomperPair': nonlocal, 
           'laserField': nonlocal, 
           'securityCamera': nonlocal, 
           'elevatorMarker': nonlocal, 
           'trigger': nonlocal, 
           'moleField': nonlocal, 
           'maze': nonlocal})