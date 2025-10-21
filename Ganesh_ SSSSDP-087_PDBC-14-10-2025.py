'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''

import mysql.connector as mc
try:
	con = mc.connect(host='localhost',database='employee',user='root',password='root')
	cur = con.cursor()
	cur.execute('select *from emp')
	for x in cur:
		print(x)
	print("Number of tuples: ",cur.rowcount)
	cur.close()
	con.close()
except mc.errors.ProgrammingError as msg:
	print(msg)
except mc.errors.DatabaseError as msg:
	print('start mysql')
'''
 Emp Number       Emp Name                Salary
 10                Rama Rao               10000.0
 15                Kiran                  15000.0
 20                Sita           		 20000.0
 Number  of  tuples :   3
'''



'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''
import mysql.connector as mc
try:
	con = mc.connect(host='localhost',user='root',database='employee',password='root')
	cur = con.cursor()
	cond = input("Enter the condition: ")
	if cond == '':
		cur.execute('select *from emp')
	else:
		cur.execute(f'select *from emp where {cond}')

	for i in cur.description:
		print(f'{i[0]: ^10}',end='\t')
	print()
	while tpl:= cur.fetchone():
		for i in tpl:
			print(f'{i: ^10}',end='\t')
		print()
	print("Number of rows",cur.rowcount)
	cur.close()
	con.close()
except mc.errors.ProgrammingError as msg:
	print(msg)
except mc.errors.DataError:
	print('please start mysql')

'''
 Enter  any  condition : sal > 12000
 Emp Number       Emp Name                Salary
   15             Kiran                   15000.0
   20             Sita                    20000.0
 Number  of  tuples  :  2
'''



'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''
import mysql.connector as mc
try:
	con = mc.connect(host='localhost',user='root',database='employee',password='root')
	cur = con.cursor()
	colname = input("Enter the column name: ")
	if colname == '':
		cur.execute(f'select *from emp')
	else:
		cur.execute(f'select *from emp order by {colname}')
	for i in cur.description:
		print(f'{i[0] : ^10}',end='\t')
	print()
	while tpl := cur.fetchone():
		for i in tpl:
			print(f'{i: ^10}',end='\t')
		print()
	print("Number of rows",cur.rowcount)
	con.close()
	cur.close()
except mc.errors.ProgrammingError as msg:
	print(msg)
except mc.errors.DatabaseError:
	print("please start mysql") 

'''
 Enter column name: sal desc
 Emp Number       Emp Name                Salary
   20             Sita                    20000.0
   15             Kiran                   15000.0
   10             Rama Rao                10000.0
 Num  of rows :  3
'''


'''
Write  a  program  to  print  user  input  table  with  next()  function

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  {table}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the   table  name

3) What  does  next(cur)  do ?  --->  Yields  the  next  tuple  of  cursor  object

4) What  does   next()  function  do  when  end  of   the  cursor  is  reached ?  ---> Throws StopIteration  error

5) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                          execute()                                   next()                  print()
'''
import mysql.connector as mc
try:
	con = mc.connect(host='localhost',user='root',database='employees',password='root')
	cur = con.cursor()
	table = input("Enter the table name: ")
	while table == '':
		table = input("Enter the table name: ")
	cur.execute(f'select *from {table}')
	for i in cur.description:
		print(f'{i[0] : ^10}',end='\t')
	print()
	while True:
		try:
			tpl = next(cur)
			for i in tpl:
				print(f'{i : ^10}',end='\t')
			print()
		except StopIteration:
			break
	print("Number of rows: ",cur.rowcount)
	cur.close()
	con.close()
except mc.errors.ProgrammingError as msg:
	print(msg)
except mc.DatabaseError:
	print("please start mysql")

'''
 Enter   table  name :  emp
 Emp  Number      Emp  Name       Salary
   10             Rama Rao        10000.00
   15             Kiran           15000.00
   20             Sita            20000.00
 Number  of  tuples :   3

 Enter   table  name :  stud
 1146 (42S02): Table 'empdb.stud' doesn't exist
'''



'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''
import mysql.connector as mc
try:
	con = mc.connect(host='localhost',user='root',database='employees',password='root')
	cur = con.cursor()
	cur.execute('select *from emp')
	list = cur.fetchall()
	for i in cur.description:
		print(f'{i[0] : ^10}',end='\t')
	print()
	for i in list:
		for j in i:
			print(f'{j : ^10}',end='\t')
		print()
	print("Number of rows:",cur.rowcount)
	cur.close()
	con.close()
except mc.errors.ProgrammingError as msg:
	print(msg)
except mc.DatabaseError:
	print("please start mysql")
'''
 Emp Number       Emp Name        Salary
   10             Rama Rao          10000.00
   15             Kiran             15000.00
   20             Sita              20000.00
 Number  of  tuples  :  3
'''