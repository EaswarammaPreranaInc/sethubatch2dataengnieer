'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''
import mysql.connector as mc
try:
	con = mc.connect(database = 'empdb' , user = 'root')
	cur = con.cursor()
	cur.execute('select * from emp')
	while tpl := cur.fetchone():
		print(f'{tpl[0]} \t  {tpl[1]} \t  {tpl[2]}')
	print(f'Number of tuples : {cur . rowcount}')
except  mc.errors.ProgrammingError  as  msg:
	print(msg)
except   mc.errors.DatabaseError:
	print('Pls  start  mysql')


'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''
import mysql.connector as mc
try:
	cond = input('Enter a Condition : ')
	con = mc.connect(database = 'empdb' , user = 'root')
	cur = con . cursor()
	cur.execute(f'select * from emp where {cond}')
	while tpl := cur.fetchone():
		print(f'{tpl[0]}\t {tpl[1]}\t  {tpl[2]}\t')
	print(f'Number of Rows : {cur.rowcount}')
except  mc.errors.ProgrammingError  as  msg:
	print(msg)
except   mc.errors.DatabaseError:
	print('Pls  start  mysql')



'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''

import mysql.connector as mc
try:
	cond = input('Enter a Column name : ')
	con = mc.connect(database = 'empdb' , user = 'root')
	cur = con . cursor()
	cur.execute(f'select * from emp order by {cond}')
	while tpl := cur.fetchone():
		print(f'{tpl[0]}\t {tpl[1]}\t  {tpl[2]}\t')
	print(f'Number of Rows : {cur.rowcount}')
except  mc.errors.ProgrammingError  as  msg:
	print(msg)
except   mc.errors.DatabaseError:
	print('Pls  start  mysql')



'''
Write  a  program  to  print  user  input  table  with  next()  function

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  {table}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the   table  name

3) What  does  next(cur)  do ?  --->  Yields  the  next  tuple  of  cursor  object

4) What  does   next()  function  do  when  end  of   the  cursor  is  reached ?  ---> Throws StopIteration  error

5) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                          execute()                                   next()                  print()
'''
import mysql.connector as mc
try:
	cond = input('Enter Table name : ')
	con = mc.connect(database = 'empdb' , user = 'root')
	cur = con . cursor()
	cur.execute(f'select * from {cond}')
	while True:
		try:
			tpl = next(cur)
			print(f'{tpl[0]}\t {tpl[1]}\t  {tpl[2]}\t')
		except StopIteration:
			break
	print(f'Number of Rows : {cur.rowcount}')
except  mc.errors.ProgrammingError  as  msg:
	print(msg)
except   mc.errors.DatabaseError:
	print('Pls  start  mysql')



'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''
import mysql.connector as mc
try:
	con = mc.connect(database = 'empdb' , user = 'root')
	cur = con . cursor()
	cur.execute(f'select * from emp')
	list = cur.fetchall()
	for x in list:
		print(f'{x[0]}\t , {x[1]}\t , {x[2]}\t')
	print(f'Number of Rows : {len(list)}')
except  mc.errors.ProgrammingError  as  msg:
	print(msg)
except   mc.errors.DatabaseError:
	print('Pls  start  mysql')
