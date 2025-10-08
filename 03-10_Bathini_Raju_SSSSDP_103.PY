# BATHINI RAJU SSSSDP 103
# 03-10-2025
# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b)) #5
print(sys . getrefcount(c1())) #2
print(sys . getrefcount(352)) #May be 2 or more as it is reusable
print(sys . getrefcount([10 , 20 , 15 , 18])) #2
print(sys . getrefcount(10.8)) #May be 2 or more as it is reusable
print(sys . getrefcount({10 , 20 , 15 , 18})) #2
print(sys . getrefcount('Hyd')) #May be 2 or more as it is reusable
print(sys . getrefcount({10 : 20 , 30 : 40})) #2
print(sys . getrefcount((10 , 20 , 30 , 40))) #May b 2 or more as it is reusable

# Find  outputs  (Home  work)
import  sys
class  Test:
	def  _init_(self):
		print('Constructor  :  ' , id(self))
		return    None
	def  _del_(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test()
print(t . _init_())
print(sys . getrefcount(t))
print(t . _del_())
print(sys . getrefcount(t))
print('Bye')
'''
Constructor  :  1000
Constructor  :  1000
None
2
Destructor  :  1000
25
2
Bye
Destructor  :  1000
'''

#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')
	def  _del_(self):
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
Program Begin
Function  Begin
Object  is    created
Type and address of a
Function  end
Type and address of a
Program  End
Object  is  lost
'''
#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')
	def  _del_(self):
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
Program Begin
Function  begin
Object  is    created
Function  end
Object  is  lost
Program  End
'''
#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')
	def  _del_(self):
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
	def   _init_(self , k):
		print('c1  class  object  is  created')
		self . b = k
		print('End  of  c1  class constructor')
	def   _del_(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  _init_(self):
		print('c2  class  object  is  created')
		self . a = c1(self)
		print('End  of  c2  class constructor')
	def  _del_(self):
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
Program end
c2  class  object  is  lost
c1  class  object  is  lost
'''

#  Lucky  object
# Find  outputs (Home  work)
class   c1:
	def  _del_(self):
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