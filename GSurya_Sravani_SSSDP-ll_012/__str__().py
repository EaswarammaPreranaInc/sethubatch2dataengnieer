'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
from prog5a import triangle 
a=triangle()How  to  create  triangle  object
n=a.get()How  to  call  get()  method  in  another  way
p=b.test()How  to  call  test()  method  in  another  way
print('Area : ', n)# How  to  call  area()  method  in  another  way)
print('Perimeter: ',p)#  How  to  call  peri()  method  in  another  way)



#  Find  outputs  (Home  work)
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
a . m1()#10
20
a . m2()#error
20
print(a . x)#26
print(self . x)#error
print(x)#error




#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)#__str__()is invoked and type and address is printed



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
print(a)#__str__()is invoked and type and address is printed
print(b)#__str__()is invoked and type and address is printed
print(c)#__str__()is invoked and type and address is printed
print(d)#__str__()is invoked and type and address is printed
print(b . __str__())#35
print(c . __str__())#hyd
print(d . __str__(50))#50





'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class Test:
    def get(self):
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))
        self.z = int(input("Enter z: "))

    def add(self, m, n):
        # add fields of objects m and n, store in self
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z

    def disp(self):
        print(f"x = {self.x}, y = {self.y}, z = {self.z}")


# Create 3 objects
a = Test()
b = Test()
c = Test()

print("Enter values for 1st object:")
a.get()

print("Enter values for 2nd object:")
b.get()

# Add a and b → store in c
c.add(a, b)

print("Result stored in 3rd object:")
c.disp()



'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self.x=int(input("enter roll number")How  to  read  roll  number  into  object  self
		self.name=input("enter student name:)#How  to  read  student  name  into  object  self
		self.gender=input("enter gender:")How  to  read  gender  into  object  self
		self.m1=eval(input("enter marks of 1st sub:")#How  to  read  marks  of  3  subjects
                self.m2=eval(input("enter marks of 2nd sub:")
                self.m3=eval(input("enter marks of 3rd sub: ")
	def   compute(self,m,n,p):
		self.sum=m.m1+n.m2+p.m3 #How  to  calculate  total  marks
		self.avg=sum/3How  to  calculate  average  marks
		if m1 or m2 or m3 <  40:
				 'Fail')
		elif  self.avg   >= 70:
				self.d='Distinction'
		elif  self.avg >= 60:
				self.d= 'First  class'
		elif  self.avg>= 50%:
				self.d=  'Second  class'
		else:
				self.d=  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' self.x   )
		print('Student  Name  :  self.name)
		print('Gender  :  ' ,self.gender)
		print('Total  Marks  :  ' ,self.sum )
		print('Average  :  ' ,self.avg )
		print('Grade  :  ' , self.d)
	def   __str__(self):
		return  F'{self.x}{self.name} {self.gender} {self.sum} {self.avg} {self.d}'
#End  of  the  class
s=student()#How  to  create  Student  class  object
s.get()#How  to  read  inputs  into  object
How  to  store  results  in  object
print(s.disp())#How  to  print  object  with  disp()  method
print(s.__str__())#How  to  print  object  with  __str__()  method


















