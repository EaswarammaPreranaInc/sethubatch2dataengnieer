'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()

Emp Number       Emp Name                Salary
10                Rama Rao               10000.0
15                Kiran                  15000.0
20                Sita           20000.0
Number  of  tuples :   3

'''

import mysql.connector

try:
    con=mysql.connector.connect(host='localhost',user='root',database='empdb')
    cur=con.cursor()
    cur.execute('select * from emp')
    for i in cur.description:
        print(f'{i[0]:^10}',end='\t')
    print()
    while x:=cur.fetchone():
        for i in x:
            print(f'{i:^10}',end='\t')  
        print() 
    print("Number of Tuples  :",cur.rowcount)

except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
  
except mysql.connector.errors.InterfaceError:
    print("Start Mysql")
