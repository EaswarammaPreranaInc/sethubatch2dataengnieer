# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b)) # count no,of references for the object : 5
print(sys . getrefcount(c1())) # 1
print(sys . getrefcount(352)) # cannot be predicted as 352 is immutable
print(sys . getrefcount([10 , 20 , 15 , 18])) # 1
print(sys . getrefcount(10.8)) # cannot be predicted as 10.8 is immutable
print(sys . getrefcount({10 , 20 , 15 , 18})) # 1
print(sys . getrefcount('Hyd')) # 1
print(sys . getrefcount({10 : 20 , 30 : 40})) # 1
print(sys . getrefcount((10 , 20 , 30 , 40))) # 1



# Find  outputs  
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
o/p:
constructor : address of object a 
constructor : address of object a 
None
2
Destructor : address of a 
25 : destructor is called explicitly so it returns 25 and the prints
2
Bye
Destructor : address of object which is going to delete
'''


#  Tricky  program
# Find  outputs 
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
o/p:
Program Begin
Function Begin
object is created
type and address of class c1
Function end
type and address of class c1
program end
object is lost
Destructor : address of object a
'''


#  Tricky  program
# Find  outputs 
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
o/p:
Program Begin
Function begin
object is created
Function end
object is lost
program End
'''



# Find  outputs 
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
o/p:
program begin
Function begin
object is created
Function end
object is lost
None
program End
'''


# Most  tricky  program
# Circular  reference 
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
o/p:
program begin
c2 class object is created
c1 class object is created
End of c1 class contructor
End of c2 class contructor
program end
c2 class object is lost
c1 class object is lost
'''



# Find  outputs 
class   c1:
	def  __del__(self):
		print('Destructor')
		global  b
		b = self
a = c1()
del  a
print('Hello')
'''
o/p:
Destructor
Hello
'''