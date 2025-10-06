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
output:
Program  Begin
Function  begin 
Object  is    created
Function  end
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
print('Program  Begin')
b = f1()
print(b)
print('Program  End')

'''
output:
Program  Begin
Function  begin
Object  is    created
Function  end
Program  End
Object  is  lost
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
output:
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
	def  _del_(self):
		print('Destructor')
		global  b
		b = self
a = c1()
del  a
print('Hello')

'''
output:
Destructor
Hello
'''