# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self.x=10 # How  to  initialize  public  variable  'x'  to  10
		self.__y=20 # How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		print(self.x) #  print   variable  'x'
		print(self.__y) # print  private  variable  'y'
		self.__m2() # call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x) # print   variable  'x'
		print(self.__y) # print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x) #  print  variable  'x'
print(t._Test__y) # print   variable  'y'
#print(t . __y) # error
print(t . __dict__)
t.m1() # call  method  m1()
t._Test__m2() # call   method  m2()
#t . __m2() # error
print('End')
'''
o/p:
Outside
10
20
{'x': 10, '_Test__y': 20}
m1  method
10
20
__m2  method
10
20
Back to m1 method
__m2  method
10
20
End
'''


#  Find  outputs
class  c1:
	def __init__(self):
		self.x=10 # initialize  public  variable  'x'  with  10
		self.__x=20 # initialize  private  variable  'x'  with  20
		self.__x__=30 # initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x) # How  to  print   variable  'x'
print(a.__x__) # How  to  print  public  dunder  variable  'x'
print(a._c1__x) # How  to  print   private  variable  'x'
#print(a . __x) # error
a.m1() # How  to  call  public  method  m1()
a.__m1__() # How  to  call  public  dunder  method  m1()
a._c1__m1() # How  to  call  private  method  m1()
# a . __m1() # error
'''
o/p
10
30
20
public method
public Dunder method
private method
'''


'''
Find  outputs
Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively
'''
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End    of    the    class
a = c1() 
a = None 
b = c1() 
del    b
c = c1()
c = c1()
d = c1()
e = c1()
'''
o/p:
Object is created at address : 1000
Object at address 1000 is lost
Object is created at address : 2000
Object at address 2000 is lost
Object is created at address : 3000
Object at address 3000 is lost
Object is created at address : 4000
Object is created at address : 5000
Object is created at address : 6000
'''


# Identify  Error 
class   c1:
	def  __del__(self , x):
		print('destructor : ' ,  x)
a = c1()
#a . __del__(25) # cannot call destructor manually with arguments



# Find  outputs 
class   c1:
	def  __del__(self , x = 35):
		print('destructor : ' , x)
a = c1() # destructor : 35
a . __del__(25)



# Find  outputs 
class   c1:
	def  __del__(self):
			print('destructor')
			#b = c1() # error : infinite loop
a = c1()



# Find  outputs 
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		#b = c1() # error : infinite loop
a = c1()



#  Find  outputs
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')
# End  of  the  class
a = c1() # 3rd contructor



#Find  outputs 
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()
del   a
print('Hello')
del   b
print('Hi')
del   c
print('Bye')
d = c1()
print('End')
'''
o/p:
Object  is  created  at  address  : address of a
Hello
Hi
Object  at  address  address of b  is  lost
Bye
Object  is  created  at  address  :  address of c
End
Object  at  address  of d  is  lost
'''


# Find  outputs
class  c1:
        def     _init_(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]
del  list
'''
Object at address c1 is lost
Object at address c1 is lost
Object at address c1 is lost
'''


# Find  outputs  
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()
print(a . __del__())
print('Hello')
del   a
'''
o/p:
destructor
25
Hello
destructor'''