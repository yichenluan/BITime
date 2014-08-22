#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime

def getTimeNow():
	datetimeNow = datetime.datetime.now()
	timeNow = datetimeNow.time()
	return timeNow


def checkTimeNow(timeNow):
	if timeNow.hour < 6 or (timeNow.hour == 6 and timeNow.minute <= 30) or timeNow.hour >= 23:
		return 'situationOne'
	elif timeNow.hour == 11 and timeNow.minute <= 40 :
		return 'situationTwo'
	elif timeNow.hour == 17 and timeNow.minute <= 40:
		return 'situationThree'
	elif timeNow.hour == 10 and timeNow.minute >= 20:
		return 'situationFour'
	elif timeNow.hour == 16 and timeNow.minute >= 20:
		return 'situationFive'
	else:
		return 'situationSix'


def handleTime(minuteBegin, hourNow):
	timeList = list()
	if minuteBegin == 0:
		timeList = [
		(hourNow -1, '52', hourNow, '00'), (hourNow, '02', hourNow, '05'),
		(hourNow, '07', hourNow, '15'), (hourNow, '17', hourNow, '20'),
		(hourNow, '22', hourNow, '30'), (hourNow, '32', hourNow, '35')
		]
	elif minuteBegin == 15:
		timeList = [
		(hourNow, '07', hourNow, '15'), (hourNow, '17', hourNow, '20'),
		(hourNow, '22', hourNow, '30'), (hourNow, '32', hourNow, '35'),
		(hourNow, '37', hourNow, '45'), (hourNow, '47', hourNow, '50')
		]
	elif minuteBegin == 30:
		timeList = [
		(hourNow, '22', hourNow, '30'), (hourNow, '32', hourNow, '35'),
		(hourNow, '37', hourNow, '45'), (hourNow, '47', hourNow, '50'),
		(hourNow, '52', hourNow + 1, '00'), (hourNow + 1, '02', hourNow + 1, '05')
		]
	elif minuteBegin == 45:
		timeList = [
		(hourNow, '37', hourNow, '45'), (hourNow, '47', hourNow, '50'),
		(hourNow, '52', hourNow + 1, '00'), (hourNow + 1, '02', hourNow + 1, '05'),
		(hourNow + 1, '07', hourNow + 1, '15'), (hourNow + 1, '17', hourNow  + 1, '20'),
		]
	return timeList



def getFerryBus():
	timeNow = getTimeNow()
	situation = checkTimeNow(timeNow)
	responseContent = dict()
	responseContent['number'] = 5
	responseContent['items'] = list()
	responseContent['items'].append({'Title': '摆渡车时刻：', 
		'PicUrl':'http://drp.io/files/53f0428dc0ac3.png', 'Url': 'http://weixin.jinke.me/ferryBus', 'Description':''})
	responseContent['items'].append({'Description':'', 'PicUrl':'', 'Url': 'http://weixin.jinke.me/ferryBus', 'Title':'地铁站停靠时间' + '\t' + '学校停靠时间'})
	if situation == 'situationOne':
		responseContent['items'].append({'Description':'', 'PicUrl':'', 'Url': 'http://weixin.jinke.me/ferryBus', 'Title':'6:27 - 6:30' + '\t\t\t' + '6:32 - 6:35'})
		responseContent['items'].append({'Description':'', 'PicUrl':'', 'Url': 'http://weixin.jinke.me/ferryBus', 'Title':'6:37 - 6:45' + '\t\t\t' + '6:47 - 6:50'})
		responseContent['items'].append({'Description':'', 'PicUrl':'', 'Url': 'http://weixin.jinke.me/ferryBus', 'Title':'6:52 - 7:00' + '\t\t\t' + '7:02 - 7:05'})
	elif situation == 'situationTwo':
		responseContent['items'].append({'Description':'', 'PicUrl':'', 'Url': 'http://weixin.jinke.me/ferryBus', 'Title':'---------------' + '\t\t' + '11:32 - 11:35'})
		responseContent['items'].append({'Description':'', 'PicUrl':'', 'Url': 'http://weixin.jinke.me/ferryBus', 'Title':'11:37 - 11:45' + '\t\t' + '11:47 - 11:50'})
		responseContent['items'].append({'Description':'', 'PicUrl':'', 'Url': 'http://weixin.jinke.me/ferryBus', 'Title':'11:52 - 12:00' + '\t\t' + '12:02 - 12:05'})
	elif situation == 'situationThree':
		responseContent['items'].append({'Description':'', 'PicUrl':'', 'Url': 'http://weixin.jinke.me/ferryBus', 'Title':'---------------' + '\t\t' + '17:32 - 17:35'})
		responseContent['items'].append({'Description':'', 'PicUrl':'', 'Url': 'http://weixin.jinke.me/ferryBus', 'Title':'17:37 - 17:45' + '\t\t' + '17:47 - 17:50'})
		responseContent['items'].append({'Description':'', 'PicUrl':'', 'Url': 'http://weixin.jinke.me/ferryBus', 'Title':'17:52 - 18:00' + '\t\t' + '18:02 - 18:05'})
	elif situation == 'situationFour':
		responseContent['items'].append({'Description':'', 'PicUrl':'', 'Url': 'http://weixin.jinke.me/ferryBus', 'Title':'10:22 - 10:30' + '\t\t' + '10:32 - 10:35'})
		responseContent['items'].append({'Description':'', 'PicUrl':'', 'Url': 'http://weixin.jinke.me/ferryBus', 'Title':'10:37 - 10:45' + '\t\t' + '10:47 - 10:50'})
		responseContent['items'].append({'Description':'', 'PicUrl':'', 'Url': 'http://weixin.jinke.me/ferryBus', 'Title':'10:52 - 11:00' + '\t\t' + '---------------'})
	elif situation == 'situationFive':
		responseContent['items'].append({'Description':'', 'PicUrl':'', 'Url': 'http://weixin.jinke.me/ferryBus', 'Title':'16:22 - 16:30' + '\t\t' + '16:32 - 16:35'})
		responseContent['items'].append({'Description':'', 'PicUrl':'', 'Url': 'http://weixin.jinke.me/ferryBus', 'Title':'16:37 - 16:45' + '\t\t' + '16:47 - 16:50'})
		responseContent['items'].append({'Description':'', 'PicUrl':'', 'Url': 'http://weixin.jinke.me/ferryBus', 'Title':'16:52 - 17:00' + '\t\t' + '---------------'})
	elif situation == 'situationSix':
		minuteBegin = 15 * ((timeNow.minute + 5) / 15)
		timeList = handleTime(minuteBegin, timeNow.hour)
		responseContent['items'].append({'Description':'', 'PicUrl':'', 'Url': 'http://weixin.jinke.me/ferryBus', 
			'Title':'%s:%s - %s:%s'%timeList[0] + '\t\t' + '%s:%s - %s:%s'%timeList[1]})
		responseContent['items'].append({'Description':'', 'PicUrl':'', 'Url': 'http://weixin.jinke.me/ferryBus', 
			'Title':'%s:%s - %s:%s'%timeList[2] + '\t\t' + '%s:%s - %s:%s'%timeList[3]})
		responseContent['items'].append({'Description':'', 'PicUrl':'', 'Url': 'http://weixin.jinke.me/ferryBus', 
			'Title':'%s:%s - %s:%s'%timeList[4] + '\t\t' + '%s:%s - %s:%s'%timeList[5]})
	return responseContent, 'news'












