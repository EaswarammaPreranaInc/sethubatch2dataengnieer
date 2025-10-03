# Find  outputs
import   sys
class   c1: # empty class
        pass
# End  of  the  class
a = b = c = d = c1() # obj created
print(sys . getrefcount(b)) # 5
print(sys . getrefcount(c1())) # 1
print(sys . getrefcount(352)) # cannot  predict
print(sys . getrefcount([10 , 20 , 15 , 18])) # 1
print(sys . getrefcount(10.8)) # cannot  predict
print(sys . getrefcount({10 , 20 , 15 , 18})) # 1
print(sys . getrefcount('Hyd')) # 3
print(sys . getrefcount({10 : 20 , 30 : 40})) # 1
print(sys . getrefcount((10 , 20 , 30 , 40))) # 3


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
t = Test() # Constructor  : 1000
print(t . _init_()) # None
print(sys . getrefcount(t)) # 2
print(t . _del_()) # Destructor  : 1000  25
print(sys . getrefcount(t)) # 2
print('Bye') # Bye


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
print('Program  Begin') # Program  Begin
b = f1() 
'''
Function  Begin
Object  is    created
Type and address
Function  end

'''
print(b) # type and addres
print('Program  End') # Program End
# Object  is  lost


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
print('Program  Begin') # Program  Begin
f1()
'''
Function  begin
Object  is    created
Function  end
Object  is  lost
'''
print('Program  End') # Program  End


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
print('Program  Begin') # Program  Begin
b = f1() 
'''
Function  begin
Object  is    created
Function  end
Object  is  lost
'''
print(b) # None
print('Program  End') # Program  End


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
print('Program  begin') # Program  begin
x = c2() 
'''
c2  class  object  is  created
c1  class  object  is  created
End  of  c1  class constructor
End  of  c2  class constructor
'''

print('program end') # program end
# c2  class  object  is  lost
# c1  class  object  is  lost


#  Lucky  object
# Find  outputs (Home  work)
class   c1:
	def  _del_(self):
		print('Destructor')
		global  b
		b = self
a = c1() # Destructor
del  a
print('Hello') # Hello
