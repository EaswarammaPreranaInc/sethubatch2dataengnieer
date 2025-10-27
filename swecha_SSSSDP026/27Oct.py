# Identify  Error  (Home  work)
try:
	print('Hyd')
	print('Sec')
	print('Cyb')
'we cannot use only try suite without except '
# Find  outputs  (Home  work)
#print(7 / 0)#error ZDE
try:
	print(7 / 0)
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')#Division  by  zero  is  not  permitted
print(7 / 0)#ZDE
print('Bye')#Bye
# Identify  error  (Home  work)
except:
        print('Hyd')
        print('Sec')
        print('Cyb')

'without try suite we cannot use only except suite'
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
'''Five
Six
Seven
Eight'''
# Find  outputs  (Home work)
try:
	print('try suite')
except:
	print('default  except')#defa
	except NameError:
	print('Name  Error')
# Find  outputs  (Home  work)
try:
	print('try suite')
except:
	print('1st  default  except')#1st default except
except:
	print('2nd  default  except')
#  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0)#ZDE
print(7 / 0.0)#ZDE
print(0 / 0)#ZDE
print(0.0 / 0.0)#ZDE
print(7 // 0)#ZDE
print(7 % 0)#ZDE
#  Which  of  the  following  statements  raise  ValueError ?  (Home  work)
import  math
print(int('10.8'))#error
print(float('Ten'))#error
print(complex('True'))#error
print(bool('Ten'))#True
print(bool(''))#False
print(float('10.8'))#10.8
print(float('25'))#25.0
print(int(10.8))#10
print(math . sqrt(-25))#error


'''
When  is  ValueError  raised  ?  --->  When   a  function  (or)  method  does  not  return  any  result
													       i.e. not  even  None
'''
# Which  of  the  following  statements  raise  NameError ?
a = 25
print(a)#25
del  a
print(a)#error
print(eval("   'Ten'   "))#Ten
print(eval('Ten'))#error


'''
When  is  NameError  raised ?  --->  When  a  non-existing  object  is  being  used
'''
# Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0])#H
print('Hyd'[1])#y
print('Hyd'[2])#d
print('Hyd'[3])#error
list = [10 , 20 , 15 , 18]
print(list[0])#10
print(list[3])#18
print(list[4])#error
print(list[-1])#18
print(list[-4])#10
print(list[-5])#error
tpl = (10 , 20 , 30)
print(tpl[3])#error
r = range(10)
print(r[10])#error
s = {10 , 20 , 15 , 18}
print(s[4])#error
d = {10 : 'Hyd' , 20 : 'Sec'}
print(d[0])#error


'''
When  is  IndexError  raised  ?  --->  When  a  non-existing  index  is  being  used
'''
#  Which  of  the  following  statements  raise TypeError ?
print(10 + 20)#30
print('10' + '20')#1020
print(10 + '20')#error
print(len('25'))#error
print(len(25))#error
s = {10 , 20 , 15 , 18}
print(s[0])#error
b = { [10 , 20] : [30 , 40] }#error
print(int(3 + 4j))#error
print(int([10 , 20 , 30]))#error
print(float(None))#error


'''
When  is  TypeError  raised ? ---> When  the  operands  are  illegal  in  an  expression
																			            (or)
													  when  an  illegal  argument  is  passed  to  the  function (or)  method
'''
# Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G'])#Green
print(a['Y'])#error


'''
When  is  KeyError  raised  ?  ---> When  the  dictionary  key  is  invalid
'''
# Find  outputs  (Home  work)
try:
	print(7 / 0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')#ZDE 1
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye')#Bye
# Find  outputs  (Home  work)
try:
	print(7 / 0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')#ZDE 1
	print(8 / 0)
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye')#Bye
# Find  outputs
try:
	print(7 / 0)
	print('Hello')
except  ZeroDivisionError:
	print('ZDE  1')#ZDE 1
	try:
		print(8 / 0)
	except  ZeroDivisionError:
		print('ZDE   2')#ZDE 2
	print('Bye')#Bye
except  ZeroDivisionError:
	print('ZDE  3')
print('End')#End
'''
Find  outputs  (Home  work)

Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError
'''
try:
	print(7 / 0)
except   ArithmeticError:
	print('Arithmetic Error')#Arithmetic Error
except   ZeroDivisionError:
	print('Zero Division  Error')
print('End')#End
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
'''Begin
f1  function
ZDE  is  caught  outside
End'''
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
	print('Begin')#Begin
	f1()
	print('Hello')
except  ZeroDivisionError:
	print("Hi")
except  ValueError:
	print("Bye")
print('End')
'''Begin
f1  function
ZDE  is  caught  by  f1  function
End  of  f1  function
Hello
End'''
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
'''Invalid  index
Invalid  index
No  result
Invalid   argument (or)  operand
Object  does  not  exist
Div by 0 is not allowed
Invalid   argument (or)  operand
Invalid dict key'''
#  Find  outputs
def  f1():
	print('f1  function')#f1 function
	raise   ValueError('Hyd')#Hyd
	print('Sec')#Skipped
# End of  the  function
#f1()
try:
	print('Begin')#Begin
	f1()#f1 function    Caught  ValueError  outside  the  function  :  Hyd
	print('Bye')
except  ValueError  as  msg:
	print('Caught  ValueError  outside  the  function  :  ' , msg)
f1()#f1 function
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
'''Begin
f1  function
Caught  TypeError  outside  the  function :   25
End'''
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
'''Caught  ValueError  :   25
End  of  f1  function
Caught   NameError  :   10.8
End  of  f1  function
Caught  IndexError  :   Hyd
End  of  f1  function
Caught   EOFError  :   True
End  of  f1  function
End of the program'''
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
'''Begin
f1 function
Caught  by  f1 function  :  25
Recaught  by  f1 function  :  25
End  of  f1  function
Hyd
End of the program'''
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
'''Begin
f1 function
Caught  by  f1 function  :  25
Recaught  by  f1 function  :  25
End  of  f1  function
Hyd
End of the program'''
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
'''Begin
f1 function
Caught  by  f1 function  :   25
Some other error
End of the program'''
Threading

#  Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
	for  i  in  range(10):
		print('child  thread')
child = Thread(target = f1)
f1()
for  i  in  range(10):
        print('main  thread')
'''child  thread
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
main  thread'''
#  Find  outputs  (Home  work)
from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')
child = Thread(target =  f1())
child . start()
for  i  in  range(10):
        print('main  thread')
'''main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
'''
# Find  outputs  (Home  work)
from  threading  import  *
def   f1():
        for  i  in  range(10):
                print('child  thread')
child = Thread()
child . start()
for  i   in   range(10):
        print('main  thread')
'''main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread'''
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
'''Child Thread
Child Thread
Child Thread
Main Thread
Main Thread
Child Thread
Main Thread
Child Thread
Child Thread
Main Thread
Main Thread
Main Thread
Child Thread
Child Thread
Main Thread
Child Thread
Child Thread
Main Thread
Main Thread
Main Thread
'''
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
'Recursion Error'
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
'''main  thread
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
#  Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i   in  range(1 , 11):
			print('Child  Thread  :  ' , i)
child = Thread(c1.m1())#How  to  specify  the  target  as  class  method
child . start()
for  i  in  range(1 , 11):
        print('Main  Thread  :  ' , i)
'''Child  Thread  :   1
Child  Thread  :   2
Child  Thread  :   3
Child  Thread  :   4
Main  Thread  :   5
Child  Thread  :   6
Main  Thread  :   7
Child  Thread  :   8
Child  Thread  :   9
Main  Thread  :   10
Main  Thread  :   1
Main  Thread  :   2
Main  Thread  :   3
Main  Thread  :   4
Child  Thread  :   5
Main  Thread  :   6
Child  Thread  :   7
Main  Thread  :   8
Main  Thread  :   9
Child  Thread  :   10'''
# Identify  error  (Home  work)
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
        
'start method is not present in current program'
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
'''Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread'''
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
'''main  thread
main  thread
main  thread
main  thread
main  thread
child  thread
child  thread
main  thread
main  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
main  thread
main  thread
child  thread
child  thread
main  thread
main  thread'''
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
'''main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread'''
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
'''run method
Main method'''
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
'''f1  function : 1
Main  Thread : 1
f1  function : 2
Main  Thread : 2
f1  function : 3
Main  Thread : 3
f1  function : 4
Main  Thread : 4
f1  function : 5
Main  Thread : 5
f1  function : 6
Main  Thread : 6
f1  function : 7
Main  Thread : 7
f1  function : 8
Main  Thread : 8
f1  function : 9
Main  Thread : 9
f1  function : 10
Main  Thread : 10
'''
# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
child = MyThread()
child . start()
print('Main  Thread')

'Main Thread'