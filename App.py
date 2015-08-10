#!/usr/bin/env python3
#-*- coding:utf-8 -*-
请在Python3下运行此程序='Please run this program with Python3'

import xlrd # Doc : http://www.cnblogs.com/lhj588/archive/2012/01/06/2314181.html

# 介绍
# 	1、导入模块
# 		import xlrd
# 	2、打开Excel文件读取数据
# 		data = xlrd.open_workbook('excelFile.xls')
# 	3、使用技巧
# 		获取一个工作表
# 		table = data.sheets()[0]          #通过索引顺序获取
# 		table = data.sheet_by_index(0) #通过索引顺序获取
# 		table = data.sheet_by_name(u'Sheet1')#通过名称获取

# 		获取整行和整列的值（数组）
# 		table.row_values(i)
# 		table.col_values(i)

# 		获取行数和列数
# 		nrows = table.nrows
# 		ncols = table.ncols
	
# 		循环行列表数据
# 		for i in range(nrows ):
# 			print table.row_values(i)
def str2float(s):
	if s.startswith('.'):
		s = '0' + s
	return float(s)

datalist = []
data = xlrd.open_workbook('f.xls')
table = data.sheets()[0]  # 获取一个工作表
nrows = table.nrows  # 获取行数
for i in range(nrows):
	row_value = table.row_values(i)
	# print(row_value)
	datalist.append(row_value)
datadict = {}
for item in datalist[1:]:
	date = item[0]
	amount = item[5]
	if date in datadict.keys():
		datadict[date] += str2float(amount)
	else:
		datadict[date] = str2float(amount)

for item in  sorted( datadict.items() ):
	print(item)

















