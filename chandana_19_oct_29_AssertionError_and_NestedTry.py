''' 
1) What  is  the  output  if  input  is  24 ?  --->Hyd <nextline> End

2) What  is  the  output  if  input  is  25 ?  --->Sec <nextline> End
'''
try:
	x = eval(input('Enter  any  number  :  '))
	assert  x >= 25 ,'Hyd' # when condition is false AssertionError is raised with the message
	print('Sec')
except  AssertionError  as   msg:
	print(msg)
print('End')


''' 
1) What  is  the  output  when  input  is  24 ?  --->empty string <nextline> End

2) What  is  the  output  when  input  is  25 ?  ---> sec <next line> End
'''
try:
	x = eval(input('Enter  any  number  :  '))
	assert   x >= 25 # msg is empty string
	print('Sec')
except  AssertionError   as    msg:
	print(msg)
print('End')



# Find  outputs   
try:
	print('Outer try')
	try:
		print('Inner try')
		print(7/0) # ZeroDivision error is raised
		int('Hyd') # skipped
		'Hyd'[5] # skipped
		eval('Hyd') # skipped
	except   ZeroDivisionError:
		print('ZDE of inner try')
		int('Ten')
	except  ValueError:
		print('ValueError  of  inner  try')
	finally:
		print('Inner  try  finally')
	print('End  of  inner  try')
except   ValueError:
	print('ValueError of outer try')
except   IndexError:
	print('IndexError of outer try')
except:
	print('default  except  of  outer  try')
finally:
	print('Outer  try  finally')
print('End  of  outer  try')
'''
o/p:
Outer try
Inner try
ZDE of inner try
Inner  try  finally
ValueError of outer try
Outer  try  finally
End  of  outer  try
'''


#  Find outputs  
try:
	print('Outer  try')
	try:
		print('Inner  try')
		int('Hyd') # valueError is raise
		'Hyd'[5] # skipped
		eval('Hyd') # skipped
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
'''
Outer  try
Inner  try
ValueError  of  inner  try
Inner  try  finally
End  of  inner  try
Outer try finally
End of outer try
'''


#Find outputs  
try:
	print('Outer try')
	try:
		print('Inner try')
		'Hyd'[3] # indexerror is raised
		eval('Hyd') # skipped
	except  ZeroDivisionError:
		print('ZDE of inner try')
		int('Ten')
	except  ValueError:
		print('ValueError of inner try ')
	finally:
		print('Inner try finally')
	print('End of inner try')
except  ValueError:
	print('ValueError of outer try')
except  IndexError: # as their is no indexerror in the corresponding except suite of inner try . The outer except is executed
	print('IndexError of outer try')
except:
	print('default except of outer try')
finally:
	print('Outer try finally')
print('End  of  outer  try')
'''
o/p:
Outer try
Inner try
Inner try finally
IndexError of outer try
Outer try finally
End  of  outer  try
'''


#  Find  outputs
try:
	print('Outer try')
	try:
		print('Inner try')
		eval('Hyd') # NameError is raised
	except  ZeroDivisionError:
		print('ZDE  of  inner  try')
		int('Ten')
	except ValueError:
		print('ValueError  of   inner  try ')
	finally:
		print('Inner  try  finally')
	print('End of inner try')
except  ValueError:
	print('ValueError of outer try')
except  IndexError:
	print('IndexError of outer try')
except: # default except suite is executed
	print('default except of outer  try')
finally:
	print('Outer  try  finally')
print('End  of  outer  try')
'''
o/p:
Outer try
Inner try
Inner  try  finally
default except of outer  try
Outer  try  finally
End  of  outer  try
'''

'''
#  Find  outputs 
try:
	print('Outer try')
	try:
		print('Inner try')
		print(10+'20') # TypeError is raised and it is not handled in the corresponding except suite of inner try nor outer try . so error is reported
	except  ZeroDivisionError:
		print('ZDE of inner try')
		int('Ten')
	except ValueError:
		print('ValueError of inner try ')
	finally:
		print('Inner  try  finally')
	print('End of inner try')
except  ValueError:
	print('ValueError  of  outer try')
except  IndexError:
	print('IndexError of outer try')
finally:
	print('Outer try finally')
print('End of outer try')
'''


# Find  outputs  
class   MyError(BaseException):
	def    __init__(self,y):
		self.a = y
		print('Constructor')
# End of  the class
def  compute(x):
	print(x)
	if  x > 20:
		raise  MyError(x) # error is raised so __init__ of MyError is executed
	print('Hello')
# End of  the functrion
try:
	compute(10)
	compute(30)
except  MyError  as  msg:
	print('Caught  MyError  outside  :  ',msg)
print('End')
'''
o/p:
10
Hello
30
Constructor
Caught  MyError  outside  :   30
End
'''


# Find  outputs  
class   MyError(NameError):
	def    __init__(self):
		self.a =25
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
except  MyError  as  msg: # msg is empty string
	print('Caught  MyError  outside  :  ',msg)
print('End')
'''
o/p:
30
Constructor
Caught  MyError  outside  :
End
'''


# Find  outputs
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
'''
o/p:
1
2
3
5
6
7
'''


# Find  outputs  
try:
	print(1)
	print(7/0)
	print(3)
except:
	print(4)
else: # it is not executed as there is an exception in try suite
	print(5)
finally:
	print(6)
print(7)
'''
o/p:
1
4
6
7
'''


# Find  outputs   
try:
	print(1)
	print(7/0) # ZeroDivisionError
	print(3)
except:
	pass
	#int('Two') # valueError and it is not handled
else:
    print(5)
finally:
    print(6)
print(7)


