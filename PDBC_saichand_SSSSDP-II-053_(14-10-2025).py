'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

#Sample output:
Enter  any  condition : sal > 12000
Emp Number       Emp Name                Salary
  15             Kiran                   15000.0
  20             Sita                    20000.0
Number  of  tuples  :  2
'''

#Program:
import mysql.connector
try:
    con = mysql.connector.connect(host='localhost', database='empdb', user='root')
    cur = con.cursor()
    cond=input('Enter condition : ')
    cur.execute(f'select * from emp where {cond}')
    print(cur.rowcount)
    for x in cur.description:
        print(f'{x[0]:^10}', end = '\t')
    print()
    while tpl:= cur.fetchone():
        for y in tpl:
            print(f'{y:^10}', end = '\t')
        print()
    print(cur.rowcount)
    cur.close() 
    con.close()

except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError:
    print('Start mysql')








'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()

#Sample output:
Enter column name: sal desc
Emp Number       Emp Name                Salary
  20             Sita                    20000.0
  15             Kiran                   15000.0
  10             Rama Rao                10000.0
Num  of rows :  3
'''

#Program:
import mysql.connector
try:
    con = mysql.connector.connect(host='localhost', database='empdb', user='root')
    cur = con.cursor()
    col=input('Enter Column name to sort  : ')
    cur.execute(f'select * from emp order by {col}')
    print(cur.rowcount)
    for x in cur.description:
        print(f'{x[0]:^10}', end = '\t')
    print()
    while tpl:= cur.fetchone():
        for y in tpl:
            print(f'{y:^10}', end = '\t')
        print()
    print(cur.rowcount)
    cur.close() 
    con.close()

except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError:
    print('Start mysql')








'''
Write  a  program  to  print  user  input  table  with  next()  function

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  {table}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the   table  name

3) What  does  next(cur)  do ?  --->  Yields  the  next  tuple  of  cursor  object

4) What  does   next()  function  do  when  end  of   the  cursor  is  reached ?  ---> Throws StopIteration  error

5) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                          execute()                                   next()                  print()
#Sample output:
Enter   table  name :  emp
Emp  Number      Emp  Name       Salary
  10             Rama Rao        10000.00
  15             Kiran           15000.00
  20             Sita            20000.00
Number  of  tuples :   3
Enter   table  name :  stud
1146 (42S02): Table 'empdb.stud' doesn't exist
'''

#Program:
import mysql.connector
try:
    con = mysql.connector.connect(host='localhost', database='empdb', user='root')
    cur = con.cursor()
    table=input('Enter the table name  : ')
    cur.execute(f'select * from {table}')
    print(cur.rowcount)
    for x in cur.description:
        print(f'{x[0]:^10}', end = '\t')
    print()
    while True:
        try:
            for y in next(cur):
                print(f'{y:^10}', end = '\t')
            print()
        except StopIteration:
            break
    print(cur.rowcount)
    cur.close() 
    con.close()

except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError:
    print('Start mysql')








'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()

#Sample output:
Emp Number       Emp Name        Salary
  10             Rama Rao          10000.00
  15             Kiran             15000.00
  20             Sita              20000.00
Number  of  tuples  :  3
'''

#Program:
import mysql.connector
try:
    con = mysql.connector.connect(host='localhost', database='empdb', user='root')
    cur = con.cursor()
    cur.execute(f'select * from emp')
    print(cur.rowcount)
    for x in cur.description:
        print(f'{x[0]:^10}', end = '\t')
    print()
    rows = cur.fetchall()
    if rows:
        for row in rows:
            for value in row:
                print(f'{value:^10}', end='\t')
            print()
    else:
        print("No records found.")
    print(cur.rowcount)
    cur.close() 
    con.close()

except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError:
    print('Start mysql')