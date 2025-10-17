'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''

import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur=con.cursor()
    cur.execute(F'select * from emp')
    for x in cur.description:
        print(f'{x[0]:^10}',end='\t')
    print()
    while x:=cur.fetchone():
        for a in x:
            print(f'{a:^10}',end='\t')
        print()
    print("Number of tuples : ",cur.rowcount)
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError: 
    print("Start Mysql")

'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''
import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur=con.cursor()
    cond=input("Enter any condition : ")
    if cond=='':
        cur.execute(f'select * from emp')
    else:
        cur.execute(F'select * from emp where {cond}')
    for x in cur.description:
        print(f'{x[0]:^10}',end='\t')
    print()
    while x:=cur.fetchone():
        for a in x:
            print(f'{a:^10}',end='\t')
        print()
    print("Number of tuples : ",cur.rowcount)
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError: 
    print("Start Mysql")

'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''


import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur=con.cursor()
    column=input("Enter column name : ")
    if column=='':
        cur.execute(f'select * from emp')
    else:
        cur.execute(F'select * from emp order by {column}')
    for x in cur.description:
        print(f'{x[0]:^10}',end='\t')
    print()
    while x:=cur.fetchone():
        for a in x:
            print(f'{a:^10}',end='\t')
        print()
    print("Number of tuples : ",cur.rowcount)
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError: 
    print("Start Mysql")

'''
Write  a  program  to  print  user  input  table  with  next()  function

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  {table}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the   table  name

3) What  does  next(cur)  do ?  --->  Yields  the  next  tuple  of  cursor  object

4) What  does   next()  function  do  when  end  of   the  cursor  is  reached ?  ---> Throws StopIteration  error

5) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                          execute()                                   next()             print()
'''


import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur=con.cursor()
    table=input("Enter table name : ")
    cur.execute(F'select * from {table}')
    for x in cur.description:
        print(f'{x[0]:^10}',end='\t')
    print()
    while True:
        try:
            tpl=next(cur)
            for x in tpl:
                print(f'{x:^10}',end='\t')
            print()
        except StopIteration:
            break
    print()
    print("Number of tuples : ",cur.rowcount)
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError: 
    print("Start Mysql")

'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''


import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur=con.cursor()
    cur.execute(F'select * from emp')
    for x in cur.description:
        print(f'{x[0]:^10}',end='\t')
    print()
    list=cur.fetchall()
    for x in list:
        for a in x:
            print(f'{a:^10}',end='\t')
        print()
    print("Number of tuples : ",cur.rowcount)
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError: 
    print("Start Mysql")

'''
Write  a  program  to  print  first  'n'  rows  of  emp  table

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
            execute()                           fetchmany(n)               for  loop                print()
'''

import mysql.connector as mc
try:
    con=mc.connect(database='empdb',user='root')
    cur=con.cursor()
    cur.execute(f'select * from emp')
    n=int(input("How many rows ? : "))
    list=cur.fetchmany(n)
    for x in cur.description:
        print(f'{x[0]:^10}',end='\t')
    print()
    for x in list:
        for a in x:
            print(f'{a:^10}',end='\t')
        print()
    print("Number of tuples fetched : ",cur.rowcount)
    cur.close()
    con.close()
except mc.errors.InternalError:
    print('cursor cannot be closed')
except mc.errors.ProgrammingError as msg:
    print(msg)
except mc.errors.DatabaseError:
    print('Start Mysql')
except AttributeError:
    print('Input cannot be negative')
    
'''
Write  a  program  to  insert  rows  into  emp  table ,  one  at  a  time

1) How  to  call  execute()  method ?  --->
															cur . execute(F"insert  into  emp  values  ({empno} ,  '{ename}' , {sal})")

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
import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur=con.cursor()
    while True:
        id=int(input("Enter Employee Id : "))
        name=input("Enter Employee Name : ")
        sal=float(input("Enter Employee Salary : "))
        try:
            cur.execute(f"insert into emp values({id},'{name}',{sal})")
            con.commit()
            print(f'{cur.rowcount} row is inserted')
        except mysql.connector.errors.IntegrityError:
            print('Duplicate Employee Id and Hence cannot be Inserted')
        ch=input("Do you wish to insert another row (y/n) : ")
        if ch=='n' or ch=='N':
            break
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError: 
    print("Start Mysql")
'''
Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition

1) How  to  call  execute()  method ?  --->   cur . execute(F'delete  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the  cond
'''

import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur=con.cursor()
    cond=input("Enter any condition : ")
    if cond=='':
        cur.execute(f'delete from student')
        con.commit()
    else:
        cur.execute(F'delete from student where {cond}')
        con.commit()
        print(f'{cur.rowcount} Rows Deleted')
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError: 
    print("Start Mysql")
'''
Write  a  program to  modify  data  of  emp  table

1) How  to  call  execute()  method ?  --->  cur . execute(F'update  emp  set  {expr}   where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  expr  and  cond
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

'''
Repeat  prog8b(fetchmany)  but  validate  input
i.e. Print  a  msg  when  input > number  of  tuples

Hint:  Use  fetchmany()  method
'''
import mysql.connector as mc
try:
    con=mc.connect(database='empdb',user='root')
    cur=con.cursor()
    cur.execute(f'select * from emp')
    n=int(input("How many rows ? : "))
    list=cur.fetchmany(n)
    if len(list)<n:
        print('invalid input')
    else:
        for x in cur.description:
            print(f'{x[0]:^10}',end='\t')
        print()
        for x in list:
            for a in x:
                print(f'{a:^10}',end='\t')
            print()
        print("Number of tuples fetched : ",cur.rowcount)
    cur.close()
    con.close()
except mc.errors.InternalError:
    print('cursor cannot be closed')
except mc.errors.ProgrammingError as msg:
    print(msg)
except mc.errors.DatabaseError:
    print('Start Mysql')
except AttributeError:
    print('Input cannot be negative')

'''
Write  a  program  to  insert  multiple  rows  into  emp  table

1) How  to  insert  multiple  rows  into  the  table ?  --->  With  executemany()  method

2) Where  is  executemany()  method  defined ?  --->  In  MySqlCursor  class  (like  execute()  method)

3) cur . executemany('insert   into  emp  values (%s,%s,%s)' ,  list)
    What  does  the  method  do ?  ---> Inserts  all  the  tuples  of  the  list  into  emp  table

4) What  is  first  %s  for ?  --->  First  element  of  each  tuple  in  the  list
    What  is  2nd  %s  for ?  ---> 2nd  element  of  each  tuple  in  the  list
    What  is  3rd  %s  for ?  ---> 3rd  element  of  each  tuple  in  the  list

5) How  many  rows  are  inserted  if  there  are  four  tuples  in  the  list  ?  ---> 4  rows
    What  is  the  result  of  cur . rowcount ? ---> 4

6) What  are  the  two  arguments  of  executemany()  method  ?  --->
						sql  command   and   list  of  tuples  where  each  tuple  is  a  row
'''

import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur=con.cursor()
    n=int(input("How many rows do you want to insert : ? "))
    list=[]
    for i in range(1,n+1):
        print("Faculty ",i)
        id=int(input("Enter Faculty Id : "))
        name=input("Enter Faculty Name : ")
        dept=input("Enter Faculty Dept : ")
        list.append((id,name,dept))
    try:
        cur.executemany(f"insert into faculty values(%s,%s,%s)",list)
        con.commit()
        print(f'{cur.rowcount} row is inserted')
    except mysql.connector.errors.IntegrityError:
        print('Duplicate Employee Id and Hence cannot be Inserted')
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError: 
    print("Start Mysql")