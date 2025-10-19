'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()


Emp Number       Emp Name        Salary
  10             Rama Rao          10000.00
  15             Kiran             15000.00
  20             Sita              20000.00
Number  of  tuples  :  3
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
          


