#  Find  outputs  (Home  work)
try:
	raise  ArithmeticError
except   ZeroDivisionError:
	print('Zero Division  Error')
except   ArithmeticError:
	print('Arithmetic Error')
print('End')


'''
Is  child  error  except  suite  executed  when  parent  error   raised ?  ---> 
'''


# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')
		raise  ValueError('Hyd')
		print('Hi')
	finally:
		print("f1's  finally")
	print('End  of  f1  function')
def  f2():
	try:
		print('f2  function')
		return
		print('Hello')
	finally:
		print("f2's  finally")
	print('End  of  f2  function')
def  f3():
	try:
		print('f3  function')
		raise   KeyError(25)
		print('Hello')
	except KeyError as  msg:
		print('Caught  by  f3  function :  ' , msg)
	finally:
		print("f3's  finally")
	print('End of f3 function')
def  f4():
	try:
		print('f4 function')
		exit()
	finally:
		print("f4's  finally")
	print('End of f4 function')
# End  of  all  the  functions
try:
	print('Begin')
	f1()
	print('Hello')
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)
f2()
f3()
try:
	f4()
finally:
		print('Outside  finally')
print('End  of  the  program')


# Find  outputs  (Home  work)
import sys
def  f1():
	try:
		print('f1  function')
		raise  ValueError('Hyd')
		print('Hi')
	finally:
		print("f1's  finally")
	print('End  of  f1  function')
def  f2():
	try:
		print('f2  function')
		return
		print('Hello')
	finally:
		print("f2's  finally")
	print('End  of  f2  function')
def  f3():
	try:
		print('f3  function')
		raise   KeyError(25)
		print('Hello')
	except  KeyError  as  msg:
		print('Caught  by  f3  function : ' , msg)
	finally:
		print("f3's  finally")
	print('End  of  f3  function')
def  f4():
	try:
		print("f4  function")
		sys . exit()
	finally:
		print("f4's  finally")
	print('End  of  f4  function')
#End  of  all  the  functions
try:
	print('Begin')
	f1()
	f2()
	f3()
	f4()
	print('Hello')
except  ValueError  as  msg:
	print('ValueError  is  caught  outside :  ' , msg)
print('End  of  the  program')


# Find  outputs (Home  work)
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')
		raise  Exception()
	except:
		print('Sec')
	finally:
		print("f1's  finally")
	print('End  of  f1  function')
#End  of  the  function
try:
	print('Begin')
	f1()
	print('Hello')
except  ValueError:
	print('Hello')
except  Exception:
	print('Recaught  Exception')
finally:
	print('Outside  finally')
print('End  of  the  program')


# Find outputs (Home  work)
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')
		raise  NameError()
	except  NameError:
		print('Sec')
	finally:
		print('f1 finally')
	print('End  of  f1 function')
#outside function
try:
	print('Begin')
	f1()
	print('Hello')
except ValueError:
	print('Hello')
except   Exception:
	print('Recaught  Exception')
except  NameError:
	print('Caught  Name Error  outside')
finally:
	print('Outside  finally')
print('End of the program')


# Find  outputs  (Home   work)
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')
		raise   NameError()
	except  NameError:
		print('Sec')
	finally:
		print('f1 finally')
	print('End  of  f1 function')
#outside function
try:
	print('Begin')
	f1()
	print('Hello')
except  ValueError:
	print('Hello')
except   KeyError:
	print('Recaught  KeyError')
finally:
	print('Outside  finally')
print('End of the program')


# Find  outputs  (Home   work)
def  f1():
	try:
		print('f1  function')
		raise  KeyError()
		print('Hyd')
	except  KeyError:
		print('Caught  KeyError')
		raise   NameError()
	except  NameError:
		print('Sec')
	finally:
		print('f1 finally')
	print('End  of  f1 function')
#outside function
try:
	print('Begin')
	f1()
	print('Hello')
except  ValueError:
	print('Hello')
except   KeyError:
	print('Recaught  KeyError')
finally:
	print('Outside  finally')
print('End of the program')


# Find  outputs  (Home  work)
try:
	print('try')
	print(7 / 0)
except:
	print('except')
else:
	print('else')
finally:
	print('finally')
print('End')


# Find  outputs  (Home  work)
try:
	print('try')
	print(7 / 0)
except:
	print('except')
else:
	print('else')
finally:
	print('finally')
print('End')


# Find  outputs  (Home  work)
try:
	print('try')
except:
	print('except')
else:
	print('else')
finally:
	print('finally')
print('End')


# Find  outputs  (Home  work)
try:
	print('try')
except:
	print('except')
else:
	print('else')
finally:
	print('finally')
print('End')


# Find  outputs   (Home  work)
try:
	print('try')
else:
    print('else')
finally:
    print('finally')
print('End')


# Find  outputs   (Home  work)
try:
	print('try')
except:
	print('except')
else:
	print('else1')
else:
	print('else2')
finally:
	print('finally')
print('end')


# Identify  error   (Home  work)
try:
	print('try')
else:
	print('else')
except:
	print('except')
finally:
	print('finally')
print('end')


# Find  outputs   (Home  work)
try:
	print('try')
except:
	print('except')
if   10 > 20:
	print('if')
else:
	print('else')
	

# Find  outputs
def   f1():
	try:
		return  10 + '20'
	except:
		return  10 + 20
print(f1())



# Find  outputs
def   f1():
	try:
		return  10
	except:
		return  20
	else:
		return  30
print(f1())


# Find  outputs
def   f1():
	try:
		return  10 + '20'
	except:
		return  20
	else:
		return  30
print(f1())


# Find  outputs
def   f1():
	try:
		pass
	except:
		return  20
	else:
		return  30
print(f1())


# Find  outputs
def   f1():
	try:
		return  10
	except:
		return   20
	else:
		return  30
	finally:
		return  40
print(f1())


'''  (Home  work)
1) What  is  the  output  if  input  is  24 ?  --->

2) What  is  the  output  if  input  is  25 ?  --->
'''
try:
	x = eval(input('Enter  any  number  :  '))
	assert    x >= 25 ,  'Hyd'
	print('Sec')
except  AssertionError  as   msg:
	print(msg)
print('End')


''' (Home  work)
1) What  is  the  output  when  input  is  24 ?  --->

2) What  is  the  output  when  input  is  25 ?  --->
'''
try:
	x = eval(input('Enter  any  number  :  '))
	assert   x >= 25
	print('Sec')
except  AssertionError   as    msg:
	print(msg)
print('End')


# Find  outputs   (Home  work)
try:
	print('Outer   try')
	try:
		print('Inner    try')
		print(7 / 0)
		int('Hyd')
		'Hyd'[5]
		eval('Hyd')
	except   ZeroDivisionError:
		print('ZDE   of   inner   try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try')
	finally:
		print('Inner  try  finally')
	print('End  of  inner  try')
except   ValueError:
	print('ValueError  of  outer  try')
except   IndexError:
	print('IndexError  of  outer  try')
except:
	print('default  except  of  outer  try')
finally:
	print('Outer  try  finally')
print('End  of  outer  try')


#  Find outputs   (Home  work)
try:
	print('Outer  try')
	try:
		print('Inner  try')
		int('Hyd')
		'Hyd'[5]
		eval('Hyd')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try ')
	finally:
		print('Inner  try  finally')
	print('End  of  inner  try')
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
except:
	print('default except of outer try')
finally:
	print('Outer try finally')
print('End of outer try')


#  Find  outputs (Home  work)
try:
	print('Outer  try')
	try:
		print('Inner  try')
		eval('Hyd')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')
	finally:
		print('Inner  try  finally')
	print('End of inner try')
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
except:
	print('default  except  of  outer  try')
finally:
	print('Outer  try  finally')
print('End  of  outer  try')


#  Find  outputs (Home  work)
try:
	print('Outer  try')
	try:
		print('Inner  try')
		print(10 + '20')
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')
	finally:
		print('Inner  try  finally')
	print('End of inner try')
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
finally:
	print('Outer  try  finally')
print('End  of  outer  try')


# Find  outputs   (Home  work)
class   MyError(BaseException):
	def    __init__(self , y):
		self . a = y
		print('Constructor')
# End of  the class
def  compute(x):
	print(x)
	if  x > 20:
		raise   MyError(x)
	print('Hello')
# End of  the functrion
try:
	compute(10)
	compute(30)
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ' ,  msg)
print('End')


# Find  outputs   (Home  work)
class   MyError(NameError):
	def    __init__(self):
		self . a =  25
		print('Constructor')
# End of  the class
def  compute(x):
	print(x)
	if  x > 20:
		raise   MyError()
	print('Hello')
#end of  the functrion
try:
	compute(30)
	compute(10)
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ' ,  msg)
print('End')


# Find  outputs   (Home  work)
class   MyError(NameError):
	def    __init__(self):
		self . a =  25
		print('Constructor')
# End of  the class
def  compute(x):
	print(x)
	if  x > 20:
		raise   MyError()
	print('Hello')
#end of  the functrion
try:
	compute(30)
	compute(10)
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ' ,  msg)
print('End')


# Find  outputs (Home  work)
try:
	print(1)
	print(2)
	print(3)
except:
	print(4)
else:
	print(5)
finally:
	print(6)
print(7)


# Find  outputs   (Home  work)
try:
	print(1)
	print(7 / 0)
	print(3)
except:
	print(4)
else:
	print(5)
finally:
	print(6)
print(7)


