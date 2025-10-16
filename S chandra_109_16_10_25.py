# Repeat prog8b(fetchmany) but validate input
# Print message when input > number of tuples

import sqlite3

con = sqlite3.connect("employee.db")
cur = con.cursor()
cur.execute("SELECT * FROM emp")

rows = cur.fetchall()
total = len(rows)
print("Total tuples available :", total)

n = int(input("Enter number of rows to fetch : "))

if n > total:
    print("Input exceeds total number of tuples. Please enter a value ≤", total)
else:
    cur.execute("SELECT * FROM emp")
    tpl = cur.fetchmany(n)
    for rec in tpl:
        print(rec)

con.close()


# Write a program to insert multiple rows into emp table

import sqlite3

con = sqlite3.connect("employee.db")
cur = con.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS emp (
    empno INTEGER,
    ename TEXT,
    sal REAL
)
""")

rows = [
    (101, 'Rama', 25000),
    (102, 'Sita', 30000),
    (103, 'Krishna', 40000),
    (104, 'Radha', 35000)
]

cur.executemany("INSERT INTO emp VALUES (?, ?, ?)", rows)
con.commit()
print("Multiple rows inserted successfully.")

con.close()
