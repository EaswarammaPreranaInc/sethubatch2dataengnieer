 # Find  outputs   (Home  work)
try:
	print('Outer   try')					
	try:
		print('Inner    try')
		print(7 / 0)
		int('Hyd')
		'Hyd'[5]
		eval('Hyd')
	except   ZeroDivisionError:
		print('ZDE   of   inner   try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try')
	finally:
		print('Inner  try  finally')
	print('End  of  inner  try')
except   ValueError:
	print('ValueError  of  outer  try')
except   IndexError:
	print('IndexError  of  outer  try')
except:
	print('default  except  of  outer  try')
finally:
	print('Outer  try  finally')
print('End  of  outer  try')
'''
	# output
 Outer try
 Inner try
 ZDE of inner try
 Inner try finally
 ValueError of outer try
 Outer try finally
 End of outer try
'''


 #  Find outputs   (Home  work)
try:
	print('Outer  try')
	try:
		print('Inner  try')
		int('Hyd')
		'Hyd'[5]
		eval('Hyd')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try ')
	finally:
		print('Inner  try  finally')
	print('End  of  inner  try')
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
except:
	print('default except of outer try')
finally:
	print('Outer try finally')
print('End of outer try')
'''
	#Output
 Outer try
 Inner try
 ValueError of inner try
 Inner try finally
 End of inner try
 Outer try finally
 End of outer try
'''


 #  Find outputs   (Home  work)
try:
	print('Outer  try')
	try:
		print('Inner  try')
		'Hyd'[3]
		eval('Hyd')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try ')
	finally:
		print('Inner  try  finally')
	print('End  of  inner  try')
except  ValueError:
	print('ValueError  of  outer  try')
except  IndexError:
	print('IndexError  of  outer  try')
except:
	print('default except of outer try')
finally:
	print('Outer try finally')
print('End  of  outer  try')
'''
	output
 Outer try
 Inner try
 Inner try finally
 IndexError of outer try
 Outer try finally
 End of outer try
'''




 #  Find  outputs (Home  work)
try:
	print('Outer  try')
	try:
		print('Inner  try')
		eval('Hyd')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')
	finally:
		print('Inner  try  finally')
	print('End of inner try')
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
except:
	print('default  except  of  outer  try')
finally:
	print('Outer  try  finally')
print('End  of  outer  try')
'''
	ouput
 Outer try
 Inner try
 Inner try finally
 default except of outer try
 Outer try finally
 End of outer try
'''




 #  Find  outputs (Home  work)
try:
	print('Outer  try')
	try:
		print('Inner  try')
		print(10 + '20')			# error 
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')
	finally:
		print('Inner  try  finally')
	print('End of inner try')
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
finally:
	print('Outer  try  finally')
print('End  of  outer  try')
'''
	outer 
 Outer try
 Inner try
 # error in line 5 becaues cannot cancate the int and string
 Inner try finally
 end of inner try
 Outer try finally
 End of outer try
'''



 # Find  outputs   (Home  work)
class   MyError(BaseException):
	def    _init_(self , y):
		self . a = y
		print('Constructor')
# End of  the class
def  compute(x):
	print(x)
	if  x > 20:
		raise   MyError(x)
	print('Hello')
# End of  the functrion
try:
	compute(10)
	compute(30)
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ' ,  msg)
print('End')
'''
	output
 10
 Hello
 30
 Caught MyError outside:  30
 End
'''



 # Find  outputs   (Home  work)
class   MyError(NameError):
	def    _init_(self):
		self . a =  25
		print('Constructor')
# End of  the class
def  compute(x):
	print(x)
	if  x > 20:
		raise   MyError()
	print('Hello')
#end of  the functrion
try:
	compute(30)
	compute(10)
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ' ,  msg)
print('End')
'''
	output
 30
 Caught MyError outside:  30
 End
'''



 # Find  outputs (Home  work)
try:
	print(1)
	print(2)
	print(3)
except:
	print(4)
else:
	print(5)
finally:
	print(6)
print(7)
'''
	output
 1
 2
 3
 5
 6
 7
'''




 # Find  outputs   (Home  work)
try:
	print(1)
	print(7 / 0)
	print(3)
except:
	print(4)
else:
	print(5)
finally:
	print(6)
print(7)
'''
	output
 1
 4
 6
 7
'''



 # Find  outputs   (Home  work)
try:
	print(1)
	print(7 / 0)
	print(3)
except:
	int('Two')
else:
        print(5)
finally:
        print(6)
print(7)
'''
	output
 1
 error line 3 Zerodivision error cannot handled in except suite and raised the valueerror 
 6
 7
'''



 # Find  outputs (Home  work)
from  threading  import  *
def  f1():
	print('child thread name: ',current_thread().name)			# How  to  print  name  of  child  thread
# main  thread  executes  following  statements
new=Thread(target=f1,name='new')						# How  to  create  a  new  thread  with  name  'new'   and  target  f1
new.start()									# How  to  start  the  new  thread
print('main thread name: ',current_thread().name) 				# How  to  print  name  of   main  thread
'''
	output
 child thread name: new 
 main thread name: Mainthread
'''



 # Find  outputs (Home  work)
 def f1():
	pass
 t1=Thread(target=f1,name='Hyd')						# How  to  create  a  thread  t1  with  name  'Hyd'
 t2=Thread(target=f1)						# How  to  create  another  thread  t2  without  a  name
 print(current_thread().name)			# How  to  print  name  of  main  thread
 print(t1.name)					# How  to  print  name  of  thread  t1
 print(t2.name)					# How  to  print  name  of  thread  t2
 current_thread().name='India'			# How  to  modify  name  of  main  thread  to  'India'
 t1.name='Sec'					# How  to  modify  name  of  thread  t1  to  'Sec'
 t2.name='Cyb'					# How  to  modify  name  of  thread  t2  to  'Cyb'
 print(current_thread().name)			# How  to  print  name  of  main  thread
 print(t1.name)					# How  to  print  name  of  thread  t1
 print(t2.name)					# How  to  print  name  of  thread  t2
 print(active_count())				# How  to  print  number  of  threads  under  execution
'''
	output
 MainThread
 Hyd
 Thread-1
 India
 Sec
 Cyb
 1
'''




 # Find  outputs  (Home  work)
from  threading  import  *
def   f1(x):
	s = current_thread() . name
	while   True:
		print(s , ' : ' , x)
#  main  thread  executes  following  statements
t1 = Thread(target = f1 , name = 'Hyd' , args = (10,))
t2 = Thread(target = f1 , name = 'Sec' , args =  [20])
t1 . start()
t2 . start()
print(active_count())
print('Press  ctrl + break  or  Fn + b  to  stop ')
'''
	output
 Hyd : 10
 Sec : 20     # this two elements prints until the you the loop pressing control + break  
 1
 Press ctrl+break or Fn + b to stop
'''

'''
1) Which  of  the  following  are  valid ?
    args = [10]  ---> Valid  due  to  sequence
    args = (10,) ---> Valid  due  to  sequence
    args = {10}  --->  Valid  due  to  sequence
    args = 10   ---> 	Invalid  becoz  10  is  not  a  sequence
    args = 10.8 --->	Invalid  becoz  10.8  is  not  a  sequence
    args = '10'  ---> Valid  when  function  has  got  two  arguments  and  invalid  otherwise  becoz  '10'  has  2  characters
    args = (10)  ---> Invalid  becoz  10  is  not  a  sequence

2) In  general,  args  argument  of  Thread  constructor  can  be  any  sequence




 # Find  outputs (Home  work)
from  threading  import  Thread , current_thread
from  random  import  randint
def   f1(n):
	ctr = 0
	s = current_thread() . name
	while  True:
		x = randint(1 , 100)
		ctr += 1
		print(F'{s}  guess  {x}   in  attempt  :  {ctr}')
		if   x ==  n:
			break
	#end of while loop
	print(F'{s}  finish  in  {ctr}  attempts')
# End  of  function   f1()
t1 = Thread(target = f1 , args = [75] , name = 'Rama')
t2 = Thread(target = f1 , args = [50] , name = 'Sita')
t1 . start() #   t1  executes  f1(75)
t2 . start()  #   t2  executes  f1(50)
'''
	output
Rama  guess  19   in  attempt  :  1
Rama  guess  88   in  attempt  :  2
Rama  guess  75   in  attempt  :  3
Rama  finish  in  3  attempts
Sita  guess  15   in  attempt  :  1
Sita  guess  25   in  attempt  :  2
Sita  guess  40   in  attempt  :  3
Sita  guess  98   in  attempt  :  4
Sita  guess  89   in  attempt  :  5
Sita  guess  85   in  attempt  :  6....
Sita  finish  in  6  attempts
    like this until it stop the iteration
'''



 # Find  outputs (Home  work)
from threading import *
def   disp():
	for  i  in  range(10):
		print('new  thread')		
#  child  thread  is  dead
new = Thread(target = disp)
new . start()
new . join()
for  i  in  range(10):
	print('main  thread')
# main   thread is  dead
'''
	output
	new  thread
new  thread
new  thread
new  thread
new  thread
new  thread
new  thread
new  thread
new  thread
new  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
''''




 #  Find  outputs (Home  work)
from  threading  import *
import  time
def   disp():
	for  i  in  range(10):
		print('new  thread')
		time . sleep(2)
new = Thread(target = disp)
new . start()
new . join(10)
for  i  in  range(10):
	print('main  thread')

'''
 	output
 new thread  (10 times)   each new thread print after 2 seconds if any order
 main thread (10 times)  each main thread print after 2 seconds if any order
'''



 # Find  outputs (Home  work)
from threading import *
import time
def   double():
	for   i  in  range(1 , 7):
		print('Double : ' , 2 * i)
		time . sleep(1)
def   square():
	for   i  in   range(1 , 7):
		print('Square : ' , i * i)
		time . sleep(1)
start = time . time()
double()
square()
end = time . time()
print(end - start)
'''
	output
 Double :  2
Double :  4
Double :  6
Double :  8
Double :  10
Double :  12
Square :  1
Square :  4
Square :  9
Square :  16
Square :  25
Square :  36
12.001637935638428
 each double and square print after 1 second if any order
 '''





 # Find  outputs  (Home  work)
from  threading  import  *
import  time
def   display():
        name = current_thread() . name
        print(name , ' is  started')
        time . sleep(3)
        print(name , ' is  ended')
# End  of  the  function
print(active_count())
t1 = Thread(target = display , name = 'One')
t2 = Thread(target = display , name = 'Two')
t3 = Thread(target = display , name = 'Three')
print(active_count())
t1 . start()
t2 . start()
t3 . start()
print(active_count())
t1 . join()
t2 . join()
t3 . join()
print(active_count())
'''
	output'
 1
1
One  is  started
Two  is  started
Three  is  started
4
One  is  ended
Two  is  ended
Three  is  ended
1
 some print after 3 seconds 
'''




 # Find  outputs  (Home  work)
from  threading  import  *
import  time
def   disp():
	name = current_thread() . name
	print(name , ' is  started')
	time . sleep(3)
	print(name , '  is  ended')
# End  of  the  function
t1 = Thread(target = disp , name = 'One')
t2 = Thread(target = disp , name = 'Two')
t3 = Thread(target = disp , name = 'Three')
t1 . start()
t2 . start()
t3 . start()
list = enumerate()
for  t  in   list:
	print(t . name)
t1 . join()
t2 . join()
t3 . join()
list = enumerate()
for  t  in  list:
	print(t . name)
'''
	output
 One  is  started
 Two  is  started
 Three  is  started
 MainThread
 One
 Two
 Three
	# here this values print after 3 sec 
 One   is  ended
 Two   is  ended
 Three   is  ended
 MainThread
'''




 # is_alive()  method   demo  program
from  threading  import *
import  time
def   disp():
	name =  current_thread() . name
	print(name , 'is   started')
	time . sleep(3)
	print(name , '   is    ended')
t1 = Thread(target = disp , name = 'One')
t2 = Thread(target = disp , name = 'Two')
t3 = Thread(target = disp , name = 'Three')
t1 . start()
t2 . start()
t3 . start()
print(t1 . is_alive())
print(t2 . is_alive())
print(t3 . is_alive())
t1 . join()
t2 . join()
t3 . join()
print(t1 . is_alive())
print(t2 . is_alive())
print(t3 . is_alive())
'''
	output
One is   started
Two is   started
Three is   started
True
True
True
   # here below elements print after 3 sec
One    is    ended
Two    is    ended
Three    is    ended
False
False
False
'''




 # Find  outputs (Home  work)
from  threading  import  *
import  time
def   table(n):
	print('Table  :  ' , n)
	for i  in  range(1 , 11):
		print(F'{n}  *  {i}    =   {n * i}')
		time . sleep(1)
t1 = Thread(target = table , args = (7,))
t2 = Thread(target = table , args = (4,))
t1 . start()
t2 . start()
'''
Table  :   7
7  *  1    =   7
Table  :   4
4  *  1    =   4
7  *  2    =   14
4  *  2    =   8
7  *  3    =   21
4  *  3    =   12
7  *  4    =   28
4  *  4    =   16
7  *  5    =   35
4  *  5    =   20
7  *  6    =   42
4  *  6    =   24
7  *  7    =   49
4  *  7    =   28
7  *  8    =   56
4  *  8    =   32
7  *  9    =   63
4  *  9    =   36
7  *  10    =   70
4  *  10    =   40
 # here each 2 lines print after 1 second
'''