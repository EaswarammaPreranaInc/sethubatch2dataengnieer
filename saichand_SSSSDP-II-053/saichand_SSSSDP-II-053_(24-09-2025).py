from pro1 import triangle
a=triangle()
a.get()				# How  to  call  get()  method  in  another  way
a.test()			# How  to  call  test()  method  in  another  way
print('Area : ', a.area())	# How  to  call  area()  method  in  another  way)
print('Perimeter: ', a.peri())	# How  to  call  peri()  method  in  another  way)






#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x)				# 10
		print(self . x)				# 20
		x += 5					# x=15
		self . x += 7 
	def   m2(self):
		print(x)				# Error, x is local var
		print(self . x)				# 27
		self . x += 6 				# 33
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x)						# 33
print(self . x)						# error 
print(x)						# error






'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''

#Program:
class  Test:
	def   get(self):
		self.x=int(input('Enter  x  value : '))		# How  to  read  inputs  into  variables  x , y  and  z  of  object  self
		self.y=int(input('Enter  y  value : '))
		self.z=int(input('Enter  z  value : '))
	def   add(self , m , n):
		self.x = m.x + n.x				# How  to  add  objects  m  and  n  and  store  results  in  object  self
		self.y = m.y + n.y
		self.z = m.z + n.z
	def  disp(self):
		print(self.x)					# How  to  print  object  self 
		print(self.y)
		print(self.z)
# End  of  the  class
a=Test() 
print('First  Object')						# How  to  create  three  Test  class  objects  a , b  and  c
a.get()								# How  to  read  inputs  into  object  'a'
b=Test()
print('Second  Object')

b.get()								# How  to  read  inputs  into  object  'b'
c=Test()							# How  to  add  objects  a  and  b  and  store  results in  object  'c'
c.add(a,b)
print('Addition  results')
c.disp()






#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)					# Type and address






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
print(a)					# 25  
print(b)					# Error 
print(c)					# Hyd
						# Error
print(d)					# Error
print(b . __str__())				# 35
print(c . __str__())				# Hyd
						# None
print(d . __str__(50))				# 50








'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''

#Program:
class   Student:
	def   get(self):
		self.rollno=int(input("enter roll no: "))				# How  to  read  roll  number  into  object  self
		self.name = input("enter name: ")					# How  to  read  student  name  into  object  self
		self.gender = input("enter gender: ")					# How  to  read  gender  into  object  self
		self.m=[]								# How  to  read  marks  of  3  subjects
		for i in range(3):
			marks=int(input("enter marks: "))
			self.m.append(marks)
	def   compute(self):
		self.total= sum(self.m)							# How  to  calculate  total  marks
		self.avg=self.total/3							# How  to  calculate  average  marks
		if  self.avg < 40:
			self.grade= 'Fail'						# How  to  initilaize  grade  to  'Fail'
		elif self.avg >= 70:
			self.grade= 'Distinction'   
		elif self.avg >= 60:
			self.grade= 'First  Class'  					# How  to  initilaize  grade  to  'First  Class'
		elif self.avg >= 50:
			self.grade= 'Second  Class' 					# How  to  initilaize  grade  to  'Second  Class'
		else:
			self.grade= 'Third  class' 					# How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   self.rollno  )
		print('Student  Name  :  ' , self.name )
		print('Gender  :  ' ,  self.gender )
		print('Total  Marks  :  ' ,self.total)
		print('Average  :  ' , self.avg)
		print('Grade  :  ' , self.grade)
	def   __str__(self):								# All  the   values  of  object  self  in  the  form  of strings
		return  f'roll no : {self.rollno} name: {self.name}  Gender : {self.gender}  Total Marks : {self.total}  average : {self.avg}  Grade : {self.grade}'  
#End  of  the  class
a=Student()										# How  to  create  Student  class  object
a.get()											# How  to  read  inputs  into  object
a.compute()										# How  to  store  results  in  object
a.disp()										# How  to  print  object  with  disp()  method
print(a)										# How  to  print  object  with  _str_()  method







'''
Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

1) 1st  rational  number  --->  2 / 3
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

#Program:
import math
class Rat:
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))
        self.test()   
    def test(self):
        while self.den == 0:						# Denominator must not be zero
            print("Denominator cannot be zero")
            self.den = int(input("Enter denominator again: "))
    def __str__(self):
        return f"{self.num} / {self.den}"				# Print as rational number (e.g., "2 / 3")
    def add(self, a, b):
        self.num = a.num * b.den + b.num * a.den
        self.den = a.den * b.den
        self.simplify()
    def sub(self, a, b):
        self.num = a.num * b.den - b.num * a.den
        self.den = a.den * b.den
        self.simplify()
    def mul(self, a, b):
        self.num = a.num * b.num
        self.den = a.den * b.den
        self.simplify()
    def div(self, a, b):
        if b.num == 0:							# Division by zero check
            self.num = 1
            self.den = 0  						# represent invalid division
        else:
            self.num = a.num * b.den
            self.den = a.den * b.num
            self.simplify()
    def simplify(self):
        if self.num != 0 and self.den != 0:				# Simplify only if numerator is non-zero
            g = math.gcd(self.num, self.den)
            self.num //= g
            self.den //= g
# Create 6 objects
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()
# Input
print("First Rational Number:")
a.get()
print("Second Rational Number:")
b.get()
# Operations
c.add(a, b)
d.sub(a, b)
e.mul(a, b)
f.div(a, b)
# Output
print("\nResults:")
print("Addition:", c)
print("Subtraction:", d)
print("Multiplication:", e)
if f.den == 0:   # invalid division case
    print("Division is not permitted")
else:
    print("Division:", f)