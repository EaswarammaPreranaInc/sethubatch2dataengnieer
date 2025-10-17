'''
Write  a  program  to  print  first  'n'  rows  of  emp  table

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
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
  list=cur.fetchmany(n)
  for col in list:
    for val in col:
      print(f"{val:^40}",end=' ')
    print()
  print(cur.rowcount)
except mysql.connector.Error as err:
    print("Database error:", err)


enter table name : movies
                movie_id                                  title                                 release_year            
enter how many rows? : 6
                  101                                K.G.F: Chapter 2                               2022                
                  102                    Doctor Strange in the Multiverse of Madness                   2022             
                  103                             Thor: The Dark World                              2013                
                  104                                Thor: Ragnarok                                 2017                
                  105                            Thor: Love and Thunder                             2022                
                  106                                     Sholay                                    1975                
6




Write  a  program  to  insert  rows  into  emp  table ,  one  at  a  time

1) How  to  call  execute()  method ?  --->cur . execute(F"insert  into  emp  values  ({empno} ,  '{ename}' {sal})")

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

import mysql.connector
try:
  con=mysql.connector.connect(host="localhost", user="root",database="moviesdb",password="root")
  cur=con.cursor()
  table=input("enter table name : ")
  actor_id=input("enter actor_id: ")
  name=input("enter name: ")
  birth_year=input("enter birth year : ")
  cur.execute(F"insert  into  actors  values  ({actor_id} ,  '{name}', {birth_year});")
  con.commit()
  print("insert successful")
  #print(cur.rowcount)
except mysql.connector.Error as err:
    print("Database error:", err)





'''
Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition

1) How  to  call  execute()  method ?  --->   cur . execute(F'delete  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the  cond
'''

import mysql.connector
try:
  con=mysql.connector.connect(host="localhost", user="root",database="moviesdb",password="root")
  cur=con.cursor()
  table=input("enter table name : ")
  cond=input("enter condition: ")
  cur.execute(F"delete  from  actors  where  {cond};")
  con.commit()
  print("deletion successful")
  #print(cur.rowcount)
except mysql.connector.Error as err:
    print("Database error:", err)




'''
Write  a  program  to  create  student  table

1) How  to  call  execute()  method ?  --cur . execute(F'create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float)')
2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  table  name

3) What  action  to  be  made  when  table  already  exists ?  --->Delete  the  existing  table  and  create  a  new  table  with  same  name
'''
import mysql.connector
try:
  con=mysql.connector.connect(host="localhost", user="root",database="moviesdb",password="root")
  cur=con.cursor()
  tablename=input("enter table name : ")
  cur.execute(F"create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float);")
  con.commit()
  print("creation successful")
  #print(cur.rowcount)
except mysql.connector.Error as err:
    print("Database error:", err)