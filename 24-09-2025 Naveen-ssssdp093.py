'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
'''
How  to  create  triangle  object
How  to  call  get()  method  in  another  way
How  to  call  test()  method  in  another  way
print('Area : ',  How  to  call  area()  method  in  another  way)
print('Perimeter: ',  How  to  call  peri()  method  in  another  way)



from prog5a import triangle

#to create a traingle
t=triangle()
#to call get() method in another way
triangle.get(t)
#to call test() method in another way
triangle.test(t)
#to call area() method in another way
print('Area:',triangle.area(t))
#to call peri() method in another way
print('Perimeter :'triangle.peri(t))
'''



'''
#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x)                    # local variable x=10
		print(self . x)             # instance variable self.x=20
		x += 5                      # x = 15
		self . x += 7               # x = 27
	def   m2(self):
		print(x)                    # x is not defined
		print(self . x)             # x = 27
		self . x += 6               # x = 33
# End  of  the  class
a = c1()
a . m1()                            # prints: 10 20
a . m2()                            # error x and self.x are not defined
print(a . x)                        # a.x=27 if program continued
print(self . x)                     # Error self is not defined outside the class
print(x)                            # Error x is not defined globally
'''



'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
'''
class  Test:
	def   get(self):
		 How  to  read  inputs  into  variables  x , y  and  z  of  object  self
	def   add(self , m , n):
		 How  to  add  objects  m  and  n  and  store  results  in  object  self
	def  disp(self):
		 How  to  print  object  self
# End  of  the  class
How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
How  to  read  inputs  into  object  'a'
print('Second  Object')
How  to  read  inputs  into  object  'b'
How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
How  to  print  object  'c'
'''


'''
class Test:
    def get(self):
        # read  inputs  into  variables  x , y  and  z  of  object  self
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))
        self.z = int(input("Enter z: "))

    def add(self, m, n):
        # add  objects  m  and  n  and  store  results  in  object  self
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z

    def disp(self):
        # print  object  self
        print("x =", self.x)
        print("y =", self.y)
        print("z =", self.z)

		
#create  three  Test  class  objects  a , b  and  c
a=Test()
b=Test()
c=Test()

#read inputs for first object
print('First Object')
a.get()

#read inputs for second object
print('Second Object')
b.get()

# add object a and b and stores results in object c
c.add(a,b)

#prints addition results
print('Addition results')
c.disp()
'''


#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)                            # prints type and address\




#  Find  outputs (Home  work)
class   c1:
	def  _str_(self):
			return  '25'
class   c2:
	def  _str_(self):
			return   35
class   c3:
	def  _str_(self):
			print('Hyd')
class   c4:
	def  _str_(self , x):
			return   F'{x}'
#end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a)                            # prints type and address of class c1
print(b)                            # prints type and address of class c2
print(c)                            # prints type and address of class c3
print(d)                            # prints type and address of class c4
print(b . _str_())                  # return 35 ---> prints 35
print(c . _str_())                  # prints 'Hyd' inside method ---> returns None ---> prints None
print(d . _str_(50))                # returns '50' ---> prints 50




'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		#How  to  read  roll  number  into  object  self
		self.roll=input('Enter roll number:')
		#How  to  read  student  name  into  object  self
		self.name=input('Enter Student Name:')
		#How  to  read  gender  into  object  self
		self.gender=input('Enter Gender:')
		#How  to  read  marks  of  3  subjects
		self.sub1=int(input('Enter marks of subject1:'))
		self.sub2=int(input('Enter marks of subject2:'))
		self.sub3=int(input('Enter marks of subject3:'))
	def   compute(self):
		#How  to  calculate  total  marks
		self.total=self.sub1+self.sub2+self.sub3
		#How  to  calculate  average  marks
		self.avg=self.total / 3
		#if  At  least  one  subject  is  below  40:
		#		How  to  initilaize  grade  to  'Fail'
		if self.sub1 < 40 or self.sub2 < 40 or self.sub3 < 40:
				self.grade='Fail'
		
		#elif  average  is  above  >= 70%:
		#		How  to  initilaize  grade  to  'Distinction'
		elif self.avg >= 70:
			self.grade='Distinction'
			
		#elif  average  is  above  >= 60%:
		#		How  to  initilaize  grade  to  'First  class'
		elif self.avg >= 60:
			self.grade='First class' 
			
		#elif  average  is  above  >= 50%:
		#		How  to  initilaize  grade  to  'Second  class'
		elif self.avg >= 50:
			self.grade='Second class'
		else:
				#How  to  initilaize  grade  to  'Third  class'
				self.grade='Third class'
				
	def  disp(self):
		print('Roll  Number  :  ' , self.roll)
		print('Student  Name  :  ' , self.name)
		print('Gender  :  ' , self.gender)
		print('Total  Marks  :  ' , self.total)
		print('Average  :  ' , round(self.avg,2))
		print('Grade  :  ' , self.grade)
	def   _str_(self):
		#return  All  the   values  of  object  self  in  the  form  of  string
		return(f"Roll:{self.roll},Name:{self.Name},gender:{self.gender},total:{self.total},average:{self.average:.2f},grade:{self.grade}")
#End  of  the  class
#How  to  create  Student  class  object
s=Student()
#How  to  read  inputs  into  object
s.get()
#How  to  store  results  in  object
s.compute()
#How  to  print  object  with  disp()  method
print("\nStudent Details (disp method):")
s.disp()
#How  to  print  object  with  _str_()  method
print("\nStudent Details (__str__ method):")
print(s._str_())





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
		#How  to  read  numerator  into  object  self
		self.num=int(input('Enter numerator:'))
		#How  to  read  denominator  into  object  self
		self.den=int(input('Enter denominator:'))
		#How  to  call  test()  method
		self.test()
		
	def  test(self):
		#Ask  user  to  reenter  denom  when  denom  is  zero
		while self.den == 0:
			print('Denominator cannot be zero. re-enter')
			self.den=int(input('Enter denominator:'))
			
	def    _str_(self):
			 #return  values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
			 return f"{self.num} / {self.den}"
	
    def   add(self , a , b):
		#How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
        self.num = a.num+b.den+b.num+a.den
        self.den = a.den+b.den
        
		#How  to  simplify  object  self
		self.simplify()
		
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		#How  to  subtract  objects  'a'  and  'b' and  store  results  in  object  self
		self.num = a.num+b.den - b.num+a.den
		self.den= a.den+b.den
		
		#How  to  simplify  object  self
		self.simplify()
		
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		#How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  self
		self.num=a.num*b.num
		self.den=a.den*b.den
		#How  to  simplify  object  self
		self.simplify()
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		#How  to  divide  objects  'a'  and  'b' and  store  results  in  object  self
		#How  to  simplify  object  self
		if b.num == 0:
			self.num = None
			self.den = None
		else:
			self.num = a.num * b.den
			self.den = a.den * b.num
			self.simplify()
		
		
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
			#How  to  find  gcd  of  numerator  and   denominator
			if self.num != 0:
				g=math.gcd(self.num,self.den)
			#How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
                self.num //= g
                self.den //= g
			
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
#How  to  create  6  objects  a , b , c , d , e , f
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()
#How  to  read  rational  number  into  object  'a'
print('Enter first rational number:')
a.get()
#How to  read  rational  number  into  object  'b'
print('Enter second rational number:')
b.get()
#How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
c.add(a,b)
#How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
d.sub(a,b)
#How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
e.mul(a,b)
#How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
f.div(a,b)
#How  to  print  object   'c'
print('\nAddition(a+b)',c.__str__())
#How  to  print  object   'd'
print('Substraction(a-b)',d.__str__())
#How  to  print  object   'e'
print('Multiplication(a*b)',e.__str__())
if  f.den != 0:
	print('Division(a/b)'f.__str__())
	
else:
	print('Division  is  not  permitted')

