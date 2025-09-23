# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:# error there should be any one method defined




# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))# address of class object a
print(type(a))# <class c1>
print(a . __dict__)#{}
print(a)#tyoe and address
del  a
print(a)# error because it is deleted 




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
a . m1()#1st method
m1()# error , there is no m1() function 



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
a . m1(10 , 20)#two argument method:10,20
a . m1(30)#Single  argument  method : ' , 30
a . m1()#no argument method 



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
a . m1(10 , 20)#Two  argument  method : ' , 1, 2)
a . m1(30)#Single  argument  method : ' , 30
a . m1()#no argument method




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
a . m1()#Method  of  second  c1  class



#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__)  #{}
a . x = 10
print(a . __dict__){x:10}
a . y = 20
print(a . __dict__)#{x:10,y:20}
a . x = 30
print(a . __dict__)#{x:30,y:20,}
a . y = 40
print(a . __dict__)#{x:30,y:40,}
del  a . x
print(a . __dict__){y:40}
del  a . y
print(a . __dict__)#{}
del   a
print(a . __dict__)#error



'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import  math
class  triangle:
	def  get(self):
		How  to  read  three  sides  into  object  self
	def  test(self):
		if  sum  of  every  2  sides  >=  3rd  side:
				Do  nothing
		 else:
				print('Not  a  triangle')
				How  to  stop  execution
	def  area(self):
			return   area  of  triangle
	def  peri(self,a,b,c):
			return  a+b+c
# End of the class
N=triangle()How  to  create  triangle  class  object
N.a=10
N.b=20
N.c=30
How  to  test  whether  inputs  are  valid
print('Area : ',   N.area())
print('Perimeter : ',  N.peri(a,b,c))