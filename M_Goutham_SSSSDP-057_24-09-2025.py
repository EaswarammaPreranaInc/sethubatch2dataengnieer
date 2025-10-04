'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''

a = Triangle() #How  to  create  triangle  object
Triangle.get(a)  #How  to  call  get()  method  in  another  way
if Triangle.test(a): #How  to  call  test()  method  in  another  way
	print('Area : ',Triangle.area(a))  # How  to  call  area()  method  in  another  way
	print('Perimeter: ',Triangle.peri(a)) #How  to  call  peri()  method  in  another  way


#  Find  outputs  (Home  work)
class   c1: #Here we are creating the class with name c1
	def  m1(self): #Here we are defining the m1 method in c1 class
		x = 10 #Here x is a local variable of m1 method
		self . x = 20 #Here we are adding the instance variable x with value 20 
		print(x) #printing the x i.e 10
		print(self . x) #Printing the instance varible of obj i,e 20
		x += 5 #Here we are incrementing the value of local variable x i.e 10 to 15
		self . x += 7 #Here we are incrementing the value of instance variable x i.e 20 to 27
	def   m2(self): #Here we are defining another method in c1 class m2
		#print(x) #Error #There is no x is defined in m2 method
		print(self . x) #27
		self . x += 6 #27+6 i.e 33
# End  of  the  class
a = c1() #Here we are creating the obj for c1 class
a . m1() #Here we are calling the m1 method with obj a 
a . m2() #Here we are calling the m2 method with obj a 
print(a . x) #33
#print(self . x) #Error #as we have creating the obj with ref a and we are using with self
#print(x) #Error There is no global x 



'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class Test:
    def get(self):
        self.x = int(input("Enter value for x: "))
        self.y = int(input("Enter value for y: "))
        self.z = int(input("Enter value for z: ")) #How to read inputs into variables x , y and z of object self

    def add(self, m, n):
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z #How to add objects m and n and store results in object self

    def disp(self):
        print("x =", self.x)
        print("y =", self.y)
        print("z =", self.z) #How to print object self

a = Test() #how to create three Test class objects a , b and c 
b = Test() #how to create three Test class objects a , b and c 
c = Test() #how to create three Test class objects a , b and c

print("Enter values for First Object:") #How to read inputs into object 'a'
a.get()

print("Enter values for Second Object:") #How to read inputs into object 'b'
b.get()

c.add(a, b) #How to add objects a and b and store results in object 'c'

print("Addition results:")
c.disp()

'''outputs:
Enter values for First Object:
Enter value for x: 3
Enter value for y: 4
Enter value for z: 5
Enter values for Second Object:
Enter value for x: 1
Enter value for y: 2
Enter value for z: 3
Addition results:
x = 4
y = 6
z = 8
'''


#  Find  outputs (Home  work)
class  Date: #Here we are creating the class with name Date
	pass #We are not creating any methods in the class
# End of the class
a =  Date() #Here we are creating the obj for Date class
a . dd = 15 #Here we are adding instance varible dd into obj a with value 15
a . mm = 8  #Here we are adding instance varible mm into obj a with value 8
a . yy = 1947 #Here we are adding instance varible yy into obj a with value 1947
print(a) #Prints the type and address as we know that when we say print(object) it will call ___str___ is executed



#  Find  outputs (Home  work)
class   c1: #Here we have defined the class with name c1
	def  ___str___(self): #Here we have defined the __str__ method
			return  '25' 
class   c2: #Here we have defined the class with name c2
	def  __str__(self): #Here we have defined the __str__ method
			return   35 #Error #as we have to return only string obj
class   c3: #Here we have defined the class with name c3
	def  __str__(self): #Here we have defined the __str__ method
			print('Hyd') #Error as we should only return string obj
class   c4: #Here we have defined the class with name c4
	def  __str__(self , x): #Here we have defined the __str__ method
			return   F'{x}' 
#end of the class
a = c1() #Here we are creating the obj for c1 class
b = c2() #Here we are creating the obj for c2 class
c = c3() #Here we are creating the obj for c3 class
d = c4() #Here we are creating the obj for c4 class
print(a) #Prints the type and address
#print(b) #Error #as we have to return only string obj
#print(c) #Error #as we have to return only string obj
#print(d) #Error #argument for x is missing
print(b . __str__()) #35
print(c . __str__()) #Hyd 
					 #None
print(d . __str__(50)) #50




'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self.roll_no = int(input("Enter the roll number: ")) #How  to  read  roll  number  into  object  self
		self.student_name = input("Enter the name: ") #How  to  read  student  name  into  object  self
		self.gender = input("Enter the Gender(M/F): ") #How  to  read  gender  into  object  self
		self.sub = []
		for i in range(3):
			self.marks = int(input(f"Enter marks for subject {i+1}: "))
			self.sub.append(self.marks)
	def   compute(self):
		self.Total = sum(self.sub) #How  to  calculate  total  marks
		self.average = self.Total / 3 #How  to  calculate  average  marks
		if  min(self.sub) < 40: #At  least  one  subject  is  below  40:
				self.grade = 'Fail' #How  to  initilaize  grade  to  'Fail'
		elif  self.average >= 70: #average  is  above  >= 70%
				self.grade = 'Distinction' #How  to  initilaize  grade  to  'Distinction'
		elif  self.average >= 60:	#average  is  above  >= 60%:
				self.grade = 'First  class' #How  to  initilaize  grade  to  'First  class'
		elif  self.average >= 50: #average  is  above  >= 50%:
				self.grade = 'Second  class' #How  to  initilaize  grade  to  'Second  class'
		else:
				self.grade = 'Third  class' #How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' , self.roll_no)
		print('Student  Name  :  ' , self.student_name)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.Total)
		print('Average  :  ' , self.average)
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		return  f"Roll No: {self.roll_no}, Name: {self.student_name}, Gender: {self.gender}, Total: {self.Total}, Average: {self.average:.2f}, Grade: {self.grade}" #All  the   values  of  object  self  in  the  form  of  string
#End  of  the  class
a = Student() #How  to  create  Student  class  object
a.get() #How  to  read  inputs  into  object
a.compute() #How  to  store  results  in  object
a.disp() #How  to  print  object  with  disp()  method
print(a) #How  to  print  object  with  __str__()  method

'''outputs:
Enter the roll number: 34
Enter the name: goutham
Enter the Gender(M/F): M
Enter marks for subject 1: 34
Enter marks for subject 2: 44
Enter marks for subject 3: 44
Roll  Number  :   34
Student  Name  :   goutham
Gender  :   M
Total  Marks  :   122
Average  :   40.666666666666664
Grade  :   Fail
Roll No: 34, Name: goutham, Gender: M, Total: 122, Average: 40.67, Grade: Fail
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
        self.nr = int(input("Enter the numerator: "))
        self.dr = int(input("Enter the denominator: "))
        self.test()  # Check denominator validity

    def test(self):
        while self.dr == 0:
            print("Denominator cannot be zero.")
            self.dr = int(input("Please reenter the denominator: "))

    def __str__(self):
        return f"{self.nr} / {self.dr}"

    def add(self, a, b):
        self.nr = a.nr * b.dr + b.nr * a.dr
        self.dr = a.dr * b.dr
        self.simplify()

    def sub(self, a, b):
        self.nr = a.nr * b.dr - b.nr * a.dr
        self.dr = a.dr * b.dr
        self.simplify()

    def mul(self, a, b):
        self.nr = a.nr * b.nr
        self.dr = a.dr * b.dr
        self.simplify()

    def div(self, a, b):
        if b.nr == 0:
            self.nr = None
            self.dr = None
        else:
            self.nr = a.nr * b.dr
            self.dr = a.dr * b.nr
            self.simplify()

    def simplify(self):
        if self.nr != 0:
            gcd = math.gcd(self.nr, self.dr)
            self.nr //= gcd
            self.dr //= gcd
        # If numerator is 0, denominator remains as is; no simplification needed

# End of class

# Create 6 objects
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()

# Read rational numbers
print("\nEnter first rational number (a):")
a.get()
print("\nEnter second rational number (b):")
b.get()

# Perform operations
c.add(a, b)
d.sub(a, b)
e.mul(a, b)
f.div(a, b)

# Print results
print(f"\nSum: {c}")
print(f"Difference: {d}")
print(f"Product: {e}")

if f.nr is not None and f.dr != 0:
    print(f"Division: {f}")
else:
    print("Division is not permitted.")

'''output:
Enter first rational number (a):
Enter the numerator: 6
Enter the denominator: 8

Enter second rational number (b):
Enter the numerator: 6
Enter the denominator: 9

Sum: 17 / 12
Difference: 1 / 12
Product: 1 / 2
Division: 9 / 8

'''
