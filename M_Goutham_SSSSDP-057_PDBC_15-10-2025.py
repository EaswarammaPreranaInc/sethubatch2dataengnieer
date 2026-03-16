'''
Write  a  program  to  print  first  'n'  rows  of  emp  table

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
'''

import mysql.connector as mc
try:
	con = mc.connect(host='localhost',user='root',database='chotu',password='0512')
	cur = con.cursor()
	cur.execute('select *from emp')
	n = int(input("Enter the number of rows: "))
	list = cur.fetchmany(n)
	if list:
		for i in cur.description:
			print(f'{i[0]: ^10}',end='\t')
		print()
	for i in list:
		for j in i:
			print(f'{j: ^10}',end='\t')
	print()
	print("Number of rows: ",len(list))
	cur.close()
	con.close()
except mc.InternalError as msg:
	print('cursor cannot be closed')
except mc.errors.ProgrammingError as msg:
	print(msg)
except mc.errors.DatabaseError:
	print("Please start mysql")
except AttributeError:
	print("Input should be +ve")






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
import mysql.connector as mc
try:
	con = mc.connect(host='localhost',user='root',database='chotu',password='0512')
	cur = con.cursor()
	while True:
		empno = int(input("Enter the emp no: "))
		ename = input("Enter the ename: ")
		sal = float(input("Enter the sal: "))
		try:
			cur . execute(F"insert  into  emp  values  ({empno} ,  '{ename}' , {sal})")
			con.commit()
			print(f'{cur.rowcount} row is inserted')
		except mc.errors.IntegrityError:
			print("Duplicates cannot be insterted")

		ch = input("Insert another row ? Y or N: ").upper()
		if ch == 'N':
			break
except mc.errors.ProgrammingError as msg:
	print(msg)
except mc.errors.DatabaseError:
	print("please start mysql")






'''
Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition

1) How  to  call  execute()  method ?  --->   cur . execute(F'delete  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the  cond
'''

import mysql.connector as mc
try:
	con = mc.connect(host='localhost',user='root',database='chotu',password='0512')
	cur = con.cursor()
	cond = input("Enter the condition: ")
	if cond == '':
		cur.execute('delete from emp')
	else:
		cur . execute(F'delete  from  emp  where  {cond}')
	con.commit()
	print(f'{cur.rowcount} row is deleted')
	cur.close()
	con.close()
except mc.errors.ProgrammingError as msg:
	print(msg)
except mc.errors.DatabaseError:
	print("Please start mysql")




'''
Write  a  program to  modify  data  of  emp  table

1) How  to  call  execute()  method ?  --->  cur . execute(F'update  emp  set  {expr}   where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  expr  and  cond
'''

import mysql.connector as mc
try:
	con = mc.connect(host='localhost',user='root',database='chotu',password='0512')
	cur = con.cursor()
	cond = input("Enter the condition: ")
	expr = input("Enter the expression: ")
	if cond == '':
		cur . execute(F'update  emp  set  {expr}')
	else:
		cur . execute(F'update  emp  set  {expr}   where  {cond}')
	con.commit()
	print(f'{cur.rowcount} rows updated')
	cur.close()
	con.close()
except mc.errors.ProgrammingError as msg:
	print(msg)
except mc.errors.DatabaseError:
	print("Please start mysql")
    



'''
Write  a  program  to  create  student  table

1) How  to  call  execute()  method ?  --->
									cur . execute(F'create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float)')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  table  name

3) What  action  to  be  made  when  table  already  exists ?  --->
																	Delete  the  existing  table  and  create  a  new  table  with  same  name
'''

import mysql.connector as mc
try:
	con = mc.connect(database='chotu',password='0512')
	cur = con.cursor()
	table_name = input("Enter the table name: ")
	cur . execute(F'create  table  {table_name}(rollno  int  primary  key , sname  char(20) ,  marks  float)')
	print(f'{table_name} table is created')
	cur.close()
	con.close()
except mc.errors.ProgrammingError:
	cur.execute(f'drop table {table_name}')
	print(f'Existing {table_name} table is deleted')
	cur . execute(F'create  table  {table_name}(rollno  int  primary  key , sname  char(20) ,  marks  float)')
	print(f'{table_name} table is created')
except mc.errors.DatabaseError:
	print("please start mysql")