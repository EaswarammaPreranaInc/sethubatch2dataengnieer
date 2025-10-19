'''
Write  a  program to  modify  data  of  emp  table

1) How  to  call  execute()  method ?  --->  cur . execute(F'update  emp  set  {expr}   where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  expr  and  cond
'''

import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur=con.cursor()
    cond=input("Enter condition : ")
    val=input("Enter column name=value : ")
    if cond=='':
        cur.execute(f'update emp set {val}')
        con.commit()
    else:
        cur.execute(F'update  emp set {val} where {cond}')
        con.commit()
        print(f'{cur.rowcount} Rows Deleted')
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError: 
    print("Start Mysql")
import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur=con.cursor()
    table=input("Enter table name : ")
    cur.execute(F'create table {table}(id int primary key,name varchar(100),dept varchar(10))')
    print(f'{table} table is created')
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    cur.execute(f'drop table {table}')
    print(f'Existing {table} table is created')
    cur.execute(f'create table {table}(id int primary key,name varchar(100),dept varchar(10))')
    print(f'New {table} table is created')
except mysql.connector.errors.DatabaseError: 
    print("Start Mysql")

