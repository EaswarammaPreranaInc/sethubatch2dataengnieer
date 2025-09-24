'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
from prog5a import triangle
t=triangle()#How  to  create  triangle  object
triangle.get(t)#How  to  call  get()  method  in  another  way
triangle.test(t)#How  to  call  test()  method  in  another  way
print('Area : ',triangle.area(t))
print('Perimeter: ',triangle.peri(t))
#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x)#10
		print(self . x)#20
		x += 5
		self . x += 7
	def   m2(self):
		print(x)#error 
		print(self . x)#27
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x)#33
print(self . x)#error
print(x)#error
'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		self.x=int(input('Enter a number:'))
		self.y=int(input('Enter a number:'))
		self.z=int(input('Enter a number:'))#How  to  read  inputs  into  variables  x , y  and  z  of  object  self
	def   add(self , m , n):
		self.x=m.x+n.x
		self.y=m.y+n.y
		self.z=m.z+n.z#How  to  add  objects  m  and  n  and  store  results  in  object  self
	def  disp(self):
		print("x =", self.x, ", y =", self.y, ", z =", self.z)#How  to  print  object  self
# End  of  the  class
a=Test()
b=Test()
c=Test()#How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
a.get()#aHow  to  read  inputs  into  object  'a'
print('Second  Object')
b.get()#How  to  read  inputs  into  object  'b'
c.add(a,b)#How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
c.disp()#How  to  print  object  'c'
#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)#Type and address 
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
print(a)#25
print(b)#error
print(c)#Error
print(d)#error
print(b . __str__())#35
print(c . __str__())#Hyd None
print(d . __str__(50))#50
'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
    def  get(self):
        self.rollno=int(input('Enter a number:'))#How  to  read  roll  number  into  object  self
        self.sname=input('Enter name of student:')#How  to  read  student  name  into  object  self
        self.gender=input('Enter m or f:')#How  to  read  gender  into  object  self
        print("Enter marks of 3 subjects :")
        self.m1 = int(input("Subject 1 : "))
        self.m2 = int(input("Subject 2 : "))
        self.m3 = int(input("Subject 3 : "))#How  to  read  marks  of  3  subjects
    def compute(self):
        self.total=self.m1+self.m2+self.m3#How  to  calculate  total  marks
        self.avg=self.total/3#How  to  calculate  average  marks
        if  self.m1<40 or self.m2<40 or self.m3<40:
                self.grade="Fail"#How  to  initilaize  grade  to  'Fail'
        elif  self.avg>=70:
                self.grade="Distinction"#How  to  initilaize  grade  to  'Distinction'
        elif  self.avg>=60:
                self.grade="First Class"#How  to  initilaize  grade  to  'First  class'
        elif  self.avg>=50:
                self.grade="Second Class"#How  to  initilaize  grade  to  'Second  class'
        else:
                self.grade="Third Class"#How  to  initilaize  grade  to  'Third  class'
    def  disp(self):
        print('Roll  Number  :  ' , self.rollno)
        print('Student  Name  :  ' , self.sname)
        print('Gender  :  ' ,  self.gender)
        print('Total  Marks  :  ' ,self.total)
        print('Average  :  ' ,self.avg)
        print('Grade  :  ' , self.grade)
    def   __str__(self):
          return  f"Roll: {self.rollno}, Name: {self.sname}, Gender: {self.gender}, Total: {self.total}, Average: {self.avg}, Grade: {self.grade}"
#End  of  the  class
a=Student()#How  to  create  Student  class  object
a.get()#How  to  read  inputs  into  object
a.compute()#How  to  store  results  in  object
a.disp()#How  to  print  object  with  disp()  method
print(a)#How  to  print  object  with  __str__()  method
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
import  math
class  Rat:
	def  get(self):
		self.num=int(input('Enter numerator :'))#How  to  read  numerator  into  object  self
		self.den=int(input('Enter denominator'))#How  to  read  denominator  into  object  self
		self.test()#How  to  call  test()  method
	def  test(self):
		while self.den==0:
			print("Denominator cannot be zero..Re-enter")
			self.den=int(input("Enter denomionator again:"))#Ask  user  to  reenter  denom  when  denom  is  zero
	def    __str__(self):
			return str(self.num) + " / " + str(self.den) 
	def   add(self , a , b):
		self.num=a.num*b.den+b.num*a.den
		self.den=a.den*b.den#How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
		self.simplify()#How  to  simplify  object  self
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		self.num=a.num*b.den-b.num*a.den
		self.den=a.den*b.den#How  to  subtract  objects  'a'  and  'b' and  store  results  in  object  self
		self.simplify()#How  to  simplify  object  self
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		self.num=a.num*b.num
		self.den=a.den*b.den#How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  self
		self.simplify()#How  to  simplify  object  self
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		if b.num==0:
			self.num=1
			self.den=0
		else:
			self.num=a.num*b.den
			self.den=a.den*b.num#How  to  divide  objects  'a'  and  'b' and  store  results  in  object  self
		self.simplify()#How  to  simplify  object  self
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
			if self.num!=0:
				g=math.gcd(self.num,self.den)#How  to  find  gcd  of  numerator  and   denominator
				self.num//=g
				self.den//=g#How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
a=Rat()
b=Rat()
c=Rat()
d=Rat()
e=Rat()
f=Rat()#How  to  create  6  objects  a , b , c , d , e , f
a.get()#How  to  read  rational  number  into  object  'a'
b.get()#How to  read  rational  number  into  object  'b'
c.add(a,b)#How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
d.sub(a,b)#How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
e.mul(a,b)#How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
f.div(a,b)#How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
print("Sum:",c)#How  to  print  object   'c'
print("Difference:",d)#How  to  print  object   'd'
print("Product:",e)#How  to  print  object   'e'
if  f.den!=0:
	print("Division:",f)#How  to  print  object  'f
else:
	print('Division  is  not  permitted')
Sum: 11 / 9
Difference: 1 / 9
Product: 10 / 27
Division: 6 / 