#  Find  outputs  (Home  work)
try:
	raise  ArithmeticError
except   ZeroDivisionError:
	print('Zero Division  Error')
except   ArithmeticError:
	print('Arithmetic Error')  #  Arithmetic  Error
print('End')  #  End


'''
Is  child  error  except  suite  executed  when  parent  error   raised ?  ---> 
'''


# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')  #  f1  function
		raise  ValueError('Hyd')
		print('Hi')
	finally:
		print("f1's  finally")
	print('End  of  f1  function')
def  f2():
	try:
		print('f2  function')  #  f2  function
		return
		print('Hello')
	finally:
		print("f2's  finally")  #  f2's  finally
	print('End  of  f2  function')
def  f3():
	try:
		print('f3  function')  #  f3  function
		raise   KeyError(25)
		print('Hello')
	except KeyError as  msg:
		print('Caught  by  f3  function :  ' , msg)  #  Caught  by  f3  function :   25
	finally:
		print("f3's  finally")  # f3's  finally
	print('End of f3 function')  #  End of f3 function
def  f4():
	try:
		print('f4 function')  # f4 function
		exit()
	finally:
		print("f4's  finally")  #   f4's  finally
	print('End of f4 function')  #  End of f4 function
# End  of  all  the  functions
try:
	print('Begin')  #  Begin
	f1()
	print('Hello')
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)  #  ValueError  is  caught  outside :   Hyd
f2()
f3()
try:
	f4()
finally:
		print('Outside  finally')  #  Outside  finally
print('End  of  the  program')  #  End  of  the  program




# Find  outputs  (Home  work)
import sys
def  f1():
	try:
		print('f1  function')  # f1  function
		raise  ValueError('Hyd')
		print('Hi')
	finally:
		print("f1's  finally")  #  f1's  finally
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
	print('Begin')  #  Begin
	f1()
	f2()
	f3()
	f4()
	print('Hello')  
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)  #  ValueError  is  caught  outside :   Hyd
print('End  of  the  program')  #  End  of  the  program



# Find  outputs (Home  work)
def  f1():
	try:
		print('f1  function')  # f1  function
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')  #  Caught  KeyError
		raise  Exception()
	except:
		print('Sec')
	finally:
		print("f1's  finally")  #  f1's  finally
	print('End  of  f1  function')
#End  of  the  function
try:
	print('Begin')  #  Begin
	f1()
	print('Hello')
except  ValueError:
	print('Hello')
except  Exception:
	print('Recaught  Exception')  #  Recaught  Exception
finally:
	print('Outside  finally')  # Outside  finally
print('End  of  the  program')  # End  of  the  program



# Find outputs (Home  work)
def  f1():
	try:
		print('f1  function')  # f1  function
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')  #  Caught  KeyError
		raise  NameError()
	except  NameError:
		print('Sec')
	finally:
		print('f1 finally')  #  f1 finally
	print('End  of  f1 function')
#outside function
try:
	print('Begin')  #  Begin
	f1()
	print('Hello')
except ValueError:
	print('Hello')
except   Exception:
	print('Recaught  Exception')  #  Recaught  Exception
except  NameError:
	print('Caught  Name Error  outside')
finally:
	print('Outside  finally')  #  Outside  finally
print('End of the program')  # End of the program




# Find  outputs  (Home   work)
def  f1():
	try:
		print('f1  function')  # f1  function
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')  #  Caught  KeyError
		raise   NameError()  #  NameError Reports
	except  NameError:
		print('Sec')
	finally:
		print('f1 finally')  #  f1 finally
	print('End  of  f1 function')
#outside function
try:
	print('Begin')  # Begin
	f1()
	print('Hello')
except  ValueError:
	print('Hello')
except   KeyError:
	print('Recaught  KeyError')
finally:
	print('Outside  finally')  #  Outside  finally
print('End of the program')



# Find  outputs  (Home  work)
try:
	print('try')  #  try
	print(7 / 0)
except:
	print('except')  #  except
else:
	print('else')
finally:
	print('finally')  #  finally
print('End')  #  End



# Find  outputs  (Home  work)
try:
	print('try')  #  try
except:
	print('except')
else:
	print('else')  #  else
finally:
	print('finally')  #  finally
print('End')  #  End



# Find  outputs   (Home  work)
try:
	print('try')  #  try
else:
    print('else') #  Error due to wiuthout except block used else
finally:
    print('finally')
print('End')



# Find  outputs   (Home  work)
try:
	print('try')  #  try
except:
	print('except')
else:
	print('else1')  #  else1
else:
	print('else2')  #  Error due to multiple else blocks
finally:
	print('finally')  #  finally
print('end')  #  End



# Identify  error   (Home  work)
try:
	print('try')  #  try
else:
	print('else')  #  Error due to without except block used else
except:
	print('except')  
finally:
	print('finally')  
print('end')




# Find  outputs   (Home  work)
try:
	print('try')  #  try
except: 
	print('except')
if   10 > 20:
	print('if')
else:
	print('else')  #  else


# Find  outputs
def   f1():
	try:
		return  10 + '20'
	except:
		return  10 + 20  #  30
print(f1())  #  30



# Find  outputs
def   f1():
	try:
		return  10  #  10
	except:
		return  20
	else:
		return  30
print(f1())  #  10


# Find  outputs
def   f1():
	try:
		return  10 + '20'
	except:
		return  20  #  20 
	else:
		return  30
print(f1())  #  20



# Find  outputs
def   f1():
	try:
		pass
	except:
		return  20
	else:
		return  30  #  30
print(f1())  #  30



# Find  outputs
def   f1():
	try:
		return  10  #  10
	except:
		return   20
	else:
		return  30
	finally:
		return  40 
print(f1())  # 40




'''  (Home  work)
1) What  is  the  output  if  input  is  24 ?  --->  Hyd,End

2) What  is  the  output  if  input  is  25 ?  ---> Sec,End
'''
try:
	x = eval(input('Enter  any  number  :  '))
	assert    x >= 25 ,  'Hyd'
	print('Sec')
except  AssertionError  as   msg:
	print(msg)  
print('End')



''' (Home  work)
1) What  is  the  output  when  input  is  24 ?  --->  End

2) What  is  the  output  when  input  is  25 ?  --->  Sec , End
'''
try:
	x = eval(input('Enter  any  number  :  '))
	assert   x >= 25
	print('Sec')
except  AssertionError   as    msg:
	print(msg)
print('End')



# Find  outputs   (Home  work)
try:
	print('Outer   try')  #  Outer   try
	try:
		print('Inner    try')  #  Inner    try
		print(7 / 0)
		int('Hyd')
		'Hyd'[5]
		eval('Hyd')
	except   ZeroDivisionError:
		print('ZDE   of   inner   try')  #  ZDE   of   inner   try
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try')
	finally:
		print('Inner  try  finally')  #  Inner  try  finally
	print('End  of  inner  try')
except   ValueError:
	print('ValueError  of  outer  try')  #  ValueError  of  outer  try
except   IndexError:
	print('IndexError  of  outer  try')
except:
	print('default  except  of  outer  try')
finally:
	print('Outer  try  finally')  #  Outer  try  finally
print('End  of  outer  try')  #  End  of  outer  try



#  Find outputs   (Home  work)
try:
	print('Outer  try')  #  Outer  try
	try:
		print('Inner  try')  #  Inner  try
		int('Hyd')
		'Hyd'[5]
		eval('Hyd')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try ')  #  Vakue
	finally:
		print('Inner  try  finally')  #  Inner  try  finally
	print('End  of  inner  try')
except  ValueError:
	print('ValueError  of  outer try')  #  ValueError of outer try
except  IndexError:
	print('IndexError of outer try')
except:
	print('default except of outer try')
finally:
	print('Outer try finally')  #  Outer try finally
print('End of outer try')  #  End of outer try



#  Find outputs   (Home  work)
try:
	print('Outer  try')  #  Outer  try
	try:
		print('Inner  try')  #  Inner  try
		'Hyd'[3]
		eval('Hyd')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try ')
	finally:
		print('Inner  try  finally')  #  Inner  try  finally
	print('End  of  inner  try')
except  ValueError:
	print('ValueError  of  outer  try')
except  IndexError:
	print('IndexError  of  outer  try')  #  IndexError  of  outer  try
except:
	print('default except of outer try')
finally:
	print('Outer try finally')  #  Outer try finally
print('End  of  outer  try')  #  End  of  outer  try




#  Find  outputs (Home  work)
try:
	print('Outer  try')  #  Outer  try
	try:
		print('Inner  try')  	#  Inner  try
		eval('Hyd') 
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')
	finally:
		print('Inner  try  finally')  #  Inner  try  finally
	print('End of inner try') 
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
except:
	print('default  except  of  outer  try')  #  default  except  of  outer  try
finally:
	print('Outer  try  finally')  #  Outer  try  finally
print('End  of  outer  try')  #  End  of  outer  try



#  Find  outputs (Home  work)
try:
	print('Outer  try')  #  Outer  try
	try:
		print('Inner  try')  #  Inner  try
		print(10 + '20')  #  Raises  TypeError
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')
	finally:
		print('Inner  try  finally')  #  Inner  try  finally
	print('End of inner try')
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
finally:
	print('Outer  try  finally')  #  Outer  try  finally
print('End  of  outer  try')



# Find  outputs   (Home  work)
class   MyError(BaseException):
	def    __init__(self , y):
		self . a = y
		print('Constructor')  #  Constructor
# End of  the class
def  compute(x):
	print(x)  
	if  x > 20:
		raise   MyError(x)  #  Raise  MyError
	print('Hello')  
# End of  the functrion
try:
	compute(10)  #  Hello
	compute(30) 
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ' ,  msg)  #  Caught  MyError  outside  : 30
print('End')  #  End



# Find  outputs   (Home  work)
class   MyError(NameError):
	def    __init__(self):
		self . a =  25
		print('Constructor')  #  Constructor
# End of  the class
def  compute(x):
	print(x)  #  x value
	if  x > 20:
		raise   MyError()
	print('Hello')  #  Hello
#end of  the functrion
try:
	compute(30)
	compute(10)
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ' ,  msg)  #  Caught  MyError  outside  :
print('End')  #  End



# Find  outputs (Home  work)
try:
	print(1)  # 1
	print(2)  # 2
	print(3)  # 3
except:
	print(4)
else:
	print(5)  # 5
finally:
	print(6)  # 6
print(7)	  # 7




# Find  outputs   (Home  work)
try:
	print(1)  # 1
	print(7 / 0)
	print(3)
except:
	print(4)  # 4
else:
	print(5)
finally:
	print(6)  # 6
print(7)  # 7



# Find  outputs   (Home  work)
try:
	print(1)  # 1
	print(7 / 0)
	print(3)
except:
	int('Two')  #  Raises  ValueError
else:
        print(5)
finally:
        print(6)  # 6
print(7)




# Find  outputs (Home  work)
from  threading  import  *
def  f1():
	print(current_thread)  #  How  to  print  name  of  child  thread
# main  thread  executes  following  statements
new=Thread(target=f1)  #  How  to  create  a  new  thread  with  name  'new'   and  target  f1
new.start()  #  How  to  start  the  new  thread
print(current_thread)  #  How  to  print  name  of   main  thread



# Find  outputs (Home  work)
t1=Thread(target=None,name='Hyd')	# How  to  create  a  thread  t1  with  name  'Hyd'
t2=Thread(target=None)	# How  to  create  another  thread  t2  without  a  name
print(current_thread().name)	# How  to  print  name  of  main  thread
t1.name	# How  to  print  name  of  thread  t1
t2.name	# How  to  print  name  of  thread  t2
current_thread().name = 'India'	# How  to  modify  name  of  main  thread  to  'India'
t1.name = 'Sec'	# How  to  modify  name  of  thread  t1  to  'Sec'
t2.name = 'Cyb'	# How  to  modify  name  of  thread  t2  to  'Cyb'
current_thread().name	# How  to  print  name  of  main  thread
t1.name	# How  to  print  name  of  thread  t1
t2.name	# How  to  print  name  of  thread  t2
print(active_count())	# How  to  print  number  of  threads  under  execution



# Find  outputs  (Home  work)
from  threading  import  *
def   f1(x):
	s = current_thread() . name  #  Get  name  of  current  thread
	while   True:
		print(s , ' : ' , x)  #  Print  thread  name  and  x
#  main  thread  executes  following  statements
t1 = Thread(target = f1 , name = 'Hyd' , args = (10,))
t2 = Thread(target = f1 , name = 'Sec' , args =  [20])
t1 . start()  #  Start  thread  t1
t2 . start()  #  Start  thread  t2
print(active_count())
print('Press  ctrl + break  or  Fn + b  to  stop ')


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
	s = current_thread() . name  #  current thread
	while  True:
		x = randint(1 , 100)
		ctr += 1
		print(F'{s}  guess  {x}   in  attempt  :  {ctr}')  #  Rama/Sita guess x in attemt ctr
		if   x ==  n:
			break
	#end of while loop
	print(F'{s}  finish  in  {ctr}  attempts')  #  Rama.Sita finish in ctr attemts
# End  of  function   f1()
t1 = Thread(target = f1 , args = [75] , name = 'Rama')
t2 = Thread(target = f1 , args = [50] , name = 'Sita')
t1 . start() #   t1  executes  f1(75)
t2 . start()  #   t2  executes  f1(50)



# Find  outputs (Home  work)
from threading import *
def   disp():
	for  i  in  range(10):
		print('new  thread')  #  new thread 10 times
#  child  thread  is  dead
new = Thread(target = disp)
new . start()
new . join()
for  i  in  range(10):
	print('main  thread')  #  main thread 10 times
# main   thread is  dead



#  Find  outputs (Home  work)
from  threading  import *
import  time
def   disp():
	for  i  in  range(10):
		print('new  thread')  #  new thread  10 times
		time . sleep(2)  #  sleeps 2 sec every time
new = Thread(target = disp)
new . start()
new . join(10)
for  i  in  range(10):  
	print('main  thread')  #  main thread 10 times


# Find  outputs (Home  work)
from threading import *
import time
def   double():
	for   i  in  range(1 , 7):
		print('Double : ' , 2 * i)  #  1,4,6,8,10,12
		time . sleep(1)  #  sleeps 1 sec
def   square():
	for   i  in   range(1 , 7):
		print('Square : ' , i * i)  #  1,4,9,16,25,36
		time . sleep(1)  #  sleeps 1 sec
start = time . time()
double()
square()
end = time . time()
print(end - start)




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
1
1
One  is  started
Two  is  started
Three  is  started
4
One  is  ended
Three  is  ended
Two  is  ended
1
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
One  is  started
Two  is  started
Three  is  started
MainThread
One
Two
Three
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
One is   started
Two is   started
Three is   started
True
True
True
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
	print('Table  :  ' , n)  #  7,4
	for i  in  range(1 , 11):  
		print(F'{n}  *  {i}    =   {n * i}')  #  table
		time . sleep(1)  #  sleep 1sec
t1 = Thread(target = table , args = (7,))
t2 = Thread(target = table , args = (4,))
t1 . start()
t2 . start()
