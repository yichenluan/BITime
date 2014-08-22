#!/usr/bin/env python
# -*- coding: utf-8 -*-



from weibo import APIClient

from re import split
import urllib,httplib

APP_KEY = 'key' 
APP_SECRET = 'secret' 
CALLBACK_URL = 'http://jinke.me'
ACCOUNT = 'account'
PASSWORD = 'password'   


client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()

def get_code(url):
    conn = httplib.HTTPSConnection('api.weibo.com')
    postdata = urllib.urlencode({'client_id':APP_KEY,'response_type':'code','redirect_uri':CALLBACK_URL,'action':'submit','userId':ACCOUNT,'passwd':PASSWORD,'isLoginSina':0,'from':'','regCallback':'','state':'','ticket':'','withOfficalFlag':0})
    conn.request('POST','/oauth2/authorize',postdata,{'Referer':url,'Content-Type': 'application/x-www-form-urlencoded'})
    res = conn.getresponse()
    location = res.getheader('location')
    code = location.split('=')[1]
    conn.close()
    return code

def send(content):
	contentDict = content.split('+')
	if len(contentDict) != 3:
		return u'发送失败，请检查格式', 'text'
	else:	
		for i in range(len(contentDict)):
			contentDict[i] = contentDict[i].strip()
		code = get_code(url)
		client = APIClient(app_key = APP_KEY, app_secret = APP_SECRET, redirect_uri = CALLBACK_URL)
		r = client.request_access_token(code)
		access_token = r.access_token
		expires_in = r.expires_in
		client.set_access_token(access_token, expires_in)
		try:
			status = client.statuses.update.post(status = contentDict[1]+':'+contentDict[2])
			return u'发送成功', 'text'
		except:
			return u'抱歉，由于时间间隔原因，微博发送失败，请稍候再试，如有疑问，请联系 @比较困zzz', 'text'
