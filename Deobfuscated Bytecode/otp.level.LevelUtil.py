# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.level.LevelUtil
# Compiled at: 2014-04-30 09:53:54
import string, LevelConstants

def getZoneNum2Node(levelModel, logFunc=lambda str: str):

    def findNumberedNodes(baseString, model, caseInsens=1):
        srch = '**/%s*' % baseString
        if caseInsens:
            srch += ';+i'
        potentialNodes = model.findAllMatches(srch)
        num2node = {}
        for potentialNode in potentialNodes:
            name = potentialNode.getName()
            logFunc('potential match for %s: %s' % (baseString, name))
            name = name[len(baseString):]
            numDigits = 0
            while numDigits < len(name):
                if name[numDigits] not in string.digits:
                    break
                numDigits += 1

            if numDigits == 0:
                continue
            num = int(name[:numDigits])
            if num == LevelConstants.UberZoneEntId:
                logFunc('warning: cannot use UberZone zoneNum (%s). ignoring %s' % (LevelConstants.UberZoneEntId, potentialNode))
                continue
            if num < LevelConstants.MinZoneNum or num > LevelConstants.MaxZoneNum:
                logFunc('warning: zone %s is out of range. ignoring %s' % (num, potentialNode))
                continue
            if num in num2node:
                logFunc('warning: zone %s already assigned to %s. ignoring %s' % (num, num2node[num], potentialNode))
                continue
            num2node[num] = potentialNode

        return num2node

    zoneNum2node = findNumberedNodes('zone', levelModel)
    zoneNum2node[LevelConstants.UberZoneEntId] = levelModel
    return zoneNum2node