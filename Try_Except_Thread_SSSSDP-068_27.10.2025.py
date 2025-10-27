# Identify  Error  (Home  work)
try:
	print('Hyd')
	print('Sec')
	print('Cyb')
#  Error due to missing except or finally block


# Find  outputs  (Home  work)
print(7 / 0)  #  ZeroDivisionError
try:
	print(7 / 0)
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')  #  division  by  zero  is  not  permitted
print(7 / 0)  #  ZeroDivisionError
print('Bye')  #  Bye



# Identify  error  (Home  work)
except:
        print('Hyd')
        print('Sec')
        print('Cyb')

#  Error due to we cant use except without try block



# Find  outputs (Home  work)
try:
        print('One')
        print('Two')
        print('Three')
print('Four')  #  Error due to after try block must be except or finally block
except:
		print('Five')
		print('Six')
		print('Seven')
print('Eight')



# Find  outputs  (Home work)
try:
	print('try suite')
except:
	print('default  except')
except NameError:  #  Error after except block cannot appear another except block
	print('Name  Error')


# Find  outputs  (Home  work)
try:
	print('try suite')
except:
	print('1st  default  except')
except:  #   Error due to after except block cannot appear another except block
	print('2nd  default  except')



#  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0)  #  ZeroDivisionError
print(7 / 0.0)  #  ZeroDivisionError
print(0 / 0)  # ZeroDivisionError
print(0.0 / 0.0)  #  ZeroDivisionError
print(7 // 0)  #  zeroDivisionError
print(7 % 0)  #  zeroDivisionError


#  Which  of  the  following  statements  raise  ValueError ?  (Home  work)
import  math
print(int('10.8'))  #  ValueError
print(float('Ten'))  #  ValueError
print(complex('True'))  #  ValueError
print(bool('Ten'))  #  ValueError
print(bool(''))  
print(float('10.8'))  
print(float('25'))  
print(int(10.8))  #  ValueError
print(math . sqrt(-25))  #  ValueError


# Which  of  the  following  statements  raise  NameError ?
a = 25
print(a)
del  a
print(a)  #  NameError
print(eval("   'Ten'   "))
print(eval('Ten'))  #  NameError


'''
When  is  NameError  raised ?  --->  When  a  non-existing  object  is  being  used
'''


# Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0])
print('Hyd'[1])
print('Hyd'[2])
print('Hyd'[3])  #  IndexError
list = [10 , 20 , 15 , 18]
print(list[0])
print(list[3])
print(list[4])  # IndexError
print(list[-1])
print(list[-4])
print(list[-5])  #  IndexError
tpl = (10 , 20 , 30)
print(tpl[3])  #  IndexError
r = range(10)  
print(r[10])  #  IndexError 
s = {10 , 20 , 15 , 18}
print(s[4])  #  IndexError
d = {10 : 'Hyd' , 20 : 'Sec'}
print(d[0])  #  KeyError


'''
When  is  IndexError  raised  ?  --->  When  a  non-existing  index  is  being  used
'''


#  Which  of  the  following  statements  raise TypeError ?
print(10 + 20)
print('10' + '20')
print(10 + '20')  #  TypeError
print(len('25'))
print(len(25))  #  TypeError
s = {10 , 20 , 15 , 18}
print(s[0])  #  TypeError
b = { [10 , 20] : [30 , 40] }
print(int(3 + 4j))   #  TypeError
print(int([10 , 20 , 30]))  #  TypeError
print(float(None))  #  TypeError


'''
When  is  TypeError  raised ? ---> When  the  operands  are  illegal  in  an  expression													            (or)
when  an  illegal  argument  is  passed  to  the  function (or)  method
'''



# Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G'])       
print(a['Y'])  #  KeyError


'''
When  is  KeyError  raised  ?  ---> When  the  dictionary  key  is  invalid
'''


# Find  outputs  (Home  work)
try:
	print(7 / 0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')  #  ZDE  1
except    ZeroDivisionError:  #  Not executed
	print('ZDE  2')
print('Bye')  #  Bye


# Find  outputs  (Home  work)
try:
	print(7 / 0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')  #  ZDE  1
	print(8 / 0)
except    ZeroDivisionError:
	print('ZDE  2')  #  ZDE  2
print('Bye')  #  Bye



# Find  outputs
try:
	print(7 / 0)
	print('Hello')
except  ZeroDivisionError:
	print('ZDE  1')  # ZDE  1
	try:
		print(8 / 0)
	except  ZeroDivisionError:
		print('ZDE   2')  # ZDE   2
	print('Bye')  # Bye
except  ZeroDivisionError:
	print('ZDE  3')
print('End')  # End



'''
Find  outputs  (Home  work)

Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError
'''
try:
	print(7 / 0)
except   ArithmeticError:
	print('Arithmetic Error')
except   ZeroDivisionError:  #  Not  executed due to arithmeticerror  is  parent  class  to  zerodivisionerror
	print('Zero Division  Error')
print('End')  # End




# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')  #  f1 function
		print(7 / 0)  #  ZeroDivisionError
	except  ValueError:
		print('Hello')
	try:
		print(int('Ten'))  #  ValueError
	except ZeroDivisionError:
		print('Bye')
	print('End  of  f1  function')  # End of f1  function
# End of f1  function
try:
	print('Begin')  # Begin
	f1()
	print('Hi')  
except  ZeroDivisionError:
	print('ZDE  is  caught  outside')  # ZDE  is  caught  outside
except:
	print('Bye')
print('End')  # End




# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')  #  f1 function
		print(7 / 0)
	except  ValueError:
		print('Hello')
	except  ZeroDivisionError:
		print('ZDE  is  caught  by  f1  function')  # ZDE  is  caught  by  f1  function
	print('End  of  f1  function')  # End of f1  function
# End  of  the  function
try:
	print('Begin')  #  Begin
	f1()
	print('Hello')  #  Hello
except  ZeroDivisionError:
	print("Hi")
except  ValueError:
	print("Bye")
print('End')  #  End



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
				print(list[5])  # IndexError
			case  2:
				s = 'Hyd'
				print(s[3])  #  IndexError
			case  3:
				print(int('Two'))  #  ValueError
			case  4:
				a = 25
				print(len(a))  #  TypeError
			case  5:
				print(eval('Hyd'))  # NameError
			case  6:
				print(7 / 0)  #  ZeroDivisionError
			case  7:
				print(10 + '20')  #  TypeError
			case   8:
				d = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb'}
				print(d[18])  #  KeyError
			case   9:
				exit()
	except   ZeroDivisionError:
		print('Div by 0 is not allowed')  #  Div by 0 is not allowed
	except  ValueError:
		print('No  result')		  #  No  result
	except  IndexError:
		print('Invalid  index')  #  Invalid  index
	except  TypeError:
		print('Invalid   argument (or)  operand')  #  Invalid   argument (or)  operand
	except  KeyError:
		print('Invalid dict key')  #  Invalid dict key
	except  NameError:
		print('Object  does  not  exist')   #  Object  does  not  exist
	except:
		print('A new error')	
# End of while loop
print('Bye')  



#  Find  outputs
def  f1():
	print('f1  function')  #  f1  function
	raise   ValueError('Hyd')  #  Raising  ValueError  with  message  'Hyd'
	print('Sec')
# End of  the  function
f1()  #  raising  ValueError  with  message  'Hyd'
try:
	print('Begin')  #  Begin
	f1()
	print('Bye')
except  ValueError  as  msg:
	print('Caught  ValueError  outside  the  function  :  ' , msg)  # Caught  ValueError  outside  the  function  :   Hyd
f1()  #  raising  ValueError  with  message  'Hyd'
print('End of the program')  #  End of the program



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
	print('Begin')  # Begin
	f1(10)  #  raising  TypeError  with  message  25
	f1(20)  #  raising  ArithmeticError
	f1(30)  #  raising  ValueError
	f1(0)  #  raising  IndexError
except  ArithmeticError:
	print('Hyd')  #  Hyd
except  IndexError:
	print('Sec')  #  Sec
except  TypeError  as   msg:
	print('Caught  TypeError  outside  the  function :  '  , msg)  # Caught  TypeError  outside  the  function :   25
except  ValueError:
	print('Hello')  #  Hello
except:
	print('some error')  
print('End')  #  End



# Find  outputs  (Home  work)
def  f1(a):
	try:
		if   a == 10:
			raise  ValueError(25)  #  raising  ValueError  with  message  25
		elif   a == 20:
			raise  NameError(10.8)  #  raising  NameError  with  message  10.8
		elif   a == 30:
			raise  IndexError('Hyd')  #  raising  IndexError  with  message  'Hyd'
		raise  EOFError(True)  #  raising  EOFError  with  message  True
	except  IndexError  as  msg:
		print('Caught  IndexError  :  ' , msg)  #  Caught  IndexError  :   Hyd
	except ValueError  as  msg:
		print('Caught  ValueError  :  ' , msg)   #  Caught  ValueError  :   25
	except  NameError  as  msg:
		print('Caught   NameError  :  ' , msg)  #  Caught   NameError  :   10.8
	except  EOFError  as  msg:
		print('Caught   EOFError  :  '  , msg)  #  Caught   EOFError  :   True
	print('End  of  f1  function')  #  End  of  f1  function
#outside the function
f1(10)  
f1(20)
f1(30)
f1(0)
print('End of the program')  #  End of the program




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
	print('Begin')  # Begin
	f1()  
	print('Hyd')
except  ValueError  as  x:
	print('Recaught ValueError  :  ' , x)
except:
	print('Some other error')
print('End of the program')

'''
Begin
f1 function
Caught  by  f1 function  :  25
Recaught  by  f1 function  :  25
End  of  f1  function
Hyd
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
		print('child  thread')  #  10 times child thread
child = Thread(target = f1)
f1()
for  i  in  range(10):
        print('main  thread')  #  10 times main thread



#  Find  outputs  (Home  work)
from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')  #  10 times child thread
child = Thread(target =  f1())  #  here f1()  is  function call
child . start()
for  i  in  range(10):
        print('main  thread')  #  10 times main thread



# Find  outputs  (Home  work)
from  threading  import  *
def   f1():
        for  i  in  range(10):
                print('child  thread')
child = Thread()
child . start()
for  i   in   range(10):
        print('main  thread')  # 10 times main thread



# Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
        for  i  in  range(10):
                print('Child  Thread')  # 10 times Child Thread  
child = Thread(target = f1)
child . start()
for  i  in  range(10):
        print('Main  Thread')  # 10 times Main Thread
child . start()  #  Error due to thread  can  be  started  only  once


# Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')  # 10 times child thread
a = c1()
child  = Thread(target = a . m1)
child . start()  
a . m1()
for  i  in  range(10):
	print('main  thread')  # 10 times main thread


# Find  outputs (Home  work)
from  threading  import   *
class   c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')  # 10 times child thread
a = c1()
child = Thread(target =  a . m1())
child . start()
for  i  in  range(10):
        print('main  thread')  # 10 times main thread



#  Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i   in  range(1 , 11):
			print('Child  Thread  :  ' , i)    #  10 times Child  Thread 1-10
child = Thread(c1.m1())
child . start()
for  i  in  range(1 , 11):
        print('Main  Thread  :  ' , i)  #  10 times Main  Thread 1-10



# Identify  error  (Home  work)
from  threading  import  Thread
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')  # 10 times Child  Thread
# End of the class
t = Thread()  
t . start()  #  Error due to  start()  method  is  not  defined  in  the  Thread  class
for  i  in  range(10):
        print('main  thread')  # 10 times main  thread




# Find  outputs  (Home  work)
from threading import *
class    MyThread(Thread):
        def   run(self):
                for  i  in  range(10):
                        print('child  thread')  # 10 times child thread
#end of the class
child = MyThread()
child . run()
for  i  in  range(10):
        print('main  thread')  # 10 times main thread



# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
def  f1():
	for  i  in   range(1 , 11):
		print('f1  function : ' , i)  #  f1 function 1-10
child = MyThread(target = f1)
child . start()
for  i  in  range(1 , 11):
	print('Main  Thread : ' , i)  #  Main Thread 1-10



# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
child = MyThread()
child . start()
print('Main  Thread') #  Main  Thread

