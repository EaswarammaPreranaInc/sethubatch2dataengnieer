'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
import triangle_oops
t = triangle_oops.triangle()#How  to  create  triangle  object
triangle_oops.triangle.get(t)#How  to  call  get()  method  in  another  way
triangle_oops.triangle.test(t)#How  to  call  test()  method  in  another  way
print('Area : ',triangle_oops.area(t)) # How  to  call  area()  method  in  another  way)
print('Perimeter: ', triangle_oops.peri(t) )#How  to  call  peri()  method  in  another  way)

#Find outputs(Home work)
class c1:
    def m1(self):
        x = 10
        self.x = 20
        print(x)# 10
        print(self.x)# 20
        x += 5# x = 15
        self.x += 7# self.x = 27
    def m2(self):
        print(x)# error (x is not defined globally)
        print(self.x)# prints current self.x if above error commented
        self.x += 6# self.x = self.x + 6
# End of the class
a = c1()
a.m1()# prints 10 and 20
a.m2()# error
print(a.x)# would print 27 (if m2 ran without error)
print(self.x)# error (self is not defined globally)
print(x)# error (x is not defined globally)

'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		 #How  to  read  inputs  into  variables  x , y  and  z  of  object  self
         self . x = int(input('Enter x: '))
	def   add(self , m , n):
		    ##How  to  add  objects  m  and  n  and  store  results  in  object  self
            self . x = m . x + n . x
            self . y = m . y + n . y
            self . z = m . z + n . z        
	def  disp(self):
		    #How  to  print  object  self
            print('x =', self . x)
            print('y =', self . y)
            print('z =', self . z)
# End  of  the  class
#How  to  create  three  Test  class  objects  a , b  and  c
a = Test()
b = Test()  
c = Test()
#print('First  Object')
print(a)
#How  to  read  inputs  into  object  'a'
a . get()
#print('Second  Object')
print(b)
#How  to  read  inputs  into  object  'b'
b . get()
#How  to  add  objects  a  and  b  and  store  results in  object  'c'
c . add(a , b)
print('Addition  results')
#How  to  print  object  'c'
c . disp()

# Find outputs (Home work)
class Date:
    pass
# End of the class

a = Date()
a.dd = 15
a.mm = 8
a.yy = 1947
print(a)# <__main__.Date object at ...>
# Output: default object representation, e.g., <__main__.Date object at 0x7f...>

# Find outputs (Home work)
class c1:
    def _str_(self):
        return '25'
class c2:
    def _str_(self):
        return 35
class c3:
    def _str_(self):
        print('Hyd')
class c4:
    def _str_(self, x):
        return F'{x}'
# end of the class

a = c1()
b = c2()
c = c3()
d = c4()
print(a)# <__main__.c1 object at ...>
print(b)# <__main__.c2 object at ...>
print(c)# <__main__.c3 object at ...>
print(d)# <__main__.c4 object at ...>
print(b._str_())# 35
print(c._str_())# Hyd, followed by None
print(d._str_(50))  # 50


'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class Student:
    def get(self):
        # How to read roll number into object self
        self.roll = input("Enter roll number: ")
        # How to read student name into object self
        self.name = input("Enter student name: ")
        # How to read gender into object self
        self.gender = input("Enter gender: ")
        # How to read marks of 3 subjects
        self.marks = []
        for i in range(1, 4):
            m = float(input(f"Enter marks of subject {i}: "))
            self.marks.append(m)

    def compute(self):
        # How to calculate total marks
        self.total = sum(self.marks)
        # How to calculate average marks
        self.average = self.total / 3
        # At least one subject is below 40
        if any(m < 40 for m in self.marks):
            self.grade = "Fail"
        elif self.average >= 70:
            self.grade = "Distinction"
        elif self.average >= 60:
            self.grade = "First class"
        elif self.average >= 50:
            self.grade = "Second class"
        else:
            self.grade = "Third class"

    def disp(self):
        print("Roll Number  : ", self.roll)
        print("Student Name : ", self.name)
        print("Gender       : ", self.gender)
        print("Total Marks  : ", self.total)
        print("Average      : ", self.average)
        print("Grade        : ", self.grade)

    def __str__(self):
        # return all values of object self in the form of string
        return (f"Roll Number: {self.roll}, Name: {self.name}, Gender: {self.gender}, "
                f"Total: {self.total}, Average: {self.average}, Grade: {self.grade}")
# How to create Student class object
stu = Student()
# How to read inputs into object
stu.get()
# How to store results in object
stu.compute()
# How to print object with disp() method
stu.disp()
# How to print object with __str__() method
print(stu)

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
            print("Denominator cannot be zero, reenter:")
            self.den = int(input("Enter denominator: "))

    def __str__(self):
        return f"{self.num} / {self.den}"

    def simplify(self):
        gcd = math.gcd(self.num, self.den)
        if self.num != 0:    
            self.num //= gcd
            self.den //= gcd

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
            self.num = 0
            self.den = 1
            self.division_valid = False
        else:
            self.num = a.num * b.den
            self.den = a.den * b.num
            self.division_valid = True
            self.simplify()
# Create 6 objects a,b,c,d,e,f
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()
# Read rational numbers into objects 'a' and 'b'
print("Enter 1st rational number:")
a.get()
print("Enter 2nd rational number:")
b.get()

c.add(a, b)# Add a and b, store result in c
d.sub(a, b)#Subtract a and b, store result in d
e.mul(a, b)# Multiply a and b, store result in e
f.div(a, b)# Divide a and b, store result in f
# Print objects c, d, e
print("Sum :", c)
print("Difference :", d)
print("Product :", e)
# Print object f or division error message
if getattr(f, 'division_valid', True):
    print("Division :", f)
else:
    print("Division is not permitted")




