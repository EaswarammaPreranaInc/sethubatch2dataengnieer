Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
How  to  create  triangle  object                                                                   t=Triangle()
How  to  call  get()  method  in  another  way                                                      Triangle.get(t)
How  to  call  test()  method  in  another  way                                                     Triangle.test(t)
print('Area : ',  How  to  call  area()  method  in  another  way)                                  Triangle.area(t)
print('Perimeter: ',  How  to  call  peri()  method  in  another  way)                              Triangle.peri(t)

#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x)                                                     10
		print(self . x)                                              20
		x += 5
		self . x += 7
	def   m2(self):
		print(x)                                                     Error
		print(self . x)                                              27
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x)                                                     33
print(self . x)                                                  Error
print(x)                                                         Error

Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object
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
print("Addition results")
c.disp()

#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)                                                 <__main__.Date object at 0x76344ee93530>

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
print(a)                                        <__main__.c1 object at 0x7b52c1415d30>
print(b)                                        <__main__.c2 object at 0x7b52c1415b80>
print(c)                                        <__main__.c3 object at 0x7b52c1415ac0>
print(d)                                        <__main__.c4 object at 0x7b52c1415af0>
print(b . _str_())                              35
print(c . _str_())                              Hyd
                                                None
print(d . _str_(50))                            50

Write a program to determine total , average and grade of a student Inputs are Roll Number , Stud Name , Marks of 3 subjects and Gender
class Student:
    def get(self):
        self.roll = int(input("Enter Roll Number: "))
        self.name = input("Enter Student Name: ")
        self.gender = input("Enter Gender (M/F): ")
        self.marks = []   
        for i in range(1, 4):
            mark = int(input(f"Enter marks of subject {i}: "))
            self.marks.append(mark)
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
        print("Roll Number : ", self.roll)
        print("Student Name : ", self.name)
        print("Gender : ", self.gender)
        print("Total Marks : ", self.total)
        print("Average : ", self.avg)
        print("Grade : ", self.grade)
    def __str__(self):
        return (f"Roll Number: {self.roll}, "
                f"Name: {self.name}, "
                f"Gender: {self.gender}, "
                f"Total: {self.total}, "
                f"Average: {self.avg:.2f}, "
                f"Grade: {self.grade}")
s = Student()
print("Enter Student Details:")
s.get()        
s.compute()    
print("\n--- Using disp() ---")
s.disp()
print("\n--- Using __str__() ---")
print(s)

Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers
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
        if b.num == 0:   # division not possible
            self.num, self.den = None, None
        else:
            self.num = a.num * b.den
            self.den = a.den * b.num
            self.simplify()
    def simplify(self):
        if self.num != 0:  
            gcd = math.gcd(self.num, self.den)
            self.num //= gcd
            self.den //= gcd
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
d.sub(a, b)
e.mul(a, b)
f.div(a, b)
print("\nResults:")
print("Sum        :", c)
print("Difference :", d)
print("Product    :", e)
if f.num is None:  
    print("Division   : Division is not permitted")
else:
    print("Division   :", f)
