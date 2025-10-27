#1st program
# Identify  Error  (Home  work)
try:
	print('Hyd')
	print('Sec')
	print('Cyb')
#error because there is no except suite


#2nd  program
# Find  outputs  (Home  work)
#print(7 / 0)#ZeroDivisionError
try:
	print(7 / 0)#Division by zero is not permitted
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')
#print(7 / 0)#ZeroDivisionError
print('Bye')#Bye


#3rd  program
# Identify  error  (Home  work)
except:
        print('Hyd')
        print('Sec')
        print('Cyb')
#error because except cannot be used without try suite


#4th  program
# Find  outputs (Home  work)
try:
        print('One')#one
        print('Two')#two
        print('Three')#Three
#print('Four')#Error coz stmts after try suite should be inside except suite
except:
		print('Five')
		print('Six')
		print('Seven')
print('Eight')#Eight


#5th  program
# Find  outputs  (Home work)
try:
	print('try suite') #try suite
#except: #Error coz default except should be at the end of all except suites
#	print('default  except')
except NameError:
	print('Name  Error')


#6th  program
# Find  outputs  (Home  work)
try:
	print('try suite')#try suite
#except:
#	print('1st  default  except') #error default except must be at the last
except:
	print('2nd  default  except')


#7th  program
#  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0)#error
print(7 / 0.0)#error
print(0 / 0)#error
print(0.0 / 0.0)#error
print(7 // 0)#error
print(7 % 0)#Error


# 8th  program
#  Which  of  the  following  statements  raise  ValueError ?  (Home  work)
import  math
#print(int('10.8'))#valueerror
#print(float('Ten'))#valueerror
#print(complex('True'))#valueerror
print(bool('Ten'))#True
print(bool(''))#False
print(float('10.8'))#10.8
print(float('25'))#25.0
print(int(10.8))#10
#print(math . sqrt(-25))#value error


#9th  program
# Which  of  the  following  statements  raise  NameError ?
a = 25
print(a)#25
del  a
#print(a)#Name Error
print(eval("   'Ten'   "))#Ten
#print(eval('Ten'))#Name Error


#10th  program
# Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0])#H
print('Hyd'[1])#y
print('Hyd'[2])#d
#print('Hyd'[3])#IndexError
list = [10 , 20 , 15 , 18]
print(list[0])#10
print(list[3])#18
#print(list[4])#IndexError
print(list[-1])#18
print(list[-4])#10
#print(list[-5])#IndexError
tpl = (10 , 20 , 30)
#print(tpl[3])#IndexError
r = range(10)
#print(r[10])#IndexError
s = {10 , 20 , 15 , 18}
#print(s[4]) #TypeError NO INDEXES IN SET
d = {10 : 'Hyd' , 20 : 'Sec'}
#print(d[0])#KeyError


#11th  program
#  Which  of  the  following  statements  raise TypeError ?
print(10 + 20)#30
print('10' + '20')#1020
#print(10 + '20')#TypeError
print(len('25'))#2
#print(len(25))#TypeError
s = {10 , 20 , 15 , 18}
#print(s[0])#TypeError
#b = { [10 , 20] : [30 , 40] }#TypeError
#print(int(3 + 4j))#TypeError
#print(int([10 , 20 , 30]))#TypeError
#print(float(None))#TypeError


#12th  program
# Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G'])#Green
print(a['Y'])#Key Error


#13th  program
# Find  outputs  (Home  work)
try:
	print(7 / 0)#ZeroDivisionError
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')#ZDE 1
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye')#Bye


#14th  program
# Find  outputs  (Home  work)
try:
	print(7 / 0)#ZeroDivisionError
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')#ZDE 1
	#print(8 / 0)#re raised and not handled so error
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye')#Bye


#15th program
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


#16th program
'''
Find  outputs  (Home  work)

Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError
'''
try:
	print(7 / 0)
except   ArithmeticError:
	print('Arithmetic Error')#Arithmetic Error is caught though it is ZDE coz AE is parent error
except   ZeroDivisionError:
	print('Zero Division  Error')
print('End')#End


#17th
# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')#f1 function
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
	print('Begin')#Begin
	f1()
	print('Hi')
except  ZeroDivisionError:
	print('ZDE  is  caught  outside')#ZDE  is  caught  outside
except:
	print('Bye')
print('End')#End


#18th
# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')#f1 function
		print(7 / 0)
	except  ValueError:
		print('Hello')
	except  ZeroDivisionError:
		print('ZDE  is  caught  by  f1  function')#ZDE  is  caught  by  f1  function
	print('End  of  f1  function')#End  of  f1  function
# End  of  the  function
try:
	print('Begin')#Begin
	f1()
	print('Hello')#Hello
except  ZeroDivisionError:
	print("Hi")
except  ValueError:
	print("Bye")
print('End')#End


#19th
'''
What  are   the  outputs  if  input  is  1 ?  --->Invalid  index

What  are   the  outputs  if  input  is  2 ?  --->Invalid  index

What  are   the  outputs  if  input  is  3 ?  --->No  result

What  are   the  outputs  if  input  is  4 ?  --->Invalid   argument (or)  operand

What  are   the  outputs  if  input  is  5 ?  --->Object  does  not  exist

What  are   the  outputs  if  input  is  6 ?  --->Div by 0 is not allowed

What  are   the  outputs  if  input  is  7 ?  --->Invalid   argument (or)  operand

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


#20th
#  Find  outputs
def  f1():
	print('f1  function')#f1 function
	#raise   ValueError('Hyd')#error because it is not inside try block
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
print('End of the program')#End of the program

'''
f1  function
Sec
Begin
f1  function
Sec
Bye
f1  function
Sec
End of the program
'''

#21st 
#Find  outputs  (Home  work)
def  f1(a):
	print('f1  function')
	if   a == 20:
		raise  ArithmeticError()
	elif   a == 0:
		raise  IndexError()
	elif  a == 10:
		raise  TypeError(25)#Caught  TypeError  outside  the  function :  25

	raise ValueError()
# end of  the function
try:
	print('Begin')#Begin
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
print('End')#End


#22nd
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
f1(10)#Caught  ValueError  :  25
f1(20)#Caught  NameError  :  10.8
f1(30)#Caught  IndexError  :  Hyd 
f1(0)#Caught  EOFError  :  True
print('End of the program')#End of the program

'''
Caught  ValueError  :   25
End  of  f1  function
Caught   NameError  :   10.8
End  of  f1  function
Caught  IndexError  :   Hyd
End  of  f1  function
Caught   EOFError  :   True
End  of  f1  function
End of the program
'''

#23rd
#  Find  outputs  (Home  work)
def f1():
	try:
		print('f1 function')#f1 function
		raise  ValueError(25)
		print('Hi')
	except  ValueError  as  msg:
		try:
			print('Caught  by  f1 function  : ' , msg)#Caught  by  f1 function  :25
			raise   ValueError(msg)#Recaught  by  f1 function  :25
		except  ValueError  as   msg:
			print('Recaught  by  f1 function  : ' , msg)
	except:
		print('Hello')
	print('End  of  f1  function')#End of f1 function
# End  of  f1()  function
try:
	print('Begin')#Begin
	f1()
	print('Hyd')#hyd
except  ValueError  as  x:
	print('Recaught ValueError  :  ' , x)
except:
	print('Some other error')
print('End of the program')#End of the program


#24th
#  Find  outputs  (Home  work)
def f1():
	try:
		print('f1 function')#f1 function
		raise  ValueError(25)
		print('Hi')#skipped
	except  ValueError  as  msg:
		print('Caught  by  f1 function  : ' , msg)#Caught  by  f1 function  : 25
		raise   ValueError(msg)
	except:
		print('Hello')
	print('End  of  f1  function')
# End  of  f1()  function
try:
	print('Begin')#Begin
	f1()
	print('Hyd')
except  ValueError  as  x:
	print('Recaught ValueError  :  ' , x)#Recaught ValueError  :  25
except:
	print('Some other error')
print('End of the program')#End of the program


#25th
# Find  outputs  (Home   work)
def f1():
	try:
		print('f1 function')#f1 function
		raise  ValueError(25)
		print('Hi')#skipped
	except  ValueError  as  msg:
		print('Caught  by  f1 function  :  ' , msg)#Caught  by  f1 function  :  25
		raise  NameError(msg)#Some other error
	except:
		print('Hello')
	print('End of f1 function')
# End  of  the  function
try:
	print('Begin')#Begin
	f1()
	print('Hyd')
except  ValueError  as  x:
	print('Recaught ValueError : ' , x)
except:
	print('Some other error')#Some other error
print('End of the program')#End of the program


#26th
#  Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
	for  i  in  range(10):
		print('child  thread')#1st 10 times child thread
child = Thread(target = f1)
f1()
for  i  in  range(10):
        print('main  thread')#next 10 times main thread


#27th
#  Find  outputs  (Home  work)
from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')#1st 10 times child thread
child = Thread(target =  f1())
child . start()
for  i  in  range(10):
        print('main  thread')#next 10 times main thread


#28th
# Find  outputs  (Home  work)
from  threading  import  *
def   f1():
        for  i  in  range(10):
                print('child  thread')
child = Thread()
child . start()
for  i   in   range(10):
        print('main  thread')#10 times main thread


#29th
# Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
        for  i  in  range(10):
                print('Child  Thread')
child = Thread(target = f1)
child . start()#unpredictable
for  i  in  range(10):
        print('Main  Thread')
#child . start()#error 


#30th
# Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child  = Thread(target = a . m1)
child . start()#unpredictable
a . m1()#10 times child thread
for  i  in  range(10):
	print('main  thread')


#31st
# Find  outputs (Home  work)
from  threading  import   *
class   c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child = Thread(target =  a . m1())
child . start()#1o times child thread
for  i  in  range(10):
        print('main  thread')#10 times main thread


#32nd
#  Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	@classmethod
	def  m1(cls):
		for  i   in  range(1 , 11):
			print('Child  Thread  :  ' , i)
child = Thread(target=c1.m1)#How  to  specify  the  target  as  class  method)
child . start()#unpredictable 
for  i  in  range(1 , 11):
        print('Main  Thread  :  ' , i)


#33rd
# Identify  error  (Home  work)
from  threading  import  Thread
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
# End of the class
t = Thread()
#t . start()#error no start method in thread class
for  i  in  range(10):
        print('main  thread')#10 times main thread
		

#34th       
# Find  outputs  (Home  work)       
class   Thread:
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
from  threading  import  Thread
t = Thread()
t . start()
for  i  in  range(10):
        print('Main  Thread')#10 times main thread
		

#35th
# Find  outputs  (Home  work)
from threading import *
class    MyThread(Thread):
        def   run(self):
                for  i  in  range(10):
                        print('child  thread')
#end of the class
child = MyThread()
child . run()#10 times child thread
for  i  in  range(10):
        print('main  thread')#10 times main thread
		

#36th
# Find  outputs (Home  work)
from  threading  import *
class    MyThread(Thread):
	def  walk(self):
		for  i  in  range(10):
			print('walk  method')
child = MyThread()
child . start()
for  i  in  range(10):
	print('Main  Thread')#10 times main thread
	

#37th
# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	def   run(self):
			print('run  method')
def  f1():
	print('f1  function')
child = MyThread(target = f1)
child . start()#run method
print('Main  Thread')#main thread


#38th
# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
def  f1():
	for  i  in   range(1 , 11):
		print('f1  function : ' , i)#unpredictable
child = MyThread(target = f1)
child . start()
for  i  in  range(1 , 11):
	print('Main  Thread : ' , i)
	
#39th
# Find  outputs
from  threading  import  *
class   MyThread(Thread):
	pass
child = MyThread()
child . start()
print('Main  Thread')#Main Thread