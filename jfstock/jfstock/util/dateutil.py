# -*- coding: utf-8 -*-
# @Author: jiangfeng
# @Date:   2019-01-22 21:31:24
# @Last Modified by:   jiangfeng
# @Last Modified time: 2019-04-24 10:16:28

import pandas as pd 
import numpy as np 
from datetime import datetime

def _quar(mon):
	if mon in [1,2,3]:
		return '1'
	elif mon in [4,5,6]:
		return '2'
	elif mon in [7,8,9]:
		return '3'
	elif mon in [10,11,12]:
		return '4'
	else:
		return None

def year_quar(date):
	mon = int(date[5:7])
	return [date[:4],_quar(mon)]

def today():
	day = datetime.today().date()
	return str(day)

def get_year():
	return datetime.today().year
	
def get_month():
	return datetime.today().month 

def get_hour():
	return datetime.today().hour 

def today_last_year():
	last_y = datetime.today().date()+datetime.timedelta(-365)
	return str(last_y)

