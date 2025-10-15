Write  a  program  to  print  first  'n'  rows  of  emp  table

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
import mysql.connector as mc
try:
    con = mc.connect(user='root',database='empdb')
    cur = con.cursor()
    cur.execute('SELECT * FROM emp')
    n = int(input("Enter number of rows to display: "))
    rows = cur.fetchmany(n)
    print("\n--- Employee Table ---\n")
    for col in cur.description:
        print(f"{col[0]:^15}", end='\t')
    for tpl in rows:
        for x in tpl:
            print(f"{str(x):^15}", end='\t')
        print()
    cur.close()
    con.close()
except mc.errors.ProgrammingError as msg:
    print("Programming Error:", msg)
except mc.errors.DatabaseError:
    print("Please start MySQL server")

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
import mysql.connector as mc
try:
    con = mc.connect(user='root',database='empdb')
    cur = con.cursor()
    empno = int(input("Enter employee number: "))
    ename = input("Enter employee name: ")
    sal = float(input("Enter employee salary: "))
    cur.execute(f"INSERT INTO emp VALUES ({empno}, '{ename}', {sal})")
    con.commit()
    print(f"{cur.rowcount} row inserted successfully into emp table.")
    cur.close()
    con.close()
except mc.errors.IntegrityError:
    print("Error: Duplicate empno not allowed.")
except mc.errors.ProgrammingError as msg:
    print("Programming Error:", msg)
except mc.errors.DatabaseError:
    print("Please start MySQL server")

Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition

1) How  to  call  execute()  method ?  --->   cur . execute(F'delete  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the  cond
import mysql.connector as mc
try:
    con = mc.connect(user='root',database='empdb')
    cur = con.cursor()
    cond = input("Enter condition to delete rows (e.g. empno = 101 or sal < 3000): ")
    cur.execute(f"DELETE FROM emp WHERE {cond}")
    con.commit()
    print(f"{cur.rowcount} row(s) deleted successfully.")
    cur.close()
    con.close()
except mc.errors.ProgrammingError as msg:
    print("Programming Error:", msg)
except mc.errors.DatabaseError:
    print("Please start MySQL server")

Write  a  program to  modify  data  of  emp  table

1) How  to  call  execute()  method ?  --->  cur . execute(F'update  emp  set  {expr}   where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  expr  and  cond
'''
import mysql.connector as mc
try:
    con = mc.connect(user='root',database='empdb')
    cur = con.cursor()
    expr = input("Enter modification expression (e.g. sal = sal + 500): ")
    cond = input("Enter condition to modify rows (e.g. empno = 101): ")
    cur.execute(f"UPDATE emp SET {expr} WHERE {cond}")
    con.commit()
    print(f"{cur.rowcount} row(s) updated successfully.")
    cur.close()
    con.close()
except mc.errors.ProgrammingError as msg:
    print("Programming Error:", msg)
except mc.errors.DatabaseError:
    print("Please start MySQL server")

Write  a  program  to  create  student  table

1) How  to  call  execute()  method ?  --->
									cur . execute(F'create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float)')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  table  name

3) What  action  to  be  made  when  table  already  exists ?  --->
																	Delete  the  existing  table  and  create  a  new  table  with  same  name
import mysql.connector as mc
try:
    con = mc.connect(user='root',database='schooldb')
    cur = con.cursor()
    tablename = input("Enter table name to create: ")
    cur.execute(f"DROP TABLE IF EXISTS {tablename}")
    cur.execute(
        f"CREATE TABLE {tablename}("
        f"rollno INT PRIMARY KEY, "
        f"sname CHAR(20), "
        f"marks FLOAT)"
    )
    print(f"Table '{tablename}' created successfully.")
    cur.close()
    con.close()
except mc.errors.ProgrammingError as msg:
    print("Programming Error:", msg)
except mc.errors.DatabaseError:
    print("Please start MySQL server")
