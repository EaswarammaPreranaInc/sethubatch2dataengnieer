'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
from prog5a import triangle
t=triangle()# How  to  create  triangle  object
triangle.get(t)# How  to  call  get()  method  in  another  way
triangle.test(t)# How  to  call  test()  method  in  another  way
print('Area : ', triangle.area(t)) #How  to  call  area()  method  in  another  way)
print('Perimeter: ',triangle.peri()) # How  to  call  peri()  method  in  another  way)

#============================================ #  Find  outputs  (Home  work)

class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x)   #10
		print(self . x) #20
		x += 5
		self . x += 7
	def   m2(self):
		# print(x)  #Error
		print(self . x)  #27
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x) #33
# print(self . x)  #error
# print(x) #Error

#============================================ '''  (Home  work)

#Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and store  results  in   third  object
'''
1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		self.x=int(input('Enter x: '))
		self.y=int(input('Enter y: '))
		self.z=int(input('Enter z: '))
		 #How  to  read  inputs  into  variables  x , y  and  z  of  object  self
	def add(self , m , n):
		self.x=m.x+n.x
		self.y=m.y+n.y
		self.z=m.z+n.z
		 #How  to  add  objects  m  and  n  and  store  results  in  object  self
	def  disp(self):
		print( f'x={self.x} \ny={self.y} \nz={self.z}')
		 #How  to  print  object  self
# End  of  the  class
# How  to  create  three  Test  class  objects  a , b  and  c
a=Test()
b=Test()
c=Test()
print('First  Object')
# How  to  read  inputs  into  object  'a'
a.get()
print('Second  Object')
# How  to  read  inputs  into  object  'b'
# How  to  add  objects  a  and  b  and  store  results in  object  'c'
b.get()
c.add(a,b)
print('Addition  results')
# How  to  print  object  'c'
c.disp()

#============================================ #  Find  outputs (Home  work)

class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) #type and address

#============================================ #  Find  outputs (Home  work)

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
print(a)
print(b)
print(c)
print(d)
print(b . _str_())
print(c . _str_())
print(d . _str_(50))
'''
<__main__.c1 object at 0x000001F5D90A7230>
<__main__.c2 object at 0x000001F5D90A7380>
<__main__.c3 object at 0x000001F5D90A74D0>
<__main__.c4 object at 0x000001F5D90A7620>
35
Hyd
None
50
'''
#============================================
'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
#prog9
class   Student:
	def   get(self):
		self.rno=input("enter roll number: ")		# How  to  read  roll  number  into  object  self
		self.sname=	input("enter student name: ")	# How  to  read  student  name  into  object  self
		self.gender=input("enter gender: ")		# How  to  read  gender  into  object  self
		self.m=[]		# How  to  read  marks  of  3  subjects
		for i in range(3):
			marks=float(input(f"entert marks of subject {i+1}: "))
			self.m.append(marks)
	def   compute(self):
		self.tot=sum(self.m) # 	How  to  calculate  total  marks
		self.avg=self.tot/3 # 	How  to  calculate  average  marks
		if  min(self.m)<40:#at  least  one  subject  is  below  40:
			self.grade='Fail'#How  to  initilaize  grade  to  'Fail'
		elif self.avg>=70:# average  is  above  >= 70%:
			self.grade='Distinction'	#How  to  initilaize  grade  to  'Distinction'
		elif self.avg>=60:# average  is  above  >= 60%:
			self.grade='First class'	#How  to  initilaize  grade  to  'First  class'
		elif self.avg>=50:# average  is  above  >= 50%:
			self.grade='Second class'	#How  to  initilaize  grade  to  'Second  class'
		else:
			self.grade='third class'	#How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   self.rno)
		print('Student  Name  :  ' ,self.sname )
		print('Gender  :  ' ,self.gender  )
		print('Total  Marks  :  ' ,self.tot )
		print('Average  :  ' ,self.avg )
		print('Grade  :  ' ,self.grade )
	def   __str__(self):
		return  f'{self.rno}\t {self.sname}\t {self.gender}\t {self.tot}\t {self.avg}\t {self.grade}'#All  the   values  of  object  self  in  the  form  of  string
#End  of  the  class
# How  to  create  Student  class  object
if __name__=='__main__':
	s=Student()
	# How  to  read  inputs  into  object
	s.get()
	# How  to  store  results  in  object
	s.compute()
	# How  to  print  object  with  disp()  method
	s.disp()
	# How  to  print  object  with  _str_()  method
	print(s)



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


#prog10a
import  math
class  Rat:
	def  get(self):
		self.nr=int(input("enter the nr: "))# How  to  read  numerator  into  object  self
		self.dr=int(input("enter the dr: "))# How  to  read  denominator  into  object  self
		self.test()# How  to  call  test()  method
	def  test(self):
		while self.dr==0:
			self.dr=int(input("denom can not be zero, reenter: "))# Ask  user  to  reenter  denom  when  denom  is  zero
	def    __str__(self):
			 return f'{self.nr}/{self.dr}'    #values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	def	add(self , a , b):
		self.nr=a.nr*b.dr+a.dr*b.nr# How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
		self.dr=a.dr*b.dr
		self.simplify()	# How  to  simplify  object  self
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		self.nr=a.nr*b.dr-a.dr*b.nr# How  to  subtract  objects  'a'  and  'b' and  store  results  in  object  self
		self.dr=a.dr*b.dr
		self.simplify()
		# How  to  simplify  object  self
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		self.nr=a.nr*b.nr  # How  to  subtract  objects  'a'  and  'b' and  store  results  in  object  self
		self.dr=a.dr*b.dr
		self.simplify()	# How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  self
		# How  to  simplify  object  self
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		self.nr=a.nr*b.nr
		self.dr=a.dr*b.nr
		self.simplify()# How  to  divide  objects  'a'  and  'b' and  store  results  in  object  self
		# How  to  simplify  object  self
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
		if self.nr!=0:
			g=math.gcd(self.nr,self.dr)
			self.nr=self.nr//g		# How  to  find  gcd  of  numerator  and   denominator
			self.dr=self.dr//g		# How  to  find  gcd  of  numerator  and   denominator
			# How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
# How  to  create  6  objects  a , b , c , d , e , f
if __name__=='__main__':
	a=Rat()
	b=Rat()
	c=Rat()
	d=Rat()
	e=Rat()
	f=Rat()
	# How  to  read  rational  number  into  object  'a'
	a.get()
	# How to  read  rational  number  into  object  'b'
	b.get()
	# How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
	c.add(a,b)
	# How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
	d.sub(a,b)
	# How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
	e.mul(a,b)
	# How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
	f.div(a,b)
	# How  to  print  object   'c'
	print('add: ',c)
	# How  to  print  object   'd'
	print('sub: ',d)
	# How  to  print  object   'e'
	print('mul: ',e)

	if  b.nr!=0:
		print('div: ',f)
		# How  to  print  object  'f
	else:
		print('Division  is  not  permitted')