'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
How  to  create  triangle  object
How  to  call  get()  method  in  another  way
How  to  call  test()  method  in  another  way
print('Area : ',  How  to  call  area()  method  in  another  way)
print('Perimeter: ',  How  to  call  peri()  method  in  another  way)

######################

# Suppose prog5a already had this class:
class Triangle:
    def get(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def test(self):
        return (self.a + self.b > self.c and 
                self.b + self.c > self.a and 
                self.c + self.a > self.b)

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def peri(self):
        return self.a + self.b + self.c


# Reuse class without redefining
t = Triangle()

# Two ways of calling
Triangle.get(t, 3, 4, 5)   # classname.method(object, args)
print("Valid triangle:", Triangle.test(t))
print("Area:", Triangle.area(t))
print("Perimeter:", Triangle.peri(t))

###output:-
Valid triangle: True
Area: 6.0
Perimeter: 12

2) Find outputs – c1 class


class c1:
    def m1(self):
        x = 10
        self.x = 20
        print(x)         # 10
        print(self.x)    # 20
        x += 5           # local x becomes 15
        self.x += 7      # self.x becomes 27

    def m2(self):
        print(x)         #  ERROR: x is not defined (local x of m1 not visible here)
        print(self.x)
        self.x += 6

a = c1()
a.m1()
a.m2()        # will crash here




'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		 How  to  read  inputs  into  variables  x , y  and  z  of  object  self
	def   add(self , m , n):
		 How  to  add  objects  m  and  n  and  store  results  in  object  self
	def  disp(self):
		 How  to  print  object  self
# End  of  the  class
How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
How  to  read  inputs  into  object  'a'
print('Second  Object')
How  to  read  inputs  into  object  'b'
How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
How  to  print  object  'c'

###############################
class Test:
    def get(self):
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))
        self.z = int(input("Enter z: "))

    def add(self, m, n):
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z

    def disp(self):
        print(f"x = {self.x}, y = {self.y}, z = {self.z}")


a = Test()
b = Test()
c = Test()

print("First Object")
a.get()
print("Second Object")
b.get()

c.add(a, b)

print("Addition Results")
c.disp()


 If you enter (10,20,30) and (40,50,60), output:

x = 50, y = 70, z = 90


#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)
######################
<__main__.Date object at 0x000001B5E4F0>






class c1:
    def __str__(self):
        return '25'   #  string ok

class c2:
    def __str__(self):
        return 35    #  must return str → TypeError

class c3:
    def __str__(self):
        print('Hyd') # prints but returns None → TypeError

class c4:
    def __str__(self, x):  #  wrong signature, Python expects only (self)
        return f'{x}'

a = c1()
b = c2()
c = c3()
d = c4()

print(a)   # prints 25
print(b)   # crash here (TypeError: __str__ returned non-string)



'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		How  to  read  roll  number  into  object  self
		How  to  read  student  name  into  object  self
		How  to  read  gender  into  object  self
		How  to  read  marks  of  3  subjects
	def   compute(self):
		How  to  calculate  total  marks
		How  to  calculate  average  marks
		if  At  least  one  subject  is  below  40:
				How  to  initilaize  grade  to  'Fail'
		elif  average  is  above  >= 70%:
				How  to  initilaize  grade  to  'Distinction'
		elif  average  is  above  >= 60%:
				How  to  initilaize  grade  to  'First  class'
		elif  average  is  above  >= 50%:
				How  to  initilaize  grade  to  'Second  class'
		else:
				How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   ???)
		print('Student  Name  :  ' , ???)
		print('Gender  :  ' ,  ???)
		print('Total  Marks  :  ' , ???)
		print('Average  :  ' , ???)
		print('Grade  :  ' , ???)
	def   _str_(self):
		return  All  the   values  of  object  self  in  the  form  of  string
#End  of  the  class
How  to  create  Student  class  object
How  to  read  inputs  into  object
How  to  store  results  in  object
How  to  print  object  with  disp()  method
How  to  print  object  with  _str_()  method


##############################

class Student:
    def get(self):
        self.roll = int(input("Enter Roll Number: "))
        self.name = input("Enter Name: ")
        self.gender = input("Enter Gender: ")
        self.marks = [int(input(f"Enter mark {i+1}: ")) for i in range(3)]

    def compute(self):
        self.total = sum(self.marks)
        self.avg = self.total / 3
        if any(m < 40 for m in self.marks):
            self.grade = "Fail"
        elif self.avg >= 70:
            self.grade = "Distinction"
        elif self.avg >= 60:
            self.grade = "First class"
        elif self.avg >= 50:
            self.grade = "Second class"
        else:
            self.grade = "Third class"

    def disp(self):
        print("Roll Number :", self.roll)
        print("Student Name:", self.name)
        print("Gender :", self.gender)
        print("Total Marks:", self.total)
        print("Average:", self.avg)
        print("Grade:", self.grade)

    def __str__(self):
        return f"{self.roll}, {self.name}, {self.gender}, {self.total}, {self.avg}, {self.grade}"


s = Student()
s.get()
s.compute()
s.disp()
print(s)   # calls __str__




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
import  math
class  Rat:
	def  get(self):
		How  to  read  numerator  into  object  self
		How  to  read  denominator  into  object  self
		How  to  call  test()  method
	def  test(self):
		Ask  user  to  reenter  denom  when  denom  is  zero
	def    _str_(self):
			 return  values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	def   add(self , a , b):
		How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
		How  to  simplify  object  self
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		How  to  subtract  objects  'a'  and  'b' and  store  results  in  object  self
		How  to  simplify  object  self
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  self
		How  to  simplify  object  self
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		How  to  divide  objects  'a'  and  'b' and  store  results  in  object  self
		How  to  simplify  object  self
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
			How  to  find  gcd  of  numerator  and   denominator
			How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
How  to  create  6  objects  a , b , c , d , e , f
How  to  read  rational  number  into  object  'a'
How to  read  rational  number  into  object  'b'
How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
How  to  print  object   'c'
How  to  print  object   'd'
How  to  print  object   'e'
if  ???
	How  to  print  object  'f
else:
	print('Division  is  not  permitted')

##########################

import math

class Rat:
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))
        self.test()

    def test(self):
        while self.den == 0:
            print("Denominator cannot be zero.")
            self.den = int(input("Re-enter denominator: "))

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
            self.num = 1
            self.den = 0   # invalid fraction
        else:
            self.num = a.num * b.den
            self.den = a.den * b.num
            self.simplify()

    def simplify(self):
        if self.num != 0:
            g = math.gcd(self.num, self.den)
            self.num //= g
            self.den //= g


# Main program
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()

print("Enter first rational number")
a.get()
print("Enter second rational number")
b.get()

c.add(a, b)
d.sub(a, b)
e.mul(a, b)
f.div(a, b)

print("Sum =", c)
print("Difference =", d)
print("Product =", e)
if f.den != 0:
    print("Division =", f)
else:
    print("Division is not permitted")









