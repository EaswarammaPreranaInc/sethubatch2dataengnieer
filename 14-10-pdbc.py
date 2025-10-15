"""
===============================================================
PROGRAM 1: PRINT EMP TABLE USING fetchone()
===============================================================

QUESTION:
Write a program to print emp table of the database with fetchone() method.

FLOW:
emp table ----------------> cursor object -----------------> tpl ---------> monitor
             execute()                               fetchone()             print()
"""

import mysql.connector

con = mysql.connector.connect(
    database='empdb'
)
cur = con.cursor()

cur.execute("select * from emp")
print("Emp Number\tEmp Name\t\tSalary")

count = 0
tpl = cur.fetchone()
while tpl is not None:
    print(tpl[0], "\t", tpl[1], "\t\t", tpl[2])
    tpl = cur.fetchone()
    count += 1
print("Number of tuples :", count)

cur.close()
con.close()



"""
===============================================================
PROGRAM 2: PRINT EMP TABLE BASED ON USER CONDITION
===============================================================

QUESTION:
Write a program to print emp table based on user condition.

1) How to call execute() method?
   ---> cur.execute('select * from emp where ' + cond)

2) What is the pre-requisite to call execute() method?
   ---> Read the condition from the user

FLOW:
emp table ----------------> cursor object -----------------> tpl ---------> monitor
             execute()                               fetchone()             print()
"""

import mysql.connector

con = mysql.connector.connect(
    database='empdb'
)
cur = con.cursor()

cond = input("Enter any condition : ")
query = "select * from emp where " + cond
cur.execute(query)

print("Emp Number\tEmp Name\t\tSalary")

count = 0
tpl = cur.fetchone()
while tpl is not None:
    print(tpl[0], "\t", tpl[1], "\t\t", tpl[2])
    tpl = cur.fetchone()
    count += 1

print("Number of tuples :", count)

cur.close()
con.close()



"""
===============================================================
PROGRAM 3: PRINT EMP TABLE IN SORTED ORDER
===============================================================

QUESTION:
Write a program to print emp table in sorted order.

1) How to call execute() method?
   ---> cur.execute('select * from emp order by ' + colname)

2) What is the pre-requisite to call execute() method?
   ---> Read the column name

FLOW:
emp table ----------------> cursor object -----------------> tpl ---------> monitor
             execute()                               fetchone()             print()
"""

import mysql.connector

con = mysql.connector.connect(
    database='empdb'
)
cur = con.cursor()

colname = input("Enter column name (e.g. sal desc): ")
query = "select * from emp order by " + colname
cur.execute(query)

print("Emp Number\tEmp Name\t\tSalary")

count = 0
tpl = cur.fetchone()
while tpl is not None:
    print(tpl[0], "\t", tpl[1], "\t\t", tpl[2])
    tpl = cur.fetchone()
    count += 1

print("Num of rows :", count)

cur.close()
con.close()



"""
===============================================================
PROGRAM 4: PRINT USER INPUT TABLE USING next() FUNCTION
===============================================================

QUESTION:
Write a program to print user input table with next() function.

1) How to call execute() method?
   ---> cur.execute('select * from ' + table)

2) What is the pre-requisite to call execute() method?
   ---> Read the table name

3) What does next(cur) do?
   ---> Yields the next tuple of cursor object

4) What does next() function do when end of cursor is reached?
   ---> Throws StopIteration error

FLOW:
emp table ----------------> cursor object -----------------> tpl ---------> monitor
             execute()                                  next()             print()
"""

import mysql.connector

con = mysql.connector.connect(
    database='empdb'
)
cur = con.cursor()

table = input("Enter table name: ")
try:
    query = "select * from " + table
    cur.execute(query)
    print("Emp Number\tEmp Name\t\tSalary")

    count = 0
    try:
        while True:
            tpl = next(cur)
            print(tpl[0], "\t", tpl[1], "\t\t", tpl[2])
            count += 1
    except StopIteration:
        pass
    print("Number of tuples :", count)
except mysql.connector.Error as err:
    print(err)

cur.close()
con.close()



"""
===============================================================
PROGRAM 5: PRINT CURSOR USING fetchall()
===============================================================

QUESTION:
Write a program to print cursor with fetchall() method.

FLOW:
emp table ---------------> cur object ---------------> list -------------> tpl ------------> monitor
          execute()                            fetchall()                for loop              print()
"""

import mysql.connector

con = mysql.connector.connect(
    database='empdb'
)
cur = con.cursor()

cur.execute("select * from emp")
records = cur.fetchall()

print("Emp Number\tEmp Name\t\tSalary")

count = 0
for tpl in records:
    print(tpl[0], "\t", tpl[1], "\t\t", tpl[2])
    count += 1

print("Number of tuples :", count)

cur.close()
con.close()
