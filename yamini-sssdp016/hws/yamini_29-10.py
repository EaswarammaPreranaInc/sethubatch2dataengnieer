# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')
		raise  ValueError('Hyd')
		print('Hi')
	finally:
		print("f1's  finally")
	print('End  of  f1  function')
def  f2():
	try:
		print('f2  function')
		return
		print('Hello')
	finally:
		print("f2's  finally")
	print('End  of  f2  function')
def  f3():
	try:
		print('f3  function')
		raise   KeyError(25)
		print('Hello')
	except KeyError as  msg:
		print('Caught  by  f3  function :  ' , msg)
	finally:
		print("f3's  finally")
	print('End of f3 function')
def  f4():
	try:
		print('f4 function')
		exit()
	finally:
		print("f4's  finally")
	print('End of f4 function')
# End  of  all  the  functions
try:
	print('Begin')
	f1()
	print('Hello')
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)
f2()
f3()
try:
	f4()
finally:
		print('Outside  finally')
print('End  of  the  program')

'''
Begin
f1  function
f1's  finally
ValueError  is  caught  outside :  Hyd
f2  function
f2's  finally
f3  function
Caught  by  f3  function :  25
f4 function
End of f3 function
f4's  finally
Outside  finally
'''

# Find  outputs  (Home  work)
import sys
def  f1():
	try:
		print('f1  function')
		raise  ValueError('Hyd')
		print('Hi')
	finally:
		print("f1's  finally")
	print('End  of  f1  function')
def  f2():
	try:
		print('f2  function')
		return
		print('Hello')
	finally:
		print("f2's  finally")
	print('End  of  f2  function')
def  f3():
	try:
		print('f3  function')
		raise   KeyError(25)
		print('Hello')
	except  KeyError  as  msg:
		print('Caught  by  f3  function : ' , msg)
	finally:
		print("f3's  finally")
	print('End  of  f3  function')
def  f4():
	try:
		print("f4  function")
		sys . exit()
	finally:
		print("f4's  finally")
	print('End  of  f4  function')
#End  of  all  the  functions
try:
	print('Begin')
	f1()
	f2()
	f3()
	f4()
	print('Hello')
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)
print('End  of  the  program')

'''
Begin
f1  function
ValueError  is  caught  outside :  Hyd
f1's  finally
End  of  the  program
'''

# Find  outputs (Home  work)
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')
		raise  Exception()
	except:
		print('Sec')
	finally:
		print("f1's  finally")
	print('End  of  f1  function')
#End  of  the  function
try:
	print('Begin')
	f1()
	print('Hello')
except  ValueError:
	print('Hello')
except  Exception:
	print('Recaught  Exception')
finally:
	print('Outside  finally')
print('End  of  the  program')

'''
Begin
f1  function
Caught  KeyError
f1's  finally
'Recaught  Exception
Outside  finally
End  of  the  program
'''

# Find outputs (Home  work)
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')
		raise  NameError()
	except  NameError:
		print('Sec')
	finally:
		print('f1 finally')
	print('End  of  f1 function')
#outside function
try:
	print('Begin')
	f1()
	print('Hello')
except ValueError:
	print('Hello')
except   Exception:
	print('Recaught  Exception')
except  NameError:
	print('Caught  Name Error  outside')
finally:
	print('Outside  finally')
print('End of the program')

'''
Begin
f1  function
Caught  KeyError
Sec
f1 finally
End  of  f1 function
Hello
Outside  finally
End of the program
'''

# Find  outputs  (Home   work)
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')
		raise   NameError()     # error because we should raise only error but not error cls object
	except  NameError:
		print('Sec')
	finally:
		print('f1 finally')
	print('End  of  f1 function')
#outside function
try:
	print('Begin')
	f1()
	print('Hello')
except  ValueError:
	print('Hello')
except   KeyError:
	print('Recaught  KeyError')
finally:
	print('Outside  finally')
print('End of the program')
'''
Begin
f1  function
Caught  KeyError
f1 finally
Outside  finally
'''

# Find  outputs  (Home  work)
try:
	print('try')
	print(7 / 0)
except:
	print('except')
else:
	print('else')
finally:
	print('finally')
print('End')

'''
try
except
finally
End
'''

# Find  outputs  (Home  work)
try:
	print('try')
except:
	print('except')
else:
	print('else')
finally:
	print('finally')
print('End')

'''
try
else
finally
End
'''


# Find  outputs   (Home  work)
try:
	print('try')
else:
    print('else')   # error because else without except should not be there
finally:
    print('finally')
print('End')



# Find  outputs   (Home  work)
try:
	print('try')
except:
	print('except')
else:
	print('else1')
else:
	print('else2')  # error as only one else should be there
finally:
	print('finally')
print('end')

''''
try
else1
finally
end
'''

# Identify  error   (Home  work)
try:
	print('try')
else:
	print('else')   # error as else should be in between except and finslly
except:
	print('except')     #
finally:
	print('finally')
print('end')

# Find  outputs   (Home  work)
try:
	print('try')
except:
	print('except')
if   10 > 20:
	print('if')
else:
	print('else')
	'''
	try
	else
	'''
# Find  outputs
def   f1():
	try:
		return  10 + '20'       # raises TypeError
	except:
		return  10 + 20  # returns 30
print(f1()) # prits 30


# Find  outputs
def   f1():
	try:
		return  10  # no error so 10 is returned
	except:
		return  20
	else:
		return  30
print(f1())     # 10n is  printed

# Find  outputs
def   f1():
	try:
		return  10 + '20'   # raises TypeError
	except:
		return  20  # 20 is returned
	else:
		return  30  # skipped
print(f1()) # 20 is printed

# Find  outputs
def   f1():
	try:
		pass    # no error
	except:
		return  20
	else:
		return  30  # so else suite is executed and returned 30
print(f1()) # 30 is printed


'''  (Home  work)
1) What  is  the  output  if  input  is  24 ?  --->

2) What  is  the  output  if  input  is  25 ?  --->
'''
try:
	x = eval(input('Enter  any  number  :  '))  
	assert    x >= 25 ,  'Hyd'
	print('Sec')
except  AssertionError  as   msg:
	print(msg)
print('End')

'''
x=24
assert stat is false
so assertion error is raised with message 'Hyd'
Hyd is printed
End

x=25
assert stat is true
so next statement is executed
Sec
End
'''

''' (Home  work)
1) What  is  the  output  when  input  is  24 ?  --->

2) What  is  the  output  when  input  is  25 ?  --->
'''
try:
	x = eval(input('Enter  any  number  :  '))
	assert   x >= 25
	print('Sec')
except  AssertionError   as    msg:
	print(msg)
print('End')
'''
x=24
assert stat is false
so assertion error is raised with message ''
nothing is printed
End

x=25
assert stat is true
so next statement is executed
Sec
End
'''

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
Outer try
Inner try
ZDE   of   inner   try
Inner  try  finally
ValueError  of  outer  try
Outer  try  finally
End  of  outer  try

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
outer try
inner try
ValueError  of  inner  try
Inner  try  finally
End  of  inner  try
outer try finally
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

outer try
inner try
inner try finally
IndexError  of  outer  try
outer try finally
end  of  outer  try
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
outer try
inner try
inner try finally
default except of outer try
Outer try finally
End of outer try

'''

#  Find  outputs (Home  work)
try:
	print('Outer  try')
	try:
		print('Inner  try')
		print(10 + '20')
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
outer try
Inner  try
Inner  try  finally
Outer  try  finally
type error is reported but not caught so program terminates
'''



# Find  outputs   (Home  work)
class   MyError(BaseException):
	def    __init__(self , y):
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
compute method is called with 10
10 is printed
Hello is printed
compute method is called with 30
30 is printed
MyError is raised so go to Myerror class constructor
Constructor is printed
go to except block with x=30 passed on
print Caught MyError outside : 30
End is printed

'''

# Find  outputs   (Home  work)
class   MyError(NameError):
	def    __init__(self):
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
compute function is called with 30
print 30
MyError is raised so go to Myerror class constructor
Constructor is printed
go to except block with x='' passed on
Caught  MyError  outside  :  
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
try block
1
2
3
as no error in try block else block will be executed
5
finally
6
outside finally
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
try 
1
error 
so go to except
4
6
outside finally
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
try
1
zde error
except
value error is reported
finally
6
'''

# Find  outputs (Home  work)
from  threading  import  *
def  f1():
	print(new.name)  #How  to  print  name  of  child  thread
# main  thread  executes  following  statements
new=Thread(target=f1)  #How  to  create  a  new  thread  with  name  'new'   and  target  f1
new.start()  #How  to  start  the  new  thread
x=current_thread()
print(x.name)   #How  to  print  name  of   main  thread

# Find  outputs (Home  work)
from threading import *
t1=Thread(name='Hyd') #How  to  create  a  thread  t1  with  name  'Hyd'
t2=Thread() #How  to  create  another  thread  t2  without  a  name
print(current_thread().name) #How  to  print  name  of  main  thread
print(t1.name) #How  to  print  name  of  thread  t1
print(t2.name) #How  to  print  name  of  thread  t2
current_thread().name='India' #How  to  modify  name  of  main  thread  to  'India'
t1.name='Sec' #How  to  modify  name  of  thread  t1  to  'Sec'
t2.name='Cyb' #How  to  modify  name  of  thread  t2  to  'Cyb'
print(current_thread().name) #How  to  print  name  of  main  thread
print(t1.name) #How  to  print  name  of  thread  t1
print(t2.name) #How  to  print  name  of  thread  t2
active_count() #How  to  print  number  of  threads  under  execution

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
thread t1 is created with name 'Hyd' and target function f1 with argument 10
thread t2 is created with name 'Sec' and target function f1 with argument 20
t1 and t2 are started
number of active threads is printed 3 
inside function while loop is always true so both threads keep printing their name and argument value indefinitely until interrupted
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
'''

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
thread t1 is created with name 'Rama' and target function f1 with argument 75
thread t2 is created with name 'Sita' and target function f1 with argument 50
t1 and t2 are started
funcction f1 is executed by both threads concurrently
ctr=0
while condition is true
    a random number x between 1 and 100 is generated
    ctr is incremented by 1
    if random number x is equal to n (75 for t1 and 50 for t2) loop breaks
	ctr is printed
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
new thread is created and registered with thread scheduler
main thread waits till new thread is completed
main thread is started after new thread is completed
'''

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
new thread is created and disp function is executed
main thread waits for 10 seconds or for new thread to complete	
then main thread continues its execution
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
start time is time before calling double() function
calling double() function
prints 2i within range 1 to 6
come back to main thread
calls square() function
prints i*i within range 1 to 6
come back to main thread
end time is time after calling square() function
prints total time taken to execute both functions
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
3 threads are created with names One, Two and Three and target function display
all 3 threads are started by main thread
all 3 threads execute display function concurrently
then main thread 1st waits for t1 to complete using join()
then main thread waits for t2 to complete using join()
then main thread waits for t3 to complete using join()
finally main thread prints active count as 1

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
3 threads are created with names One, Two and Three and target function display
all 3 threads are started by main thread
all 3 threads execute display function concurrently
list returns the list of all threads under execution usong enumerate function
main thread waits for t1 to complete
main thread waits for t3 to complete
main thread waits for t3 to complete
now only main thread is under execution so enumerate func returns main thread object
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
3 threads are created with names One, Two and Three and target function display
all 3 threads are started by main thread
all 3 threads execute display function concurrently
checking whether t1,t2,t3 are under execution or not
main thread waits for t1 to complete
main thread waits for t3 to complete
main thread waits for t3 to complete
now only main thread is under execution so enumerate func returns main thread object
so is_alive returns false for t1,t2,t3 beacuse all 3 are expired
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
2 threads are created target function table
all 2 threads are started by main thread
all 2 threads execute table function concurrently
t1 executes table method with n=7
t2 executes table method with n=4
so 4 table and 7 table are printed concurrently
'''



