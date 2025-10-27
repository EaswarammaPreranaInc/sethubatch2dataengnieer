#Find  outputs
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
'''