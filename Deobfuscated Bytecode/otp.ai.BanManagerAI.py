# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.ai.BanManagerAI
# Compiled at: 2014-04-30 09:53:54
import urllib, os
from pandac.PandaModules import HTTPClient, Ramfile
from direct.directnotify import DirectNotifyGlobal

class BanManagerAI:
    notify = DirectNotifyGlobal.directNotify.newCategory('BanManagerAI')
    BanUrl = config.GetString('ban-base-url', 'http://vapps.disl.starwave.com:8005/dis-hold/action/event')
    App = config.GetString('ban-app-name', 'TTWorldAI')
    Product = config.GetString('ban-product', 'Toontown')
    EventName = config.GetString('ban-event-name', 'tthackattempt')

    def __init__(self):
        self.curBanRequestNum = 0
        self.channels = {}
        self.ramFiles = {}

    def ban(self, avatarId, dislid, comment):
        parameters = ''
        parameters += 'app=%s' % self.App
        parameters += '&product=%s' % self.Product
        parameters += '&user_id=%s' % dislid
        parameters += '&event_name=%s' % self.EventName
        commentWithAvatarId = 'avId-%s ' % avatarId
        commentWithAvatarId += comment
        parameters += '&comments=%s' % urllib.quote(str(commentWithAvatarId))
        baseUrlToUse = self.BanUrl
        osBaseUrl = os.getenv('BAN_URL')
        if osBaseUrl:
            baseUrlToUse = osBaseUrl
        fullUrl = baseUrlToUse + '?' + parameters
        self.notify.info('ban request %s dislid=%s comment=%s fullUrl=%s' % (self.curBanRequestNum,
         dislid,
         comment,
         fullUrl))
        simbase.air.writeServerEvent('ban-request', avId=avatarId, dislid=dislid, comment=comment, fullUrl=fullUrl)
        if config.GetBool('do-actual-ban', True):
            newTaskName = 'ban-task-%d' % self.curBanRequestNum
            newTask = taskMgr.add(self.doBanUrlTask, newTaskName)
            newTask.banRequestNum = self.curBanRequestNum
            http = HTTPClient.getGlobalPtr()
            channel = http.makeChannel(False)
            self.channels[self.curBanRequestNum] = channel
            rf = Ramfile()
            self.ramFiles[self.curBanRequestNum] = rf
            channel.beginGetDocument(fullUrl)
            channel.downloadToRam(rf)
        self.curBanRequestNum += 1

    def cleanupBanReq(self, banReq):
        channel = self.channels.get(banReq)
        if channel:
            del self.channels[banReq]
        ramfile = self.ramFiles.get(banReq)
        if ramfile:
            del self.ramFiles[banReq]

    def doBanUrlTask(self, task):
        banReq = task.banRequestNum
        channel = self.channels.get(banReq)
        if channel:
            if channel.run():
                return task.cont
        else:
            self.notify.warning('no channel for ban req %s' % banReq)
            self.cleanupBanReq(banReq)
            return task.done
        result = ''
        ramfile = self.ramFiles.get(banReq)
        if ramfile:
            result = ramfile.getData()
        self.notify.info('done processing ban request %s, ramFile=%s' % (banReq, result))
        self.cleanupBanReq(banReq)
        return task.done