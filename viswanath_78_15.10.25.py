Q) Write  a  program  to  print  first  'n'  rows  of  emp  table
 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
Ans) import mysql.connector as mc
try:
    con = mc.connect( user='root',  database=’empdb')
    cur = con.cursor()
    n = int(input("Enter number of rows to display: "))
    cur.execute("SELECT * FROM emp")
    for x in cur.description:
        print(F’{x[0]:^10}’,end =’\t’) 
    print()
    lst = cur.fetchmany(n)
    for tpl in lst:
        print(F’{x:^10}’,end =’\t’)
    print("No of uples fetched : ",cur.rowcount)  
   con.cur() 
   con.close()
except mc.errors.InternalError as msg:
    print("cursor cannot be clsoed")
except mc.errors.ProgmmingError as msg:
    print("msg")
except mc.errors.DatabaseError as msg:
    print("pls start MySQL")
except mc.errors.AttributeError as msg:
    print("Input must be +ve value")

Q) Write  a  program  to  insert  rows  into  emp  table ,  one  at  a  time
Ans) import mysql.connector
try:
    con = mysql.connector.connect(user='root', database='empdb')
    cur = con.cursor()
    empno = int(input("Enter employee number: "))  # read empno
    ename = input("Enter employee name: ")         # read ename
    sal = float(input("Enter salary: "))           # read salary
    try:
         cur.execute(f"INSERT INTO emp VALUES ({empno}, '{ename}', {sal})")  # insert one row
         con.commit()  # make insertion permanent
         print(f"{cur.rowcount} row inserted successfully")  
    except mysql.connector.IntegrityError:
         print("Error: Duplicate empno not allowed")  # Error: same empno already exists
ch = input("Insert another row (y or n) : ")
if ch == "N" or ch == "n":
      break
except mysql.connector.ProgrammingError as pe:
    print("Child Error:", pe)  # Error: wrong SQL syntax or invalid operation
except mysql.connector.Error as e:
    print("Parent Error:", e)  # Error: general database issue
            
Q)  Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition
Ans) import mysql.connector
try:
    con = mysql.connector.connect(user='root', database='empdb')
    cur = con.cursor()
    cond = input("Enter condition for deletion ")  # read cond
    cur.execute(f"DELETE FROM emp WHERE {cond}")  # delete based on condition
    con.commit()  # make deletion permanent
    print(f"{cur.rowcount} row(s) deleted successfully")  # prints how many rows deleted
    cur.close()  # close cursor
    con.close()  # close connection
except mysql.connector.ProgrammingError as pe:
    print("Child Error:", pe)  
except mysql.connector.DatabaseError :
    print("Pls start MySQL")  # Error: general DB issue
        
Q) Write  a  program to  modify  data  of  emp  table
Ans) import mysql.connector
try:
    con = mysql.connector.connect(user='root', database='company')
    cur = con.cursor()
    expr = input("Enter expression to modify (e.g., sal=sal+1000): ")  # read expr
    cond = input("Enter condition (e.g., deptno=10 or empno=105): ")   # read cond
    cur.execute(f"UPDATE emp SET {expr} WHERE {cond}")  # update based on expr & cond
    con.commit()  # make modification permanent
    print(f"{cur.rowcount} row(s) updated successfully")  # prints how many rows modified
    cur.close()  # close cursor
    con.close()  # close connection
except mysql.connector.ProgrammingError as pe:
    print("Child Error:", pe)  # Error: invalid SQL or wrong column
except mysql.connector.Error as e:
    print("Parent Error:", e)  # Error: general DB issue

Q) Write  a  program  to  create  student  table
Ans) import mysql.connector
try:
    con = mysql.connector.connect(user='root', database='empdb')
    cur = con.cursor()
    tablename = input("Enter table name: ")  # read table name
    try:
        cur.execute(f"CREATE TABLE {tablename}(rollno INT PRIMARY KEY, sname CHAR(20), marks FLOAT)")  # create table
        print(f"Table '{tablename}' created successfully")  # prints success message
        cur.close()  # close cursor
       con.close()  # close connection
    except mysql.connector.ProgrammingError as pe:
        print("Child Error:", pe)  # Error: SQL syntax issue
    except mysql.connector.Error as e:
        if e.errno == 1050:  # 1050 -> Table already exists
            print(f"Table '{tablename}' already exists... recreating")  # info message
            cur.execute(f"DROP TABLE {tablename}")  # delete old table
            cur.execute(f"CREATE TABLE {tablename}(rollno INT PRIMARY KEY, sname CHAR(20), marks FLOAT)")  # recreate
            print(f"Table '{tablename}' recreated successfully")  # prints recreate message
        else:
            print("Parent Error:", e)  
except mysql.connector.Error as e:
    print("Connection Error:", e)  
