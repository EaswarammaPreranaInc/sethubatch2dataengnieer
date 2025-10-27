# Identify  Error  (Home  work)
try: # error as there is no except
	print('Hyd')
	print('Sec')
	print('Cyb')


# Find  outputs  (Home  work)
print(7 / 0) # zero division error is raised
try:
	print(7 / 0)
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')
print(7 / 0) # zero division error is raised
print('Bye')

'''
Division  by  zero  is  not  permitted
Bye
'''


# Identify  error  (Home  work)
except: # error as there is no try
        print('Hyd')
        print('Sec')
        print('Cyb')



# Find  outputs (Home  work)
try:
        print('One')
        print('Two')
        print('Three')
print('Four') # error as there is a statement between try and except block
except:
		print('Five')
		print('Six')
		print('Seven')
print('Eight')


'''
One
Two
Three
Eight
'''


# Find  outputs  (Home work)
try:
	print('try suite')
except: # error as default except must be last
	print('default  except')
except NameError:
	print('Name  Error')


# Find  outputs  (Home  work)
try:
	print('try suite')
except:
	print('1st  default  except')
except: # error as there are 2 default excepts
	print('2nd default except')



#  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0) # zero division error
print(7 / 0.0) # zero division error
print(0 / 0) # zero division error
print(0.0 / 0.0) # zero division error
print(7 // 0) # zero division error
print(7 % 0) # zero division error


#  Which  of  the  following  statements  raise  ValueError ?  (Home  work)
import  math
print(int('10.8')) # value error
print(float('Ten')) # value error
print(complex('True')) # value error
print(bool('Ten')) # True
print(bool('')) # False
print(float('10.8')) # 10.8
print(float('25')) # 25.0
print(int(10.8)) # 10
print(math . sqrt(-25)) # error as sqrt argument should not be negative


# Which  of  the  following  statements  raise  NameError ?
a = 25
print(a) # 25
del  a 
print(a) # Name error as object a is deleted
print(eval("   'Ten'   ")) # 'Ten'
print(eval('Ten')) # Name error as there is no object Ten

# Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0]) # H
print('Hyd'[1]) # y
print('Hyd'[2]) # d
print('Hyd'[3]) # Index error as there is no index 3
list = [10 , 20 , 15 , 18]
print(list[0]) # 10
print(list[3]) # 18
print(list[4]) # index error as there is no index 4 
print(list[-1]) # 18
print(list[-4]) # 10
print(list[-5]) # error as there is no index -5
tpl = (10 , 20 , 30)
print(tpl[3])  # Index error as there is no index 3 
r = range(10)
print(r[10])  # Index error as there is no index 10
s = {10 , 20 , 15 , 18}
print(s[4])  # Index error as set does not have indexes
d = {10 : 'Hyd' , 20 : 'Sec'}
print(d[0])   # Index error as dict does not have indexes


#  Which  of  the  following  statements  raise TypeError ?
print(10 + 20) # 30
print('10' + '20') # 1020
print(10 + '20') # Type Error
print(len('25')) # 2
print(len(25)) # Type error
s = {10 , 20 , 15 , 18}
print(s[0]) # error as set does not have indexes
b = { [10 , 20] : [30 , 40] } # Type error as key should not be muttable 
print(int(3 + 4j))  # Type error as type casting complex to int cannot be done
print(int([10 , 20 , 30])) # Type error as type casting list to int cannot be done
print(float(None)) # type error



# Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G']) # Green
print(a['Y']) # key error as there is no key 'y'



# Find  outputs  (Home  work)
try:
	print(7 / 0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')
except    ZeroDivisionError:
	print('ZDE 2')
print('Bye')

'''
ZDE 1
Bye
'''



# Find  outputs  (Home  work)
try:
	print(7 / 0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')
	print(8 / 0) # error is raised as it is not handeled
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye')

'''
ZDE 1
Bye
'''


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
except  ZeroDivisionError:
	print('ZDE  3')
print('End')

'''
ZDE 1
ZDE 2
Bye
'''

'''
Find  outputs  (Home  work)

Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError
'''
try:
	print(7 / 0)
except   ArithmeticError: # error as child errro should be handeled first
	print('Arithmetic Error')
except   ZeroDivisionError:
	print('Zero Division  Error')
print('End')


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
Begin
f1 function
ZDE  is  caught  by  f1  function
End  of  f1  function
Hello
End
'''

'''
What  are   the  outputs  if  input  is  1 ?  ---> Invalid Index

What  are   the  outputs  if  input  is  2 ?  ---> Invalid Index

What  are   the  outputs  if  input  is  3 ?  ---> Object  does  not  exist

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
	print('f1  function')
	raise   ValueError('Hyd')
	print('Sec')
# End of  the  function
f1() # value error is raised
try:
	print('Begin')
	f1()
	print('Bye')
except  ValueError  as  msg:
	print('Caught  ValueError  outside  the  function  :  ' , msg)
f1() # value error is raised
print('End of the program') 

'''
Begin
f1 function
Caught  ValueError  outside  the  function  :  Hyd
'''


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

'''
Begin
f1 function
Caught  TypeError  outside  the  function : 25
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
print('End of the program')

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

'''
Begin
f1 function
Caught  by  f1 function  : 25
Recaught  by  f1 function  : 25
Hyd
'''

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
print('End of the program')

'''
Begin
f1 function
Caught  by  f1 function  : 25
Recaught ValueError  : 25
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
Caught  by  f1 function  : 25
Some other error
End of the program
'''
