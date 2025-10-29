# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')                                   # f1 function
		raise  ValueError('Hyd')
		print('Hi')
	finally:
		print("f1's  finally")                                  # f1's finally
	print('End  of  f1  function')
def  f2():
	try:
		print('f2  function')                                   # f2 function
		return
		print('Hello')
	finally:
		print("f2's  finally")                                  # f2's finally
	print('End  of  f2  function')
def  f3():
	try:
		print('f3  function')                                   # f3 function
		raise   KeyError(25)
		print('Hello')
	except KeyError as  msg:
		print('Caught  by  f3  function :  ' , msg)             # Caught by f3 function : 25
	finally:
		print("f3's  finally")                                  # f3's finally
	print('End of f3 function')                                 # End of f3 function
def  f4():
	try:
		print('f4 function')                                    # f4 function
		exit()
	finally:
		print("f4's  finally")                                  # f4's finally
	print('End of f4 function')
# End  of  all  the  functions
try:
	print('Begin')                                              # Begin
	f1()
	print('Hello')
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)          # ValueError is caught outside : Hyd
f2()
f3()
try:
	f4()
finally:
		print('Outside  finally')                               # Outside finally
print('End  of  the  program')





# Find  outputs  (Home  work)
import sys
def  f1():
	try:
		print('f1  function')                                   # f1 function
		raise  ValueError('Hyd')
		print('Hi')
	finally:
		print("f1's  finally")                                  # f1's finally
	print('End  of  f1  function')
def  f2():
	try:
		print('f2  function')                                   # f2 function
		return
		print('Hello')
	finally:
		print("f2's  finally")                                  # f2's finally
	print('End  of  f2  function')
def  f3():
	try:
		print('f3  function')                                   # f3 function
		raise   KeyError(25)
		print('Hello')
	except  KeyError  as  msg:
		print('Caught  by  f3  function : ' , msg)              # Caught by f3 function : 25
	finally:
		print("f3's  finally")                                  # f3's finally
	print('End  of  f3  function')
def  f4():
	try:
		print("f4  function")                                   # f4 function
		sys . exit()
	finally:
		print("f4's  finally")
	print('End  of  f4  function')
#End  of  all  the  functions
try:
	print('Begin')                                              # Begin
	f1()
	f2()
	f3()
	f4()
	print('Hello')
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)         # ValueError is caught outside : Hyd
print('End  of  the  program')                                 # End of the program




# Find  outputs (Home  work)
def  f1():
	try:
		print('f1  function')                   # f1 function
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')               # Caught KeyError
		raise  Exception()
	except:
		print('Sec')
	finally:
		print("f1's  finally")                  # f1's finally
	print('End  of  f1  function')
#End  of  the  function
try:
	print('Begin')                              # Begin
	f1()
	print('Hello')
except  ValueError:
	print('Hello')
except  Exception:
	print('Recaught  Exception')                # Recaught Exception
finally:
	print('Outside  finally')                   # Outside finally
print('End  of  the  program')                  # End of the program




# Find outputs (Home  work)
def  f1():
	try:
		print('f1  function')                       # f1 function
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')                   # Caught KeyError
		raise  NameError()
	except  NameError:
		print('Sec')
	finally:
		print('f1 finally')                         # f1 finally
	print('End  of  f1 function')
#outside function
try:
	print('Begin')                                  # Begin
	f1()
	print('Hello')
except ValueError:
	print('Hello')
except   Exception:
	print('Recaught  Exception')                    # Recaught Exception
except  NameError:
	print('Caught  Name Error  outside')
finally:
	print('Outside  finally')                       # Outside finally
print('End of the program')                         # End of the program




# Find  outputs  (Home   work)
def  f1():
	try:
		print('f1  function')                       # f1 function
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')                   # Caught KeyError
		raise   NameError()
	except  NameError:
		print('Sec')
	finally:
		print('f1 finally')                         # f1 finally
	print('End  of  f1 function')
#outside function
try:
	print('Begin')                                  # Begin
	f1()
	print('Hello')
except  ValueError:
	print('Hello')
except   KeyError:
	print('Recaught  KeyError')
finally:
	print('Outside  finally')                       # Outside finally
print('End of the program')



# Find  outputs  (Home  work)
try:
	print('try')                # try
	print(7 / 0)
except:
	print('except')             # except
else:
	print('else')
finally:
	print('finally')            # finally
print('End')                    # End




# Find  outputs  (Home  work)
try:
	print('try')                # try 
except:
	print('except')
else:
	print('else')               # else
finally:
	print('finally')            # finally
print('End')                    # End



'''
# Find  outputs   (Home  work)
try:
	print('try')
else:
    print('else')
finally:
    print('finally')
print('End')               
'''

# Error due to there is no except suite after try suite


# Find  outputs   (Home  work)
try:
	print('try')                    # try
except:
	print('except')
else:
	print('else1')                  # else 1
#else:
	print('else2')                  # Error due to multiple else suite
finally:
	print('finally')                # finally
print('end')                        # end


'''
# Identify  error   (Home  work)
try:
	print('try')                    # try
else:
	print('else')
except:
	print('except')
finally:
	print('finally')
print('end')                        # end
'''

# Error due except suite should be after try suite



# Find  outputs   (Home  work)
try:
	print('try')                # try
except:
	print('except')
if   10 > 20:
	print('if')
else:
	print('else')               # else
	


# Find  outputs
def   f1():
	try:
		return  10 + '20'
	except:
		return  10 + 20
print(f1())                     # 30



# Find  outputs
def   f1():
	try:
		return  10
	except:
		return  20
	else:
		return  30
print(f1())                 # 10



# Find  outputs
def   f1():
	try:
		return  10 + '20'
	except:
		return  20
	else:
		return  30
print(f1())                     # 20


# Find  outputs
def   f1():
	try:
		pass
	except:
		return  20
	else:
		return  30
print(f1())                 # 30



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
print(f1())                 # 40



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
if input is 24

output:
Hyd
End

if input is 25

output:
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
if input is 24

output:
End

if input is 25

output:
Sec
End
'''


# Find  outputs   (Home  work)
try:
	print('Outer   try')                        # Outer try
	try:
		print('Inner    try')                   # Inner try
		print(7 / 0)
		int('Hyd')
		'Hyd'[5]
		eval('Hyd')
	except   ZeroDivisionError:
		print('ZDE   of   inner   try')         # ZDE of inner try
		int('Ten')                              
	except  ValueError:
		print('ValueError  of  inner  try')
	finally:
		print('Inner  try  finally')            # Inner try finally
	print('End  of  inner  try')
except   ValueError:
	print('ValueError  of  outer  try')         # ValueError of outer try
except   IndexError:
	print('IndexError  of  outer  try')
except:
	print('default  except  of  outer  try')
finally:
	print('Outer  try  finally')                # Outer try finally
print('End  of  outer  try')                    # End of outer try



#  Find outputs   (Home  work)
try:
	print('Outer  try')                         # Outer try
	try:
		print('Inner  try')                     # Inner try
		int('Hyd')
		'Hyd'[5]
		eval('Hyd')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try ')    # ValueError of inner try
	finally:
		print('Inner  try  finally')            # Inner try finally
	print('End  of  inner  try')                # End of inner try
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
except:
	print('default except of outer try')
finally:
	print('Outer try finally')                  # Outer try finally
print('End of outer try')                       # End of outer try



#  Find outputs   (Home  work)
try:
	print('Outer  try')                         # Outer try
	try:
		print('Inner  try')                     # Inner try
		'Hyd'[3]
		eval('Hyd')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try ')
	finally:
		print('Inner  try  finally')            # Inner try finally
	print('End  of  inner  try')
except  ValueError:
	print('ValueError  of  outer  try')
except  IndexError:
	print('IndexError  of  outer  try')         # Index of outer try
except:
	print('default except of outer try')
finally:
	print('Outer try finally')                  # Outer try finally
print('End  of  outer  try')                    # End of outer try



#  Find  outputs (Home  work)
try:
	print('Outer  try')                             # Outer try
	try:
		print('Inner  try')                         # Inner try
		eval('Hyd')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')
	finally:
		print('Inner  try  finally')                # Inner try finally
	print('End of inner try')
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
except:
	print('default  except  of  outer  try')        # default except of other try
finally:
	print('Outer  try  finally')                    # Outer try finally
print('End  of  outer  try')                        # End of outer try



#  Find  outputs (Home  work)
try:
	print('Outer  try')                             # Outer try
	try:
		print('Inner  try')                         # Inner try
		print(10 + '20')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')
	finally:
		print('Inner  try  finally')                # Inner try finally
	print('End of inner try')
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
finally:
	print('Outer  try  finally')                    # Outer try finally
print('End  of  outer  try')





# Find  outputs   (Home  work)
class   MyError(BaseException):
	def    _init_(self , y):
		self . a = y
		print('Constructor')
# End of  the class
def  compute(x):
	print(x)                                        # 10
	if  x > 20:
		raise   MyError(x)
	print('Hello')                                  # Hello
# End of  the function
try:
	compute(10)
	compute(30)
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ' ,  msg)   # Caught MyError outside : 30
print('End')                                        # End



# Find  outputs   (Home  work)
class   MyError(NameError):
	def    _init_(self):
		self . a =  25
		print('Constructor')
# End of  the class
def  compute(x):
	print(x)                                        # 30
	if  x > 20:
		raise   MyError()
	print('Hello')
#end of  the functrion
try:
	compute(30)
	compute(10)
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ' ,  msg)   # Caught MyError outside : 30
print('End')                                        # End




# Find  outputs (Home  work)
try:
	print(1)            # 1
	print(2)            # 2
	print(3)            # 3
except:
	print(4)
else:
	print(5)            # 5
finally:
	print(6)            # 6
print(7)                # 7


# Find  outputs   (Home  work)
try:
	print(1)            # 1
	print(7 / 0)
	print(3)
except:
	print(4)            # 4
else:
	print(5)
finally:
	print(6)            # 6
print(7)                # 7


# Find  outputs   (Home  work)
try:
	print(1)            # 1
	print(7 / 0)
	print(3)
except:
	int('Two')
else:
        print(5)
finally:
        print(6)        # 6
print(7)



# Find  outputs (Home  work)
from  threading  import  *
def  f1():
	print('Child thread name:',current_thread().name)       #How  to  print  name  of  child  thread
# main  thread  executes  following  statements
t = Thread(target=f1,name='new')                #How  to  create  a  new  thread  with  name  'new'   and  target  f1
t.start()       #How  to  start  the  new  thread
print('Main thread name:',current_thread().name)    #How  to  print  name  of   main  thread


# Find  outputs (Home  work)
from threading import *
def f():
	pass
t1=Thread(target=f, name='Hyd')     #How  to  create  a  thread  t1  with  name  'Hyd'
t2=Thread(target=f)                 #How  to  create  another  thread  t2  without  a  name
print('Main thread name:',current_thread().name)    #How  to  print  name  of  main  thread
print('Thread t1 name:',t1.name)        #How  to  print  name  of  thread  t1
print('Thread t2 name:',t2.name)        #How  to  print  name  of  thread  t2
current_thread().name='India'           #How  to  modify  name  of  main  thread  to  'India'
t1.name='Sec'       #How  to  modify  name  of  thread  t1  to  'Sec'
t2.name='Cyb'       #How  to  modify  name  of  thread  t2  to  'Cyb'
print('updated main thread name:',current_thread().name)    
print('updated thread t1 name:',t1.name)
print('updated thread t2 name:',t2.name)            #How  to  print  name  of  main  thread
t1.start()      #How  to  print  name  of  thread  t1
t2.start()      #How  to  print  name  of  thread  t2
print('Active thread count:',active_count())        #How  to  print  number  of  threads  under  execution



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

# program continuosly prints Hyd:10 \n Sec:20
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




# Find  outputs (Home  work)
from threading import *
def   disp():
	for  i  in  range(10):
		print('new  thread')            # new thread*10 (10 times)
#  child  thread  is  dead
new = Thread(target = disp)
new . start()
new . join()
for  i  in  range(10):
	print('main  thread')               # main thread*10 (10 times)
# main   thread is  dead



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
output:
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
new  thread
new  thread
new  thread
new  thread
new  thread
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
output:
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
12.01150393486023
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
output:
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
output:
One is started
Two is started
Three is started
MainThread
One
Two
Three
One  is ended
Two  is ended
Three  is ended
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
output:
One is started
Two is started
Three is started
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
	print('Table  :  ' , n)
	for i  in  range(1 , 11):
		print(F'{n}  *  {i}    =   {n * i}')
		time . sleep(1)
t1 = Thread(target = table , args = (7,))
t2 = Thread(target = table , args = (4,))
t1 . start()
t2 . start()


'''
output:
Table  :   7
Table  :   4
7  *  1    =   7
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