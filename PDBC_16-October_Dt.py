'''
Repeat  prog8b(fetchmany)  but  validate  input
i.e. Print  a  msg  when  input > number  of  tuples

Hint:  Use  fetchmany()  method
'''
import mysqlconnector as mc
try:
	con = mc.connect(database = 'emp' , user = 'root')
	cur = con.cursor()
	con.execute('select * from emp')
	n = int(input('Enter How Many Rows : '))
	list = cur.fetchmany(n)
	if n < 1 or n > cur.rowcount:		
		print('Invalid Input')
	else:
		for y in cur.description:
			print(f'y[0] : ^7' , end = \t)
		for x in list:
			print(f'{x[0]\t}  {x[1]\t}  {x[2]\t}')
		print(f'Number of Rows : {len(list)}')
except mc.errors.ProgrammingError as msg:
	print(msg)
except mc.errors.DatabaseError:
	print('Start Mysql')




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
import mysql.connector as mc
try:
	con = mc.connect(database = 'empdb' , user = 'root')
	cur = con.cursor()
	list = [(101 , 'CBN' , 250000) , (102 , 'PK' , 3000000)]
	cur.executemany('insert   into  emp  values (%s,%s,%s)' ,  list)
	con.commit()
	print(f'{cur.rowcount} rows inserted')
except mc.errors.ProgrammingError as msg:
	print(msg)
except mc.errors.DatabaseError:
	print('Connect to mysql')
