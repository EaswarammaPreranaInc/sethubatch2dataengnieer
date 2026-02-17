'''
Repeat  prog8b(fetchmany)  but  validate  input
i.e. Print  a  msg  when  input > number  of  tuples

Hint:  Use  fetchmany()  method
'''
try:
    import mysql.connector as mc
    con = mc.connect(database='empdb', user='root')
    table = input('Enter table name - ')
    while table == '':
        table = input('Enter table name - ')
    n = int(input('Enter the number of rows to be displayed ? - '))
    cur = con.cursor()
    cur.execute(f'SELECT COUNT(*) FROM {table}')
    x = cur.fetchone()
    total = x[0]
    if 0 < n <= total:
        cur.execute(f'SELECT * FROM {table}')
        rows = cur.fetchmany(n)
        for col in cur.description:
            print(col[0], end='\t')
        print()
        for tpl in rows:
            for val in tpl:
                print(val, end='\t')
            print()
    elif n <= 0:
        print('Input should be a positive number')
    else:
        print('Invalid input: exceeds number of tuples')
    con.close()
except AttributeError:
    print('No of rows should not be negative')
except mc.ProgrammingError as msg:
    print(msg)


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

6) What  are  the  two  arguments  of  executemany()  method  ?  ---> sql  command   and   list  of  tuples  where  each  tuple  is  a  row
'''

try:
    import mysql.connector as mc
    con = mc.connect( database='empdb', user='root')
    cur = con.cursor()
    n = int(input('Enter number of employees to insert: '))
    a = []
    for i in range(n):
        print(f'Enter details for employee {i + 1} -')
        empno = int(input('Enter empno: '))
        ename = input('Enter ename: ').strip()
        sal = float(input('Enter salary: '))
        a.append((empno, ename, sal))
    cur.executemany('INSERT INTO emp VALUES (%s, %s, %s)', a)
    print(f'{cur.rowcount} rows inserted')
    con.commit()
    con.close()
except mc.IntegrityError:
    print('Duplicate empno found. Some rows not inserted.')
except mc.ProgrammingError as msg:
    print('SQL Error:', msg)
