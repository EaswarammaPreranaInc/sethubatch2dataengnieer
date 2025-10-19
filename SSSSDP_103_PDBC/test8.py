'''
Write  a  program  to  insert  rows  into  emp  table ,  one  at  a  time

1) How  to  call  execute()  method ?  --->
															cur . execute(F"insert  into  emp  values  ({empno} ,  '{ename}' , {sal})")

2) Are  quotes  mandatory  for  ename ? --->  Yes  becoz  it  is  a  string

3) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  inputs  empno , ename  and  sal

4) What  action  to  be  made  after  insert ?  --->  Call  commit()  method

5) What  does  commit()  method  do ?  --->  Makes  insertion  becomes  permanent

6) What  happens  when  commit()  is  not  called ?  --->  Insertion  is  only  temporary

7) In  other  words,  insertion  does  not  happen

8) Where  is  commit()  method  defined ?  ---> In  MySqlConnection  class

9) cur . execute(F'insert  into  emp  values (25 , "Rama  Rao" , 10000.0)')
    What  is  the  result  of  cur . rowcount ?  ---> 1  becoz  only  one  row  is  inserted  into  emp  table

10) Can  a  tuple  be  inserted  into  cur  object ?  --->  No  becoz  it  is  immutable

11) What  happens  when  we  try  to  insert  duplicate  empno ?  --->  Raises  mc . errors . IntegrityError
'''

import mysql.connector

try:
    
    con = mysql.connector.connect(host='localhost', user='root', database='empdb')
    cur = con.cursor()
    while True:
        
        empno = int(input("Enter the Emp No :"))
        ename = input("Enter the Emp Name :")
        sal = float(input("Enter the Emp Salary :"))
        cur.execute(F"insert  into  emp  values  ({empno} ,  '{ename}' , {sal})")
        con.commit()
        print("Record inserted successfully.")
        ch = input("Do you want to insert a record (y/n) ? ")
        if ch.lower() == 'n':
            break
    print("Rows Inserted :", cur.rowcount)
    
except mysql.connector.errors.IntegrityError as msg:
    print("Integrity error:", msg)  
except mysql.connector.errors.ProgrammingError as msg:
    print("Programming error:", msg)  
except mysql.connector.errors.DatabaseError as msg:
    print("Database not found:", msg)
except mysql.connector.errors.InterfaceError:
    print("Start MySQL server")
finally:
    if 'con' in locals() and con.is_connected():
        cur.close()
        con.close()

