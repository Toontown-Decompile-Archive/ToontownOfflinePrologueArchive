# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.election.ElectionGlobals
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
AnnouncementMusic = 'phase_4/audio/bgm/EE_Announcement.ogg'
VictoryMusic = 'phase_4/audio/bgm/EE_Celebration.ogg'
SadMusic = 'phase_4/audio/bgm/EE_DiesandPies.ogg'
CreditsMusic = 'phase_4/audio/bgm/EE_Theme.ogg'
SurleeTips = [
 'Always watch all sides of you, the Cogs are sneaky and love to backstab.', 
 "Make sure to not only pie the cogs, but your fellow toons as well! There's lots of Laff to go around.", 
 "Mover and Shakers give tremors as they walk -- You'll need to hit them from a distance.", 
 'Come on, get more pies! Fight for the town!', 
 'The bigger a Cog is, the faster they walk and the more they talk.', 
 "Don't let them take away our fun! Stop them!", 
 "The Cog's business is too boring to bear. Don't let them talk to you.", 
 "That's what I'm talking about. Keep at it!", 
 "Flippy, we need more pies over here. They're flying out quick.", 
 "Doctor Dimm, have you had any luck on Slappy's stand?", 
 'Keep a close eye on your pie count, it can run out fast.']
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
  1127, 1128],
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
  1112, 1114, 1554, 1555, 1556, 1557, 1559, 812],
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
  10103, 10104],
 [
  10105],
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
  1605],
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
 '...like, the gear? What have gears ever done to you? :(', 
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
 'Slappy is pretty fun, too. Great balloon. Though... See that plane stuck up there...?', 
 'Me too. Alec did a great job, and I hear there are more coming.', 
 'Ooooh, I just love that word! Good to see it catching on.', 
 "Don't worry, I have time.", 
 'At least you have me to keep you company.', 
 "I probably should. There's way too many butterflies here!", 
 'Please, take as many as you want!', 
 'I think Slappy has some over at his stand.', 
 "We're already in Toontown Central!"]
SlappySpeech1 = [
 'Hiya! Up for a ride?', 
 'Off we goooo!', 
 "In case you didn't get it back there, that was a pun.", 
 '"Up" for a ride. Get it?', 
 'Haha! I quack myself up.', 
 'That was another pun!', 
 "Do you know any good puns? I'm full of them.", 
 "That wasn't a pun, though. I should have had one there. It was fitting.", 
 "Oh man, we're almost back already?", 
 'Well, at least we had a WHALE of a time!', 
 "Err- no. Wrong pun. That one didn't make sense.", 
 "I'll CATCHA later! Get it, because of the whale pun? It makes sense now. I planned that."]
SlappySpeech2 = [
 'Hello! Want a ride, I assume?', 
 "Good! It would be kind of weird if you didn't.", 
 "I take it you're a balloon fanatic like myself, eh?", 
 "No? Oh. I don't see how you can't be.", 
 "Just look at this thing. It's a 500 pound bag floating in the sky!", 
 "If that isn't amazing, I don't know what is.", 
 "Small balloons, too. You know, I've always wanted to be a balloon salesman.", 
 "I'd get my own little cart and everything!", 
 'They soar through the skies, going beyond what we know.', 
 "Maybe even into another world. Who knows what they'd see on the outskirts of Toontown?", 
 "I've always wondered what kind of mysteries lie out there. The balloons know.", 
 "D'awh, here already. I was just about to get into the history of balloons. Come back any time!"]
SlappySpeech3 = [
 'Hey there! Yep, just hop on in!', 
 "You know, some may consider it rude to jump into someone else's balloon without permission.", 
 "In fact, I'm going to have to ask you to step out now.", 
 "Yeah, just right off the side there. It's not too high up yet.", 
 "I'm joking! I'm joking. Don't jump out, the ride is free.", 
 'Can you see your house from up here?', 
 "I can't. This cardboard hill is in the way.", 
 "I've always wondered why they put those up. Why not enjoy the scenery?", 
 'Not to mention the Jellybeans they could have saved by not buying paint.', 
 'It seems counterproductive to me. Those are definitely getting torn down.', 
 'That is, if I get elected. Hey, are you voting for me?', 
 "Nonono, don't tell me. I want to be surprised. Remember this free balloon ride at the polls, though!"]
SlappySpeech5 = [
 'Oooh, look who it is!', 
 'I was wondering when you would come by for a ride.', 
 'How are things going? Having fun with this election excitement?', 
 "I know I certainly am. I've been on hundreds of these balloon rides, and they never get old.", 
 'You get used to the air sickness after a while.', 
 'Woah, look over there! You can see some of the grey!', 
 'The grey is just one of those many things in Toontown that bewilders me.', 
 'An undrawn area, just waiting for color. Can you imagine the creativity?', 
 "It's an unexplored blank canvas of imagination.", 
 "You know what? You and I -- after this election, we're going to go out there.", 
 'You and I will figure out the secrets of the grey, unleash the creativity it holds. I promise you on that.', 
 "We'll find out what it is, for not only Toontown but for the whole Tooniverse. Make sure you hold me to it! "]
SlappySpeechChoices = [
 SlappySpeech1, SlappySpeech2, SlappySpeech3, SlappySpeech5]
SlappySpeeches = choice(SlappySpeechChoices)
NumBalloonPaths = 1

def generateFlightPaths(balloon):
    flightPaths = []
    flightPaths.append(Sequence(Wait(0.5), balloon.balloon.posHprInterval(1.5, Point3(-19, 35, 3), (0,
                                                                                                    2,
                                                                                                    2)), balloon.balloon.posHprInterval(1.5, Point3(-23, 38, 5), (0,
                                                                                                                                                                  -2,
                                                                                                                                                                  -2)), balloon.balloon.posHprInterval(8.0, Point3(-53, 75, 24), (0,
                                                                                                                                                                                                                                  0,
                                                                                                                                                                                                                                  0)), balloon.balloon.posHprInterval(0.5, Point3(-54, 76, 25), (5,
                                                                                                                                                                                                                                                                                                 2,
                                                                                                                                                                                                                                                                                                 2)), balloon.balloon.posHprInterval(11.0, Point3(-105, 33, 54), (180,
                                                                                                                                                                                                                                                                                                                                                                  -2,
                                                                                                                                                                                                                                                                                                                                                                  -2)), balloon.balloon.posHprInterval(0.5, Point3(-106, 34, 55), (175,
                                                                                                                                                                                                                                                                                                                                                                                                                                   -4,
                                                                                                                                                                                                                                                                                                                                                                                                                                   0)), balloon.balloon.posHprInterval(10.0, Point3(-100, -60, 54), (0,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     2,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     -2)), balloon.balloon.posHprInterval(0.5, Point3(-97.5, -59.5, 54), (-2,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          -2,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          2)), balloon.balloon.posHprInterval(18.0, Point3(60, -10, 54), (-70,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          0,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          0)), balloon.balloon.posHprInterval(0.5, Point3(62, -11, 54), (-65,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         -2,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         2)), balloon.balloon.posHprInterval(15.0, Point3(-15, 33, 1.1), (0,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          0,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          0))))
    return flightPaths


def generateToonFlightPaths(balloon):
    toonFlightPaths = []
    toonFlightPaths.append(Sequence(Wait(0.5), base.localAvatar.posInterval(1.5, Point3(-19, 35, 3)), base.localAvatar.posInterval(1.5, Point3(-23, 38, 5)), base.localAvatar.posInterval(8.0, Point3(-53, 75, 24)), base.localAvatar.posInterval(0.5, Point3(-54, 76, 25)), base.localAvatar.posInterval(11.0, Point3(-105, 33, 54)), base.localAvatar.posInterval(0.5, Point3(-106, 34, 55)), base.localAvatar.posInterval(10.0, Point3(-100, -60, 54)), base.localAvatar.posInterval(0.5, Point3(-99, -59, 53)), base.localAvatar.posInterval(18.0, Point3(60, -10, 54)), base.localAvatar.posInterval(0.5, Point3(62, -11, 54)), base.localAvatar.posInterval(15.0, Point3(-15, 33, 1.1))))
    return toonFlightPaths


def generateSpeechSequence(balloon):
    speechSequence = Sequence(Func(balloon.slappy.setChatAbsolute, SlappySpeeches[0], CFSpeech | CFTimeout), Wait(4), Func(balloon.slappy.setChatAbsolute, SlappySpeeches[1], CFSpeech | CFTimeout), Wait(6), Func(balloon.slappy.setChatAbsolute, SlappySpeeches[2], CFSpeech | CFTimeout), Wait(4), Func(balloon.slappy.setChatAbsolute, SlappySpeeches[3], CFSpeech | CFTimeout), Wait(6), Func(balloon.slappy.setChatAbsolute, SlappySpeeches[4], CFSpeech | CFTimeout), Wait(10), Func(balloon.slappy.setChatAbsolute, SlappySpeeches[5], CFSpeech | CFTimeout), Wait(6), Func(balloon.slappy.setChatAbsolute, SlappySpeeches[6], CFSpeech | CFTimeout), Wait(10), Func(balloon.slappy.setChatAbsolute, SlappySpeeches[7], CFSpeech | CFTimeout), Wait(6), Func(balloon.slappy.setChatAbsolute, SlappySpeeches[8], CFSpeech | CFTimeout), Wait(7), Func(balloon.slappy.setChatAbsolute, SlappySpeeches[9], CFSpeech | CFTimeout), Wait(5), Func(balloon.slappy.setChatAbsolute, SlappySpeeches[10], CFSpeech | CFTimeout), Wait(6), Func(balloon.slappy.setChatAbsolute, SlappySpeeches[11], CFSpeech | CFTimeout))
    return speechSequence