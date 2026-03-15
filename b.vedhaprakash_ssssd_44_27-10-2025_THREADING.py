---- home work on 27/10/2025 
# Identify  Error  (Home  work)
try:
	print('Hyd')
	print('Sec')
	print('Cyb') 
# error is no except and no finally 


----------------------------------

# Find  outputs  (Home  work)
print(7 / 0) # it raise a ZDE and below code is not executed because it never reaches the try or except or print(bye) line
try:
	print(7 / 0)
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')
print(7 / 0)
print('Bye')  

----------------------------------------------

# Identify  error  (Home  work)
except:
        print('Hyd')
        print('Sec')
        print('Cyb')

# no try: block there should be a try without these except cant exist by itself 

------------------------------------------------

# Find  outputs (Home  work)
try:
        print('One')
        print('Two')
        print('Three')
print('Four') # raises error because in between try and except there should not be any statement 
except:
		print('Five')
		print('Six')
		print('Seven')
print('Eight')

# program is not runned 
--------------------------------------------------

# Find  outputs  (Home work)
try:
	print('try suite')
except:
	print('default  except')
except NameError:  # these line is default error should be at last 
	print('Name  Error')

---------------------------------------------------

# Find  outputs  (Home  work)
try:
	print('try suite')
except:
	print('1st  default  except')
except:                                  # default except must be last 
	print('2nd  default  except')



------------------------------------------------------

#  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0) #ZDE
print(7 / 0.0) #ZDE
print(0 / 0) #ZDE
print(0.0 / 0.0) # these line doesnot raise error 
print(7 // 0) #ZDE
print(7 % 0) #ZDE

---------------------------------------------------------

#  Which  of  the  following  statements  raise  ValueError ?  (Home  work)
import  math
print(int('10.8')) #ValueError
print(float('Ten')) #ValueError
print(complex('True')) # ValueError
print(bool('Ten')) #NO ValueError
print(bool('')) # NO ValueError
print(float('10.8')) # NO ValueError
print(float('25')) # NO ValueError
print(int(10.8)) # NO ValueError
print(math . sqrt(-25)) #ValueError


'''
When  is  ValueError  raised  ?  --->  When   a  function  (or)  method  does  not  return  any  result
													       i.e. not  even  None
'''

---------------------------------------------------------------------------------------



# Which  of  the  following  statements  raise  NameError ?
a = 25
print(a) # PRINTS 25
del  a # DELETES OBJECT 
print(a) # NameError 
print(eval("   'Ten'   ")) # PYTHON SEES IT AS STR AND TAKES AS 'TEN'
print(eval('Ten')) # NameError


'''
When  is  NameError  raised ?  --->  When  a  non-existing  object  is  being  used
'''


---------------------------------------------------------------------------------------------
# Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0])
print('Hyd'[1])
print('Hyd'[2])
print('Hyd'[3]) # Index Error
list = [10 , 20 , 15 , 18]
print(list[0])
print(list[3])
print(list[4]) # Index Error
print(list[-1])
print(list[-4]) #prints 10 
print(list[-5]) # Index Error
tpl = (10 , 20 , 30)
print(tpl[3]) # Index Error
r = range(10)
print(r[10]) # # Index Error
s = {10 , 20 , 15 , 18}
print(s[4])
d = {10 : 'Hyd' , 20 : 'Sec'}
print(d[0])


'''
When  is  IndexError  raised  ?  --->  When  a  non-existing  index  is  being  used
'''

--------------------------------------------------------------------------------------------


#  Which  of  the  following  statements  raise TypeError ?
print(10 + 20) # TypeError
print('10' + '20')
print(10 + '20')
print(len('25'))
print(len(25)) # TypeError 
s = {10 , 20 , 15 , 18}
print(s[0])
b = { [10 , 20] : [30 , 40] } # TypeError
print(int(3 + 4j)) # TypeError 
print(int([10 , 20 , 30])) # TypeError 
print(float(None)) # TypeError


'''
When  is  TypeError  raised ? ---> When  the  operands  are  illegal  in  an  expression  (or) when  an  illegal  argument  is  passed  to  the  function (or)  method
'''
------------------------------------------------------------------------------------------------------------------

# Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G'])
print(a['Y']) # KeyError 


'''
When  is  KeyError  raised  ?  ---> When  the  dictionary  key  is  invalid
'''
----------------------------------------------------------------------------------------------

# Find  outputs  (Home  work)
try:
	print(7 / 0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')
except    ZeroDivisionError: # syntax error and no output for these code
	print('ZDE  2')
print('Bye')


-----------------------------------------------------------------------
# Find  outputs  (Home  work)
try:
	print(7 / 0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')
	print(8 / 0)
except    ZeroDivisionError: # here already we have ZDE 
	print('ZDE  2')
print('Bye')


-----------------------------------------------------------------------

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
except  ZeroDivisionError: # ERROR 
	print('ZDE  3')
print('End')

----------------------------------------------------------------------

'''
Find  outputs  (Home  work)

Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError
'''
try:
	print(7 / 0)
except   ArithmeticError:
	print('Arithmetic Error') # Arithmetic Error
except   ZeroDivisionError:
	print('Zero Division  Error')
print('End')  # End

-------------------------------------------------------------------

# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function') # f1 function 
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
	print('Begin') # begin
	f1()
	print('Hi')
except  ZeroDivisionError:
	print('ZDE  is  caught  outside') # prints these 
except:
	print('Bye')
print('End') # prints end


------------------------------------------------------------

# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function') # f1 function
		print(7 / 0)
	except  ValueError:
		print('Hello')
	except  ZeroDivisionError:
		print('ZDE  is  caught  by  f1  function') # prints these line 
	print('End  of  f1  function') # prints these 
# End  of  the  function
try:
	print('Begin') # begin 
	f1()
	print('Hello') # prints the hello 
except  ZeroDivisionError:
	print("Hi")
except  ValueError:
	print("Bye")
print('End') # end 

-------------------------------------------------------------
'''


What are the outputs if input is 1 ? ---> Invalid index

What are the outputs if input is 2 ? ---> Invalid index

What are the outputs if input is 3 ? ---> No result

What are the outputs if input is 4 ? ---> Invalid argument (or) operand

What are the outputs if input is 5 ? ---> Object does not exist

What are the outputs if input is 6 ? ---> Div by 0 is not allowed

What are the outputs if input is 7 ? ---> Invalid argument (or) operand

What are the outputs if input is 8 ? ---> Invalid dict key
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



------------------------------------------------------------------
#  Find  outputs
def  f1():
	print('f1  function')
	raise   ValueError('Hyd') # raises error here 
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

---------------------------------------------------------------------

#Find  outputs  (Home  work)
def  f1(a):
	print('f1  function') # f1 function 
	if   a == 20:
		raise  ArithmeticError()
	elif   a == 0:
		raise  IndexError()
	elif  a == 10:
		raise  TypeError(25)
	raise ValueError()
# end of  the function
try:
	print('Begin') # begin 
	f1(10)
	f1(20)
	f1(30)
	f1(0)
except  ArithmeticError:
	print('Hyd');
except  IndexError:
	print('Sec')
except  TypeError  as   msg:
	print('Caught  TypeError  outside  the  function :  '  , msg) # here these line is printed 
except  ValueError:
	print('Hello')
except:
	print('some error')
print('End') # end is printed at the end


-------------------------------------------------------------------

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
		print('Caught  ValueError  :  ' , msg) # 25 
	except  NameError  as  msg:
		print('Caught   NameError  :  ' , msg) # 10.8 
	except  EOFError  as  msg:
		print('Caught   EOFError  :  '  , msg) # prints these line for TRUE 
	print('End  of  f1  function') # end of function is printed for the lines 25 ,10.8 , hyd 
#outside the function
f1(10)
f1(20)
f1(30)
f1(0)
print('End of the program') # END OF THE PROGRAM 

------------------------------------------------


#  Find  outputs  (Home  work)
def f1():
	try:
		print('f1 function') # F1 FUNCTION 
		raise  ValueError(25)
		print('Hi')
	except  ValueError  as  msg:
		try:
			print('Caught  by  f1 function  : ' , msg) # CAUGHT BY F1 FUNCTION 25 
			raise   ValueError(msg)
		except  ValueError  as   msg:
			print('Recaught  by  f1 function  : ' , msg) # RECAUGHT BY F1 FUNCTION BY 25 
	except:
		print('Hello')
	print('End  of  f1  function') # END OF THE FUNCTION 
# End  of  f1()  function
try:
	print('Begin') # BEGIN 
	f1()
	print('Hyd') # HYD 
except  ValueError  as  x:
	print('Recaught ValueError  :  ' , x)
except:
	print('Some other error')
print('End of the program') # END OF THE PROGRAM 

------------------------------------------------------

#  Find  outputs  (Home  work)
def f1():
	try:
		print('f1 function') # F1 FUNCTION 
		raise  ValueError(25)
		print('Hi')
	except  ValueError  as  msg:
		print('Caught  by  f1 function  : ' , msg) # CAUGHT BY F1 FUNCTION , 25 
		raise   ValueError(msg)
	except:
		print('Hello')
	print('End  of  f1  function')
# End  of  f1()  function
try:
	print('Begin') # BEGIN 
	f1()
	print('Hyd')
except  ValueError  as  x:
	print('Recaught ValueError  :  ' , x) # RECAUGHT VALUEERROR BY , 25 
except:
	print('Some other error')
print('End of the program')# END OF THE PROGRAM 

-----------------------------------------------------------------------


# Find  outputs  (Home   work)
def f1():
	try:
		print('f1 function') # F1 FUNCTION 
		raise  ValueError(25)
		print('Hi')
	except  ValueError  as  msg:
		print('Caught  by  f1 function  :  ' , msg) # CAUGHT BY F1 FUNCTION , 25 
		raise  NameError(msg)
	except:
		print('Hello') # HELLO 
	print('End of f1 function')# END OF THE FUNCTION 
# End  of  the  function
try:
	print('Begin') # BEGIN 
	f1()
	print('Hyd')# HYD 
except  ValueError  as  x:
	print('Recaught ValueError : ' , x)
except:
	print('Some other error')
print('End of the program') # END OF THE PROGRAM 

----------------------------------------------------------------------------


#  Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
	for  i  in  range(10):
		print('child  thread') # 10 TIMES CHILD 
child = Thread(target = f1)
f1()
for  i  in  range(10):
        print('main  thread') # MAIN 10 TIMES 

-------------------------------------------------------------
#  Find  outputs  (Home  work)
from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')
child = Thread(target =  f1())
child . start()
for  i  in  range(10):
        print('main  thread')
# 10 TIMES CHILD AND MAIN THREAD 
-----------------------------------------------------------



# Find  outputs  (Home  work)
from  threading  import  *
def   f1():
        for  i  in  range(10):
                print('child  thread')
child = Thread()
child . start()
for  i   in   range(10):
        print('main  thread') # HERE MAIN THEARD IS PRINTED 10 TIMES 


------------------------------------------------------------------------------

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

# HERE THE RUN IS DIFFERENT FOR EVERY RUN 
---------------------------------------------------------------------------------

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
# PROGRAM PRINTS 10 TIMES CHILD THREADD AND REMAINING IS ERROR

----------------------------------------------------------------

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
# HERE THE UOTPUT IS DIFFERENT FOR EVERY RUN 
-----------------------------------------------------------

# Identify  error  (Home  work)
from  threading  import  Thread
class   Thread: # DOESNOT INHERIT
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
# End of the class
t = Thread() # CREATING THE OBJECT OF THE MY CLASS 
t . start() # THERE IS NO ATTRIBUTE T FOR START()
for  i  in  range(10):
        print('main  thread')
---------------------------------------------------------

# Find  outputs  (Home  work)
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
from  threading  import  Thread
t = Thread()
t . start()
for  i  in  range(10):
        print('Main  Thread') # PRINTS FOR THE 10 TIMES 

--------------------------------------------------------------------

# Find  outputs  (Home  work)
from threading import *
class    MyThread(Thread):
        def   run(self):
                for  i  in  range(10):
                        print('child  thread') # PRINTS10 TIMES 
#end of the class
child = MyThread()
child . run()
for  i  in  range(10):
        print('main  thread') # PRINTS 10 TIMES 

-------------------------------------------------------


# Find  outputs (Home  work)
from  threading  import *
class    MyThread(Thread):
	def  walk(self):
		for  i  in  range(10):
			print('walk  method')
child = MyThread()
child . start()
for  i  in  range(10):
	print('Main  Thread') # 10 TIMES 
----------------------------------------------------------------
# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	def   run(self):
			print('run  method')
def  f1():
	print('f1  function') # PRNTS 
child = MyThread(target = f1)
child . start()
print('Main  Thread') # PRINTS 

---------------------------------------------------------
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

------------------------------------------------------------------

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
# OUTUT


Main Thread : 1
f1 function : 1
Main Thread : 2
Main Thread : 3
f1 function : 2
Main Thread : 4
f1 function : 3
 ANS SOOO ON.....

--------------------------------------------

# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
child = MyThread()
child . start()
print('Main  Thread') #  PRINTS 

----------------------------------------------




















