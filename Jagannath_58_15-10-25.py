Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
import mysql.connector as mc
try:
  con=mc.connect(database='empdb',user='root')
  cur=con.cursor()
  cur.execute('select * from emp')
  for x in cur.description:
           print(f'{x[0]:^10}',end='/t')
  print()
  while tpl:=cur.fetchone():
           for x in tpl:
                print(f'{x[0]:^10}',end='/t')
           print()
 print('Number of tuples:',cur.rowcount)
 cur.close()
 con.close()
except mc.errors.ProgrammingError as msg:
    print(msg)
except mc.errors.DatabaseError:
    print('please start mysql')

Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()
import mysql.connector as mc
try:
    con = mc.connect(user='root',database='empdb')
    cur = con.cursor()
    cond = input("Enter condition for employee search: ")
    cur.execute(f'SELECT * FROM emp WHERE {cond}')
    for x in cur.description:
        print(f'{x[0]:^15}', end='\t')
    while True:
        tpl = cur.fetchone()
        if tpl is None:
            break
        for val in tpl:
            print(f'{val:^15}', end='\t')
        print()
    print('\nNumber of tuples:', cur.rowcount)
    cur.close()
    con.close()
except mc.errors.ProgrammingError as msg:
    print('Programming Error:', msg)
except mc.errors.DatabaseError:
    print('Please start MySQL')

Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
import mysql.connector as mc
try:
    con = mc.connect(user='root',database='empdb')
    cur = con.cursor()
    colname = input("Enter column name to sort by (e.g., ename, sal, deptno): ")
    cur.execute(f'SELECT * FROM emp ORDER BY {colname}')
    for col in cur.description:
        print(f'{col[0]:^15}', end='\t')
    while True:
        tpl = cur.fetchone()
        if tpl is None:
            break
        for val in tpl:
            print(f'{val:^15}', end='\t')
        print()
    print('\nNumber of tuples:', cur.rowcount)
    cur.close()
    con.close()
except mc.errors.ProgrammingError as msg:
    print('Programming Error:', msg)
except mc.errors.DatabaseError:
    print('Please start MySQL')

Write  a  program  to  print  user  input  table  with  next()  function

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  {table}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the   table  name

3) What  does  next(cur)  do ?  --->  Yields  the  next  tuple  of  cursor  object

4) What  does   next()  function  do  when  end  of   the  cursor  is  reached ?  ---> Throws StopIteration  error

5) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                          execute()                                   next()                  print()
import mysql.connector as mc
try:
    con = mc.connect(user='root',database='empdb')
    cur = con.cursor()
    table = input("Enter table name to display: ")
    cur.execute(f'SELECT * FROM {table}')
    for col in cur.description:
        print(f'{col[0]:^15}', end='\t')
    while True:
        try:
            tpl = next(cur)   
            for val in tpl:
                print(f'{val:^15}', end='\t')
            print()
        except StopIteration:
            break   
    print('\nNumber of tuples:', cur.rowcount)
    cur.close()
    con.close()
except mc.errors.ProgrammingError as msg:
    print('Programming Error:', msg)
except mc.errors.DatabaseError:
    print('Please start MySQL server.')

Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
import mysql.connector as mc
try:
    con = mc.connect(user='root',database='empdb')
    cur = con.cursor()
    cur.execute('SELECT * FROM emp')
    rows = cur.fetchall()
    for col in cur.description:
        print(f'{col[0]:^15}', end='\t')
    for tpl in rows:
        for val in tpl:
            print(f'{val:^15}', end='\t')
        print()
    print('\nNumber of tuples:', cur.rowcount)
    cur.close()
    con.close()
except mc.errors.ProgrammingError as msg:
    print('Programming Error:', msg)
except mc.errors.DatabaseError:
    print('Please start MySQL server.')
