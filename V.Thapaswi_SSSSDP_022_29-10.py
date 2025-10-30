#Find  outputs  (Home  work)
try:
	raise  ArithmeticError
except   ZeroDivisionError:
	print('Zero Division  Error')
except   ArithmeticError:
	print('Arithmetic Error')#Arithmetic Error
print('End')#end






# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')#f1 function
		raise  ValueError('Hyd')
		print('Hi')#skipped
	finally:
		print("f1's  finally")#f1's finally
	print('End  of  f1  function')#skipped
def  f2():
	try:
		print('f2  function')#f2 function
		return
		print('Hello')
	finally:
		print("f2's  finally")#f2's finally
	print('End  of  f2  function')#skipped
def  f3():
	try:
		print('f3  function')#f3 function
		raise   KeyError(25)
		print('Hello')#skipped
	except KeyError as  msg:
		print('Caught  by  f3  function :  ' , msg)#Caught  by  f3  function :  ' , 25
	finally:
		print("f3's  finally")#f3's finally
	print('End of f3 function')#end of f3  function
def  f4():
	try:
		print('f4 function')#f4 function
		exit()
	finally:
		print("f4's  finally")#f4's finally
	print('End of f4 function')#skipped
# End  of  all  the  functions
try:
	print('Begin')#begin
	f1()
	print('Hello')#skipped
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)#ValueError  is  caught  outside :  ' , hyd
f2()#hello
f3()
try:
	f4()
finally:
		print('Outside  finally')#outside finally
print('End  of  the  program')#skipped

'''
o/p:
Begin
f1  function
f1's  finally
ValueError  is  caught  outside :   Hyd 
f2  function
f2's  finally
f3  function
Caught  by  f3  function :   25
f3's  finally
End of f3 function
f4 function
f4's  finally
Outside finally
'''



# Find  outputs  (Home  work)
import sys
def  f1():
	try:
		print('f1  function')#f1 function
		raise  ValueError('Hyd')
		print('Hi')#skipped
	finally:
		print("f1's  finally")#f1's finally
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
	print('End  of  f4  function')#skipped
#End  of  all  the  functions
try:
	print('Begin')#Begin
	f1()
	f2()#skipped bcz error not caught
	f3()#skipped bcz error not caught
	f4()#skipped bcz error not caught
	print('Hello')#skipped bcz error not caught
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)#ValueError  is  caught  outside :  ' , hyd
print('End  of  the  program')#End  of  the  program
'''
o/P:
Begin
f1  function
f1's  finally
ValueError  is  caught  outside :   Hyd 
End  of  the  program
'''

# Find  outputs (Home  work)
def  f1():
	try:
		print('f1  function')#f1 function
		raise  KeyError()
		print('Hyd')#skipped
	except  KeyError:
		print('Caught  KeyError')#caught KerError
		raise  Exception()
	except:
		print('Sec')
	finally:
		print("f1's  finally")#f1's finaly
	print('End  of  f1  function')
#End  of  the  function
try:
	print('Begin')#Begin
	f1()
	print('Hello')
except  ValueError:
	print('Hello')
except  Exception:
	print('Recaught  Exception')#recaught Exception
finally:
	print('Outside  finally')#outside finally
print('End  of  the  program')#End of the program

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


# Find outputs (Home  work)
def  f1():
	try:
		print('f1  function')#f1 function
		raise  KeyError()#error raised
		print('Hyd')#skipped
	except  KeyError:
		print('Caught  KeyError')#caught keyError
		raise  NameError()#reraise error
	except  NameError:
		print('Sec')
	finally:
		print('f1 finally')#f1 finally
	print('End  of  f1 function')#skipped
#outside function
try:
	print('Begin')#Begin
	f1() #f1 function calling
	print('Hello')#skipped
except ValueError:
	print('Hello')
except   Exception:#except Exception is executed bcz NameError is a subclass of Exception
	print('Recaught  Exception')#Recaught Exception 
except  NameError:
	print('Caught  Name Error  outside')
finally:
	print('Outside  finally')#Outside finally
print('End of the program')#End of the program

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


# Find  outputs  (Home   work)
def  f1():
	try:
		print('f1  function')#f1 function
		raise  KeyError()
		print('Hyd')#skipped
	except  KeyError:
		print('Caught  KeyError')#caught KeyError
		raise   NameError()
	except  NameError:
		print('Sec')
	finally:
		print('f1 finally')#f1 fnally
	print('End  of  f1 function')#skipped
#outside function
try:
	print('Begin')#Begin
	f1()
	print('Hello')#skipped bcz error not handled
except  ValueError:
	print('Hello')
except   KeyError:
	print('Recaught  KeyError')
finally:
	print('Outside  finally')#outside finally
print('End of the program')#skipped

'''
o/p;
Begin
f1  function
Caught  KeyError
f1 finally
End  of  f1 function
Hello
Outside  finally
'''


# Find  outputs  (Home  work)
try:
	print('try')#try
	print(7 / 0)#ZeroDivisionError raised
except:
	print('except')#except
else:#skipped bcz when there is no in try suite in that time else suite is execute 
	print('else')
finally:
	print('finally')#finally
print('End')#end
'''
o/p:
try
except
finally
End
'''


# Find  outputs  (Home  work)
try:
	print('try')#try
except:
	print('except')
else:
	print('else')#else
finally:
	print('finally')#finally
print('End')#end



# Find  outputs   (Home  work)
try:
	print('try')
else:
    print('else')
finally:
    print('finally')
print('End')
#error :There is no except suite bcz else suite demands for except suite



# Find  outputs   (Home  work)
try:
	print('try')#try
except:
	print('except')
else:
	print('else1')#else1
#else:#Error only one else suite is permitted
	print('else2')
finally:
	print('finally')#finally
print('end')#end


# Identify  error   (Home  work)
try:
	print('try')
else:
	print('else')
except:#error order is missing except is there in before else suite
	print('except')
finally:
	print('finally')
print('end')



# Find  outputs   (Home  work)
try:
	print('try')#try
except:
	print('except')
if   10 > 20:
	print('if')
else:
	print('else')#else



# Find  outputs
def   f1():
	try:
		return  10 + '20'#TypeError raised
	except:
		return  10 + 20
print(f1())#30



# Find  outputs
def   f1():
	try:
		return  10#returned to function call
	except:
		return  20
	else:
		return  30
print(f1())#10



# Find  outputs
def   f1():
	try:
		return  10 + '20'#TypeError raised
	except:
		return  20#return to function call
	else:
		return  30#not executed
print(f1())#20



# Find  outputs
def   f1():
	try:
		pass
	except:
		return  20
	else:
		return  30
print(f1())#30


# Find  outputs
def   f1():
	try:
		return  10
	except:
		return   20
	else:
		return  30
	finally:
		return  40
print(f1())#40


'''
 (Home  work)
1) What  is  the  output  if  input  is  24 ?  --->

2) What  is  the  output  if  input  is  25 ?  --->
'''
try:
	x = eval(input('Enter  any  number  :  '))#24,25
	assert    x >= 25 ,  'Hyd'
	print('Sec')#skipped if x is 24,sec if x =25
except  AssertionError  as   msg:
	print(msg)#hyd
print('End')#End
'''
o/p:
if input is 24:
Hyd
End
if input is 25:
Sec
End	
'''




# Find  outputs   (Home  work)
try:
	print('Outer   try')#outer try
	try:
		print('Inner    try')#Inner try
		print(7 / 0)#ZeroDivisionError raised
		int('Hyd')#ValueError
		'Hyd'[5]#IndexError
		eval('Hyd')#NameError
	except   ZeroDivisionError:
		print('ZDE   of   inner   try')#ZDE of iner try
		int('Ten')#ValueError
	except  ValueError:
		print('ValueError  of  inner  try')#skipped
	finally:
		print('Inner  try  finally')#Inner  try  finally
	print('End  of  inner  try')#skipped
except   ValueError:
	print('ValueError  of  outer  try')#ValueError  of  outer  try
except   IndexError:
	print('IndexError  of  outer  try')
except:
	print('default  except  of  outer  try')
finally:
	print('Outer  try  finally')#Outer try finally
print('End  of  outer  try')#End of outer try
'''
o/p:

Outer   try
Inner    try
ZDE   of   inner   try
Inner  try  finally
ValueError  of  outer  try
Outer  try  finally
End  of  outer  try

'''



#  Find outputs   (Home  work)
try:
	print('Outer  try')#Outer try
	try:
		print('Inner  try')#Inner try
		int('Hyd')#ValueError
		'Hyd'[5]#IndexError
		eval('Hyd')#NameError
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try ')#'ValueError  of  inner  try
	finally:
		print('Inner  try  finally')#Inner  try  finally
	print('End  of  inner  try')#End  of  inner  try
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
except:
	print('default except of outer try')
finally:
	print('Outer try finally')#Outer try finally
print('End of outer try')#End of outer try

'''
o/p:
Outer  try
Inner  try
ValueError  of  inner  try
Inner  try  finally
End  of  inner  try
Outer try finally
End of outer try
'''




#  Find outputs   (Home  work)
try:
	print('Outer  try')#Outer try
	try:
		print('Inner  try')#Inner try
		'Hyd'[3]#IndexError
		eval('Hyd')#NameError
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')#ValueError
	except  ValueError:
		print('ValueError  of  inner  try ')
	finally:
		print('Inner  try  finally')#Inner try finally
	print('End  of  inner  try')
except  ValueError:
	print('ValueError  of  outer  try')
except  IndexError:#when inner try suite  raises error outside try suite is executed
	print('IndexError  of  outer  try')#IndexError  of  outer  try
except:
	print('default except of outer try')
finally:
	print('Outer try finally')#Outer try finally
print('End  of  outer  try')#End of outer try
	
'''
o/p:
Outer  try
Inner  try
Inner  try  finally
IndexError  of  outer  try
Outer try finally
End  of  outer  try

'''



#  Find  outputs (Home  work)
try:
	print('Outer  try')#Outer try
	try:
		print('Inner  try')#Inner try
		eval('Hyd')#NameError
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')#ValueError
	except ValueError:
		print('ValueError  of   inner  try ')
	finally:
		print('Inner  try  finally')#Inner  try  finally
	print('End of inner try')#skipped
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
except:
	print('default  except  of  outer  try')#default  except  of  outer  try
finally:
	print('Outer  try  finally')#Outer  try  finally
print('End  of  outer  try')#End  of  outer  try
'''
O/p:
Outer  try
Inner  try
Inner  try  finally
default  except  of  outer  try
Outer  try  finally
End  of  outer  try

'''



#  Find  outputs (Home  work)
try:
	print('Outer  try')#Outer try
	try:
		print('Inner  try')#Inner try
		print(10 + '20')#TypeError
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')
	finally:
		print('Inner  try  finally')#Inner  try  finally
	print('End of inner try')#skipped error not caught
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
finally:
	print('Outer  try  finally')#Outer  try  finally
print('End  of  outer  try')#skipped bcz error not caught

'''
O/P:
Outer  try
Inner  try
Inner  try  finally
Outer  try  finally
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
o/p:
10
Hello
30
Constructor
Caught  MyError  outside  :   30
End

'''


# Find  outputs   (Home  work)
class   MyError(NameError):
	def    __init__(self):
		self . a =  25
		print('Constructor')#constructor
# End of  the class
def  compute(x):
	print(x)#30
	if  x > 20:
		raise   MyError()
	print('Hello')
#end of  the functrion
try:
	compute(30)
	compute(10)
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ' ,  msg)#Caught  MyError  outside  :
print('End')#End





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
'''
o/p:
1
2
3
5
6
7
'''




# Find  outputs   (Home  work)
try:
	print(1)#1
	print(7 / 0)#ZeroDivisionError
	print(3)#skipped
except:
	print(4)#4
else:
	print(5)
finally:
	print(6)#6
print(7)#7

'''
o/p:
1
4
6
7
'''


# Find  outputs   (Home  work)
try:
	print(1)#1
	print(7 / 0)#ZeroDivisionError
	print(3)#skipped
except:
	int('Two')#ValueError
else:
        print(5)
finally:
        print(6)#6
print(7)#skipped bcz error not caught



# Find  outputs (Home  work)
from  threading  import  *
def  f1():
	print(current_thread().name)#How  to  print  name  of  child  thread
# main  thread  executes  following  statements
main=Thread(target=f1,name='new')#How  to  create  a  new  thread  with  name  'new'   and  target  f1
main.start()#How  to  start  the  new  thread
print(current_thread().name)#How  to  print  name  of   main  thread

'''
o/p:
new
MainThread
'''


# Find  outputs (Home  work)
from threading import*
t1=Thread(name='Hyd')#How  to  create  a  thread  t1  with  name  'Hyd'
t2=Thread()#How  to  create  another  thread  t2  without  a  name
print(current_thread().name)#How  to  print  name  of  main  thread
print(t1.name)#How  to  print  name  of  thread  t1
print(t2.name)#How  to  print  name  of  thread  t2
current_thread().name='India'#How  to  modify  name  of  main  thread  to  'India'
t1.name='Sec'#How  to  modify  name  of  thread  t1  to  'Sec'
t2.name='cyb'#How  to  modify  name  of  thread  t2  to  'Cyb'
print(current_thread().name)#How  to  print  name  of  main  thread
print(t1.name)#How  to  print  name  of  thread  t1
print(t2.name)#How  to  print  name  of  thread  t2
print(active_count())#How  to  print  number  of  threads  under  execution

'''
o/p:
MainThread
Hyd
Thread-1
India
Sec
cyb
1
'''





# Find  outputs  (Home  work)
from  threading  import  *
def   f1(x):
	s = current_thread() . name
	while   True:
		print(s , ' : ' , x)
#  main  thread  executes  following  statements
t1 = Thread(target = f1 , name = 'Hyd' , args = (10,))#creates hyd thread 
t2 = Thread(target = f1 , name = 'Sec' , args =  [20])#creates sec thread
t1 . start()
t2 . start()
print(active_count())#3(MainThread+Hyd+Sec)
print('Press  ctrl + break  or  Fn + b  to  stop ')
# Both threads will run its own infinity loop

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
o/p:
Rama  guess  47   in  attempt  :  1
Sita  guess  19   in  attempt  :  1

Rama  guess  84   in  attempt  :  2
Sita  guess  70   in  attempt  :  2

Rama  guess  86   in  attempt  :  3
Sita  guess  13   in  attempt  :  3
Rama  guess  1   in  attempt  :  4 

Sita  guess  42   in  attempt  :  4
Rama  guess  24   in  attempt  :  5
Sita  guess  98   in  attempt  :  5

Rama  guess  18   in  attempt  :  6
Sita  guess  96   in  attempt  :  6
Rama  guess  24   in  attempt  :  7

Rama  guess  49   in  attempt  :  8
Sita  guess  46   in  attempt  :  7

'''




# Find  outputs (Home  work)
from threading import *
def   disp():
	for  i  in  range(10):
		print('new  thread')#new thread 10 times
#  child  thread  is  dead
new = Thread(target = disp)
new . start()
new . join()
for  i  in  range(10):
	print('main  thread')#main threa 10 times
# main   thread is  dead
'''
o/p:
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
'''




#  Find  outputs (Home  work)
from  threading  import *
import  time
def   disp():
	for  i  in  range(10):
		print('new  thread')#new thread 10 times
		time . sleep(2)#each print it sleeps 2 seconds
new = Thread(target = disp)#new thread is created
new . start()#executing disp()
new . join(10)#wait for the new thread
for  i  in  range(10):
	print('main  thread')#main thread 10 times



	
# Find  outputs (Home  work)
from threading import *
import time
def   double():
	for   i  in  range(1 , 7):
		print('Double : ' , 2 * i)#2,4,6,8,10,12
		time . sleep(1)# waits 1 second between each print
def   square():
	for   i  in   range(1 , 7):
		print('Square : ' , i * i)#1,4,9,16,25,36
		time . sleep(1)# waits 1 second between each print
start = time . time()#start timing
double()
square()
end = time . time()
print(end - start) #12 seconds approximately   




# Find  outputs  (Home  work)
from  threading  import  *
import  time
def   display():
        name = current_thread() . name
        print(name , ' is  started')
        time . sleep(3)
        print(name , ' is  ended')
# End  of  the  function
print(active_count())#1 i.e main thread
t1 = Thread(target = display , name = 'One')
t2 = Thread(target = display , name = 'Two')
t3 = Thread(target = display , name = 'Three')
print(active_count())#1 bcz t1,t2 & t3 just created but not start
t1 . start()
t2 . start()
t3 . start()#Three threads start running display() sequentially
print(active_count())#4
t1 . join()
t2 . join()
t3 . join()#Thread waits until all three threads finish execution
print(active_count())#1 only main thread is left


'''
o/p:
1
1
One is started
Two is started
Three is started
4
One is ended
Two is ended
Three is ended
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
t1 = Thread(target = disp , name = 'One')#Thread one is created
t2 = Thread(target = disp , name = 'Two')#Thread two is created
t3 = Thread(target = disp , name = 'Three')#Thread three is created
t1 . start()#executes disp() i.e one is started
t2 . start()#Two is started
t3 . start()#Three is started
list = enumerate()#[main thread+t1+t2+t3]
for  t  in   list:
	print(t . name)#main thread
	               #one
				   #Two
				   #Three
t1 . join()#one is ended
t2 . join()#Two is ended
t3 . join()#Three is ended
list = enumerate()#[main thread]
for  t  in  list:
	print(t . name)#main thread




# is_alive()  method   demo  program
from  threading  import *
import  time
def   disp():
	name =  current_thread() . name
	print(name , 'is   started')
	time . sleep(3)
	print(name , '   is    ended')
t1 = Thread(target = disp , name = 'One')#Thread one is created
t2 = Thread(target = disp , name = 'Two')#Thread Two is created
t3 = Thread(target = disp , name = 'Three')#Thread Threeis created
t1 . start()#executes disp() i.e one is started
t2 . start()#Two is started
t3 . start()#Three is started
print(t1 . is_alive())#True
print(t2 . is_alive())#True
print(t3 . is_alive())#True
t1 . join()#one is ended
t2 . join()#Two is ended
t3 . join()#Three is ended
print(t1 . is_alive())#False
print(t2 . is_alive())#False
print(t3 . is_alive())#False





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
O/P:
Table  :   7
Table  :  7  *  1    =   7
4
4  *  1    =   4
4  *  2    =   8
7  *  2    =   14
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