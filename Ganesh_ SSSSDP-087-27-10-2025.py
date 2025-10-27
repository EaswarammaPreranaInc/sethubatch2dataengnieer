 # Find  outputs  (Home  work)
try:
	print('try suite')
except:						# error because default except suit write only once 
	print('1st  default  except')
except:
	print('2nd  default  except')       
'''
	# output
 error because default except suit write only once if only one except suit try suit executes
 try suite
''' 



 #  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0)						# ZeroDivisionError					
print(7 / 0.0)						# ZeroDivisionError
print(0 / 0)						# ZeroDivisionError					
print(7 / 0.0)						# ZeroDivisionError
print(0 / 0)						# ZeroDivisionError
print(0.0 / 0.0)					# ZeroDivisionError
print(7 // 0)						# ZeroDivisionError
print(7 % 0)						# ZeroDivisionError
'''
	
 	



 #  Which  of  the  following  statements  raise  ValueError ?  (Home  work)
import  math
print(int('10.8'))					# ValueError because we cannot convert string to int
print(float('Ten'))					# ValueError because we cannot convert string letter to float
print(complex('True'))					# ValueError because we cannot convert string to complex
print(bool('Ten'))					# true
print(bool(''))						# false
print(float('10.8'))					# 10.8
print(float('25'))					# 25
print(int(10.8))					# 10
print(math . sqrt(-25))					# ValueError because we cannot convert square root
'''
When  is  ValueError  raised  ?  --->  When   a  function  (or)  method  does  not  return  any  result
													       i.e. not  even  None
'''



 # Which  of  the  following  statements  raise  NameError ?
a = 25
print(a)						# 25
del  a							# obj a deleted
print(a)						# error a is not defined
print(eval("   'Ten'   "))				# 	'Ten'
print(eval('Ten'))					# Ten


'''
When  is  NameError  raised ?  --->  When  a  non-existing  object  is  being  used
'''




 # Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0])						# H
print('Hyd'[1])						# y
print('Hyd'[2])						# d
print('Hyd'[3])						# Indexerror because there is not index value of 3
list = [10 , 20 , 15 , 18]
print(list[0])						# 10
print(list[3])						# 18
print(list[4])						# Indexerror because there is not index value of 4
print(list[-1])						# list[-1]
print(list[-4])						# list[-4]
print(list[-5])						# list[-5]
tpl = (10 , 20 , 30)
print(tpl[3])						# Indexerror because index out of range
r = range(10)
print(r[10])						# Indexerror because index out of range
s = {10 , 20 , 15 , 18}
print(s[4])						# Indexerror because index out of range
d = {10 : 'Hyd' , 20 : 'Sec'}
print(d[0])						# error because there no key of 0

'''
When  is  IndexError  raised  ?  --->  When  a  non-existing  index  is  being  used
'''




 #  Which  of  the  following  statements  raise TypeError ?
print(10 + 20)						# 30
print('10' + '20')					# 1020
print(10 + '20')					# Typeerror because there is we cannot add string and integer
print(len('25'))					# 2
print(len(25))						# TypeError because int doesnot have len() method
s = {10 , 20 , 15 , 18}
print(s[0])						# TypeError because set doesnot have index method
b = { [10 , 20] : [30 , 40] }				# TypeError because you cannot write the list dictionary
print(int(3 + 4j))					# TypeError because complex value cannot convert int
print(int([10 , 20 , 30]))				# TypeError because list of value cannot convert int
print(float(None))					# TypeError because float value cannot convert nonetype

'''
When  is  TypeError  raised ? ---> When  the  operands  are  illegal  in  an  expression
																			            (or)
when  an  illegal  argument  is  passed  to  the  function (or)  method
'''



 # Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G'])						# Green
print(a['Y'])						# keyerror there is no key value of 'y'

'''
When  is  KeyError  raised  ?  ---> When  the  dictionary  key  is  invalid
'''




 # Find  outputs  (Home  work)
try:
	print(7 / 0)						
	print('Hello')						
except    ZeroDivisionError:
	print('ZDE  1')						# ZDE 1
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye')							# Bye





 # Find  outputs  (Home  work)
try:
	print(7 / 0)						
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')						# ZDE 1
	print(8 / 0)						# error
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye')							# Bye





 # Find  outputs
try:
	print(7 / 0)
	print('Hello')
except  ZeroDivisionError:
	print('ZDE  1')						# ZDE 1
	try:
		print(8 / 0)
	except  ZeroDivisionError:
		print('ZDE   2')				# ZDE 2
	print('Bye')						# Bye
except  ZeroDivisionError:
	print('ZDE  3')
print('End')							# End





 '''
Find  outputs  (Home  work)

Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError
'''
try:
	print(7 / 0)
except   ArithmeticError:
	print('Arithmetic Error')				# Arithmetic Error
except   ZeroDivisionError:
	print('Zero Division  Error')
print('End')							# End





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
	# output
	Begin
	f1 function
	ZDE is caught outside
	End
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
	#output
	Begin
	f1 function
	ZDE is caught by f1 function
	End of f1 function
	Hello
	End
'''



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
'''
	Caught IndexError : 25
	End of f1 function
	Caught ValueError : 10.8
	End of f1 function 
	Caught NameError :  Hyd
	End of f1 function
	Caught EOF  :       True
	End of f1 function
	End of the program
''' 


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
'''
	output
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
'''
	output
 Begin
 f1 function
 Caught  by  f1 function  :  25
 Recaught ValueError  :   25
 End of the program
'''



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
'''
	output
 Begin
 f1 function
 Caught  by  f1 function  :   25
 Some other error
 End of the program
'''



 #  Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
	for  i  in  range(10):
		print('child  thread')
child = Thread(target = f1)
f1()
for  i  in  range(10):
        print('main  thread')
'''
	output
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
'''



 #  Find  outputs  (Home  work)
from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')
child = Thread(target =  f1())
child . start()
for  i  in  range(10):
        print('main  thread')
'''
	#output
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
'''
	output
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
'''
	output
Child  Thread
Child  Thread
Child  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Child  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Main  Thread
Child  Thread
Child  Thread
Child  Thread
Child  Thread
Child  Thread
Child  Thread
error because we can start only once
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
'''
	# output
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
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
'''



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
'''
	output
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
'''




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
'''
	# output
 Child  Thread  :   1
 Child  Thread  :   2
 Main  Thread  :   1
 Main  Thread  :   2
 Main  Thread  :   3
 Main  Thread  :   4
 Main  Thread  :   5
 Main  Thread  :   6
 Main  Thread  :   7
 Main  Thread  :   8 
 Main  Thread  :   9
 Main  Thread  :   10
 Child  Thread  :   3
 Child  Thread  :   4
 Child  Thread  :   5
 Child  Thread  :   6
 Child  Thread  :   7
 Child  Thread  :   8
 Child  Thread  :   9
 Child  Thread  :   10
'''



 # Identify  error  (Home  work)
from  threading  import  Thread
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
# End of the class
t = Thread()
t . start()					# error
for  i  in  range(10):
        print('main  thread')
'''
	output
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
'''
 	output
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
'''



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
'''
	output
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
'''




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
''' 
	output
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
'''




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
'''
	output
run  method
Main  Thread
'''



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
'''
	output
f1  function :  1
Main  Thread :  1
f1  function :  2
f1  function :  3
f1  function :  4
f1  function :  5
f1  function :  6
f1  function :  7
f1  function :  8
f1  function :  9
f1  function :  10
Main  Thread :  2
Main  Thread :  3
Main  Thread :  4
Main  Thread :  5
Main  Thread :  6
Main  Thread :  7
Main  Thread :  8
Main  Thread :  9
Main  Thread :  10
'''




# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
child = MyThread()
child . start()
print('Main  Thread') 
	# output
	# Main Thread