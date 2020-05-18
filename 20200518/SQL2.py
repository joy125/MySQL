# -*- coding: utf-8 -*-
"""
Created on Thu May 14 16:50:44 2020

@author: ASUS
"""
import sqlite3
#建立資料庫連接
#路徑因為\為跳脫字元,所以前面要加r或是改成\\
conn=sqlite3.connect(r"C:\Users\ASUS\Desktop\students.db")
#執行SQL指令SELECT
cursor= conn.execute("SELECT cID,cName,cSex,cPhone\
                     FROM students\
                     WHERE (cPhone !='NULL')AND(cSex=F)")
for row in  cursor:
    print(row[0],row[1],row[2],row[3])
conn.close

'''
print('%d %s' % (100,200))
print('{:d}{:s}'.format(100,'200'))
'''



'''
import sqlite3
book= "16,ABC,M,1900-01-01,asd@asd.com,0909090909,addr,155,49"
#.split=用,切割資料
f=book.split(",")
conn=sqlite3.connect(r"C:\Users\ASUS\Desktop\students.db")

sql ="INSERT INTO students (cID,cName,cSex,cBirthday,cEmail,cPhone,cAddr,cHeight,cWeight) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')"
sql=sql.format(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8])
print(sql)
cur=conn.execute(sql)
print(cur.rowcount)
conn.commit()
conn.close()
'''

import sqlite3
book= "4,d,D"
#.split=用,切割資料
f=book.split(",")
conn=sqlite3.connect(r"C:\Users\ASUS\Desktop\students.db")

sql ="INSERT INTO CSVtest (ID,account,password) VALUES ('{0}','{1}','{2}')"
sql=sql.format(f[0],f[1],f[2])
print(sql)
cur=conn.execute(sql)
print(cur.rowcount)
conn.commit()
conn.close()

#---------------------------------------------

import sqlite3
book= "5,f,F"
#.split=用,切割資料
f=book.split(",")
conn=sqlite3.connect(r"C:\Users\ASUS\Desktop\Python_ceart.db")
#建立資料表的SQL語法
sql_CREATE ="CREATE TABLE if NOT EXISTS cID6(\
    ID int NOT NULL UNIQUE,\
    account text NOT NULL,\
    password VARCHAR(20) NOT NULL\
    );"
#插入資料的SQL語法
sql_INSERT ="INSERT INTO cID6 (ID,account,password) VALUES ('{0}','{1}','{2}')"
sql_INSERT=sql_INSERT.format(f[0],f[1],f[2])
cur=conn.execute(sql_CREATE)
cur=conn.execute(sql_INSERT)
conn.commit()
conn.close()


