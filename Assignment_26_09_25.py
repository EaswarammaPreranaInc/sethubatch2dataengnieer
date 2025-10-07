#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . __dict__)
s . get()
print(s . __dict__)
s . compute()
print(s . __dict__)
'''#output:
{}
Enter  roll  number : 21
Enter  student  name :  Jhansi
Enter  gender (m/f) : f
Enter  marks  of  subject  1  :  78
Enter  marks  of  subject  2  :  54
Enter  marks  of  subject  3  :  67
{'rno': 21, 'sname': 'Jhansi', 'gender': 'f', 'm': [78, 54, 67]}
{'rno': 21, 'sname': 'Jhansi', 'gender': 'f', 'm': [78, 54, 67], 'tot': 199, 'avg': 66.33333333333333, 'grade': 'First  class'}'''


'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
'''# prog9b.py
from prog9a import student   

if __name__ == "__main__":
    n = int(input("Enter number of students : "))
    studs = []   # 

    for i in range(n):
        print(f"\n--- Student {i+1} details ---")
        s = student()   
        s.get()         
        s.compute()     
        studs.append(s) 

    print("\n--- Student Results ---")
    for s in studs:
        s.disp()        
        print(s)

'''#output:
Enter number of students : 4

--- Student 1 details ---
Enter  roll  number : 21
Enter  student  name :  Jhansi
Enter  gender (m/f) : f
Enter  marks  of  subject  1  :  76
Enter  marks  of  subject  2  :  45
Enter  marks  of  subject  3  :  31

--- Student 2 details ---
Enter  roll  number : 20
Enter  student  name :  Varsha
Enter  gender (m/f) : f
Enter  marks  of  subject  1  :  56
Enter  marks  of  subject  2  :  65
Enter  marks  of  subject  3  :  41

--- Student 3 details ---
Enter  roll  number : 23
Enter  student  name :  Gangotri
Enter  gender (m/f) : 87
Enter  marks  of  subject  1  :  56
Enter  marks  of  subject  2  :  67
Enter  marks  of  subject  3  :  87

--- Student 4 details ---
Enter  roll  number : 25
Enter  student  name :  Sandhya
Enter  gender (m/f) : f
Enter  marks  of  subject  1  :  45
Enter  marks  of  subject  2  :  88
Enter  marks  of  subject  3  :  45'''

#  dir()  function  demo  program  (Home  work)

from  prog10a   import  rat

a = rat()

a . nr = 22

a . dr = 7

print(dir(rat))

print()

print()
print(dir(a))


['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_str_', 'add', 'div', 'get', 'mul', 'simplify', 'sub', 'test']


['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_str_', 'add', 'div', 'dr', 'get', 'mul', 'nr', 'simplify', 'sub', 'test']



#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr'))#True
print(hasattr(a , 'dr'))#False
print(hasattr(a , 'm1'))#True
print(hasattr(a , 'm2'))#False
print(hasattr(Rat , 'm1'))#True
print(hasattr(Rat , 'm2'))#False
print(hasattr(Rat , 'nr'))#False


# Find  outputs  (Home  work)
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
#output:
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....

#  Find  outputs  (Home  work)
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

#output:
Enter  variable  name  to  be  added  to  object  :  y
Enter  value  of  the  variable  :  20
{'x': 10, 'y': 20}
10
Enter  variable  name  whose  value  is  to  be  retrieved  :  x
10
Enter  variable  name  whose  value  is  to  be  retrieved  :  y
20
Enter  variable  name  whose  value  is  to  be  retrieved  :  z
Invalid  variable   name   :  z


'''
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''

class Emp:
    pass
# End of class

d = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 10000.0}

e = Emp()   # create empty Emp object

# dictionary → object attributes
for k, v in d.items():
    setattr(e, k.lower(), v)   # make attributes lowercase

# print object attributes using getattr
print("\nEmployee Details:")
for k in d.keys():
    print(k, ":", getattr(e, k.lower()))

#output:
Employee Details:
Empno : 25
Ename : Rama Rao
Sal : 10000.0

'''
Repeat  prog10a  with  3  objects

Eg:  c = a + b
	 print  c
	 c = a - b
	 print  c
	 c = a * b
	 print  c
	 c = a / b
	 print  c

Hint:  Reuse   rat  class  defined  in  prog10a  but  do  not  define  rat  class   again
'''
from  prog10a  import  rat  #   imports  rat  class  and  if  statement  outside  rat  class  in  prog10a
a = rat()  #  Creates  3  empty  rat  class  objects
b = rat()
c = rat()
a . get()  #  Reads  numerator  and  denominator  into   object  'a'
b . get()  #  Reads  numerator  and  denominator  into   object  'b'
c . add(a , b)  #  Adds  rational   numbers  in  objects  'a'  and  'b'  and  stores  results  in  object  'c'
print(F'Addition : {c}') #   _str_()  method  returns  values  of  object  'c'  in  the  form  of   string
c . sub(a , b)  #  Subtracts  rational   numbers  in  objects  'a'  and  'b'  and  stores  results  in  object  'c'
print(F'Substraction : {c}')  #   _str_()  method  returns  values  of  object  'c'  in  the  form  of   string
c . mul(a , b)  #  Multiplies   rational   numbers  in  objects  'a'  and  'b'  and  stores  results  in  object  'c'
print(F'Multiplication : {c}')   #   _str_()  method  returns  values  of  object  'c'  in  the  form  of   string
if  b . nr == 0:
	print('Division  is  not  permitted')
else:
	c . div(a , b)  #  Divides   rational   numbers  in  objects  'a'  and  'b'  and  stores  results  in  object  'c'
	print(F'Division : {c}')  #   _str_()  method  returns  values  of  object  'c'  in  the  form  of   string


'''
Is  if  statement  of  prog10a  executed ?  --->  No  becoz  if  condition  is  false
'''


'''
Repeat  prog10a  with  list  of  6  objects

Hint: Reuse  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
from  prog10a  import  rat   #   imports  rat  class  and  if  statement  outside  rat  class  in  prog10a
a = [rat()  , rat() , rat() , rat() , rat() , rat()]  #  Creates  a  list  of  6  rat  class  objects
a[0] . get()   #  Reads  numerator  and  denominator  into   object  a[0]
a[1] . get()   #  Reads  numerator  and  denominator  into   object  a[1]
a[2] . add(a[0] , a[1]) #  Adds  rational   numbers  in  objects   a[0]  and   a[1]  and  stores  results  in  object  a[2]
a[3] . sub(a[0] , a[1]) #  Subtracts  rational   numbers  in  objects   a[0]  and   a[1]  and  stores  results  in  object  a[3]
a[4] . mul(a[0] , a[1]) #  Multiplies  rational   numbers  in  objects   a[0]  and   a[1]  and  stores  results  in  object  a[4]
print('Sum : ' , a[2])  #   _str_()  method  returns  values  of  object   a[2]  in  the  form  of   string
print('Difference :  ' , a[3])  #   _str_()  method  returns  values  of  object   a[3]  in  the  form  of   string
print('Product :  '  ,  a[4])  #   _str_()  method  returns  values  of  object   a[4]  in  the  form  of   string
if  a[1] . nr == 0:
	print('Division  is  not  permitted')
else:
	a[5] . div(a[0] , a[1])  #  Divides  rational   numbers  in  objects   a[0]  and   a[1]  and  stores  results  in  object  a[5]
	print('Division :  ' , a[5])  #   _str_()  method  returns  values  of  object   a[5]  in  the  form  of   string



'''
1) def  add(self , a , b):
	     	pass
    a[2]  .  add(a[0] , a[1])
    What  are  self ,  a   and  b  for  the  above  method  call  ?  ---> self  is  a[2]  ,  a  is  a[0]  and    b  is  a[1]

2) a = [Rat() , Rat() , Rat() , Rat() , Rat() , Rat()]
    How  to  create  list  of  objects  with  for  loop ?  --->  a = []
	                                                                                       for  i  in  range(6):
		                                                                                         a . append(Rat())
'''













