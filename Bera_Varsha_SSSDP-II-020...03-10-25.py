# Find  outputs
import   sys
class   c1:
    pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b)) # 5
print(sys . getrefcount(c1())) # 1
print(sys . getrefcount(352)) # 3
print(sys . getrefcount([10 , 20 , 15 , 18])) # 1
print(sys . getrefcount(10.8)) # 3
print(sys . getrefcount({10 , 20 , 15 , 18})) # 1
print(sys . getrefcount('Hyd')) # 3
print(sys . getrefcount({10 : 20 , 30 : 40})) # 1
print(sys . getrefcount((10 , 20 , 30 , 40))) # 3

# Find  outputs  (Home  work)
import  sys
class  Test:
	def  _init_(self):
		print('Constructor  :  ' , id(self)) # Constructor  :  address  of self
		return    None
	def  _del_(self):
		print('Destructor  :  ' , id(self)) # Destructor  :   address of self
		return  25
# End  of  the  class
t = Test()
print(t . _init_()) # None is returned
print(sys . getrefcount(t)) #2
print(t . _del_()) # 25 is returned
print(sys . getrefcount(t)) # 2
print('Bye') # Bye
'''Output:
Constructor  :   address of object 't'
Constructor  :   address of object 't'
None
2
Destructor  :   address of object 't'
25
2
Bye
Destructor  :   address of object 't'
'''
# # Tricky  program
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
'''Output:
Program  Begin
Function  begin
Object  is    created
Function  end
Object  is  lost
None
Program  End'''
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

'''Output
Program  Begin
Function  Begin
Object  is    created
type and address of c1
Function  end
type and address of c1
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

'''Output:
Program  Begin
Function  begin
Object  is    created
Function  end
Object  is  lost
Program  End'''

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

'''Output:
Program  begin
c2  class  object  is  created
c1  class  object  is  created
End  of  c1  class constructor
End  of  c2  class constructor
program end
c2  class  object  is  lost
c1  class  object  is  lost'''

#  Lucky  object
# Find  outputs (Home  work)
class   c1:
	def  _del_(self):
		print('Destructor') # Destructor
		global  b
		b = self
a = c1()
del  a
print('Hello') # Hello
'''Output:
Destructor
Hello'''