#1st Program
#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		self.num=int(input("Enter number: "))#How  to   read  number
		self.name=input("Enter name: ")#How  to   read  name
		self.age=int(input("Enter age: "))#How  to   read   age
		self.gender=input("Enter gender: ")#How  to   read   gender
	def   disp(self):
		print(self.num,self.name,self.age,self.gender,sep="\t",end="/t")#How  to  print  number , name , age , gender  in  same  line  separated  by  tab
	@abstractmethod
	def   compute(self):
                pass
class  student(person):
	def  get(self):
		super().get()#How  to  read   number , name , age , gender
		self.lst=[]
		for i in range(3):
			a=float(input(f"Enter marks {i+1}: "))
			self.lst.append(a)#How  to  read  marks  of  3  subjects  into  a  list
	def  compute(self):
		self.total=sum(self.lst)#How  to  calculate  total  marks
		self.avg=self.total/3 #How  to  calculate  average  marks
	def  disp(self):
		super().disp()#How  to  print  number , name , age , gender
		print(self.total,self.avg,sep="/t")#How  to  print  total  and  average  in  same  line separated  by  tab
class  teacher(person):
	def   get(self):
		super().get()#How  to  read  number , name , age  and  gender
		self.subject=input("Enter any subject: ")#How  to  read   subject
		self.sal=float(input("Enter salary: "))#How  to  read   salary
		self.city=input("Enter city: ")#How  to  read   city
	def   compute(self):
		da = 0.5 *  self.sal
		hra = 0.2 *  self.sal
		if  self.city == 'Hyd'  :
			cca = 1000  
		else:
			cca = 800
		self.grosspay=self.sal + da+hra +cca 
		if self.grosspay * 0.08  < 400:
			pf = 0.08 * self.grosspay
		else:
			pf = 400
		if self.grosspay < 10000:
			tax = 0.1 * self.grosspay
		else:
			tax = 0.15 * self.grosspay
		self.netpay=self.grosspay - pf - tax 
	def   disp(self):
		super().disp()#How  to  print  number , name , age , gender
		print(self.subject,self.sal,self.grosspay,self.netpay,sep="/t")#How  to  print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
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
			a.append(teacher())#How  to  append  teacher  object  to  list  'a'
	elif  ch == 2:
			a.append(student())#How  to  append  student  object  to  list  'a'
	else:
			exit()#How  to  stop  execution
	a[-1].get()#How  to  read  inputs  into  object
	a[-1].compute()#How  to  store   results  in  object
#end of loop
print('Teachers')
for x in a:
	if isinstance(x,teacher):
		x.disp()#How  to  print  all  teacher  objects
print()
print('Students')
if isinstance(x,student):
		x.disp()#How  to  print  all  student  objects
print('Good  Bye')


#2nd Program
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
        self.x = int(input("Enter a number: "))  

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
    print("1. Add numbers")
    print("2. Join strings")
    print("3. Exit")

#  Main program
if __name__ == "__main__":
    while True:
        menu()
        ch = int(input("Enter choice: "))  

        if ch == 1:
            a = [number(), number(), number()]   
        elif ch == 2:
            a = [string(), string(), string()] 
        else:
            break  #  Stop execution

        a[0].get() 
        a[1].get()  
        a[2].add(a[0], a[1])  
        a[2].display()  