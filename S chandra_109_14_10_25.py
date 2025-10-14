 : '''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''
: Emp Number       Emp Name                Salary
10                Rama Rao               10000.0
15                Kiran                  15000.0
20                Sita           20000.0
Number  of  tuples :   3

###########################
import sqlite3

# Step 1: Connect to database (or create one)
con = sqlite3.connect("company.db")

# Step 2: Create cursor object
cur = con.cursor()

# Step 3: Create table (optional — only for demo)
cur.execute("""
CREATE TABLE IF NOT EXISTS emp(
    empno INTEGER PRIMARY KEY,
    ename TEXT,
    sal REAL
)
""")

# Step 4: Insert sample records (optional)
cur.execute("DELETE FROM emp")  # Clear previous data
cur.execute("INSERT INTO emp VALUES(10, 'Rama Rao', 10000.0)")
cur.execute("INSERT INTO emp VALUES(15, 'Kiran', 15000.0)")
cur.execute("INSERT INTO emp VALUES(20, 'Sita', 20000.0)")
con.commit()

# Step 5: Execute SELECT query
cur.execute("SELECT * FROM emp")

# Step 6: Fetch and print records one by one using fetchone()
print("Emp Number\tEmp Name\tSalary")
count = 0
while True:
    tpl = cur.fetchone()   # fetch one record at a time
    if tpl == None:
        break
    print(f"{tpl[0]}\t\t{tpl[1]}\t\t{tpl[2]}")
    count += 1

print("Number of tuples :", count)

# Step 7: Close connection
con.close()
 





: '''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''
: Enter  any  condition : sal > 12000
Emp Number       Emp Name                Salary
  15             Kiran                   15000.0
  20             Sita                    20000.0
Number  of  tuples  :  2
#####################################
import sqlite3

# Step 1: Connect to database
con = sqlite3.connect("company.db")

# Step 2: Create cursor object
cur = con.cursor()

# Step 3: (Optional) Create and fill emp table for demo
cur.execute("""
CREATE TABLE IF NOT EXISTS emp(
    empno INTEGER PRIMARY KEY,
    ename TEXT,
    sal REAL
)
""")

cur.execute("DELETE FROM emp")
cur.execute("INSERT INTO emp VALUES(10, 'Rama Rao', 10000.0)")
cur.execute("INSERT INTO emp VALUES(15, 'Kiran', 15000.0)")
cur.execute("INSERT INTO emp VALUES(20, 'Sita', 20000.0)")
con.commit()

# Step 4: Read condition from the user
cond = input("Enter any condition : ")   # Example: sal > 12000

# Step 5: Execute query using f-string
cur.execute(f"SELECT * FROM emp WHERE {cond}")

# Step 6: Fetch and display tuples one by one
print("Emp Number\tEmp Name\tSalary")
count = 0
while True:
    tpl = cur.fetchone()
    if tpl is None:
        break
    print(f"{tpl[0]}\t\t{tpl[1]}\t\t{tpl[2]}")
    count += 1

print("Number of tuples :", count)

# Step 7: Close connection
con.close()




: '''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''
: Enter column name: sal desc
Emp Number       Emp Name                Salary
  20             Sita                    20000.0
  15             Kiran                   15000.0
  10             Rama Rao                10000.0
Num  of rows :  3

################################

import sqlite3

# Step 1: Connect to database
con = sqlite3.connect("company.db")

# Step 2: Create cursor object
cur = con.cursor()

# Step 3: (Optional) Create and fill emp table for demo
cur.execute("""
CREATE TABLE IF NOT EXISTS emp(
    empno INTEGER PRIMARY KEY,
    ename TEXT,
    sal REAL
)
""")

cur.execute("DELETE FROM emp")
cur.execute("INSERT INTO emp VALUES(10, 'Rama Rao', 10000.0)")
cur.execute("INSERT INTO emp VALUES(15, 'Kiran', 15000.0)")
cur.execute("INSERT INTO emp VALUES(20, 'Sita', 20000.0)")
con.commit()

# Step 4: Read column name from user
colname = input("Enter column name: ")     # Example: sal desc  OR  ename

# Step 5: Execute SELECT query with ORDER BY
cur.execute(f"SELECT * FROM emp ORDER BY {colname}")

# Step 6: Fetch and display each row using fetchone()
print("Emp Number\tEmp Name\tSalary")
count = 0
while True:
    tpl = cur.fetchone()
    if tpl is None:
        break
    print(f"{tpl[0]}\t\t{tpl[1]}\t\t{tpl[2]}")
    count += 1

print("Num of rows :", count)

# Step 7: Close connection
con.close()




: '''
Write  a  program  to  print  user  input  table  with  next()  function

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  {table}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the   table  name

3) What  does  next(cur)  do ?  --->  Yields  the  next  tuple  of  cursor  object

4) What  does   next()  function  do  when  end  of   the  cursor  is  reached ?  ---> Throws StopIteration  error

5) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                          execute()                                   next()                  print()
'''
: Enter   table  name :  emp
Emp  Number      Emp  Name       Salary
  10             Rama Rao        10000.00
  15             Kiran           15000.00
  20             Sita            20000.00
Number  of  tuples :   3
: Enter   table  name :  stud
1146 (42S02): Table 'empdb.stud' doesn't exist

################

import sqlite3

# Step 1: Connect to database
con = sqlite3.connect("company.db")

# Step 2: Create cursor object
cur = con.cursor()

# Step 3: Create emp table (optional demo data)
cur.execute("""
CREATE TABLE IF NOT EXISTS emp(
    empno INTEGER PRIMARY KEY,
    ename TEXT,
    sal REAL
)
""")
cur.execute("DELETE FROM emp")
cur.execute("INSERT INTO emp VALUES(10, 'Rama Rao', 10000.0)")
cur.execute("INSERT INTO emp VALUES(15, 'Kiran', 15000.0)")
cur.execute("INSERT INTO emp VALUES(20, 'Sita', 20000.0)")
con.commit()

# Step 4: Read table name from user
table = input("Enter table name: ")   # Example: emp

try:
    # Step 5: Execute SELECT query
    cur.execute(f"SELECT * FROM {table}")

    # Step 6: Fetch and print tuples using next()
    print("Emp Number\tEmp Name\tSalary")
    count = 0
    while True:
        try:
            tpl = next(cur)   # get next record
            print(f"{tpl[0]}\t\t{tpl[1]}\t\t{tpl[2]:.2f}")
            count += 1
        except StopIteration:
            break

    print("Number of tuples :", count)

except Exception as e:
    print(e)

# Step 7: Close connection
con.close()







: '''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
''
: Emp Number       Emp Name        Salary
  10             Rama Rao          10000.00
  15             Kiran             15000.00
  20             Sita              20000.00
Number  of  tuples  :  3

###########################

import sqlite3

# Step 1: Connect to the database
con = sqlite3.connect("company.db")

# Step 2: Create cursor object
cur = con.cursor()

# Step 3: (Optional) Create emp table and insert demo records
cur.execute("""
CREATE TABLE IF NOT EXISTS emp(
    empno INTEGER PRIMARY KEY,
    ename TEXT,
    sal REAL
)
""")

cur.execute("DELETE FROM emp")
cur.execute("INSERT INTO emp VALUES(10, 'Rama Rao', 10000.0)")
cur.execute("INSERT INTO emp VALUES(15, 'Kiran', 15000.0)")
cur.execute("INSERT INTO emp VALUES(20, 'Sita', 20000.0)")
con.commit()

# Step 4: Execute SQL query
cur.execute("SELECT * FROM emp")

# Step 5: Fetch all tuples into a list
records = cur.fetchall()

# Step 6: Display data
print("Emp Number\tEmp Name\tSalary")
for tpl in records:
    print(f"{tpl[0]}\t\t{tpl[1]}\t\t{tpl[2]:.2f}")

print("Number of tuples :", len(records))

# Step 7: Close connection
con.close()
