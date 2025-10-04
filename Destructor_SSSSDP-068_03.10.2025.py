# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()  #  creates 4 objects of c1 class
print(sys . getrefcount(b))  #  5
print(sys . getrefcount(c1()))  #  1
print(sys . getrefcount(352))  #  # cannot be predicted as it is immutable
print(sys . getrefcount([10 , 20 , 15 , 18]))  #  1
print(sys . getrefcount(10.8))  #  # cannot be predicted as it is immutable
print(sys . getrefcount({10 , 20 , 15 , 18}))  #  1
print(sys . getrefcount('Hyd'))  # cannot be predicted as it is immutable
print(sys . getrefcount({10 : 20 , 30 : 40}))  #  1
print(sys . getrefcount((10 , 20 , 30 , 40)))  # cannot be predicted as it is immutable


# Find  outputs  (Home  work)
import  sys
class  Test:
	def  __init__(self):
		print('Constructor  :  ' , id(self))
		return    None
	def  __del__(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test()  #  object a is created ,Constructor is executed
print(t . __init__())  #  Constructor is executed , return None
print(sys . getrefcount(t))  #  2
print(t . __del__())  #  Destructor is excuted and return 25
print(sys . getrefcount(t))   #  2
print('Bye')  #  Bye
#  Destructor is excuted before pregram terminates



#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')  
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
	print('Function  Begin')  #   Function Begin
	a  =  c1()  #  object a is craeted and Constructor is executed
	print(a)  #  type and address
	print('Function  end')  #  function end
	return   a  
print('Program  Begin')  #  Program Begin
b = f1()  
print(b)  #  name and address of class
print('Program  End')  #  Program end
# Destructor is executed
'''
Program  Begin
Function  Begin
Object  is    created
type and address
Function  end
Type an address
Program  End
Object  is  lost
'''


#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1()
        print('Function  end')
        return   a
print('Program  Begin')
f1()
print('Program  End')

'''
Program  Begin
Function  begin
Object  is    created
Function  end
Object  is  lost
Program  End
'''


#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1()
        print('Function  end')
print('Program  Begin')
b = f1()
print(b)
print('Program  End')

'''
Program  Begin
Function  begin
Object  is    created
Function  end
Object  is  lost
None
Program  End
'''


# Most  tricky  program
# Circular  reference (Home  work)
class   c1:
	def   __init__(self , k):
		print('c1  class  object  is  created')
		self . b = k
		print('End  of  c1  class constructor')
	def   __del__(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  __init__(self):
		print('c2  class  object  is  created')
		self . a = c1(self)
		print('End  of  c2  class constructor')
	def  __del__(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin')
x = c2()
print('program end')

'''
Program  begin
c2  class  object  is  created
c1  class  object  is  created
End  of  c1  class constructor
End  of  c2  class constructor
program end
c1  class  object  is  lost
c2  class  object  is  lost
'''


#  Lucky  object
# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
		print('Destructor')
		global  b
		b = self
a = c1()  # object a is creayed
del  a  #  Destructor is executed and object a is deleted
print('Hello')  #  Hello
