'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()
                         
    
Enter the Conditon :  
    id             name            sal    
    1              raju          20000.0
    2             nandha         30000.0
    3            shruthik        40000.0
    4              sai           15000.0
    5              ramu          35000.0
Number of Tuples : 5  


py test3.py

Enter the Conditon :sal>20000
    id             name            sal    
    2             nandha         30000.0
    3            shruthik        40000.0
    5              ramu          35000.0
Number of Tuples : 3                   

'''

import mysql.connector

try:
    con=mysql.connector.connect(host='localhost',user='root',database='empdb')
    cur=con.cursor()
    cond=input("Enter the Conditon :")
    if cond=='':
        cur.execute(f'select * from emp')
    else:
        cur.execute(f'select * from emp where {cond}')


    for x in cur.description:
        print(f'{x[0]:^10}',end='\t')
    print()
    while x:=cur.fetchone():
        for i in x:
            print(f'{i:^10}',end='\t')
        print()
    print("Number of Tuples :",cur.rowcount)

except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
  
except mysql.connector.errors.InterfaceError:
    print("Start Mysql")
          

