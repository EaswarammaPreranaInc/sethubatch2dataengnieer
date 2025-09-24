q)Repeat  prog5a  such  that  methods  are  called  in  another  way
1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)
2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
Ans) import prog5a
a = prog5a.triangle()  # How  to  create  triangle  object
prog5a.triangle.get(a)  # How  to  call  get()  method  in  another  way
prog5a.triangle.test(a)  # How  to  call  test()  method  in  another  way
print('Area : ', prog5a.triangle.area(a)) # print('Area : ',  How  to  call  area()  method  in  another  way)
print('Perimeter : ', prog5a.triangle.peri(a)) # print('Perimeter: ',  How  to  call  peri()  method  in  another  way)

class c1:
    def m1(self):
        x = 10
        self.x = 20
        print(x)         # 10
        print(self.x)    # 20
        x += 5           # local x becomes 15
        self.x += 7      # self.x becomes 27
    def m2(self):
        print(x)         # Error: no x in m2 
        print(self.x)    # 27
        self.x += 6      # self.x becomes 33
a = c1()
a.m1()
a.m2()
print(a.x)               # 33
print(self.x)            # Error: self not defined outside class
print(x)                 # Error: x not defined globally

q) Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object
1st  object   --->  x = 10 , y = 20 , z = 30
2nd  object --->  x = 40 , y = 50 , z = 60
3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
Ans) class  Test:
    def get(self):
        self.x = float(input('Enter value of x: '))
        self.y = float(input('Enter value of y: '))
        self.z = float(input('Enter value of z: ')) # How  to  read  inputs  into  variables  x , y  and  z  of  object  self
    def add(self, m, n):
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z # How  to  add  objects  m  and  n and  store  results  in  object  self
    def disp(self):
        print(self.x, self.y, self.z, sep='\n') # How  to  print  object  self 
	# End  of  the  class 
a = Test()  
b = Test()  
c = Test() # How  to  create  three  Test  class  objects  a , b  and  c
print('First Object')
a.get()  # How  to  read  inputs  into  object  'a'
print('Second Object')
b.get()  # How  to  read  inputs  into  object  'b'
c.add(a, b)  # How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition results')
c.disp()  #How  to  print  object 'c'

class Date:
    pass
# End of the class
a = Date()
a.dd = 15
a.mm = 8
a.yy = 1947
print(a)  # <__main__.Date object at 0xXXXXXXXX>  # type and address of date class

#  Find  outputs (Home  work)
class c1:
    def __str__(self): 
        return '25'
class c2:
    def __str__(self): 
        return 35
class c3:
    def __str__(self): 
        print('Hyd')
class c4:
    def __str__(self , x): 
        return F'{x}'
# end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a)               # 25  # c1.__str__() returns string
print(b)              # Error: c2.__str__() returned non-string (int)
print(c)          # Hyd  # printed inside c3.__str__() method
                      # Error because c3.__str__() does not return non string
print(d)          # Error: c4.__str__() missing 1 required positional argument: 'x'
print(b.__str__())    # 35  # calling method directly works
print(c.__str__())    # Hyd  # printed inside method
                                # None  # because __str__ does not return anything
print(d.__str__(50))   # 50  # calling with argument works

q) Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
Ans) class Student:
    def get(self):
        self.rollno = int(input('Enter Roll Number: '))  # How to read roll number into object self
        self.name = input('Enter Student Name: ')        # How to read student name into object self
        self.gender = input('Enter Gender (M/F): ')      # How to read gender into object self
        self.m1 = float(input('Enter marks of subject 1: ')) 
        self.m2 = float(input('Enter marks of subject 2: '))
        self.m3 = float(input('Enter marks of subject 3: '))  # How to read marks of 3 subjects
    def compute(self):
        self.total = self.m1 + self.m2 + self.m3              # How to calculate total marks
        self.avg = self.total / 3                             # How to calculate average marks
        if self.m1 < 40 or self.m2 < 40 or self.m3 < 40:
            self.grade = 'Fail'  # How  to  initilaize  grade  to  'Fail'
        elif self.avg >= 70:
            self.grade = 'Distinction'  # How  to  initilaize  grade  to  'Distinction'
        elif self.avg >= 60:
            self.grade = 'First class'  # How  to  initilaize  grade  to  'First  class'
        elif self.avg >= 50:
            self.grade = 'Second class'  # How  to  initilaize  grade  to  'Second  class'
        else:
            self.grade = 'Third class'  # How  to  initilaize  grade  to  'First  class'
    def disp(self):
        print('Roll  Number  :  ', self.rollno)              
        print('Student  Name  :  ', self.name)               
        print('Gender  :  ', self.gender)                    
        print('Total  Marks  :  ', self.total)               
        print('Average  :  ', self.avg)                      
        print('Grade  :  ', self.grade)                      
    def _str_(self):
        return f'{self.rollno = } {self.name = } {self.gender = } {self.total = } {self.avg = } {self.grade = }'  
        # All the values of object self in the form of string
#End of the class
s = Student()  # How to create Student class object
s.get()  # How to read inputs into object
s.compute()  # How to store results in object
s.disp()  # How to print object with disp() method
print(s._str_())  # How to print object with _str_() method

q) Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers
Ans) import math
class Rat:
    def get(self):
        self.num = int(input('Enter numerator: '))       # How to read numerator into object self
        self.den = int(input('Enter denominator: '))     # How to read denominator into object self
        self.test()                                      # How to call test() method
    def test(self):
        while self.den == 0:                             # Ask user to reenter denom when denom is zero
            print('Denominator cannot be zero.')
            self.den = int(input('Re-enter denominator: '))
    def _str_(self):
        return f'{self.num} / {self.den}'               # values of object in the form of rational number
    def simplify(self):
        g = math.gcd(self.num, self.den)               # find gcd of numerator and denominator
        self.num //= g                                 # simplify numerator
        self.den //= g                                 # simplify denominator
    def add(self, a, b):
        self.num = a.num * b.den + b.num * a.den       # How to add objects a and b
        self.den = a.den * b.den
        self.simplify()                                # How to simplify object self
    def sub(self, a, b):
        self.num = a.num * b.den - b.num * a.den       # How to subtract objects a and b
        self.den = a.den * b.den
        self.simplify()                                # How to simplify object self
    def mul(self, a, b):
        self.num = a.num * b.num                        # How to multiply objects a and b
        self.den = a.den * b.den
        self.simplify()                                # How to simplify object self
    def div(self, a, b):
        if b.num != 0:
            self.num = a.num * b.den                    # How to divide objects a and b
            self.den = a.den * b.num
            self.simplify()                            # How to simplify object self
        else:
            self.num = None                             # Division not permitted
            self.den = None
# End of the class
a = Rat()              # How to create object a
b = Rat()              # How to create object b
c = Rat()              # How to create object c
d = Rat()              # How to create object d
e = Rat()              # How to create object e
f = Rat()              # How to create object f
print('First Rational Number')
a.get()                # How to read rational number into object 'a'
print('Second Rational Number')
b.get()                # How to read rational number into object 'b'
c.add(a, b)            # How to add rational numbers in objects a and b and store results in object 'c'
d.sub(a, b)            # How to subtract rational numbers in objects a and b and store results in object 'd'
e.mul(a, b)            # How to multiply rational numbers in objects a and b and store results in object 'e'
f.div(a, b)            # How to divide rational numbers in objects a and b and store results in object 'f'
print(c._str_())       # How to print object 'c' 
print(d._str_())       # How to print object 'd' 
print(e._str_())       # How to print object 'e' 
if f.num is not None:  # Check if division is valid
    print(f._str_())   # How to print object 'f' 
else:
    print('Division is not permitted')
