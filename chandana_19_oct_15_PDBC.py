'''
Write  a  program  to  print  first  'n'  rows  of  emp  table

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
'''

import mysql.connector
try:
    con = mysql.connector.connect(host='localhost',database='empdb',user='root',password='pass123')
    cur=con.cursor()
    n=int(input('Enter number of rows : '))
    if n<0:
        print('input should be +ve integer')
    elif n==0:
        print('Number of tuples :',0)
    else:
        cur.execute("select * from emp")
        a=cur.fetchmany(n)
        for x in cur.description:
            print(f'{x[0]:^10}', end='\t')
        print()
        for row in a:
            for i in row:
                print(f'{i:^10}', end='\t')
            print()
        print('Number of tuples :', len(a))
        cur.close()
        con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)  
except mysql.connector.errors.DatabaseError:
    print("Start mysql")




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


import mysql.connector as mc
try:
    con=mc.connect(host='localhost',database='empdb',user='root',password='pass123')
    cur=con.cursor()
    while True:
        empno=int(input('Enter empno :'))
        ename=input('Enter ename :')
        sal=float(input('Enter sal :'))
        try:
            cur.execute(f"insert into emp values({empno} ,'{ename}',{sal})")
            con.commit()
            print(f'{cur.rowcount}')
        except mc.errors.IntegrityError:
            print('Duplicates empno so row cannot be inserted')
        x=input('insert another row?(y/n) :')
        if x=='N' or x=='n':
            break
except mc.errors.ProgrammingError as msg :
    print(msg)
except mc.errors.DatabaseError:
    print('start mysql')




'''
Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition

1) How  to  call  execute()  method ?  --->   cur . execute(F'delete  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the  cond
'''

import mysql.connector as mc
try:
    con=mc.connect(host='localhost',database='empdb',user='root',password='pass123')
    cur=con.cursor()
    condition=input('enter condition :')
    if condition=='':
        cur.execute(f'delete from emp')
    else:
        cur.execute(f'delete from emp where {condition}')
    con.commit()
    print(cur.rowcount,'rows are deleted')
    cur.close()
    con.close()
except mc.errors.ProgrammingError as msg :
    print(msg)
except mc.errors.DatabaseError:
    print('start mysql')




'''
Write  a  program to  modify  data  of  emp  table

1) How  to  call  execute()  method ?  --->  cur . execute(F'update  emp  set  {expr}   where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  expr  and  cond
'''

import mysql.connector as mc
try:
    con=mc.connect(host='localhost',database='empdb',user='root',password='pass123')
    cur=con.cursor()
    condition=input('enter condition :')
    expression=input('enter expression :')
    if condition=='':
        cur.execute(f'update emp set {expression}')
    else:
        cur.execute(f'update emp set {expression} where {condition}')
    con.commit()
    print(cur.rowcount,'rows are updates')
    cur.close()
    con.close()
except mc.errors.ProgrammingError as msg :
    print(msg)
except mc.errors.DatabaseError:
    print('start mysql')


'''
Write  a  program  to  create  student  table

1) How  to  call  execute()  method ?  --->
									cur . execute(F'create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float)')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  table  name

3) What  action  to  be  made  when  table  already  exists ?  --->
																	Delete  the  existing  table  and  create  a  new  table  with  same  name
'''

import mysql.connector as mc
try:
    con=mc.connect(host='localhost',database='empdb',user='root',password='pass123')
    cur=con.cursor()
    table=input('enter table name :')
    cur.execute(f'create table {table} (rollno int primary key, student_name char(20), hobbies char(30))')
    print(table, 'table is created')
    cur.close()
    con.close()
except mc.errors.ProgrammingError as msg :
    cur.execute(f'drop table {table}')
    print(f'existing {table} table is deleted')
    cur.execute(f'create table {table} (rollno int primary key, student_name char(20), hobbies char(30))')
    print(f'New {table} is created')
except mc.errors.DatabaseError:
    print('start mysql')
'''
o/p:
enter table name :students
students table is created
'''