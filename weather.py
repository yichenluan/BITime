#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import urllib2
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

weatherRequest = u'http://api.map.baidu.com/telematics/v3/weather?location=%s&output=json&ak=yourak'

def getWeatherInfo (city):
	cityRequest = weatherRequest % city
	req = urllib2.Request(cityRequest)
	res = urllib2.urlopen(req)
	jsonResult = res.read()
	res.close()
	dicResult = json.loads(jsonResult)
	weatherInfo = dict()
	if dicResult['status'] != 'success':
		return False
	else:
		weatherInfo['city'] = dicResult['results'][0]['currentCity']
		weatherInfo['pm25'] = dicResult['results'][0]['pm25']
		weatherInfo['weather1'] = dicResult['results'][0]['weather_data'][0]
		weatherInfo['weather2'] = dicResult['results'][0]['weather_data'][1]
		weatherInfo['weather3'] = dicResult['results'][0]['weather_data'][2]
		return weatherInfo

def getWeatherContent (city):
	weatherInfo = getWeatherInfo(city)
	if weatherInfo != False:
		responseContent = dict()
		responseContent['number'] = 4
		responseContent['items'] = list()
		responseContent['items'].append({'Title': city +u'天气预报' + '\n' + weatherInfo['weather1']['date'], 
			'PicUrl':'http://drp.io/files/53f04501cd2ed.png', 'Url': '', 'Description':''})
		responseContent['items'].append({'Description':'', 'PicUrl':weatherInfo['weather1']['dayPictureUrl'], 'Url': '', 'Title':u'今天' + ' ' + weatherInfo['weather1']['weather'] + ' ' + weatherInfo['weather1']['temperature'] + ' ' + weatherInfo['weather1']['wind']})
		responseContent['items'].append({'Description':'', 'PicUrl':weatherInfo['weather2']['dayPictureUrl'], 'Url': '', 'Title':u'明天' + ' ' + weatherInfo['weather2']['weather'] + ' ' + weatherInfo['weather2']['temperature'] + ' ' + weatherInfo['weather2']['wind']})
		responseContent['items'].append({'Description':'', 'PicUrl':weatherInfo['weather3']['dayPictureUrl'], 'Url': '', 'Title':u'后天' + ' ' + weatherInfo['weather3']['weather'] + ' ' + weatherInfo['weather3']['temperature'] + ' ' + weatherInfo['weather3']['wind']})
		return responseContent, 'news'
	else:
		return u'抱歉，该城市名似乎不存在，如有疑问，请您联系 @比较困zzz', 'text'








