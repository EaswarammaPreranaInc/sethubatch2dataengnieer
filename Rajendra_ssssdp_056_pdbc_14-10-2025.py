
import mysql.connector
try:
    con = mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur=con.cursor()
    cur.execute('select * from emp')
    print(cur.rowcount)
    for x in cur:
        print(x)
        print(cur.rowcount)
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.Error.DatabaseError:
    print("start mqsql")
'''
o/p:
-1
(10, 'Rama Rao', 10000.0)
1
(20, 'vamsi', 25000.0)
2
(30, 'sita', 20000.0)
3
'''


'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''

import mysql.connector
try:
    con = mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur=con.cursor()
    cur.execute('select * from emp')
    for x in cur.description:
        print(f'{x[0]:^10}',end='\t')
    print()
    while x:=cur.fetchone():
        for i in x:
            print(f'{i:^10}',end='\t')
        print()
    print('Number of tuples :',cur.rowcount)
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError:
    print("start mqsql")
'''
o/p:
 empno           ename            sal    
    10           Rama Rao        10000.0  
    20            vamsi          25000.0
    30             sita          20000.0
Number of tuples : 3
'''


'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''

import mysql.connector
try:
    con = mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur = con.cursor()
    condition = input("Enter condition : ")
    query = f"SELECT * FROM emp WHERE {condition}"
    cur.execute(query)
    for x in cur.description:
        print(f'{x[0]:^10}', end='\t')
    print()
    count = 0
    while row := cur.fetchone():
        count += 1
        for value in row:
            print(f'{value:^10}', end='\t')
        print()
    print('Number of tuples :', count)
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError:
    print("Start mysql")
'''
o/p:
Enter condition : sal>15000
 empno           ename            sal    
    20            vamsi          25000.0  
    30             sita          20000.0
Number of tuples : 2
'''


'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''


import mysql.connector
try:
    con = mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur = con.cursor()
    order_by = input("Enter column name : ")
    query = f"SELECT * FROM emp order by {order_by}"
    cur.execute(query)
    for x in cur.description:
        print(f'{x[0]:^10}', end='\t')
    print()
    count = 0
    while row := cur.fetchone():
        count += 1
        for value in row:
            print(f'{value:^10}', end='\t')
        print()
    print('Number of tuples :', count)
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError:
    print("Start mysql")
'''
o/p:
Enter column name : sal
  empno           ename            sal    
    10           Rama Rao        10000.0
    30             sita          20000.0
    20            vamsi          25000.0
Number of tuples : 3
'''


'''
Write  a  program  to  print  user  input  table  with  next()  function

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  {table}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the   table  name

3) What  does  next(cur)  do ?  --->  Yields  the  next  tuple  of  cursor  object

4) What  does   next()  function  do  when  end  of   the  cursor  is  reached ?  ---> Throws StopIteration  error

5) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                          execute()                                   next()                  print()
'''

import mysql.connector
try:
    con =mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur =con.cursor()
    table =input("Enter table name: ")
    query = f"SELECT * FROM {table}"
    cur.execute(query)
    for x in cur.description:
        print(f'{x[0]:^10}', end='\t')
    print()
    count = 0
    while True:
        try:
            row=next(cur)      
            count += 1
            for i in row:
                print(f'{i:^10}', end='\t')
            print()
        except StopIteration:
            break
    print('Number of tuples :', count)
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError:
    print("Start MySQL")
'''
o/p:
Enter table name: emp
  empno           ename            sal    
    10           Rama Rao        10000.0
    20            vamsi          25000.0
    30             sita          20000.0
Number of tuples : 3
'''



'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''


import mysql.connector
try:
    con = mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur = con.cursor()
    cur.execute("select * from emp")
    tp1 = cur.fetchall()
    for x in cur.description:
        print(f'{x[0]:^10}', end='\t')
    print()
    for row in tp1:
        for i in row:
            print(f'{i:^10}', end='\t')
        print()
    print('Number of tuples :', len(tp1))
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError:
    print("Start MySQL server")
'''
o/p:
  empno           ename            sal    
    10           Rama Rao        10000.0
    20            vamsi          25000.0
    30             sita          20000.0    
Number of tuples : 3
'''
