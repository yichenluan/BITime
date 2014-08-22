#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

weekdaysTable = u'''

中关村 ←→ 良乡（对开）
6:40	8:00	10:10
12:20	12:50	14:30
16:10	18:30	21:40
'''

fridayTable = u'''

周五加开班次

良乡 → 中关村:
18:30 → 19:20

中关村 → 良乡:
17:30 → 18:20
'''

weekendsTable = u'''

良乡 → 中关村:
8:30 → 9:20	
14:30 → 15:20	
21:00 → 21:50

中关村 → 良乡:
7:30 → 8:20
13:30 → 14:20
20:00 → 20:50
'''

holidaysTable = u'''

良乡 → 中关村:
9:00 → 9:50	
16:00 → 16:50

中关村 → 良乡:
8:00 → 8:50	
15:00 → 15:50
'''

holidays = [[[2014, 7, 1], [2014, 9, 5]]]

def getTimetable(content):
	if content == u'校车':
		return timetable(u'今天', 0)
	elif content == u'明天校车':
		return timetable(u'明天', 1)

def timetable(day, offset):
	date = datetime.date.today() + datetime.timedelta(days = offset)
	if check(date, holidays):
		return u'%s是法定节假日，校车时刻如下：' % day + holidaysTable, 'text'
	elif date.weekday() == 5 or date.weekday() == 6:
		return u'%s是周末，校车时刻如下：' % day + weekendsTable, 'text'
	elif date.weekday() == 4:
		return u'%s是周五，校车时刻如下：' % day + weekdaysTable + fridayTable, 'text'
	else:
		return u'%s是%s，校车时刻如下：' % (day, checkWeekday(date)) +weekdaysTable, 'text'

def check(date, days):
	for day in days:
		start = datetime.date(day[0][0], day[0][1], day[0][2])
		end = datetime.date(day[1][0], day[1][1], day[1][2])
		if start <= date <= end:
			return True
	return False

def checkWeekday(date):
	dictWeekday = {
	0 : u'周一', 
	1 : u'周二', 
	2 : u'周三',
	3 : u'周四',
	4 : u'周五'
	}

	return dictWeekday[date.weekday()]

















