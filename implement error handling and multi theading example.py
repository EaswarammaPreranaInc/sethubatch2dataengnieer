# Identify  Error  (Home  work)
try: # Error due to try cannot use without except
	print('Hyd')
	print('Sec')
	print('Cyb')


# Find  outputs  (Home  work)
print(7 / 0) # ZeroDevisionError can be can be raised
try:
	print(7 / 0)
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')
print(7 / 0)   # ZeroDevisionError can be can be raised
print('Bye')


# Identify  error  (Home  work)
except: # Error due to except cannot use without try
        print('Hyd')
        print('Sec')
        print('Cyb')


# Find  outputs (Home  work)
try:
        print('One')
        print('Two')
        print('Three')
#print('Four') # Error due to after try followed by except or finally 
except:
		print('Five')
		print('Six')
		print('Seven')
print('Eight')

# Output:
One
Two
Three
Eight


# Find  outputs  (Home work)
try:
	print('try suite')
except: # Error due default except should be use in last after another error except block
	print('default  except')
except NameError:
	print('Name  Error')


# Find  outputs  (Home  work)
try:
	print('try suite')
except:
	print('1st  default  except')
except: # Error due to only one or zero default except block can be used
	print('2nd  default  except')


#  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0) # ZeroErrorDevision can be raised
print(7 / 0.0) # ZeroErrorDevision can be raised
print(0 / 0) # ZeroErrorDevision can be raised
print(0.0 / 0.0) # ZeroErrorDevision can be raised
print(7 // 0) # ZeroErrorDevision can be raised
print(7 % 0) # ZeroErrorDevision can be raised


#  Which  of  the  following  statements  raise  ValueError ?  (Home  work)
import  math
print(int('10.8')) # ValueError can be raised
print(float('Ten')) # ValueError can be raised
print(complex('True')) # ValueError can be raised
print(bool('Ten')) # True
print(bool('')) # False
print(float('10.8')) # 1o.8
print(float('25')) # 25.0
print(int(10.8)) # 10
print(math . sqrt(-25)) # ValueError can be raised


'''
When  is  ValueError  raised  ?  --->  When   a  function  (or)  method  does  not  return  any  result
													       i.e. not  even  None
'''


# Which  of  the  following  statements  raise  NameError ?
a = 25
print(a)
del  a
print(a) # NameError can be raised
print(eval("   'Ten'   "))
print(eval('Ten')) # NameError can be raised


'''
When  is  NameError  raised ?  --->  When  a  non-existing  object  is  being  used
'''


# Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0])
print('Hyd'[1])
print('Hyd'[2])
print('Hyd'[3]) # IndexError can be raised
list = [10 , 20 , 15 , 18]
print(list[0])
print(list[3])
print(list[4]) # IndexError can be raised
print(list[-1])
print(list[-4])
print(list[-5]) # IndexError can be raised
tpl = (10 , 20 , 30)
print(tpl[3]) # IndexError can be raised
r = range(10)
print(r[10]) # IndexError can be raised
s = {10 , 20 , 15 , 18}
print(s[4]) # Set cannot be Subscripted
d = {10 : 'Hyd' , 20 : 'Sec'}
print(d[0]) # KeyError can be raised


'''
When  is  IndexError  raised  ?  --->  When  a  non-existing  index  is  being  used
'''


#  Which  of  the  following  statements  raise TypeError ?
print(10 + 20) # 30
print('10' + '20') # 1020
print(10 + '20') # TypeError can be raised
print(len('25'))
print(len(25)) # TypeError can be raised
s = {10 , 20 , 15 , 18}
print(s[0]) # Set cannot be Subscripted
b = { [10 , 20] : [30 , 40] } # key must be immutable 
print(int(3 + 4j)) # TypeError can be raised
print(int([10 , 20 , 30])) # TypeError can be raised
print(float(None)) # TypeError can be raised


'''
When  is  TypeError  raised ? ---> When  the  operands  are  illegal  in  an  expression
																			            (or)
													  when  an  illegal  argument  is  passed  to  the  function (or)  method
'''

# Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G'])
print(a['Y']) # KeyError can be raised


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

# Output :
ZDE  1
Bye


# Find  outputs  (Home  work)
try:
	print(7 / 0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')
	print(8 / 0) # ZeroDevisionError can be raised
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye')


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
#except  ZeroDivisionError: # Error due to only one or zero default except can be used
	print('ZDE  3')
print('End')

# Output :
ZDE 1
ZDE 2
ZDE 3
End


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

# Output :
ArithmeticError
End

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

# Output :
Begin
f1  function
ZDE  is  caught  outside
End


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

# Output :
Begin
f1  function
ZDE  is  caught  by  f1  function
End  of  f1  function
Hello
End


'''
What  are   the  outputs  if  input  is  1 ?  ---> # Invalid  index

What  are   the  outputs  if  input  is  2 ?  ---> # Invalid  index

What  are   the  outputs  if  input  is  3 ?  ---> # No  result

What  are   the  outputs  if  input  is  4 ?  ---> # Invalid   argument (or)  operand

What  are   the  outputs  if  input  is  5 ?  ---> # Object  does  not  exist

What  are   the  outputs  if  input  is  6 ?  ---> # Div by 0 is not allowed

What  are   the  outputs  if  input  is  7 ?  ---> # Invalid   argument (or)  operand

What  are   the  outputs  if  input  is  8 ?  ---> # Invalid dict key
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
#f1() # Error can be raised
try:
	print('Begin')
	f1()
	print('Bye')
except  ValueError  as  msg:
	print('Caught  ValueError  outside  the  function  :  ' , msg)
#f1() # Error can be raised
print('End of the program')

# Output :
Begin
f1  function
Caught  ValueError  outside  the  function  :   Hyd
End of the program

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
	f1(10)
	f1(20)
	f1(30)
	f1(0)
except  ArithmeticError:
	print('Hyd');
except  IndexError:
	print('Sec')
except  TypeError  as   msg:
	print('Caught  TypeError  outside  the  function :  '  , msg)
except  ValueError:
	print('Hello')
except:
	print('some error')
print('End')

# Output :
Begin
f1  function
Caught  TypeError  outside  the  function :   25
End


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
f1(10)
f1(20)
f1(30)
f1(0)
print('End of the program')

# Output :
Caught  ValueError  :   25
End  of  f1  function
Caught   NameError  :   10.8
End  of  f1  function
Caught  IndexError  :   Hyd
End  of  f1  function
Caught   EOFError  :   True
End  of  f1  function
End of the program


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
	print('Begin')
	f1()
	print('Hyd')
except  ValueError  as  x:
	print('Recaught ValueError  :  ' , x)
except:
	print('Some other error')
print('End of the program')

# Output :
Begin
f1 function
Caught  by  f1 function  :  25
Recaught  by  f1 function  :  25
End  of  f1  function
Hyd
End of the program


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
	print('Begin')
	f1()
	print('Hyd')
except  ValueError  as  x:
	print('Recaught ValueError  :  ' , x)
except:
	print('Some other error')
print('End of the program')

# Output :
Begin
f1 function
Caught  by  f1 function  :  25
Recaught ValueError  :   25
End of the program

# Find  outputs  (Home   work)
def f1():
	try:
		print('f1 function')
		raise  ValueError(25)
		print('Hi')
	except  ValueError  as  msg:
		print('Caught  by  f1 function  :  ' , msg)
		raise  NameError(msg)
	except:
		print('Hello')
	print('End of f1 function')
# End  of  the  function
try:
	print('Begin')
	f1()
	print('Hyd')
except  ValueError  as  x:
	print('Recaught ValueError : ' , x)
except:
	print('Some other error')
print('End of the program')

# Output :
Begin
f1 function
Caught  by  f1 function  :   25
Some other error
End of the program


#  Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
	for  i  in  range(10):
		print('child  thread')
child = Thread(target = f1)
f1()
for  i  in  range(10):
        print('main  thread')

# Output :
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
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


#  Find  outputs  (Home  work)
from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')
child = Thread(target =  f1())
child . start()
for  i  in  range(10):
        print('main  thread')

# Output :
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
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


# Find  outputs  (Home  work)
from  threading  import  *
def   f1():
        for  i  in  range(10):
                print('child  thread')
child = Thread()
child . start()
for  i   in   range(10):
        print('main  thread')

# Output :
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
from  threading  import  Thread
def    f1():
        for  i  in  range(10):
                print('Child  Thread')
child = Thread(target = f1)
child . start()
for  i  in  range(10):
        print('Main  Thread')
#child . start() # Error

# Output :
Child  Thread
Main  Thread
Child  Thread
Main  Thread
Child  Thread
Main  Thread
Child  Thread
Main  Thread
Child  Thread
Main  Thread
Child  Thread
Main  Thread
Child  Thread
Main  Thread
Child  Thread
Main  Thread
Child  Thread
Main  Thread
Child  Thread
Main  Thread


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

# Output :
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
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
from  threading  import   *
class   c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child = Thread(target =  a . m1())
child . start()
for  i  in  range(10):
        print('main  thread')

# Output :
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
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


#  Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i   in  range(1 , 11):
			print('Child  Thread  :  ' , i)
child = Thread(How  to  specify  the  target  as  class  method)
child . start()
for  i  in  range(1 , 11):
        print('Main  Thread  :  ' , i)

# Output :
Child  Thread  :   1
Main  Thread  :   1
Child  Thread  :   2
Main  Thread  :   2
Child  Thread  :   3
Main  Thread  :   3
Child  Thread  :   4
Main  Thread  :   4
Child  Thread  :   5
Main  Thread  :   5
Child  Thread  :   6
Main  Thread  :   6
Child  Thread  :   7
Main  Thread  :   7
Child  Thread  :   8
Main  Thread  :   8
Child  Thread  :   9
Child  Thread  :   10
Main  Thread  :   9
Main  Thread  :   10


# Identify  error  (Home  work)
from  threading  import  Thread
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
# End of the class
t = Thread()
#t . start() # Error
for  i  in  range(10):
        print('main  thread')

# Output :
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

# Output :
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread


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

# Output :
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
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
from  threading  import *
class    MyThread(Thread):
	def  walk(self):
		for  i  in  range(10):
			print('walk  method')
child = MyThread()
child . start()
for  i  in  range(10):
	print('Main  Thread')

# Output :
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread


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

# Output :
run  method
Main  Thread


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

# Output :
f1  function :  1
Main  Thread :  1
f1  function :  2
Main  Thread :  2
f1  function :  3
Main  Thread :  3
f1  function :  4
Main  Thread :  4
f1  function :  5
Main  Thread :  5
f1  function :  6
Main  Thread :  6
f1  function :  7
Main  Thread :  7
Main  Thread :  8
f1  function :  8
Main  Thread :  9
f1  function :  9
Main  Thread :  10
f1  function :  10

# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
child = MyThread()
child . start()
print('Main  Thread')

# Output :
Main  Thread
