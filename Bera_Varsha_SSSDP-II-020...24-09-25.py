'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
# from prog5a import *
# t=triangle()# How  to  create  triangle  object
# triangle.get(t)# How  to  call  get()  method  in  another  way
# triangle.test(t)# How  to  call  test()  method  in  another  way
# print('Area : ', triangle.area(t))# print('Area : ',  How  to  call  area()  method  in  another  way)
# print('Perimeter: ',  triangle.peri(t))# print('Perimeter: ',  How  to  call  peri()  method  in  another  way)
'''
Enter side a:5
Enter side b:6
Enter side c:7
Area :  14.696938456699069
Perimeter :  9.0
'''

#  Find  outputs  (Home  work)
# class   c1:
# 	def  m1(self):
# 		x = 10
# 		self . x = 20
# 		print(x)
# 		print(self . x)
# 		x += 5
# 		self . x += 7
# 	def   m2(self):
# 		# print(x)error
# 		print(self . x)
# 		self . x += 6
# # End  of  the  class
# a = c1()
# a . m1()
# a . m2()
# print(a . x)
## print(self . x)#name 'self' is not defined
## print(x)#x is not defined
'''
output:
10
20
27
33
'''
'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
# class  Test:
# 	def   get(self):
# 		#  How  to  read  inputs  into  variables  x , y  and  z  of  object  self
# 		self.x=float(input("enter x value: "))
# 		self.y=float(input("enter y value: "))
# 		self.z=float(input("enter z value: "))
# 	def   add(self , m , n):
# 		#  How  to  add  objects  m  and  n  and  store  results  in  object  self
# 		self.x=m.x +n.x
# 		self.y=m.x+n.y
# 		self.z=m.x+n.y
# 	def  disp(self):
# 		# How  to  print  object  self
# 		print(f"x={self.x}, y={self.y}, z= {self.z}")
# # End  of  the  class
# # How  to  create  three  Test  class  objects  a , b  and  c
# a = Test()
# b=Test()
# c=Test()
# print('First  Object')
# # How  to  read  inputs  into  object  'a'
# a.get()
# print('Second  Object')
# # How  to  read  inputs  into  object  'b'
# b.get()
# # How  to  add  objects  a  and  b  and  store  results in  object  'c'
# c.add(a,b)
# print('Addition  results')
# # How  to  print  object  'c'
# c.disp()
'''
# output:
First  Object
enter x value: 10
enter y value: 20
enter z value: 30
Second  Object
enter x value: 40
enter y value: 50
enter z value: 60
Addition  results
x=50.0, y=60.0, z= 60.0
'''
#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
# print(a)#<__main__.Date object at 0x00000205605F8510>

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
print(a)
print(b)
print(c)
print(d)
print(b . _str_())
print(c . _str_())
print(d . _str_(50))
'''
# output:
<__main__.c1 object at 0x00000262699FA150>
<__main__.c2 object at 0x00000262699F9250>
<__main__.c3 object at 0x00000262699FA190>
<__main__.c4 object at 0x00000262699FA1D0>
35
Hyd
None
50
'''
'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self.roll_no =int(input("Enter a roll number: "))# How  to  read  roll  number  into  object  self
		self.stud_name=input("Enter student name: ")# How  to  read  student  name  into  object  self
		self.gender=input("Enter gender: ")# How  to  read  gender  into  object  self
		self.s1=float(input("Enter the marks of s1: "))# How  to  read  marks  of  3  subjects
		self.s2=float(input("Enter the marks of s2: "))
		self.s3=float(input("Enter the marks of s3: "))
	def   compute(self):
		self.total=self.s1+self.s2+self.s3# How  to  calculate  total  marks
		self.avg=self.total/3# How  to  calculate  average  marks
		if self.s1 < 40 or self.s2 < 40 or self.s3 < 40:#At  least  one  subject  is  below  40
			self.grade='Fail'# How  to  initilaize  grade  to  'Fail'
		elif  self.avg>=70:#average  is  above  >= 70%:
			self.grade='Distinction'#How  to  initilaize  grade  to  'Distinction'
		elif  self.avg>=60:#average  is  above  >= 60%:
			self.grade='First  class'#How  to  initilaize  grade  to  'First  class'
		elif  self.avg>=50:#average  is  above  >= 50%:
			self.grade='Second  class'#How  to  initilaize  grade  to  'Second  class'
		else:
			self.grade='Third Class'#How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   self.roll_no)
		print('Student  Name  :  ' , self.stud_name)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.total)
		print('Average  :  ' , self.avg)
		print('Grade  :  ' , self.grade)
	def   _str_(self):
		#return  All  the   values  of  object  self  in  the  form  of  string
		return (f"Roll Number: {self.roll_no}, "
                f"Student Name: {self.stud_name}, "
                f"Gender: {self.gender}, "
                f"Total Marks: {self.total}, "
                f"Average: {self.avg}, "
                f"Grade: {self.grade}")
#End  of  the  class
s=Student()# How  to  create  Student  class  object
s.get()# How  to  read  inputs  into  object
s.compute()# How  to  store  results  in  object
s.disp()# How  to  print  object  with  disp()  method
print(s)# How  to  print  object  with  _str_()  method
'''
# output:
Enter a roll number: 1
Enter student name: varsha
Enter gender: female
Enter the marks of s1: 90
Enter the marks of s2: 80
Enter the marks of s3: 70
Roll  Number  :   1
Student  Name  :   varsha
Gender  :   female
Total  Marks  :   240.0
Average  :   80.0
Grade  :   Distinction
<__main__.Student object at 0x000001473F8FAB10>
'''

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
import math

class Rat:
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))
        self.test()

    def test(self):
        while self.den == 0:
            print("Denominator cannot be zero. Please re-enter.")
            self.den = int(input("Enter denominator: "))

    def __str__(self):
        return f"{self.num} / {self.den}"

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
        if b.num == 0:
            self.num = None
            self.den = None
        else:
            self.num = a.num * b.den
            self.den = a.den * b.num
            self.simplify()

    def simplify(self):
        if self.num != 0 and self.num is not None:
            g = math.gcd(self.num, self.den)
            self.num //= g
            self.den //= g

a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()

print("Enter first rational number:")
a.get()
print("Enter second rational number:")
b.get()

c.add(a, b)
print("Sum:", c)

d.sub(a, b)
print("Difference:", d)

e.mul(a, b)
print("Product:", e)

f.div(a, b)
if f.num is None:
    print("Division is not permitted")
else:
    print("Division:", f)
