# -*- coding: utf-8 -*-
# @Author: jiangfeng
# @Date:   2018-11-22 16:48:39
# @Last Modified by:   jiangfeng
# @Last Modified time: 2019-04-23 17:23:44

# import pymysql
# import pandas as pd

# dbconf = {
# 	"host":"rm-uf6qagldug54g2k312o.mysql.rds.aliyuncs.com",
# 	"db":"database_tx",
# 	"user":"jf",
# 	"password":"jiangfeng=0",
# 	"charset":"utf8",
# 	"cursorclass": pymysql.cursors.DictCursor,

# }

# conn = pymysql.connect(**dbconf)
# sql = "select * from i_date"
# df = pd.read_sql(sql,con=conn)
# print df


#*****************测试默认数据库连接********************************

# from db import database

# db = database.database()
# sql = "select * from t_stock_trade where F_STOCK_CODE=%s limit 100"
# print db.fetch_all(sql,"000001")

#*****************测试数据调取************************************
# from api import DataAPI

# dp = DataAPI.DataAPI()
# print dp.get_mkt_equd("000001")
# print dp.get_mkt_equd("000001",begin_date='20180101',end_date='20181228')
# print dp.get_mkt_equd("000001",begin_date='20180101',end_date='20181228',field=["F_STOCK_STDCODE","F_CLOSE"])
# df = dp.get_mkt_equd("000001",adj='hfq')

#******************测试指标计算**********************************

# from util import indictor
# from api import DataAPI

# dp = DataAPI.DataAPI()
# df = dp.get_mkt_equd('000001',field=["F_STOCK_STDCODE","F_CLOSE"])
# rsi1,rsi2,rsi3 = indictor.RSI(df["F_CLOSE"])
# print rsi1