
#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . _dict_)
s . get()
print(s . _dict_)
s . compute()
print(s . _dict_)




'''
output
Enter Roll Number: 21
Enter Name: Rama Rao
Enter Gender: male
Enter Marks of Subject 1: 52
Enter Marks of Subject 2: 48
Enter Marks of Subject 3: 55


Output:
{}                                                
{'rno': 21, 'name': 'Rama Rao', 'gender': 'male', 'm1': 52, 'm2': 48, 'm3': 55}
{'rno': 21, 'name': 'Rama Rao', 'gender': 'male', m1': 52, 'm2': 48, 'm3': 55, 'total': 155, 'avg': 51.67, 'grade': 'Pass'}
'''



'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''



from prog9a import student

n=int(input('Enter number of students:'))
students=[]

for i in range(n):
    print(f"\nStudent{i+1}")
    s=student()
    s.get()
    s.compute()
    student.append(s)

print("\nRollNo Name Gender Total Average Grade")
for s in students:
    print(f"{s:rno:<7} {s.gender:<7} {s.gender:<7} {s.gender:<7} {s.total:<9.1f} {s.avg:<10.2f} {s.grade}")


#  dir()  function  demo  program  (Home  work)

from  prog10a   import  Rat

a = Rat()                   # Create an Rat object

a . nr = 22                 # create a new attribute in the object

a . dr = 7                  # create another new attribute

print(dir(Rat))             # prints all names defined for class

print()

print()

print(dir(a))               # prints all names defined for class



#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr'))            # True  'a' has attribute 'nr'
print(hasattr(a , 'dr'))            # False 'a' does not have 'dr'
print(hasattr(a , 'm1'))            # True 'a' inherits method 'm1' from class
print(hasattr(a , 'm2'))            # False no attribute or method 'm2'
print(hasattr(Rat , 'm1'))          # True class Rat has method 'm1'
print(hasattr(Rat , 'm2'))          # False class Rat does not have 'm2'
print(hasattr(Rat , 'nr'))          # False 'nr' exists only in object 'a', not in class



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
		x . talk()                      # 'Meow Meow Meow ....'
                                        # 'Mehar  Mehar  Mehar  ....'
	else:
		x . bark()                      # 'Bhow Bhow Bhow ....'
		



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
	


'''
output

Enter  variable  name  to  be  added  to  object  :  y
Enter  value  of  the  variable  :  30
{'x': 10, 'y': 30}
10
Enter  variable  name  whose  value  is  to  be  retrieved  :  x    
10
Enter  variable  name  whose  value  is  to  be  retrieved  :  y    
30
Enter  variable  name  whose  value  is  to  be  retrieved  :  z    
Invalid  variable   name   :  z
'''



'''
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
e = Emp()
#How  to  convert  dictionary  to  object  'e'  with  for  loop
for key, value in dict_emp.items():
	setattr(e,key,value)
#How  to  print  object  'e'  with  for  loop
for key in dict_emp.keys():
	print(f"{key}: {getattr(e,key)}")
	


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

Hint:  Import   Rat  class  defined  in  prog10a  but  do  not  define  Rat  class   again
'''




from prog10a import Rat

a=Rat()
b=Rat()
c=Rat()

print('Enter 1st rational number:')
a.get()

print('Enter 2nd rational number:')
b.get()

c.add(a,b)
print('\nAddition result(a+b):',c)

c.sub(a,b)
print('\nsubstraction result(a-b):',c)

c.mul(a,b)
print('\nMultiplication result(a*b):',c)

c.div(a,b)
if c.den!=0:
	print('Division result(a/b):',c)
else:
	print('Division is not permitted')
	


'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''


from prog10a import Rat

a= [Rat() for_in range(6)]
print('Enter 1st rational number:')
a[0].get()

print('Enter 2nd rational number:')
a[1].get()

a[2].add(a[0],a[1])
print('\nAddition result (a[0]+a[1]):'a[2])

a[3].sub(a[0],a[1])
print('\nSubstraction result (a[0]-a[1]):'a[3])

a[4].mul(a[0],a[1])
print('\nMultiplication result (a[0]*a[1]):'a[4])


a[5.div(a[0],a[1])]
if a[5].den!=0:
	print('Division reslut (a[0]/a[1]):',a[5])
else:
	print('Division is not permitted')