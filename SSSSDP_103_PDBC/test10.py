
'''
Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition

1) How  to  call  execute()  method ?  --->   cur . execute(F'delete  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read the cond
'''

import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur=con.cursor()
    cond=input("Enter any condition : ")
    if cond=='':
        cur.execute(f'delete from emp')
        con.commit()
    else:
        cur.execute(F'delete from emp where {cond}')
        con.commit()
        print(f'{cur.rowcount} Rows Deleted')
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError: 
    print("Start Mysql")