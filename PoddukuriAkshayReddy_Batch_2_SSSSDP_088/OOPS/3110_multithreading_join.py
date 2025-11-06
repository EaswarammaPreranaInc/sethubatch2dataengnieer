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
0 - main thread
2 - main thread
4 - main thread
6 - main thread
8 - main thread
10 - main thread or 10 times new thread
12 - main thread
14 - main thread
16 - main thread
18 - main thread


'''
    
    
    
#  Find  outputs  (Home  work)
from threading import *
import time
def  disp():
	main_thread() . join() # child thread waits for main thread expiry
	for  i  in  range(10):
		print('child  thread')
child = Thread(target = disp)
child . start()
child . join() # main thread waits for child thread expiry
for  i  in  range(10):
	  print('main  thread')
'''

this a example for deadlock beacuse each thread waits for 
each other thread expiry  this is a dead lock

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
]
    
'''
    
#  Find  outputs (Home  work)
from  threading  import *
import  time
class   Account:
	def  __init__(self , acno1 , bal1):
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



'''



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
print(list[5])

    
    
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
[31-10-2025 14:18] SRINIVAS Sir SSSSDP: #  Can  set  be  enumerated  ?  (Home  work)
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
[31-10-2025 14:19] SRINIVAS Sir SSSSDP: # Can  dictionary  be  enumerated ?   (Home  work)
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
[31-10-2025 14:19] SRINIVAS Sir SSSSDP: # Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
Write  code  to   print  the  following  outputs  using  enumerate  iterator
Telangana        ... Hyderabad
Andhra  Pradesh  ... Amaravathi
Karnataka        ... Bangalore
TamilNadu        ... Chennai
Maharastra       ... Mumbai
[31-10-2025 14:44] SRINIVAS Sir SSSSDP: # How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1))
print(z1)
print('Iterate  thru  zip  object  with   next()   function')
How  to   iterate  thru  zip  object  with  next()  function
print('Iterate  thru  zip  object  with  _next_  method')
How  to   iterate  thru  zip  object  with  _next_()  method
print('Iterate  thru  zip  object  with   for  loop')
How  to   iterate  thru  zip  object  with  for  loop
print('Iterate  thru  elements  of  each  tuple  in  zip  object')
How  to   iterate  thru  elements  of  each  tuple  of  zip  object  with  for  loop
print('Unpacks  zip  object  with   *  operator  :  ' , ???)
print()
print('zip   object  in  the  form  of   list  :  ' ,  ???)
print()
print('zip   object  in  the  form  of   dictionary :  ' ,  ???)
[31-10-2025 14:44] SRINIVAS Sir SSSSDP: #  Find  outputs  (Home  work)
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
[31-10-2025 14:44] SRINIVAS Sir SSSSDP: #  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)
[31-10-2025 14:44] SRINIVAS Sir SSSSDP: # Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)
	time . sleep(1)
[31-10-2025 14:45] SRINIVAS Sir SSSSDP: # Find outputs  (Home  work)
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
[31-10-2025 14:45] SRINIVAS Sir SSSSDP: # Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]
print(a)