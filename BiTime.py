#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import datetime, time
import cgi
import hashlib
import xml.etree.ElementTree as ET


import weather
import postWeibo
import xiaoche
import translate
import ferryBus


import tornado.web
from tornado.httpclient import AsyncHTTPClient

sorryInfo = u'抱歉，无法处理请求，回复「帮助」可查看使用说明。如有疑问，请您联系 @比较困zzz\n\n我在 http://jinke.me'

class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        signature = self.get_argument("signature", "")
        timestamp = self.get_argument("timestamp", "")
        nonce = self.get_argument("nonce", "")
        echostr = self.get_argument("echostr", "")
        token = "yourtoken"
        L = [timestamp, nonce, token]
        L.sort()
        s = L[0] + L[1] + L[2]
        if hashlib.sha1(s).hexdigest() == signature:
            self.write(echostr)
        else:
            self.render('index.html')

    def getMsg(self):
        body = self.request.body
        data = ET.fromstring(body)
        msg = dict()
        if data.tag == 'xml':
            for child in data:
                msg[child.tag] = child.text
        return msg

    def manageMsg(self, msg):
        msg['Content'] = msg['Content'].strip()
        if msg['Content'][:1] == '#':
            pass
        elif msg['Content'][:2] == u'天气':
            if msg['Content'] == u'天气':
                return weather.getWeatherContent('北京')
            else:
                return weather.getWeatherContent(msg['Content'][2:])
        elif isinstance(msg['Content'], type('string')) or msg['Content'][:2] == u'翻译':
            return translate.getTransInfo(msg['Content'])
        elif msg['Content'] == u'摆渡车':
            return ferryBus.getFerryBus()
        elif msg['Content'] == u'校车' or msg['Content'] == u'明天校车':
            return xiaoche.getTimetable(msg['Content'])
        elif msg['Content'][:2] == '微博':
            return postWeibo.send(msg['Content'])
        elif msg['Content'][:2] == '帮助':
            responseContent = dict()
            responseContent['number'] = 1
            responseContent['items'] = [{'Title':u'北理时间，专注此刻', 'Description':u'感谢您的关注，点击查看使用说明。', 
            'PicUrl':'http://pic.yupoo.com/hanapp/DoQbujO1/custom.jpg', 'Url':'http://mp.weixin.qq.com/s?__biz=MzA4Njk3MzgwMA==&mid=200385632&idx=1&sn=8277bf3c3992e00d238c80af43489fd4#rd'}]
            contentType = 'news'
            return responseContent, contentType
        else:
            return sorryInfo, 'text'


    def responseXML(self, msg, responseContent, contentType):

        textTpl = """ <xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName> 
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[%s]]></MsgType>
                <Content><![CDATA[%s]]></Content>
                <FuncFlag>1</FuncFlag>
                </xml>
                """

        newsTplHead = """
                     <xml>
                     <ToUserName><![CDATA[%s]]></ToUserName>
                     <FromUserName><![CDATA[%s]]></FromUserName>
                     <CreateTime>%s</CreateTime>
                     <MsgType><![CDATA[news]]></MsgType>
                     <ArticleCount>%d</ArticleCount>
                     <Articles>
                        """
        newsTplItem = """
                     <item>
                     <Title><![CDATA[%s]]></Title> 
                     <Description><![CDATA[%s]]></Description>
                     <PicUrl><![CDATA[%s]]></PicUrl>
                     <Url><![CDATA[%s]]></Url>
                     </item>
                     """

        newsTplTail = """
                    </Articles>
                    <FuncFlag>1</FuncFlag>
                    </xml> 
                    """
        if contentType == "text":
            echoXML = textTpl % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), "text", responseContent)
        elif contentType == 'news':
            echoXML = newsTplHead % (msg['FromUserName'], msg['ToUserName'],
                str(int(time.time())), responseContent['number'])
            for item in responseContent['items']:
                echoXML += newsTplItem % (item['Title'], item['Description'],
                    item['PicUrl'], item['Url'])
            echoXML += newsTplTail

        return echoXML


    def response(self, msg):
        if msg['MsgType'] == 'text':
            responseContent, contentType = self.manageMsg(msg)
        elif msg['MsgType'] == 'event' and msg['Event'] == 'subscribe':
            responseContent = dict()
            responseContent['number'] = 1
            responseContent['items'] = [{'Title':u'北理时间，专注此刻', 'Description':u'感谢您的关注，点击查看使用说明。', 
            'PicUrl':'http://pic.yupoo.com/hanapp/DoQbujO1/custom.jpg', 'Url':'http://mp.weixin.qq.com/s?__biz=MzA4Njk3MzgwMA==&mid=200385632&idx=1&sn=8277bf3c3992e00d238c80af43489fd4#rd'}]
            contentType = 'news'
        echoXML = self.responseXML(msg, responseContent, contentType)
        return echoXML



    def post(self):
        msg = self.getMsg()
        echoXML = self.response(msg)
        self.write(echoXML)

class FerryBusHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('ferryBus.html')
        















