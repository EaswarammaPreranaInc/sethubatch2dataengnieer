#  Find  outputs  
class  parent:
	def  m1(self):
		print('Overridden  Method')
class  child(parent):
	def  m1(self):
		print('Overriding  Method')
#end of the class
x = parent()
x . m1()
x = child()
x . m1() # m1 method in child class overrides the m1 method in parent class
'''
o/p:
overridden Method
overriding Method
'''

# Find  outputs   
class   parent:
	def  m1(self):
		print('m1  method  of  parent  class')
	def  m2(self):
		print('m2  method  of  parent class')
class  child(parent):
	def  m1(self):
		print('m1  method  of  child  class')
	def  m3(self):
		print('m3  method  of  child  class')
#end of the class
x = parent()
x . m1()
x . m2()
#x . m3() # error : no m3 method in parent class
x = child()
x . m1()
x . m2()
x . m3()
'''
o/p:
m1  method  of  parent  class
m2  method  of  parent class
m1  method  of  child  class
m2  method  of  parent class
m3  method  of  child  class
'''


# Find  outputs 
class  parent:
	def  marriage(self):
		print('Arranged Marriage')
	def  property(self):
		print('One  Crore')
	def  study(self):
		print('Studies only' , end = '\t')
class  child(parent):
	def  marriage(self):
		print('Love Marriage')
	def  study(self):
		super() . study() # parent class study method is executed
		print(' + Entertainment')
#end of the class
c = child()
c . marriage()
c . property()
c . study()
'''
o/p:
Love Marriage
One  Crore
Studies only + Entertainment
'''


# Find  outputs  
class  parent:
	def  add(self , x , y):
		return  x + y
class  child(parent):
	def   add(self , x , y , z):
		return   x + y + z
# End of the class
c = child()
print(c.add(10 , 20 , 30)) # 60
#print(c.add(10 , 20)) # error : require 3 positional arguments
print(super(child,c).add(40,50)) # 90



# Find  output 
class  parent:
	def  add(self , x , y):
		print('parent  method')
		return  x + y
class  child(parent):
	def   add(self , x , y , z = 3):
		print('child  method')
		return  x + y + z
#End  of  the  class
c = child()
print(c . add(10 , 20 , 30))
print(c . add(10 , 20)) # default argument z=3
'''
o/p:
child method
60
child method
33
'''


#Find  output
class  parent:
	def   m1(self , a , b , /):
		print(F'parent  method  --->   a  :  {a}  \t  b  :  {b}')
class  child(parent):
	def   m1(self , x , y):
		print(F'child  method  --->  x  :  {x}  \t  y  :  {y}')
# End of the class
c = child()
c . m1(x = 10 , y = 20)
c . m1(30 , 40)
'''
o/p:
child method ---> x : 10    y : 20
child method ---> x : 30    y : 40
'''


