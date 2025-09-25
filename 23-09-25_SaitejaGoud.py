# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3: #Error 

# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a)) #Address of a
print(type(a)) #<class '_main_.c1'>
print(a . _dict_) #{}
print(a) #Type and Address
del  a #obj a is deleted
print(a) #Error


#  Find  outputs  (Home  work)
def   m1():
		print('Function')
class   c1:
	def   m1(self):
		print('1st  method')
	def   m1(self):
		print('2nd  method')
	def   m1(self):
		print('3rd  method')
# End  of  class  c1
a = c1()
a . m1() #3rd  method
m1() #Function


#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20) #Two  argument  method : 10 20
a . m1(30) #Error
a . m1() #Error

#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20) #Two  argument  method : 10 20
a . m1(30) #Two  argument  method : 30 2
a . m1() #Two  argument  method : 1 2

# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  third  c1  class')
a = c1()
a . m1() #Method  of  third  c1  class

# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1()
a . m1() #Error

#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . _dict_)  #{}
a . x = 10
print(a . _dict_) #{'x':10}
a . y = 20
print(a . _dict_) #{'x':10,'y':20}
a . x = 30
print(a . _dict_) #{'x':30,'y':20}
a . y = 40
print(a . _dict_) #{'x':30,'y':40}
del  a . x
print(a . _dict_) #{'y':40}
del  a . y
print(a . _dict_) #{}
del   a
print(a . _dict_) #Error

(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c


import  math
class  triangle:
	def  get(self):
	    self.x=int(input("Enter the x :"))
	    self.y=int(input("Enter the y :"))
	    self.z=int(input("Enter the z :"))
	def  test(self):
		if  self.x+self.y>=self.z and self.y+self.z>=self.x and self.z+self.x>=self.y:
				pass
		else:
		    print('Not  a  triangle')
		    exit()
				
	def  area(self):

	    s=(self.x+self.y+self.z)//2
	    return   math.sqrt(s * (s - self.x) * (s - self.y) * (s - self.z))
	def  peri(self):
			return  self.x+self.y+self.z
# End of the class
a=triangle()#How  to  create  triangle  class  object
a.get() 
a.test()#How  to  test  whether  inputs  are  valid
print('Area : ',   a.area())
print('Perimeter : ', a.peri())