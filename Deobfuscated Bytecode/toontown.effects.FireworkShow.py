# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.effects.FireworkShow
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from toontown.effects.FireworkGlobals import *
from toontown.effects.Firework import Firework
from toontown.toonbase import ToontownGlobals
from toontown.parties import PartyGlobals
import random
colors = [
 Vec4(1, 1, 1, 1),
 Vec4(1, 0.1, 0.1, 1),
 Vec4(0.1, 1, 0.1, 1),
 Vec4(0.3, 1, 0.3, 1),
 Vec4(0.2, 0.2, 1, 1),
 Vec4(1, 1, 0.1, 1),
 Vec4(1, 0.5, 0.1, 1),
 Vec4(1, 0.1, 1, 1),
 Vec4(0.1, 1, 1, 1),
 Vec4(0.1, 0.5, 1, 1)]
fireworkShowTypes = [ToontownGlobals.JULY4_FIREWORKS,
 PartyGlobals.FireworkShows.Summer,
 ToontownGlobals.NEWYEARS_FIREWORKS,
 ToontownGlobals.COMBO_FIREWORKS]

class FireworkShow(NodePath):

    def r():
        return random.randint(8, 12) / 10.0

    def rV():
        return Vec3(random.randint(-60, 60), random.randint(10, 30), random.randint(125, 150))

    def rP():
        return Point3(0, 0, 0)

    def rS():
        return 1.0 + random.random() / 2.0

    def rC():
        return random.choice(colors)

    def rT():
        return random.randint(12, 20) / 10.0

    def rD():
        return random.randint(1, 20) / 10.0

    showData = {ToontownGlobals.JULY4_FIREWORKS: [
                                       [FireworkType.GlowFlare,
                                        Vec3(-90, 0, 80),
                                        Vec3(120, 0, 0),
                                        rS(),
                                        Vec4(1, 1, 1, 1),
                                        Vec4(1, 1, 1, 1),
                                        1.5,
                                        0.0],
                                       [
                                        FireworkType.GlowFlare,
                                        Vec3(90, 0, 80),
                                        Vec3(-120, 0, 0),
                                        rS(),
                                        Vec4(1, 1, 1, 1),
                                        Vec4(1, 1, 1, 1),
                                        1.5,
                                        1.0],
                                       [
                                        FireworkType.BasicPeony,
                                        Vec3(50, 0, 140),
                                        rP(),
                                        rS(),
                                        Vec4(1, 1, 1, 1),
                                        Vec4(1, 1, 1, 1),
                                        rT(),
                                        0.0],
                                       [
                                        FireworkType.BasicPeony,
                                        Vec3(-50, 0, 140),
                                        rP(),
                                        rS(),
                                        Vec4(1, 1, 1, 1),
                                        Vec4(1, 1, 1, 1),
                                        rT(),
                                        3.0],
                                       [
                                        FireworkType.AdvancedPeony,
                                        Vec3(-90, 0, 110),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        0.25],
                                       [
                                        FireworkType.AdvancedPeony,
                                        Vec3(0, 0, 90),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        0.25],
                                       [
                                        FireworkType.AdvancedPeony,
                                        Vec3(90, 0, 110),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        4.0],
                                       [
                                        FireworkType.GlowFlare,
                                        Vec3(-90, 0, 80),
                                        Vec3(120, 0, 0),
                                        1.5,
                                        Vec4(1, 1, 1, 1),
                                        Vec4(1, 1, 1, 1),
                                        3.0,
                                        3.0],
                                       [
                                        FireworkType.Ring,
                                        Vec3(-90, 0, 120),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        0.2],
                                       [
                                        FireworkType.Ring,
                                        Vec3(-30, 0, 100),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        0.2],
                                       [
                                        FireworkType.Ring,
                                        Vec3(30, 0, 120),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        0.2],
                                       [
                                        FireworkType.Ring,
                                        Vec3(90, 0, 100),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        3.0],
                                       [
                                        FireworkType.Bees,
                                        Vec3(0, 50, 120),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        2.0],
                                       [
                                        FireworkType.TrailBurst,
                                        Vec3(-70, 0, 120),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        0.25],
                                       [
                                        FireworkType.TrailBurst,
                                        Vec3(70, 0, 120),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        3.0],
                                       [
                                        FireworkType.DiademPeony,
                                        Vec3(90, 0, 120),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        0.15],
                                       [
                                        FireworkType.DiademPeony,
                                        Vec3(-30, 0, 120),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        0.15],
                                       [
                                        FireworkType.DiademPeony,
                                        Vec3(30, 0, 100),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        0.15],
                                       [
                                        FireworkType.DiademPeony,
                                        Vec3(-90, 0, 100),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        3.0],
                                       [
                                        FireworkType.PalmTree,
                                        Vec3(0, 40, 100),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        4.0],
                                       [
                                        FireworkType.Chrysanthemum,
                                        rV(),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        0.0],
                                       [
                                        FireworkType.DiademChrysanthemum,
                                        rV(),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        0.5],
                                       [
                                        FireworkType.DiademChrysanthemum,
                                        rV(),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        3.0],
                                       [
                                        FireworkType.Saturn,
                                        Vec3(90, 0, 120),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        0.0],
                                       [
                                        FireworkType.Saturn,
                                        Vec3(-90, 0, 120),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        2.5],
                                       [
                                        FireworkType.GlowFlare,
                                        Vec3(0, 0, 90),
                                        Vec3(-120, 0, 0),
                                        rS(),
                                        Vec4(0.1, 0.5, 1, 1),
                                        Vec4(1, 1, 1, 1),
                                        1.5,
                                        1.0],
                                       [
                                        FireworkType.GlowFlare,
                                        Vec3(0, 0, 100),
                                        Vec3(-60, 0, 0),
                                        rS(),
                                        Vec4(0.1, 0.5, 1, 1),
                                        Vec4(1, 1, 1, 1),
                                        1.5,
                                        1.0],
                                       [
                                        FireworkType.GlowFlare,
                                        Vec3(0, 0, 110),
                                        Vec3(0, 0, 0),
                                        rS(),
                                        Vec4(0.1, 0.5, 1, 1),
                                        Vec4(1, 1, 1, 1),
                                        1.5,
                                        1.0],
                                       [
                                        FireworkType.GlowFlare,
                                        Vec3(0, 0, 120),
                                        Vec3(60, 0, 0),
                                        rS(),
                                        Vec4(0.1, 0.5, 1, 1),
                                        Vec4(1, 1, 1, 1),
                                        1.5,
                                        1.0],
                                       [
                                        FireworkType.GlowFlare,
                                        Vec3(0, 0, 130),
                                        Vec3(120, 0, 0),
                                        rS(),
                                        Vec4(0.1, 0.5, 1, 1),
                                        Vec4(1, 1, 1, 1),
                                        1.5,
                                        2.0],
                                       [
                                        FireworkType.DiademChrysanthemum,
                                        rV(),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        0.5],
                                       [
                                        FireworkType.DiademChrysanthemum,
                                        rV(),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        2.0],
                                       [
                                        FireworkType.DiademChrysanthemum,
                                        rV(),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        0.5],
                                       [
                                        FireworkType.DiademChrysanthemum,
                                        rV(),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        2.0],
                                       [
                                        FireworkType.DiademChrysanthemum,
                                        rV(),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        0.5],
                                       [
                                        FireworkType.DiademChrysanthemum,
                                        rV(),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        1.0],
                                       [
                                        FireworkType.DiademChrysanthemum,
                                        rV(),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        0.5],
                                       [
                                        FireworkType.DiademChrysanthemum,
                                        rV(),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        3.0],
                                       [
                                        FireworkType.AmericanFlag,
                                        Vec3(0, 0, 230),
                                        Vec3(-50, 0, 0),
                                        rS(),
                                        rC(),
                                        rC(),
                                        rT(),
                                        6],
                                       [
                                        FireworkType.DiademPeony,
                                        Vec3(90, 0, 120),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        2.5,
                                        0.15],
                                       [
                                        FireworkType.DiademPeony,
                                        Vec3(30, 0, 140),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        2.5,
                                        0.15],
                                       [
                                        FireworkType.DiademPeony,
                                        Vec3(-30, 0, 120),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        2.5,
                                        0.15],
                                       [
                                        FireworkType.DiademPeony,
                                        Vec3(-90, 0, 140),
                                        rP(),
                                        rS(),
                                        rC(),
                                        rC(),
                                        2.5,
                                        3.0],
                                       [
                                        FireworkType.Mickey,
                                        Vec3(0, 0, 100),
                                        rP(),
                                        1.4,
                                        rC(),
                                        rC(),
                                        2.0,
                                        10.0]], 
       PartyGlobals.FireworkShows.Summer: [
                                         [
                                          FireworkType.DiademPeony,
                                          Vec3(90, 0, 120),
                                          rP(),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          0.0],
                                         [
                                          FireworkType.DiademPeony,
                                          Vec3(0, 0, 70),
                                          rP(),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          0.0],
                                         [
                                          FireworkType.DiademPeony,
                                          Vec3(-90, 0, 100),
                                          rP(),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          3.0],
                                         [
                                          FireworkType.GlowFlare,
                                          Vec3(0, 0, 130),
                                          Vec3(0, 0, 0),
                                          rS(),
                                          Vec4(0.1, 0.5, 1, 1),
                                          Vec4(1, 1, 1, 1),
                                          3.5,
                                          1.0],
                                         [
                                          FireworkType.GlowFlare,
                                          Vec3(0, 0, 90),
                                          Vec3(-50, 0, 0),
                                          rS(),
                                          Vec4(0.1, 0.5, 1, 1),
                                          Vec4(1, 1, 1, 1),
                                          2.5,
                                          0.0],
                                         [
                                          FireworkType.GlowFlare,
                                          Vec3(0, 0, 90),
                                          Vec3(50, 0, 0),
                                          rS(),
                                          Vec4(0.1, 0.5, 1, 1),
                                          Vec4(1, 1, 1, 1),
                                          2.5,
                                          2.0],
                                         [
                                          FireworkType.DiademChrysanthemum,
                                          Vec3(40, 50, 140),
                                          rP(),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          1.5],
                                         [
                                          FireworkType.DiademChrysanthemum,
                                          Vec3(-40, -50, 140),
                                          rP(),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          3.0],
                                         [
                                          FireworkType.GlowFlare,
                                          Vec3(-90, 0, 80),
                                          Vec3(120, 0, 0),
                                          1.5,
                                          Vec4(1, 1, 1, 1),
                                          Vec4(1, 1, 1, 1),
                                          3.0,
                                          5.5],
                                         [
                                          FireworkType.DiademChrysanthemum,
                                          Vec3(0, 0, 100),
                                          Vec3(-120, 0, 0),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          0.5],
                                         [
                                          FireworkType.GlowFlare,
                                          Vec3(0, 0, 100),
                                          Vec3(-120, 0, 0),
                                          rS(),
                                          rC(),
                                          rC(),
                                          1.5,
                                          1.0],
                                         [
                                          FireworkType.DiademChrysanthemum,
                                          Vec3(0, 0, 100),
                                          Vec3(0, 20, 0),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          0.5],
                                         [
                                          FireworkType.GlowFlare,
                                          Vec3(0, 0, 100),
                                          Vec3(0, 20, 0),
                                          rS(),
                                          rC(),
                                          rC(),
                                          1.5,
                                          1.0],
                                         [
                                          FireworkType.DiademChrysanthemum,
                                          Vec3(0, 0, 100),
                                          Vec3(120, 0, 0),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          0.5],
                                         [
                                          FireworkType.GlowFlare,
                                          Vec3(0, 0, 100),
                                          Vec3(120, 0, 0),
                                          rS(),
                                          rC(),
                                          rC(),
                                          1.5,
                                          5.0],
                                         [
                                          FireworkType.AdvancedPeony,
                                          Vec3(-90, 0, 110),
                                          rP(),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          0.25],
                                         [
                                          FireworkType.AdvancedPeony,
                                          Vec3(0, 0, 90),
                                          rP(),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          0.25],
                                         [
                                          FireworkType.AdvancedPeony,
                                          Vec3(90, 0, 110),
                                          rP(),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          4.0],
                                         [
                                          FireworkType.Mickey,
                                          Vec3(70, 0, 120),
                                          rP(),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          3.0],
                                         [
                                          FireworkType.DiademPeony,
                                          Vec3(90, 0, 120),
                                          rP(),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          0.15],
                                         [
                                          FireworkType.DiademPeony,
                                          Vec3(-30, 0, 120),
                                          rP(),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          0.15],
                                         [
                                          FireworkType.DiademPeony,
                                          Vec3(30, 0, 100),
                                          rP(),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          0.15],
                                         [
                                          FireworkType.DiademPeony,
                                          Vec3(-90, 0, 100),
                                          rP(),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          3.0],
                                         [
                                          FireworkType.Bees,
                                          Vec3(0, 0, 100),
                                          rP(),
                                          1.4,
                                          rC(),
                                          rC(),
                                          2.0,
                                          4.0],
                                         [
                                          FireworkType.Chrysanthemum,
                                          rV(),
                                          rP(),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          0.0],
                                         [
                                          FireworkType.DiademChrysanthemum,
                                          rV(),
                                          rP(),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          0.5],
                                         [
                                          FireworkType.DiademChrysanthemum,
                                          rV(),
                                          rP(),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          3.0],
                                         [
                                          FireworkType.GlowFlare,
                                          Vec3(200, 0, 180),
                                          Vec3(-60, 0, 0),
                                          rS(),
                                          rC(),
                                          Vec4(1, 1, 1, 1),
                                          1.5,
                                          2.0],
                                         [
                                          FireworkType.GlowFlare,
                                          Vec3(150, 10, 180),
                                          Vec3(-60, 0, 0),
                                          rS(),
                                          rC(),
                                          Vec4(1, 1, 1, 1),
                                          1.5,
                                          1.0],
                                         [
                                          FireworkType.GlowFlare,
                                          Vec3(100, 20, 180),
                                          Vec3(-60, 0, 0),
                                          rS(),
                                          rC(),
                                          Vec4(1, 1, 1, 1),
                                          1.5,
                                          1.0],
                                         [
                                          FireworkType.GlowFlare,
                                          Vec3(50, 30, 180),
                                          Vec3(-60, 0, 0),
                                          rS(),
                                          rC(),
                                          Vec4(1, 1, 1, 1),
                                          1.5,
                                          1.0],
                                         [
                                          FireworkType.GlowFlare,
                                          Vec3(0, 40, 180),
                                          Vec3(-60, 0, 0),
                                          rS(),
                                          rC(),
                                          Vec4(1, 1, 1, 1),
                                          1.5,
                                          2.0],
                                         [
                                          FireworkType.Saturn,
                                          Vec3(0, 0, 100),
                                          Vec3(-120, 0, 0),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          0.5],
                                         [
                                          FireworkType.GlowFlare,
                                          Vec3(0, 0, 100),
                                          Vec3(-120, 0, 0),
                                          rS(),
                                          rC(),
                                          rC(),
                                          1.5,
                                          1.0],
                                         [
                                          FireworkType.Saturn,
                                          Vec3(0, 0, 100),
                                          Vec3(0, 0, 0),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          0.5],
                                         [
                                          FireworkType.GlowFlare,
                                          Vec3(0, 0, 100),
                                          Vec3(0, 0, 0),
                                          rS(),
                                          rC(),
                                          rC(),
                                          1.5,
                                          1.0],
                                         [
                                          FireworkType.Saturn,
                                          Vec3(0, 0, 100),
                                          Vec3(120, 0, 0),
                                          rS(),
                                          rC(),
                                          rC(),
                                          rT(),
                                          0.5],
                                         [
                                          FireworkType.GlowFlare,
                                          Vec3(0, 0, 100),
                                          Vec3(120, 0, 0),
                                          rS(),
                                          rC(),
                                          rC(),
                                          1.5,
                                          5.0],
                                         [
                                          FireworkType.GlowFlare,
                                          Vec3(-15, 0, 60),
                                          Vec3(0, 0, 0),
                                          rS(),
                                          Vec4(1, 1, 0.4, 1),
                                          Vec4(1, 1, 1, 1),
                                          2.5,
                                          0.0],
                                         [
                                          FireworkType.GlowFlare,
                                          Vec3(15, 0, 60),
                                          Vec3(0, 0, 0),
                                          rS(),
                                          Vec4(1, 1, 0.4, 1),
                                          Vec4(1, 1, 1, 1),
                                          2.5,
                                          0.0],
                                         [
                                          FireworkType.IceCream,
                                          Vec3(0, 0, 80),
                                          Vec3(0, 0, 0),
                                          1.0,
                                          Vec4(1, 1, 1, 1),
                                          Vec4(1, 1, 1, 1),
                                          1.5,
                                          0.0],
                                         [
                                          FireworkType.IceCream,
                                          Vec3(0, 0, 110),
                                          Vec3(0, 0, 0),
                                          0.6,
                                          Vec4(1, 1, 1, 1),
                                          Vec4(1, 1, 1, 1),
                                          1.5,
                                          0.0],
                                         [
                                          FireworkType.IceCream,
                                          Vec3(0, 0, 130),
                                          Vec3(0, 0, 0),
                                          0.3,
                                          Vec4(1, 1, 1, 1),
                                          Vec4(1, 1, 1, 1),
                                          1.5,
                                          10.0]], 
       ToontownGlobals.NEWYEARS_FIREWORKS: [
                                          [
                                           FireworkType.GlowFlare,
                                           Vec3(0, 0, 180),
                                           Vec3(-120, 0, 0),
                                           rS(),
                                           rC(),
                                           Vec4(1, 1, 1, 1),
                                           1.5,
                                           1.0],
                                          [
                                           FireworkType.GlowFlare,
                                           Vec3(0, 0, 120),
                                           Vec3(-60, 0, 0),
                                           rS(),
                                           rC(),
                                           Vec4(1, 1, 1, 1),
                                           1.5,
                                           1.0],
                                          [
                                           FireworkType.GlowFlare,
                                           Vec3(0, 0, 80),
                                           Vec3(-10, 0, 0),
                                           rS(),
                                           rC(),
                                           Vec4(1, 1, 1, 1),
                                           1.5,
                                           1.0],
                                          [
                                           FireworkType.GlowFlare,
                                           Vec3(0, 0, 80),
                                           Vec3(10, 0, 0),
                                           rS(),
                                           rC(),
                                           Vec4(1, 1, 1, 1),
                                           1.5,
                                           1.0],
                                          [
                                           FireworkType.GlowFlare,
                                           Vec3(0, 0, 120),
                                           Vec3(60, 0, 0),
                                           rS(),
                                           rC(),
                                           Vec4(1, 1, 1, 1),
                                           1.5,
                                           1.0],
                                          [
                                           FireworkType.GlowFlare,
                                           Vec3(0, 0, 180),
                                           Vec3(120, 0, 0),
                                           rS(),
                                           rC(),
                                           Vec4(1, 1, 1, 1),
                                           1.5,
                                           2.0],
                                          [
                                           FireworkType.GlowFlare,
                                           Vec3(0, 0, 80),
                                           Vec3(120, 0, 0),
                                           rS(),
                                           rC(),
                                           Vec4(1, 1, 1, 1),
                                           1.5,
                                           1.0],
                                          [
                                           FireworkType.GlowFlare,
                                           Vec3(0, 0, 120),
                                           Vec3(60, 0, 0),
                                           rS(),
                                           rC(),
                                           Vec4(1, 1, 1, 1),
                                           1.5,
                                           1.0],
                                          [
                                           FireworkType.GlowFlare,
                                           Vec3(0, 0, 180),
                                           Vec3(10, 0, 0),
                                           rS(),
                                           rC(),
                                           Vec4(1, 1, 1, 1),
                                           1.5,
                                           1.0],
                                          [
                                           FireworkType.GlowFlare,
                                           Vec3(0, 0, 180),
                                           Vec3(-10, 0, 0),
                                           rS(),
                                           rC(),
                                           Vec4(1, 1, 1, 1),
                                           1.5,
                                           1.0],
                                          [
                                           FireworkType.GlowFlare,
                                           Vec3(0, 0, 120),
                                           Vec3(-60, 0, 0),
                                           rS(),
                                           rC(),
                                           Vec4(1, 1, 1, 1),
                                           1.5,
                                           1.0],
                                          [
                                           FireworkType.GlowFlare,
                                           Vec3(0, 0, 80),
                                           Vec3(-120, 0, 0),
                                           rS(),
                                           rC(),
                                           Vec4(1, 1, 1, 1),
                                           1.5,
                                           2.0],
                                          [
                                           FireworkType.GlowFlare,
                                           Vec3(-180, 0, 180),
                                           Vec3(-60, 0, 0),
                                           rS(),
                                           rC(),
                                           Vec4(1, 1, 1, 1),
                                           2.5,
                                           0.15],
                                          [
                                           FireworkType.GlowFlare,
                                           Vec3(180, 0, 180),
                                           Vec3(60, 0, 0),
                                           rS(),
                                           rC(),
                                           Vec4(1, 1, 1, 1),
                                           2.5,
                                           0.15],
                                          [
                                           FireworkType.DiademChrysanthemum,
                                           Vec3(40, 50, 140),
                                           rP(),
                                           rS(),
                                           rC(),
                                           rC(),
                                           rT(),
                                           1.5],
                                          [
                                           FireworkType.DiademChrysanthemum,
                                           Vec3(-40, -50, 140),
                                           rP(),
                                           rS(),
                                           rC(),
                                           rC(),
                                           rT(),
                                           3.0],
                                          [
                                           FireworkType.DiademChrysanthemum,
                                           Vec3(-140, 50, 120),
                                           Vec3(0, 0, 0),
                                           rS(),
                                           rC(),
                                           rC(),
                                           rT(),
                                           0.25],
                                          [
                                           FireworkType.DiademChrysanthemum,
                                           Vec3(70, -40, 90),
                                           Vec3(0, 0, 0),
                                           rS(),
                                           rC(),
                                           rC(),
                                           1.5,
                                           0.25],
                                          [
                                           FireworkType.DiademChrysanthemum,
                                           Vec3(-100, 30, 60),
                                           Vec3(0, 0, 0),
                                           rS(),
                                           rC(),
                                           rC(),
                                           rT(),
                                           0.25],
                                          [
                                           FireworkType.DiademChrysanthemum,
                                           Vec3(0, 20, 100),
                                           Vec3(0, 0, 0),
                                           rS(),
                                           rC(),
                                           rC(),
                                           1.5,
                                           0.25],
                                          [
                                           FireworkType.DiademChrysanthemum,
                                           Vec3(-70, 0, 130),
                                           Vec3(0, 0, 0),
                                           rS(),
                                           rC(),
                                           rC(),
                                           rT(),
                                           0.5],
                                          [
                                           FireworkType.DiademChrysanthemum,
                                           Vec3(120, 50, 100),
                                           Vec3(0, 0, 0),
                                           rS(),
                                           rC(),
                                           rC(),
                                           1.5,
                                           3.5],
                                          [
                                           FireworkType.Mickey,
                                           Vec3(70, 0, 120),
                                           rP(),
                                           rS(),
                                           rC(),
                                           rC(),
                                           rT(),
                                           3.5],
                                          [
                                           FireworkType.DiademPeony,
                                           Vec3(90, 0, 120),
                                           rP(),
                                           rS(),
                                           rC(),
                                           rC(),
                                           rT(),
                                           0.15],
                                          [
                                           FireworkType.DiademPeony,
                                           Vec3(-30, 0, 120),
                                           rP(),
                                           rS(),
                                           rC(),
                                           rC(),
                                           rT(),
                                           0.15],
                                          [
                                           FireworkType.DiademPeony,
                                           Vec3(30, 0, 100),
                                           rP(),
                                           rS(),
                                           rC(),
                                           rC(),
                                           rT(),
                                           0.15],
                                          [
                                           FireworkType.DiademPeony,
                                           Vec3(-90, 0, 100),
                                           rP(),
                                           rS(),
                                           rC(),
                                           rC(),
                                           rT(),
                                           3.0],
                                          [
                                           FireworkType.Chrysanthemum,
                                           rV(),
                                           rP(),
                                           rS(),
                                           rC(),
                                           rC(),
                                           rT(),
                                           0.15],
                                          [
                                           FireworkType.DiademChrysanthemum,
                                           rV(),
                                           rP(),
                                           rS(),
                                           rC(),
                                           rC(),
                                           rT(),
                                           0.5],
                                          [
                                           FireworkType.DiademChrysanthemum,
                                           rV(),
                                           rP(),
                                           rS(),
                                           rC(),
                                           rC(),
                                           rT(),
                                           1.5],
                                          [
                                           FireworkType.DiademChrysanthemum,
                                           rV(),
                                           rP(),
                                           rS(),
                                           rC(),
                                           rC(),
                                           rT(),
                                           3.0],
                                          [
                                           FireworkType.Saturn,
                                           Vec3(0, 0, 100),
                                           Vec3(-120, 0, 0),
                                           rS(),
                                           rC(),
                                           rC(),
                                           rT(),
                                           0.5],
                                          [
                                           FireworkType.Saturn,
                                           Vec3(20, 0, 70),
                                           Vec3(-120, 0, 0),
                                           rS(),
                                           rC(),
                                           rC(),
                                           rT(),
                                           0.5],
                                          [
                                           FireworkType.DiademPeony,
                                           Vec3(-30, 0, 120),
                                           Vec3(120, 0, 0),
                                           rS(),
                                           rC(),
                                           rC(),
                                           rT(),
                                           0.5],
                                          [
                                           FireworkType.DiademPeony,
                                           Vec3(0, 0, 90),
                                           Vec3(120, 0, 0),
                                           rS(),
                                           rC(),
                                           rC(),
                                           rT(),
                                           4.0],
                                          [
                                           FireworkType.DiademPeony,
                                           Vec3(-140, 50, 120),
                                           Vec3(0, 0, 0),
                                           rS(),
                                           rC(),
                                           rC(),
                                           rT(),
                                           0.25],
                                          [
                                           FireworkType.DiademChrysanthemum,
                                           Vec3(70, -40, 90),
                                           Vec3(0, 0, 0),
                                           rS(),
                                           rC(),
                                           rC(),
                                           1.5,
                                           0.25],
                                          [
                                           FireworkType.DiademPeony,
                                           Vec3(-100, 30, 60),
                                           Vec3(0, 0, 0),
                                           rS(),
                                           rC(),
                                           rC(),
                                           2.25,
                                           0.25],
                                          [
                                           FireworkType.DiademChrysanthemum,
                                           Vec3(0, 20, 100),
                                           Vec3(0, 0, 0),
                                           rS(),
                                           rC(),
                                           rC(),
                                           1.5,
                                           2.0],
                                          [
                                           FireworkType.DiademPeony,
                                           Vec3(-70, 0, 130),
                                           Vec3(0, 0, 0),
                                           rS(),
                                           rC(),
                                           rC(),
                                           rT(),
                                           1.5],
                                          [
                                           FireworkType.DiademChrysanthemum,
                                           Vec3(120, 50, 100),
                                           Vec3(0, 0, 0),
                                           rS(),
                                           rC(),
                                           rC(),
                                           1.5,
                                           5.0],
                                          [
                                           FireworkType.Bees,
                                           Vec3(0, 0, 100),
                                           rP(),
                                           1.4,
                                           rC(),
                                           rC(),
                                           2.0,
                                           10.0]]}
    showData[ToontownGlobals.COMBO_FIREWORKS] = showData[ToontownGlobals.NEWYEARS_FIREWORKS]
    sectionData = {ToontownGlobals.JULY4_FIREWORKS: [(0, 24), (24, len(showData[ToontownGlobals.JULY4_FIREWORKS]))], PartyGlobals.FireworkShows.Summer: [
                                         (0, 24), (24, len(showData[PartyGlobals.FireworkShows.Summer]))], 
       ToontownGlobals.NEWYEARS_FIREWORKS: [
                                          (
                                           0, len(showData[PartyGlobals.FireworkShows.Summer]))], 
       ToontownGlobals.COMBO_FIREWORKS: [
                                       (
                                        0, len(showData[PartyGlobals.FireworkShows.Summer]))]}
    showMusic = {}

    @classmethod
    def isValidShowType(cls, showType=-1):
        if showType in cls.showData.keys():
            return True
        else:
            return False

    def __init__(self, showType=ToontownGlobals.NEWYEARS_FIREWORKS):
        NodePath.__init__(self, 'FireworkShow')
        self.showType = showType
        self.sectionIvals = []
        self.fireworks = []
        self.delaySectionStart = None
        self.curSection = None
        self.curOffset = 0.0
        return

    def beginSection(self, startIndex, endIndex, offset):
        taskMgr.remove('beginSection' + str(startIndex) + str(endIndex))
        sectionIval = Parallel()
        time = 2.0
        showMusic = self.showMusic.get(self.showType)
        if showMusic:
            base.musicMgr.load(showMusic, looping=False)
            musicOffset = self.getDuration(0, startIndex) - self.getDuration(startIndex, startIndex) + offset
            sectionIval.append(Func(base.musicMgr.request, showMusic, priority=2, looping=False))
            sectionIval.append(Func(base.musicMgr.offsetMusic, musicOffset))
        sectionData = self.showData.get(self.showType)[startIndex:endIndex]
        for fireworkInfo in sectionData:
            typeId = fireworkInfo[0]
            velocity = fireworkInfo[1]
            pos = fireworkInfo[2]
            scale = fireworkInfo[3]
            color1 = fireworkInfo[4]
            color2 = fireworkInfo[5]
            if color2 == -1:
                color2 = color1
            trailDur = fireworkInfo[6]
            delay = fireworkInfo[7]
            firework = Firework(typeId, velocity, scale, color1, color2, trailDur)
            firework.reparentTo(self)
            firework.setPos(pos)
            self.fireworks.append(firework)
            sectionIval.append(Sequence(Wait(time), firework.generateFireworkIval()))
            time += delay

        self.sectionIvals.append(sectionIval)
        self.curSection = sectionIval
        self.curOffset = offset
        self.delaySectionStart = FrameDelayedCall('delaySectionStart', self.startCurSection, frames=24)

    def startCurSection(self):
        self.curSection.start(self.curOffset)

    def begin(self, timestamp):
        time = 0.0
        for section in self.sectionData.get(self.showType):
            startIndex = section[0]
            endIndex = section[1]
            sectionDur = self.getDuration(startIndex, endIndex)
            if timestamp < sectionDur:
                timestamp = max(0.0, timestamp)
                taskMgr.doMethodLater(time, self.beginSection, 'beginSection' + str(startIndex) + str(endIndex), extraArgs=[startIndex, endIndex, timestamp])
                time = time + sectionDur - timestamp
            timestamp -= sectionDur

    def getDuration(self, startIndex=0, endIndex=None):
        duration = 0.0
        if endIndex == None:
            endIndex = len(self.showData.get(self.showType))
        for firework in self.showData.get(self.showType)[startIndex:endIndex]:
            duration += firework[7]

        return duration

    def getShowDuration(self, eventId=None):
        duration = 0.0
        if eventId:
            for firework in self.showData[eventId]:
                duration += firework[7]

        else:
            for firework in self.showData[self.showType]:
                duration += firework[7]

        return duration

    def isPlaying(self):
        for ival in self.sectionIvals:
            if ival.isPlaying():
                return True

        return False

    def cleanupShow(self):
        if self.delaySectionStart:
            self.delaySectionStart.destroy()
            del self.delaySectionStart
            self.delaySectionStart = None
        showMusic = self.showMusic.get(self.showType)
        if showMusic:
            base.musicMgr.requestFadeOut(showMusic)
        for section in self.sectionData.get(self.showType):
            startIndex = section[0]
            endIndex = section[1]
            taskMgr.remove('beginSection' + str(startIndex) + str(endIndex))

        for ival in self.sectionIvals:
            ival.pause()
            del ival
            ival = None

        self.sectionIvals = []
        for firework in self.fireworks:
            firework.cleanup()
            del firework
            firework = None

        self.fireworks = []
        return