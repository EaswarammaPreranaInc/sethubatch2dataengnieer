                                NAME:M.SAICHARAN              HOMEWORK
                                DATE:11-10-2025

1.# Find  outputs (Home work)
class  Person:
	def  __init__(self):
		self . name  =  ''
	@property
	def   name(self):
		print('getter  method')
		return  self . _name
	@name . setter
	def   name(self , value):
		print('Setter  Method')
		self . _name = value
	@name . deleter
	def  name(self):
		print('Deleter  method ')
		del  self .  _name
#end  of  the  class
p = Person()
print(p . name)
p . name = 'Vamsi'
print(p . name)
del   p . name
#print(p . name)
del   p

#Output:
Setter  Method
getter  method

Setter  Method
getter  method
Vamsi
Deleter  method 


'''
2.#
1) Write  a  program  to  validate  emp  number , emp  name  and  salary  and  also  print  them

2) Emp  number  and  salary  can  not  be  -ve

3) Emp  name  can  not  be  empty  string

4) class  name   is  Emp

5) 3  getter  and  3  setter  methods

6) Constructor  initializes  empno , ename  and  sal

7) Outside  the  class
    ----------------------
    a) Create  Emp  class  object
    b) Print  empno , ename  and  sal
'''
Enter  employee  number :  -25
Empno cannot be negative

Enter  employee  number :  25
Enter  employee  name :
Emp  name cannot be empty  string

Enter  employee  number :  25
Enter  employee  name :  Vamsi
Enter  salary :  -20
Salary cannot be negative

Enter  employee  number :  25
Enter  employee  name :  Vamsi
Enter  salary :  10000.0
Employee number  :  25
Employee name  :  Vamsi
Employee salary :   10000.0
#Program:
class Emp:
    def __init__(self, empno, ename, sal):
        self.set_empno(empno)
        self.set_ename(ename)
        self.set_sal(sal)
    def set_empno(self, empno):
        if empno < 0:
            raise ValueError("Empno cannot be negative")
        self.__empno = empno
    def set_ename(self, ename):
        if ename == "":
            raise ValueError("Emp name cannot be empty string")
        self.__ename = ename
    def set_sal(self, sal):
        if sal < 0:
            raise ValueError("Salary cannot be negative")
        self.__sal = sal
    def get_empno(self):
        return self.__empno
    def get_ename(self):
        return self.__ename
    def get_sal(self):
        return self.__sal
while True:
    try:
        empno = int(input("Enter employee number : "))
        ename = input("Enter employee name : ")
        sal = float(input("Enter salary : "))

        e = Emp(empno, ename, sal)

        print("Employee number :", e.get_empno())
        print("Employee name :", e.get_ename())
        print("Employee salary :", e.get_sal())
        break

    except ValueError as ve:
        print(ve)
        print()


3.#  Write  functions  to  create  and  print  linked  list
class  node:
		def   __init__(self , x):
				self . data = x
				self . link = None
		#   new  = node(25)
class  linked_list:
		def   __init__(a):
				a . first = None
		#  a = linked_list()
		def  isempty(a):
				return  a . first == None
		# a . isempty()  --->  True / False
		def  disp(a):
				if  a . isempty():
						print('Linked  List  is  empty')
				else:
						p = a . first
						while  p  !=  None:
								print(p . data , end = '\t')
								p = p . link
						print()
		def  append(a , new):
				if   a . isempty():
						a . first = new
				else:
						last = a . first
						while  last . link != None:
								last = last . link
						last . link = new
		def  create(a):
				try:
						a . first = None
						print('Enter  values  terminated  by  ctrl+z')
						while  True:
								x = eval(input())
								new = node(x)
								a . append(new)
				except:
						pass
# End  of  the  class
if  __name__ == '__main__':
	a = linked_list()
	a . create()
	print('Linked  List  :  ' , end = '')
	a . disp()


#Program:
class node:
    def __init__(self, x):
        self.data = x
        self.link = None
class linked_list:
    def __init__(self):
        self.first = None

    def isempty(self):
        return self.first is None

    def disp(self):
        if self.isempty():
            print("Linked List is empty")
        else:
            p = self.first
            while p is not None:
                print(p.data, end='\t')
                p = p.link
            print()

    def append(self, new):
        if self.isempty():
            self.first = new
        else:
            last = self.first
            while last.link is not None:
                last = last.link
            last.link = new

    def create(self):
        try:
            self.first = None
            print("Enter values terminated by Ctrl+Z (Windows) or Ctrl+D (Linux/mac):")
            while True:
                x = eval(input())
                new = node(x)
                self.append(new)
        except:
            pass


# End of the class
if __name__ == "__main__":
    a = linked_list()
    a.create()
    print("Linked List :", end=' ')
    a.disp()
