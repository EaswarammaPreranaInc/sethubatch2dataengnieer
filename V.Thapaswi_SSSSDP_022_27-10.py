#Identify  Error  (Home  work)
try:
	print('Hyd')
	print('Sec')
	print('Cyb')
# There is no except suite	or finally


# Find  outputs  (Home  work)
#print(7 / 0)#error :division by zero
try:
	print(7 / 0)
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')
#print(7 / 0)#error:division by zero
print('Bye')#bye
'''
o/p:
Division  by  zero  is  not  permitted
bye
'''





# Identify  error  (Home  work)
except:
        print('Hyd')
        print('Sec')
        print('Cyb')
#There is no try suite



# Find  outputs (Home  work)
try:
        print('One')
        print('Two')
        print('Three')
#print('Four')#error expected except or finaly
except:
		print('Five')
		print('Six')
		print('Seven')
print('Eight')
'''
o/p:
One
Two
Three
Eight
'''


# Find  outputs  (Home work)
try:
	print('try suite')
#except:
	print('default  except')#cannot write default except middle of the program
except NameError:
	print('Name  Error')
'''	
o/p:
try suite
default except    
'''


# Find  outputs  (Home  work)
try:
	print('try suite')#tr suite
except:
	print('1st  default  except')
#except:#error bcz cannot use multiple default execpt suite
	print('2nd  default  except')
	


#  Which  of  the  following  statements  raise  ZeroDivisionError ?
print(7 / 0)#ZeroDivisionError
print(7 / 0.0)#ZeroDivisionError
print(0 / 0)#ZeroDivisionError
print(0.0 / 0.0)#ZeroDivisionError
print(7 // 0)#ZeroDivisionError
print(7 % 0)#ZeroDivisionError






#  Which  of  the  following  statements  raise  ValueError ?  (Home  work)
import  math
#print(int('10.8'))#ValueError
#print(float('Ten'))#ValueError
#print(complex('True'))#ValueError
print(bool('Ten'))#True bcz non empty
print(bool(''))#False
print(float('10.8'))#10.8
print(float('25'))#25.0
print(int(10.8))#10
print(math . sqrt(-25))#ValueError



#When  is  ValueError  raised  ?  --->  When   a  function  (or)  method  does  not  return  any  result i.e. not  even  None







# Which  of  the  following  statements  raise  NameError ?
a = 25
print(a)#25
del  a#object is deleted
print(a)#Nameerror 
print(eval("   'Ten'   "))#'Ten'
print(eval('Ten'))#NameError



#When  is  NameError  raised ?  --->  When  a  non-existing  object  is  being  used




# Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0])#H
print('Hyd'[1])#y
print('Hyd'[2])#d
print('Hyd'[3])#IndexError
list = [10 , 20 , 15 , 18]
print(list[0])#10
print(list[3])#18
print(list[4])#IndexError
print(list[-1])#18
print(list[-4])#10
print(list[-5])#IndexError
tpl = (10 , 20 , 30)
print(tpl[3])#IndexError
r = range(10)
print(r[10])#IndexError
s = {10 , 20 , 15 , 18}
print(s[4])#IndexError
d = {10 : 'Hyd' , 20 : 'Sec'}
print(d[0])#IndexError bcz there is no indexies in dictionary



#When  is  IndexError  raised  ?  --->  When  a  non-existing  index  is  being  used







#  Which  of  the  following  statements  raise TypeError ?
print(10 + 20)#30
print('10' + '20')#1020
print(10 + '20')#TypeError
print(len('25'))#TypeError
print(len(25))#TypeError
s = {10 , 20 , 15 , 18}
print(s[0])#TypeError
b = { [10 , 20] : [30 , 40] }#TypeError: cannot use list as a dictionary
print(int(3 + 4j))#TypeError
print(int([10 , 20 , 30]))#TypeError
print(float(None))#TypeError







# Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G'])#Green
print(a['Y'])#KeyError

'''
When  is  KeyError  raised  ?  ---> When  the  dictionary  key  is  invalid
'''




# Find  outputs  (Home  work)
try:
	print(7 / 0)#except suite is executed
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')#ZDE 1
except    ZeroDivisionError:
	print('ZDE  2')#skipped
print('Bye')#Bye






# Find  outputs  (Home  work)
try:
	#print(7 / 0)#error 
	print('Hello')#Hello
except    ZeroDivisionError:
	print('ZDE  1')
	#print(8 / 0)#error
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye')#Bye




# Find  outputs
try:
	print(7 / 0)#raises a ZeroDivisionError
	print('Hello')#skipped
except  ZeroDivisionError:#except suite is executed bcz it catch that handle
	print('ZDE  1')#ZDE 1
	try:
		print(8 / 0)
	except  ZeroDivisionError:
		print('ZDE   2')#ZDE 2
	print('Bye')#Bye
except  ZeroDivisionError:
	print('ZDE  3')
print('End')#End





#Find  outputs  (Home  work)

#Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError

try:
	print(7 / 0)
except   ArithmeticError:
	print('Arithmetic Error')#Arithmetic Error
except   ZeroDivisionError:#when we got ZeroDivisonError raised ArithmeticError raised bcz its parent class
	print('Zero Division  Error')
print('End')#End






# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')#f1 function
		print(7 / 0)#error raised ZeroDisionError
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
	print('Hi')#Hi
except  ZeroDivisionError:
	print('ZDE  is  caught  outside')#ZDE  is  caught  outside
except:
	print('Bye')
print('End')#End


'''
o/p:
Begin
f1  function
ZDE  is  caught  outside
End
'''


# Find  outputs  (Home  work)
def  f1():
	try:
		print('f1  function')#f1 function
		print(7 / 0)#ZeroDivisionError raised
	except  ValueError:#skiped
		print('Hello')
	except  ZeroDivisionError:
		print('ZDE  is  caught  by  f1  function')#ZDE  is  caught  by  f1  function
	print('End  of  f1  function')#End of f1 function
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





'''

What  are   the  outputs  if  input  is  1 ?  --->

What  are   the  outputs  if  input  is  2 ?  --->

What  are   the  outputs  if  input  is  3 ?  --->

What  are   the  outputs  if  input  is  4 ?  --->

What  are   the  outputs  if  input  is  5 ?  --->

What  are   the  outputs  if  input  is  6 ?  --->

What  are   the  outputs  if  input  is  7 ?  --->

What  are   the  outputs  if  input  is  8 ?  --->
'''
while  True:
	ch = eval(input('Enter  choice (9-exit) : '))
	try:
		match  ch:
			case  1:
				list = [10 , 20 , 15 , 12 , 18]
				print(list[5])#IndexError
			case  2:
				s = 'Hyd'
				print(s[3])#IndexError
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
				print(d[18])#KeyError
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
print('bye')

'''
o/p:
Invalid index
Invalid index
No result
Invalid   argument (or)  operand
Object  does  not  exist
Div by 0 is not allowed
Invalid   argument (or)  operand
Invalid dict key

'''



#  Find  outputs
def  f1():
	print('f1  function')#f1 function
	raise   ValueError('Hyd')
	print('Sec')
# End of  the  function
#f1()#error
try:
	print('Begin')
	f1()
	print('Bye')
except  ValueError  as  msg:
	print('Caught  ValueError  outside  the  function  :  ' , msg)
#f1()#error
print('End of the program')
'''
o/p:
Begin
f1  function
Caught  ValueError  outside  the  function  :   Hyd
End of the program
'''



#Find  outputs  (Home  work)
def  f1(a):
	print('f1  function')#f1 function
	if   a == 20:
		raise  ArithmeticError()
	elif   a == 0:
		raise  IndexError()
	elif  a == 10:
		raise  TypeError(25)
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
print('End')

'''
o/p:
Begin
f1  function
Caught  TypeError  outside  the  function :   25
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
f1(10)#
f1(20)
f1(30)
f1(0)
print('End of the program')
'''
o/p:
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
print('End of the program')

'''
o/P:
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
o/p:
Begin
f1 function
Caught  by  f1 function  :  25
Recaught ValueError  :   25
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
o/P:
Begin
f1 function
Caught  by  f1 function  :   25
Some other error
End of the program
'''