'''
Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition

1) How  to  call  execute()  method ?  --->   cur . execute(F'delete  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the  cond
'''

import mysql.connector

try:
    con=mysql.connector.connect(host='localhost',user='root',database='empdb')
    cur=con.cursor()
    
    cond=input("Enter the Condition  :")

    cur.execute(f'select * from emp where {cond}')


    for x in cur.description:
        print(f'{x[0]:^10}',end='\t')
    print()
    try:
        x=cur.fetchall()
        for i in x:
            for j in i:
                print(f'{j:^10}',end='\t')
            print()
    except StopIteration:
        
        print("Number of Tuples :",cur.rowcount)

except mysql.connector.errors.ProgrammingError as msg:
    print("Programming error:", msg)
except mysql.connector.errors.DatabaseError as msg:
    print("Database not found", msg)
except mysql.connector.errors.InterfaceError:
    print("Start Mysql")
          


