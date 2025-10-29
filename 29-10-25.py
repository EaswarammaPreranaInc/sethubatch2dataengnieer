''' 
1) What  is  the  output  if  input  is  24 ?  --->Hyd <nextline> End

2) What  is  the  output  if  input  is  25 ?  --->Sec <nextline> End
'''
try:
	x = eval(input('Enter  any  number  :  '))
	assert  x >= 25 ,'Hyd' # when condition is false AssertionError is raised with the message
	print('Sec')
except  AssertionError  as   msg:
	print(msg)
print('End')


''' 
1) What  is  the  output  when  input  is  24 ?  --->empty string <nextline> End

2) What  is  the  output  when  input  is  25 ?  ---> sec <next line> End
'''
try:
	x = eval(input('Enter  any  number  :  '))
	assert   x >= 25 # msg is empty string
	print('Sec')
except  AssertionError   as    msg:
	print(msg)
print('End')



# Find  outputs   
try:
	print('Outer try')
	try:
		print('Inner try')
		print(7/0) # ZeroDivision error is raised
		int('Hyd') # skipped
		'Hyd'[5] # skipped
		eval('Hyd') # skipped
	except   ZeroDivisionError:
		print('ZDE of inner try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try')
	finally:
		print('Inner  try  finally')
	print('End  of  inner  try')
except   ValueError:
	print('ValueError of outer try')
except   IndexError:
	print('IndexError of outer try')
except:
	print('default  except  of  outer  try')
finally:
	print('Outer  try  finally')
print('End  of  outer  try')
'''
o/p:
Outer try
Inner try
ZDE of inner try
Inner  try  finally
ValueError of outer try
Outer  try  finally
End  of  outer  try
'''


#  Find outputs  
try:
	print('Outer  try')
	try:
		print('Inner  try')
		int('Hyd') # valueError is raise
		'Hyd'[5] # skipped
		eval('Hyd') # skipped
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
Outer  try
Inner  try
ValueError  of  inner  try
Inner  try  finally
End  of  inner  try
Outer try finally
End of outer try
'''


#Find outputs  
try:
	print('Outer try')
	try:
		print('Inner try')
		'Hyd'[3] # indexerror is raised
		eval('Hyd') # skipped
	except  ZeroDivisionError:
		print('ZDE of inner try')
		int('Ten')
	except  ValueError:
		print('ValueError of inner try ')
	finally:
		print('Inner try finally')
	print('End of inner try')
except  ValueError:
	print('ValueError of outer try')
except  IndexError: # as their is no indexerror in the corresponding except suite of inner try . The outer except is executed
	print('IndexError of outer try')
except:
	print('default except of outer try')
finally:
	print('Outer try finally')
print('End  of  outer  try')
'''
o/p:
Outer try
Inner try
Inner try finally
IndexError of outer try
Outer try finally
End  of  outer  try
'''


#  Find  outputs
try:
	print('Outer try')
	try:
		print('Inner try')
		eval('Hyd') # NameError is raised
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')
	finally:
		print('Inner  try  finally')
	print('End of inner try')
except  ValueError:
	print('ValueError of outer try')
except  IndexError:
	print('IndexError of outer try')
except: # default except suite is executed
	print('default except of outer  try')
finally:
	print('Outer  try  finally')
print('End  of  outer  try')
'''
o/p:
Outer try
Inner try
Inner  try  finally
default except of outer  try
Outer  try  finally
End  of  outer  try
'''

'''
#  Find  outputs 
try:
	print('Outer try')
	try:
		print('Inner try')
		print(10+'20') # TypeError is raised and it is not handled in the corresponding except suite of inner try nor outer try . so error is reported
	except  ZeroDivisionError:
		print('ZDE of inner try')
		int('Ten')
	except ValueError:
		print('ValueError of inner try ')
	finally:
		print('Inner  try  finally')
	print('End of inner try')
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
finally:
	print('Outer try finally')
print('End of outer try')
'''


# Find  outputs  
class   MyError(BaseException):
	def    __init__(self,y):
		self.a = y
		print('Constructor')
# End of  the class
def  compute(x):
	print(x)
	if  x > 20:
		raise  MyError(x) # error is raised so __init__ of MyError is executed
	print('Hello')
# End of  the functrion
try:
	compute(10)
	compute(30)
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ',msg)
print('End')
'''
o/p:
10
Hello
30
Constructor
Caught  MyError  outside  :   30
End
'''


# Find  outputs  
class   MyError(NameError):
	def    __init__(self):
		self.a =25
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
except  MyError  as  msg: # msg is empty string
	print('Caught  MyError  outside  :  ',msg)
print('End')
'''
o/p:
30
Constructor
Caught  MyError  outside  :
End
'''


# Find  outputs
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
o/p:
1
2
3
5
6
7
'''


# Find  outputs  
try:
	print(1)
	print(7/0)
	print(3)
except:
	print(4)
else: # it is not executed as there is an exception in try suite
	print(5)
finally:
	print(6)
print(7)
'''
o/p:
1
4
6
7
'''


# Find  outputs   
try:
	print(1)
	print(7/0) # ZeroDivisionError
	print(3)
except:
	pass
	#int('Two') # valueError and it is not handled
else:
    print(5)
finally:
    print(6)
print(7)# Find  outputs 
from  threading  import  *
def  f1():
	print(current_thread().name) # print  name  of  child  thread
# main  thread  executes  following  statements
new=Thread(target=f1) # create  a  new  thread  with  name  'new'   and  target  f1
new.start() # start  the  new  thread
print(current_thread().name) # print  name  of   main  thread


# Find  outputs 
t1=Thread(name='Hyd') # create  a  thread  t1  with  name  'Hyd'
t2=Thread() # create  another  thread  t2  without  a  name
print(current_thread().name)# print  name  of  main  thread
print(t1.name) # print  name  of  thread  t1
print(t2.name) # print  name  of  thread  t2
current_thread().name='India' # modify  name  of  main  thread  to  'India'
t1.name='sec' # modify  name  of  thread  t1  to  'Sec'
t2.name='cyb' # modify  name  of  thread  t2  to  'Cyb'
print(current_thread().name) # print  name  of  main  thread
print(t1.name) # print  name  of  thread  t1
print(t2.name) # print  name  of  thread  t2
print(active_count()) # print  number  of  threads  under  execution



# Find  outputs  
from threading import  *
def   f1(x):
	s=current_thread().name
	while True:
		print(s,' :' ,x) # infinite loop because condition is always true
#  main  thread  executes  following  statements
t1 = Thread(target = f1 , name = 'Hyd' , args =(10,))
t2 = Thread(target = f1 , name = 'Sec' , args =[20])
t1.start() # starts t1 thread
t2.start() # starts t2 thread
print(active_count()) # prints no,of thread under execution
print('Press  ctrl + break  or  Fn + b  to  stop ')



# Find  outputs 
from  threading  import  Thread,current_thread
from  random  import  randint
def   f1(n):
	ctr=0
	s = current_thread().name
	while  True:
		x = randint(1,100) 
		ctr += 1
		print(F'{s} guess {x} in attempt : {ctr}')
		if   x ==n:
			break
	#end of while loop
	print(F'{s} finish in {ctr} attempts')
# End  of  function   f1()
t1 = Thread(target = f1 ,args = [75] ,name = 'Rama')
t2 = Thread(target = f1 ,args = [50] ,name = 'Sita')
t1.start() # t1  executes  f1(75)
t2.start() # t2  executes  f1(50)
'''
o/p:
Rama guess 34 in attempt :1
Sita guess 23 in attempt :1
Rama guess 45 in attempt :2
Rama guess 12 in attempt :2 so on
'''


# Find  outputs 
from threading import *
def   disp():
	for i in range(10):
		print('new  thread')
#  child  thread  is  dead
new = Thread(target =disp)
new.start()
new.join() # main thread waits until the child thread is completely finished
for  i  in  range(10):
	print('main  thread')
# main   thread is  dead
'''
o/p:
10 times new thread
10 times main thread
'''



#  Find  outputs 
from  threading  import *
import  time
def   disp():
	for  i  in  range(10):
		print('new  thread')
		time.sleep(2) # pauses the thread execution for 2 seconds
new = Thread(target =disp)
new.start()
new.join(10) # main thread waits only 10 seconds for new to finish and after 10 seconds main thread resumes even though the child thread is in execution 
for  i  in  range(10): # cannot predict the output
	print('main  thread')
	


# Find  outputs 
from threading import *
import time
def   double():
	for i  in  range(1 , 7):
		print('Double : ',2 * i)
		time.sleep(1)  # pause thread execution for 1 second
def   square():
	for i in range(1 , 7):
		print('Square : ',i * i)
		time.sleep(1)  # pause thread execution for 1 second
start = time.time() # record start time
double()
square()
end = time.time() # record end time
print(end -start) # 6+6=12
'''
o/p:
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
12'''



# Find  outputs  
from  threading  import  *
import  time
def   display():
        name = current_thread().name
        print(name , 'is  started')
        time . sleep(3)
        print(name , 'is  ended')
# End  of  the  function
print(active_count())
t1 = Thread(target = display,name = 'One')
t2 = Thread(target = display,name = 'Two')
t3 = Thread(target = display,name = 'Three')
print(active_count()) # returns no,of threads currently running
t1.start()
t2.start()
t3.start()
print(active_count())
t1.join()
t2.join()
t3.join()
print(active_count())
'''
o/p:
1
1
One is  started
Two is  started
Three is  started
4
One is  ended
Two is  ended
Three is  ended
1
'''


# Find  outputs  
from  threading  import  *
import  time
def   disp():
	name = current_thread() . name
	print(name , 'is  started')
	time . sleep(3)
	print(name , 'is  ended')
# End  of  the  function
t1 = Thread(target = disp,name = 'One')
t2 = Thread(target = disp,name = 'Two')
t3 = Thread(target = disp,name = 'Three')
t1.start()
t2.start()
t3.start()
list = enumerate() # returns a list of all active therad objects at that moment
for  t  in   list:
	print(t.name)
t1.join()
t2.join()
t3.join()
list = enumerate()
for t in list:
	print(t.name)
'''
o/p:
One is  started
Two is  started
Three is  started
MainThread
One
Two
Three
One is  ended
Two is  ended
Three is  ended
MainThread
'''


# is_alive()  method   demo  program
from  threading  import *
import  time
def   disp():
	name =current_thread().name
	print(name ,'is started')
	time.sleep(3)
	print(name ,'is  ended')
t1 = Thread(target = disp , name ='One')
t2 = Thread(target = disp , name ='Two')
t3 = Thread(target = disp , name ='Three')
t1.start()
t2.start()
t3.start()
print(t1.is_alive()) # returns True if a thread is still running, otherwise False
print(t2.is_alive())
print(t3.is_alive())
t1.join()
t2.join()
t3.join()
print(t1.is_alive())
print(t2.is_alive())
print(t3.is_alive())
'''
o/p:
One is started
Two is started
Three is started
True
True
True
One is  ended
Two is  ended
Three is  ended
False
False
False
'''



#Find  outputs 
from  threading  import  *
import  time
def   table(n):
	print('Table : ',n)
	for i in range(1 , 11):
		print(F'{n} * {i} = {n * i}')
		time.sleep(1)
t1 = Thread(target = table , args =(7,))
t2 = Thread(target = table , args =(4,))
t1.start()
t2.start() # both thread starts simultaneoulsy so, output cannot be predicted#Find  outputs  
try:
	raise  ArithmeticError
except   ZeroDivisionError:
	print('Zero Division  Error')
except   ArithmeticError: # child error except suite is not executed when parent error is raise
	print('Arithmetic Error')
print('End')
'''
o/p:
Arithmetic Error
End
'''


#Find outputs 
def  f1():
	try:
		print('f1  function')
		raise  ValueError('Hyd') # exception is raised
		print('Hi') # skipped
	finally:
		print("f1's  finally")
	print('End  of  f1  function') # skipped
def  f2():
	try:
		print('f2  function')
		return # control goes out of the function
		print('Hello') # skipped
	finally:
		print("f2's  finally")
	print('End  of  f2  function') # skipped 
def  f3():
	try:
		print('f3  function')
		raise   KeyError(25) # raises exception
		print('Hello') # skipped
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
		print("f4's  finally") # before exit() terminates the program finally block is executed
	print('End of f4 function')
# End  of  all  the  functions
try:
	print('Begin')
	f1()
	print('Hello')
except  ValueError  as  msg:
	print('ValueError is caught outside :  ' , msg)
f2()
f3()
try:
	f4()
finally:
		print('Outside finally')
print('End of the program')
'''
o/p:
Begin
f1  function
f1's  finally
ValueError is caught outside : Hyd
f2  function
f2's  finally
f3  function
Caught  by  f3  function : 25
f3's  finally
End of f3 function
f4 function
f4's  finally
Outside finally
'''


#Find  outputs  
import sys
def  f1():
	try:
		print('f1  function')
		raise  ValueError('Hyd') # raises exception
		print('Hi') # skipped
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
o/p:
Begin
f1  function
f1's  finally
ValueError  is  caught  outside :   Hyd
End  of  the  program
'''


#Find  outputs 
def  f1():
	try:
		print('f1  function')
		raise  KeyError() # raises keyerror
		print('Hyd') # skipped
	except  KeyError:
		print('Caught  KeyError')
		raise  Exception()
	except:
		print('Sec')
	finally:
		print("f1's  finally") # executes finally
	print('End  of  f1  function')
#End  of  the  function
try:
	print('Begin')
	f1()
	print('Hello') # skipped
except  ValueError:
	print('Hello')
except  Exception:
	print('Recaught  Exception')
finally:
	print('Outside  finally')
print('End  of  the  program')
'''
o/p:
Begin
f1  function
Caught  KeyError
f1's  finally
Recaught  Exception
Outside  finally
End  of  the  program
'''


#Find outputs 
def  f1():
	try:
		print('f1  function')
		raise  KeyError() # raises Keyerror
		print('Hyd') # skipped
	except  KeyError:
		print('Caught  KeyError')
		raise  NameError() # raises Nameerror
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
o/p:
Begin
f1  function
Caught  KeyError
f1 finally
Recaught  Exception
Outside  finally
End of the program
'''


#Find  outputs  
def  f1():
	try:
		print('f1  function')
		raise  KeyError() # raises keyerror
		print('Hyd') # skipped
	except  KeyError:
		print('Caught  KeyError')
		#raise   NameError() # error : because NameError is no handled in any of the corresponding except suite in outer try
	except  NameError:
		print('Sec')
	finally:
		print('f1 finally') # executes finally
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



#Find  outputs  
try:
	print('try')
	print(7/0)
except:
	print('except')
else:
	print('else')
finally:
	print('finally')
print('End')
'''
o/p:
try
except
finally
End
'''


#Find outputs 
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
o/p:
try
else
finally
End
'''

'''
#Find outputs 
try:
	print('try')
#else: # error : cannot write else without except suite
    print('else')
finally:
    print('finally')
print('End')
'''


# Find  outputs   
try:
	print('try')
except:
	print('except')
else:
	print('else1')
#else: # error cannot write more then one else
	print('else2')
finally:
	print('finally')
print('end')



# Identify  error   
try:
	print('try')
#else: # else before except is not allowed
	print('else')
except:
	print('except')
finally:
	print('finally')
print('end')


#Find outputs   
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
		return  10+'20' # error so, except suite is executed
	except:
		return  10+20 # 30
print(f1())



# Find  outputs
def   f1():
	try:
		return  10 # as return statement is executed else block is not executed 
	except:
		return  20
	else:
		return  30
print(f1()) # 10


#Find  outputs
def   f1():
	try:
		return  10+'20'
	except:
		return  20 # 20 : as error is raised except suite is executed
	else:
		return  30
print(f1())



# Find  outputs
def   f1():
	try:
		pass
	except:
		return  20
	else:
		return  30 # no error is raised in try suite . so, else block is executed
print(f1()) # 30

# Find  outputs
def   f1():
	try:
		return  10
	except:
		return   20
	else:
		return  30
	finally:
		return  40 # finally block is executed and it returns 40
print(f1()) # 40 