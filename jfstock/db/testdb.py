# -*- coding: utf-8 -*-
# @Author: jiangfeng
# @Date:   2018-11-22 16:48:39
# @Last Modified by:   jiangfeng
# @Last Modified time: 2019-04-23 11:31:19

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


import database

db = database.database()
sql = "select * from t_stock_trade where F_STOCK_CODE=%s limit 100"
print db.fetch_all(sql,"000001")