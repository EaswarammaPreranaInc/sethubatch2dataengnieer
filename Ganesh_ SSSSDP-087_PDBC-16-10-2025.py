'''
Repeat  prog8b(fetchmany)  but  validate  input
i.e. Print  a  msg  when  input > number  of  tuples

Hint:  Use  fetchmany()  method
'''
import mysql.connector as mc
try:
	con = mc.connect(host='localhost',user='root',database='employees',password='root')
	cur = con.cursor()
	cur.execute('select *from emp')
	n = int(input("Enter the number of rows: "))
	list = cur.fetchmany(n)
	if n > len(list):
		print("Input must be less than or equal to number of rows in the table")
	else:
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
import mysql.connector as mc
try:
    con = mc.connect(host='localhost', user='root', password='root', database='employees')
    cur = con.cursor()
    data = [] 
    while True:
        empno = int(input("Enter Emp No: "))
        ename = input("Enter Emp Name: ")
        sal = float(input("Enter Salary: "))
        data.append((empno, ename, sal))  					# add tuple to list
        ch = input("Insert another row? (Y/N): ").upper()
        if ch == 'N':
            break
    cur.executemany("INSERT INTO emp VALUES (%s, %s, %s)", data)
    con.commit()
    print(f"{cur.rowcount} rows inserted")
    cur.close()
    con.close()
except mc.errors.IntegrityError:
    print("Duplicate record found. Some rows were not inserted.")
except mc.errors.ProgrammingError as msg:
    print(msg)
except mc.errors.DatabaseError:
    print("Please start MySQL server.")