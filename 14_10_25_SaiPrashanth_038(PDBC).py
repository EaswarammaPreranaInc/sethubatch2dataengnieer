'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''
import mysql.connector
con=mysql.connector.connect(host='localhost',database='company_db',user='root',password='Sai@1234')
cur=con.cursor()
cur.execute("select * from emp")
for i in cur.description:
    print(f'{i[0]:^10}',end='\t')
print()
tpl=cur.fetchall()
for i in tpl:
    for x in i:
        print(f'{x:^10}',end='\t')
    print()
print('Number  of tuples : ',cur.rowcount)
con.close()
cur.close()


'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''
import mysql.connector
con=mysql.connector.connect(host='localhost',database='company_db',user='root',password='Sai@1234')
cur=con.cursor()
cond=input("Enter  the  condition  to  fetch  the  records : ")
cur.execute(F'select * from emp where {cond}')
for i in cur.description:
    print(f'{i[0]:^10}',end='\t')
print()
tpl=cur.fetchall()
for i in tpl:
    for x in i:
        print(f'{x:^10}',end='\t')
    print()
print('Number  of tuples : ',cur.rowcount)
con.close()
cur.close()


'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''
import mysql.connector
con=mysql.connector.connect(host='localhost',database='company_db' ,user='root',password='Sai@1234')
cur=con.cursor()
colname=input("Enter  the  column  name  to  sort  the  records : ")
cur.execute(F'select * from emp order by {colname}')
for i in cur.description:
    print(f'{i[0]:^10}',end='\t')
print()
tpl=cur.fetchall()
for i in tpl:
    for x in i:
        print(f'{x:^10}',end='\t')
    print()
print('Number  of tuples : ',cur.rowcount)
con.close()
cur.close()


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
con=mysql.connector.connect(host='localhost',database='company_db' ,user='root',password='Sai@1234')
cur=con.cursor()
table=input("Enter  the  table  name  to  fetch  the  records : ")
cur.execute(F'select * from {table}')
for i in cur.description:
    print(f'{i[0]:^10}',end='\t')   
print()
while True:
    try:
        tpl=next(cur)
        for x in tpl:
            print(f'{x:^10}',end='\t')
        print()
    except StopIteration:
        break           
print('Number  of tuples : ',cur.rowcount)
con.close()
cur.close()


'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''
import mysql.connector
con=mysql.connector.connect(host='localhost',database='company_db' ,user='root',password='Sai@1234')
cur=con.cursor()
cur.execute("select * from emp")
for i in cur.description:
    print(f'{i[0]:^10}',end='\t')
print()
tpl=cur.fetchall()
for i in tpl:
    for x in i:
        print(f'{x:^10}',end='\t')
    print()
print('Number  of tuples : ',cur.rowcount)
con.close()
cur.close()
