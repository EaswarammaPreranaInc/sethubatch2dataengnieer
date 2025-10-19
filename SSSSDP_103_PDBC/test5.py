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
    con=mysql.connector.connect(host='localhost',user='root',database='empdb')
    cur=con.cursor()
    
    table=input("Enter the Table name :")

    cur.execute(f'select * from {table}')


    for x in cur.description:
        print(f'{x[0]:^10}',end='\t')
    print()
    try:
        while x:=next(cur):
            for i in x:
                print(f'{i:^10}',end='\t')
            print()
    except StopIteration:
        
        print("Number of Tuples :",cur.rowcount)

except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.InterfaceError:
    print("Start Mysql")
          

