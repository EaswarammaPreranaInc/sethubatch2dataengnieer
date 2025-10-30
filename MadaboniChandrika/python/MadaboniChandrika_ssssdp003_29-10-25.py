#1st program
#  Find  outputs  (Home  work)
try:
	raise  ArithmeticError #moves to line 7
except   ZeroDivisionError:
	print('Zero Division  Error')
except   ArithmeticError:
	print('Arithmetic Error') #Arithmetic Error
print('End')#End


'''
Is  child  error  except  suite  executed  when  parent  error   raised ?  ---> No
'''

#2nd program
# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function') #f1 function
		raise  ValueError('Hyd')
		print('Hi')
	finally:
		print("f1's  finally") #f1's finally
	print('End  of  f1  function')
def  f2():
	try:
		print('f2  function')#f2 function
		return
		print('Hello')
	finally:
		print("f2's  finally")#f2's finally
	print('End  of  f2  function')
def  f3():
	try:
		print('f3  function')#f3 function
		raise   KeyError(25)
		print('Hello')
	except KeyError as  msg:
		print('Caught  by  f3  function :  ' , msg)#Caught  by  f3  function :   25
	finally:
		print("f3's  finally")#f3's finally
	print('End of f3 function')#End of f3 function
def  f4():
	try:
		print('f4 function')#f4 function
		exit()
	finally:
		print("f4's  finally")#f4's finally
	print('End of f4 function')
# End  of  all  the  functions
try:
	print('Begin')#Begin
	f1()#moves to line 18
	print('Hello')
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)#ValueError  is  caught  outside :   Hyd
f2()
f3()
try:
	f4()
finally:
		print('Outside  finally')#outside finally
print('End  of  the  program')


#3rd program
# Find  outputs  (Home  work)
import sys
def  f1():
	try:
		print('f1  function')#f1 function-2
		raise  ValueError('Hyd')
		print('Hi')
	finally:
		print("f1's  finally")#f1's finally-3
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
	print('Begin')#Begin-1
	f1()#moves to line 70
	f2()#skipped
	f3()#skipped
	f4()#skipped
	print('Hello')
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)#ValueError  is  caught  outside :   Hyd -4
print('End  of  the  program')#End  of  the  program-5


#4th program
# Find  outputs (Home  work)
def  f1():
	try:
		print('f1  function')#f1 function -2
		raise  KeyError()#moves to line 123
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')#caught KeyError -3
		raise  Exception()#moves to line 138
	except:
		print('Sec')
	finally:
		print("f1's  finally")#f1's finally -4
	print('End  of  f1  function')
#End  of  the  function
try:
	print('Begin')#Begin -1
	f1()#moves to line 118
	print('Hello')
except  ValueError:
	print('Hello')
except  Exception:
	print('Recaught  Exception')#Recaught  Exception -5
finally:
	print('Outside  finally')#Outside  finally -6
print('End  of  the  program')#End  of  the  program -7


#5th program
# Find outputs (Home  work)
def  f1():
	try:
		print('f1  function')#f1 function -2
		raise  KeyError()#moves to line 152
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')#caught KeyError -3
		raise  NameError()#moves to line 169
	except  NameError:
		print('Sec')
	finally:
		print('f1 finally')#f1 finally -4
	print('End  of  f1 function')
#outside function
try:
	print('Begin')#Begin - 1
	f1()#moves to line 148
	print('Hello')
except ValueError:
	print('Hello')
except   Exception:
	print('Recaught  Exception')#recaught exception -5 (except is parent class to errors so )
except  NameError:
	print('Caught  Name Error  outside')
	print('Outside  finally')#Outside  finally -6
print('End of the program')#End of the program -7


#6th program
# Find  outputs  (Home   work)
def  f1():
	try:
		print('f1  function')#f1 function -2
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')#caught KeyError -3
		raise   NameError()#error 
	except  NameError:
		print('Sec')
	finally:
		print('f1 finally')#f1 finally -4
	print('End  of  f1 function')
#outside function
try:
	print('Begin')#Begin - 1
	f1()
	print('Hello')
except  ValueError:
	print('Hello')
except   KeyError:
	print('Recaught  KeyError')
finally:
	print('Outside  finally')#Outside  finally - 5
print('End of the program')


#7th program
# Find  outputs  (Home  work)
try:
	print('try')#try
	print(7 / 0)#move to except suite due to ZDE
except:
	print('except')#except
else:
	print('else')#skipped because error is raised in try suite
finally:
	print('finally')#finally
print('End')#End


#8th program
# Find  outputs  (Home  work)
try:
	print('try')#try
except:
	print('except')#skipped
else:
	print('else')#else
finally:
	print('finally')#finally
print('End')#end


#9th program
# Find  outputs   (Home  work)
try:
	print('try')#error because there is no except suite
else:
    print('else')
finally:
    print('finally')
print('End')


#10th program
# Find  outputs   (Home  work)
try:
	print('try')#try
except:
	print('except')
else:
	print('else1')#else1
else:
	print('else2')#error,only one else suite is permitted
finally:
	print('finally')
print('end')


#11st program
# Identify  error   (Home  work)
try:
	print('try')#error there is no except suite immediately after try
else:
	print('else')
except:
	print('except')
finally:
	print('finally')
print('end')


#12th program
# Find  outputs   (Home  work)
try:
	print('try')#try
except:
	print('except')
if   10 > 20:
	print('if')
else:
	print('else')#else


#13th program
# Find  outputs
def   f1():
	try:
		return  10 + '20'#error
	except:
		return  10 + 20#30
print(f1())#30


#14th program
# Find  outputs
def   f1():
	try:
		return  10
	except:
		return  20
	else:
		return  30
print(f1())#10 ,it should execute the else suite as try is not raising any error but upon encountering return the control comes out of the function without executing else suite


#15th program
# Find  outputs
def   f1():
	try:
		return  10 + '20'#error
	except:
		return  20
	else:
		return  30
print(f1())#20


#16th program
# Find  outputs
def   f1():
	try:
		pass
	except:
		return  20
	else:
		return  30
print(f1())#30


#17th program
# Find  outputs
def   f1():
	try:
		return  10 
	except:
		return   20
	else:
		return  30
	finally:
		return  40 #40
print(f1())# 40


#18th program
'''  (Home  work)
1) What  is  the  output  if  input  is  24 ?  ---> Hyd \n  End

2) What  is  the  output  if  input  is  25 ?  --->Sec \n End
'''

try:
	x = eval(input('Enter  any  number  :  '))
	assert    x >= 25 ,  'Hyd'
	print('Sec')
except  AssertionError  as   msg:
	print(msg)
print('End')


#19th program
''' (Home  work)
1) What  is  the  output  when  input  is  24 ?  --->empty \n End

2) What  is  the  output  when  input  is  25 ?  --->Sec \n End
'''

try:
	x = eval(input('Enter  any  number  :  '))
	assert   x >= 25
	print('Sec')
except  AssertionError   as    msg:
	print(msg)
print('End')


#20th program
# Find  outputs   (Home  work)
try:
	print('Outer   try')#outer try 
	try:
		print('Inner    try')#inner try 
		print(7 / 0)# error,moves to line 383
		int('Hyd')
		'Hyd'[5]
		eval('Hyd')
	except   ZeroDivisionError:
		print('ZDE   of   inner   try')#ZDE   of   inner   try - 3
		int('Ten') #moves to line 391
	except  ValueError:
		print('ValueError  of  inner  try')
	finally:
		print('Inner  try  finally')#Inner  try  finally 
	print('End  of  inner  try')
except   ValueError:
	print('ValueError  of  outer  try')#ValueError  of  outer  try
except   IndexError:
	print('IndexError  of  outer  try')
except:
	print('default  except  of  outer  try')
finally:
	print('Outer  try  finally')#Outer  try  finally
print('End  of  outer  try')#End  of  outer  try


#21st program
#  Find outputs   (Home  work)
try:
	print('Outer  try')#outer try
	try:
		print('Inner  try')#inner try
		int('Hyd')#error,moves to line 414
		'Hyd'[5]
		eval('Hyd')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try ')#ValueError of inner try
	finally:
		print('Inner  try  finally')#Inner try finally
	print('End  of  inner  try')# End of inner try
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
except:
	print('default except of outer try')
finally:
	print('Outer try finally')#outer try finally
print('End of outer try')#End of outer try


#22nd program
#  Find outputs   (Home  work)
try:
	print('Outer  try')#outer try
	try:
		print('Inner  try')#Inner try
		'Hyd'[3]#moves to line 448
		eval('Hyd')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try ')
	finally:
		print('Inner  try  finally')#Inner try finally
	print('End  of  inner  try')
except  ValueError:
	print('ValueError  of  outer  try')
except  IndexError:
	print('IndexError  of  outer  try')#IndexError of outer try
except:
	print('default except of outer try')
finally:
	print('Outer try finally')#Outer try finally
print('End  of  outer  try')#End of outer try


#23rd program
#  Find  outputs (Home  work)
try:
	print('Outer  try')#Outer try
	try:
		print('Inner  try')#Inner try
		eval('Hyd')#moves to line 476
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')
	finally:
		print('Inner  try  finally')#Inner try finally
	print('End of inner try')
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
except:
	print('default  except  of  outer  try')#default except of outer try
finally:
	print('Outer  try  finally')#outer try finally
print('End  of  outer  try')#End of outer try


#24th program
#  Find  outputs (Home  work)
try:
	print('Outer  try')#Outer try
	try:
		print('Inner  try')#Inner try
		print(10 + '20')#Type error is reported
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')
		print('Inner  try  finally')#Inner try finally
	print('End of inner try')
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
finally:
	print('Outer  try  finally')#outer try finally
print('End  of  outer  try')


#25th program
# Find  outputs   (Home  work)
class   MyError(BaseException):
	def    __init__(self , y):
		self . a = y
		print('Constructor')
# End of  the class
def  compute(x):
	print(x) #30
	if  x > 20:
		raise   MyError(x) #Class obj is created and also control shifts to except suite
	print('Hello')#Hello
# End of  the functrion
try:
	compute(10) #10 \n Hello
	compute(30) #30 \n constructor
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ' ,  msg)#caught myerror ouside: 30
print('End')#End


#26th program
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
	compute(30)#30 \n constructor
	compute(10)
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ' ,  msg)#caught error ouside: 
print('End')#end


#27th program
# Find  outputs (Home  work)
try:
	print(1)#1
	print(2)#2
	print(3)#3
except:
	print(4)
else:
	print(5)#5
finally:
	print(6)#6
print(7)#7


#28th program
# Find  outputs   (Home  work)
try:
	print(1)#1
	print(7 / 0)#error
	print(3)
except:
	print(4)#4
else:
	print(5)
finally:
	print(6)#6
print(7)#7


#29th program
# Find  outputs   (Home  work)
try:
	print(1)#1
	print(7 / 0)#error- handled 
	print(3)
except:
	int('Two')#error is reported
else:
        print(5)
finally:
        print(6)#6
print(7)


#30th program
# Find  outputs (Home  work)
from  threading  import  *
def  f1():
	print(current_thread().name)#How  to  print  name  of  child  thread
# main  thread  executes  following  statements
new=Thread(target=f1)#How  to  create  a  new  thread  with  name  'new'   and  target  f1
new.start()#How  to  start  the  new  thread
print(current_thread().name)#How  to  print  name  of   main  thread


#31st program
# Find  outputs (Home  work)
from threading import *
t1=Thread(name="Hyd")#How  to  create  a  thread  t1  with  name  'Hyd'
t2=Thread()#How  to  create  another  thread  t2  without  a  name
print(current_thread().name)#How  to  print  name  of  main  thread
print(t1.name)#How  to  print  name  of  thread  t1
print(t2.name)#How  to  print  name  of  thread  t2
current_thread().name="India"#How  to  modify  name  of  main  thread  to  'India'
t1.name="Sec"#How  to  modify  name  of  thread  t1  to  'Sec'
t2.name="Cyb"#How  to  modify  name  of  thread  t2  to  'Cyb'
print(current_thread().name)#How  to  print  name  of  main  thread
print(t1.name)#How  to  print  name  of  thread  t1
print(t2.name)#How  to  print  name  of  thread  t2
print(active_count())#How  to  print  number  of  threads  under  execution


#32nd program
# Find  outputs  (Home  work)
from  threading  import  *
def   f1(x):
	s = current_thread() . name
	while   True:
		print(s , ' : ' , x)
#  main  thread  executes  following  statements
t1 = Thread(target = f1 , name = 'Hyd' , args = (10,))
t2 = Thread(target = f1 , name = 'Sec' , args =  [20])
t1 . start()#infinite times Hyd:10
t2 . start()#infinite times  Sec :20 alternatively
print(active_count())#3
print('Press  ctrl + break  or  Fn + b  to  stop ')#Press  ctrl + break  or  Fn + b  to  stop


#33rd program
# Find  outputs (Home  work)
from  threading  import  Thread , current_thread
from  random  import  randint
def   f1(n):
	ctr = 0
	s = current_thread() . name#t1 and t2 
	while  True:
		x = randint(1 , 100)
		ctr += 1 
		print(F'{s}  guess  {x}   in  attempt  :  {ctr}')#Rama(Sita for t2) guess 25 in attempt 1
		if   x ==  n:#executed when generated number==75 for t1 and 50 for t2 
			break #comes out of the loop 
	#end of while loop
	print(F'{s}  finish  in  {ctr}  attempts')#Rama(Sita) finish in 5(suppose) attempts
# End  of  function   f1()
t1 = Thread(target = f1 , args = [75] , name = 'Rama')
t2 = Thread(target = f1 , args = [50] , name = 'Sita')
t1 . start() #   t1  executes  f1(75)
t2 . start()  #   t2  executes  f1(50)


#34th program
# Find  outputs (Home  work)
from threading import *
def   disp():
	for  i  in  range(10):
		print('new  thread') # 10 times new thread(1)
#  child  thread  is  dead
new = Thread(target = disp)
new . start()
new . join()
for  i  in  range(10):
	print('main  thread')#10 times main thread(2)
# main   thread is  dead


#35th program
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
	output is either 5 times new thread followed by 10 times main thread and then again 5 times new thread (or) 6 times new thread followed by 10 times main thread and then again 4 times new thread depending on which thread is choosen for execution at the 10th second because at 10th second both threads are in ready state
	'''

#36th program
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
print(end - start)#results execution time -which is approx 12 sec because each loop produces o/p for 1 sec repeated for 6+6 times for double and square respectively and some milli sec extra for executing the outside statements 

'''
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
12.001800298690796
'''

#37th program
# Find  outputs  (Home  work)
from  threading  import  *
import  time
def   display():
        name = current_thread() . name
        print(name , ' is  started')
        time . sleep(3)
        print(name , ' is  ended')
# End  of  the  function
print(active_count())#1
t1 = Thread(target = display , name = 'One')
t2 = Thread(target = display , name = 'Two')
t3 = Thread(target = display , name = 'Three')
print(active_count())#1
t1 . start()#One is started
t2 . start()#Two is started
t3 . start()#Three is started
print(active_count())#4
t1 . join()#One is ended
t2 . join()#Two is ended
t3 . join()#Three is ended ---in any order
print(active_count())#1


#38th program
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
t1 . start()#One is started
t2 . start()#two is started
t3 . start()#three is started
list = enumerate()#[mainThread,t1,t2,t3]
for  t  in   list:
	print(t . name)#Main Thread \n one \n two \n three
t1 . join()#One is ended
t2 . join()#two is ended
t3 . join()#three is ended  --- in any order
list = enumerate()#[mainThread]
for  t  in  list:
	print(t . name)#mainThread


#39th program
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
t1 . start()#One is started
t2 . start()#two is started
t3 . start()#three is started
print(t1 . is_alive())#True
print(t2 . is_alive())#True
print(t3 . is_alive())#True
t1 . join()#One is ended
t2 . join()#two is ended
t3 . join()#three is ended
print(t1 . is_alive())#False
print(t2 . is_alive())#False
print(t3 . is_alive())#False


#40th program
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
t1 . start()#7 table is printed 
t2 . start()#4 table is printed in any order
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
'''