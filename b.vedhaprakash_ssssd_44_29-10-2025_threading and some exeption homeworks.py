------------------------- homeworks on 29/10/2025 --------------------

-----------------------------------------------
# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function') # f1 function
		raise  ValueError('Hyd') 
		print('Hi')
	finally:
		print("f1's  finally") # f1's finally 
	print('End  of  f1  function') # skipped 
def  f2():
	try:
		print('f2  function') # f2 function 
		return
		print('Hello')
	finally:
		print("f2's  finally") # f2's finally 
	print('End  of  f2  function')
def  f3():
	try:
		print('f3  function') # f3 function 
		raise   KeyError(25)
		print('Hello')
	except KeyError as  msg:
		print('Caught  by  f3  function :  ' , msg) # caught by f3 function : 25
	finally:
		print("f3's  finally") # f3's finally 
	print('End of f3 function') # end of f3 function 
def  f4():
	try:
		print('f4 function') # f4 function 
		exit()
	finally:
		print("f4's  finally")
	print('End of f4 function')
# End  of  all  the  functions
try:
	print('Begin') # begin 
	f1()
	print('Hello')
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg) # value error is caught outside : Hyd 
f2()
f3()
try:
	f4()
finally:
		print('Outside  finally') # outside finally 
print('End  of  the  program')

-----------------------------------------------------------------------------------------------------
import sys
def  f1():
	try:
		print('f1  function') # f1 function
		raise  ValueError('Hyd')
		print('Hi') # skipped
	finally:
		print("f1's  finally") # f1's finally
	print('End  of  f1  function') # skipped
def  f2():
	try:
		print('f2  function') # skipped
		return
		print('Hello') # skipped
	finally:
		print("f2's  finally") # skipped
	print('End  of  f2  function') # skipped
def  f3():
	try:
		print('f3  function') # skipped
		raise   KeyError(25)
		print('Hello') # skipped
	except  KeyError  as  msg:
		print('Caught  by  f3  function : ' , msg) # skipped
	finally:
		print("f3's  finally") # skipped
	print('End  of  f3  function') # skipped
def  f4():
	try:
		print("f4  function") # skipped
		sys . exit()
	finally:
		print("f4'ss  finally") # skipped
	print('End  of  f4  function') # skipped
#End  of  all  the  functions
try:
	print('Begin') # Begin
	f1()
	f2() # skipped
	f3() # skipped
	f4() # skipped
	print('Hello') # skipped
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg) # ValueError is caught outside : Hyd
print('End  of  the  program') # End of the program
-----------------------------------------------------------------------------------------------------------------------

# Find  outputs (Home  work)
def  f1():
	try:
		print('f1  function') # f1  function
		raise  KeyError()
		print('Hyd') # skipped
	except  KeyError:
		print('Caught  KeyError') # Caught  KeyError
		raise  Exception() # A new Exception is raised
	except:
		print('Sec') # skipped
	finally:
		print("f1's  finally") # f1's  finally
	print('End  of  f1  function') # skipped (due to raise in except)
#End  of  the  function
try:
	print('Begin') # Begin
	f1() # Function is called
	print('Hello') # skipped (f1 raised an Exception)
except  ValueError:
	print('Hello') # skipped (Exception is not a ValueError)
except  Exception:
	print('Recaught  Exception') # Recaught  Exception
finally:
	print('Outside  finally') # Outside  finally
print('End  of  the  program') # End  of  the  program
----------------------------------------------------------------------------------------------------------

# Find  outputs (Home  work)
def  f1():
	try:
		print('f1  function') # f1  function
		raise  KeyError()
		print('Hyd') # skipped
	except  KeyError:
		print('Caught  KeyError') # Caught  KeyError
		raise  Exception() # A new Exception is raised
	except:
		print('Sec') # skipped
	finally:
		print("f1's  finally") # f1's  finally
	print('End  of  f1  function') # skipped (due to raise in except)
#End  of  the  function
try:
	print('Begin') # Begin
	f1() # Function is called
	print('Hello') # skipped (f1 raised an Exception)
except  ValueError:
	print('Hello') # skipped (Exception is not a ValueError)
except  Exception:
	print('Recaught  Exception') # Recaught  Exception
finally:
	print('Outside  finally') # Outside  finally
print('End  of  the  program') # End  of  the  program

-----------------------------------------------------------------------------------

# Find outputs (Home  work)
def  f1():
	try:
		print('f1  function') # f1  function
		raise  KeyError()
		print('Hyd') # skipped
	except  KeyError:
		print('Caught  KeyError') # Caught  KeyError
		raise  NameError() # A new NameError is raised
	except  NameError:
		print('Sec') # skipped
	finally:
		print('f1 finally') # f1 finally
	print('End  of  f1 function') # skipped (due to raise in except)
#outside function
try:
	print('Begin') # Begin
	f1() # Function is called
	print('Hello') # skipped (f1 raised a NameError)
except ValueError:
	print('Hello') # skipped
except   Exception: # NameError is a subclass of Exception, so this block catches it
	print('Recaught  Exception') # Recaught  Exception
except  NameError:
	print('Caught  Name Error  outside') # skipped (caught by Exception block first)
finally:
	print('Outside  finally') # Outside  finally
print('End of the program') # End of the program
-------------------------------------------------------------------------------------

# Find  outputs  (Home  work)
try:
	print('try') # try
	print(7 / 0) # Raises ZeroDivisionError
except:
	print('except') # except
else:
	print('else') # skipped (exception occurred)
finally:
	print('finally') # finally
print('End') # End
--------------------------------------

# Find  outputs  (Home  work)
try:
	print('try') # try
except:
	print('except') # skipped (no exception)
else:
	print('else') # else
finally:
	print('finally') # finally
print('End') # End
---------------------------------------

# Find  outputs   (Home  work)
try:
	print('try')
else:
    print('else')
finally:
    print('finally')
print('End')
# else without except 
-----------------------------------------
# Find  outputs   (Home  work)
try:
	print('try')
except:
	print('except')
else:
	print('else1')
else:
	print('else2')
finally:
	print('finally')
print('end')
# multiple else blocks
-------------------------------------
# Identify  error   (Home  work)
try:
	print('try')
else:
	print('else')
except:
	print('except')
finally:
	print('finally')
print('end')
# except must be after try
------------------------------------------

# Find  outputs   (Home  work)
try:
	print('try') # try
except:
	print('except') # skipped
if   10 > 20: # False
	print('if') # skipped
else:
	print('else') # else
-----------------------------

# Find  outputs
def   f1():
	try:
		return  10 + '20' # Raises TypeError
	except:
		return  10 + 20 # returns 30
print(f1()) # 30
------------------------------------
# Find  outputs
def   f1():
	try:
		return  10 # returns 10
	except:
		return  20 # skipped
	else:
		return  30 # skipped (because 'try' block returned)
print(f1()) # 10
--------------------------------
# Find  outputs
def   f1():
	try:
		return  10 + '20' # Raises TypeError
	except:
		return  20 # returns 20
	else:
		return  30 # skipped (exception occurred)
print(f1()) # 20
----------------------------------
# Find  outputs
def   f1():
	try:
		pass # Completes successfully
	except:
		return  20 # skipped
	else:
		return  30 # returns 30
print(f1()) # 30
------------------------------
# Find  outputs
def   f1():
	try:
		return  10 # This 'return' is superseded by 'finally'
	except:
		return   20 # skipped
	else:
		return  30 # skipped
	finally:
		return  40 # This 'return' overwrites any previous return
print(f1()) # 40
--------------------------------------------

'''  (Home  work)
1) What  is  the  output  if  input  is  24 ?  --->
# Enter  any  number  :  24
# Hyd
# End
2) What  is  the  output  if  input  is  25 ?  --->
# Enter  any  number  :  25
# Sec
# End
'''
try:
	x = eval(input('Enter  any  number  :  ')) # Case 1: 24, Case 2: 25
	assert   x >= 25 ,  'Hyd' # Case 1: Fails, raises AssertionError('Hyd'). Case 2: Passes.
	print('Sec') # Case 1: skipped. Case 2: Sec
except  AssertionError  as   msg:
	print(msg) # Case 1: Hyd. Case 2: skipped
print('End') # End
-------------------------------------------------

''' (Home  work)
1) What  is  the  output  when  input  is  24 ?  --->
# Enter  any  number  :  24
# (empty line is printed)
# End
2) What  is  the  output  when  input  is  25 ?  --->
# Enter  any  number  :  25
# Sec
# End
'''
try:
	x = eval(input('Enter  any  number  :  ')) # Case 1: 24, Case 2: 25
	assert   x >= 25 # Case 1: Fails, raises AssertionError(). Case 2: Passes.
	print('Sec') # Case 1: skipped. Case 2: Sec
except  AssertionError   as   msg:
	print(msg) # Case 1: (prints empty line, as msg has no message). Case 2: skipped
print('End') # End
---------------------------------------------------------
# Find  outputs   (Home  work)
try:
	print('Outer   try') # Outer   try
	try:
		print('Inner   try') # Inner   try
		print(7 / 0) # Raises ZeroDivisionError
		int('Hyd') # skipped
		'Hyd'[5] # skipped
		eval('Hyd') # skipped
	except   ZeroDivisionError:
		print('ZDE   of   inner   try') # ZDE   of   inner   try
		int('Ten') # Raises ValueError
	except  ValueError:
		print('ValueError  of  inner  try') # skipped
	finally:
		print('Inner  try  finally') # Inner  try  finally
	print('End  of  inner  try') # skipped (due to ValueError in except)
except   ValueError:
	print('ValueError  of  outer  try') # ValueError  of  outer  try
except   IndexError:
	print('IndexError  of  outer  try') # skipped
except:
	print('default  except  of  outer  try') # skipped
finally:
	print('Outer  try  finally') # Outer  try  finally
print('End  of  outer  try') # End  of  outer  try
------------------------------------------------------
#  Find outputs   (Home  work)
try:
	print('Outer  try') # Outer  try
	try:
		print('Inner  try') # Inner  try
		int('Hyd') # Raises ValueError
		'Hyd'[5] # skipped
		eval('Hyd') # skipped
	except  ZeroDivisionError:
		print('ZDE  of  inner  try') # skipped
		int('Ten') # skipped
	except  ValueError:
		print('ValueError  of  inner  try ') # ValueError  of  inner  try 
	finally:
		print('Inner  try  finally') # Inner  try  finally
	print('End  of  inner  try') # End  of  inner  try
except  ValueError:
	print('ValueError  of  outer try') # skipped
except  IndexError:
	print('IndexError of outer try') # skipped
except:
	print('default except of outer try') # skipped
finally:
	print('Outer try finally') # Outer try finally
print('End of outer try') # End of outer try
----------------------------------------------------------

#  Find outputs   (Home  work)
try:
	print('Outer  try') # Outer  try
	try:
		print('Inner  try') # Inner  try
		'Hyd'[3] # Raises IndexError
		eval('Hyd') # skipped
	except  ZeroDivisionError:
		print('ZDE  of  inner  try') # skipped
		int('Ten') # skipped
	except  ValueError:
		print('ValueError  of  inner  try ') # skipped
	finally:
		print('Inner  try  finally') # Inner  try  finally
	print('End  of  inner  try') # skipped (due to unhandled IndexError)
except  ValueError:
	print('ValueError  of  outer  try') # skipped
except  IndexError:
	print('IndexError  of  outer  try') # IndexError  of  outer  try
except:
	print('default except of outer try') # skipped
finally:
	print('Outer try finally') # Outer try finally
print('End  of  outer  try') # End  of  outer  try
-----------------------------------------------------

#  Find  outputs (Home  work)
try:
	print('Outer  try') # Outer  try
	try:
		print('Inner  try') # Inner  try
		eval('Hyd') # Raises NameError
	except  ZeroDivisionError:
		print('ZDE  of  inner  try') # skipped
		int('Ten') # skipped
	except ValueError:
		print('ValueError  of   inner  try ') # skipped
	finally:
		print('Inner  try  finally') # Inner  try  finally
	print('End of inner try') # skipped (due to unhandled NameError)
except  ValueError:
	print('ValueError  of  outer try') # skipped
except  IndexError:
	print('IndexError of outer try') # skipped
except:
	print('default  except  of  outer  try') # default  except  of  outer  try
finally:
	print('Outer  try  finally') # Outer  try  finally
print('End  of  outer  try') # End  of  outer  try
------------------------------------------------

#  Find  outputs (Home  work)
try:
	print('Outer  try') # Outer  try
	try:
		print('Inner  try') # Inner  try
		print(10 + '20') # Raises TypeError
	except  ZeroDivisionError:
		print('ZDE  of  inner  try') # skipped
		int('Ten') # skipped
	except ValueError:
		print('ValueError  of   inner  try ') # skipped
	finally:
		print('Inner  try  finally') # Inner  try  finally
	print('End of inner try') # skipped (due to unhandled TypeError)
except  ValueError:
	print('ValueError  of  outer try') # skipped
except  IndexError:
	print('IndexError of outer try') # skipped
finally:
	print('Outer  try  finally') # Outer  try  finally
print('End  of  outer  try') # skipped (unhandled TypeError causes program to crash)
# Traceback (most recent call last):
#   File "...", line 18, in <module>
#     print(10 + '20')
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
---------------------------------------------------
# Find  outputs   (Home  work)
class   MyError(BaseException):
	def   __init__(self , y):
		self . a = y
		print('Constructor') # Constructor
# End of  the class
def  compute(x):
	print(x) # 10 (first call), 30 (second call)
	if  x > 20:
		raise   MyError(x) # skipped (first call), raises MyError(30) (second call)
	print('Hello') # Hello (first call), skipped (second call)
# End of  the functrion
try:
	compute(10) # 10, Hello
	compute(30) # 30, Constructor
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ' ,  msg) # Caught  MyError  outside  :  30
print('End') # End
------------------------------------------------------

# Find  outputs   (Home  work)
class   MyError(NameError):
	def   __init__(self):
		self . a =  25
		print('Constructor') # Constructor
# End of  the class
def  compute(x):
	print(x) # 30
	if  x > 20:
		raise   MyError() # raises MyError
	print('Hello') # skipped
#end of  the functrion
try:
	compute(30) # 30, Constructor
	compute(10) # skipped
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ' ,  msg) # Caught  MyError  outside  :  (prints empty string after colon)
print('End') # End
-------------------------------------------------
# Find  outputs (Home  work)
try:
	print(1) # 1
	print(2) # 2
	print(3) # 3
except:
	print(4) # skipped
else:
	print(5) # 5
finally:
	print(6) # 6
print(7) # 7
--------------------------------------


# Find  outputs   (Home  work)
try:
	print(1) # 1
	print(7 / 0) # Raises ZeroDivisionError
	print(3) # skipped
except:
	print(4) # 4
else:
	print(5) # skipped
finally:
	print(6) # 6
print(7) # 7

------------------------------------
# Find  outputs   (Home  work)
try:
	print(1) # 1
	print(7 / 0) # Raises ZeroDivisionError
	print(3) # skipped
except:
	int('Two') # Raises ValueError
else:
        print(5) # skipped
finally:
        print(6) # 6
print(7) # skipped 

--------------------------------------
# Find  outputs (Home  work)
from  threading  import  *
def  f1():
	# How  to  print  name  of  child  thread
	print(current_thread().name) # new
# main  thread  executes  following  statements
# How  to  create  a  new  thread  with  name  'new'   and  target  f1
t = Thread(target=f1, name='new')
# How  to  start  the  new  thread
t.start()
# How  to  print  name  of   main  thread
print(current_thread().name) # MainThread

# Note: The output is non-deterministic. It could be:
# new
# MainThread
# OR
# MainThread
# new
---------------------------------------------------------

# Find  outputs (Home  work)
from threading import *
# How  to  create  a  thread  t1  with  name  'Hyd'
t1 = Thread(name='Hyd')
# How  to  create  another  thread  t2  without  a  name
t2 = Thread()
# How  to  print  name  of  main  thread
print(current_thread().name) # MainThread
# How  to  print  name  of  thread  t1
print(t1.name) # Hyd
# How  to  print  name  of  thread  t2
print(t2.name) # Thread-1 (or some other number)
# How  to  modify  name  of  main  thread  to  'India'
current_thread().name = 'India'
# How  to  modify  name  of  thread  t1  to  'Sec'
t1.name = 'Sec'
# How  to  modify  name  of  thread  t2  to  'Cyb'
t2.name = 'Cyb'
# How  to  print  name  of  main  thread
print(current_thread().name) # India
# How  to  print  name  of  thread  t1
print(t1.name) # Sec
# How  to  print  name  of  thread  t2
print(t2.name) # Cyb
# How  to  print  number  of  threads  under  execution
print(active_count()) # 1 (t1 and t2 were never started)
---------------------------------------------------------------------
# Find  outputs  (Home  work)
from  threading  import  *
def   f1(x):
	s = current_thread() . name
	while   True: # This is an infinite loop
		print(s , ' : ' , x) # Hyd : 10 (or Sec : 20, interleaved)
#  main  thread  executes  following  statements
t1 = Thread(target = f1 , name = 'Hyd' , args = (10,))
t2 = Thread(target = f1 , name = 'Sec' , args =  [20])
t1 . start()
t2 . start()
print(active_count()) # 3
print('Press  ctrl + break  or  Fn + b  to  stop ') # Press  ctrl + break  or  Fn + b  to  stop

# The output will be 'Hyd : 10' and 'Sec : 20' printed
# infinitely and interleaved, e.g.:
# 3
# Press  ctrl + break  or  Fn + b  to  stop 
# Hyd : 10
# Sec : 20
# Hyd : 10
# Hyd : 10
# Sec : 20
# ... (forever)

'''
1) Which  of  the  following  are  valid ?
    args = [10]  ---> Valid
    args = (10,) ---> Valid
    args = {10}  ---> Valid (a set is iterable)
    args = 10    ---> Invalid
    args = 10.8  ---> Invalid
    args = '10'  ---> Valid, but f1(x) will get '1' (f1('1') and f1('0') will be called, causing a TypeError)
    args = (10)  ---> Invalid (this is just the integer 10, not a tuple)

2) In  general,  args  argument  of  Thread  constructor  can  be  any  sequence
# (True, it can be any iterable.)
'''
--------------------------------------------------------------------------------------------------------------------------------------------

# Find  outputs (Home  work)
from  threading  import  Thread , current_thread
from  random  import  randint
def   f1(n):
	ctr = 0
	s = current_thread() . name
	while  True:
		x = randint(1 , 100)
		ctr += 1
		print(F'{s}  guess  {x}   in  attempt  :  {ctr}') # e.g., Rama  guess  42   in  attempt  :  1
		if   x ==  n:
			break
	#end of while loop
	print(F'{s}  finish  in  {ctr}  attempts') # e.g., Rama  finish  in  87  attempts
# End  of  function   f1()
t1 = Thread(target = f1 , args = [75] , name = 'Rama')
t2 = Thread(target = f1 , args = [50] , name = 'Sita')
t1 . start() #  t1  executes  f1(75)
t2 . start() #  t2  executes  f1(50)

# The output is non-deterministic.
# It will be an interleaved series of guesses from 'Rama' and 'Sita',
# until 'Rama' guesses 75 and 'Sita' guesses 50.
# e.g.:
# Rama  guess  12   in  attempt  :  1
# Sita  guess  88   in  attempt  :  1
# Rama  guess  75   in  attempt  :  2
# Rama  finish  in  2  attempts
# Sita  guess  3   in  attempt  :  2
# ... (Sita continues until she guesses 50)
--------------------------------------------------------------------------------

# Find  outputs (Home  work)
from threading import *
def   disp():
	for  i  in  range(10):
		print('new  thread') # new  thread (prints 10 times)
#  child  thread  is  dead
new = Thread(target = disp)
new . start()
new . join() # Main thread waits for 'new' to finish
for  i  in  range(10):
	print('main  thread') # main  thread (prints 10 times, *after* child finishes)
# main   thread is  dead

-------------------------------------------------
#  Find  outputs (Home  work)
from  threading  import *
import  time
def   disp():
	for  i  in  range(10):
		print('new  thread') # new  thread (prints, then sleeps 2s)
		time . sleep(2)
new = Thread(target = disp)
new . start()
new . join(10) # Main thread waits for a *maximum* of 10 seconds
# In 10s, the child thread will print 5 times (at t=0, 2, 4, 6, 8)
# At t=10s, join() times out and the main thread starts.
# The child thread *continues* to run in the background.
for  i  in  range(10):
	print('main  thread') # main  thread (prints 10 times, quickly)

# The output will be interleaved.
# e.g.:
# new  thread (t=0)
# new  thread (t=2)
# new  thread (t=4)
# new  thread (t=6)
# new  thread (t=8)
# main  thread (t=10)
# main  thread (t=10)
# ... (all 10 'main thread' lines)
# new  thread (t=10)
# new  thread (t=12)
# ... (child finishes)

-----------------------------------------------------
# Find  outputs (Home  work)
from threading import *
import time
def   double():
	for   i  in  range(1 , 7):
		print('Double : ' , 2 * i) # Double : 2, Double : 4, ... Double : 12
		time . sleep(1) # sleeps 1s
def   square():
	for   i  in   range(1 , 7):
		print('Square : ' , i * i) # Square : 1, Square : 4, ... Square : 36
		time . sleep(1) # sleeps 1s
start = time . time()
double() # Runs sequentially. Takes ~6 seconds.
square() # Runs *after* double. Takes ~6 seconds.
end = time . time()
print(end - start) # 12.0... (a number around 12)
--------------------------------------------------
# Find  outputs  (Home  work)
from  threading  import  *
import  time
def   display():
        name = current_thread() . name
        print(name , ' is  started') # e.g., One  is  started
        time . sleep(3)
        print(name , ' is  ended') # e.g., One  is  ended
# End  of  the  function
print(active_count()) # 1
t1 = Thread(target = display , name = 'One')
t2 = Thread(target = display , name = 'Two')
t3 = Thread(target = display , name = 'Three')
print(active_count()) # 1 (threads are not started yet)
t1 . start()
t2 . start()
t3 . start()
print(active_count()) # 4 (MainThread + One + Two + Three)
t1 . join()
t2 . join()
t3 . join() # Main thread waits here until all 3 are done
print(active_count()) # 1

# Full output (start/end order is non-deterministic):
# 1
# 1
# 4
# One  is  started
# Two  is  started
# Three  is  started
# (after ~3 seconds)
# Two  is  ended
# One  is  ended
# Three  is  ended
# 1
-------------------------------------------------------
# Find  outputs  (Home  work)
from  threading  import  *
import  time
def   disp():
	name = current_thread() . name
	print(name , ' is  started') # e.g., One  is  started
	time . sleep(3)
	print(name , '  is  ended') # e.g., One  is  ended
# End  of  the  function
t1 = Thread(target = disp , name = 'One')
t2 = Thread(target = disp , name = 'Two')
t3 = Thread(target = disp , name = 'Three')
t1 . start()
t2 . start()
t3 . start()
list = enumerate() # Gets a list of active threads
for  t  in   list:
	print(t . name) # Prints 'MainThread', 'One', 'Two', 'Three' (order may vary)
t1 . join()
t2 . join()
t3 . join() # Main thread waits
list = enumerate() # Gets list of active threads
for  t  in  list:
	print(t . name) # Prints 'MainThread' (children are dead)

# Full output (start/end/list order is non-deterministic):
# One  is  started
# Two  is  started
# Three  is  started
# MainThread
# One
# Two
# Three
# (after ~3 seconds)
# One   is  ended
# Three   is  ended
# Two   is  ended
# MainThread

-----------------------------------------------------------
# is_alive()  method   demo  program
from  threading  import *
import  time
def   disp():
	name =  current_thread() . name
	print(name , 'is   started') # e.g., One is   started
	time . sleep(3)
	print(name , '   is    ended') # e.g., One    is    ended
t1 = Thread(target = disp , name = 'One')
t2 = Thread(target = disp , name = 'Two')
t3 = Thread(target = disp , name = 'Three')
t1 . start()
t2 . start()
t3 . start()
print(t1 . is_alive()) # True
print(t2 . is_alive()) # True
print(t3 . is_alive()) # True
t1 . join()
t2 . join()
t3 . join() # Main thread waits
print(t1 . is_alive()) # False
print(t2 . is_alive()) # False
print(t3 . is_alive()) # False

# Full output (start/end order is non-deterministic):
# One is   started
# Two is   started
# Three is   started
# True
# True
# True
# (after ~3 seconds)
# One    is    ended
# Three    is    ended
# Two    is    ended
# False
# False
# False
-----------------------------------------------

# Find  outputs (Home  work)
from  threading  import  *
import  time
def   table(n):
	print('Table  :  ' , n) # Table  :  7 (or 4)
	for i  in  range(1 , 11):
		print(F'{n}  * {i}   =   {n * i}') # e.g., 7  * 1   =   7
		time . sleep(1)
t1 = Thread(target = table , args = (7,))
t2 = Thread(target = table , args = (4,))
t1 . start()
t2 . start()

# The output will be the 7-times table and 4-times table,
# interleaved. The lines for each step (e.g., 7*1 and 4*1)
# will appear at roughly the same time, but their
# specific order is non-deterministic.
# Table  :  7
# 7  * 1   =   7
# Table  :  4
# 4  * 1   =   4
# (1s wait)
# 7  * 2   =   14
# 4  * 2   =   8
# (1s wait)
# ...
-------------------------------------------------------------------
