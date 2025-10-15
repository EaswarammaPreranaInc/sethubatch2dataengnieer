"""
===============================================================
PROGRAM: PRINT FIRST 'n' ROWS OF EMP TABLE
===============================================================

QUESTION:
Write a program to print first 'n' rows of emp table.

FLOW:
emp table ---------------> cur object ---------------> list -------------> tpl ------------> monitor
          execute()                           fetchmany(n)              for loop              print()
"""

import mysql.connector

con = mysql.connector.connect(database='empdb')
cur = con.cursor()

n = int(input("Enter number of rows to display: "))
cur.execute("select * from emp")
records = cur.fetchmany(n)
print("Emp Number\tEmp Name\t\tSalary")
count = 0
for tpl in records:
    print(tpl[0], "\t", tpl[1], "\t\t", tpl[2])
    count += 1
print("Number of tuples displayed :", count)
cur.close()
con.close()

"""
======================================================================
PROGRAM: INSERT ROWS INTO EMP TABLE, ONE AT A TIME
======================================================================

QUESTION:
Write a program to insert rows into emp table, one at a time.

1) How to call execute() method ?
   ---> cur.execute("insert into emp values (" + str(empno) + ", '" + ename + "', " + str(sal) + ")")

2) Are quotes mandatory for ename ?
   ---> Yes, because it is a string.

3) What is the pre-requisite to call execute() method ?
   ---> Read inputs empno, ename, and sal.

4) What action to be made after insert ?
   ---> Call commit() method.

5) What does commit() method do ?
   ---> Makes insertion permanent.

6) What happens when commit() is not called ?
   ---> Insertion is only temporary.

7) In other words, insertion does not happen.

8) Where is commit() method defined ?
   ---> In MySqlConnection class.

9) Example:
   cur.execute('insert into emp values (25, "Rama Rao", 10000.0)')
   Result of cur.rowcount ---> 1 (because one row is inserted)

10) Can a tuple be inserted into cur object ?
    ---> No, because it is immutable.

11) What happens when we try to insert duplicate empno ?
    ---> Raises mysql.connector.errors.IntegrityError
"""

import mysql.connector

con = mysql.connector.connect(database='empdb')
cur = con.cursor()

while True:
    empno = int(input("Enter Emp Number: "))
    ename = input("Enter Emp Name: ")
    sal = float(input("Enter Salary: "))
    query = "insert into emp values(" + str(empno) + ", '" + ename + "', " + str(sal) + ")"
    try:
        cur.execute(query)
        con.commit()
        print("Record inserted successfully. Rows affected:", cur.rowcount)
    except mysql.connector.IntegrityError:
        print("Error: Duplicate empno, record not inserted.")
    except mysql.connector.Error as err:
        print("Error:", err)
    ans = input("Do you want to insert another record? (yes/no): ")
    if ans.lower() != "yes":
        break
cur.close()
con.close()




"""
======================================================================
PROGRAM: DELETE ROWS FROM EMP TABLE BASED ON USER INPUT CONDITION
======================================================================

QUESTION:
Write a program to delete rows of emp table based on user input condition.

1) How to call execute() method ?
   ---> cur.execute("delete from emp where " + cond)

2) What is the pre-requisite to call execute() method ?
   ---> Read the condition (cond) from the user.

FLOW:
emp table ----------------> cursor object -----------------> execute() ----------> commit()
             input(cond)                         delete query                        permanent
"""

import mysql.connector

con = mysql.connector.connect(database='empdb')
cur = con.cursor()

cond = input("Enter delete condition (e.g. sal < 15000): ")
query = "delete from emp where " + cond
try:
    cur.execute(query)
    con.commit()
    print("Rows deleted:", cur.rowcount)
except mysql.connector.Error as err:
    print("Error:", err)
cur.close()
con.close()


"""
======================================================================
PROGRAM: MODIFY DATA OF EMP TABLE
======================================================================

QUESTION:
Write a program to modify data of emp table.

1) How to call execute() method ?
   ---> cur.execute("update emp set " + expr + " where " + cond)

2) What is the pre-requisite to call execute() method ?
   ---> Read expr and cond from the user.

FLOW:
emp table ----------------> cursor object -----------------> execute() ----------> commit()
             input(expr,cond)                     update query                      permanent
"""

import mysql.connector

con = mysql.connector.connect(database='empdb')
cur = con.cursor()

expr = input("Enter update expression (e.g. sal = sal + 1000): ")
cond = input("Enter condition (e.g. empno = 101): ")
query = "update emp set " + expr + " where " + cond
try:
    cur.execute(query)
    con.commit()
    print("Rows updated:", cur.rowcount)
except mysql.connector.Error as err:
    print("Error:", err)
cur.close()
con.close()



"""
======================================================================
PROGRAM: CREATE STUDENT TABLE
======================================================================

QUESTION:
Write a program to create student table.

1) How to call execute() method ?
   ---> cur.execute("create table " + tablename + "(rollno int primary key, sname char(20), marks float)")

2) What is the pre-requisite to call execute() method ?
   ---> Read the table name from the user.

3) What action to be made when table already exists ?
   ---> Delete the existing table and create a new table with the same name.

FLOW:
user input ----------------> cursor -----------------> execute() -----------------> commit()
 table name                   create query              table creation               saved
"""

import mysql.connector

con = mysql.connector.connect(database='empdb')
cur = con.cursor()

tablename = input("Enter new table name: ")
try:
    cur.execute("drop table if exists " + tablename)
    query = "create table " + tablename + "(rollno int primary key, sname char(20), marks float)"
    cur.execute(query)
    con.commit()
    print("Table '" + tablename + "' created successfully!")
except mysql.connector.Error as err:
    print("Error:", err)
cur.close()
con.close()

