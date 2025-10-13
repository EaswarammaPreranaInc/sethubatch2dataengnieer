# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass 
class   c3: #must give pass statement no to leave it blank



# Find  outputs  (Home  work)
class   c1:
	pass    
# End  of  the  class
a = c1() #nothing printed
print(id(a)) #address of object
print(type(a)) #class type
print(a . _dict_)#dictionary of object
print(a)#nothing printed
del  a #deletes the object
print(a)#error as object is deleted




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
a . m1() #3rd method
m1() #function


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
a . m1(10 , 20)#Two argument method :  10 20
a . m1(30)#Single argument method :  30
a . m1()#No argument method




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
a . m1(10 , 20)#Two argument method :  10 20
a . m1(30)#Single argument method :  30
a . m1()#No argument method


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
a . m1()#Method  of  third  c1  class



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
a . m1()#'c1' object has no attribute 'm1'


#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . _dict_)  # {}
a . x = 10
print(a . _dict_)# {'x': 10}
a . y = 20
print(a . _dict_)# {'x': 10, 'y': 20}
a . x = 30
print(a . _dict_)# {'x': 30, 'y': 20}
a . y = 40
print(a . _dict_)# {'x': 30, 'y': 40}
del  a . x
print(a . _dict_)# {'y': 40}
del  a . y
print(a . _dict_)# {}
del   a
print(a . _dict_)#name 'a' is not defined



'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import  math
class  triangle:
	def  get(self):
		#How  to  read  three  sides  into  object  self
		self.a = float(input('Enter side a: '))
		self.b = float(input('Enter side b: '))
		self.c = float(input('Enter side c: '))
	def  test(self):
		if  (self.a + self.b >= self.c) and (self.a + self.c >= self.b) and (self.b + self.c >= self.a):
			pass
		else:
			print('Not  a  triangle')
			exit()
	def  area(self):
		s = (self.a + self.b + self.c) / 2
		return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
	def  peri(self):
		return self.a + self.b + self.c
# End of the class
a = triangle()
a.get()
a.test()
print('Area : ',   a.area())
print('Perimeter : ',  a.peri())
