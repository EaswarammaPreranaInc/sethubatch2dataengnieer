# 1. Program to print `emp` table using 'fetchone()'
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="empdb"
)
cur = con.cursor()
cur.execute("select * from emp")

print("Emp Number       Emp Name                Salary")

count = 0
tpl = cur.fetchone()
while tpl is not None:
    print(f"{tpl[0]:<15}{tpl[1]:<20}{tpl[2]:<10.2f}")
    count += 1
    tpl = cur.fetchone()

print("Number of tuples :", count)
'''
Output:
Emp Number       Emp Name                Salary
10               Rama Rao               10000.00
15               Kiran                  15000.00
20               Sita                   20000.00
Number of tuples : 3
'''






# 2. Program to print `emp` table based on user condition

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="empdb"
)
cur = con.cursor()
cond = input("Enter any condition : ")
cur.execute(f"select * from emp where {cond}")

print("Emp Number       Emp Name                Salary")

count = 0
tpl = cur.fetchone()
while tpl is not None:
    print(f"{tpl[0]:<15}{tpl[1]:<20}{tpl[2]:<10.2f}")
    count += 1
    tpl = cur.fetchone()

print("Number of tuples :", count)
'''

Sample Input:
Enter any condition : sal > 12000

Output:
Emp Number       Emp Name                Salary
15               Kiran                  15000.00
20               Sita                   20000.00
Number of tuples : 2
'''





# 3. Program to print `emp` table in sorted order

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="empdb"
)
cur = con.cursor()
colname = input("Enter column name : ")
cur.execute(f"select * from emp order by {colname}")

print("Emp Number       Emp Name                Salary")

count = 0
tpl = cur.fetchone()
while tpl:
    print(f"{tpl[0]:<15}{tpl[1]:<20}{tpl[2]:<10.2f}")
    count += 1
    tpl = cur.fetchone()

print("Num of rows :", count)
'''

Sample Input:
Enter column name : sal desc

Output:
Emp Number       Emp Name                Salary
20               Sita                   20000.00
15               Kiran                  15000.00
10               Rama Rao               10000.00
Num of rows : 3
'''







# 4. Program to print user-input table using 'next()' function

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="empdb"
)
cur = con.cursor()
table = input("Enter table name : ")

try:
    cur.execute(f"select * from {table}")
    print("Emp Number   Emp Name       Salary")

    count = 0
    while True:
        tpl = next(cur)
        print(f"{tpl[0]:<15}{tpl[1]:<20}{tpl[2]:<10.2f}")
        count += 1
except StopIteration:
    print("Number of tuples :", count)
except mysql.connector.Error as err:
    print(err)
'''

Input:
Enter table name : emp

Output:
Emp Number       Emp Name                Salary
10               Rama Rao               10000.00
15               Kiran                  15000.00
20               Sita                   20000.00
Number of tuples : 3


Input:
Enter table name : stud

Output:
1146 (42S02): Table 'empdb.stud' doesn't exist
'''





# 5. Program to print cursor with `fetchall()` method

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="empdb"
)
cur = con.cursor()
cur.execute("select * from emp")
rows = cur.fetchall()

print("Emp Number    Emp Name        Salary")

for tpl in rows:
    print(f"{tpl[0]:<15}{tpl[1]:<20}{tpl[2]:<10.2f}")

print("Number of tuples :", len(rows))
'''

Output:
Emp Number       Emp Name                Salary
10               Rama Rao               10000.00
15               Kiran                  15000.00
20               Sita                   20000.00
Number of tuples : 3
'''
