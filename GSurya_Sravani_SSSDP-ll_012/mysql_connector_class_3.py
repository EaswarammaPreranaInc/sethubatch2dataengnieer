'''
Repeat  prog8b(fetchmany)  but  validate  input
i.e. Print  a  msg  when  input > number  of  tuples

Hint:  Use  fetchmany()  method
'''
import mysql.connector
try:
  con=mysql.connector.connect(host="localhost", user="root",database="moviesdb",password="root")
  cur=con.cursor()
  table=input("enter table name : ")
  cur.execute(f'select movie_id,title,release_year  from {table};')
  for i in cur.description:
    print(f"{i[0]:^40}",end=" ")
  print()
  n=int(input("enter how many rows? : "))
  if n>len(table):
       print(f" ivalid number of rows ")
  else:
      list=cur.fetchmany(n)
      for col in list:
         for val in col:
           print(f"{val:^40}",end=' ')
         print()
      print(cur.rowcount)
except mysql.connector.Error as err:
    print("Database error:", err)



enter how many rows? : 50
 ivalid number of rows


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
  con=mysql.connector.connect(host="localhost", user="root",database="moviesdb",password="root")
  cur=con.cursor()
  list=[]
  while True:
     table=input("enter table name : ")
     actor_id=input("enter actor_id: ")
     name=input("enter name: ")
     birth_year=input("enter birth year : ")
     list.append((actor_id, name, birth_year))
     cur . executemany('insert   into  actors  values (%s,%s,%s)' ,  list)
     con.commit()
     print("insert successful")
  #print(cur.rowcount)
     s=input("You want to insert more elements (y/n): ")
     if s=='n':
       print("ok")
       break
except mysql.connector.Error as err:
    print("Database error:", err)
