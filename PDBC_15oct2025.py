'''
Write  a  program  to  print  first  'n'  rows  of  emp  table

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
'''
import mysql.connector as mc
try:
	n = int(input('How many Rows? :  '))
	con = mc.connect(database = 'empdb' , user = 'root')
	cur = con.cursor()
	cur.execute('select * from emp')
	list = cur.fetchmany(n)
	for y in cur.description:
		print(f'{y[0]:^7}' , end = '\t')
	print()
	for x in list:
		print(f'{x[0]}\t{x[1]}\t{x[2]}\t')
	print(f'Number of Rows : {cur.rowcount}')
except  mc.errors.ProgrammingError  as  msg:
	print(msg)
except   mc.errors.DatabaseError:
	print('Pls  start  mysql')\t)



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
	con = mc.connect(database = 'empdb' , user = 'root')
	cur = con.cursor()
	while True:
		try:
			empno = int(input('Enter Employee Number : '))
			ename = input('Enter Employee Name : ')
			sal = float(input('Enter Salary : '))
			cur.execute(f"insert into emp values ({empno} , '{ename}' , {sal})")
			con.commit()
		except mc.errors.IntegrityError:
			print('No duplicate value allowed for employee number')
		print(f'Number of Rows Inserted : {cur.rowcount}')
		a = input('Want to add one more row (Yes or No) : ')
		if a == 'NO' or a == 'n' or a == 'N' or a == 'no':
			break
except  mc.errors.ProgrammingError  as  msg:
	print(msg)
except   mc.errors.DatabaseError:
	print('Pls  start  mysql')



'''
Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition

1) How  to  call  execute()  method ?  --->   cur . execute(F'delete  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the  cond
'''
import mysql.connector as mc
try:
	con = mc.connect(database = 'empdb' , user = 'root')
	cur = con.cursor()
	cond = input('Enter Condition : ')
	cur.execute(f'delete from emp where {cond}')
	con.commit()
	print(f'{cur.rowcount} Rows deleted')
except mc.errors.ProgrammingError as msg:
	print(msg)
except mc.errors.DatabaseError:
	print('Pls Start mysql')



'''
Write  a  program to  modify  data  of  emp  table

1) How  to  call  execute()  method ?  --->  cur . execute(F'update  emp  set  {expr}   where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  expr  and  cond
'''
import  mysql . connector as mc
try:
	con  =  mc . connect(database = 'empdb' , user = 'root')
	cur  =  con . cursor()
	cond = input('Enter condition: ')
	expr = input('Enter column name = value: ')
	cur . execute(F'update emp set {expr} where {cond}')
	con . commit()
	print(F'{cur . rowcount} Rows Updated')
except mc . errors . ProgrammingError  as   msg:
	print(msg)
except     mc . errors . InterfaceError:
	print('Pls  start  mysql')
