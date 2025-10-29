# Identify  Error  (Home  work)
try:
	print('Hyd')
	print('Sec')
	print('Cyb')
#error did'nt close this with except

 # Find  outputs  (Home  work)
print(7 / 0)
try:
	print(7 / 0)
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')
print(7 / 0)
print('Bye')
'''
Output:
Division  by  zero  is  not  permitted
Bye'''
# Identify  error  (Home  work)
#except:
        print('Hyd')
        print('Sec')
        print('Cyb')
#there should be try before except suite


# Find  outputs (Home  work)
try:
        print('One')
        print('Two')
        print('Three')
print('Four')#indentation error
except:
		print('Five')
		print('Six')
		print('Seven')
print('Eight')#indentation error


# Find  outputs  (Home work)
try:
	print('try suite')
except:
	print('default  except')
except NameError:
	print('Name  Error')
#cannot write syntax error after a bare error

# Find  outputs  (Home  work)
try:
	print('try suite')
except:
	print('1st  default  except')
except:
	print('2nd  default  except')
	#same as above error


#  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0)   
print(7 / 0.0)
print(0 / 0)
print(0.0 / 0.0)
print(7 // 0)
print(7 % 0)
#All the six statements raise the ZeroDivisionerror

 #  Which  of  the  following  statements  raise  ValueError ?  (Home  work)
import math
print(int('10.8'))#ValueError 
print(float('Ten'))#ValueError 
print(complex('True'))#ValueError 
print(bool('Ten'))         
print(bool(''))             
print(float('10.8'))        
print(float('25'))           
print(int(10.8)) 
print(math.sqrt(-25))# ValueError  



'''
When  is  ValueError  raised  ?  --->  When   a  function  (or)  method  does  not  return  any  result
													       i.e. not  even  None
'''
# Which  of  the  following  statements  raise  NameError ?
a = 25
print(a)
del  a
print(a) #NameError
print(eval("   'Ten'   "))
print(eval('Ten'))#NameError


'''
When  is  NameError  raised ?  --->  When  a  non-existing  object  is  being  used
'''


# Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0])
print('Hyd'[1])
print('Hyd'[2])
print('Hyd'[3])#IndexError
list = [10 , 20 , 15 , 18]
print(list[0])
print(list[3])
print(list[4])#IndexError
print(list[-1])
print(list[-4])
print(list[-5])#IndexError
tpl = (10 , 20 , 30)
print(tpl[3])#IndexError
r = range(10)
print(r[10])  # IndexError
s = {10 , 20 , 15 , 18}
print(s[4])#TypeError
d = {10 : 'Hyd' , 20 : 'Sec'}
print(d[0]) #KeyError 



'''
When  is  IndexError  raised  ?  --->  When  a  non-existing  index  is  being  used
'''
#  Which  of  the  following  statements  raise TypeError ?
print(10 + 20)       
print('10' + '20')  
print(10 + '20')#TypeError
print(len('25'))                   
print(len(25))#TypeError
s = {10 , 20 , 15 , 18}
print(s[0])#TypeError
b = { [10 , 20] : [30 , 40] }#TypeError
print(int(3 + 4j))#TypeError
print(int([10 , 20 , 30]))#TypeError
print(float(None))#TypeError

'''
When  is  TypeError  raised ? ---> When  the  operands  are  illegal  in  an  expression
																			            (or)
													  when  an  illegal  argument  is  passed  to  the  function (or)  method
'''

# Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G'])
print(a['Y'])#KeyError


'''
When  is  KeyError  raised  ?  ---> When  the  dictionary  key  is  invalid
'''

 # Find  outputs  (Home  work)
try:
	print(7 / 0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')
except    ZeroDivisionError:  #duplicate error is not allowed
	print('ZDE  2')
print('Bye')


 # Find  outputs  (Home  work)
try:
	print(7 / 0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')
	print(8 / 0)
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye') 
 
#both the errors areoccured second occurs during the first one
 
 # Find  outputs
try:
	print(7 / 0)             #ZeroDivisionError occurs → jumps to first except block
	print('Hello')           #Skipped because error occurred above
except  ZeroDivisionError:
	print('ZDE  1')          #Output: ZDE  1
	try:
		print(8 / 0)         #ZeroDivisionError again → jumps to inner except
	except  ZeroDivisionError:
		print('ZDE   2')     #Output: ZDE   2
	print('Bye')             #Output: Bye
except  ZeroDivisionError:
	print('ZDE  3')          #Not executed (first except already handled it)
print('End')                 #Output: End

'''
Find  outputs  (Home  work)

Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError
'''
try:
	print(7 / 0)                    #Raises ZeroDivisionError goes to first matching except
except   ArithmeticError:
	print('Arithmetic Error')       #Executed (parent of ZeroDivisionError)
except   ZeroDivisionError:
	print('Zero Division  Error')   #Skipped (already handled by parent class)
print('End')                        #Executed after exception handling
'''
Output:
Arithmetic Error
End
'''


# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')           #Output: f1  function
		print(7 / 0)                   #Raises ZeroDivisionError → not caught by ValueError except
	except  ValueError:
		print('Hello')                 #Skipped (different error type)
	try:
		print(int('Ten'))              #ValueError (not ZeroDivisionError) → goes to next except
	except ZeroDivisionError:
		print('Bye')                   #Skipped (error is ValueError)
	print('End  of  f1  function')     #Not executed because ValueError from int('Ten') not caught
# End of f1  function
try:
	print('Begin')                     #Output: Begin
	f1()                               #Raises ZeroDivisionError inside f1() → handled by outer try
	print('Hi')                        #Skipped because control goes to except
except  ZeroDivisionError:
	print('ZDE  is  caught  outside')  #Output: ZDE  is  caught  outside
except:
	print('Bye')                       #Skipped (first except already matched)
print('End')                           #Output: End
'''
Output:
Begin
f1  function
ZDE  is  caught  outside
End
'''

 # Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')                 #  Output: f1  function
		print(7 / 0)                         # Raises ZeroDivisionError → goes to corresponding except
	except  ValueError:
		print('Hello')                       # Skipped (not a ValueError)
	except  ZeroDivisionError:
		print('ZDE  is  caught  by  f1  function')   # Output: ZDE  is  caught  by  f1  function
	print('End  of  f1  function')           #Output: End  of  f1  function
# End  of  the  function
try:
	print('Begin')                           # Output: Begin
	f1()                                     # Executes successfully (error handled inside f1)
	print('Hello')                           # Output: Hello
except  ZeroDivisionError:
	print("Hi")                              #Not executed (no unhandled ZeroDivisionError)
except  ValueError:
	print("Bye")                             #Not executed
print('End')                                 #Output: End



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
'''
What  are   the  outputs  if  input  is  1 ?  ---> Enter choice (9-exit) : 1  Invalid  index

What  are   the  outputs  if  input  is  2 ?  ---> Enter choice (9-exit) : 2  Invalid  index

What  are   the  outputs  if  input  is  3 ?  ---> Enter choice (9-exit) : 3  No  result

What  are   the  outputs  if  input  is  4 ?  ---> Enter choice (9-exit) : 4  Invalid   argument (or)  operand

What  are   the  outputs  if  input  is  5 ?  ---> Enter choice (9-exit) : 5  Object  does  not  exist

What  are   the  outputs  if  input  is  6 ?  ---> Enter choice (9-exit) : 6  Div by 0 is not allowed

What  are   the  outputs  if  input  is  7 ?  ---> Enter choice (9-exit) : 7  Invalid   argument (or)  operand

What  are   the  outputs  if  input  is  8 ?  ---> Enter choice (9-exit) : 8  Invalid dict key
'''

#  Find  outputs
def  f1():
	print('f1  function')
	raise   ValueError('Hyd')  #raises valueerror
	print('Sec')               #Not excecuted
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
Output: 
Begin
f1  function
Caught  TypeError  outside  the  function :  25
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
print('End of the program')
'''Output: 
Caught  ValueError  :  25
End  of  f1  function
Caught   NameError  :  10.8
End  of  f1  function
Caught  IndexError  :  Hyd
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
print('End of the program')
'''
Begin
f1 function
Caught  by  f1 function  :  25
Recaught  by  f1 function  :  25
End  of  f1  function
Hyd
End of the program
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
print('End of the program')
'''
Begin
f1 function
Caught  by  f1 function  :  25
Recaught ValueError  :  25
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
Output: 
Begin
f1 function
Caught  by  f1 function  :  25
Some other error
End of the program
'''

#  Find  outputs  (Home  work)
try:
	raise  ArithmeticError
except   ZeroDivisionError:
	print('Zero Division  Error')
except   ArithmeticError:
	print('Arithmetic Error')
print('End')


'''
Is  child  error  except  suite  executed  when  parent  error   raised ?  ---> No the child error does not excecute
'''