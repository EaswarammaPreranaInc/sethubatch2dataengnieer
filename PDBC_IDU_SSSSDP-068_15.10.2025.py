'''
Write  a  program  to  print  first  'n'  rows  of  emp  table

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
'''


import mysql.connector as mc
try:
    con = mc.connect(host='localhost', database='empdb', user='root')
    cur = con.cursor()
    n=int(input('How many rows to fetch : '))
    cur.execute('select * from emp')
    list=cur.fetchmany(n)
    if list:
        for x in cur.description:
            print(f'{x[0]:^10}', end = '\t')
        print()
    for tpl in list:
        for y in tpl:
            print(f'{y:^10}', end = '\t')
        print()
    print("Number of tuples fetched : ",len(list))
    cur.close() 
    con.close()
except mc.errors.InternalError as msg:
    print('cursor can not be closed')

except mc.errors.ProgrammingError as msg:
    print(msg)

except mc.errors.DatabaseError:
    print('Pls start mysql')

except AttributeError: 
    print('Input should be a +ve number')



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
    con = mc.connect(database='empdb', user='root')
    cur = con.cursor()
    while True:
        try:
            empno = int(input('Enter empno : '))
            ename = input('Enter emp name : ')
            sal = float(input('Enter salary : '))

            cur.execute(F"insert into emp values ({empno},'{ename}',{sal})")

            con.commit()
            print(F'{cur.rowcount} row is inserted')

        except mc.errors.IntegrityError:
            print('Duplicate empno and hence row can not be inserted')

        ch = input('Insert another row? (y / n) : ')
        if ch == 'N' or ch == 'n':
            break

except mc.errors.ProgrammingError as msg:
    print(msg)

except mc.errors.DatabaseError:
    print('Pls start mysql')



'''
Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition

1) How  to  call  execute()  method ?  --->   cur . execute(F'delete  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the  cond
'''


import mysql.connector as mc

try:
    con = mc.connect(database='empdb', user='root')
    cur = con.cursor()
    cond = input('Enter condition : ')
    if cond == '':
        cur.execute(F'delete from emp')
    else:
        cur.execute(F'delete from emp where {cond}')
    
    con.commit()
    print(cur.rowcount, 'rows are deleted')
    cur.close()
    con.close()

except mc.errors.ProgrammingError as msg:
    print(msg)
except mc.errors.DatabaseError:
    print('Pls start mysql')



'''
Write  a  program to  modify  data  of  emp  table

1) How  to  call  execute()  method ?  --->  cur . execute(F'update  emp  set  {expr}   where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  expr  and  cond
'''

import mysql.connector as mc
try:
    con = mc.connect(host='localhost', database='empdb', user='root')
    cur = con.cursor()
    expr=input('Give expression : ')
    cond=input('Condition : ')
    if cond == '' and expr=='':
        cur.execute(F'select * from emp')
    else:
        cur . execute(F'update  emp  set  {expr}   where  {cond}')
    con.commit()
    print(cur.rowcount, 'rows are updated')
    cur.close()
    con.close()

except mc.errors.ProgrammingError as msg:
    print(msg)
except mc.errors.DatabaseError:
    print('Pls start mysql')



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
    con = mc.connect(host='localhost', database='empdb', user='root')
    cur = con.cursor()
    tablename=input('Give expression : ')
    try:
        cur . execute(F'create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float)')
    except:
        cur . execute(F'drop table {tablename};')
        cur . execute(F'create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float)')
        
    con.commit()
    print(tablename, 'Table Created Successfully')
    cur.close()
    con.close()

except mc.errors.ProgrammingError as msg:
    print(msg)
except mc.errors.DatabaseError:
    print('Pls start mysql')





