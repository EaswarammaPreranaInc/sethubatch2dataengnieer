: # Identify  Error  (Home  work)
try:
	print('Hyd')
	print('Sec')
	print('Cyb')
############################
SyntaxError: expected 'except' or 'finally' block





: # Find  outputs  (Home  work)
print(7 / 0)
try:
	print(7 / 0)
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')
print(7 / 0)
print('Bye')
#####################
ZeroDivisionError: division by zero
Bye



: # Identify  error  (Home  work)
except:
        print('Hyd')
        print('Sec')
        print('Cyb')
###############################
SyntaxError: invalid syntax




: # Find  outputs (Home  work)
try:
        print('One')
        print('Two')
        print('Three')
print('Four') #### IndentationError: expected an indented block after 'try' statement
except:
		print('Five')
		print('Six')
		print('Seven')
print('Eight') 





: # Find  outputs  (Home work)
try:
	print('try suite')
except:
	print('default  except')
except NameError:
	print('Name  Error')

#######################
SyntaxError: default 'except:' must be last



: # Find  outputs  (Home  work)
try:
	print('try suite')
except:
	print('1st  default  except')
except:
	print('2nd  default  except')

############################
SyntaxError: default 'except:' must be last




: #  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0)
print(7 / 0.0)
print(0 / 0)
print(0.0 / 0.0)
print(7 // 0)
print(7 % 0)
######################
| Statement          | Result / Error     | Reason                   |
| ------------------ | ------------------ | ------------------------ |
| `print(7 / 0)`     |  ZeroDivisionError | Integer division by 0    |
| `print(7 / 0.0)`   |  ZeroDivisionError | Float division by 0.0    |
| `print(0 / 0)`     |  ZeroDivisionError | 0 divided by 0 undefined |
| `print(0.0 / 0.0)` |  ZeroDivisionError | Same reason              |
| `print(7 // 0)`    |  ZeroDivisionError | Floor division by 0      |
| `print(7 % 0)`     |  ZeroDivisionError | Modulus by 0             |





: #  Which  of  the  following  statements  raise  ValueError ?  (Home  work)
import  math
print(int('10.8'))
print(float('Ten'))
print(complex('True'))
print(bool('Ten'))
print(bool(''))
print(float('10.8'))
print(float('25'))
print(int(10.8))
print(math . sqrt(-25))


'''
When  is  ValueError  raised  ?  --->  When   a  function  (or)  method  does  not  return  any  result
													       i.e. not  even  None
'''
##################################

| Statement         | Result / Error | Reason                                                        |
| ----------------- | -------------- | ------------------------------------------------------------- |
| `int('10.8')`     |  ValueError   | `'10.8'` is not a valid integer string                        |
| `float('Ten')`    |  ValueError   | `'Ten'` cannot be converted to a float                        |
| `complex('True')` |  ValueError   | `'True'` is not a valid complex number string                 |
| `bool('Ten')`     |  `True`       | Non-empty string → True                                       |
| `bool('')`        |  `False`      | Empty string → False                                          |
| `float('10.8')`   |  `10.8`       | Valid float                                                   |
| `float('25')`     |  `25.0`       | Valid float                                                   |
| `int(10.8)`       |  `10`         | Converts float to int by truncation                           |
| `math.sqrt(-25)`  |  ValueError   | Square root of negative number not allowed (for real numbers) |





: # Which  of  the  following  statements  raise  NameError ?
a = 25
print(a)
del  a
print(a)
print(eval("   'Ten'   "))
print(eval('Ten'))


'''
When  is  NameError  raised ?  --->  When  a  non-existing  object  is  being  used
'''
##########################
| Statement                    | Result / Error     | Reason                           |
| ---------------------------- | ------------------ | -------------------------------- |
| `a = 25`                     |  No error         | Variable created                 |
| `print(a)`                   |  Prints `25`      | Works fine                       |
| `del a`                      |  Deletes variable | OK                               |
| `print(a)`                   |  NameError        | `a` no longer exists             |
| `print(eval("   'Ten'   "))` |  Prints `'Ten'`   | Evaluates string literal `'Ten'` |
| `print(eval('Ten'))`         |  NameError        | Variable `Ten` is undefined      |





: # Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0])
print('Hyd'[1])
print('Hyd'[2])
print('Hyd'[3])
list = [10 , 20 , 15 , 18]
print(list[0])
print(list[3])
print(list[4])
print(list[-1])
print(list[-4])
print(list[-5])
tpl = (10 , 20 , 30)
print(tpl[3])
r = range(10)
print(r[10])
s = {10 , 20 , 15 , 18}
print(s[4])
d = {10 : 'Hyd' , 20 : 'Sec'}
print(d[0])


'''
When  is  IndexError  raised  ?  --->  When  a  non-existing  index  is  being  used
'''
#####################
| Statement                          | Result / Error | Reason                           |
| ---------------------------------- | -------------- | -------------------------------- |
| `'Hyd'[0]`, `'Hyd'[1]`, `'Hyd'[2]` |  OK           | Valid indices                    |
| `'Hyd'[3]`                         |  IndexError   | Index out of range (max index 2) |
| `list[0]`, `list[3]`               |  OK           | Valid indices                    |
| `list[4]`                          |  IndexError   | Out of range                     |
| `list[-1]`, `list[-4]`             |  OK           | Valid negative indices           |
| `list[-5]`                         |  IndexError   | Out of range                     |
| `tpl[3]`                           |  IndexError   | Tuple max index 2                |
| `r[10]`                            |  IndexError   | Range max index 9                |
| `s[4]`                             |  TypeError    | Sets are unordered (no index)    |
| `d[0]`                             |  KeyError     | Key 0 not in dictionary          |





: #  Which  of  the  following  statements  raise TypeError ?
print(10 + 20)
print('10' + '20')
print(10 + '20')
print(len('25'))
print(len(25))
s = {10 , 20 , 15 , 18}
print(s[0])
b = { [10 , 20] : [30 , 40] }
print(int(3 + 4j))
print(int([10 , 20 , 30]))
print(float(None))


'''
When  is  TypeError  raised ? ---> When  the  operands  are  illegal  in  an  expression
																			            (or)
													  when  an  illegal  argument  is  passed  to  the  function (or)  method
'''
##############################
| Statement                  | Result / Error | Reason                                       |
| -------------------------- | -------------- | -------------------------------------------- |
| `10 + 20`                  |  30           | Valid                                        |
| `'10' + '20'`              |  `'1020'`     | String concatenation                         |
| `10 + '20'`                |  TypeError    | Mixing int + str                             |
| `len('25')`                |  2            | Valid                                        |
| `len(25)`                  |  TypeError    | Integer has no length                        |
| `s[0]`                     |  TypeError    | Sets are unordered; can’t use index          |
| `b = { [10,20]: [30,40] }` |  TypeError    | List is unhashable, cannot be dictionary key |
| `int(3 + 4j)`              |  TypeError    | Complex number → cannot convert to int       |
| `int([10,20,30])`          |  TypeError    | List cannot convert to int                   |
| `float(None)`              |  TypeError    | None cannot convert to float                 |






: # Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G'])
print(a['Y'])#### Raises KeyError: print(a['Y'])


'''
When  is  KeyError  raised  ?  ---> When  the  dictionary  key  is  invalid
'''



: # Find  outputs  (Home  work)
try:
	print(7 / 0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye')

#######################
SyntaxError: default 'except:' must be last (duplicate except)




: # Find  outputs  (Home  work)
try:
	print(7 / 0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')
	print(8 / 0)
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye')

#####################
SyntaxError: duplicate except block



: # Find  outputs
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
###########################
ZDE  1
ZDE  2
Bye
End




: '''
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
#####################
Arithmetic Error
End




: # Find  outputs  (Home  work)
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

######################
Begin
f1  function
ZDE  is  caught  outside
End




: # Find  outputs  (Home  work)
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
#########################
Begin
f1  function
ZDE  is  caught  by  f1  function
End  of  f1  function
Hello
End



: '''
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

#####################################
| Input | Error Raised                | Output Message                  |
| ----- | --------------------------- | ------------------------------- |
| **1** | `IndexError` (`list[5]`)    | `Invalid  index`                |
| **2** | `IndexError` (`s[3]`)       | `Invalid  index`                |
| **3** | `ValueError` (`int('Two')`) | `No  result`                    |
| **4** | `TypeError` (`len(25)`)     | `Invalid argument (or) operand` |
| **5** | `NameError` (`eval('Hyd')`) | `Object does not exist`         |
| **6** | `ZeroDivisionError` (`7/0`) | `Div by 0 is not allowed`       |
| **7** | `TypeError` (`10 + '20'`)   | `Invalid argument (or) operand` |
| **8** | `KeyError` (`d[18]`)        | `Invalid dict key`              |
| **9** | program exits               | —                               |





: #  Find  outputs
def  f1():
	print('f1  function')
	raise   ValueError('Hyd')
	print('Sec')
# End of  the  function
f1()
try:
	print('Begin')
	f1()
	print('Bye')
except  ValueError  as  msg:
	print('Caught  ValueError  outside  the  function  :  ' , msg)
f1()
print('End of the program')
######################
f1  function
Traceback (most recent call last):
  ...
ValueError: Hyd





: #Find  outputs  (Home  work)
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

###########################
Begin
f1  function
Caught  TypeError  outside  the  function :  25
End




: # Find  outputs  (Home  work)
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
#################################
| Input | Exception           | Output                       |
| ----- | ------------------- | ---------------------------- |
| 10    | `ValueError(25)`    | `Caught  ValueError  :  25`  |
| 20    | `NameError(10.8)`   | `Caught  NameError  :  10.8` |
| 30    | `IndexError('Hyd')` | `Caught  IndexError  :  Hyd` |
| 0     | `EOFError(True)`    | `Caught  EOFError  :  True`  |

Caught  ValueError  :  25
End  of  f1  function
Caught  NameError  :  10.8
End  of  f1  function
Caught  IndexError  :  Hyd
End  of  f1  function
Caught  EOFError  :  True
End  of  f1  function
End of the program






: #  Find  outputs  (Home  work)
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

#####################################

Begin
f1 function
Caught  by  f1 function  :  25
Recaught  by  f1 function  :  25
End  of  f1  function
Hyd
End of the program





: #  Find  outputs  (Home  work)
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
######################################
child thread
child thread
...
(child thread printed 10 times)
main thread
main thread
...
(main thread printed 10 times)




: # Find  outputs  (Home   work)
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

################################
child thread (10 times)
main thread (10 times)




: #  Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
	for  i  in  range(10):
		print('child  thread')
child = Thread(target = f1)
f1()
for  i  in  range(10):
        print('main  thread')
######################################
main thread
main thread
...
(main thread printed 10 times)



: #  Find  outputs  (Home  work)
from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')
child = Thread(target =  f1())
child . start()
for  i  in  range(10):
        print('main  thread')
############################################
Child Thread
Main Thread
(interleaved output)
RuntimeError: threads can only be started once




: # Find  outputs  (Home  work)
from  threading  import  *
def   f1():
        for  i  in  range(10):
                print('child  thread')
child = Thread()
child . start()
for  i   in   range(10):
        print('main  thread')
########################
main thread
main thread
...
(main thread printed 10 times)




: # Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
        for  i  in  range(10):
                print('Child  Thread')
child = Thread(target = f1)
child . start()
for  i  in  range(10):
        print('Main  Thread')
child . start()
############################
Child Thread
Main Thread
(interleaved order)
RuntimeError: threads can only be started once



: # Find  outputs  (Home  work)
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
################################
child thread
child thread
(main + child threads mixed)
main thread
main thread
...



: # Find  outputs (Home  work)
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

###########################
child thread   (×10)
main thread    (×10)



: #  Find  outputs  (Home  work)
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

################################
Child Thread : 1
Main Thread : 1
Child Thread : 2
Main Thread : 2
...
child = Thread(target=c1.m1)  #  this is the right syntax




: # Identify  error  (Home  work)
from  threading  import  Thread
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
# End of the class
t = Thread()
t . start()
for  i  in  range(10):
        print('main  thread')
######################################
AttributeError: 'Thread' object has no attribute 'start'




: # Find  outputs  (Home  work)
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
from  threading  import  Thread
t = Thread()
t . start()
for  i  in  range(10):
        print('Main  Thread')
########################################
Main Thread  (×10)




: # Find  outputs  (Home  work)
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

###################################
child thread (×10)
main thread  (×10)




: # Find  outputs (Home  work)
from  threading  import *
class    MyThread(Thread):
	def  walk(self):
		for  i  in  range(10):
			print('walk  method')
child = MyThread()
child . start()
for  i  in  range(10):
	print('Main  Thread')
#######################################
Main Thread  (×10)




: # Find  outputs
from  threading  import  *
class   MyThread(Thread):
	def   run(self):
			print('run  method')
def  f1():
	print('f1  function')
child = MyThread(target = f1)
child . start()
print('Main  Thread')
##################################
run method
Main Thread



: # Find  outputs
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
###############################################
f1 function : 1
Main Thread : 1
f1 function : 2
Main Thread : 2
...




: # Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
child = MyThread()
child . start()
print('Main  Thread')
###################################
Main Thread
