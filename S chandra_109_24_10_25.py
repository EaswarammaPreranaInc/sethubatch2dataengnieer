#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		How  to   read  number
		How  to   read  name
		How  to   read   age
		How  to   read   gender
	def   disp(self):
		How  to  print  number , name , age , gender  in  same  line  separated  by  tab
	@abstractmethod
	def   compute(self):
                pass
class  student(person):
	def  get(self):
		How  to  read   number , name , age , gender
		How  to  read  marks  of  3  subjects  into  a  list
	def  compute(self):
		How  to  calculate  total  marks
		How  to  calculate  average  marks
	def  disp(self):
		How  to  print  number , name , age , gender
		How  to  print  total  and  average  in  same  line separated  by  tab
class  teacher(person):
	def   get(self):
		How  to  read  number , name , age  and  gender
		How  to  read   subject
		How  to  read   salary
		How  to  read   city
	def   compute(self):
		da = 50%  of  salary
		hra = 20%  of  salary
		cca = 1000  if  employee  lives  in  'Hyd'  and  800  otherwise
		How  to  calculate  grosspay  i.e. salary + da + hra + cca
		pf = 8%  of  grosspay  but  a  max  of  400
		tax = 10%  of  grosspay  if  grosspay is  < 10000  and  15%  otherwise
		How  to  calculate  netpay  i.e. grosspay - pf - tax
	def   disp(self):
		How  to  print  number , name , age , gender
		How  to  print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
def  menu():
	print('1. Teacher')
	print('2. Student')
	print('3. Exit')
# End  of  the  function
a = []
while  True:
	menu()
	ch = eval(input('Enter choice : '))
	if   ch == 1:
			How  to  append  teacher  object  to  list  'a'
	elif  ch == 2:
			How  to  append  student  object  to  list  'a'
	else:
			How  to  stop  execution
	How  to  read  inputs  into  object
	How  to  store   results  in  object
	How  to  move  to  next  index
	menu()
	ch = eval(input('Enter choice : '))
#end of loop
print('Teachers')
How  to  print  all  teacher  objects
print()
print('Students')
How  to  print  all  student  objects
print('Good  Bye')
############################
# Base class
class Person:
    def __init__(self, number, name, age, gender):
        self.number = number
        self.name = name
        self.age = age
        self.gender = gender

    def display_person(self):
        print(f"Number: {self.number}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

# Derived class - Teacher
class Teacher(Person):
    def __init__(self, number, name, age, gender, subject, salary):
        super().__init__(number, name, age, gender)
        self.subject = subject
        self.salary = salary
        self.gross_pay = self.salary + (0.10 * self.salary) + (0.05 * self.salary)  # Example: DA + HRA
        self.net_pay = self.gross_pay - (0.08 * self.gross_pay)  # Example: deductions

    def display_teacher(self):
        self.display_person()
        print(f"Subject: {self.subject}")
        print(f"Salary: {self.salary}")
        print(f"Gross Pay: {self.gross_pay:.2f}")
        print(f"Net Pay: {self.net_pay:.2f}")

# Derived class - Student
class Student(Person):
    def __init__(self, number, name, age, gender, marks):
        super().__init__(number, name, age, gender)
        self.marks = marks
        self.total = sum(marks)
        self.average = self.total / len(marks)

    def display_student(self):
        self.display_person()
        print(f"Marks: {self.marks}")
        print(f"Total: {self.total}")
        print(f"Average: {self.average:.2f}")

# Example usage
t1 = Teacher(101, "Ravi", 40, "Male", "Math", 50000)
print("Teacher Details:")
t1.display_teacher()

print("\nStudent Details:")
s1 = Student(201, "Sita", 18, "Female", [85, 90, 95])
s1.display_student()





#####################################
#  Write  a  progran  to  add  num  class  objects  and  join  str  class  objects
from  abc  import  abstractmethod , ABC
class   datatype(ABC):
	@abstractmethod
	def  get(self):
		 pass
	@abstractmethod
	def  add(self , m ,  n):
		pass
	@abstractmethod
	def  display(self):
		pass
class   number(datatype):
	def  get(self):
			How  to  read  number  into  variable  'x' of  object  self
	def  add(self , m , n):
			How  to  add  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Sum  of  the  numbers  :  ' , How  to  print  sum  result)
class   string(datatype):
	def  get(self):
			How  to  read  string  into  variable  'x' of  object  self
	def  add(self , m , n):
			How  to  join  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Join  of  the  two  strings :  ' , How  to  print  the   join  result)
def   menu():
	print('1. Add  numbers')
	print('2. Join  Strings')
	print('3. Exit')
# End  of  the  function
if  _name_ == '_main_':
	while  True:
			menu()
			ch =  eval(input('Enter choice : '))
			if   ch == 1:
					How  to  create  list  of  3  number  class  objects
			elif  ch  == 2:
					How  to  create  list  of  3  string  class  objects
			else:
					How  to  stop  execution
			How  to  read  input  into  first  object
			How  to  read  input  into  2nd  object
			How  to  add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
			How  to  print  3rd  object
	# end of  while  loop
	print('Good  Bye')

################################

# Base class
class Datatype:
    def get(self):
        pass

    def add(self):
        pass

    def disp(self):
        pass


# Derived class for Numbers
class Number(Datatype):
    def get(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))

    def add(self):
        self.result = self.a + self.b

    def disp(self):
        print("Sum of numbers =", self.result)


# Derived class for Strings
class String(Datatype):
    def get(self):
        self.a = input("Enter first string: ")
        self.b = input("Enter second string: ")

    def add(self):
        self.result = self.a + self.b

    def disp(self):
        print("Concatenated string =", self.result)


# Example usage
print("=== Number Addition ===")
n = Number()
n.get()
n.add()
n.disp()

print("\n=== String Concatenation ===")
s = String()
s.get()
s.add()
s.disp()


