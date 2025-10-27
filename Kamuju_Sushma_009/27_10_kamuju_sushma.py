# Identify  Error  (Home  work)
try:
	print('Hyd')
	print('Sec')
	print('Cyb')
#try alone should not exist

# Find  outputs  (Home  work)
print(7 / 0) #ZeroDivisionError
try:
	print(7 / 0)
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')
print(7 / 0) #ZeroDivisionError
print('Bye') 

# Identify  error  (Home  work)
except:
        print('Hyd')
        print('Sec')
        print('Cyb')
#except alone cannot exist

# Find  outputs (Home  work)
try:
        print('One')
        print('Two')
        print('Three')
# print('Four') #nothing should come between try and
#except
except:
		print('Five')
		print('Six')
		print('Seven')
print('Eight')
#one two three eight

# Find  outputs  (Home work)
try:
	print('try suite')
except:
	print('default  except')
except NameError:
	print('Name  Error')
	
#try suite, none of the except suites are executed
#because no error

# Find  outputs  (Home  work)
try:
	print('try suite')
except:
	print('1st  default  except')
except:
	print('2nd  default  except')
#only one default except suite is allowed

#  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0) #ZeroDivisionError
print(7 / 0.0) #ZeroDivisionError
print(0 / 0) #ZeroDivisionError
print(0.0 / 0.0) #ZeroDivisionError
print(7 // 0)#ZeroDivisionError
print(7 % 0) #ZeroDivisionError

#  Which  of  the  following  statements  raise  ValueError ?  (Home  work)
import  math
print(int('10.8'))
print(float('Ten')) #ValueError
print(complex('True'))#ValueError
print(bool('Ten'))
print(bool(''))
print(float('10.8'))
print(float('25'))#ValueError
print(int(10.8))
print(math . sqrt(-25))#ValueError


'''
When  is  ValueError  raised  ?  --->  When   a  function  (or)  method  does  not  return  any  result
													       i.e. not  even  None
'''

# Which  of  the  following  statements  raise  NameError ?
a = 25
print(a)
del  a
print(a) #NameError
print(eval("   'Ten'   ")) 
print(eval('Ten')) #NameError


'''
When  is  NameError  raised ?  --->  When  a  non-existing  object  is  being  used
'''

# Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0])
print('Hyd'[1])
print('Hyd'[2])
print('Hyd'[3]) #IndexError
list = [10 , 20 , 15 , 18]
print(list[0])
print(list[3])
print(list[4])#IndexError
print(list[-1])
print(list[-4])
print(list[-5])#IndexError
tpl = (10 , 20 , 30)
print(tpl[3])#IndexError
r = range(10)
print(r[10])#IndexError
s = {10 , 20 , 15 , 18}
print(s[4])#there wont be any index
d = {10 : 'Hyd' , 20 : 'Sec'}
print(d[0])#keyerror


'''
When  is  IndexError  raised  ?  --->  When  a  non-existing  index  is  being  used
'''

#  Which  of  the  following  statements  raise TypeError ?
print(10 + 20)
print('10' + '20')
print(10 + '20') #TypeError
print(len('25')) 
print(len(25))#TypeError
s = {10 , 20 , 15 , 18}
print(s[0]) 
b = { [10 , 20] : [30 , 40] }#error keys should be mutable
print(int(3 + 4j)) #TypeError
print(int([10 , 20 , 30]))#TypeError
print(float(None)) #TypeError


'''
When  is  TypeError  raised ? ---> When  the  operands  are  illegal  in  an  expression
																			            (or)
													  when  an  illegal  argument  is  passed  to  the  function (or)  method
'''
# Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G'])
print(a['Y']) #KeyError


'''
When  is  KeyError  raised  ?  ---> When  the  dictionary  key  is  invalid
'''
# Find  outputs  (Home  work)
try:
	print(7 / 0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye')

#ZDE1 Bye

# Find  outputs
try:
	print(7 / 0)
	print('Hello')
except  ZeroDivisionError:
	print('ZDE  1')
	try:
		print(8 / 0)
	except  ZeroDivisionError:
		print('ZDE   2')
	print('Bye')
except  ZeroDivisionError:
	print('ZDE  3')
print('End')

#ZDE1 ZDE2 Bye End

'''
Find  outputs  (Home  work)

Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError
'''
try:
	print(7 / 0)
except   ArithmeticError:
	print('Arithmetic Error')
except   ZeroDivisionError:
	print('Zero Division  Error')
print('End')
#Arithmetic Error

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

#begin, f1 function,  zde is caught outside, end

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

#begin, f1 function, zde is caught by f1 function, end of f1 function, hello, 
#end

'''
What  are   the  outputs  if  input  is  1 ?  --->

What  are   the  outputs  if  input  is  2 ?  --->

What  are   the  outputs  if  input  is  3 ?  --->

What  are   the  outputs  if  input  is  4 ?  --->

What  are   the  outputs  if  input  is  5 ?  --->

What  are   the  outputs  if  input  is  6 ?  --->

What  are   the  outputs  if  input  is  7 ?  --->

What  are   the  outputs  if  input  is  8 ?  --->
'''
# invalid  index, invalid  index, Invalid   argument (or)  operand, Invalid   argument (or)  operand, Object  does  not  exist, Div by 0 is not allowed, Invalid   argument (or)  operand
#Invalid dict key
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
f1() # f1 function, error is reported, sec
try:
	print('Begin') #begin
	f1() 
	print('Bye')
except  ValueError  as  msg:
	print('Caught  ValueError  outside  the  function  :  ' , msg)
	#Caught  ValueError  outside  the  function  : Hyd
f1() #f1 function, error is reported, sec
print('End of the program')

#Find  outputs  (Home  work)
def  f1(a):
	print('f1  function')
	if   a == 20:
		raise  ArithmeticError()
	elif   a == 0:
		raise  IndexError()
	elif  a == 10:
		raise  TypeError(25)
	raise ValueError()
# end of  the function
try:
	print('Begin')
	f1(10) #Caught  TypeError  outside  the  function :  10
	f1(20) #Hyd
	f1(30) #Hello
	f1(0) #sec
except  ArithmeticError:
	print('Hyd')
except  IndexError:
	print('Sec')
except  TypeError  as   msg:
	print('Caught  TypeError  outside  the  function :  '  , msg)
except  ValueError:
	print('Hello')
except:
	print('some error')
print('End') #end

# Find  outputs  (Home  work)
def  f1(a):
	try:
		if   a == 10:
			raise  ValueError(25)
		elif   a == 20:
			raise  NameError(10.8)
		elif   a == 30:
			raise  IndexError('Hyd')
		raise  EOFError(True)
	except  IndexError  as  msg:
		print('Caught  IndexError  :  ' , msg)
	except ValueError  as  msg:
		print('Caught  ValueError  :  ' , msg)
	except  NameError  as  msg:
		print('Caught   NameError  :  ' , msg)
	except  EOFError  as  msg:
		print('Caught   EOFError  :  '  , msg)
	print('End  of  f1  function')
#outside the function
f1(10) #caught valueerror 25
f1(20)# caught nameerror 10.8
f1(30) # caught indexerror hyd
f1(0)#caught eoferror true
print('End of the program') #end of program

#  Find  outputs  (Home  work)
def f1():
	try:
		print('f1 function')
		raise  ValueError(25)
		print('Hi')
	except  ValueError  as  msg:
		try:
			print('Caught  by  f1 function  : ' , msg)
			raise   ValueError(msg)
		except  ValueError  as   msg:
			print('Recaught  by  f1 function  : ' , msg)
	except:
		print('Hello')
	print('End  of  f1  function')
# End  of  f1()  function
try:
	print('Begin') #begin
	f1() #f1 function, caught by f1 function 
	print('Hyd')
except  ValueError  as  x:
	print('Recaught ValueError  :  ' , x) #recaught valueerror 25 
except:
	print('Some other error')
print('End of the program') #end of program

#  Find  outputs  (Home  work)
def f1():
	try:
		print('f1 function')
		raise  ValueError(25)
		print('Hi')
	except  ValueError  as  msg:
		print('Caught  by  f1 function  : ' , msg)
		raise   ValueError(msg)
	except:
		print('Hello')
	print('End  of  f1  function')
# End  of  f1()  function
try:
	print('Begin') #begin 
	f1() #f1 function caught f1 function 25 , recaught valueerror 25
	print('Hyd')
except  ValueError  as  x:
	print('Recaught ValueError  :  ' , x)
except:
	print('Some other error')
print('End of the program') #end of the program

#  Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
	for  i  in  range(10):
		print('child  thread')
child = Thread(target = f1)
f1() 
for  i  in  range(10):
        print('main  thread')
#child thread.. 10 times
#main thread .. 10 times

#  Find  outputs  (Home  work)
from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')
child = Thread(target =  f1())
#child thread 10 times
child . start()
for  i  in  range(10):
        print('main  thread')
#main thread 10 times

# Find  outputs  (Home  work)
from  threading  import  *
def   f1():
        for  i  in  range(10):
                print('child  thread')
child = Thread()
child . start() 
for  i   in   range(10):
        print('main  thread')
# child thread, main thread .. in any order 20 times

# Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
        for  i  in  range(10):
                print('Child  Thread')
child = Thread(target = f1)
child . start()
for  i  in  range(10):
        print('Main  Thread')
child . start()
#main thread ..10 times
#child thread .. 10 times

# Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1() 
child  = Thread(target = a . m1)
child . start()
a . m1() 
for  i  in  range(10):
	print('main  thread')
# child thread, main thread .. in any order 20 times

# Find  outputs (Home  work)
from  threading  import   *
class   c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child = Thread(target =  a . m1())
#child thread .. 10 times
child . start()
for  i  in  range(10):
        print('main  thread')
#main thread .. 10times

#  Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i   in  range(1 , 11):
			print('Child  Thread  :  ' , i)
child = Thread(target=c1.m1) #How  to  specify  the  target  as  class  method)
child . start()
for  i  in  range(1 , 11):
        print('Main  Thread  :  ' , i)
#child thread, main thread ... 20 times in any order

# Identify  error  (Home  work)
from  threading  import  Thread
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
# End of the class
t = Thread()
t . start() # error 
for  i  in  range(10):
        print('main  thread')
#main thread 10 times
# Find  outputs  (Home  work)
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
from  threading  import  Thread
t = Thread()
t . start()
for  i  in  range(10):
        print('Main  Thread')
#main thread 10 times

# Find  outputs  (Home  work)
from threading import *
class    MyThread(Thread):
        def   run(self):
                for  i  in  range(10):
                        print('child  thread')
#end of the class
child = MyThread()
child . run()
for  i  in  range(10):
        print('main  thread')
#child thread, main thread .. 10 times in any order

# Find  outputs (Home  work)
from  threading  import *
class    MyThread(Thread):
	def  walk(self):
		for  i  in  range(10):
			print('walk  method')
child = MyThread()
child . start()
for  i  in  range(10):
	print('Main  Thread')
#main thread .. 10times

# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	def   run(self):
			print('run  method')
def  f1():
	print('f1  function')
child = MyThread(target = f1)
child . start()
print('Main  Thread') 
#run method, main thread

# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
def  f1():
	for  i  in   range(1 , 11):
		print('f1  function : ' , i)
child = MyThread(target = f1)
child . start()
for  i  in  range(1 , 11):
	print('Main  Thread : ' , i)
# main thread, child thread .. 10 times in any order

# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass 
child = MyThread()
child . start()
print('Main  Thread')
#main thread 