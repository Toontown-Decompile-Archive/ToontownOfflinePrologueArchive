# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.uberdog.ScavengerHuntDataStore
# Compiled at: 2014-04-30 09:53:54
from direct.directnotify import DirectNotifyGlobal
from toontown.uberdog.DataStore import *

class ScavengerHuntDataStore(DataStore):
    QueryTypes = DataStore.addQueryTypes(['GetGoals', 'AddGoal'])
    notify = DirectNotifyGlobal.directNotify.newCategory('ScavengerHuntDataStore')

    def __init__(self, filepath):
        DataStore.__init__(self, filepath)

    def handleQuery(self, query):
        qId, qData = query
        if qId == self.QueryTypes['GetGoals']:
            avId, goal = qData
            goals = self.__getGoalsForAvatarId(avId)
            return (
             qId, (avId, goal, goals))
        else:
            if qId == self.QueryTypes['AddGoal']:
                avId, goal = qData
                self.__addGoalToAvatarId(avId, goal)
                return (
                 qId, (avId,))
            return

    def __addGoalToAvatarId(self, avId, goal):
        if self.wantAnyDbm:
            pAvId = cPickle.dumps(avId)
            pGoal = cPickle.dumps(goal)
            pData = self.data.get(pAvId, None)
            if pData is not None:
                data = cPickle.loads(pData)
            else:
                data = set()
            data.add(goal)
            pData = cPickle.dumps(data)
            self.data[pAvId] = pData
        else:
            self.data.setdefault(avId, set())
            self.data[avId].add(goal)
        self.incrementWriteCount()
        return

    def __getGoalsForAvatarId(self, avId):
        if self.wantAnyDbm:
            pAvId = cPickle.dumps(avId)
            pData = self.data.get(pAvId, None)
            if pData is not None:
                data = list(cPickle.loads(pData))
            else:
                data = []
            return data
        return list(self.data.get(avId, []))
        return