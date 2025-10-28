# Identify  Error  (Home  work)
try:
	print('Hyd')
	print('Sec')
	print('Cyb')
	
#Error no except block

# Find  outputs  (Home  work)
print(7 / 0)                                                # ZeroDivisionError
try:
	print(7 / 0)                                            # Error
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')         # Division  by  zero  is  not  permitted
print(7 / 0)                                                # ZeroDivisionError
print('Bye')                                                # Bye

# Identify  error  (Home  work)
except:                                                     # Error no try block
        print('Hyd')
        print('Sec')
        print('Cyb')


# Find  outputs (Home  work)
try:
        print('One')                            #one
        print('Two')                            #two
        print('Three')                          #three
        print('Four')                           # Four
except: 
		print('Five')
		print('Six')
		print('Seven')
print('Eight')                                  #eight

# Find  outputs  (Home work)
try:
	print('try suite')                          # try suite
except:
	print('default  except')                    # default  except
except NameError:                               # error NameError should come before except
	print('Name  Error')
	
# Find  outputs  (Home  work)
try:
	print('try suite')                          # try suite
except:
	print('1st  default  except')               # 1st  default  except
except:                                         # only one except block is allowed
	print('2nd  default  except')

#  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0)                                    # ZeroDivisionError
print(7 / 0.0)                                  # ZeroDivisionError
print(0 / 0)                                    # ZeroDivisionError
print(0.0 / 0.0)                                # ZeroDivisionError
print(7 // 0)                                   # ZeroDivisionError
print(7 % 0)                                    # ZeroDivisionError

#  Which  of  the  following  statements  raise  ValueError ?  (Home  work)
import  math
print(int('10.8'))                              # ValueError
print(float('Ten'))                             # ValueError
print(complex('True'))                          # ValueError
print(bool('Ten'))                              # True
print(bool(''))                                 # False
print(float('10.8'))                            # 10.8
print(float('25'))                              # 25.0
print(int(10.8))                                # 10
print(math . sqrt(-25))                         # ValueError



'''
When  is  ValueError  raised  ?  --->  When   a  function  (or)  method  does  not  return  any  result
													       i.e. not  even  None
'''

# Which  of  the  following  statements  raise  NameError ?
a = 25 
print(a)                                        # 25
del  a
print(a)                                        # NameError
print(eval("   'Ten'   "))                      # Ten
print(eval('Ten'))                              # NameError


'''
When  is  NameError  raised ?  --->  When  a  non-existing  object  is  being  used
'''

# Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0])                                 # H
print('Hyd'[1])                                 # y
print('Hyd'[2])                                 # d
print('Hyd'[3])                                 # IndexError
list = [10 , 20 , 15 , 18]
print(list[0])                                  # 10
print(list[3])                                  # 18
print(list[4])                                  # IndexError
print(list[-1])                                 # 18
print(list[-4])                                 # 10
print(list[-5])                                 # IndexError
tpl = (10 , 20 , 30)
print(tpl[3])                                   # IndexError
r = range(10)   
print(r[10])                                    # IndexError
s = {10 , 20 , 15 , 18}
print(s[4])                                     # IndexError
d = {10 : 'Hyd' , 20 : 'Sec'}
print(d[0])                                     # KeyError


'''
When  is  IndexError  raised  ?  --->  When  a  non-existing  index  is  being  used
'''

#  Which  of  the  following  statements  raise TypeError ?
print(10 + 20)                                  # 30
print('10' + '20')                              # 1020
print(10 + '20')                                # TypeError
print(len('25'))                                # 2
print(len(25))                                  # TypeError
s = {10 , 20 , 15 , 18}  
print(s[0])                                     # TypeError
b = { [10 , 20] : [30 , 40] }                   # TypeError
print(int(3 + 4j))                              # TypeError
print(int([10 , 20 , 30]))                      # TypeError
print(float(None))                              # TypeError


'''
When  is  TypeError  raised ? ---> When  the  operands  are  illegal  in  an  expression
																			            (or)
													  when  an  illegal  argument  is  passed  to  the  function (or)  method
'''

# Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G'])                                   # Green
print(a['Y'])                                   # KeyError


'''
When  is  KeyError  raised  ?  ---> When  the  dictionary  key  is  invalid
'''

# Find  outputs  (Home  work)
try:
	print(7 / 0)                            # Error   
	print('Hello')      
except    ZeroDivisionError:
	print('ZDE  1')                         # ZDE 1
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye')                                # Bye



# Find  outputs
try:
	print(7 / 0)
	print('Hello')
except  ZeroDivisionError:
	print('ZDE  1')                         # ZDE 1
	try:
		print(8 / 0)
	except  ZeroDivisionError:
		print('ZDE   2')                    # ZDE 2
	print('Bye')                            # Bye
except  ZeroDivisionError:
	print('ZDE  3')
print('End')                                # End




'''
Find  outputs  (Home  work)

Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError
'''
try:
	print(7 / 0)
except   ArithmeticError:
	print('Arithmetic Error')               # Arithmetic Error
except   ZeroDivisionError:
	print('Zero Division  Error')
print('End')                                # Bye



# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')               # f1 function
		print(7 / 0)
	except  ValueError:
		print('Hello')
	try:
		print(int('Ten'))
	except ZeroDivisionError:
		print('Bye')                        # Bye
	print('End  of  f1  function')          # End of f1 function
# End of f1  function
try:
	print('Begin')                          # Begin
	f1()
	print('Hi')                             # Hi
except  ZeroDivisionError:
	print('ZDE  is  caught  outside')
except:
	print('Bye')
print('End')                                # End




# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')                           # f1 function
		print(7 / 0)
	except  ValueError:
		print('Hello')                                  # Hello
	except  ZeroDivisionError:
		print('ZDE  is  caught  by  f1  function')      # ZDE  is  caught  by  f1  function
	print('End  of  f1  function')                      # End of f1 function
# End  of  the  function
try:
	print('Begin')                                      # Begin
	f1()
	print('Hello')                                      # Hello
except  ZeroDivisionError:
	print("Hi")
except  ValueError:
	print("Bye")
print('End')                                            # End 




'''
What  are   the  outputs  if  input  is  1 ?  --->  #Invalid  index

What  are   the  outputs  if  input  is  2 ?  ---> #Invalid  index

What  are   the  outputs  if  input  is  3 ?  ---> # Invalid   argument (or)  operand

What  are   the  outputs  if  input  is  4 ?  ---> #Invalid   argument (or)  operand

What  are   the  outputs  if  input  is  5 ?  --->#Invalid   argument (or)  operand

What  are   the  outputs  if  input  is  6 ?  ---> #Div by 0 is not allowed

What  are   the  outputs  if  input  is  7 ?  ---> #Invalid   argument (or)  operand

What  are   the  outputs  if  input  is  8 ?  ---> #Invalid dict key
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
	print('f1  function')                       # f1 function
	raise   ValueError('Hyd')                   # ValueError : Hyd
	print('Sec')
# End of  the  function
f1()
try:
	print('Begin')                                                      # Begin
	f1()
	print('Bye')                                                        # Bye
except  ValueError  as  msg:
	print('Caught  ValueError  outside  the  function  :  ' , msg)      # Caught  ValueError  outside  the  function  :   Hyd
f1()  
print('End of the program')                                             # End of the program


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
	print('Hyd')
except  IndexError:
	print('Sec')
except  TypeError  as   msg:
	print('Caught  TypeError  outside  the  function :  '  , msg)
except  ValueError:
	print('Hello')
except:
	print('some error')
print('End')


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
		print('Caught  IndexError  :  ' , msg)              # Caught  IndexError  :   Hyd     
	except ValueError  as  msg:
		print('Caught  ValueError  :  ' , msg)              # Caught  ValueError  :   25
	except  NameError  as  msg:
		print('Caught   NameError  :  ' , msg)              # Caught   NameError  :   10.8
	except  EOFError  as  msg:
		print('Caught   EOFError  :  '  , msg)              # Caught   EOFError  :   True
	print('End  of  f1  function')                          # End  of  f1  function
#outside the function
f1(10)
f1(20)
f1(30)
f1(0)
print('End of the program')                                 # End of the program


#  Find  outputs  (Home  work)
def f1():
	try:
		print('f1 function')                                # f1 function
		raise  ValueError(25)
		print('Hi')
	except  ValueError  as  msg:
		try:
			print('Caught  by  f1 function  : ' , msg)      # Caught  by  f1 function  :  25
			raise   ValueError(msg)
		except  ValueError  as   msg:
			print('Recaught  by  f1 function  : ' , msg)    # Recaught  by  f1 function  :  25
	except:
		print('Hello')
	print('End  of  f1  function')                          # End of f1 function
# End  of  f1()  function
try:
	print('Begin')                                          # Begin
	f1()
	print('Hyd')                                            # Hyd
except  ValueError  as  x:
	print('Recaught ValueError  :  ' , x)
except:
	print('Some other error')
print('End of the program')                                 # End of the program



#  Find  outputs  (Home  work)
def f1():
	try:
		print('f1 function')                                # f1 function
		raise  ValueError(25)
		print('Hi')
	except  ValueError  as  msg:
		print('Caught  by  f1 function  : ' , msg)          # Caught  by  f1 function  :  25
		raise   ValueError(msg)
	except:
		print('Hello')
	print('End  of  f1  function')                          # End of f1 program
# End  of  f1()  function
try:
	print('Begin')                                          # Begin
	f1()
	print('Hyd')                
except  ValueError  as  x:
	print('Recaught ValueError  :  ' , x)                   # Recaught ValueError  :   25
except:
	print('Some other error')
print('End of the program')                                 # End of the program



# Find  outputs  (Home   work)
def f1():
	try:
		print('f1 function')                            # f1 function
		raise  ValueError(25)
		print('Hi')
	except  ValueError  as  msg:
		print('Caught  by  f1 function  :  ' , msg)     # Caught  by  f1 function  :   25
		raise  NameError(msg)
	except:
		print('Hello')
	print('End of f1 function')
# End  of  the  function
try:
	print('Begin')                                  # Begin
	f1()
	print('Hyd')                                    # Hyd
except  ValueError  as  x:
	print('Recaught ValueError : ' , x)
except:
	print('Some other error')
print('End of the program')                         # End of the program



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
no thread started so everything runs in main thread
outputs  :
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
everything runs in main thread as f1() is called directly
outputs  :
child thread for 10 times
main thread for 10 times
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
everything runs in main thread as no target function is specified
outputs  :
main thread for 10 times
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
RuntimeError: threads can only be started once
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
everything runs in main thread as m1() is called directly
outputs  :

child thread for 10 times
main thread for 10 times
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
everything runs in main thread as m1() is called directly
outputs  :
child thread for 10 times
main thread for 10 times
'''

#  Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i   in  range(1 , 11):
			print('Child  Thread  :  ' , i)
child = Thread(target=c1.m1)#How  to  specify  the  target  as  class  method)
child . start()
for  i  in  range(1 , 11):
        print('Main  Thread  :  ' , i)
		
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
'''
AttributeError: 'Thread' object has no attribute 'start'
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
everything runs in main thread as threading.Thread is shadowed by user-defined Thread class
outputs  :
Main Thread for 10 times
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
everything runs in main thread as run() is called directly
outputs  :
child thread for 10 times
main thread for 10 times
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
everything runs in main thread as walk() is never called
outputs  :
Main Thread for 10 times
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
outputs  :
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
outputs  :
f1 function :  1 to 10 (not in order)
Main Thread :  1 to 10 (not in order)
'''


# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
child = MyThread()
child . start()
print('Main  Thread')

'''
outputs  :
run  method
Main  Thread
'''
