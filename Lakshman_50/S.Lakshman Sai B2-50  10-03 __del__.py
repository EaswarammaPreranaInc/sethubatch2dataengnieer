
#================================================== # Find  outputs

import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b))      # 5
print(sys . getrefcount(c1()))      #1
print(sys . getrefcount(352))    #3    it gives how many '352' present in entire cwd
print(sys . getrefcount([10 , 20 , 15 , 18]))      #1
print(sys . getrefcount(10.8))      #3
print(sys . getrefcount({10 , 20 , 15 , 18}))      #1
print(sys . getrefcount('Hyd'))     #3
print(sys . getrefcount((10 , 20 , 30 , 40)))      #1
print(sys . getrefcount({10 : 20 , 30 : 40}))      #3

#================================================== # Find  outputs  (Home  work)

import  sys
class  Test:
	def  __init__(self):
		print('Constructor  :  ' , id(self))
		return    None
	def  __del__(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test()
print(t . __init__())
print(sys . getrefcount(t))
print(t . __del__())
print(sys . getrefcount(t))
print('Bye')
'''
Constructor  :   1850464236080
Constructor  :   1850464236080
None
2
Destructor  :   1850464236080
25
2
Bye
Destructor  :   1850464236080
'''
#================================================== #  Tricky  program

# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
	print('Function  Begin')
	a  =  c1()
	print(a)
	print('Function  end')
	return   a
print('Program  Begin')
b = f1()
print(b)
print('Program  End')
'''
Program  Begin
Function  Begin
Object  is    created
<__main__.c1 object at 0x000002B2E7997230>
Function  end
<__main__.c1 object at 0x000002B2E7997230>
Program  End
Object  is  lost
'''
#================================================== #  Tricky  program

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
#================================================== #  Tricky  program

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
#================================================== # Most  tricky  program

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
c2  class  object  is  lost
c1  class  object  is  lost
'''

#================================================== #  Lucky  object

# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
		print('Destructor')
		global  b
		b = self
a = c1()
del  a
print('Hello')
'''
Destructor
Hello
'''