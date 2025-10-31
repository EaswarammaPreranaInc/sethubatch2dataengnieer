# Find  outputs (Home  work)
import   time
list = [25 , 10.8 , 'Hyd' , True]
e = enumerate(list , start = 5)
while   True:
	try:
		print(next(e))
		time . sleep(1)
	except  StopIteration:
		break
print(list[5]) #Error
'''
(5, 25)
(6,10.8)
(7,Hyd)
(8,True)
'''

'''  (Home  work)
Can  string  be  enumerated ?
'''
import   time
a = input('Enter  any  string  :  ') #  Assume  that  input  is  'Hyd'
e = enumerate(a)
while   True:
	try:
		print(next(e))
		time . sleep(1)
	except  StopIteration:
		break
'''
(0, 'H')
(1, 'y')
(2, 'd')
'''

#  Can  set  be  enumerated  ?  (Home  work)
import  time
a = {25 , 10.8 , 'Hyd' , True}
print(a) 
b = enumerate(a)
while   True:
	try:
		print(next(b))
		time . sleep(1)
	except  StopIteration:
		break
'''
{25 , 10.8 , 'Hyd' , True} in any order
(0, 25) #yeild one at a time according to the printed order
(1, 10.8)
(2, 'Hyd')
(3, True)
'''

# Can  dictionary  be  enumerated ?   (Home  work)
import   time
def  disp(e):
	while  True:
		try:
			print(next(e))
			time . sleep(1)
		except:
			break
	print()
a = {'Empno'  :  25 , 'Emp Name'  :  'Rama Rao' , 'Sal' : 10000.0}
e1 = enumerate(a . keys())
disp(e1)
e2 = enumerate(a . values())
disp(e2)
e3 = enumerate(a . items())
disp(e3)
e4 = enumerate(a , start = 5)
disp(e4)
'''
(0, 'Empno')
(1, 'Emp Name')
(2, 'Sal')

(0, 25)
(1, 'Rama Rao')
(2, 10000.0)

(0, ('Empno', 25))
(1, ('Emp Name', 'Rama Rao'))
(2, ('Sal', 10000.0))

(5, 'Empno')
(6, 'Emp Name')
(7, 'Sal')
'''

# Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
'''Write  code  to   print  the  following  outputs  using  enumerate  iterator
Telangana        ... Hyderabad
Andhra  Pradesh  ... Amaravathi
Karnataka        ... Bangalore
TamilNadu        ... Chennai
Maharastra       ... Mumbai'''
e1=enumerate(a)
e2=enumerate(b)
while True:
    try:
        print(next(e1)[1],next(e2)[1],sep='...')
        time.sleep(1)
    except:
        break
    
# How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1)) #<class 'zip'>
print(z1)#Type and Address
print('Iterate  thru  zip  object  with   next()   function')
while True:
    try:
        print(next(z1))#How  to   iterate  thru  zip  object  with  next()  function
        time.sleep(1)
    except:
        break
z2 = zip(a , b)
print('Iterate  thru  zip  object  with  __next__  method')
while True:
    try:
        print(z2.__next__())#How  to   iterate  thru  zip  object  with  next()  function
        time.sleep(1)
    except:
        break
z3= zip(a , b)
print('Iterate  thru  zip  object  with   for  loop')
for x in z3:
    print(x)
    time.sleep(1)#How  to   iterate  thru  zip  object  with  for  loop
print('Iterate  thru  elements  of  each  tuple  in  zip  object')
z4 = zip(a , b)
for x,y in z4:
    print(x,y)
    time.sleep(1)#How  to   iterate  thru  elements  of  each  tuple  of  zip  object  with  for  loop
z5 = zip(a , b)
print('Unpacks  zip  object  with   *  operator  :  ' , *z5)
print()
z6 = zip(a , b)
print('zip   object  in  the  form  of   list  :  ' ,  list(z6))
print()
z7 = zip(a , b)
print('zip   object  in  the  form  of   dictionary :  ' ,  dict(z7))
'''
<class 'zip'>
<zip object at 0x7f9ec7275e80>
Iterate  thru  zip  object  with   next()   function
('Telangana', 'Hyderabad')
('Andhra Pradesh', 'Amaravathi')
('Karnataka ', 'Bangalore')
('Tamilnadu', 'Chennai')
Iterate  thru  zip  object  with  __next__  method
('Telangana', 'Hyderabad')
('Andhra Pradesh', 'Amaravathi')
('Karnataka ', 'Bangalore')
('Tamilnadu', 'Chennai')
Iterate  thru  zip  object  with   for  loop
('Telangana', 'Hyderabad')
('Andhra Pradesh', 'Amaravathi')
('Karnataka ', 'Bangalore')
('Tamilnadu', 'Chennai')
Iterate  thru  elements  of  each  tuple  in  zip  object
Telangana Hyderabad
Andhra Pradesh Amaravathi
Karnataka  Bangalore
Tamilnadu Chennai
Unpacks  zip  object  with   *  operator  :   ('Telangana', 'Hyderabad') ('Andhra Pradesh', 'Amaravathi') ('Karnataka ', 'Bangalore') ('Tamilnadu', 'Chennai')

zip   object  in  the  form  of   list  :   [('Telangana', 'Hyderabad'), ('Andhra Pradesh', 'Amaravathi'), ('Karnataka ', 'Bangalore'), ('Tamilnadu', 'Chennai')]

zip   object  in  the  form  of   dictionary :   {'Telangana': 'Hyderabad', 'Andhra Pradesh': 'Amaravathi', 'Karnataka ': 'Bangalore', 'Tamilnadu': 'Chennai'}

'''

#  Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
c = zip(a , b)
while   True:
	try:
		print(next(c))
		time . sleep(1)
	except  StopIteration:
		break
'''
('Empno', 25)
('Emp Name', 'Rama  Rao')
('Salary', 10000.0)
'''

#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)
'''
('Telangana', 'Hyderabad', 50000000)
('Andhra  Pradesh', 'Amaravathi', 40000000)
('Karnataka', 'Banglore', 70000000)
('TamilNadu', 'Chennai', 60000000)
('Maharastra', 'Mumbai', 30000000)
'''

# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)
	time . sleep(1)
'''
5
7
9
'''

# Find outputs  (Home  work)
import   time
def   disp(z):
	while   True:
		try:
			print(next(z))
			time . sleep(1)
		except:
			break
	print()
a = [10 , 20 ,  30]
b = {1 : 2 , 3 : 4 , 5 : 6}
z1 = zip(a , b . keys())
disp(z1)
z2 = zip(a , b . values())
disp(z2)
z3 = zip(a , b . items())
disp(z3)
z4 = zip(a , b)
disp(z4)
z5 = zip(a)
disp(z5)
z6 = zip(b)
disp(z6)
z7 = zip()
disp(z7)

'''
(10, 1)
(20, 3)
(30, 5)

(10, 2)
(20, 4)
(30, 6)

(10, (1, 2))
(20, (3, 4))
(30, (5, 6))

(10, 1)
(20, 3)
(30, 5)

(10,)
(20,)
(30,)

(1,)
(3,)
(5,)
'''

# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]
print(a)
'''
[[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]
'''

# Find   outputs (Home  work)
from threading import *
import  time
def    disp():
	main_thread() . join(10)
	for  i  in  range(10):
		print('new  thread')
new = Thread(target = disp)
new . start()
for  i  in  range(10):
	print('main  thread')
	time . sleep(2)
'''
main  thread
main  thread
main  thread
main  thread
main  thread
main thread (or) 10 times new thread
main  thread
main  thread
main  thread
main  thread
'''

#  Find  outputs  (Home  work)
from threading import *
import time
def  disp():
	main_thread() . join()
	for  i  in  range(10):
		print('child  thread')
child = Thread(target = disp)
child . start()
child . join()
for  i  in  range(10):
	  print('main  thread')
'''
The child thread waits for main thread expiry
and the main thread waits for child thread expiry
No output
'''

# Find  outputs (Home  work)
from  threading  import *
import  time
def   disp(s):
	print('[' , s , end = '')
	time . sleep(3)
	print(']')
t1 = Thread(target = disp , args = ('Hyd',))
t2 = Thread(target = disp , args = ('Sec',))
t3 = Thread(target = disp , args = ('Cyb',))
t1 . start()
t2 . start()
t3 . start()
'''
[ Hyd[ Sec[ Cyb]
]
]'''

#  Find  outputs (Home  work)
from  threading  import *
import  time
class   Account:
	def    __init__(self , acno1 , bal1):
		self . acno = acno1
		self . bal = bal1
	def    credit(self , amt):
		s = current_thread() . name
		print(F'{s}  is  depositing  Rs. {amt}  into account   {self . acno}')
		x = self . bal
		time . sleep(1)
		self . bal  =  x  +  amt
# End  of  the  class
ac = Account(25 , 1000.0)
print('Initial  Balance :  ' , ac . bal)
t1 = Thread(target = ac . credit ,  args = [100] ,  name = 'Rama')
t2 = Thread(target = ac  . credit , args = (200,) , name = 'Sita')
t1 . start()
t2 . start()
t1 . join()
t2 . join()
print('Final  Balance  :   ' , ac . bal)
'''
Initial  Balance :   1000.0
Rama  is  depositing  Rs. 100  into account   25
Sita  is  depositing  Rs. 200  into account   25
Final  Balance  :   1200
'''