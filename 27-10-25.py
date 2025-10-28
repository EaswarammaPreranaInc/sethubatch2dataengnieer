#Find  outputs 
from  threading  import  Thread
def  f1():
	for i in range(10):
		print('child  thread')
child = Thread(target = f1)
f1() # only one therad in the program so output can be predicted
for i in range(10):
        print('main  thread')
'''
o/p:
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


#Find  outputs  
from threading import Thread
def  f1():
        for i in range(10) :
                print('child  thread')
child =Thread(target =  f1()) # executes f1 function and it returns None so. target=None . No child thread is created
child.start() 
for  i  in  range(10):
        print('main  thread')


#Find  outputs  
from  threading  import  *
def   f1():
        for i in range(10):
                print('child  thread')
child =Thread()
child.start() # no target is specified .so, empty run method of thread class is executed 
for i in range(10):
        print('main  thread')
'''
o/p:
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

#Find  outputs 
from  threading  import  Thread
def    f1():
        for  i  in  range(10):
                print('Child  Thread')
child = Thread(target = f1)
child.start()
for  i  in  range(10):
        print('Main  Thread')
#child.start() error : threads can only be started once



#Find  outputs  
from  threading  import  *
class  c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child  = Thread(target = a.m1)
child.start() # child thread is created and executed prallely with the main thread and output cannot be predicted 
a.m1()
for  i  in  range(10):
	print('main  thread')



#Find  outputs 
from  threading  import   *
class   c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child = Thread(target = a.m1()) # executes m1 method and returns None .so. target=None and output can be predicted
child.start()
for  i  in  range(10):
        print('main  thread')
'''
o/p:
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



#Find  outputs  
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i in range(1,11):
			print('Child  Thread  :' , i)
child = Thread(target=c1.m1) # How  to  specify  the  target  as  class  method)
child.start() # output cannot be predicted as there are 2 threads in the program that run parallely
for  i  in  range(1,11):
        print('Main  Thread  :  ' , i)



#Identify  error  
from  threading  import  Thread
class   Thread:
        def   run(self):
                for i in range(10):
                        print('Child  Thread')
# End of the class
t = Thread()
#t.start() # error : Thread doesn't have start() method 
for  i  in  range(10):
        print('main  thread')
'''
o/p:
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



#Find outputs  
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
from  threading  import  Thread
t =Thread()
t.start() # child thread starts and ends immediately
for  i  in  range(10):
        print('Main  Thread')
'''
o/p:
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



# Find  outputs  
from threading import *
class    MyThread(Thread):
        def   run(self):
                for  i  in  range(10):
                        print('child  thread')
#end of the class
child = MyThread()
child.run() # no thread is created only one main thread is created 
for  i  in  range(10):
        print('main  thread')




# Find  outputs 
from  threading  import *
class    MyThread(Thread):
	def  walk(self):
		for  i  in  range(10):
			print('walk  method')
child = MyThread()
child.start() # start() calls thread's run() method .run() does nothing
for  i  in  range(10):
	print('Main  Thread')
'''
o/p:
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
child.start()
print('Main  Thread')
'''
o/p:
run method
Main Thread
'''



# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
def  f1():
	for i in range(1 , 11):
		print('f1  function : ' , i)
child = MyThread(target = f1)
child.start() # child thread is created and output cannot be predicted
for i in range(1 , 11):
	print('Main  Thread : ' , i)
 
        

# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
child = MyThread()
child.start()
print('Main  Thread') # Main Thread#Find  outputs
def  f1():
	print('f1  function')
	raise   ValueError('Hyd')
	print('Sec')
# End of  the  function
#f1() # raises ValueError and it is not handled in try and except
try:
	print('Begin')
	f1()
	print('Bye')
except  ValueError  as  msg:
	print('Caught  ValueError  outside  the  function  :  ' , msg)
f1()
print('End of the program')


#Find  outputs  
def  f1(a):
	print('f1  function')
	if   a ==20:
		raise  ArithmeticError()
	elif   a ==0:
		raise  IndexError()
	elif  a ==10:
		raise TypeError(25)
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
'''
o/p:
Begin
f1  function
Caught  TypeError  outside  the  function :   25
End
'''


# Find  outputs
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
		print('Caught  IndexError  : ' , msg)
	except ValueError  as  msg:
		print('Caught  ValueError  : ' , msg)
	except  NameError  as  msg:
		print('Caught   NameError  : ' , msg)
	except  EOFError  as  msg:
		print('Caught   EOFError  : '  , msg)
	print('End  of  f1  function')
#outside the function
f1(10)
f1(20)
f1(30)
f1(0)
print('End of the program')
'''
o/p:
Caught  ValueError  :  25
End  of  f1  function
Caught   NameError  :  10.8
End  of  f1  function
Caught  IndexError  :  Hyd
End  of  f1  function
Caught   EOFError  :  True
End  of  f1  function
End of the program
'''


#Find  outputs 
def f1():
	try:
		print('f1 function')
		raise  ValueError(25)
		print('Hi')
	except  ValueError  as  msg:
		try:
			print('Caught  by  f1 function  :' , msg)
			raise   ValueError(msg)
		except  ValueError  as   msg:
			print('Recaught  by  f1 function  :' , msg)
	except:
		print('Hello')
	print('End  of  f1  function')
# End  of  f1()  function
try:
	print('Begin')
	f1()
	print('Hyd')
except  ValueError  as  x:
	print('Recaught ValueError  :' , x)
except:
	print('Some other error')
print('End of the program')
'''
o/p:
Begin
f1 function
Caught  by  f1 function  : 25
Recaught  by  f1 function  : 25
End  of  f1  function
Hyd
End of the program
'''



#  Find  outputs  
def f1():
	try:
		print('f1 function')
		raise  ValueError(25)
		print('Hi')
	except  ValueError  as  msg:
		print('Caught  by  f1 function  :' , msg)
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
	print('Recaught ValueError  :' , x)
except:
	print('Some other error')
print('End of the program')
'''
o/p:
Begin
f1 function
Caught  by  f1 function  : 25
Recaught ValueError  : 25
End of the program
'''


# Find  outputs  
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
Caught  by  f1 function  : 25
Some other error
End of the program
'''#Identify  Error  
'''
try: # error : try should be paired with except or finally or both
	print('Hyd')
	print('Sec')
	print('Cyb')
'''



# Find  outputs  
#print(7/0) # ZeroDivision error
try:
	print(7/0) # error so except suite is executed
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')
#print(7/0) # zeroDivisionError
print('Bye')



#Identify error  
'''
except: # error becaues cannot write except without try
        print('Hyd')
        print('Sec')
        print('Cyb')
'''


# Find  outputs 
try:
        print('One')
        print('Two')
        print('Three')
#print('Four') # error : try and except blocks must be directly paired
except:
		print('Five')
		print('Six')
		print('Seven')
print('Eight')
'''
o/p:
One
Two
Three
Eight
'''


# Find  outputs 
try:
	print('try suite')
#except: #error : cannot be witten in the middle  
	print('default  except')
except NameError:
	print('Name  Error')



# Find  outputs  
try:
	print('try suite')
except:
	print('1st  default  except')
#except: # error : cannot write two except suits
	print('2nd  default  except')
	


#  Which  of  the  following  statements  raise  ZeroDivisionError ?
#print(7/0) # ZeroDivisionError
#print(7/0.0) # ZeroDivisionError
#print(0/0) # ZeroDivisionError
#print(0.0/0.0) # ZeroDivisionError
#print(7//0) # ZeroDivisionError
#print(7%0) # ZeroDivisionError


#  Which  of  the  following  statements  raise  ValueError ?  
import  math
#print(int('10.8')) # ValueError : cannot convert string'10.8' to int
#print(float('Ten')) # ValueError
#print(complex('True')) # ValueError
print(bool('Ten')) # True
print(bool('')) # False
print(float('10.8')) # 10.8
print(float('25')) # 25.0
print(int(10.8)) # 10
#print(math . sqrt(-25)) # ValueError



# Which  of  the  following  statements  raise  NameError ?
a = 25
print(a) # 25
del  a # deletes object a
#print(a) # NameError : non-existing object is being used
#print(eval("   'Ten'   ")) # NameError : there is no object Ten 
#print(eval('Ten')) # NameError


# Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0]) # H
print('Hyd'[1]) # y
print('Hyd'[2]) # d
#print('Hyd'[3]) # IndexError : non-existing index
list = [10 , 20 , 15 , 18]
print(list[0]) # 10
print(list[3]) # 18
#print(list[4]) # IndexError : index 4 doesn't exist
print(list[-1]) # 18
print(list[-4]) # 10
#print(list[-5]) # IndexError
tpl = (10 , 20 , 30)
#print(tpl[3]) # IndexError
r = range(10)
#print(r[10]) # IndexError
s = {10 , 20 , 15 , 18}
#print(s[4]) # IndexError : set is not indexed
d = {10 : 'Hyd' , 20 : 'Sec'}
#print(d[0]) # KeyError : there is no key 0 in the dict



#  Which  of  the  following  statements  raise TypeError ?
print(10 + 20) # 30
print('10' + '20') # 1020
#print(10 + '20') # TypeError 
print(len('25')) # 2
#print(len(25)) # TypeError : int doesn't have length
s = {10 , 20 , 15 , 18}
#print(s[0]) # TypeError : set is not indexed
#b = { [10 , 20] : [30 , 40] } # TypeError
#print(int(3 + 4j)) # TypeError
#print(int([10 , 20 , 30])) # TypeError
#print(float(None)) # TypeError



# Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G']) # Green
#print(a['Y']) # KeyError : invalid key



# Find  outputs 
try:
	print(7/0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE 1')
except    ZeroDivisionError:
	print('ZDE 2')
print('Bye')
'''
o/p:
ZDE 1
Bye
'''


# Find  outputs  
try:
	print(7 / 0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')
	#print(8 / 0) # ZeroDivisionError
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye')


print()
# Find  outputs
try:
	print(7 / 0)
	print('Hello')
except  ZeroDivisionError:
	print('ZDE 1')
	try:
		print(8 / 0)
	except  ZeroDivisionError:
		print('ZDE 2')
	print('Bye')
except  ZeroDivisionError:
	print('ZDE  3')
print('End')
'''
o/p:
ZDE 1
ZDE 2
Bye
End
'''


'''
Find  outputs  

Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError
'''
try:
	print(7 / 0)
except   ArithmeticError:
	print('Arithmetic Error')
except   ZeroDivisionError:
	print('Zero Division  Error')
print('End') 
'''
o/p:
Arithmetic Error
End
'''


# Find  outputs  
def  f1():
	try:
		print('f1 function')
		print(7/0)
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
	print('ZDE is caught outside')
except:
	print('Bye')
print('End')
'''
o/p:
Begin
f1 function
ZDE is caught outside
End
'''


#Find outputs 
def  f1():
	try:
		print('f1  function')
		print(7/0)
	except  ValueError:
		print('Hello')
	except  ZeroDivisionError:
		print('ZDE is caught by f1 function')
	print('End of f1 function')
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
Begin
f1  function
ZDE is caught by f1 function
End of f1 function
Hello
End
'''


'''
What  are   the  outputs  if  input  is  1 ?  ---> Invalid index

What  are   the  outputs  if  input  is  2 ?  ---> Invalid index

What  are   the  outputs  if  input  is  3 ?  ---> No result

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
				print(7/0)
			case  7:
				print(10+'20')
			case   8:
				d = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb'}
				print(d[18])
			case   9:
				break
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