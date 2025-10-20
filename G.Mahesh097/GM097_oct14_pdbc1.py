"""
Write a program to print emp table of the database with fetchone() method.

FLOW:
emp table ----------------> cursor object -----------------> tpl ---------> monitor
             execute()                               fetchone()             print()
"""

import   mysql . connector   as   mc   
try:
	con = mc . connect(database = 'empdb' , user = 'root')
	cur = con . cursor()  
	cur . execute('select  *  from  emp')
	for  x  in  cur . description: 
		print(F'{x[0] : ^10}' ,  end = '\t')  
	print() 
	while  tpl := cur . fetchone():  
		for  x  in  tpl:  
			print(F'{x : ^10} ' , end='\t')
		print()
	print('Number  of  tuples :  ' , cur . rowcount)
	cur . close()
	con . close()
except  mc . errors . ProgrammingError  as  msg:
	print(msg)
except  mc . errors . DatabaseError:
	print('Pls  start  mysql')



"""
Write a program to print emp table based on user condition.

1) How to call execute() method?
   ---> cur.execute('select * from emp where ' + cond)

2) What is the pre-requisite to call execute() method?
   ---> Read the condition from the user

FLOW:
emp table ----------------> cursor object -----------------> tpl ---------> monitor
             execute()                               fetchone()             print()
"""

import mysql.connector as mc
try:
	con = mc.connect(database='empdb', user='root')
	cur = con.cursor()
	cond = input('Enter any condition : ')
	if cond == '':
		cur.execute('select * from emp')
	else:
		cur.execute(f'select * from emp where {cond}')
	for x in cur.description:
		print(f'{x[0]:^10}', end='\t')
	print()
	while tpl := cur.fetchone():
		for x in tpl:
			print(f'{x:^10}', end='\t')
		print()
	print('Number of tuples :', cur.rowcount)
	cur.close()
	con.close()
except mc.errors.ProgrammingError as msg:
	print(msg)
except mc.errors.DatabaseError:
	print('Pls start mysql')



"""
Write a program to print emp table in sorted order.

1) How to call execute() method?
   ---> cur.execute('select * from emp order by ' + colname)

2) What is the pre-requisite to call execute() method?
   ---> Read the column name

FLOW:
emp table ----------------> cursor object -----------------> tpl ---------> monitor
             execute()                               fetchone()             print()
"""

import mysql.connector as mc
try:
	con = mc.connect(database='empdb', user='root')
	cur = con.cursor()
	colname = input('Enter column name: ')
	if colname == '':
		cur.execute('select * from emp')
	else:
		cur.execute(f'select * from emp order by {colname}')
	for x in cur.description:
		print(f'{x[0]:^10}', end='\t')
	print()
	while tpl := cur.fetchone():
		for x in tpl:
			print(f'{x:^10}', end='\t')
		print()
	print('Number of tuples :', cur.rowcount)
	cur.close()
	con.close()
except mc.errors.ProgrammingError as msg:
	print(msg)
except mc.errors.DatabaseError:
	print('Pls start mysql')




"""
Write a program to print user input table with next() function.

1) How to call execute() method?
   ---> cur.execute('select * from ' + table)

2) What is the pre-requisite to call execute() method?
   ---> Read the table name

3) What does next(cur) do?
   ---> Yields the next tuple of cursor object

4) What does next() function do when end of cursor is reached?
   ---> Throws StopIteration error

FLOW:
emp table ----------------> cursor object -----------------> tpl ---------> monitor
             execute()                                  next()             print()
"""

import mysql.connector as mc
try:
	con = mc.connect(database='empdb', user='root')
	cur = con.cursor()
	table_name = input('Enter table name : ')
	while table_name == '':
		table_name = input('Enter table name : ')
	cur.execute(f'select * from {table_name}')
	for x in cur.description:
		print(f'{x[0]:^10}', end='\t')
	print()
	while True:
		try:
			tpl = next(cur)
			for x in tpl:
				print(f'{x:^10}', end='\t')
			print()
		except StopIteration:
			break
	print('Number of tuples :', cur.rowcount)
	cur.close()
	con.close()
except mc.errors.ProgrammingError as msg:
	print('Invalid table name')
except mc.errors.DatabaseError:
	print('Pls start mysql')




"""
Write a program to print cursor with fetchall() method.

FLOW:
emp table ---------------> cur object ---------------> list -------------> tpl ------------> monitor
          execute()                            fetchall()                for loop              print()
"""

import mysql.connector as mc
try:
	con = mc.connect(database='empdb', user='root')
	cur = con.cursor()
	cur.execute('select * from emp')
	list = cur.fetchall()
	for x in cur.description:
		print(f'{x[0]:^10}', end='\t')
	print()
	for tpl in list:
		for x in tpl:
			print(f'{x:^10}', end='\t')
		print()
	print('Number of tuples :', len(list))
	cur.close()
	con.close()
except mc.errors.ProgrammingError as msg:
	print(msg)
except mc.errors.DatabaseError:
	print('Pls start mysql')
