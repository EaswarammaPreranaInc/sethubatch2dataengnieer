#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from abc import *
class person(ABC):
    def get(self):
        self.number=int(input('Enter a number:'))
        self.name=input('Enter a name:')
        self.age=int(input('Enter age:'))
        self.gender=input('Enter gender:')
    def disp(self):
        print(f'{self.number}\t{self.name}\t{self.age}\t{self.gender}',end='\t')
    @abstractmethod
    def compute(self):
        pass
class student(person):
    def get(self):
        super().get()
        print('Enter marks of 3 subjects:')
        self.marks=[float(input(f'subject {i+1}:')) for i in range(3)]
    def compute(self):
        self.total=sum(self.marks)
        self.average=self.total/len(self.marks)
    def disp(self):
        super().disp()
        print(f"{self.total}\t{self.average:.2f}")
class teacher(person):
    def get(self):
        super().get()
        self.subject = input("Enter subject: ")
        self.salary = float(input("Enter salary: "))
        self.city = input("Enter city: ")
    def compute(self):
        da = 0.5 * self.salary
        hra = 0.2 * self.salary
        if self.city.lower() == 'hyd':
            cca = 1000
        else:
            cca = 800
        self.grosspay = self.salary + da + hra + cca
        pf = 0.08 * self.grosspay
        if pf > 400:
            pf = 400
        if self.grosspay < 10000:
            tax = 0.10 * self.grosspay
        else:
            tax = 0.15 * self.grosspay
        self.netpay = self.grosspay - pf - tax
    def disp(self):
        super().disp()
        print(f"{self.subject}\t{self.salary}\t{self.grosspay:.2f}\t{self.netpay:.2f}")
def menu():
    print('1.Teacher')
    print('2.Student')
    print('3.Exit')
a=[]
while True:
    menu()
    choice=eval(input('Enter your choice:'))
    if choice==1:
        c=teacher()
    elif choice==2:
        c=student()
    elif choice==3:
        break
    else:
        print('Invalid choice')
        continue
    c.get()
    c.compute()
    a.append(c)
print('Teachers')
for i in a:
    if isinstance(i,teacher):
        i.disp()
print()
print('Students')
for i in a:
    if isinstance(i,student):
        i.disp()
print('Good Bye')

#  Write  a  progran  to  add  num  class  objects  and  join  str  class  objects
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
        self.x = float(input("Enter a number: "))
    def add(self, m, n):
        self.x = m.x + n.x
    def display(self):
        print("Sum of the numbers:", self.x)        
class string(datatype):
    def get(self):
        self.x = input("Enter a string: ")
    def add(self, m, n):
        self.x = m.x + n.x                          
    def display(self):
        print("Join of the two strings:", self.x)   
def menu():
    print("\n1. Add numbers")
    print("2. Join Strings")
    print("3. Exit")
if __name__ == '__main__':
    while True:
        menu()
        ch = int(input("Enter choice: "))
        if ch == 1:
            a = [number(), number(), number()]     
        elif ch == 2:
            a = [string(), string(), string()]      
        elif ch == 3:
            break                                   
        else:
            print("Invalid choice!")
            continue
        a[0].get()
        a[1].get()
        a[2].add(a[0], a[1])
        a[2].display()
    print("Good Bye")
