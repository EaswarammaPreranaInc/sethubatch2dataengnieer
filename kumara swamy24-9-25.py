'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
from prog5a import triangle  # How  to  create  triangle  object
t=triangle()    
a=float(input("Enter 1st Side :"))
b=float(input("Enter 2nd Side :"))
c=float(input("Enter 3rd Side :"))       
triangle.get(t,a,b,c)    # How  to  call  get()  method  in  another  way
triangle.test(t)   # How  to  call  test()  method  in  another  way
print('Area : ',triangle.area(t))   #  How  to  call  area()  method  in  another  way
print('Perimeter: ',triangle.peri(t))  # How  to  call  peri()  method  in  another  way


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
		print(x)
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1()
a . m1()  #10,20
a . m2() # 27
print(a . x) # 33
print(self . x) # Error
print(x) # error

Oytput :
10
20
27
33
Error
Error

'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
# program 
class  Test:
	def   get(self):
		 #How  to  read  inputs  into  variables  x , y  and  z  of  object  self
		self.x=int(input('Enter  x  value : '))
		self.y=int(input('Enter  y  value : '))
		self.z=int(input('Enter  z  value : '))
	def   add(self , m , n):
		self.x=m.x+n.x 
		self.y=m.y+n.y
		self.z=m.z+n.z
		 #How  to  add  objects  m  and  n  and  store  results  in  object  self
	def  disp(self):
		print(self.x) 
		print(self.y)
		print(self.z)
        #How  to  print  object  self
# End  of  the  class
a=Test() 
#How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
#How  to  read  inputs  into  object  'a'
a.get()
b=Test()
print('Second  Object')

#How  to  read  inputs  into  object  'b'
b.get()
#How  to  add  objects  a  and  b  and  store  results in  object  'c'
c=Test()
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
print(a) # Type and address of class object 'a'


#  Find  outputs (Home  work)
class   c1:
	def  _str_(self):
			return  '25'
class   c2:
	def  _str_(self):
			return   35
class   c3:
	def  _str_(self):
			print('Hyd')
class   c4:
	def  _str_(self , x):
			return   F'{x}'
#end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a) # Type and address of class object 'a'
print(b) # Type and address of class object 'b'
print(c) # Type and address of class object 'c'
print(d) # Type and address of class object 'd'
print(b . _str_()) # 35
print(c . _str_()) # print 'Hyd' and return None
print(d . _str_(50)) # 50


'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
# program
class   Student:
	def   get(self):
		self.rollno=int(input("enter roll no: ")) #How  to  read  roll  number  into  object  self
		self.name = input("enter name: ") #How  to  read  student  name  into  object  self
		self.gender = input("enter gender: ")#How  to  read  gender  into  object  self
		#How  to  read  marks  of  3  subjects
		self.m=[]
		for i in range(3):
			marks=int(input("enter marks: "))
			self.m.append(marks)
	def   compute(self):
		self.total= sum(self.m) #How  to  calculate  total  marks
		self.avg=self.total/3 #How  to  calculate  average  marks
		if  self.avg < 40:
			self.grade= 'Fail' #How  to  initilaize  grade  to  'Fail'
		elif self.avg >= 70:
			self.grade= 'Distinction'   
		elif self.avg >= 60:
			self.grade= 'First  Class'  #How  to  initilaize  grade  to  'First  Class'
		elif self.avg >= 50:
			self.grade= 'Second  Class' #How  to  initilaize  grade  to  'Second  Class'
		else:
			self.grade= 'Third  class' #How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   self.rollno  )
		print('Student  Name  :  ' , self.name )
		print('Gender  :  ' ,  self.gender )
		print('Total  Marks  :  ' ,self.total)
		print('Average  :  ' , self.avg)
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		return  f'roll no : {self.rollno} name: {self.name}  Gender : {self.gender}  Total Marks : {self.total}  average : {self.avg}  Grade : {self.grade}'#All  the   values  of  object  self  in  the  form  of  
#End  of  the  class
a=Student()#How  to  create  Student  class  object
a.get()##How  to  read  inputs  into  object
a.compute()#How  to  store  results  in  object
a.disp() #How  to  print  object  with  disp()  method
print(a)#How  to  print  object  with  _str_()  method



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
# program
import math

class Rat:
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))
        self.test()   

    def test(self):
        # Denominator must not be zero
        while self.den == 0:
            print("Denominator cannot be zero")
            self.den = int(input("Enter denominator again: "))

    def __str__(self):
        # Print as rational number (e.g., "2 / 3")
        return f"{self.num} / {self.den}"

    def add(self, a, b):
        # (a.num * b.den + b.num * a.den) / (a.den * b.den)
        self.num = a.num * b.den + b.num * a.den
        self.den = a.den * b.den
        self.simplify()

    def sub(self, a, b):
        # (a.num * b.den - b.num * a.den) / (a.den * b.den)
        self.num = a.num * b.den - b.num * a.den
        self.den = a.den * b.den
        self.simplify()

    def mul(self, a, b):
        # (a.num * b.num) / (a.den * b.den)
        self.num = a.num * b.num
        self.den = a.den * b.den
        self.simplify()

    def div(self, a, b):
        # Division by zero check
        if b.num == 0:
            self.num = 1
            self.den = 0  # represent invalid division
        else:
            # (a.num * b.den) / (a.den * b.num)
            self.num = a.num * b.den
            self.den = a.den * b.num
            self.simplify()

    def simplify(self):
        # Simplify only if numerator is non-zero
        if self.num != 0 and self.den != 0:
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
