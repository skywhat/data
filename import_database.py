#!/usr/bin/env python
import sqlite3
fname="data.txt"
s=open(fname).readline().split('"')
delete_list=['data','{',':[{',':','}]','recordId','3388','}','},{','}],','}\n']
for element in delete_list:
	s=[x for x in s if x!=element]
for i in range(len(s)):
	if i%2==1:
		s[i]=s[i].lstrip(':')
		s[i]=s[i].rstrip(',')
dataset={}
subdataset={}

for i in range(0,len(s)+1,2):
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

#insert all the datasets into the tables
rid=3388

c.execute("insert into show_mode(recordId,sportMode,heartRate,altOffset,planeOffset) values(?,?,?,?,?)",(rid,dataset[0]['sportMode'],dataset[0]['heartRate'],dataset[0]['altOffset'],dataset[0]['planeOffset']))

for i in range(len(dataset)):
	c.execute("insert into show_data(altitude,deviceX,deviceY,deviceZ,isIntegerKM,latitude,longitude,pointDist,speed,timeStamp,Mode_id) values(?,?,?,?,?,?,?,?,?,?,?)",(dataset[i]['altitude'],dataset[i]['deviceX'],dataset[i]['deviceY'],dataset[i]['deviceZ'],dataset[i]['isIntegerKM'],dataset[i]['latitude'],dataset[i]['longitude'],dataset[i]['pointDist'],dataset[i]['speed'],dataset[i]['timeStamp'],rid))

conn.commit()
conn.close()


