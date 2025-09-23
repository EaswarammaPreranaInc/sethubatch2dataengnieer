'''vaishnavi koneru '''
[12:41, 9/23/2025] +91 99482 50500: # Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:#class should atleast one method or pass
[12:41, 9/23/2025] +91 99482 50500: # Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1() 
print(id(a))#address of class object 1000
print(type(a))#__main__.c1
print(a . _dict_)#creates dictionary with keyvalue pairs with object variables
print(a)#__main__.c1 object at 000001
del  a #deletes c1  calss object 
print(a)#error because c1 class object is deleted
[12:47, 9/23/2025] +91 99482 50500: #  Find  outputs  (Home  work)
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
a = c1()#c1 class object is created
a . m1()#method m1 of c1 class is called 
m1()#outer function of the module is called.
[12:47, 9/23/2025] +91 99482 50500: #  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()#c1 class object is created
a . m1(10 , 20)#Two argument method : 10 20
a . m1(30)#single argument method : 30
a . m1()#No argument method
[12:47, 9/23/2025] +91 99482 50500: #  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1#c1 class object is created
a . m1(10 , 20)#x and y values are replaced and Two  argument  method : 10 20 is printed
a . m1(30)#single argument method : 30
a . m1()#No argument method
[12:48, 9/23/2025] +91 99482 50500: # Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  third  c1  class')
a = c1()#class c1 object is created and last c1 class is considered
a . m1()#prints method of third c1 class
[12:48, 9/23/2025] +91 99482 50500: # Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1()#object of last c1 class is created 
a . m1()#error because there is no method m1 in last c1 class
[12:50, 9/23/2025] +91 99482 50500: #  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()#c1 class object is created
print(a . _dict_)#class variables turns to key value pairs as append to dictionary
a . x = 10
print(a . _dict_)#{x : 10}
a . y = 20
print(a . _dict_)#{x:10,y:20}
a . x = 30
print(a . _dict_)#replaces a value {x:30,y:20}
a . y = 40
print(a . _dict_)#replaces b value{x:30,y:40}
del  a . x #deletes x key and value
print(a . _dict_)#{y:40}
del  a . y#deletes y key and value
print(a . _dict_)#prints empty dictionary {}
del   a#object a is deleted
print(a . _dict_)#error because object a is deleted before.






[12:53, 9/23/2025] +91 99482 50500: '''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import  math
class  triangle:
	def  get(self):
		self.a = int(input("enter 1st number : "))
		self.b = int(input("enter 2nd number : "))
		self.c = int(input("enter 3rd number : "))

	def  test(self):
		if  ((self.a+self.b > self.c) and (self.b+self.c > self.a) and (self.c+self.a > self.b)):   
				pass
		else:
				print('Not  a  triangle')
				return False
	def  area(self):
			s = (self.a+self.b+self.c)/2
			return   math.srt(s * (s - self.a) * (s - self.b) * (s - self.c))
	def  peri(self):
			return  self.a+self.b+self.c
# End of the class
a = triangle()#How  to  create  triangle  class  object
a.get()#How  to  read  inputs  into  object
if a.get():#How  to  test  whether  inputs  are  valid
	print('Area : ',   a.area())
	print('Perimeter : ',  a.peri())
else:
	print("Invlid Input")
