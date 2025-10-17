'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
              execute()                         fetchone()           print()
'''
'''
Emp Number       Emp Name                Salary
10                Rama Rao               10000.0
15                Kiran                  15000.0
20                Sita                   20000.0
Number of tuples : 3
'''
import mysql.connector as mc
try:
    con = mc.connect(host = 'localhost', database = 'empdb', user = 'root', password = '')
    cur = con.cursor()
    table = input("Enter table name:")
    cur.execute(F'select * from {table}')
    for x in cur.description:
        print(F'{x[0]:^10}', end = '\t')
    print()
    while tpl := cur.fetchone():
        for x in tpl:
            print(F'{x:^10}', end = '\t')
        print()
    print('Number of tuples:', cur.rowcount)
    cur.close()
    con.close()
except mc.errors.ProgrammingError as msg:
    print('Error:', msg)
except mc.errors.DatabaseError:
    print('Pls start mysql')
'''
Outputs
Enter table name:emp
  empno           ename            sal    
    10          Vaishnavi        10000.0  
    20           Srinivas        20000.0
    30            Mahesh         35000.0
    40            Jyothi         40000.0
Number of tuples: 4
'''









'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                  execute()                        fetchone()           print()
Enter  any  condition : sal > 12000
Emp Number       Emp Name                Salary
  15             Kiran                   15000.0
  20             Sita                    20000.0
Number of tuples : 2
'''
import mysql.connector as mc
try:
    con = mc.connect(host = 'localhost', database = 'empdb', user = 'root', password = '')
    cur = con.cursor()
    cond = input("Enter condition:")
    cur.execute(F'select * from emp where {cond}')
    for x in cur.description:
        print(F'{x[0]:^10}', end = '\t')
    print()
    while tpl := cur.fetchone():
        for x in tpl:
            print(F'{x:^10}', end = '\t')
        print()
    print('Number of tuples:', cur.rowcount)
    cur.close()
    con.close()
except mc.errors.ProgrammingError as msg:
    print('Error:', msg)
except mc.errors.DatabaseError:
    print('Pls start mysql')
'''
Outputs
Enter condition:sal>20000
  empno           ename            sal    
    30            Mahesh         35000.0
    40            Jyothi         40000.0
Number of tuples: 2
Enter condition:empno = 20
  empno           ename            sal    
    20           Srinivas        20000.0
Number of tuples: 1
Enter condition:ename like '%s%'
  empno           ename            sal    
    10          Vaishnavi        10000.0
    20           Srinivas        20000.0
    30            Mahesh         35000.0
Number of tuples: 3
Enter condition:ename like 'J%'
  empno           ename            sal    
    40            Jyothi         40000.0
Number of tuples: 1
Enter condition:ename like '%i'
  empno           ename            sal    
    10          Vaishnavi        10000.0
    40            Jyothi         40000.0
Number of tuples: 2
'''









'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                 execute()                        fetchone()          print()
Enter column name: sal desc
Emp Number       Emp Name                Salary
  20             Sita                    20000.0
  15             Kiran                   15000.0
  10             Rama Rao                10000.0
Num of rows : 3                                                                
'''
import mysql.connector as mc
try:
    con = mc.connect(host = 'localhost', database = 'empdb', user = 'root', password = '')
    cur = con.cursor()
    colname = input("Enter column name:")
    cur.execute(F'select * from emp order by {colname}')
    for x in cur.description:
        print(F'{x[0]:^10}', end = '\t')
    print()
    while tpl := cur.fetchone():
        for x in tpl:
            print(F'{x:^10}', end = '\t')
        print()
    print('Number of tuples:', cur.rowcount)
    cur.close()
    con.close()
except mc.errors.ProgrammingError as msg:
    print('Error:', msg)
except mc.errors.DatabaseError:
    print('Pls start mysql')
'''
Outputs
Enter column name:sal
  empno           ename            sal    
    10          Vaishnavi        10000.0
    20           Srinivas        20000.0
    30            Mahesh         35000.0
    40            Jyothi         40000.0
Number of tuples: 4
Enter column name:ename
  empno           ename            sal    
    40            Jyothi         40000.0
    30            Mahesh         35000.0
    20           Srinivas        20000.0
    10          Vaishnavi        10000.0
Number of tuples: 4
'''









'''
Write  a  program  to  print  user  input  table  with  next()  function

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  {table}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the   table  name

3) What  does  next(cur)  do ?  --->  Yields  the  next  tuple  of  cursor  object

4) What  does   next()  function  do  when  end  of   the  cursor  is  reached ?  ---> Throws StopIteration  error

5) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                  execute()                           next()            print()
Enter   table  name :  emp
Emp  Number      Emp  Name       Salary
  10             Rama Rao        10000.00
  15             Kiran           15000.00
  20             Sita            20000.00
Number of tuples : 3
Enter table  name :  stud
1146 (42S02): Table 'empdb.stud' doesn't exist
'''
import mysql.connector as mc
try:
    con = mc.connect(host = 'localhost', database = 'empdb', user = 'root', password = '')
    cur = con.cursor()
    table_name = input("Enter table name:")
    cur.execute(F'select * from {table_name}')
    for x in cur.description:
        print(F'{x[0]:^10}', end = '\t')
    print()
    while True:
        try:
            tpl = next(cur)
            for x in tpl:
                print(F'{x:^10}', end = '\t')
            print()
        except StopIteration:
            break
    print('Number of tuples:', cur.rowcount)
    cur.close()
    con.close()
except mc.errors.ProgrammingError as msg:
    print('Error:', msg)
except mc.errors.DatabaseError:
    print('Pls start mysql')
'''
Outputs
Enter table name:emp
  empno           ename            sal    
    10          Vaishnavi        10000.0
    20           Srinivas        20000.0
    30            Mahesh         35000.0
    40            Jyothi         40000.0
Number of tuples: 4
Enter table name:employee
Error: 1146 (42S02): Table 'empdb.employee' doesn't exist
'''









'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                execute()                        fetchall()                 for  loop               print()
Emp Number       Emp Name        Salary
  10             Rama Rao          10000.00
  15             Kiran             15000.00
  20             Sita              20000.00
Number of tuples : 3
'''
import mysql.connector as mc
try:
    con = mc.connect(host = 'localhost', database = 'empdb', user = 'root', password = '')
    cur = con.cursor()
    table = input("Enter table name:")
    cur.execute(F'select * from {table}')
    for x in cur.description:
        print(F'{x[0]:^10}', end = '\t')
    print()
    list = cur.fetchall()
    for tpl in list:
        for x in tpl:
            print(F'{x:^10}', end = '\t')
        print()
    print('Number of tuples:', cur.rowcount)
    cur.close()
    con.close()
except mc.errors.ProgrammingError as msg:
    print('Error:', msg)
except mc.errors.DatabaseError:
    print('Pls start mysql')
'''
Outputs
 empno           ename            sal    
    10          Vaishnavi        10000.0
    20           Srinivas        20000.0
    30            Mahesh         35000.0
    40            Jyothi         40000.0
Number of tuples: 4
'''