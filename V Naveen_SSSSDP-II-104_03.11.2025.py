#1. Find  outputs (Home  work)
import   time
list = [25 , 10.8 , 'Hyd' , True]
e = enumerate(list , start = 5)
while   True:
	try:
		print(next(e)) # (5, 25) <nextline> (6, 10.8) <nextline> (7, 'Hyd') <nextline> (8, True)
		time . sleep(1)
	except  StopIteration:
		break
#print(list[5]) # IndexError




#2. Can  string  be  enumerated ? YES
import   time
a = input('Enter  any  string  :  ') #  Assume  that  input  is  'Hyd'
e = enumerate(a)
while   True:
	try:
		print(next(e)) # (0, 'H') <nextline> (1, 'y') <nextline> (2, 'd')
		time . sleep(1)
	except  StopIteration:
		break




#3.  Can  set  be  enumerated  ? YES  (Home  work)
import  time
a = {25 , 10.8 , 'Hyd' , True}
print(a)
b = enumerate(a)
while   True:
	try:
		print(next(b)) # (0, 25) <nextline> (1, 10.8) <nextline> (2, 'Hyd') <nextline> (3, True)  (in any order)
		time . sleep(1)
	except  StopIteration:
		break





#4. Can  dictionary  be  enumerated ?   (Home  work)
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
disp(e1) # (0, 'Empno') <nextline> (1, 'Emp Name') <nextline> (2, 'Sal')
e2 = enumerate(a . values())
disp(e2) # (0, 25) <nextline> (1, 'Rama Rao') <nextline> (2, 10000.0)
e3 = enumerate(a . items())
disp(e3) # (0, ('Empno', 25)) <nextline> (1, ('Emp Name', 'Rama Rao')) <nextline> (2, ('Sal', 10000.0))
e4 = enumerate(a , start = 5)
disp(e4) # (5, 'Empno') <nextline> (6, 'Emp Name') <nextline> (7, 'Sal')




#5. Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
#Write  code  to   print  the  following  outputs  using  enumerate  iterator
l = zip(a, b) 
for state, city in l:
    print(f"{state:15} ... {city}")
    time.sleep(1)
#Telangana        ... Hyderabad
#Andhra  Pradesh  ... Amaravathi
#Karnataka        ... Bangalore
#TamilNadu        ... Chennai
#Maharastra       ... Mumbai




#6. How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1))
print(z1)
print('Iterate  thru  zip  object  with   next()   function')
while True :
    try:
        print(next(z1)) # How  to   iterate  thru  zip  object  with  next()  function
        time.sleep(1)
    except StopIteration:
        break
print('Iterate  thru  zip  object  with  _next_  method')
z2 = zip(a , b)
while True : 
    try:
        print(z2.__next__()) # How  to   iterate  thru  zip  object  with  _next_()  method
        time.sleep(1)
    except StopIteration:
        break
print('Iterate  thru  zip  object  with   for  loop')
z3 = zip(a , b)
for i in z3:
    print(i) # How  to   iterate  thru  zip  object  with  for  loop
    time.sleep(1)
print('Iterate  thru  elements  of  each  tuple  in  zip  object')
z4 = zip(a , b)
for i , j in z4:
    print(f"{i}  --->  {j}") # How  to   iterate  thru  elements  of  each  tuple  of  zip  object  with  for  loop
    time.sleep(1)
z5 = zip(a , b)
print('Unpacks  zip  object  with   *  operator  :  ' , *z5)
print()
z6 = zip(a , b)
print('zip   object  in  the  form  of   list  :  ' ,  list(z6))
print()
z7 = zip(a , b)
print('zip   object  in  the  form  of   dictionary :  ' ,  dict(z7))





#7.  Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
c = zip(a , b)
while   True:
	try:
		print(next(c)) # ( 'Empno' , 25) <nextline> ( 'Emp Name' , 'Rama  Rao') <nextline> ( 'Salary' , 10000.0)
		time . sleep(1)
	except  StopIteration:
		break





#8.  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x) # ('Telangana', 'Hyderabad', 50000000) <nextline> ('Andhra  Pradesh', 'Amaravathi', 40000000) <nextline> ('Karnataka', 'Banglore', 70000000) <nextline> ('TamilNadu', 'Chennai', 60000000) <nextline> ('Maharastra', 'Mumbai', 30000000)
	time . sleep(1)





#9. Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y) # 5 <nextline> 7 <nextline> 9
	time . sleep(1)





#10. Find outputs  (Home  work)
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
disp(z1) # (10, 1) <nextline> (20, 3) <nextline> (30, 5)
z2 = zip(a , b . values())
disp(z2) # (10, 2) <nextline> (20, 4) <nextline> (30, 6)
z3 = zip(a , b . items())
disp(z3) # (10, (1, 2)) <nextline> (20, (3, 4)) <nextline> (30, (5, 6))
z4 = zip(a , b)
disp(z4) # (10, 1) <nextline> (20, 3) <nextline> (30, 5)
z5 = zip(a)
disp(z5) # (10,) <nextline> (20,) <nextline> (30,)
z6 = zip(b)
disp(z6) # (1,) <nextline> (3,) <nextline> (5,)
z7 = zip()
disp(z7) # No  output





#11. Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]
print(a) # [[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]





#12. Find   outputs (Home  work)
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
# 5 times  'main  thread'  ,  10  times  'new  thread' and 5 times  'main  thread'
# 6 times  'main  thread'  ,  10  times  'new  thread' and 4 times  'main  thread'





#13.  Find  outputs  (Home  work)
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
# infinte loop 





#14. Find  outputs (Home  work)
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
# Possible outputs :
# [Hyd[Sec[Cyb]
#]
#]





#15.  Find  outputs (Home  work)
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
#Initial  Balance :   1000.0
#Rama  is  depositing  Rs. 100  into account   25
#Sita  is  depositing  Rs. 200  into account   25
#Final  Balance  :    1200.0