#Ramu(24-09)

'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
from prog5a import triangle #How  to  create  triangle  object
a=triangle()
triangle.get(a) #How  to  call  test()  method  in  another  way
print('Area : ', triangle.area(a))
print('Perimeter: ',triangle.peri(a))


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
a . m1() 
a . m2() # Error x is not defined in m2()
print(a . x) 
print(self . x) # Error
print(x) # Error x is not defined

10
20
Error
27
self is not defined
Error
Error


'''
  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''

class  Test:
    def   get(self):
        self.x=int(input("Enter 1st number :"))
        self.y=int(input("Enter 2nd number :"))
        self.z=int(input("Enter 3rd number : ")) #How  to  read  inputs  into  variables  x , y  and  z  of  object  self
    def   add(self , m , n):
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z
        self.result = self.x + self.y + self.z
        return self.result #How  to  add  objects  m  and  n  and  store  results  in  object  self
    def  disp(self):
        return self.result
    
# End  of  the  class
a=Test()
b=Test() 
c=Test() #How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
a.get() #How  to  read  inputs  into  object  'a'
print('Second  Object')
b.get() #How  to  read  inputs  into  object  'b'
c.add(a,b)  #How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
print(c.disp()) #How  to  print  object  'c'




#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15 
a . mm = 8
a . yy = 1947
print(a) # tyee and addrress



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
print(a) # 25
print(b) #Error
print(c) #Hyd Error because  it stores None
print(d) #Error
print(b . _str_()) #35
print(c . _str_()) #Hyd None
print(d . _str_(50)) #50



'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self.id=int(input()) #How  to  read  roll  number  into  object  self
		self.name=input() #How  to  read  student  name  into  object  self
		self.g=input() #How  to  read  gender  into  object  self
		self.marks=eval(input()) #How  to  read  marks  of  3  subjects
	def   compute(self):
		total=sum(self.marks) #How  to  calculate  total  marks
            avg=sum(self.marks)/len(self.marks) #How  to  calculate  average  marks
            if any(m < 40 for m in self.marks):#At  least  one  subject  is  below  40:
                grade='Fail'
		    elif  avg>= 70:
                grade='Distinction'
		    elif  avg>=60:
				grade='First  class'
		    elif  average  is  above  >= 50%:
                grade='Second  class'
		    else:
				grade ='Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   self.id)
		print('Student  Name  :  ' , self.name)
		print('Gender  :  ' ,  self.g)
		print('Total  Marks  :  ' , self.total)
		print('Average  :  ' , self.avg)
		print('Grade  :  ' , self.grade)
	def   _str_(self):
        return   f'Roll  Number  :  ({self.id}, Student  Name  :  {self.name}, Gender  :  {self.g}, Total  Marks  :  {self.total}, Average  :  {self.avg}, Grade  :  {self.grade})'
#End  of  the  class
a= Student() #How  to  create  Student  class  object
a.get() #How  to  read  inputs  into  object
a.compute() #How  to  store  results  in  object
a.disp() #How  to  print  object  with  disp()  method
print(a) #How  to  print  object  with  _str_()  method





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