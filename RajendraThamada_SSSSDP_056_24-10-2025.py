
#1
from abc import *

class person(ABC):
    def get(self):
        self.num = int(input("Enter the number:"))
        self.name = input("Enter the name:")
        self.age = int(input("Enter age:"))
        self.gender = input("Enter gender m/f:")

    def disp(self):
        print(self.num, self.name, self.age, self.gender, end='\t')

    @abstractmethod
    def compute(self):
        pass

class student(person):
    def get(self):
        super().get()
        # Read marks of 3 subjects into a list
        self.marks = []
        for i in range(3):
            m = int(input(f"Enter marks for subject {i+1}:"))
            self.marks.append(m)

    def compute(self):
        # Calculate total and average of marks
        self.total = sum(self.marks)
        self.avg = self.total / 3

    def disp(self):
        super().disp()
        print(self.total, self.avg, sep='\t')

class teacher(person):
    def get(self):
        super().get()
        self.subject = input("Enter subject:")
        self.salary = float(input("Enter salary:"))
        self.city = input("Enter city:")

    def compute(self):
        # da = 50% of salary
        da = 0.5 * self.salary
        # hra = 20% of salary
        hra = 0.2 * self.salary
        # cca = 1000 if city is 'Hyd', else 800
        cca = 1000 if self.city.lower() == 'hyd' else 800
        # grosspay = salary + da + hra + cca
        self.grosspay = self.salary + da + hra + cca
        # pf = 8% of grosspay but max 400
        pf = 0.08 * self.grosspay
        self.pf = pf if pf < 400 else 400
        # tax = 10% if grosspay < 10000, else 15%
        if self.grosspay < 10000:
            self.tax = 0.10 * self.grosspay
        else:
            self.tax = 0.15 * self.grosspay
        # netpay = grosspay - pf - tax
        self.netpay = self.grosspay - self.pf - self.tax

    def disp(self):
        super().disp()
        print(self.subject, self.salary, self.grosspay, self.netpay, sep='\t')

def menu():
    print("1. Teacher")
    print("2. Student")
    print("3. Exit")

a = []
while True:
    menu()
    ch = int(input("Enter choice : "))
    if ch == 1:
        obj = teacher()
    elif ch == 2:
        obj = student()
    else:
        break
    obj.get()
    obj.compute()
    a.append(obj)

print("Teachers")
for obj in a:
    if isinstance(obj, teacher):
        obj.disp()
print()
print("Students")
for obj in a:
    if isinstance(obj, student):
        obj.disp()
print("Good Bye")






#2
from abc import ABC, abstractmethod

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
        self.x = int(input("Enter a number:"))

    def add(self, m, n):
        self.x = m.x + n.x

    def display(self):
        print('Sum of the numbers :', self.x)

class string(datatype):
    def get(self):
        self.x = input("Enter string:")

    def add(self, m, n):
        self.x = m.x + n.x

    def display(self):
        print('Join of the two strings :', self.x)

def menu():
    print('1. Add numbers')
    print('2. Join Strings')
    print('3. Exit')

if __name__ == '__main__':
    while True:
        menu()
        ch = int(input("Enter choice : "))
        if ch == 1:
            a = [number() for _ in range(3)]  # list of 3 number objects
        elif ch == 2:
            a = [string() for _ in range(3)]  # list of 3 string objects
        else:
            print('Good Bye')
            break
        a[0].get()  # read 1st input
        a[1].get()  # read 2nd input
        a[2].add(a[0], a[1])  # perform add/join and store result in 3rd
        a[2].display()  # print 3rd object (result)
