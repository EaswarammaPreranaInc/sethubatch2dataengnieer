                             NAME:M.SAICHARAN               PYTHON HOMEWORK
                             DATE:27-10-2025

1.# Identify  Error  (Home  work)
try:
	print('Hyd')
	print('Sec')
	print('Cyb')		#Error due to missing except or finally block



2.# Find  outputs  (Home  work)
print(7 / 0)			# zero division error
try:
	print(7 / 0)
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')
print(7 / 0)			#zero division error
print('Bye')			#Bye



3.# Identify  error  (Home  work)
except:
        print('Hyd')
        print('Sec')
        print('Cyb')		# Error due to we cannot use except without try block


4.# Find  outputs (Home  work)
try:
        print('One')
        print('Two')
        print('Three')
print('Four')			#  Error due to after try block must be except or finally block
except:
		print('Five')
		print('Six')
		print('Seven')
print('Eight')


5.# Find  outputs  (Home work)
try:
	print('try suite')
except:
	print('default  except')#  Error after except block cannot appear another except block
except NameError:
	print('Name  Error')


6.# Find  outputs  (Home  work)
try:
	print('try suite')
except:
	print('1st  default  except')
except:				# Error due to after except block cannot appear another except block
	print('2nd  default  except')


7.#  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0)#Zero Division Error
print(7 / 0.0)#Zero Division Error
print(0 / 0)#Zero Division Error
print(0.0 / 0.0)#Zero Division Error
print(7 // 0)#Zero Division Error
print(7 % 0)#Zero Division Error


8.#  Which  of  the  following  statements  raise  ValueError ?  (Home  work)
import  math
print(int('10.8'))#Value Error
print(float('Ten'))#Value Error
print(complex('True'))#Value Error
print(bool('Ten'))#Value Error
print(bool(''))
print(float('10.8'))
print(float('25'))
print(int(10.8))#Value Error
print(math . sqrt(-25))#Value Error


'''
When  is  ValueError  raised  ?  --->  When   a  function  (or)  method  does  not  return  any  result
													       i.e. not  even  None
'''

9.# Which  of  the  following  statements  raise  NameError ?
a = 25
print(a)
del  a
print(a)#Name Error 
print(eval("   'Ten'   "))
print(eval('Ten'))#Name Error


'''
When  is  NameError  raised ?  --->  When  a  non-existing  object  is  being  used
'''

10.# Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0])
print('Hyd'[1])
print('Hyd'[2])
print('Hyd'[3])#Index error
list = [10 , 20 , 15 , 18]
print(list[0])
print(list[3])
print(list[4])#Index Error
print(list[-1])
print(list[-4])
print(list[-5])#Index Error
tpl = (10 , 20 , 30)
print(tpl[3])
r = range(10)
print(r[10])#Index Error
s = {10 , 20 , 15 , 18}
print(s[4])#Index Error
d = {10 : 'Hyd' , 20 : 'Sec'}
print(d[0])#Key Error


'''
When  is  IndexError  raised  ?  --->  When  a  non-existing  index  is  being  used
'''


11.#  Which  of  the  following  statements  raise TypeError ?
print(10 + 20)
print('10' + '20')
print(10 + '20')#Type Error
print(len('25'))
print(len(25))#Type Error
s = {10 , 20 , 15 , 18}
print(s[0])#Type Error
b = { [10 , 20] : [30 , 40] }
print(int(3 + 4j))#Type Error
print(int([10 , 20 , 30]))#Type Error
print(float(None))#Type Error


'''
When  is  TypeError  raised ? ---> When  the  operands  are  illegal  in  an  expression
			 (or)
 when  an  illegal  argument  is  passed  to  the  function (or)  method
'''

12.# Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G'])
print(a['Y'])#Key Error


'''
When  is  KeyError  raised  ?  ---> When  the  dictionary  key  is  invalid
'''

13.# Find  outputs  (Home  work)
try:
	print(7 / 0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')#ZDE  1
except    ZeroDivisionError:#Not executed
	print('ZDE  2')
print('Bye')#Bye


14.# Find  outputs  (Home  work)
try:
	print(7 / 0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')#ZDE1
	print(8 / 0)
except    ZeroDivisionError:
	print('ZDE  2')#ZDE2
print('Bye')#Bye


15.# Find  outputs
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
16.Find  outputs  (Home  work)

Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError
'''
try:
	print(7 / 0)
except   ArithmeticError:
	print('Arithmetic Error')
except   ZeroDivisionError:
	print('Zero Division  Error')#  Not  executed due to arithmeticerror  is  parent  class  to  zerodivisionerror
print('End')#End


17.# Find  outputs  (Home  work)
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
#Output:
Begin
f1  function
ZDE  is  caught  outside
End

18.# Find  outputs  (Home  work)
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
#OutPut:
Begin
f1  function
ZDE  is  caught  by  f1  function
End  of  f1  function
Hello
End

19.'''
What  are   the  outputs  if  input  is  1 ?  --->Invalid Index

What  are   the  outputs  if  input  is  2 ?  --->Invalid Index

What  are   the  outputs  if  input  is  3 ?  --->no result

What  are   the  outputs  if  input  is  4 ?  --->Invalid argument or operand

What  are   the  outputs  if  input  is  5 ?  --->object doesnot exist

What  are   the  outputs  if  input  is  6 ?  --->div by 0 is not allowed

What  are   the  outputs  if  input  is  7 ?  --->Invalid argument or operand

What  are   the  outputs  if  input  is  8 ?  --->Invalid dict key
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


20.#  Find  outputs
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
#Output:
f1  function
Sec
Begin
f1  function
Sec
Bye
f1  function
Sec
End of the program


21.#Find  outputs  (Home  work)
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
#Output:
Begin
f1  function
Caught  TypeError  outside  the  function :   25
End



22.# Find  outputs  (Home  work)
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

#Output:
Caught  ValueError  :   25
End  of  f1  function
Caught   NameError  :   10.8
End  of  f1  function
Caught  IndexError  :   Hyd
End  of  f1  function
Caught   EOFError  :   True
End  of  f1  function
End of the program



23.#  Find  outputs  (Home  work)
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

#Output:
Begin
f1 function
Caught  by  f1 function  :  25
Recaught  by  f1 function  :  25
End  of  f1  function
Hyd
End of the program



24.#  Find  outputs  (Home  work)
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

#Output:
Begin
f1 function
Caught  by  f1 function  :  25
Recaught ValueError  :   25
End of the program

25.# Find  outputs  (Home   work)
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

#Output:
Begin
f1 function
Caught  by  f1 function  :   25
Some other error
End of the program

26.#  Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
	for  i  in  range(10):
		print('child  thread')
child = Thread(target = f1)
f1()
for  i  in  range(10):
        print('main  thread')
#Output
10 times child thread
10 times main thread


27.#  Find  outputs  (Home  work)
from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')
child = Thread(target =  f1())#Function call
child . start()
for  i  in  range(10):
        print('main  thread')
#Output:
10 times child thread
10 times main thread


28.# Find  outputs  (Home  work)
from  threading  import  *
def   f1():
        for  i  in  range(10):
                print('child  thread')
child = Thread()
child . start()
for  i   in   range(10):
        print('main  thread')
#Output:
10 times main thread

29.# Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
        for  i  in  range(10):
                print('Child  Thread')
child = Thread(target = f1)
child . start()
for  i  in  range(10):
        print('Main  Thread')
child . start()#Error due to thread starts once 
#Output:
10 times child thread
10 times main thread


30.# Find  outputs  (Home  work)
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
#Output:
10 times child thread
10 times main thread


31.# Find  outputs (Home  work)
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
#Output:
10 times child thread
10 times main thread


32.#  Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i   in  range(1 , 11):
			print('Child  Thread  :  ' , i)#10 times child thread 1-10
child = Thread(How  to  specify  the  target  as  class  method)
child . start()
for  i  in  range(1 , 11):
        print('Main  Thread  :  ' , i)#10 times main thread 1-10


33.# Identify  error  (Home  work)
from  threading  import  Thread
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')#10 times child thread
# End of the class
t = Thread()
t . start()#Error due to start method is not defined
for  i  in  range(10):
        print('main  thread')#10 times main thread



34.# Find  outputs  (Home  work)
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')#10 times child thread
from  threading  import  Thread
t = Thread()
t . start()
for  i  in  range(10):
        print('Main  Thread')#10 times main thread



35.# Find  outputs  (Home  work)
from threading import *
class    MyThread(Thread):
        def   run(self):
                for  i  in  range(10):
                        print('child  thread')#10 times child thread
#end of the class
child = MyThread()
child . run()
for  i  in  range(10):
        print('main  thread')#10 times main thread


36.# Find  outputs (Home  work)
from  threading  import *
class    MyThread(Thread):
	def  walk(self):
		for  i  in  range(10):
			print('walk  method')
child = MyThread()
child . start()
for  i  in  range(10):
	print('Main  Thread')#10 times main thread



37.# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	def   run(self):
			print('run  method')
def  f1():
	print('f1  function')#run method
child = MyThread(target = f1)
child . start()
print('Main  Thread')#main thread


38.# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
def  f1():
	for  i  in   range(1 , 11):
		print('f1  function : ' , i)#10 f1 function
child = MyThread(target = f1)
child . start()
for  i  in  range(1 , 11):
	print('Main  Thread : ' , i)#10 main thread



39.# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
child = MyThread()
child . start()
print('Main  Thread')#Main thread 




