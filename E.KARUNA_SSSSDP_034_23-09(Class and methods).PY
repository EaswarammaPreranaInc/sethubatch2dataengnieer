# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:#error:In class either method nor Pass here both are not there
	


# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))#address of the object 'a'
print(type(a))#<class '__main__.c1'>
print(a . _dict_)#convert object to dictionary i.e {}
print(a)#type and address
del  a#deletes object 'a'
print(a)#error bcz there is no object



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
a = c1()#object is created
a . m1()#3rd method
m1()# function


#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()#object is created
a . m1(10 , 20)#10<space>20
a . m1(30)#error one argument is missing
a . m1()#error there is no arguments


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
a = c1()#object is created
a . m1()#method of third c1 class when mutiple classes with same name so last one is recognized


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
a . m1(10 , 20)#10<space>20
a . m1(30)#30<space>2
a . m1()#1<space>2



# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1()#object 'a' is created
a . m1()#error c1 class has no m1 method



#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . _dict_) #{} 
a . x = 10
print(a . _dict_)#{x:10}
a . y = 20
print(a . _dict_)#{x:10,y:20}
a . x = 30
print(a . _dict_)#{x:30,y:20}
a . y = 40
print(a . _dict_)#{x:30,y:40}
del  a . x
print(a . _dict_)#variable 'x' is deleted from the object i.e{y:40}
del  a . y
print(a . _dict_)#variavle 'y' is deleted from the object
del   a
print(a . _dict_)#object 'a' is deleted




'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import  math
class  triangle:
	def  get(self):
		self.a=float(input('enter a first side:'))
		self.b=float(input('enter second side:'))
		self.c=float(input('enter third side:')) #How  to  read  three  sides  into  object  self
	def  test(self):
		if  self.a+self.b>=self.c or self.b+self.c>=self.a or self.c+self.a>=b:#sum  of  every  2  sides  >=  3rd  side:
				pass#Do  nothing
		else:
				print('Not  a  triangle')
				exit()#How  to  stop  execution
	def  area(self):
			s = (self . a + self . b + self . c) / 2
			return math.sqrt(s * (s - self . a) * (s - self . b) * (s - self . c)) # area  of  triangle
	def  peri(self):
			return self. a +self. b + self.c #perimeter  of  triangle
# End of the class
t=triangle()#How  to  create  triangle  class  object
t.get()#How  to  read  inputs  into  object
t.test()#How  to  test  whether  inputs  are  valid
print('Area : ', t.area())
print('Perimeter : ', t.peri())
