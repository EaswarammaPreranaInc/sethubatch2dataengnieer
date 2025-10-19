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

import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='empdb',user='root',password='')
    cur=con.cursor()
    n=int(input("How many rows do you want to insert : ? "))
    list=[]
    for i in range(1,n+1):
        print("Faculty ",i)
        id=int(input("Enter Faculty Id : "))
        name=input("Enter Faculty Name : ")
        dept=input("Enter Faculty Dept : ")
        list.append((id,name,dept))
    try:
        cur.executemany(f"insert into faculty values(%s,%s,%s)",list)
        con.commit()
        print(f'{cur.rowcount} row is inserted')
    except mysql.connector.errors.IntegrityError:
        print('Duplicate Employee Id and Hence cannot be Inserted')
    cur.close()
    con.close()
except mysql.connector.errors.ProgrammingError as msg:
    print(msg)
except mysql.connector.errors.DatabaseError: 
    print("Start Mysql")