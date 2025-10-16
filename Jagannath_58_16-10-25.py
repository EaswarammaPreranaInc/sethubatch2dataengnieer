Print  a  msg  when  input > number  of  tuples
Hint:  Use  fetchmany()  method
import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Employee"
)
cursor = con.cursor()
cursor.execute("SELECT * FROM employee")
cursor.execute("SELECT * FROM employee")
total_rows = len(cursor.fetchall())
cursor.execute("SELECT * FROM employee")
n = int(input("Enter number of rows to fetch: "))
rows = cursor.fetchmany(n)
for row in rows:
    print(row)
cursor.close()
con.close()

'''
Write  a  program  to  insert  multiple  rows  into  emp  table

1) How  to  insert  multiple  rows  into  the  table ?  --->  With  executemany()  method

2) Where  is  executemany()  method  defined ?  --->  In  MySqlCursor  class  (like  execute()  method)

3) cur . executemany('insert   into  emp  values (%s,%s,%s)' ,  list)
    What  does  the  method  do ?  ---> Inserts  all  the  tuples  of  the  list  into  emp  table

4) What  is  first  %s  for ?  --->  First  element  of  each  tuple  in  the  list
    What  is  2nd  %s  for ?  ---> 2nd  element  of  each  tuple  in  the  list
    What  is  3rd  %s  for ?  ---> 3rd  element  of  each  tuple  in  the  list

5) How  many  rows  are  inserted  if  there  are  four  tuples  in  the  list  ?  ---> 4  rows
    What  is  the  result  of  cur . rowcount ? ---> 4

6) What  are  the  two  arguments  of  executemany()  method  ?  --->
																				sql  command   and   list  of  tuples  where  each  tuple  is  a  row
'''
import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Employee"
)
cur = con.cursor()
data = [
    (101, 'Ravi', 50000),
    (102, 'Sneha', 60000),
    (103, 'Amit', 55000),
    (104, 'John', 65000)
]
sql = "INSERT INTO emp VALUES (%s, %s, %s)"
cur.executemany(sql, data)
con.commit()
print(cur.rowcount, "rows inserted successfully.")
cur.close()
con.close()
