
#  Find  outputs  (Home  work)
try:
	raise  ArithmeticError
except   ZeroDivisionError:
	print('Zero Division  Error')
except   ArithmeticError:
	print('Arithmetic Error')
print('End')


'''
Is  child  error  except  suite  executed  when  parent  error   raised ?  ---> no because w are user defined error
'''



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
print('End  of  the  program')# begin
f1 function
valueError s caught outside:hyd
hello
f2 function
outside finally
error


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
print('End  of  the  program')#  begin
f1 function
valueError is caught outside:hyd
f2 function
f2's finally
error is not handled



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
print('End  of  the  program')# begin 
f1 function
sec 
f1's  finally
end of the f1 function
hello
Outside  finally'
End  of  the  program



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
print('End  of  the  program')#begin
f1 func
caught keyerror
sec
f1s finally
end of f1 function
outside finally
end of program


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
print('End of the program')#bein
f1 function
caught keyerror
sec
f1 finally
end of f1 function
outside finally
end of the program


# Find  outputs  (Home   work)
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')
		raise   NameError()
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
print('End of the program')#begin
f1 function
caught keyerror
sec
f1 finally
end of f1 function
outside finally
end of the program



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
print('End')#try
except
finally
end


# Find  outputs  (Home  work)
try:
	print('try')
except:
	print('except')
else:
	print('else')
finally:
	print('finally')
print('End')#try
else
finally
end


# Find  outputs   (Home  work)
try:
	print('try')
else:
    print('else')
finally:
    print('finally')
print('End')# try
finally
error

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
print('end')#try
error at else2
finally

# Identify  error   (Home  work)
try:
	print('try')
else:
	print('else')
except:
	print('except')
finally:
	print('finally')
print('end')#try
error at line 3
finally

# Find  outputs   (Home  work)
try:
	print('try')
except:
	print('except')
if   10 > 20:
	print('if')
else:
	print('else')# try
if

# Find  outputs
def   f1():
	try:
		return  10 + '20'
	except:
		return  10 + 20
print(f1())#30

# Find  outputs
def   f1():
	try:
		return  10
	except:
		return  20
	else:
		return  30
print(f1())#10

# Find  outputs
def   f1():
	try:
		return  10 + '20'
	except:
		return  20
	else:
		return  30
print(f1())#20

# Find  outputs
def   f1():
	try:
		pass
	except:
		return  20
	else:
		return  30
print(f1())#20

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
print(f1())#10
finally gets error






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
print('End')#msg
25



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
print('End  of  outer  try')#outer try
inner try
zde of inner try
valueError of inner try
inner try finally
outer try finally
end of outer try





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
print('End of outer try')#outer try
inner try
valueError of inner try
inner try finally
End  of  inner  try
Outer try finally
End of outer try



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
print('End  of  outer  try')#outer try
inner try
IndexError  of  outer  try
Inner  try  finally
Outer try finally
End  of  outer  try

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
print('End  of  outer  try')#outer try
inner try
default  except  of  outer  try
Inner  try  finally
End of inner try
Outer  try  finally
End  of  outer  try


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
print('End  of  outer  try')#outer try
inner try
Inner  try  finally
End of inner try
Outer  try  finally
End  of  outer  try
error is raised




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
print('End')#hello
Caught  MyError  outside  : 30



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
print('End')#
Caught  MyError  outside  :  30
hello



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
print(7)#1
2
3
6
7


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
print(7)#1
4
6
7



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
print(7)#1
5
6
7


# Find  outputs (Home  work)
from  threading  import  *
def  f1():
	How  to  print  name  of  child  thread
# main  thread  executes  following  statements
new=thread(target=f1) #How  to  create  a  new  thread  with  name  'new'   and  target  f1
new.start()  #How  to  start  the  new  thread
print(main.name)  #How  to  print  name  of   main  thread

# Find  outputs (Home  work)
t1=Thread(target=f1,name='Hyd') #How  to  create  a  thread  t1  with  name  'Hyd'
t2=Thread(target=f1) #How  to  create  another  thread  t2  without  a  name
print(main.name) #How  to  print  name  of  main  thread
print(t1.name) #How  to  print  name  of  thread  t1
print(t2.name) #How  to  print  name  of  thread  t2
main(name)='india' #How  to  modify  name  of  main  thread  to  'India'
t1(name)='sec' #How  to  modify  name  of  thread  t1  to  'Sec'
t2(name)='cyb' #How  to  modify  name  of  thread  t2  to  'Cyb'
print(main.name) #How  to  print  name  of  main  thread
print(t1.name) #How  to  print  name  of  thread  t1
print(t2.name) #How  to  print  name  of  thread  t2
print(active_count()) #How  to  print  number  of  threads  under  execution

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
print('Press  ctrl + break  or  Fn + b  to  stop ')#hyd
hyd : 10
sec
sec:20
recursion




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
t1
t1  guess  {random number}   in  attempt  :  {1} for 75 times
t1  guess  {random number}   in  attempt  :  {1} for 50 times



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

#new  thread
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
double()#
square()
end = time . time()
print(end - start)#
Double : ' , 2
Double : ' , 4
Double : ' , 8
Double : ' , 10
Double : ' , 12
Double : ' , 14
Square : ' , 1 
Square : ' , 4
Square : ' , 9
Square : ' , 16
Square : ' , 25
Square : ' , 36


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
t1 = Thread(target = display , name = 'One')#
t2 = Thread(target = display , name = 'Two')
t3 = Thread(target = display , name = 'Three')
print(active_count())#1
t1 . start()#one
one , ' is  started
one , ' is  ended
t2 . start()#
two , ' is  started
two , ' is  ended
t3 . start()#
three , ' is  started
three , ' is  ended
print(active_count())#3
t1 . join()
t2 . join()
t3 . join()
print(active_count())#1


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
t1 . start()#
one , ' is  started
one , ' is  ended
t2 . start()#
two , ' is  started
two , ' is  ended
t3 . start()#
three , ' is  started
three , ' is  ended
list = enumerate()
for  t  in   list:
	print(t . name)
t1 . join()
t2 . join()
t3 . join()
list = enumerate()
for  t  in  list:
	print(t . name)
#main thread



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
t1 . start()#
one , ' is  started
one , ' is  ended
t2 . start()#
two , ' is  started
two , ' is  ended
t3 . start()#
three , ' is  started
three , ' is  ended
print(t1 . is_alive())#true
print(t2 . is_alive())#true
print(t3 . is_alive())#true
t1 . join()
t2 . join()
t3 . join()
print(t1 . is_alive())#false
print(t2 . is_alive())#false
print(t3 . is_alive())#false


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
t1 . start()#Table  :  (7,)
7  *  1   =   7
7  *  2    =   14
7  *  3    =   21
7  *  4    =   24
7  *  5    =   35
7  *  6    =   42
7  *  7    =   49
7  *  8    =   56
7  *  9    =   69
7  *  10    =   70

t2 . start()#
2  *  1   =   2
2  *  2    =  4
2  *  3    =  6
2  *  4    =  8
2  *  5    =  10
2  *  6    =  12
2  *  7    =  14
2  *  8    =  16
2  *  9    =  18
2  *  10    =  20


















