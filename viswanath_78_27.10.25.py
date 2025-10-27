Exceptions : 
try:
	print('Hyd')
	print('Sec')
	print('Cyb')
# Error: Missing except or finally block

print(7 / 0) # Error : ZeroDivisionError
try:
	print(7 / 0) # Division  by  zero  is  not  permitted
except ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')
print(7 / 0)  # Error : ZeroDivisionError
print('Bye') # Bye

except:
        print('Hyd')
        print('Sec')
        print('Cyb')
# Error: 'except' block cannot used without a 'try' block

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
# Error: 'except' block cannot appear after statements outside the try block (improper indentation or missing try scope)

try:
	print('try suite')
except:
	print('default  except')
except NameError:
	print('Name  Error')
# Error: default 'except' must be last

try:
	print('try suite')
except:
	print('1st  default  except')
except:
	print('2nd  default  except')
# Error: multiple default 'except' blocks not allowed

#  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0) # ZeroDivisionError: division by zero
print(7 / 0.0) # ZeroDivisionError: float division by zero
print(0 / 0) # ZeroDivisionError: division by zero
print(0.0 / 0.0) # ZeroDivisionError: float division by zero
print(7 // 0) # ZeroDivisionError: integer division or modulo by zero
print(7 % 0) # ZeroDivisionError: integer division or modulo by zero

#  Which  of  the  following  statements  raise  ValueError ?
import math
print(int('10.8'))  # ValueError: invalid literal for int() with base 10: '10.8'
print(float('Ten'))  # ValueError: could not convert string to float: 'Ten'
print(complex('True'))  # ValueError: complex() arg is a malformed string
print(bool('Ten'))  # True
print(bool(''))  # False
print(float('10.8'))  # 10.8
print(float('25'))  # 25.0
print(int(10.8))  # 10
print(math.sqrt(-25))  # ValueError: math domain error

# Which  of  the  following  statements  raise  NameError ?
a = 25
print(a)  # 25
del a
print(a)  # NameError: name 'a' is not defined
print(eval("   'Ten'   "))  # Ten
print(eval('Ten'))  # NameError: name 'Ten' is not defined

# Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0])  # H
print('Hyd'[1])  # y
print('Hyd'[2])  # d
print('Hyd'[3])  # IndexError: string index out of range
list = [10, 20, 15, 18]
print(list[0])  # 10
print(list[3])  # 18
print(list[4])  # IndexError: list index out of range
print(list[-1])  # 18
print(list[-4])  # 10
print(list[-5])  # IndexError: list index out of range
tpl = (10, 20, 30)
print(tpl[3])  # IndexError: tuple index out of range
r = range(10)  
print(r[10])  # IndexError: range object index out of range
s = {10, 20, 15, 18}
print(s[4])  # TypeError: 'set' object is not subscriptable
d = {10: 'Hyd', 20: 'Sec'}
print(d[0])  # KeyError: 0

#  Which  of  the  following  statements  raise TypeError ?
print(10 + 20)  # 30
print('10' + '20')  # 1020
print(10 + '20')  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(len('25'))  # 2
print(len(25))  # TypeError: object of type 'int' has no len()
s = {10, 20, 15, 18}
print(s[0])  # TypeError: 'set' object is not subscriptable
b = { [10, 20]: [30, 40] }  # TypeError: unhashable type: 'list'
print(int(3 + 4j))  # TypeError: can't convert complex to int
print(int([10, 20, 30]))  # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
print(float(None))  # TypeError: float() argument must be a string or a real number, not 'NoneType'

# Which  of  the  following  statements  raise  KeyError ?
a = {'R': 'Red', 'G': 'Green', 'B': 'Blue'}
print(a['G'])  # Green
print(a['Y'])  # KeyError: 'Y'

try:
	print(7 / 0)  
	print('Hello')
except ZeroDivisionError:
	print('ZDE  1')  #  ZDE  1
except ZeroDivisionError:
	print('ZDE  2')
print('Bye')  #  Bye

try:
    print(7 / 0)
    print('Hello')
except ZeroDivisionError:
    print('ZDE 1')  #  ZDE 1
    print(8 / 0)  #  ZeroDivisionError
except ZeroDivisionError:
    print('ZDE 2')
print('Bye')  #  Bye

try:
	print(7 / 0)
	print('Hello')
except ZeroDivisionError:
	print('ZDE  1')  #  ZDE  1
	try:
		print(8 / 0)
	except ZeroDivisionError:
		print('ZDE   2')  #  ZDE   2
	print('Bye')  #  Bye
except ZeroDivisionError:
	print('ZDE  3')
print('End')  #  End

try:
	print(7 / 0)
except ArithmeticError:
	print('Arithmetic Error')  # Arithmetic Error
except ZeroDivisionError:
	print('Zero Division  Error')
print('End')  # End

def f1():
	try:
		print('f1  function')  #  f1  function
		print(7 / 0)
	except ValueError:
		print('Hello')
	try:
		print(int('Ten'))
	except ZeroDivisionError:
		print('Bye')
	print('End  of  f1  function')
# End of f1  function
try:
	print('Begin')  #  # Begin
	f1()
	print('Hi')
except ZeroDivisionError:
	print('ZDE  is  caught  outside')  #  ZDE  is  caught  outside
except:
	print('Bye')
print('End')  #  End

def f1():
	try:
		print('f1  function')  # f1  function
		print(7 / 0)
	except ValueError:
		print('Hello')
	except ZeroDivisionError:
		print('ZDE  is  caught  by  f1  function')  # ZDE  is  caught  by  f1  function
	print('End  of  f1  function')  # End  of  f1  function
# End  of  the  function
try:
	print('Begin')  # Begin
	f1()
	print('Hello')  # Hello
except ZeroDivisionError:
	print("Hi")
except ValueError:
	print("Bye")
print('End')  # End

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
while  True:
	ch = eval(input('Enter  choice (9-exit) : '))
	try:
		match  ch:
			case  1:
				list = [10 , 20 , 15 , 12 , 18]
				print(list[5])  #  Invalid  index
			case  2:
				s = 'Hyd'
				print(s[3])  #  Invalid  index
			case  3:
				print(int('Two'))  #  No  result
			case  4:
				a = 25
				print(len(a))  #  Invalid   argument (or)  operand
			case  5:
				print(eval('Hyd'))  #  Object  does  not  exist
			case  6:
				print(7 / 0)  #  Div by 0 is not allowed
			case  7:
				print(10 + '20')  #  Invalid   argument (or)  operand
			case   8:
				d = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb'}
				print(d[18])  #  Invalid dict key
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

def f1():  
	print('f1  function')  #  f1  function
	raise ValueError('Hyd')
	print('Sec')
# End of  the  function
f1()
try:
	print('Begin')  #  Begin
	f1()  
	print('Bye')

except ValueError as msg:
	print('Caught  ValueError  outside  the  function  :', msg)  #  Caught  ValueError  outside  the  function  :   Hyd
f1()
print('End of the program')  #  End of the program

def f1(a):
	print('f1  function')  # f1  function
	if a == 20:
		raise ArithmeticError()
	elif a == 0:
		raise IndexError()
	elif a == 10:
		raise TypeError(25)
	raise ValueError()
# end of the function
try:
	print('Begin')  # # Begin
	f1(10)
	f1(20)
	f1(30)
	f1(0)
except ArithmeticError:
	print('Hyd')
except IndexError:
	print('Sec')
except TypeError as msg:
	print('Caught  TypeError  outside  the  function :', msg)  # # Caught  TypeError  outside  the  function : 25
except ValueError:
	print('Hello')
except:
	print('some error')
print('End')  # End

def f1(a):
    print('f1  function')  #  f1  function
    if a == 20:
        raise ArithmeticError()
    elif a == 0:
        raise IndexError()
    elif a == 10:
        raise TypeError(25)
    raise ValueError()
# end of the function
try:
    print('Begin')  #  Begin
    f1(10)
    f1(20)
    f1(30)
    f1(0)
except ArithmeticError:
    print('Hyd')
except IndexError:
    print('Sec')
except TypeError as msg:
    print('Caught  TypeError  outside  the  function :', msg)  #  Caught  TypeError  outside  the  function : 25
except ValueError:
    print('Hello')
except:
    print('some error')
print('End')  #  End

def f1(a):
    try:
        if a == 10:
            raise ValueError(25)
        elif a == 20:
            raise NameError(10.8)
        elif a == 30:
            raise IndexError('Hyd')
        raise EOFError(True)
    except IndexError as msg:
        print('Caught  IndexError  : ', msg)
    except ValueError as msg:
        print('Caught  ValueError  : ', msg)
    except NameError as msg:
        print('Caught   NameError  : ', msg)
    except EOFError as msg:
        print('Caught   EOFError  : ', msg)
    print('End  of  f1  function')
# outside the function
f1(10)
f1(20)
f1(30)
f1(0)
print('End of the program')
outputs:
Caught  ValueError  :  25
End  of  f1  function
Caught   NameError  :  10.8
End  of  f1  function
Caught  IndexError  :  Hyd
End  of  f1  function
Caught   EOFError  :  True
End  of  f1  function
End of the program

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
outputs:
Begin
f1 function
Caught  by  f1 function  :  25
Recaught  by  f1 function  :  25
End  of  f1  function
Hyd
End of the program
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
try:
	print('Begin')
	f1()
	print('Hyd')
except  ValueError  as  x:
	print('Recaught ValueError : ' , x)
except:
	print('Some other error')
print('End of the program')
outputs:
Begin
f1 function
Caught  by  f1 function  :   25
Some other error
End of the program

Thread : 
#  Find  outputs  (Home  work)
from  threading  import  Thread
def    f1():
	for  i  in  range(10):
		print('child  thread')
child = Thread(target = f1)
f1()
for  i  in  range(10):
        print('main  thread')
outputs:
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread

#  Find  outputs  (Home  work)
from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')
child = Thread(target =  f1())
child . start()
for  i  in  range(10):
        print('main thread')
outputs:
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread

# Find  outputs  (Home  work)
from  threading  import  *
def   f1():
        for  i  in  range(10):
                print('child  thread')
child = Thread()
child . start()
for  i   in   range(10):
        print('main  thread')
outputs:
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread

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
Error:Thread can be started only once

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
outputs:
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread

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
outputs:
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread

#  Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i   in  range(1 , 11):
			print('Child  Thread  :  ' , i)
child = Thread(How  to  specify  the  target  as  class  method)        #child = Thread(target=c1.m1)
child . start()
for  i  in  range(1 , 11):
        print('Main  Thread  :  ' , i)
outputs:
Child Thread :  1
Main Thread :  1
Child Thread :  2
Main Thread :  2
Main Thread :  3
Child Thread :  3
Main Thread :  4
Child Thread :  4
Child Thread :  5
Main Thread :  5
...
order may vary

# Identify  error  (Home  work)
from  threading  import  Thread
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
# End of the class
t = Thread()
t . start()                                                #Error
for  i  in  range(10):
        print('main  thread')

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
outputs:
Main Thread
Main Thread
Main Thread
Main Thread
Main Thread
Main Thread
Main Thread
Main Thread
Main Thread
Main Thread

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
outputs:
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
child thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread

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
outputs:
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
outputs:
run method
Main Thread

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
outputs:
f1 function:1
Main Thread:1
f1 function:2
Main Thread:2
Main Thread:3
Main Thread:4
Main Thread:5
Main Thread:6
Main Thread:7
Main Thread:8
Main Thread:9
Main Thread:10
f1 function:3
f1 function:4
f1 function:5
f1 function:6
f1 function:7
f1 function:8
f1 function:9
f1 function:10

# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
child = MyThread()
child . start()
print('Main  Thread')                    #Main Thread






