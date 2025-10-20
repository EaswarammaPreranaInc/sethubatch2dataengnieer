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
    con=mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur=con.cursor()
    while True:
        id=int(input("Enter Employee Id : "))
        name=input("Enter Employee Name : ")
        sal=float(input("Enter Employee Salary : "))
        try:
            cur.execute(f"insert into emp values({id},'{name}',{sal})")
            con.commit()
            print(f'{cur.rowcount} row is inserted')
        except mysql.connector.errors.IntegrityError:
            print('Duplicate Employee Id and Hence cannot be Inserted')
        ch=input("Do you wish to insert another row (y/n) : ")
        if ch=='n' or ch=='N':
            break
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError: 
    print("Start Mysql")