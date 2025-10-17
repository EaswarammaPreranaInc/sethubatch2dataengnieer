'''
Repeat  prog8b(fetchmany)  but  validate  input
i.e. Print  a  msg  when  input > number  of  tuples

Hint:  Use  fetchmany() method
'''
import mysql.connector as mc
try:
    con = mc.connect(database = 'empdb', user = 'root')
    cur = con.cursor()
    cur.execute('select * from emp')
    n = int(input("How many rows:"))
    list = cur.fetchmany(n)
    if n > len(list):
        print("Invalid input")
    else:
        for x in cur.description:
            print(F'{x[0]:^10}', end = '\t')
        print()
        for tpl in list:
            for x in tpl:
                print(F'{x:^10}', end = '\t')
            print()
        print("Number of rows:", cur.rowcount)
except mc.errors.ProgrammingError as msg:
    print("Error:", msg)
except mc.errors.DatabaseError:
    print("Pls start MySQL")
'''
How many rows:5
  empno           ename            sal    
    10           Srinivas        10000.0
    20            Jyothi         20000.0
    30            Mahesh         15000.0
    40          Vaishnavi        30000.0
    50            Akhila         50000.0
Number of rows : 5
How many rows:12
Invalid input
'''









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
																				sql  command   and   list  of  tuples  where  each  tuple  is  a  row
'''
import mysql.connector as mc
try:
    con = mc.connect(database = 'empdb', user = 'root')
    cur = con.cursor()
    n = int(input("Enter number of rows:"))
    list = []
    for i in range(n):
        print(F'Employee {i+1}')
        empno = int(input("Enter employee number:"))
        ename = input("Enter employee name:")
        sal = int(input("Enter salary:"))
        list.append((empno, ename, sal))
    cur.executemany('insert into emp values(%s, %s, %s)', list)
    con.commit()
    print(F'{cur.rowcount} rows are insereted')
except mc.errors.ProgrammingError as msg:
    print("Error:", msg)
except mc.errors.DatabaseError:
    print("Pls start MySQL")
'''
Outputs
Enter number of rows:3
Employee 1
Enter employee number:222
Enter employee name:Sreena
Enter salary:50000
Employee 2
Enter employee number:333
Enter employee name:Vaishnavi
Enter salary:24000
Employee 3
Enter employee number:444
Enter employee name:Swetha
Enter salary:60000
3 rows are insereted
'''