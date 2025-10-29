from py_HW.Class_0075_24_09 import triangle

my_triangle = triangle()
my_triangle.get()
my_triangle.test()
print('The area is:', my_triangle.area())
print('The perimeter is:', my_triangle.peri())




#Find  outputs (Home  work)
class   c1:
	def  m1(self):
		x = 10             #local variable
		self . x = 20      #instance variable
		print(x)           #10
		print(self . x)    #20
		x += 5            #local variable 15
		self . x += 7     #instance variable 27
	def   m2(self):
		print(x)          #name 'x' is not defined
		print(self . x)   #27
		self . x += 6     #instance variable 33
# End  of  the  class
a = c1()
a . m1()                  #10 20
a . m2()                  #name 'x' is not defined 27
print(a . x)              #33
print(self . x)           #33
print(x)            #name 'x' is not defined


'''(Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class Test:
    def get(self):
        # How to read inputs into variables x, y and z of object self
        print('Enter values for the object:')
        self.x = int(input('Enter value for x: '))
        self.y = int(input('Enter value for y: '))
        self.z = int(input('Enter value for z: '))
        
    def add(self, m, n):
        # How to add objects m and n and store results in object self
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z

    def disp(self):
        # How to print object self
        print(f"x: {self.x}, y: {self.y}, z: {self.z}")

# End of the class
# How to create three Test class objects a, b and c
a = Test()
b = Test()
c = Test()
print('First Object')
a.get()# How to read inputs into object 'a'
print('Second Object')
b.get()# How to read inputs into object 'b'
c.add(a, b)# How to add objects a and b and store results in object 'c'
print('Addition results')
c.disp()# How to print object 'c'




#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) #<__main__.Date object at some address>



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
print(a)#'25'
print(b)#error cannot return any other value except string
print(c)#Hyd
print(d)#error missing 1 required positional argument: 'x'
print(a . _str_())#'25'
print(b . _str_())#35
print(c . _str_())#Hyd
print(d . _str_(50))#'50'



class Student:
    def get(self):
        self.roll_no = input('Enter Roll Number: ')# How to read roll number into object self
        self.name = input('Enter Student Name: ')# How to read student name into object self
        self.gender = input('Enter Gender: ')# How to read gender into object self
        # How to read marks of 3 subjects
        self.sub1 = float(input('Enter marks for subject 1: '))
        self.sub2 = float(input('Enter marks for subject 2: '))
        self.sub3 = float(input('Enter marks for subject 3: '))

    def compute(self):
        self.total = self.sub1 + self.sub2 + self.sub3# How to calculate total marks
        self.average = self.total / 3# How to calculate average marks

        # At least one subject is below 40
        if self.sub1 < 40 or self.sub2 < 40 or self.sub3 < 40:
            # How to initialize grade to 'Fail'
            self.grade = 'Fail'
        # average is above >= 70%
        elif self.average >= 70:
            # How to initialize grade to 'Distinction'
            self.grade = 'Distinction'
        # average is above >= 60%
        elif self.average >= 60:
            # How to initialize grade to 'First class'
            self.grade = 'First class'
        # average is above >= 50%
        elif self.average >= 50:
            # How to initialize grade to 'Second class'
            self.grade = 'Second class'
        else:
            # How to initialize grade to 'Third class'
            self.grade = 'Third class'

    def disp(self):
        print('Roll Number : ', self.roll_no)
        print('Student Name : ', self.name)
        print('Gender : ', self.gender)
        print('Total Marks : ', self.total)
        print('Average : ', self.average)
        print('Grade : ', self.grade)

    def __str__(self):
        # All the values of object self in the form of a string
        return f"Roll Number: {self.roll_no}, Name: {self.name}, Gender: {self.gender}, Total: {self.total}, Average: {self.average:.2f}, Grade: {self.grade}"

# End of the class

s = Student()     # How to create a Student class object
s.get()           # How to read inputs into object
s.compute()       # How to store results in object
s.disp()          # How to print object with disp() method
print(s)          # How to print object with __str__() method



import math

class Rat:
    def get(self):
        # How to read numerator into object self
        self.num = int(input('Enter numerator: '))
        # How to read denominator into object self
        self.den = int(input('Enter denominator: '))
        # How to call test() method
        self.test()

    def test(self):
        # Ask user to reenter denom when denom is zero
        while self.den == 0:
            print('Denominator cannot be zero. Please re-enter.')
            self.den = int(input('Enter a new denominator: '))

    def __str__(self):
        # return values of object in the form of a rational number such as '2 / 3'
        return f"{self.num} / {self.den}"

    def add(self, a, b):
        # How to add objects 'a' and 'b' and store results in object self
        self.num = a.num * b.den + b.num * a.den
        self.den = a.den * b.den
        # How to simplify object self
        self.simplify()

    def sub(self, a, b):
        # How to subtract objects 'a' and 'b' and store results in object self
        self.num = a.num * b.den - b.num * a.den
        self.den = a.den * b.den
        # How to simplify object self
        self.simplify()

    def mul(self, a, b):
        # How to multiply objects 'a' and 'b' and store results in object self
        self.num = a.num * b.num
        self.den = a.den * b.den
        # How to simplify object self
        self.simplify()

    def div(self, a, b):
        # How to divide objects 'a' and 'b' and store results in object self
        if b.num != 0:
            self.num = a.num * b.den
            self.den = a.den * b.num
            # How to simplify object self
            self.simplify()
        else:
            self.num = a.num
            self.den = 0

    def simplify(self):
        # When simplification is required? ---> When numerator is non-zero
        if self.num != 0:
            # How to find gcd of numerator and denominator
            common = math.gcd(self.num, self.den)
            # How to simplify rational number in object self
            self.num //= common
            self.den //= common

# End of the class

# How to create 6 objects a, b, c, d, e, f
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()

print('--- First Rational Number ---')
a.get()# How to read rational number into object 'a'


print('\n--- Second Rational Number ---')
b.get()# How to read rational number into object 'b'


c.add(a, b)# How to add rational numbers in objects a and b and store results in object 'c'
d.sub(a, b)# How to subtract rational numbers in objects a and b and store results in object 'd'
e.mul(a, b)# How to multiply rational numbers in objects a and b and store results in object 'e'
f.div(a, b)# How to divide rational numbers in objects a and b and store results in object 'f'


print(f"Sum: {c}")
print(f"Difference: {d}")
print(f"Product: {e}")

# If the denominator of the second number is non-zero
if f.den != 0:
    # How to print object 'f'
    print(f"Division: {f}")
else:
    print('Division is not permitted')