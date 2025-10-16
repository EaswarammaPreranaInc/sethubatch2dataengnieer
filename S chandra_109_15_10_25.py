# 1) Program to print first 'n' rows of emp table
import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='root', database='company')
cur = con.cursor()
n = int(input("Enter number of rows to fetch: "))
cur.execute("SELECT * FROM emp")
rows = cur.fetchmany(n)
for tpl in rows:
    print(tpl)
con.close()


# 2) Program to insert rows into emp table, one at a time
import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='root', database='company')
cur = con.cursor()
while True:
    empno = int(input("Enter employee number: "))
    ename = input("Enter employee name: ")
    sal = float(input("Enter employee salary: "))
    cur.execute("INSERT INTO emp VALUES(%s, %s, %s)", (empno, ename, sal))
    con.commit()
    ch = input("Do you want to insert another record? (y/n): ")
    if ch.lower() != 'y':
        break
con.close()


# 3) Program to delete rows of emp table based on user input condition
import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='root', database='company')
cur = con.cursor()
sal_limit = float(input("Enter salary limit to delete employees below this value: "))
cur.execute("DELETE FROM emp WHERE sal < %s", (sal_limit,))
con.commit()
print(cur.rowcount, "rows deleted successfully")
con.close()


# 4) Program to create student table
import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='root', database='college')
cur = con.cursor()
cur.execute("CREATE TABLE student(rollno INT PRIMARY KEY, name VARCHAR(30), marks FLOAT)")
print("Student table created successfully")
con.close()


# 5) Program to delete existing student table and create a new one with same name
import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='root', database='college')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS student")
cur.execute("CREATE TABLE student(rollno INT PRIMARY KEY, name VARCHAR(30), marks FLOAT)")
print("Old student table deleted and new table created successfully")
con.close()
