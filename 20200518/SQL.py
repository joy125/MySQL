

import sqlite3
book= "3,3"
#.split=用,切割資料
f=book.split(",")
conn=sqlite3.connect\
    (r"C:\Users\ASUS\Desktop\Python_ceart.db")
#建立資料表的SQL語法

sql_CREATE ="CREATE TABLE if NOT EXISTS cID8(\
    ID int AUTO_INCREMENT,\
    account text NOT NULL,\
    password VARCHAR(20) NOT NULL,\
    PRIMARY KEY(ID)\
    );"

#插入資料的SQL語法
sql_INSERT ="INSERT INTO cID8 (account,password)\
    VALUES ('{0}','{1}')"
sql_INSERT=sql_INSERT.format(f[0],f[1])
cur=conn.execute(sql_CREATE)
cur=conn.execute(sql_INSERT)
conn.commit()
conn.close()


