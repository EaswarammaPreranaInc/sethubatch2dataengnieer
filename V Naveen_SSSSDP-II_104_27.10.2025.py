#1. Identify  Error  (Home  work)
try:
	print('Hyd')
	print('Sec')
	print('Cyb')
# Error due to except suite is missing




#2. Find  outputs  (Home  work)
#print(7 / 0) # ZeroDivisionError
try:
	print(7 / 0) 
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted') # Division  by  zero  is  not  permitted
#print(7 / 0) # ZeroDivisionError
print('Bye') # Bye




#3. Identify  error  (Home  work)
except:
        print('Hyd')
        print('Sec')
        print('Cyb')
# Error due to except without try




#4. Find  outputs (Home  work)
try:
        print('One') # One
        print('Two') # Two
        print('Three') # Three
#print('Four') # Error due to after try suite except suite should be there , not any other statement
except:
		print('Five') # Five
		print('Six') # Six
		print('Seven') # Seven
print('Eight') # Eight




#5. Find  outputs  (Home work)
try:
	print('try suite')
except:
	print('default  except')
except NameError:
	print('Name  Error')
# Error due to specified should come before default except




#6. Find  outputs  (Home  work)
try:
	print('try suite')
except:
	print('1st  default  except')
except:
	print('2nd  default  except')
# Error due to multiple default except blocks are not allowed





#7.  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0) # Raises ZeroDivisionError
print(7 / 0.0) # Raises ZeroDivisionError
print(0 / 0) # Raises ZeroDivisionError
print(0.0 / 0.0) # Raises ZeroDivisionError
print(7 // 0) # Raises ZeroDivisionError
print(7 % 0) # Raises ZeroDivisionError




#8.Which  of  the  following  statements  raise  ValueError ?  (Home  work)
import  math
print(int('10.8')) # Raises ValueError
print(float('Ten')) # Raises ValueError
print(complex('True')) # Raises ValueError
print(bool('Ten')) # Raises ValueError
print(bool('')) # False
print(float('10.8')) # 10.8
print(float('25')) # 25.0
print(int(10.8)) # 10
print(math . sqrt(-25)) # Raises ValueError





#9. Which  of  the  following  statements  raise  NameError ?
a = 25
print(a) # 25
del  a 
print(a) # Raises NameError
print(eval("   'Ten'   ")) # 'Ten'
print(eval('Ten')) # Raises NameError






#10. Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0]) # H
print('Hyd'[1]) # y
print('Hyd'[2]) # d
print('Hyd'[3]) # Raises IndexError
list = [10 , 20 , 15 , 18]
print(list[0]) # 10
print(list[3]) # 18
print(list[4]) # Raises IndexError
print(list[-1]) # 18
print(list[-4]) # 10
print(list[-5]) # Raises 
tpl = (10 , 20 , 30)
print(tpl[3]) # Raises IndexError
r = range(10)
print(r[10]) # Raises IndexError
s = {10 , 20 , 15 , 18}
print(s[4]) # Raises TypeError
d = {10 : 'Hyd' , 20 : 'Sec'}
print(d[0]) # Raises KeyError





#11.  Which  of  the  following  statements  raise TypeError ?
print(10 + 20) # 30
print('10' + '20') # '1020'
print(10 + '20') # Raises TypeError
print(len('25')) # 2
print(len(25)) # Raises TypeError
s = {10 , 20 , 15 , 18}
print(s[0]) # Raises TypeError
b = { [10 , 20] : [30 , 40] }
print(int(3 + 4j)) # Raises TypeError
print(int([10 , 20 , 30])) # Raises TypeError
print(float(None)) # Raises TypeError





#12. Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G']) # Green
print(a['Y']) # Raises KeyError




#13. Find  outputs  (Home  work)
try:
	print(7 / 0) # ZeroDivisionError
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1') # ZDE  1
except    ZeroDivisionError:
	print('ZDE  2') # ignored
print('Bye') # Bye






#14. Find  outputs  (Home  work)
try:
	print(7 / 0) # ZeroDivisionError
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1') # ZDE  1
	print(8 / 0) # ZeroDivisionError
except    ZeroDivisionError:
	print('ZDE  2') # ignored
print('Bye') # Bye





#15. Find  outputs
try:
	print(7 / 0) # ZeroDivisionError
	print('Hello')
except  ZeroDivisionError:
	print('ZDE  1') # ZDE  1
	try:
		print(8 / 0) # ZeroDivisionError
	except  ZeroDivisionError:
		print('ZDE   2') # ZDE   2
	print('Bye') # Bye
except  ZeroDivisionError:
	print('ZDE  3') # ignored
print('End') # End




#16.
try:
	print(7 / 0) # ZeroDivisionError
except   ArithmeticError:
	print('Arithmetic Error') # Arithmetic Error
except   ZeroDivisionError:
	print('Zero Division  Error') # ignored
print('End') # End
# Arithmetic Error is parent class of ZeroDivisionError , so first child class except block should come before parent class except block



#17. Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function') # f1  function
		print(7 / 0) # ZeroDivisionError
	except  ValueError:
		print('Hello') 
	try:
		print(int('Ten')) # ValueError
	except ZeroDivisionError:
		print('Bye') 
	print('End  of  f1  function') 
try:
	print('Begin') # Begin
	f1() 
	print('Hi')
except  ZeroDivisionError:
	print('ZDE  is  caught  outside') # ZDE  is  caught  outside
except:
	print('Bye') # ignored
print('End') # End





#18. Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function') # f1  function
		print(7 / 0) # ZeroDivisionError
	except  ValueError:
		print('Hello')
	except  ZeroDivisionError:
		print('ZDE  is  caught  by  f1  function') # ZDE  is  caught  by  f1  function
	print('End  of  f1  function') # End  of  f1  function
# End  of  the  function
try:
	print('Begin') # Begin
	f1() # Go to f1 function
	print('Hello') # Hello
except  ZeroDivisionError:
	print("Hi") # ignored
except  ValueError:
	print("Bye") # ignored
print('End') # End






#19.
#What  are   the  outputs  if  input  is  1 ?  ---> Invalid  index

#What  are   the  outputs  if  input  is  2 ?  ---> Invalid  index

#What  are   the  outputs  if  input  is  3 ?  ---> No  result

#What  are   the  outputs  if  input  is  4 ?  ---> Invalid   argument (or)  operand

#What  are   the  outputs  if  input  is  5 ?  ---> Object  does  not  exist

#What  are   the  outputs  if  input  is  6 ?  ---> Div by 0 is not allowed

#What  are   the  outputs  if  input  is  7 ?  ---> Invalid   argument (or)  operand

#What  are   the  outputs  if  input  is  8 ?  ---> Invalid dict key

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





#20.  Find  outputs
def  f1():
	print('f1  function') # f1  function
	raise   ValueError('Hyd')
	print('Sec')
# End of  the  function
f1()
try:
	print('Begin') # Begin
	f1() # Go to f1 function
	print('Bye')
except  ValueError  as  msg:
	print('Caught  ValueError  outside  the  function  :  ' , msg) # Caught  ValueError  outside  the  function  :  Hyd
f1() # Go to f1 function
print('End of the program') # Not executed



#21. Find  outputs  (Home  work)
def  f1(a):
	print('f1  function') # f1  function
	if   a == 20:
		raise  ArithmeticError()
	elif   a == 0:
		raise  IndexError()
	elif  a == 10:
		raise  TypeError(25)
	raise ValueError()
# end of  the function
try:
	print('Begin') # Begin
	f1(10) # Caught  TypeError  outside  the  function :   25
	f1(20) # ignored
	f1(30) # ignored
	f1(0) # ignored
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
print('End') # End+





#22. Find  outputs  (Home  work)
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
#Caught  ValueError  :   25
#End  of  f1  function
##Caught   NameError  :   10.8
#End  of  f1  function
#Caught  IndexError  :   Hyd
#End  of  f1  function
#Caught   EOFError  :   True
#End  of  f1  function
#End of the program





#23.  Find  outputs  (Home  work)
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
#Begin
#f1 function
#Caught  by  f1 function  :  25
#Recaught  by  f1 function  :  25
#End  of  f1  function
#Hyd
#End of the program





#24.  Find  outputs  (Home  work)
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
#Begin
#f1 function
#Caught  by  f1 function  :  25
#Recaught ValueError  :   25
#End of the program





#26. Find  outputs  (Home   work)
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
#Begin
#f1 function
#Caught  by  f1 function  :   25
#Some other error
#End of the program





#27.  Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
	for  i  in  range(10):
		print('child  thread')
child = Thread(target = f1)
f1()
for  i  in  range(10):
        print('main  thread')
#child thread
#child thread
#...
#main thread
#main thread
#...




#28.  Find  outputs  (Home  work)
from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')
child = Thread(target =  f1())
child . start()
for  i  in  range(10):
        print('main  thread')
#child thread
#child thread
#...
#main thread
#main thread
#...






#29. Find  outputs  (Home  work)
from  threading  import  *
def   f1():
        for  i  in  range(10):
                print('child  thread')
child = Thread()
child . start()
for  i   in   range(10):
        print('main  thread')
#main thread
#main thread
#...





#30. Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
        for  i  in  range(10):
                print('Child  Thread')
child = Thread(target = f1)
child . start()
for  i  in  range(10):
        print('Main  Thread')
child . start()
# After executing child.start() 1st time ,it can not start again , so it raises RuntimeError






#31. Find  outputs  (Home  work)
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
#child thread
#main thread
#...
#child thread
#main thread
#...





#32. Find  outputs (Home  work)
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
#child thread
#child thread
#...
#main thread
#main thread
#...





#33.  Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i   in  range(1 , 11):
			print('Child  Thread  :  ' , i)
child = Thread( target = c1.m1 ) # How  to  specify  the  target  as  class  method)
child . start()
for  i  in  range(1 , 11):
        print('Main  Thread  :  ' , i)




#34. Identify  error  (Home  work)
from  threading  import  Thread
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
# End of the class
t = Thread()
t . start() # Error due to start()  method is not defined in user defined Thread class
for  i  in  range(10):
        print('main  thread')



#35. Find  outputs  (Home  work)
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
from  threading  import  Thread
t = Thread()
t . start()
for  i  in  range(10):
        print('Main  Thread')
# main thread
# main thread
# ...




#36. Find  outputs  (Home  work)
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
#child thread
#child thread
#...
#main thread
#main thread
#...




#37. Find  outputs (Home  work)
from  threading  import *
class    MyThread(Thread):
	def  walk(self):
		for  i  in  range(10):
			print('walk  method')
child = MyThread()
child . start()
for  i  in  range(10):
	print('Main  Thread')
# main thread
# main thread
# ...




#38. Find  outputs
from  threading  import  *
class   MyThread(Thread):
	def   run(self):
			print('run  method')
def  f1():
	print('f1  function')
child = MyThread(target = f1)
child . start()
print('Main  Thread')
# run  method
# Main  Thread




#39. Find  outputs
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
# f1  function :  1
# Main  Thread :  1
# ...
# f1  function :  10
# Main  Thread :  10






#40. Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
child = MyThread()
child . start()
print('Main  Thread')
# Main  Thread
