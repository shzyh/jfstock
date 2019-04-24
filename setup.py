#encoding:utf8

# from distutils.core import setup
from setuptools import setup, find_packages
from os.path import dirname,join

def read_file(file):
	with open(file,"rt") as f:
		return f.read()

with open(join(dirname(__file__),'jfstock/VERSION.txt'),'rb') as f:
	version = f.read().decode('ascii').strip()

# atr ={
# 	"name":"jfstock",
# 	"version":"1.0",
# 	"description":"a python lib for progress stock data ",
# 	"url":"https://github.com/shzyh/jfstock",
# 	"author_email":"yxwmjf@hotmail.com",
# 	"author":"jf",
# 	"license":"MIT",
# 	"packages":find_packages("jfstock") ,
# 	"package_dir":{'':'jfstock'},
# 	"include_package_data":True,
# 	"data_files":["jfstock/db/conf/conf.cfg"],
# 	"zip_safe":False
# }

setup(
	name = 'jfstock',
	version=version,
	description = 'func for progressing stock data ',
	packages = find_packages(exclude=[]),
	author = 'jf',
	author_email = 'yxwmjf@hotmail.com',
	url = 'https://github.com/shzyh/jfstock',
	license = 'MIT',
	package_data = {'':['*.*']},
	# install_requires = read_file("requirements.txt").strip(),
	zip_safe = False,
	
	)