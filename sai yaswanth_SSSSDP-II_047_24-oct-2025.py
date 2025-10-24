# Write a program to determine total and average of student 
# and gross pay and net pay of teacher

from abc import *
class person(ABC):
	def get(self):
		self.number = int(input("Enter number: "))        # How to read number
		self.name = input("Enter name: ")                 # How to read name
		self.age = int(input("Enter age: "))              # How to read age
		self.gender = input("Enter gender: ")             # How to read gender

	def disp(self):
		print(self.number, self.name, self.age, self.gender, sep="\t")   # How to print number, name, age, gender in same line separated by tab

	@abstractmethod
	def compute(self):
		pass
class student(person):
	def get(self):
		super().get()                                      # How to read number, name, age, gender
		self.marks = []                                    # Create list for marks
		print("Enter marks of 3 subjects:")
		for i in range(3):
			self.marks.append(float(input(f"Mark {i+1}: ")))  # How to read marks of 3 subjects into a list

	def compute(self):
		self.total = sum(self.marks)                       # How to calculate total marks
		self.avg = self.total / 3                          # How to calculate average marks

	def disp(self):
		super().disp()                                     # How to print number, name, age, gender
		print(self.total, self.avg, sep="\t")              # How to print total and average in same line separated by tab


class teacher(person):
	def get(self):
		super().get()                                      # How to read number, name, age, gender
		self.subject = input("Enter subject: ")            # How to read subject
		self.salary = float(input("Enter salary: "))       # How to read salary
		self.city = input("Enter city: ")                  # How to read city

	def compute(self):
		da = 0.5 * self.salary                             # da = 50% of salary
		hra = 0.2 * self.salary                            # hra = 20% of salary
		cca = 1000 if self.city.lower() == 'hyd' else 800  # cca = 1000 if city is 'Hyd' else 800
		self.grosspay = self.salary + da + hra + cca        # How to calculate grosspay i.e. salary + da + hra + cca

		pf = 0.08 * self.grosspay                           # pf = 8% of grosspay
		if pf > 400:
			pf = 400                                       # But a max of 400

		if self.grosspay < 10000:
			tax = 0.1 * self.grosspay                      # tax = 10% if grosspay < 10000
		else:
			tax = 0.15 * self.grosspay                     # 15% otherwise

		self.netpay = self.grosspay - pf - tax              # How to calculate netpay i.e. grosspay - pf - tax

	def disp(self):
		super().disp()                                     # How to print number, name, age, gender
		print(self.subject, self.salary, self.grosspay, self.netpay, sep="\t")  # How to print subject, salary, grosspay, netpay in same line separated by tab


def menu():
	print("\n1. Teacher")
	print("2. Student")
	print("3. Exit")
# End of the function


# Main program
a = []
while True:
	menu()
	ch = int(input("Enter choice: "))

	if ch == 1:
		obj = teacher()                                   # How to append teacher object to list 'a'
	elif ch == 2:
		obj = student()                                   # How to append student object to list 'a'
	elif ch == 3:
		break                                             # How to stop execution
	else:
		print("Invalid choice!")
		continue

	obj.get()                                             # How to read inputs into object
	obj.compute()                                         # How to store results in object
	a.append(obj)                                         # How to move to next index

# End of loop
print("\nTeachers")
for i in a:
	if isinstance(i, teacher):
		i.disp()                                          # How to print all teacher objects

print("\nStudents")
for i in a:
	if isinstance(i, student):
		i.disp()                                          # How to print all student objects

print("\nGood Bye")







# Write a program to add num class objects and join str class objects
from abc import abstractmethod, ABC

class datatype(ABC):
	@abstractmethod
	def get(self):
		pass

	@abstractmethod
	def add(self, m, n):
		pass

	@abstractmethod
	def display(self):
		pass


class number(datatype):
	def get(self):
		self.x = int(input("Enter number: "))                     # How to read number into variable 'x' of object self

	def add(self, m, n):
		self.x = m.x + n.x                                        # How to add objects m and n and store result in object self

	def display(self):
		print("Sum of the numbers :", self.x)                     # How to print sum result


class string(datatype):
	def get(self):
		self.x = input("Enter string: ")                          # How to read string into variable 'x' of object self

	def add(self, m, n):
		self.x = m.x + n.x                                        # How to join objects m and n and store result in object self

	def display(self):
		print("Join of the two strings :", self.x)                # How to print the join result


def menu():
	print("\n1. Add numbers")
	print("2. Join Strings")
	print("3. Exit")
# End of the function


if __name__ == "__main__":
	while True:
		menu()
		ch = eval(input("Enter choice : "))

		if ch == 1:
			a = [number(), number(), number()]                    # How to create list of 3 number class objects
		elif ch == 2:
			a = [string(), string(), string()]                    # How to create list of 3 string class objects
		else:
			break                                                 # How to stop execution

		a[0].get()                                                # How to read input into first object
		a[1].get()                                                # How to read input into 2nd object
		a[2].add(a[0], a[1])                                      # How to add (or) join the two objects and store the result in 3rd object
		a[2].display()                                            # How to print 3rd object
	# end of while loop
	print("Good Bye")

