#Nanda Kishore Vemula

'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''

import trianglee
t=trianglee.triangle() #How  to  create  triangle  object
trianglee.triangle.get(t) #How  to  call  get()  method  in  another  way
trianglee.triangle.test(t) #How  to  call  test()  method  in  another  way
print('Area : ', trianglee.triangle.area(t)) #How  to  call  area()  method  in  another  way
print('Perimeter: ', trianglee.triangle.peri(t)) #How  to  call  peri()  method  in  another  way

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
		print(x) #Error
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x)
print(self . x) #Error
print(x) #Error
'''
10
20
27
33
'''
#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) #Type and Address of a


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
print(a)
print(b) #Error
print(c) #Error
print(d) #Error
print(b . __str__())
print(c . __str__())
print(d . __str__(50))
'''
25
35
Hyd
None
50
'''

'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		 self.x=int(input("Enter x : "))
		 self.y=int(input("Enter y : "))
		 self.z=int(input("Enter z : "))
        #How  to  read  inputs  into  variables  x , y  and  z  of  object  self
	def   add(self , m , n):
		 #How  to  add  objects  m  and  n  and  store  results  in  object  self
		 self.x=m.x+n.x
		 self.y=m.y+n.y
		 self.z=m.z+n.z
	def  disp(self):
		 print(F'x = {self.x}, y = {self.y}, z = {self.z}')#How  to  print  object  self
# End  of  the  class
a=Test()
b=Test()
c=Test()#How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
a.get()#How  to  read  inputs  into  object  'a'
print('Second  Object')
b.get()#How  to  read  inputs  into  object  'b'
c.add(a,b)#How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
c.disp()#How  to  print  object  'c'


'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self.rollno=int(input("Enter ROllNO : "))#How  to  read  roll  number  into  object  self
		self.name=input("Enter Name : ")#How  to  read  student  name  into  object  self
		self.gender=input("Enter Gender : ")#How  to  read  gender  into  object  self
		line=input("Enter marks of 3 subjects : ")
		list=line.split()
		self.marks=[]
		for i in list:
		    self.marks.append(eval(i))#How  to  read  marks  of  3  subjects
	def   compute(self):
		self.totalmarks=sum(self.marks)#How  to  calculate  total  marks
		self.avg=sum(self.marks)/len(self.marks)#How  to  calculate  average  marks
		if  self.marks[0] <40 or self.marks[1] <40 or self.marks[2] <40:
		    self.res='fail'# At  least  one  subject  is  below  40:
				#How  to  initilaize  grade  to  'Fail'
		elif  self.avg>= 70:
		    self.res='Distinction'
				# How  to  initilaize  grade  to  'Distinction'
		elif  self.avg  >= 60:
		    self.res='First  class'
				# How  to  initilaize  grade  to  'First  class'
		elif  self.avg  >= 50:
		    self.res='Second  class'
				# How  to  initilaize  grade  to  'Second  class'
		else:
		    self.res='Third  class'
				# How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   self.rollno)
		print('Student  Name  :  ' , self.name)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.totalmarks)
		print('Average  :  ' , self.avg)
		print('Grade  :  ' , self.res)
	def   __str__(self):
		return  F'RollNO : {self.rollno},Name : {self.name},Gender : {self.gender},Totalmarks : {self.totalmarks},Average : {self.avg},Grade : {self.res}'#All  the   values  of  object  self  in  the  form  of  string
#End  of  the  class
s=Student()#How  to  create  Student  class  object
s.get()#How  to  read  inputs  into  object
s.compute()#How  to  store  results  in  object
s.disp()#How  to  print  object  with  disp()  method
print(s.__str__())#How  to  print  object  with  _str_()  method


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
        self.num = int(input("Enter the Numerator :"))   # read numerator
        self.den = int(input("Enter the Denominator :")) # read denominator
        if self.den == 0:                                # check denominator
            self.test()                                  # call test()

    def test(self):
        self.den = int(input("Enter non Zero Denominator :"))  # reenter denom
        if self.den == 0:     # keep checking until valid
            self.test()

    def _str_(self):
        return f'{self.num}/{self.den}'

    def simplify(self):
        g = math.gcd(self.num, self.den)   # gcd of num and den
        self.num //= g
        self.den //= g

    def add(self , a , b):
        self.num = a.num * b.den + b.num * a.den
        self.den = a.den * b.den
        self.simplify()   # simplify result

    def sub(self , a , b):
        self.num = a.num * b.den - b.num * a.den
        self.den = a.den * b.den
        self.simplify()

    def mul(self , a , b):
        self.num = a.num * b.num
        self.den = a.den * b.den
        self.simplify()

    def div(self , a , b):
        if b.num == 0:
            print("Division not permitted (denominator becomes zero)")
            self.num, self.den = 0, 1
        else:
            self.num = a.num * b.den
            self.den = a.den * b.num
            self.simplify()

# End of the class

# Create 6 objects
a, b, c, d, e, f = Rat(), Rat(), Rat(), Rat(), Rat(), Rat()

a.get()   # read rational number into object 'a'
b.get()   # read rational number into object 'b'

c.add(a, b)   # add a and b → c
d.sub(a, b)   # subtract a and b → d
e.mul(a, b)   # multiply a and b → e
f.div(a, b)   # divide a and b → f

print("Addition :", c)      
print("Subtraction :", d)   
print("Multiplication :", e)

if b.num != 0:    # check division
    print("Division :", f)
else:
    print("Division is not permitted")

