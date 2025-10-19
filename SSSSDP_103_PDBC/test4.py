'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''


import mysql.connector

try:
    con=mysql.connector.connect(host='localhost',user='root',database='empdb')
    cur=con.cursor()
    colname=input("Enter the Column name :")
    if colname=='':
        cur.execute(f'select * from emp')
    else:
        cur.execute(f'select * from emp   order by {colname}  ')


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
          

