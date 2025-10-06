# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()	# a,b,c,d  refer  to  same  object
print(sys . getrefcount(b)) # 5   4  references  + 1  reference  for  getrefcount()  argument self
print(sys . getrefcount(352))	# cannot be determined for immutable objects
print(sys . getrefcount([10 , 20 , 15 , 18])) 	# 1  as self  is  the  only  reference
print(sys . getrefcount(10.8)) # cannot be determined for immutable objects
print(sys . getrefcount({10 , 20 , 15 , 18})) # 1  as self  is  the  only  reference
print(sys . getrefcount('Hyd')) # cannot be determined for immutable objects
print(sys . getrefcount({10 : 20 , 30 : 40})) # 1  as self  is  the  only  reference
print(sys . getrefcount((10 , 20 , 30 , 40)))	# cannot be determined for immutable objects

# Find  outputs  (Home  work)
import  sys
class  Test:
	def  _init_(self):
		print('Constructor  :  ' , id(self))	# print  id
		return    None #  return  None to constructor call
	def  _del_(self):
		print('Destructor  :  ' , id(self)) # print  id
		return  25	#  return  25 to destructor call
# End  of  the  class
t = Test()	# Object  creation
print(t . _init_())	# explicit  call  to  constructor and none is printed
print(sys . getrefcount(t)) #  reference  count is 2 
print(t . _del_())	# explicit  call  to  destructor and 25 is printed
print(sys . getrefcount(t)) #  reference  count is 2 as for explicit call the object is not deleted
print('Bye')	 # Bye  is  printed

#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):	
		print('Object  is    created')	# prints Object  is    created
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
	print('Function  Begin') 	# prints Function  Begin
	a  =  c1() 	# object  creation and calls  _init_ method
	print(a) 	# prints object  address
	print('Function  end')	# prints Function  end
	return   a # returns  object  to  function  call
print('Program  Begin')
b = f1()	# function  call
print(b)	# prints  object  address
# deletes  the  object  and  calls  destructor method

#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created') # prints Object  is    created
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1()	# Object  is    created and  constructor is  called
        print('Function  end') # prints Function  end
        return   a  # returns  the  object  reference
print('Program  Begin')	# prints Program  Begin
f1() # prints Function  begin, Object  is    created, Function  end, Object  is  lost#
print('Program  End') # prints Program  End
# calls destructor and prints Object  is  lost

#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created') # prints  object  is  created
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin') # prints  function  begin
        a  =  c1()	# creates  object and calls constructor
        print('Function  end') # prints  function  end
		# calls  destructor
print('Program  Begin')  # prints program  begin
f1() # calls  f1
print('Program  End')	# prints  program  end
b = f1() # calls  f1
print(b) # prints  none
print('Program  End') # prints  program  end


# Most  tricky  program
# Circular  reference (Home  work)
class   c1:
	def   __init__(self , k):
		print('c1  class  object  is  created')	# prints c1  class  object  is  created
		self . b = k # adds the instance variable b to class c1 with value k 
		print('End  of  c1  class constructor')	# prints End  of  c1  class constructor
	def   __del__(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  __init__(self):
		print('c2  class  object  is  created')	# prints c2  class  object  is  created
		self . a = c1(self) # creates  object  of  class  c1 and calls  their  constructors
		print('End  of  c2  class constructor') 	# prints End  of  c2  class constructor
	def  __del__(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin') 	# prints Program  begin
x = c2() 			# creates  object  of  class  c2 and calls  their  constructors
print('program end')	# prints program end
# c2 class  object  is  lost as it is 1st created
# c1 class  object  is  lost as it is 2nd created

'''
Program  begin
c2  class  object  is  created
c1  class  object  is  created
End  of  c1  class constructor
End  of  c2  class constructor
program end
c2  class  object  is  lost
c1  class  object  is  lost
'''

#  Lucky  object
# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
		print('Destructor')	# Destructor is printed
		global  b # treats b as global varaible 
		b = self # Assign  self i.e a to  b
a = c1()	# Create  object 
del  a	#  Delete  object and call destructor
print('Hello')	# Hello is printed

