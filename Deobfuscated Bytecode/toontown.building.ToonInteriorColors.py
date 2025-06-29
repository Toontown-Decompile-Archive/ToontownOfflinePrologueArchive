# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.building.ToonInteriorColors
# Compiled at: 2014-04-30 09:53:54
from toontown.toonbase.ToontownGlobals import *
wainscottingBase = [
 Vec4(0.8, 0.5, 0.3, 1.0), Vec4(0.699, 0.586, 0.473, 1.0), Vec4(0.473, 0.699, 0.488, 1.0)]
wallpaperBase = [Vec4(1.0, 1.0, 0.7, 1.0),
 Vec4(0.8, 1.0, 0.7, 1.0),
 Vec4(0.4, 0.5, 0.4, 1.0),
 Vec4(0.5, 0.7, 0.6, 1.0)]
wallpaperBorderBase = [Vec4(1.0, 1.0, 0.7, 1.0),
 Vec4(0.8, 1.0, 0.7, 1.0),
 Vec4(0.4, 0.5, 0.4, 1.0),
 Vec4(0.5, 0.7, 0.6, 1.0)]
doorBase = [Vec4(1.0, 1.0, 0.7, 1.0)]
floorBase = [Vec4(0.746, 1.0, 0.477, 1.0), Vec4(1.0, 0.684, 0.477, 1.0)]
baseScheme = {'TI_wainscotting': wainscottingBase, 'TI_wallpaper': wallpaperBase, 
   'TI_wallpaper_border': wallpaperBorderBase, 
   'TI_door': doorBase, 
   'TI_floor': floorBase}
colors = {DonaldsDock: {'TI_wainscotting': wainscottingBase, 'TI_wallpaper': wallpaperBase, 
                 'TI_wallpaper_border': wallpaperBorderBase, 
                 'TI_door': doorBase, 
                 'TI_floor': floorBase}, 
   ToontownCentral: {'TI_wainscotting': wainscottingBase, 'TI_wallpaper': wallpaperBase, 
                     'TI_wallpaper_border': wallpaperBorderBase, 
                     'TI_door': doorBase + [Vec4(0.8, 0.5, 0.3, 1.0)], 
                     'TI_floor': floorBase}, 
   TheBrrrgh: baseScheme, 
   MinniesMelodyland: baseScheme, 
   DaisyGardens: baseScheme, 
   OldDaisyGardens: baseScheme, 
   GoofySpeedway: baseScheme, 
   DonaldsDreamland: {'TI_wainscotting': wainscottingBase, 'TI_wallpaper': wallpaperBase, 
                      'TI_wallpaper_border': wallpaperBorderBase, 
                      'TI_door': doorBase, 
                      'TI_floor': floorBase}, 
   Tutorial: {'TI_wainscotting': wainscottingBase, 'TI_wallpaper': wallpaperBase, 
              'TI_wallpaper_border': wallpaperBorderBase, 
              'TI_door': doorBase + [Vec4(0.8, 0.5, 0.3, 1.0)], 
              'TI_floor': floorBase}, 
   MyEstate: baseScheme}