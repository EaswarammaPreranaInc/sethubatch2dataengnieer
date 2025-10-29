#Find  outputs  
try:
	raise  ArithmeticError
except   ZeroDivisionError:
	print('Zero Division  Error')
except   ArithmeticError: # child error except suite is not executed when parent error is raise
	print('Arithmetic Error')
print('End')
'''
o/p:
Arithmetic Error
End
'''


#Find outputs 
def  f1():
	try:
		print('f1  function')
		raise  ValueError('Hyd') # exception is raised
		print('Hi') # skipped
	finally:
		print("f1's  finally")
	print('End  of  f1  function') # skipped
def  f2():
	try:
		print('f2  function')
		return # control goes out of the function
		print('Hello') # skipped
	finally:
		print("f2's  finally")
	print('End  of  f2  function') # skipped 
def  f3():
	try:
		print('f3  function')
		raise   KeyError(25) # raises exception
		print('Hello') # skipped
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
		print("f4's  finally") # before exit() terminates the program finally block is executed
	print('End of f4 function')
# End  of  all  the  functions
try:
	print('Begin')
	f1()
	print('Hello')
except  ValueError  as  msg:
	print('ValueError is caught outside :  ' , msg)
f2()
f3()
try:
	f4()
finally:
		print('Outside finally')
print('End of the program')
'''
o/p:
Begin
f1  function
f1's  finally
ValueError is caught outside : Hyd
f2  function
f2's  finally
f3  function
Caught  by  f3  function : 25
f3's  finally
End of f3 function
f4 function
f4's  finally
Outside finally
'''


#Find  outputs  
import sys
def  f1():
	try:
		print('f1  function')
		raise  ValueError('Hyd') # raises exception
		print('Hi') # skipped
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
'''
o/p:
Begin
f1  function
f1's  finally
ValueError  is  caught  outside :   Hyd
End  of  the  program
'''


#Find  outputs 
def  f1():
	try:
		print('f1  function')
		raise  KeyError() # raises keyerror
		print('Hyd') # skipped
	except  KeyError:
		print('Caught  KeyError')
		raise  Exception()
	except:
		print('Sec')
	finally:
		print("f1's  finally") # executes finally
	print('End  of  f1  function')
#End  of  the  function
try:
	print('Begin')
	f1()
	print('Hello') # skipped
except  ValueError:
	print('Hello')
except  Exception:
	print('Recaught  Exception')
finally:
	print('Outside  finally')
print('End  of  the  program')
'''
o/p:
Begin
f1  function
Caught  KeyError
f1's  finally
Recaught  Exception
Outside  finally
End  of  the  program
'''


#Find outputs 
def  f1():
	try:
		print('f1  function')
		raise  KeyError() # raises Keyerror
		print('Hyd') # skipped
	except  KeyError:
		print('Caught  KeyError')
		raise  NameError() # raises Nameerror
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
'''
o/p:
Begin
f1  function
Caught  KeyError
f1 finally
Recaught  Exception
Outside  finally
End of the program
'''


#Find  outputs  
def  f1():
	try:
		print('f1  function')
		raise  KeyError() # raises keyerror
		print('Hyd') # skipped
	except  KeyError:
		print('Caught  KeyError')
		#raise   NameError() # error : because NameError is no handled in any of the corresponding except suite in outer try
	except  NameError:
		print('Sec')
	finally:
		print('f1 finally') # executes finally
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



#Find  outputs  
try:
	print('try')
	print(7/0)
except:
	print('except')
else:
	print('else')
finally:
	print('finally')
print('End')
'''
o/p:
try
except
finally
End
'''


#Find outputs 
try:
	print('try')
except:
	print('except')
else:
	print('else')
finally:
	print('finally')
print('End')
'''
o/p:
try
else
finally
End
'''

'''
#Find outputs 
try:
	print('try')
#else: # error : cannot write else without except suite
    print('else')
finally:
    print('finally')
print('End')
'''


# Find  outputs   
try:
	print('try')
except:
	print('except')
else:
	print('else1')
#else: # error cannot write more then one else
	print('else2')
finally:
	print('finally')
print('end')



# Identify  error   
try:
	print('try')
#else: # else before except is not allowed
	print('else')
except:
	print('except')
finally:
	print('finally')
print('end')


#Find outputs   
try:
	print('try')
except:
	print('except')
if   10 > 20:
	print('if')
else:
	print('else')
'''
try
else
'''


# Find  outputs
def   f1():
	try:
		return  10+'20' # error so, except suite is executed
	except:
		return  10+20 # 30
print(f1())



# Find  outputs
def   f1():
	try:
		return  10 # as return statement is executed else block is not executed 
	except:
		return  20
	else:
		return  30
print(f1()) # 10


#Find  outputs
def   f1():
	try:
		return  10+'20'
	except:
		return  20 # 20 : as error is raised except suite is executed
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
		return  30 # no error is raised in try suite . so, else block is executed
print(f1()) # 30

# Find  outputs
def   f1():
	try:
		return  10
	except:
		return   20
	else:
		return  30
	finally:
		return  40 # finally block is executed and it returns 40
print(f1()) # 40 



