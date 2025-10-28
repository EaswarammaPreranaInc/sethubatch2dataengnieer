# Identify  Error  (Home  work)
try:
	print('Hyd')
	print('Sec')
	print('Cyb')

'''
there is no except for try suite
'''

# Find  outputs  (Home  work)
print(7 / 0)
try:
	print(7 / 0)
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')
print(7 / 0)
print('Bye')

'''
statements outside the try suite raises the error as they are not in try suite error is reported
'''
# Identify  error  (Home  work)
except:
        print('Hyd')
        print('Sec')
        print('Cyb')
'''
there is no  try for except suite
'''

# Find  outputs (Home  work)
try:
        print('One')
        print('Two')
        print('Three')
print('Four')
except:
		print('Five')
		print('Six')
		print('Seven')
print('Eight')

'''
try suite prints one,two,three and  between try and except there should not be any statement and eight is printed
'''

# Find  outputs  (Home work)
try:
	print('try suite')
except:
	print('default  except')
except NameError:
	print('Name  Error')
'''
error as default except should always be at last
'''

# Find  outputs  (Home  work)
try:
	print('try suite')
except:
	print('1st  default  except')
except:
	print('2nd  default  except')

'''
error only one default suite should be there
'''

#  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0)
print(7 / 0.0)
print(0 / 0)
print(0.0 / 0.0)
print(7 // 0)
print(7 % 0)

'''
all raise zero division error as we are performing division with 0 in all cases
'''

#  Which  of  the  following  statements  raise  ValueError ?  (Home  work)
import  math
print(int('10.8'))	# vakue eror as float string cant be directly converted to int
print(float('Ten'))	# error as string cant be converted to floast
print(complex('True'))	# error as complex demands int or float
print(bool('Ten'))	# true as non empty string
print(bool(''))		# false empty string
print(float('10.8'))	# string float is conerted to float
print(float('25'))	# string int is converted to int
print(int(10.8))	# FLOAT IS converted to int
print(math . sqrt(-25))	# ERROR  as argument for sqrt should be positive


'''
When  is  ValueError  raised  ?  --->  When   a  function  (or)  method  does  not  return  any  result
													       i.e. not  even  None
'''

# Which  of  the  following  statements  raise  NameError ?
a = 25
print(a)	# 25
del  a
print(a)	# error as a is already deleted and we are printing the non existing object
print(eval("   'Ten'   "))	# 'Ten'
print(eval('Ten'))	# error as we don't have object ten in the current prgm


'''
When  is  NameError  raised ?  --->  When  a  non-existing  object  is  being  used
'''


# Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0])	# h
print('Hyd'[1]	# y
print('Hyd'[2])	# d
print('Hyd'[3])	# index error as there is no 3rd index element in hyd
list = [10 , 20 , 15 , 18]
print(list[0])	# 10
print(list[3])	# 18
print(list[4])	# error as in a list of 4 elements index varies from 0 to 3
print(list[-1])	# 18
print(list[-4])	#10
print(list[-5])	# index error as negative index vary from -1 to -4
tpl = (10 , 20 , 30)
print(tpl[3])	# error there is no 4th element in tuple
r = range(10)	
print(r[10])	# for range(10) index will be from 0 to 9
s = {10 , 20 , 15 , 18}
print(s[4])	# error as set is not indexed
d = {10 : 'Hyd' , 20 : 'Sec'}
print(d[0]) #  key error as ther Is no key 0


'''
When  is  IndexError  raised  ?  --->  When  a  non-existing  index  is  being  used
'''


#  Which  of  the  following  statements  raise TypeError ?
print(10 + 20)	# 30
print('10' + '20')	# 1020
print(10 + '20')	# error as operand 2 should be int class
print(len('25'))	# 2
print(len(25))	# error as argument of len function should be sequence
s = {10 , 20 , 15 , 18}
print(s[0])	# error as set is not indexed
b = { [10 , 20] : [30 , 40] }	 # error as key should be immutable
print(int(3 + 4j))	# error as converting complex to int is not possible	
print(int([10 , 20 , 30]))	# error as we cant convert list to int
print(float(None))	# error as none cant be converted to float


'''
When  is  TypeError  raised ? ---> When  the  operands  are  illegal  in  an  expression
																			            (or)
													  when  an  illegal  argument  is  passed  to  the  function (or)  method
'''

# Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G'])	# Green is printed
print(a['Y'])	# keyerror as there is no key y


'''
When  is  KeyError  raised  ?  ---> When  the  dictionary  key  is  invalid
'''

# Find  outputs  (Home  work)
try:
	print(7 / 0)	# zerodivisionerror so go to except suite
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')		# 1st except suite is executed
except    ZeroDivisionError:
	print('ZDE  2')	
print('Bye')	# prints bye

# Find  outputs  (Home  work)
try:
	print(7 / 0)    # error is raised
	print('Hello')
except    ZeroDivisionError:    # except suite is executed
	print('ZDE  1')
	print(8 / 0)        # error is raised br=eacuse it is except suite not try suite
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye')

# Find  outputs
try:
	print(7 / 0) # error is raised
	print('Hello')
except  ZeroDivisionError:	# except suite is executed
	print('ZDE  1')
	try:
		print(8 / 0)	 # error is raised
	except  ZeroDivisionError:
		print('ZDE   2')	# except suite is executed
	print('Bye')	# prints bye 1st
except  ZeroDivisionError:
	print('ZDE  3')
print('End')	# prints end last

'''
Find  outputs  (Home  work)

Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError
'''
try:
	print(7 / 0)
except   ArithmeticError:
	print('Arithmetic Error')	# parent escept should be at last
except   ZeroDivisionError:
	print('Zero Division  Error')	# child error should be catched 1st before parent
print('End')
'''
if not for even child error is raised parent error except suite is executed
'''
# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')
		print(7 / 0)
	except  ValueError:
		print('Hello')
	try:
		print(int('Ten'))
	except ZeroDivisionError:
		print('Bye')
	print('End  of  f1  function')
# End of f1  function
try:
	print('Begin')
	f1()
	print('Hi')
except  ZeroDivisionError:
	print('ZDE  is  caught  outside')
except:
	print('Bye')
print('End')

'''
f1 function is executed and prints "f1 function".
go to f1 function
zero division error occurs while executing print(7 / 0) statement.
so except suite for ValueError is skipped as the exception is ZeroDivisionError.
next except suite for ZeroDivisionError is also skipped as it is not in f1 function.
so control goes to the except suite outside f1 function as whole function is in try suite
and the end.
'''

# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')
		print(7 / 0)
	except  ValueError:
		print('Hello')
	except  ZeroDivisionError:
		print('ZDE  is  caught  by  f1  function')
	print('End  of  f1  function')
# End  of  the  function
try:
	print('Begin')
	f1()
	print('Hello')
except  ZeroDivisionError:
	print("Hi")
except  ValueError:
	print("Bye")
print('End')

'''
as the 7/0 is in try suite inside function and has corresponding except suite is executed and after function termination hello is printed and end

'''
'''
What  are   the  outputs  if  input  is  1 ?  ---> Invalid  index

What  are   the  outputs  if  input  is  2 ?  ---> Invalid  index

What  are   the  outputs  if  input  is  3 ?  ---> No  result

What  are   the  outputs  if  input  is  4 ?  ---> Invalid   argument (or)  operand

What  are   the  outputs  if  input  is  5 ?  ---> Object  does  not  exist

What  are   the  outputs  if  input  is  6 ?  ---> Div by 0 is not allowed

What  are   the  outputs  if  input  is  7 ?  ---> Invalid   argument (or)  operand

What  are   the  outputs  if  input  is  8 ?  ---> Invalid dict key
'''
while  True:
	ch = eval(input('Enter  choice (9-exit) : '))
	try:
		match  ch:
			case  1:
				list = [10 , 20 , 15 , 12 , 18]
				print(list[5])
			case  2:
				s = 'Hyd'
				print(s[3])
			case  3:
				print(int('Two'))
			case  4:
				a = 25
				print(len(a))
			case  5:
				print(eval('Hyd'))
			case  6:
				print(7 / 0)
			case  7:
				print(10 + '20')
			case   8:
				d = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb'}
				print(d[18])
			case   9:
				exit()
	except   ZeroDivisionError:
		print('Div by 0 is not allowed')
	except  ValueError:
		print('No  result')
	except  IndexError:
		print('Invalid  index')
	except  TypeError:
		print('Invalid   argument (or)  operand')
	except  KeyError:
		print('Invalid dict key')
	except  NameError:
		print('Object  does  not  exist')
	except:
		print('A new error')	
# End of while loop
print('Bye')

#  Find  outputs
def  f1():
	print('f1  function')
	raise   ValueError('Hyd')
	print('Sec')
# End of  the  function
f1()    # function call
# as f1 is not in try suote the value error will not be caught and error is raised
try:
	print('Begin')
	f1()    # function call is in try block funtion raises value error and except block catches it
	print('Bye')
except  ValueError  as  msg:
	print('Caught  ValueError  outside  the  function  :  ' , msg)  # pritns mdg
f1() # as f1 is not in try suote the value error will not be caught and error is raised
print('End of the program') # prints end of program

#Find  outputs  (Home  work)
def  f1(a):
	print('f1  function')   # f1  function  is  printed
	if   a == 20:
		raise  ArithmeticError()
	elif   a == 0:
		raise  IndexError()
	elif  a == 10:  # true  when  a  is  10
		raise  TypeError(25)    # error  is  raised  with  message  25
	raise ValueError()
# end of  the function
try:
	print('Begin')  # begin is printed
	f1(10)  # f1 is called with 10
	f1(20)
	f1(30)
	f1(0)
except  ArithmeticError:
	print('Hyd');
except  IndexError:
	print('Sec')
except  TypeError  as   msg:    # catches  TypeError
	print('Caught  TypeError  outside  the  function :  '  , msg)    # printes msg
except  ValueError:
	print('Hello')
except:
	print('some error')
print('End')

# Find  outputs  (Home  work)
def  f1(a):
	try:
		if   a == 10:
			raise  ValueError(25)   # raising ValueError with 25
		elif   a == 20:
			raise  NameError(10.8)  # raising NameError with 10.8
		elif   a == 30:
			raise  IndexError('Hyd')    # raising IndexError with 'Hyd'
		raise  EOFError(True)   # raising EOFError with True
	except  IndexError  as  msg:
		print('Caught  IndexError  :  ' , msg)  # catching IndexError is printed 3rd
	except ValueError  as  msg:
		print('Caught  ValueError  :  ' , msg)  # catching ValueError is printed 1st
	except  NameError  as  msg:
		print('Caught   NameError  :  ' , msg)  # catching NameError is printed 2nd
	except  EOFError  as  msg:
		print('Caught   EOFError  :  '  , msg)  # catching EOFError is printed 4th
	print('End  of  f1  function')     # End of f1 function us prinred every fucntion call
#outside the function
f1(10)  # f1 function  called  with 10
f1(20)  # f1 function  called  with 20
f1(30)  # f1 function  called  with 30
f1(0)   # f1 function  called  with 0
print('End of the program') # End of the program


#  Find  outputs  (Home  work)
def f1():
	try:
		print('f1 function')    #  f1 function
		raise  ValueError(25)   # raising valueerror explicitly
		print('Hi')
	except  ValueError  as  msg:  
		try:
			print('Caught  by  f1 function  : ' , msg)  # Caught by f1 function
			raise   ValueError(msg)  #  Re-raising  the  same  exception so except suite outside f1() can catch it
		except  ValueError  as   msg:
			print('Recaught  by  f1 function  : ' , msg)    # Recaught ValueError
	except:
		print('Hello')
	print('End  of  f1  function')
# End  of  f1()  function
try:
	print('Begin')  #  Begin
	f1()    # Call f1 function
	print('Hyd')
except  ValueError  as  x:
	print('Recaught ValueError  :  ' , x)   
except:
	print('Some other error')
print('End of the program') # End of the program




#  Find  outputs  (Home  work)
def f1():
	try:
		print('f1 function')    #  f1 function
		raise  ValueError(25)   #  Raise  ValueError
		print('Hi')
	except  ValueError  as  msg:
		print('Caught  by  f1 function  : ' , msg) #  Caught  by  f1 function with 25 as msg
		raise   ValueError(msg) #  Re-raise  the  ValueError
	except:
		print('Hello')
	print('End  of  f1  function')
# End  of  f1()  function
try:
	print('Begin')  #  Begin
	f1()    # Call f1 function
	print('Hyd')
except  ValueError  as  x:
	print('Recaught ValueError  :  ' , x) #  Recaught ValueError with 25 as x
except:
	print('Some other error')
print('End of the program') # End of the program


#  Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
	for  i  in  range(10):
		print('child  thread')  # printed 10 times
child = Thread(target = f1) # xCreate  thread  object but not  started
f1()    #  Call  function  in  main  thread
for  i  in  range(10):
        print('main  thread')   # printed 10 times
		
'''
 as child thread is not started so function f1() is called in main thread only.'''

#  Find  outputs  (Home  work)
from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')
child = Thread(target =  f1())  # create  thread  object and f1 us executed as target is result of f1()
child . start() # start  thread and does nothing  as  f1  is  returning none
for  i  in  range(10):
        print('main  thread')   # main  thread  prints 10 times


# Find  outputs  (Home  work)
from  threading  import  *
def   f1():
        for  i  in  range(10):
                print('child  thread')
child = Thread()    # thread cladss object is created
child . start() # thread  is  started and empty run method is called
for  i   in   range(10):
        print('main  thread')   # main  thread  is printed 10 times

# Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
        for  i  in  range(10):
                print('Child  Thread')  # print  statement  in  child  thread 10  times
child = Thread(target = f1) # create  thread  object 
child . start() # start  thread
for  i  in  range(10):
        print('Main  Thread') # print  statement  in  main  thread 10  times
child . start() # eror as child thread is already started

# Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')  # print  child  thread 10  times
a = c1()    # c1 class object
child  = Thread(target = a . m1)    # create  thread  object with  target  as m1 method  of  c1  class 
child . start() # start  the  thread  which  invokes
a . m1()    # main  thread  calls  m1  method
for  i  in  range(10):
	print('main  thread')   # print  main  thread 10  times

# Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')  # print  child  thread 10  times
a = c1()    # c1 class object
child  = Thread(target = a . m1)    # create  thread  object with  target  as m1 method  of  c1  class 
child . start() # start  the  thread  which  invokes m1  method

for  i  in  range(10):
	print('main  thread')   # print  main  thread 10  times



#  Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i   in  range(1 , 11):
			print('Child  Thread  :  ' , i)
child = Thread(target = c1 . m1)    #How  to  specify  the  target  as  class  method)
child . start()
for  i  in  range(1 , 11):
        print('Main  Thread  :  ' , i)

# Identify  error  (Home  work)
from  threading  import  Thread
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
# End of the class
t = Thread()    # thread class object is created 
t . start() # terror as there is no start method in Thread class
for  i  in  range(10):
        print('main  thread')

# Find  outputs  (Home  work)
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
from  threading  import  Thread # thread is imported
t = Thread()    # thread clas object  is  created
t . start() #  thread  is  started and empty run()  method  is  called
for  i  in  range(10):
        print('Main  Thread')   # main thread  is printed 10 times

# Find  outputs  (Home  work)
from threading import *
class    MyThread(Thread):
        def   run(self):
                for  i  in  range(10):
                        print('child  thread')      # print  child  thread 10n times
#end of the class
child = MyThread()  # Create  thread  object of mythread class
child . run()   #  start  the  thread and  call  run  method of mythread class
for  i  in  range(10):
        print('main  thread')     # print  main  thread 10n times

# Find  outputs (Home  work)
from  threading  import *
class    MyThread(Thread):
	def  walk(self):
		for  i  in  range(10):
			print('walk  method')
child = MyThread()  # Create  thread  object
child . start() #  as there is no target empty  run  method  of  Thread  class  will  be  executed
for  i  in  range(10):
	print('Main  Thread')   # Main  thread  is printed 10 times

# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	def   run(self):
			print('run  method')    # run  method  has  highest  priority
def  f1():
	print('f1  function')
child = MyThread(target = f1)   # Create  thread  object
child . start() # even thogugh target is given f1 is not executed because run method is defined in MyThread class and it has highest priority
print('Main  Thread')   # Main  thread  execution


# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
def  f1():
	for  i  in   range(1 , 11):
		print('f1  function : ' , i)    # Print  from  f1  function
child = MyThread(target = f1)   # Create  thread  object
child . start() # Start  thread  execution
for  i  in  range(1 , 11):
	print('Main  Thread : ' , i)        # Print  from  main  thread

# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
child = MyThread()  # create  object  of  MyThread  class
child . start() # start  child  thread and empty run  method  of  Thread  class  will  be  executed
print('Main  Thread')