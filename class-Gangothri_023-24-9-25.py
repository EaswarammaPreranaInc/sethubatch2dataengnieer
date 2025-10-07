#Repeat  prog5a  such  that  methods  are  called  in  another  way
#1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)
#2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
from prog3a import triangle
a=triangle() #How  to  create  triangle  object
triangle.get(a) #How  to  call  get()  method  in  another  way
triangle.test(a) #How  to  call  test()  method  in  another  way
print('Area : ', triangle.area(a)) #How  to  call  area()  method  in  another  way
print('Perimeter: ', triangle.peri(a)) #How  to  call  peri()  method  in  another  way

#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x)
		print(self . x)
		x += 5
		self . x += 7
	def   m2(self):
		print(x) # Error
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1()
a . m1() # m1() method 
a . m2() # m2() method
print(a . x) # 33
print(self.x) # Error
print(x) # Error
'''Output:
10
20
27
33'''

'''(Home  work) Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object
1st  object   --->  x = 10 , y = 20 , z = 30
2nd  object --->  x = 40 , y = 50 , z = 60
3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		self.x = int(input("Enter x value: "))
		self.y = int(input("Enter y value: "))  
		self.z = int(input("Enter z value: "))#How  to  read  inputs  into  variables  x , y  and  z  of  object  self
	def  add(self , m , n):
		self.x = m.x+n.x
		self.y = m.y+n.y
		self.z = m.z+n.z #How  to  add  objects  m  and  n  and  store  results  in  object  self
	def  disp(self):
		print("x =", self.x)
		print("y =", self.y)
		print("z =", self.z)  #How  to  print  object  self
# End  of  the  class
a=Test() 
b=Test()
c=Test() #How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
a.get() #How  to  read  inputs  into  object  'a'
print('Second  Object')
b.get() #How  to  read  inputs  into  object  'b'
c.add(a, b)#How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
c.disp() #How  to  print  object  'c

#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date() # Creates an empty Date class object
a . dd = 15 # Adds variable dd to object 'a'
a . mm = 8 # Adds variable mm to object 'a'
a . yy = 1947 # Adds variable yy to object 'a'
print(a) # type and address of the object 'a'

#  Find  outputs (Home  work)
class   c1:
	def  __str__(self):
			return  '25'
class   c2:
	def  __str__(self):
			return   35
class   c3:
	def  __str__(self):
			print('Hyd')
class   c4:
	def  __str__(self , x):
			return   F'{x}'
#end of the class
a = c1() 
b = c2()
c = c3()
d = c4()
print(a) # 25 is returned
print(b) # Error
print(c) # Error
print(d) # Error
print(b . __str__()) # 35
print(c . __str__()) # prints Hyd and None is returned
print(d . __str__(50)) # 50


#Write  a  program  to  determine  total , average  and  grade  of  a  student
#Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender

class   Student:
	def   get(self):
		self.roll_number = int(input("Enter: ")) #How  to  read  roll  number  into  object  self
		self.name = input("Enter: ") #How  to  read  student  name  into  object  self
		self.gender = input("Enter: ") #How  to  read  gender  into  object  self
		self.m= [] #How  to  read  marks  of  3  subjects
		for i in range(3):
			marks = int(input('Enter marks : '))
			self.m.append(marks)
	def   compute(self):
		self.tot = sum(self.m) #How  to  calculate  total  marks
		self.avg = self.tot/3 #How  to  calculate  average  marks
		if  min(self.m) < 40:
				self.grade = 'Fail'
		elif  self.avg >= 70:
				self.grade =  'Distinction'
		elif  self.avg  >= 60:
				self.grade = 'First  class'
		elif  self.avg >= 50:
				self.grade = 'Second  class'
		else:
				self.grade = 'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,  self.roll_number)
		print('Student  Name  :  ' , self.name)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.tot)
		print('Average  :  ' , self.avg)
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		return  F'{self.roll_number} \t {self.name} \t {self.gender} \t {self.tot}\t {self.avg} \t {self.grade}'
#End  of  the  class
if __name__ == '__main__':
	s= Student() # How  to  create  Student  class  object
	s.get() #How  to  read  inputs  into  object
	s.compute()# How  to  store  results  in  object
	s.disp() # How  to  print  object  with  disp()  method
	print(s) # How  to  print  object  with  __str__()  method


#Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

'''1) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   5 / 9
    What  is  the  sum  ?  ---> 2 / 3 + 5 / 9 = (18 + 15) / 27 = 33 / 27 = 11 / 9
    What  is  the  difference  ?  ---> 2 / 3 - 5 / 9 =  (18 - 15) / 27 =  3 / 27 = 1 / 9
    What  is  the  product  ?  ---> 	2 / 3 * 5 / 9 =  10 / 27  =  10 / 27
    What  is   the  division  ?  ---> 	2 / 3 /  5 / 9 =  2 / 3 * 9 / 5 =  18 / 15 =  6 / 5  --->  Succesful  division

2) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   0 / 9
    What  is  the  sum  ?  --->  2 / 3 + 0 / 9 = (18 + 0) / 27 =  18 / 27 =  2 / 3
    What  is  the  difference  ?  ---> 2 / 3 - 0 / 9 =  (18 - 0) / 27 =  18 / 27 = 2 / 3
    What  is  the  product  ?  ---> 	2 / 3 * 0 / 9 = 	0 / 27  =  	0 / 27  --->  Simplification  is  not  required  becoz  numerator  is  0
    What  is   the  division  ?  ---> 	2 / 3 /  0 / 9 = 2 / 3 * 9 / 0 = 	18 / 0  ---> Division  is  not   permitted

3) When  is  simplification  required ?  ---> When  numerator  is  non-zero
'''
import  math
class  Rat:
	def  get(self):
		self.nr = int(input('Enter numerator: ')) #How  to  read  numerator  into  object  self
		self.dr = int(input('Enter denominator: ')) #How  to  read  denominator  into  object  self
		self.test() # How  to  call  test()  method
	def  test(self):
		while self.dr == 0:
			self.dr = int(input('Denominator cannot be zero, re-enter: ')) #Ask  user  to  reenter  denom  when  denom  is  zero
	def    __str__(self):
			return  F'{self.nr}/{self.dr}' #values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	def   add(self , a , b):
		self.nr=a.nr*b.dr+a.dr*b.nr #How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
		self.dr=a.dr*b.dr
		self.simplify() #How  to  simplify  object  self
	
	'''c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		self.nr=a.nr*b.dr-a.dr*b.nr 
		self.dra.dr*b.dr# How  to  subtract  objects  'a'  and  'b' and  store  results  in  object  self
		self.simplify() #How  to  simplify  object  self
	
	'''d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9'''
	
	def   mul(self , a , b):
		self.nr=a.nr*b.nr 
		self.dr = a.dr*b.dr #How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  self
		self.simplify() #How  to  simplify  object  self
	
	'''e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27'''
	
	def    div(self , a , b):
		self.nr=a.nr*b.dr
		self.dr=a.dr*b.nr#How  to  divide  objects  'a'  and  'b' and  store  results  in  object  self
		self.simplify() # How  to  simplify  object  self
	
	'''f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5'''
	
	def   simplify(self):
			if self.nr!=0:
				ans= math.gcd(self.nr,self.dr)#How  to  find  gcd  of  numerator  and   denominator
				self.nr = self.nr//ans
				self.dr = self.dr//ans #How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
	
	'''c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27'''
	
# End  of the class
if __name__=='__main__':
	a=Rat() 
	b=Rat()
	c=Rat()#How  to  create  6  objects  a , b , c , d , e , f
	d=Rat()
	e=Rat()
	f=Rat()
	a.get() #How  to  read  rational  number  into  object  'a'
	b.get() #How to  read  rational  number  into  object  'b'
	c.add(a,b) #How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
	d.sub(a,b) #How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
	e.mul(a,b) #How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
	f.div(a,b) #How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
	print('Sum: ',c) #How  to  print  object   'c'
	print('Difference: ',d) # How  to  print  object   'd'
	print('Product: ',e)#How  to  print  object   'e'
	if  b.nr != 0:
		print('Division: ',f)#How  to  print  object  'f
	else:
		print('Division  is  not  permitted')
