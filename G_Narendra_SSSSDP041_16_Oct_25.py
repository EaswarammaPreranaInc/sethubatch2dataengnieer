''' Write a program to display n rows of a table
    hint: use fetchmany() method
'''
import mysql.connector
try:
    
    con = mysql.connector.connect(
        host='localhost',user='root',database='empdb'
    )
    table=input('Enter table name -')
    num=int(input('Enter the number of rows to be displayed ?-'))
    cur = con.cursor()
    while table=='':
        table=input('Enter table name -')
    cur.execute(F'select Count(*) FROM {table}')
    x=cur.fetchone()
    lst=x[0]
    if num<=lst:
        cur.execute(F'select * FROM {table}')
        list=cur.fetchmany(n)
        for col in cur.description:
            print(col[0], end='\t')
        print()
        for tpl in list:
            for i in tpl:
                    print(i, end='\t')
            print()
         
    else:
        print('Invalid input')
    con.close()
except AttributeError:
    print('No of rows should not be negative')
except mysql.connector.ProgrammingError as msg:
    print(msg)

'''
Write  a  program  to  insert  multiple  rows  into  emp  table

1) How  to  insert  multiple  rows  into  the  table ?  --->  With  executemany()  method
@@ -22,5 +58,51 @@ Write  a  program  to  insert  multiple  rows  into  emp  table
    What  is  the  result  of  cur . rowcount ? ---> 4

6) What  are  the  two  arguments  of  executemany()  method  ?  --->
																				sql  command   and   list  of  tuples  where  each  tuple  is  a  row
			sql  command   and   list  of  tuples  where  each  tuple  is  a  row
'''



try:
    import mysql.connector

        
    con = mysql.connector.connect(
            host='localhost',
            user='root',
            database='empdb'
        )

    cur = con.cursor()
    n=int(input())
    i=0
    lst=[]
    while i<n:
            i+=1
            print('Enter details for employee',i,'-')
            empno = int(input('Enter empno: '))
            ename = input('Enter ename: ')
            sal = float(input('Enter salary: '))
            data.append((empno,ename,sal))
    cur.executemany('insert   into  emp  values (%s,%s,%s)' ,  lst)
            
    print(f'{cur.rowcount} rows inserted')
    con.commit()
    con.close()

except mysql.connector.ProgrammingError as msg:
    print("Error:", msg)


