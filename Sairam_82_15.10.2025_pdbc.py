'''
Write  a  program  to  print  first  'n'  rows  of  emp  table

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
'''

try:
    import mysql.connector
    con = mysql.connector.connect(
        host='localhost',user='root',password='12345678',database='empdb'
    )
    table=input('Enter table name -')
    n=int(input('Enter the number of rows to be displayed ?-'))
    cur = con.cursor()
    while table=='':
        table=input('Enter table name -')
    cur.execute(F'select * FROM {table}')
    list=cur.fetchmany(n)
    for col in cur.description:
        print(col[0], end='\t')
    print()
    for tpl in list:
        for i in tpl:
                print(i, end='\t')
        print()

    print('no of tuples fetched :',cur.rowcount) 
    con.close()
except AttributeError:
    print('No of rows should not be negative')
except mysql.connector.ProgrammingError as msg:
    print(msg)

'''
Write  a  program  to  insert  rows  into  emp  table ,  one  at  a  time

1) How  to  call  execute()  method ?  --->
															cur . execute(F"insert  into  emp  values  ({empno} ,  '{ename}' , {sal})")

2) Are  quotes  mandatory  for  ename ? --->  Yes  becoz  it  is  a  string

3) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  inputs  empno , ename  and  sal

4) What  action  to  be  made  after  insert ?  --->  Call  commit()  method

5) What  does  commit()  method  do ?  --->  Makes  insertion  becomes  permanent

6) What  happens  when  commit()  is  not  called ?  --->  Insertion  is  only  temporary

7) In  other  words,  insertion  does  not  happen

8) Where  is  commit()  method  defined ?  ---> In  MySqlConnection  class

9) cur . execute(F'insert  into  emp  values (25 , "Rama  Rao" , 10000.0)')
    What  is  the  result  of  cur . rowcount ?  ---> 1  becoz  only  one  row  is  inserted  into  emp  table

10) Can  a  tuple  be  inserted  into  cur  object ?  --->  No  becoz  it  is  immutable

11) What  happens  when  we  try  to  insert  duplicate  empno ?  --->  Raises  mc . errors . IntegrityError
'''

try:
    import mysql.connector

    # Connect to MySQL
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678',
        database='empdb'
    )

    cur = con.cursor()

    empno = int(input('Enter empno: '))
    ename = input('Enter ename: ').strip()
    sal = float(input('Enter salary: '))

    query = f"INSERT INTO emp VALUES ({empno}, '{ename}', {sal})"
    cur.execute(query)
    con.commit()

    print('Number of tuples inserted:', cur.rowcount)

    con.close()

except mysql.connector.ProgrammingError as msg:
    print("SQL Error:", msg)


'''
Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition

1) How  to  call  execute()  method ?  --->   cur . execute(F'delete  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the  cond
'''

try:
    import mysql.connector

    # Connect to MySQL
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678',
        database='empdb'
    )

    cur = con.cursor()
    cond=input('enter the condition to delete the rows -')
    cur.execute(f"delete from emp where {cond}")
    con.commit()

    print('Number of tuples deleted:', cur.rowcount)
    con.close()
except mysql.connector.ProgrammingError as msg:
    print("SQL Error:", msg)


'''
Write  a  program to  modify  data  of  emp  table

1) How  to  call  execute()  method ?  --->  cur . execute(F'update  emp  set  {expr}   where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  expr  and  cond
'''

try:
    import mysql.connector

    # Connect to MySQL
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678',
        database='empdb'
    )

    cur = con.cursor()
    expr=input('enter the expression to modify the rows -')
    cond=input('enter the condition to delete the rows -')
    cur.execute(f"update emp set {expr} where {cond}")
    con.commit()
    print('Number of tuples modified:', cur.rowcount)
    con.close()
except mysql.connector.ProgrammingError as msg:
    print("SQL Error:", msg)


'''
Write  a  program  to  create  student  table

1) How  to  call  execute()  method ?  --->
									cur . execute(F'create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float)')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  table  name

3) What  action  to  be  made  when  table  already  exists ?  --->
																	Delete  the  existing  table  and  create  a  new  table  with  same  name
'''
try:
    import mysql.connector

    # Connect to MySQL
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678',
        database='empdb'
    )

    cur = con.cursor()
    table=input('enter the table name')
    column=input('enter the columns and data type -')
    cur.execute(f"create table {table} ({column})")
    con.commit()

    con.close()
except mysql.connector.ProgrammingError as msg:
    print("SQL Error:", msg)


