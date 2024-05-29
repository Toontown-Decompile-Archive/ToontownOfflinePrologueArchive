# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.reborn.InterimElectionGlobals
# Compiled at: 2014-04-30 09:53:54
from direct.interval.IntervalGlobal import *
from otp.nametag.NametagConstants import *
from pandac.PandaModules import *
from random import choice
FlippyWheelbarrowPies = [
 [
  1.16, 11.24, 7.0, 246.8, 351.25, 0.0, 1.6, 1.4, 1.8],
 [
  2.27, 8.02, 6.35, 104.04, 311.99, 9.46, 1.35, 1.35, 1],
 [
  -1.23, 7.33, 6.88, 276.34, 28.61, 350.54, 1.41, 1.41, 1.6],
 [
  0.27, 8.24, 6.42, 198.15, 351.87, 355.24, 1.93, 2, 2],
 [
  0.06, 5.23, 6.78, 63.43, 355.91, 15.26, 1.3, 1.6, 1.8],
 [
  -0.81, 11.37, 6.82, 326.31, 5.19, 19.98, 1.76, 1.86, 1.5],
 [
  1.35, 10.09, 5.92, 35.54, 353.66, 343.3, 1.5, 1.9, 1.8],
 [
  1.9, 5.59, 6.5, 75.96, 326.31, 8, 1.76, 1.56, 1.5],
 [
  -1.74, 5.42, 6.28, 327.53, 318.81, 4.76, 1.8, 2, 2],
 [
  -1.55, 9.22, 5.72, 266.53, 341.57, 0.0, 2.09, 1.68, 1.81]]
IntroMusic = 'phase_4/audio/bgm/EE_Intro.ogg'
CountersMusic = 'phase_4/audio/bgm/IE_CountersStop.ogg'
FakeCreditsMusic = 'phase_4/audio/bgm/IE_MangledVictory.ogg'
SadMusic = 'phase_4/audio/bgm/IE_JustDies.ogg'
CreditsMusic = 'phase_4/audio/bgm/EE_Theme.ogg'
SurleeTips = [
 "Mover and Shakers cause Tremors as they walk -- You'll need to hit them from a distance.", 
 "Don't give up this fight easy, Toons.  I'm not sure what can happen if you go sad..", 
 "That's what I'm talkin' about. Keep at it!", 
 'Keep a close eye on your pie count, it can run out fast.', 
 'Hackerbots are your worst nightmare! They have double the HP of normal Cogs.', 
 'Version 2.0 Cogs are nasty! You need to defeat them twice.', 
 'Holocogs can be hard to see. Keep yer eyes open!', 
 "Legal Eagles have an eye of evil. Don't let them buggers glare at you!", 
 'Spin Doctors can cause mighty Quakes. Jump when they do to dodge!']
BalloonBasePosition = [
 -15, 33, 1.1]
BalloonElectionPosition = [166.5, 64.0, 53.0]
BalloonScale = 2.5
FlippyGibPies = [
 "Let 'em fly!", 
 "Wow, I've never seen someone carry so many pies.", 
 'Come back any time.', 
 'Ready for WAR?', 
 'Let the pies fly!', 
 'Clobber the competition! Try not to hit him too hard, though.', 
 'Are you really going to eat that many pies, __NAME__?', 
 'Oof, I better start baking more pies!']
FlippyGibPiesChoice = choice(FlippyGibPies)
FlippyDelayResponse = 1.0
FlippyPhraseIds = [
 [
  100, 101, 102, 103, 104, 105],
 [
  107, 108],
 [
  200, 201, 202, 206, 207],
 [
  203, 204, 205],
 [
  208, 209],
 [
  301],
 [
  500, 21002],
 [
  505, 506, 507, 5602],
 [
  508, 511, 1001, 1003, 1005, 1006, 1126, 1127, 5603, 
  1106, 1107, 
  1108, 1109, 1110, 1124, 1125, 1126, 
  1127, 1128, 10115, 1112, 
  1114, 1554, 1555, 1556, 
  1557, 1559, 812],
 [
  509],
 [
  510],
 [
  600, 601, 602, 603],
 [
  700, 701, 702, 704, 705, 706, 707],
 [
  703],
 [
  800, 801, 802, 803, 804],
 [
  807],
 [
  808],
 [
  901],
 [
  900, 902, 903, 904, 905],
 [
  1200],
 [
  1500],
 [
  1501],
 [
  1508],
 [
  1415],
 [
  1520, 1527],
 [
  1526],
 [
  1558],
 [
  5400],
 [
  5401, 5407, 5408, 5409],
 [
  5402],
 [
  5404],
 [
  5405],
 [
  5500],
 [
  5501],
 [
  5502],
 [
  5503],
 [
  5504],
 [
  5505],
 [
  5506],
 [
  5507],
 [
  5600, 5601],
 [
  10100],
 [
  10101, 10102],
 [
  10110, 10111],
 [
  10105],
 [
  10112],
 [
  10113],
 [
  10114],
 [
  5700],
 [
  1130, 1131, 1132, 1133, 1136],
 [
  5406],
 [
  5411],
 [
  1600],
 [
  1104, 1105]]
FlippyPhrases = [
 'Hey there, __NAME__! How are you doing?', 
 "I'm here, present and accounted for!", 
 'Alrighty, catcha later!', 
 'Thanks! To you as well.', 
 'Leaving so soon?', 
 "Ha, that's a funny phrase. Owooo!", 
 'No problem.', 
 'You betcha!', 
 'I would if I could, but I should stay here in case new toons come along.', 
 'Thanks for the offer, but I think I have things under control.', 
 "Sorry, I'm not allowed to make friends over the election period. :(", 
 "Right back 'atcha!", 
 'Aw, shucks. I like yours too!', 
 'Not sure if I should consider that a compliement or...', 
 "No problem. It's all good.", 
 'Huh. I forget.', 
 'Good, because I can only respond to SpeedChat. Haha!', 
 "It's probably the leftover ingredients from all of those pies. Pee-yew!", 
 "I'm sorry. Did I do something wrong? :(", 
 "I haven't gotten any in a while. I guess you could say that the election is my ToonTask!", 
 'All the cream pies we need!', 
 'Oh? No problem, just grab some from the wheelbarrow.', 
 'Totally! Throw is my favorite kind of gag.', 
 "Uh oh, that's no good. You should find an ice cream cone around here.", 
 "I'm wide open, pass it here!", 
 'Sorry, only pies here.', 
 'Hmm, good idea. Pies are going so fast that we might have to switch to cupcakes by the time of the election.', 
 "Toontown... Offline? I've heard Toons say that a few times, but I can never figure out what they mean.", 
 'Hmm, well I did spot a butterfly over there.', 
 'Oof, plenty of times at first. Karts are tricky to get used to.', 
 "I do, actually! I don't use it often.", 
 "Hiya, viewers! Don't forget to Flip for Flippy!", 
 ':D', 
 ':C', 
 ':)', 
 ':(', 
 ':P', 
 ':O', 
 '>:C', 
 '>:)', 
 "I'm doing pretty great! And you?", 
 "I'm not allowed to vote, silly!", 
 "That's the spirit!", 
 'Lil Oldman has strong spirit... but is he any match for me?', 
 'Me too. Alec did a great job, and I hear there are more coming.', 
 'Toontastic!', 
 "Ooo, I heard he's dreamy!", 
 'How generous of him!', 
 'Ooooh, I just love that word! Good to see it catching on.', 
 "Don't worry, I have time.", 
 'At least you have me to keep you company.', 
 "I probably should. There's way too many butterflies here!", 
 'Please, take as many as you want!', 
 "We're already in Toontown Central!"]
oldmanTipsIntro = "Lil' Oldman: We sure can! Just to make sure, I will share some advice with you..."
toonTips = ["It's not the best to use sound on lured Cogs.. just so ya know!", 
 "Double lurin' will show Cogs they're being tricked!", 
 "Best yer 'stun' a Cog first before you drop it- you'll almost never miss.", 
 "Two traps don't make one; they make none!", 
 'Try to pick a gag each and every turn, or just call yer Doodle!', 
 "Spread out the use of Toon-up, it's best to take out those darn Cogs first!", 
 'Make sure you have the toughest gags in Town before confronting a Cog Boss!', 
 'Knockback is a charm! Use the same gag type together to produce bonus damage.', 
 'Training your gags in large Cog buildings is the best for mass multipliers!']