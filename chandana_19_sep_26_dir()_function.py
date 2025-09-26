#  dir()  function  demo  program  
from  prog2   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat)) # gets all the methods of the class in the form of list of strings
print()
print()
print(dir(a)) # gets all the variables of object and methods of the class in the form of list of strings


#  Find  outputs  
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr')) # True : returns true if the variable is present in the object and false otherwise
print(hasattr(a , 'dr')) # False
print(hasattr(a , 'm1')) # True
print(hasattr(a , 'm2')) # False
print(hasattr(Rat , 'm1')) # True # returns True if the method is present in the class and False otherwise
print(hasattr(Rat , 'm2')) # False
print(hasattr(Rat , 'nr')) # False


# Find  outputs  
class  Cat:
	def  talk(self):
		print('Meow Meow Meow ....')
class  Dog:
	def  bark(self):
		print('Bhow Bhow Bhow ....')
class  Goat:
	def  talk(self):
		print('Mehar  Mehar  Mehar  ....')
#end of the class
a = [Cat() , Dog() , Goat()]
for  x  in   a:
	if   hasattr(x , 'talk'):
		x . talk()
	else:
		x . bark()
'''
o/p:
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....
'''


#  Find  outputs
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . __dict__)
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break
	
'''
o/p:
Enter  variable  name  to  be  added  to  object  :  y
Enter  value  of  the  variable  :  21
{'x': 10, 'y': 21}
10
Enter  variable  name  whose  value  is  to  be  retrieved  :  x
10
Enter  variable  name  whose  value  is  to  be  retrieved  :  y
21
Enter  variable  name  whose  value  is  to  be  retrieved  :  z
Invalid  variable   name   :  z
'''


'''
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
e=Emp()
# convert  dictionary  to  object  'e'  with  for  loop
for key,value in dict.items():
	setattr(e,key.lower(),value) 
# How  to  print  object  'e'  with  for  loop
for i in dict.keys():
	print(f'{i} = {getattr(e,i.lower())}')
'''
o/p:
Empno = 25
Ename = Rama  Rao
Sal = 10000.0
'''


'''
Repeat  prog2  with  3  objects
Eg:  c = a + b
	 print  c
	 c = a - b
	 print  c
	 c = a * b
	 print  c
	 c = a / b
	 print  c

Hint:  Import   Rat  class  defined  in  prog10a  but  do  not  define  Rat  class   again
'''
from prog2 import Rat  
a = Rat()
b = Rat()
c = Rat()  
a.get()
b.get()
c.add(a, b)
print("a + b =", c)
c.sub(a, b)
print("a - b =", c)
c.mul(a, b)
print("a * b =", c)
c.div(a, b)
if c.nr is None:
    print("Division not permitted")
else:
    print("a / b =", c)
'''
o/p:
Enter numerator: 2
Enter denominator: 3
Enter numerator: 4
Enter denominator: 5
a + b = 22/15
a - b = -2/15
a * b = 8/15
a / b = 5/6
'''


'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
from prog2 import Rat   
a = [Rat() for i in range(6)]

a[0].get()
a[1].get()

a[2].add(a[0], a[1])
print("sum:     ", a[2])

a[3].sub(a[0], a[1])
print("diff:    ", a[3])

a[4].mul(a[0], a[1])
print("product: ", a[4])

a[5].div(a[0], a[1])
if a[5].nr is None:
    print("division not permitted")
else:
    print("division:", a[5])
'''
o/p:
Enter numerator: 3
Enter denominator: 5
Enter numerator: 6
Enter denominator: 4
sum:      21/10
diff:     -9/10
product:  9/10
division: 2/5
'''