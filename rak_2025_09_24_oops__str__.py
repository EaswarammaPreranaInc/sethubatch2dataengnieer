if __name__ == '__main__':

	'''
	Repeat  prog5a  such  that  methods  are  called  in  another  way

	1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

	2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
	'''
	from rak_2025_09_23_oops1 import triangle
	#How  to  create  triangle  object
	t = triangle()
	#How  to  call  get()  method  in  another  way
	triangle.get(t)
	#How  to  call  test()  method  in  another  way
	triangle.test(t)
	print('Area : ', triangle.area(t))        # How  to  call  area()  method  in  another  way
	print('Perimeter: ', triangle.peri(t))    # How  to  call  peri()  method  in another way



	#  Find  outputs  (Home  work)
	class   c1:
		def  m1(self):
			x = 10
			self . x = 20
			print(x)
			print(self . x)
			x += 5
			self . x += 7
		def m2(self):
			#print(x)              #local variable of another method is not accessible
			print(self . x)
			self . x += 6
	# End  of  the  class
	a = c1()
	a . m1()               
	a . m2()
	print(a . x)
	# print(self.x)                 #self is not defined
	# print(x)                      #x is not defined
	'''
	OUTPUT:
	10
	20
	27
	33
	'''




	'''  (Home  work)
	Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
	store  results  in   third  object

	1st  object   --->  x = 10 , y = 20 , z = 30

	2nd  object --->  x = 40 , y = 50 , z = 60

	3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
	'''
	class Test:
		def get(self):
			self.x = int(input('Enter x:  '))
			self.y = int(input('Enter y:  '))
			self.z = int(input('Enter z:  '))
		def add(self, m, n):
			self.x = m.x + n.x
			self.y = m.y + n.y
			self.z = m.z + n.z
		def disp(self):
			print(f'x : {self.x}, y : {self.y}, z : {self.z}')

	# End  of  the  class
	#How  to  create  three  Test  class  objects  a , b  and  c
	a = Test()
	b = Test()
	c = Test()
	print('First  Object')
	#How  to  read  inputs  into  object  'a'
	a.get()
	print('Second  Object')
	#How  to  read  inputs  into  object  'b'
	b.get()
	#How  to  add  objects  a  and  b  and  store  results in  object  'c'
	c.add(a, b)
	print('Addition  results')
	#How  to  print object 'c'
	c.disp()






	#  Find  outputs (Home  work)
	class  Date:
		pass
	# End of the class
	a =  Date()
	a . dd = 15
	a . mm = 8
	a . yy = 1947
	print(a)                #type and address
		


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
	print(a)                   #25
	# print(b)                   #error, returns int instead of str
	# print(c)                   #error, returns None instead of str
	# print(d)                   #error, implicit call not possible as it required one pos arg
	print(b . __str__())       #35
	print(c . __str__())       #Hyd <nl> None
	print(d . __str__(50))     #50



'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class  Student:
	def  get(self):
		# How  to  read  roll  number  into  object  self
		self.rollno = int(input('Enter roll no:  '))
		# How  to  read  student  name  into  object  self
		self.name = input('Enter name of the student:  ')
		# How  to  read  gender  into  object  self
		self.gender = input('Enter the gender:  ')
		# How  to  read  marks  of  3  subjects
		self.marks = []
		for i in range(3):
			m = float(input(f'Enter marks of subject {i+1}:   '))
			self.marks.append(m)
	def  compute(self):
		# How  to  calculate  total  marks
		self.total_marks = sum(self.marks)
		# How  to  calculate  average  marks
		self.avg_marks = self.total_marks / len(self.marks)
		if min(self.marks) < 40:
			self.grade = 'Fail'
		elif self.avg_marks >= 70:
			self.grade = 'Distinction'
		elif self.avg_marks >= 60:
			self.grade = 'First Class'
		elif self.avg_marks >= 50:
			self.grade = 'Seconf Class'
		else:
			self.grade = 'Third Class'
	def disp(self):
		print('Roll  Number  :  ' ,   self.rollno)
		print('Student  Name  :  ' , self.name)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.total_marks)
		print('Average  :  ' , self.avg_marks)
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		#return  All  the   values  of  object  self  in  the  form  of  string
		return f'Roll Number : {self.rollno} \n Student Name : {self.name} \n Gender : {self.gender} \n Total Marks : {self.total_marks} \n Avg Marks : {self.avg_marks} \n Grade : {self.grade}'

if __name__ == '__main__':
	#End  of  the  class
	# How  to  create  Student  class  object
	s = Student()
	# How  to  read  inputs  into  object
	s.get()
	# How  to  store  results  in  object
	s.compute()
	# How  to  print  object  with  disp()  method
	s.disp()
	# How  to  print  object  with  __str__() method
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
import  math
class  Rat:
	def  get(self):
		# How  to  read  numerator  into  object  self
		self.n = int(input('Enter numerator:  '))
		# How  to  read  denominator  into  object  self
		self.d = int(input('Enter denominator:  '))
		# How  to  call  test()  method
		self.test()
	def  test(self):
		#Ask  user  to  reenter  denom  when  denom  is  zero
		while self.d == 0:
			int(input('Denominator cannot be zero, please reenter:  '))
	def __str__(self):
		#return  values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
		return f'{self.n} / {self.d}'
	def   add(self , a , b):
		#How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
		self.n = a.n * b.d + a.d * b.n
		self.d = a.d * b.d
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
		self.n = a.n * b.d - a.d * b.n
		self.d = a.d * b.d
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
		self.n = a.n * b.n
		self.d = a.d * b.d
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
		self.n = a.n * b.d 
		self.d = a.d * b.n
		#How to simplify object 
		self.simplify()
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def simplify(self):
		if self.n != 0:
			#How  to  find  gcd  of  numerator  and   denominator
			g = math.gcd(self.n, self.d)
			#How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
			self.n = self.n / g
			self.d = self.d / g
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class

if __name__ == '__main__':
	# How  to  create  6  objects  a , b , c , d , e , f
	a, b, c, d, e, f = Rat(), Rat(), Rat(), Rat(), Rat(), Rat()
	# How  to  read  rational  number  into  object  'a'
	a.get()
	# How to  read  rational  number  into  object  'b'
	b.get()
	# How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
	c.add(a, b)
	# How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
	d.sub(a, b)
	# How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
	e.mul(a, b)
	# How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
	f.div(a, b)
	# How  to  print  object   'c'
	print(c)
	# How  to  print  object   'd'
	print(d)
	# How  to  print  object   'e'
	print(e)
	if f.d != 0:
		print(f)
	else:
		print('Division is not permitted')