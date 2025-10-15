                        NAME:M.SAICHARAN                   PDBC HOMEWORK
                        DATE:15-10-2025

1.Write  a  program  to  print  first  'n'  rows  of  emp  table

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
'''
#Program:
import mysql.connector
try:
    con = mysql.connector.connect(host='localhost', database='empdb', user='root')
    cur = con.cursor()
    n = int(input("Enter how many rows? "))
    cur.execute("SELECT * FROM emp")
    rows = cur.fetchmany(n)
    for row in rows:
        print(row)
    print(f'Number of tuples fetched: {cur.rowcount}')
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError:
    print('Start mysql')


2.Write  a  program  to  insert  rows  into  emp  table ,  one  at  a  time

1) How  to  call  execute()  method ?  --->cur . execute(F"insert  into  emp  values  ({empno} ,  '{ename}' , {sal})")

2) Are  quotes  mandatory  for  ename ? --->  Yes  becoz  it  is  a  string

3) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  inputs  empno , ename  and  sal

4) What  action  to  be  made  after  insert ?  --->  Call  commit()  method

5) What  does  commit()  method  do ?  --->  Makes  insertion  becomes  permanent

6) What  happens  when  commit()  is  not  called ?  --->  Insertion  is  only  temporary

7) In  other  words,  insertion  does  not  happen

8) Where  is  commit()  method  defined ?  ---> In  MySqlConnection  class

9) cur . execute(F'insert  into  emp  values (25 , "Rama  Rao" , 10000.0)')
    What  is  the  result  of  cur . rowcount ?  ---> 1  becoz  only  one  row  is  inserted  into  emp  table

10) Can  a  tuple  be  inserted  into  cur  object ?  --->  No  becoz  it  is  immutable

11) What  happens  when  we  try  to  insert  duplicate  empno ?  --->  Raises  mc . errors . IntegrityError
'''

#Program:
import mysql.connector
try:
    con = mysql.connector.connect(host='localhost', database='empdb', user='root')
    cur = con.cursor()
    empno = int(input("Enter empno : "))
    ename = input("Enter ename : ")
    sal = float(input("Enter sal : "))
    cur.execute(f'INSERT INTO emp (empno, ename, sal) VALUES ({empno}, '{ename}', {sal})')
    con.commit()
    print(f'Rows inserted: {cur.rowcount}')
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError:
    print('Start mysql')


3.Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition

1) How  to  call  execute()  method ?  --->   cur . execute(F'delete  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the  cond
'''
#Program:
import mysql.connector
try:
    con = mysql.connector.connect(host='localhost', database='empdb', user='root')
    cur = con.cursor()
    cond = eval(input("Enter condition : "))
    cur.execute(f'DELETE FROM emp WHERE {cond}')
    con.commit()
    print(f'{cur.rowcount} rows deleted')
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError:
    print('Start mysql')


4.Write  a  program to  modify  data  of  emp  table

1) How  to  call  execute()  method ?  --->  cur . execute(F'update  emp  set  {expr}   where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  expr  and  cond
'''
#Program:
import mysql.connector
try:
    con = mysql.connector.connect(host='localhost', database='empdb', user='root')
    cur = con.cursor()
    expr = eval(input("Enter expression : "))
    cond = eval(input("Enter column name = value : "))
    cur.execute(f'UPDATE emp SET {expr} WHERE {cond}')
    con.commit()
    print(f"{cur.rowcount} Rows updated")
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError:
    print('Start mysql')


5.Write  a  program  to  create  student  table

1) How  to  call  execute()  method ?  --->
cur . execute(F'create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float)')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  table  name

3) What  action  to  be  made  when  table  already  exists ?  --->
Delete  the  existing  table  and  create  a  new  table  with  same  name
'''
#Program:
import mysql.connector
try:
    con = mysql.connector.connect(host='localhost', database='empdb', user='root')
    cur = con.cursor()
    tablename = input("Enter table name : ")
    cur.execute(F'CREATE TABLE {tablename} (rollno INT PRIMARY KEY, sname CHAR(20), marks FLOAT)')
    con.commit()
    print(f"Table '{tablename}' created successfully.")
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError:
    print('Start mysql')
