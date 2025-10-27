
# 1. Print First 'n' Rows of emp Table ('fetchmany(n)')

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="empdb"
)
cur = con.cursor()
n = int(input("How many rows ? : "))
cur.execute("select * from emp")
rows = cur.fetchmany(n)

print("empno     ename           sal")
for tpl in rows:
    print(f"{tpl[0]:<10}{tpl[1]:<15}{tpl[2]:<10}")

print("Number of tuples fetched :", len(rows))
'''

Sample Output (with n=2):

How many rows ? : 2
empno     ename           sal
10        Rama Rao        10000.0
15        Kiran           15000.0
Number of tuples fetched : 2
'''





# 2. Insert Rows into emp Table One at a Time

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="empdb"
)
cur = con.cursor()

while True:
    empno = int(input("Enter empno :"))
    ename = input("Enter emp name :")
    sal = float(input("Enter salary :"))
    cur.execute(f"insert into emp values({empno}, '{ename}', {sal})")
    con.commit()
    print("1 Row is inserted")
    option = input("Do you wish to insert another row ? (Y / N): ")
    if option.lower() != 'y':
        break
'''

Sample Output:
Enter empno :111
Enter emp name :AAA
Enter salary :10000.0
1 Row is inserted
Do you wish to insert another row ? (Y / N): y
...
Do you wish to insert another row ? (Y / N): n
'''





# 3. Delete Rows from emp Table Based on User Condition

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="empdb"
)
cur = con.cursor()

cond = input("Enter condition : ")
query = f"delete from emp where {cond}"
cur.execute(query)
con.commit()
print(f"{cur.rowcount} Rows deleted")
'''

Sample Output:
Enter condition : sal > 12000
4 Rows deleted
Press any key to continue . . .
'''




# 4. Modify Data of emp Table (Update Rows)

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="empdb"
)
cur = con.cursor()

cond = input("Enter condition : ")
expr = input("Enter column name = value : ")
query = f"update emp set {expr} where {cond}"
cur.execute(query)
con.commit()
print(f"{cur.rowcount} Rows updated")
'''

Sample Output:
Enter condition : empno = 10
Enter column name = value : sal = sal + 1000
1 Rows updated
Press any key to continue . . .
'''




# 5. Create student Table (with Drop If Exists)

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="empdb"
)
cur = con.cursor()

tablename = input("Enter table name:")
try:
    cur.execute(f"drop table if exists {tablename}")
    print(f"Existing {tablename} table is deleted")
except:
    pass
cur.execute(f"create table {tablename} (rollno int primary key, sname char(20), marks float)")
print(f"{tablename} table created")
'''

Sample Output:
Enter table name:student
Existing student table is deleted
New student table created
Press any key to continue . . .

or if table didn't exist previously:

Enter table name:student
student table created
Press any key to continue . . .
'''
