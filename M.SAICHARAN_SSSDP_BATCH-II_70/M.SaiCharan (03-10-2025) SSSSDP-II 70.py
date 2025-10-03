                     NAME:M.SAICHARAN                       HOMEWORK
                     DATE:03-10-2025


1.# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b))				#5
print(sys . getrefcount(c1()))				#1
print(sys . getrefcount(352))				#2
print(sys . getrefcount([10 , 20 , 15 , 18]))		#1
print(sys . getrefcount(10.8))				#2
print(sys . getrefcount({10 , 20 , 15 , 18}))		#1
print(sys . getrefcount('Hyd'))				#2
print(sys . getrefcount({10 : 20 , 30 : 40}))		#1
print(sys . getrefcount((10 , 20 , 30 , 40)))		#2



2.# Find  outputs  (Home  work)
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

#Output:
Constructor  :   2194768154064
Constructor  :   2194768154064
None
2
Destructor  :   2194768154064
25
2
Bye


3.#  Tricky  program
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

#Output:
Program  Begin
Function  Begin
Object  is    created
<__main__.c1 object at 0x...>
Function  end
<__main__.c1 object at 0x...>
Program  End



4.#  Tricky  program
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

#Output:
Program  Begin
Function  begin
Object  is    created
Function  end
Object  is  lost
Program  End



5.#  Tricky  program
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

#Output:
Program  Begin
Function  begin
Object  is    created
Function  end
Object  is  lost
None
Program  End




6.# Most  tricky  program
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

#Output:
Program  begin
c2  class  object  is  created
c1  class  object  is  created
End  of  c1  class constructor
End  of  c2  class constructor
program end

7.#  Lucky  object
# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
		print('Destructor')
		global  b
		b = self
a = c1()
del  a
print('Hello')

#Output:
Destructor
Hello