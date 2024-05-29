# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.minigame.PhotoGameBase
# Compiled at: 2014-04-30 09:53:54
import PhotoGameGlobals, random

class PhotoGameBase:

    def __init__(self):
        pass

    def load(self):
        self.data = PhotoGameGlobals.AREA_DATA[self.getSafezoneId()]

    def generateAssignmentTemplates(self, numAssignments):
        self.data = PhotoGameGlobals.AREA_DATA[self.getSafezoneId()]
        random.seed(self.doId)
        assignmentTemplates = []
        numPathes = len(self.data['PATHS'])
        if numPathes == 0:
            return assignmentTemplates
        else:
            while len(assignmentTemplates) < numAssignments:
                subjectIndex = random.choice(range(numPathes))
                pose = (None, None)
                while pose[0] == None:
                    animSetIndex = self.data['PATHANIMREL'][subjectIndex]
                    pose = random.choice(self.data['ANIMATIONS'][animSetIndex] + self.data['MOVEMODES'][animSetIndex])

                newTemplate = (subjectIndex, pose[0])
                if newTemplate not in assignmentTemplates:
                    assignmentTemplates.append((subjectIndex, pose[0]))

            self.notify.debug('assignment templates')
            self.notify.debug(str(assignmentTemplates))
            for template in assignmentTemplates:
                self.notify.debug(str(template))

            return assignmentTemplates