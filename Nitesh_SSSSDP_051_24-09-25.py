'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
from triangle_class import triangle
t=triangle() #How  to  create  triangle  object
triangle.get(t) #How  to  call  get()  method  in  another  way
triangle.test(t)#How  to  call  test()  method  in  another  way
print('Area : ', triangle.area(t))# How  to  call  area()  method  in  another  way)
print('Perimeter: ',  triangle.peri(t))#How  to  call  peri()  method  in  another  way)

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
a . m1() # 10 20
a . m2() #error 27
print(a . x) #27
print(self . x)#error there is no self object here
print(x) #there is no local variable x

'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		#  How  to  read  inputs  into  variables  x , y  and  z  of  object  self
		self.x=float(input("Enter 1st value: "))
		self.y=float(input("Enter 2nd value: "))
		self.z=float(input("Enter 3rd value: "))
		
	def   add(self , m , n):
		#  How  to  add  objects  m  and  n  and  store  results  in  object  self
		self.x=m.x+n.x
		self.y=m.y+n.y
		self.z=m.z+n.z
		
	def  disp(self):
		#  How  to  print  object  self
		print('x:',self.x)
		print('y:',self.y)
		print('z:',self.z)
		
# End  of  the  class
# How  to  create  three  Test  class  objects  a , b  and  c
a=Test()
b=Test()
c=Test()

print('First  Object')
a.get()#How  to  read  inputs  into  object  'a'
print('Second  Object')
# How  to  read  inputs  into  object  'b'
b.get()
c.add(a,b) #How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
# How  to  print  object  'c'
print('c.x:',c.x)
print('c.y:',c.y)
print('c.z:',c.z)


#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) #<class '__main__.Date'>

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
print(c)#Hyd
print(d)#error argument is missing
print(b . __str__())#25
print(c . __str__())#Hyd
print(d . __str__(50))#50

'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''

class   Student:
	def   get(self):
		# How  to  read  roll  number  into  object  self
		self.rno=int(input("Enter roll number: "))
		# How  to  read  student  name  into  object  self
		self.name=input("Enter name: ")
		# How  to  read  gender  into  object  self
		self.gender=input("Enter Gender: ")
		# How  to  read  marks  of  3  subjects
		l=[]
		try:
			l.append(int(input()))
		except:
			self.marks=l
	def   compute(self):
		# How  to  calculate  total  marks
		sum=0
		for x in self.marks:
			sum+=x
		self.total=sum
		avg=sum/len(self.marks)
		self.average=avg
		avg=(avg/sum)*100
		for x in self.marks:
			if x<40:
				self.grade='Fail'
				return 
		if avg >= 70:
			self.grade='Distinction'
			return 
		elif avg >= 60:
			self.grade='First  class'
		elif avg>=50:
			self.grade='Second  class'
		else:
			self.grade='Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   self.rno)
		print('Student  Name  :  ' , self.name)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.total)
		print('Average  :  ' , self.average)
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		return  f'{self.rno} {self.name} {self.gender} {self.total} {self.average} {self.grade}' #All  the   values  of  object  self  in  the  form  of  string
#End  of  the  class
a=Student()#How  to  create  Student  class  object
a.get()#How  to  read  inputs  into  object
a.compute()#How  to  store  results  in  object
a.disp()#How  to  print  object  with  disp()  method
print(a) #How  to  print  object  with  __str__()  method
print(a.__str__)

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
		self.p=int(input("Enter numerator:")) #How  to  read  numerator  into  object  self
		self.q=int(input("Enter Denominator:")) #How  to  read  denominator  into  object  self
		self.test() #How  to  call  test()  method
	def  test(self):
		# Ask  user  to  reenter  denom  when  denom  is  zero
		if self.q==0:
			self.q=int(input("Re enter the denominator:"))
			self.test()
	def    __str__(self):
			 return f'{self.p}/{self.q}' #values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	def   add(self , a , b):
		# How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
		self.p=(a.p*b.q +a.q+b.p)
		self.q=(a.q*b.q)
		self.simplify() #How  to  simplify  object  self
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		self.p=(a.p*b.q -a.q+b.p)#How  to  subtract  objects  'a'  and  'b' and  store  results  in  object  self
		self.q=(a.q*b.q) 
		self.simplify()#How  to  simplify  object  self
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		self.p=(a.p*b.p) # How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  self
		self.q=(a.q*b.q) 
		self.simplify() #How  to  simplify  object  self
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		self.p=(a.p*b.q)#How  to  divide  objects  'a'  and  'b' and  store  results  in  object  self
		self.q=(a.q*b.p) 
		self.simplify() #How  to  simplify  object  self
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
			# How  to  find  gcd  of  numerator  and   denominator
			g=math.gcd(self.p,self.q)
			# How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
			self.p=(self.p)/g
			self.q=(self.q)/g
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
	
# End  of the class
# How  to  create  6  objects  a , b , c , d , e , f
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
print(c) #How  to  print  object   'c'
print(d) #How  to  print  object   'd'
print(e) #How  to  print  object   'e'
if  f.q!=0:
	# How  to  print  object  f
	print(f)
else:
	print('Division  is  not  permitted')