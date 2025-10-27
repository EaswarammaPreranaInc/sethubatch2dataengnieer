#Identify  Error  
'''
try: # error : try should be paired with except or finally or both
	print('Hyd')
	print('Sec')
	print('Cyb')
'''



# Find  outputs  
#print(7/0) # ZeroDivision error
try:
	print(7/0) # error so except suite is executed
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')
#print(7/0) # zeroDivisionError
print('Bye')



#Identify error  
'''
except: # error becaues cannot write except without try
        print('Hyd')
        print('Sec')
        print('Cyb')
'''


# Find  outputs 
try:
        print('One')
        print('Two')
        print('Three')
#print('Four') # error : try and except blocks must be directly paired
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


# Find  outputs 
try:
	print('try suite')
#except: #error : cannot be witten in the middle  
	print('default  except')
except NameError:
	print('Name  Error')



# Find  outputs  
try:
	print('try suite')
except:
	print('1st  default  except')
#except: # error : cannot write two except suits
	print('2nd  default  except')
	


#  Which  of  the  following  statements  raise  ZeroDivisionError ?
#print(7/0) # ZeroDivisionError
#print(7/0.0) # ZeroDivisionError
#print(0/0) # ZeroDivisionError
#print(0.0/0.0) # ZeroDivisionError
#print(7//0) # ZeroDivisionError
#print(7%0) # ZeroDivisionError


#  Which  of  the  following  statements  raise  ValueError ?  
import  math
#print(int('10.8')) # ValueError : cannot convert string'10.8' to int
#print(float('Ten')) # ValueError
#print(complex('True')) # ValueError
print(bool('Ten')) # True
print(bool('')) # False
print(float('10.8')) # 10.8
print(float('25')) # 25.0
print(int(10.8)) # 10
#print(math . sqrt(-25)) # ValueError



# Which  of  the  following  statements  raise  NameError ?
a = 25
print(a) # 25
del  a # deletes object a
#print(a) # NameError : non-existing object is being used
#print(eval("   'Ten'   ")) # NameError : there is no object Ten 
#print(eval('Ten')) # NameError


# Which  of  the  following  statements  raise  IndexError ?
print('Hyd'[0]) # H
print('Hyd'[1]) # y
print('Hyd'[2]) # d
#print('Hyd'[3]) # IndexError : non-existing index
list = [10 , 20 , 15 , 18]
print(list[0]) # 10
print(list[3]) # 18
#print(list[4]) # IndexError : index 4 doesn't exist
print(list[-1]) # 18
print(list[-4]) # 10
#print(list[-5]) # IndexError
tpl = (10 , 20 , 30)
#print(tpl[3]) # IndexError
r = range(10)
#print(r[10]) # IndexError
s = {10 , 20 , 15 , 18}
#print(s[4]) # IndexError : set is not indexed
d = {10 : 'Hyd' , 20 : 'Sec'}
#print(d[0]) # KeyError : there is no key 0 in the dict



#  Which  of  the  following  statements  raise TypeError ?
print(10 + 20) # 30
print('10' + '20') # 1020
#print(10 + '20') # TypeError 
print(len('25')) # 2
#print(len(25)) # TypeError : int doesn't have length
s = {10 , 20 , 15 , 18}
#print(s[0]) # TypeError : set is not indexed
#b = { [10 , 20] : [30 , 40] } # TypeError
#print(int(3 + 4j)) # TypeError
#print(int([10 , 20 , 30])) # TypeError
#print(float(None)) # TypeError



# Which  of  the  following  statements  raise  KeyError ?
a = {'R' : 'Red' , 'G' : 'Green' , 'B'  : 'Blue'}
print(a['G']) # Green
#print(a['Y']) # KeyError : invalid key



# Find  outputs 
try:
	print(7/0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE 1')
except    ZeroDivisionError:
	print('ZDE 2')
print('Bye')
'''
o/p:
ZDE 1
Bye
'''


# Find  outputs  
try:
	print(7 / 0)
	print('Hello')
except    ZeroDivisionError:
	print('ZDE  1')
	#print(8 / 0) # ZeroDivisionError
except    ZeroDivisionError:
	print('ZDE  2')
print('Bye')


print()
# Find  outputs
try:
	print(7 / 0)
	print('Hello')
except  ZeroDivisionError:
	print('ZDE 1')
	try:
		print(8 / 0)
	except  ZeroDivisionError:
		print('ZDE 2')
	print('Bye')
except  ZeroDivisionError:
	print('ZDE  3')
print('End')
'''
o/p:
ZDE 1
ZDE 2
Bye
End
'''


'''
Find  outputs  

Hint: ArithemeticError  is  parent  class  to  ZeroDivisionError
'''
try:
	print(7 / 0)
except   ArithmeticError:
	print('Arithmetic Error')
except   ZeroDivisionError:
	print('Zero Division  Error')
print('End') 
'''
o/p:
Arithmetic Error
End
'''


# Find  outputs  
def  f1():
	try:
		print('f1 function')
		print(7/0)
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
	print('ZDE is caught outside')
except:
	print('Bye')
print('End')
'''
o/p:
Begin
f1 function
ZDE is caught outside
End
'''


#Find outputs 
def  f1():
	try:
		print('f1  function')
		print(7/0)
	except  ValueError:
		print('Hello')
	except  ZeroDivisionError:
		print('ZDE is caught by f1 function')
	print('End of f1 function')
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
f1  function
ZDE is caught by f1 function
End of f1 function
Hello
End
'''


'''
What  are   the  outputs  if  input  is  1 ?  ---> Invalid index

What  are   the  outputs  if  input  is  2 ?  ---> Invalid index

What  are   the  outputs  if  input  is  3 ?  ---> No result

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
				print(7/0)
			case  7:
				print(10+'20')
			case   8:
				d = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb'}
				print(d[18])
			case   9:
				break
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


