Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''

# Suppose Triangle class is already defined in prog5a and imported here

t = Triangle()                             
Triangle.get(t)                         
Triangle.test(t)                  
print("Area :", Triangle.area(t))  
print("Perimeter :", Triangle.peri(t)) 


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
a . m1()
a . m2()
print(a . x)
print(self . x)
print(x)






'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
# Program to add two objects and store results in third object

class Test:
    def get(self):
        # Read inputs into object variables
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))
        self.z = int(input("Enter z: "))

    def add(self, m, n):
        # Add objects m and n, store results in current object (self)
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z

    def disp(self):
        # Print object values
        print("x =", self.x, " y =", self.y, " z =", self.z)


# End of class

# Create three objects
a = Test()
b = Test()
c = Test()

print("First Object")
a.get()   # read values into object a

print("Second Object")
b.get()   # read values into object b

# Add objects a and b, store in c
c.add(a, b)

print("Addition Results")
c.disp()

'''
#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)

'''

#  Find  outputs (Home  work)
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
    def _str_(self , x):
        return f'{x}'
# end of the class

a = c1()
b = c2()
c = c3()
d = c4()

print(a)              # <__main__.c1 object at 0x...>
print(b)              # <__main__.c2 object at 0x...>
print(c)              # <__main__.c3 object at 0x...>
print(d)              # <__main__.c4 object at 0x...>

print(b._str_())      # 35
print(c._str_())      # Hyd
                      # None
print(d._str_(50))    # 50


'''
Program to determine total, average and grade of a student
Inputs: Roll Number, Student Name, Marks of 3 subjects, and Gender
'''

class Student:
    def get(self):
        # Read inputs into object self
        self.roll = int(input("Enter Roll Number: "))
        self.name = input("Enter Student Name: ")
        self.gender = input("Enter Gender (M/F): ")
        self.m1 = int(input("Enter Marks of Subject 1: "))
        self.m2 = int(input("Enter Marks of Subject 2: "))
        self.m3 = int(input("Enter Marks of Subject 3: "))

    def compute(self):
        # Calculate total and average
        self.total = self.m1 + self.m2 + self.m3
        self.avg = self.total / 3

        # Determine grade
        if self.m1 < 40 or self.m2 < 40 or self.m3 < 40:
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
        # Display results
        print("Roll Number :", self.roll)
        print("Student Name:", self.name)
        print("Gender      :", self.gender)
        print("Total Marks :", self.total)
        print("Average     :", self.avg)
        print("Grade       :", self.grade)

    def _str_(self):
        # Return all values as string
        return f"Roll: {self.roll}, Name: {self.name}, Gender: {self.gender}, Total: {self.total}, Average: {self.avg}, Grade: {self.grade}"


# End of class

# Create Student object
s = Student()

# Read inputs
s.get()

# Compute results
s.compute()

# Print using disp() method
print("\n--- Student Report (disp) ---")
s.disp()

# Print using _str_() method
print("\n--- Student Report (_str_) ---")
print(s._str_())



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
        self.test()   # validate denominator

    def test(self):
        while self.den == 0:
            print("Denominator cannot be zero. Re-enter:")
            self.den = int(input("Enter denominator: "))

    def _str_(self):
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
            self.num, self.den = 1, 0   # mark invalid division
        else:
            self.num = a.num * b.den
            self.den = a.den * b.num
            self.simplify()

    def simplify(self):
        if self.num == 0:
            return  # keep 0 / q form
        g = math.gcd(self.num, self.den)
        self.num //= g
        self.den //= g
# End of class


# Create 6 objects
a, b, c, d, e, f = Rat(), Rat(), Rat(), Rat(), Rat(), Rat()

print("Enter first rational number:")
a.get()

print("Enter second rational number:")
b.get()

# Perform operations
c.add(a, b)
d.sub(a, b)
e.mul(a, b)
f.div(a, b)

# Display results
print("Sum        :", c._str_())
print("Difference :", d._str_())
print("Product    :", e._str_())

if f.den == 0:   # division invalid
    print("Division is not permitted")
else:
    print("Division   :", f._str_())
