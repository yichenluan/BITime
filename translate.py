#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib2

translateRequest = u'http://openapi.baidu.com/public/2.0/translate/dict/simple?client_id=yourid&q=%s&from=%s&to=%s'

def getrequestURL(content):
	contentList = content.split('+')
	for i in range(len(contentList)):
		contentList[i] = contentList[i].strip()
	contentForTranslate = contentList[-1]
	if isinstance(contentForTranslate, type('string')):
		requestURL = translateRequest % (contentForTranslate, 'en', 'zh')
	else:
		requestURL = translateRequest % (contentForTranslate, 'zh', 'en')
	return requestURL

def getTransInfo(content):
	requestURL = getrequestURL(content)
	req = urllib2.Request(requestURL)
	res = urllib2.urlopen(req)
	jsonResult = res.read()
	res.close()
	dicResult = json.loads(jsonResult)
	if dicResult['errno'] != 0:
		return u'错误', 'text'
	else:
		try:
			translateInfo = dict()
			translateInfo['wordName'] = dicResult['data']['word_name']
			translateInfo['wordPart'] = dicResult['data']['symbols'][0]['parts']
			translateStr = translateInfo['wordName'] + ' :'
			if dicResult['from'] == 'en':
				for parts in translateInfo['wordPart']:
					translateStr += '\n\n' + parts[u'part']
					for mean in parts['means']:
						translateStr += mean + ' '
			else:
				for parts in translateInfo['wordPart']:
					if parts['part']:
						translateStr += '\n\n' + parts['part'] + ':'
					else:
						translateStr += '\n\n'
					for mean in parts['means']:
						translateStr += mean + '. '
			return translateStr, 'text'
		except:
			return u'抱歉，该单词似乎不存在。如有疑问，请您联系 @比较困zzz', 'text'




	














