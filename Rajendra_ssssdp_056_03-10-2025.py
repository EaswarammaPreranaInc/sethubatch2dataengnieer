# Find  outputs
import   sys
class   c1:
    pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b))                         #5
print(sys . getrefcount(c1()))                      #1
print(sys . getrefcount(352))                       #cannot be predicted
print(sys . getrefcount([10 , 20 , 15 , 18]))       #1
print(sys . getrefcount(10.8))                      #cannot be predicted
print(sys . getrefcount({10 , 20 , 15 , 18}))       #1
print(sys . getrefcount('Hyd'))                     #cannot be predicted
print(sys . getrefcount({10 : 20 , 30 : 40}))       #1
print(sys . getrefcount((10 , 20 , 30 , 40)))       #cannot be predicted






# Find  outputs  (Home  work)
import  sys
class  Test:
	def __init__(self):
		print('Constructor  :  ' , id(self))
		return    None
	def __del__(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test()                              #Constructor  :  <1000 for example>
print(t .__init__())                    #Constructor  :  <1000><next_line>None
print(sys . getrefcount(t))             #2
print(t .__del__())                     #Destructor  : <1000><next_line>25 
print(sys . getrefcount(t))             #2
print('Bye')                            #Bye





#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def __init__(self):
		print('Object  is    created')
	def __del__(self):
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

''' outputs
Program  Begin
Function  Begin
Object is created
<c1 object at <1000 for example>>
Function  end
<c1 object at <1000>>
Program  End
Object is lost     '''






#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def __init__(self):
		print('Object  is    created')
	def __del__(self):
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

''' output
Program begin
Function begin
Object is created
Function end
Object is lost
Program End   '''






#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def __init__(self):
		print('Object  is    created')
	def __del__(self):
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

''' output
Program Begin
Function begin
Object is created
Function end
Object is lost
None
Program End    '''






# Most  tricky  program
# Circular  reference (Home  work)
class   c1:
	def  __init__(self , k):
		print('c1  class  object  is  created')
		self . b = k
		print('End  of  c1  class constructor')
	def __del__(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def __init__(self):
		print('c2  class  object  is  created')
		self . a = c1(self)
		print('End  of  c2  class constructor')
	def __del__(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin')
x = c2()
print('program end')

''' output
Program  begin
c2 class object is created
c1 class object is created
End of c1 class constructor
End of c2 class constructor
program end
c2 class object is lost
c1 class object is lost    '''






#  Lucky  object
# Find  outputs (Home  work)
class   c1:
	def __del__(self):
		print('Destructor')
		global  b
		b = self
a = c1()
del  a                      #Destructor
print('Hello')              #Hello