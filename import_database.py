#!/usr/bin/env python
import sqlite3
fname="data.txt"
s=open(fname).readline().split('"')
delete_list=['data','{',':[{',':','}]','recordId','3388','}','},{','}],']
for element in delete_list:
	s=[x for x in s if x!=element]
for i in range(len(s)):
	if i%2==1:
		s[i]=s[i].lstrip(':')
		s[i]=s[i].rstrip(',')
dataset={}
subdataset={}

for i in range(len(s)+1):
	if i!=0 and i%28==0:
		dataset[i/28-1]=subdataset
		subdataset={}
	if i%2==0 and i!=len(s):
		subdataset[s[i]]=s[i+1]

"""
database name: sports
table1: rid_table  R(recordId,table_name)
table2: data1 R(altOffset,altitude,deviceX,deviceY,
	deviceZ,heartRate,isIntegerKM,latitude,longitude,
	planeOffset,pointDist,speed,sportMode,timeStamp)
14 attributes in table data1
"""

dbname="db.sqlite3"
conn=sqlite3.connect(dbname)
c=conn.cursor()


#insert all the dataset into the tables
rid=3388
table_name_now="data1"
c.execute("insert into show_rid_table(recordId,table_name) values(?,?)",(rid,table_name_now))
for i in range(len(dataset)):
	c.execute("insert into show_data1(altOffset,altitude,deviceX,deviceY,deviceZ,heartRate,isIntegerKM,latitude,longitude,planeOffset,pointDist,speed,sportMode,timeStamp) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(dataset[i]['altOffset'],dataset[i]['altitude'],dataset[i]['deviceX'],dataset[i]['deviceY'],
	dataset[i]['deviceZ'],dataset[i]['heartRate'],dataset[i]['isIntegerKM'],dataset[i]['latitude'],
	dataset[i]['longitude'],dataset[i]['planeOffset'],dataset[i]['pointDist'],dataset[i]['speed'],dataset[i]['sportMode'],dataset[i]['timeStamp']))
conn.commit()
conn.close()


