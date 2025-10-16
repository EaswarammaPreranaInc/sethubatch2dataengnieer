# 1. Print First 'n' Rows of emp Table with Input Validation ('fetchmany()')

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="empdb"
)
cur = con.cursor()
cur.execute("select * from emp")
all_rows = cur.fetchall()
total = len(all_rows)

n = int(input("How many rows ? : "))
if n > total or n < 0:
    print("Invalid input")
else:
    print("empno     ename           sal")
    for tpl in all_rows[:n]:
        print(f"{tpl[0]:<10}{tpl[1]:<15}{tpl[2]:<10}")
    print("Number of rows :", n)
'''

Sample Output:
How many rows ? : 3
empno     ename           sal
111       Rama Rao        10000.0
222       Sita            20000.0
333       Rajesh          15000.0
Number of rows : 3
'''





# 2. Insert Multiple Rows into emp Table using 'executemany()'

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="empdb"
)
cur = con.cursor()

n = int(input("How many rows do you want to insert ? : "))
rows = []
for i in range(n):
    print(f"Employee {i+1}")
    empno = int(input("Enter employee number :"))
    ename = input("Enter employee name :")
    sal = float(input("Enter salary :"))
    rows.append((empno, ename, sal))

cur.executemany('insert into emp values (%s,%s,%s)', rows)
con.commit()
print(f"{cur.rowcount} rows are inserted")
'''

Sample Output:
How many rows do you want to insert ? : 3
Employee 1
Enter employee number :10
Enter employee name :AAA
Enter salary :10000
Employee 2
Enter employee number :20
Enter employee name :BBB
Enter salary :20000
Employee 3
Enter employee number :30
Enter employee name :CCC
Enter salary :30000
3 rows are inserted
'''



