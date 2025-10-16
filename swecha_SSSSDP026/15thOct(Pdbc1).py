# '''
# Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

# emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
#                      execute()                                 fetchone()             print()
# '''
# Emp Number       Emp Name                Salary
# 10                Rama Rao               10000.0
# 15                Kiran                  15000.0
# 20                Sita           20000.0
# Number  of  tuples :   3
# import mysql.connector
# conn = mysql.connector.connect(host="localhost",user="root",password="swechamac",database="company")
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM emp")
# for row in cursor.description:
#     print(row[0],end="\t")
# print() 
# while tpl:=cursor.fetchone():
#     for x in tpl:
#         print(x,end="\t") 
#     print()  
# print("Number of rows:",cursor.rowcount)      

# output:
# empno   ename   sal
# 10      RAMA RAO        10000.0
# 15      KIRAN   15000.0
# 20      SITA    20000.0
# Number of rows: 3
# '''
# Write  a  program  to  print  emp  table  based  on  user  condition

# 1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  emp  where  {cond}')

# 2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  condition  from  the  user

# 3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
#                          execute()                                 fetchone()              print()

# '''
# Enter  any  condition : sal > 12000
# Emp Number       Emp Name                Salary
#   15             Kiran                   15000.0
#   20             Sita                    20000.0
# Number  of  tuples  :  2
# import mysql.connector
# conn=mysql.connector.connect(host="localhost",user="root",password="swechamac",database="company")
# cursor=conn.cursor()
# cond=input("Enter any condition ")
# cursor.execute(F'select * from emp where {cond}')
# for row in cursor.description:
#     print(row[0],end="\t")
# print()  
# while tpl:=cursor.fetchone():
#     for x in tpl:
#         print(x,end="\t")
#     print() 
# print("number of rows:",cursor.rowcount)       

# output:
# Enter any condition sal >12000
# empno   ename   sal
# 15      KIRAN   15000.0
# 20      SITA    20000.0
# number of rows: 2

# '''
# Write  a  program  to  print  emp  table  in  sorted  order

# 1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

# 2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

# 3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
#                           execute()                                  fetchone()             print()
# '''
# Enter column name: sal desc
# Emp Number       Emp Name                Salary
#   20             Sita                    20000.0
#   15             Kiran                   15000.0
#   10             Rama Rao                10000.0
# Num  of rows :  3

# import mysql.connector
# conn=mysql.connector.connect(host="localhost",user="root",password="swechamac",database="company")
# cur = conn.cursor()
# colname = input("Enter column name to sort by ")
# cur.execute(F'select * from emp order by {colname}')
# for row in cur.description:
#     print(row[0],end="\t")
# print()  
# while tpl:=cur.fetchone():
#     for x in tpl:
#         print(x,end="\t")
#     print()   
# print("Number of rows:",cur.rowcount)  

# output:
# Enter column name to sort by sal desc
# empno   ename   sal
# 20      SITA    20000.0
# 15      KIRAN   15000.0
# 10      RAMA RAO        10000.0
# Number of rows: 3

# '''
# Write  a  program  to  print  user  input  table  with  next()  function

# 1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  {table}')

# 2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the   table  name

# 3) What  does  next(cur)  do ?  --->  Yields  the  next  tuple  of  cursor  object

# 4) What  does   next()  function  do  when  end  of   the  cursor  is  reached ?  ---> Throws StopIteration  error

# 5) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
#                           execute()                                   next()                  print()
# '''
# Enter   table  name :  emp
# Emp  Number      Emp  Name       Salary
#   10             Rama Rao        10000.00
#   15             Kiran           15000.00
#   20             Sita            20000.00
# Number  of  tuples :   3
# Enter   table  name :  stud
# 1146 (42S02): Table 'empdb.stud' doesn't exist

# import mysql.connector
# try:
#     conn=mysql.connector.connect(host="localhost",user="root",password="swechamac",database="company")
#     cur=conn.cursor()
#     table_name = input("Enter table name: ")
#     while table_name=='':
#               table_name = input('Enter table name:')
#     cur.execute(f'select *  from {table_name}')
#     for x in cur.description:
#       print(F'{x[0]}:^10')
#     print()  
#     while True:
#             try:  
#                  tpl = next(cur)
#                  for x in tpl:
#                               print(F'{x:^10}'),end="\t"
#                  print()
#             except StopIteration:
#                    break    
#     print("Number of rows:",cur.rowcount)
#     cur.close()
#     conn.close()
# except mysql.connector .errors . proggrammingError as msg: 
#        print("msg")   
# except mysql.connector.errors.DatabaseError:
#        print("pls start mysql")

# output:
# Enter table name: emp
# empno   ename   sal
# 10      RAMA RAO        10000.0
# 15      KIRAN   15000.0
# 20      SITA    20000.0
# Number of rows: 3      

# '''
# Write  a  program  to  print  cursor  with  fetchall()  method

#  emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
#                        execute()                               fetchall()                    for  loop                print()
# '''
# Emp Number       Emp Name        Salary
#   10             Rama Rao          10000.00
#   15             Kiran             15000.00
#   20             Sita              20000.00
# Number  of  tuples  :  3

# import mysql.connector 
# try:
#     conn = mysql.connector.connect(host="localhost",user="root",password="swechamac",database="company")
#     cur = conn.cursor()
#     cur.execute('select * from emp')
#     rows = cur.fetchall()
#     for x in cur.description:
#         print(f'{x[0]:^10}', end="\t")
#     print()  
#     for tpl in rows:
#         for x in tpl:
#             print(f'{x:^10}', end="\t") 
#         print() 
#     print("Number of tuples:", len(rows))  
#     cur.close()
#     conn.close()
# except mysql.connector.errors.ProgrammingError as msg:
#     print("msg")
# except mysql.connector.errors.DatabaseError:
#     print("pls start mysql")   

#     output:
#     empno           ename            sal    
#     10           RAMA RAO        10000.0  
#     15            KIRAN          15000.0  
#     20             SITA          20000.0  
# Number of tuples: 3 


    




