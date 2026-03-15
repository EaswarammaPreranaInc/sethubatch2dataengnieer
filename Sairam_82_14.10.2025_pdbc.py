'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''
import mysql.connector
con = mysql.connector.connect(
    host='localhost',user='root',password='12345678',database='empdb'
)
cur = con.cursor()
cur.execute('SELECT * FROM emp')
for col in cur.description:
    print(col[0], end='\t')
print()
while tpl :=cur.fetchone():
    for i in tpl:
        print(i, end='\t')
    print()

print('no of rows:',cur.rowcount)  
con.close()


'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''

import mysql.connector
con = mysql.connector.connect(
    host='localhost',user='root',password='12345678',database='empdb'
)
cond=input('Enter condition: ')
cur = con.cursor()
if cond=='':
    cur.execute('SELECT * FROM emp')
else:
    cur.execute(F'SELECT * FROM emp WHERE {cond}')
for col in cur.description:
    print(col[0], end='\t')
print()
while tpl :=cur.fetchone():
    for i in tpl:
        print(i, end='\t')
    print()

print('no of rows:',cur.rowcount) 
con.close()


'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''
import mysql.connector
con = mysql.connector.connect(
    host='localhost',user='root',password='12345678',database='empdb'
)
col=input('Enter column name: Asc or Desc -')
cur = con.cursor()
if col=='':
    cur.execute('select * FROM emp')
else:
    cur.execute(F'select * FROM emp order by {col}')
for col in cur.description:
    print(col[0], end='\t')
print()

while tpl :=cur.fetchone():
    for i in tpl:
        print(i, end='\t')
    print()

print('no of rows:',cur.rowcount) 
con.close()


'''
Write  a  program  to  print  user  input  table  with  next()  function

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  {table}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the   table  name

3) What  does  next(cur)  do ?  --->  Yields  the  next  tuple  of  cursor  object

4) What  does   next()  function  do  when  end  of   the  cursor  is  reached ?  ---> Throws StopIteration  error

5) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                          execute()                                   next()                  print()
'''
try:
    import mysql.connector
    con = mysql.connector.connect(
        host='localhost',user='root',password='12345678',database='empdb'
    )
    table=input('Enter table name -')
    cur = con.cursor()
    while table=='':
        table=input('Enter table name -')
    cur.execute(F'select * FROM {table}')
    for col in cur.description:
        print(col[0], end='\t')
    print()

    while True:
        try:
            tpl=next(cur)
            for i in tpl:
                print(i, end='\t')
            print()
        except: 
            break

    print('no of rows:',cur.rowcount) 
    con.close()
except mysql.connector.ProgrammingError as msg:
    print(msg)



'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''
try:
    import mysql.connector
    con = mysql.connector.connect(
        host='localhost',user='root',password='12345678',database='empdb'
    )
    table=input('Enter table name -')
    cur = con.cursor()
    while table=='':
        table=input('Enter table name -')
    cur.execute(F'select * FROM {table}')
    list=cur.fetchall()
    for col in cur.description:
        print(col[0], end='\t')
    print()
    for tpl in list:
        for i in tpl:
                print(i, end='\t')
        print()

    print('no of rows:',cur.rowcount) 
    con.close()
except mysql.connector.ProgrammingError as msg:
    print(msg)


