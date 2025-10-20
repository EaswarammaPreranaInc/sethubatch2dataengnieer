'''
Repeat  prog8b(fetchmany)  but  validate  input
i.e. Print  a  msg  when  input > number  of  tuples

Hint:  Use  fetchmany()  method
'''

import mysql.connector
try:
    con = mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur = con.cursor()
    cur.execute("select count(*) from emp")
    total = cur.fetchone()[0]
    n = int(input('Enter number of rows : '))
    if n < 0:
        print('Input should be a positive integer')
    elif n == 0:
        print('Number of tuples :', 0)
    elif n > total:
        print(f'Input exceeds number of tuples ({total})')
    else:
        cur.execute("select * from emp")
        a = cur.fetchmany(n)
        for x in cur.description:
            print(f'{x[0]:^10}', end='\t')
        print()
        for row in a:
            for i in row:
                print(f'{i:^10}', end='\t')
            print()
        print('Number of tuples :', len(a))
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError:
    print("Start MySQL")
except ValueError:
    print("Please enter a valid integer")


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
try:
    con = mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur = con.cursor()
    n = int(input("How many rows do you want to insert ? : "))
    emp_data = []
    for i in range(1,n+1):
        print(f"Employee {i}")
        empno = int(input("Enter employee number :"))
        ename = input("Enter employee name :")
        sal = int(input("Enter salary :"))
        emp_data.append((empno, ename, sal))
    cur.executemany("INSERT INTO emp VALUES (%s, %s, %s)", emp_data)
    con.commit()
    print(f"{cur.rowcount} rows are inserted")
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print("SQL Error:", msg)
except mysql.connector.errors.DatabaseError:
    print("Start mysql")
except ValueError:
    print("Please enter valid input")
'''
o/p:
How many rows do you want to insert ? : 2
Employee 1
Enter employee number :40
Enter employee name :'raj'
Enter salary :34000
Employee 2
Enter employee number :50
Enter employee name :'gita'
Enter salary :56000
2 rows are inserted
'''