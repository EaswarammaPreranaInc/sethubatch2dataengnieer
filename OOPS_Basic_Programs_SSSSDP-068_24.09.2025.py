'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
from sep23 import triangle 
# How  to  create  triangle  object
a=triangle()
# How  to  call  get()  method  in  another  way
triangle.get(a)
# How  to  call  test()  method  in  another  way
triangle.test(a)
# print('Area : ',  How  to  call  area()  method  in  another  way)
print("Area:", triangle.area(a))
# print('Perimeter: ',  How  to  call  peri()  method  in  another  way)
print("Perimeter:", triangle.peri(a))


#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x)  #  10
		print(self . x)  #  20
		x += 5
		self . x += 7
	def   m2(self):
		print(x)  #  Error due to x is not defined
		print(self . x)  #  27
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x)  #  33
print(self . x)  #  Error due to self is not defined
print(x)  #  Error due to x is not defiened



'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''

class Test:
    def get(self):
        self.x = int(input("Enter x value : "))
        self.y = int(input("Enter y value : "))
        self.z = int(input("Enter z value : "))
        return self.x, self.y, self.z   # storing in object variables
    def add(self, m, n):
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z   # storing sum in current object
    def disp(self):
        print("x =", self.x, " y =", self.y, " z =", self.z) 
# End of the class
a = Test()
b = Test()
c = Test()   # creating 3 objects
print('First Object')
a.get()   # reading into object 'a'
print('Second Object')
b.get()   # reading into object 'b'
c.add(a, b)  # add a and b, store results in 'c'
print('Addition results')
c.disp()   # printing object 'c'



#  Find  outputs (Home  work)
class   c1:
	def  __str__(self):
			return  '25'
class   c2:
	def  __str__(self):
			return   35
class   c3:
	def  __str__(self):
			print('Hyd')
class   c4:
	def  __str__(self , x):
			return   F'{x}'
#end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a)  #  25
print(b)  #  Error due __str__ accepts only str
print(c)  #  Hyd
print(d)  #  Error due to x is not defined
print(b . __str__())  #  35
print(c . __str__())  #  Hyd prints  returns None
print(d . __str__(50))  #  50



'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self.no=int(input("Enter Roll No : ")) # How  to  read  roll  number  into  object  self
		self.name=input("Enter student name : " )  #  How  to  read  student  name  into  object  self
		self.g=input("Enter Gener M/F : " )  # How  to  read  gender  into  object  self
		self.marks=list(map(int, input("Enter list of marks maths,Elecctronics,Computers : ").split())) #  How  to  read  marks  of  3  subjects
	def compute(self):
		self.total=sum(self.marks)  #  How  to  calculate  total  marks
		self.avg=self.total/3  #  How  to  calculate  average  marks
		if  self.marks[0] < 40 or self.marks[1] < 40 or self.marks[2] < 40:
			self.grade = "Fail"  #  How  to  initilaize  grade  to  'Fail'
		elif  self.avg >= 70:
			self.grade = "Distinction"  #  How  to  initilaize  grade  to  'Distinction'
		elif  self.avg>=60 and self.avg<70:  #  average  is  above  >= 60%:
			self.grade = "First Class" #  How  to  initilaize  grade  to  'First  class'
		elif  self.avg>=50 and self.avg<60:  #  average  is  above  >= 50%:
			self.grade = "Second Class"  #  How  to  initilaize  grade  to  'Second  class'
		else:
			self.grade = "Third Class"#  How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   self.no)
		print('Student  Name  :  ' , self.name)
		print('Gender  :  ' ,  self.g)
		print('Total  Marks  :  ' , self.total)
		print('Average  :  ' , self.avg)
		print('Grade  :  ' , self.grade)
	def   _str_(self):
		return f'Roll Number : {self.no}\nStudent Name : {self.name}\nGender : {self.g}\nTotal Marks : {self.total}\nAverage : {self.avg}\nGrade : {self.grade}'

#End  of  the  class
# How  to  create  Student  class  object
a=Student()
# How  to  read  inputs  into  object
a.get()
# How  to  store  results  in  object
a.compute()
# How  to  print  object  with  disp()  method
a.disp()
# How  to  print  object  with  _str_()  method
print(a)



