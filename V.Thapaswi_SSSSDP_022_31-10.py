#Find   outputs (Home  work)
from threading import *
import  time
def    disp():
	main_thread() . join(10)#new thread is waiting expriry of main thread
	for  i  in  range(10):
		print('new  thread')
new = Thread(target = disp)#new thread is created
new . start()#executes disp function
for  i  in  range(10):
	print('main  thread')#MainThread get chance
	time . sleep(2)
'''
o/p:
main  thread
main  thread
main  thread
main  thread
main  thread
new  thread
main  thread

new  thread
new  thread
new  thread
new  thread
new  thread
new  thread
new  thread
new  thread
new  thread
main  thread
main  thread
main  thread
main  thread	
'''



#  Find  outputs  (Home  work)
from threading import *
import time
def  disp():
	main_thread() . join()#childthread is waiting for expriry of mainthread 
	for  i  in  range(10):
		print('child  thread')
		time.sleep(2)
child = Thread(target = disp)
child . start()#excutes disp function
child . join()#mainthread is waiting for expiry of childThread 
for  i  in  range(10):
	print('main  thread')
#No outputs bcz both Threads are waitinng for each other forever	



# Find  outputs (Home  work)
from  threading  import *
import  time
def   disp(s):
	print('[' , s , end = '')
	time . sleep(3)#t1 sleeps 3 seconds,t2 sleeps,t3 sleeps
	print(']')#either t1,t2 or t3 get chance to execute
t1 = Thread(target = disp , args = ('Hyd',))
t2 = Thread(target = disp , args = ('Sec',))
t3 = Thread(target = disp , args = ('Cyb',))
t1 . start()#t1 executes disp function with'hyd'
t2 . start()#t2 executes disp function with'sec'
t3 . start()#t3 executes disp function with'cyb'
#MainThread is dead
'''
o/p:
[ [Hyd Sec[ Cyb]]]
'''



#  Find  outputs (Home  work)
from  threading  import *
import  time
class   Account:
	def    __init__(self , acno1 , bal1):#self is ac,acno1=25,bal1=1000.0
		self . acno = acno1
		self . bal = bal1
	def    credit(self , amt):
		s = current_thread() . name#current_thread is t1 .name=Rama,sita
		print(F'{s}  is  depositing  Rs. {amt}  into account   {self . acno}')#Rama is depositing rs.100 into account 25
		#Sita is depositing rs.200 into account 25
		x = self . bal#x=1000(rama)
		               #x=1000(sita)
		time . sleep(1)#rama sleeps for 1 second
		               #sita sleeps for 1 second
		self . bal  =  x  +  amt#1000+100=1100(rama)
		#1000+200=1200
		#t1 is dead
		#t2 dead
# End  of  the  class
ac = Account(25 , 1000.0)#object is created and constructor is executed
print('Initial  Balance :  ' , ac . bal)#Initial Balance:1000.0
t1 = Thread(target = ac . credit ,  args = [100] ,  name = 'Rama')
t2 = Thread(target = ac  . credit , args = (200,) , name = 'Sita')
t1 . start()#t1 executes credit method 
t2 . start()#t2 executes credit method 
t1 . join()#mainthread waiting expriry of nither t1 or t2 ,assume t1 

t2 . join()
print('Final  Balance  :   ' , ac . bal)#Final Balance:1200.0 or 1100.0

'''
object ac-->acno=25,bal=1000.0
'''

'''
o/p:
Initial  Balance :   1000.0
Rama  is  depositing  Rs. 100  into account   25   
Sita  is  depositing  Rs. 200  into account   25   
Final  Balance  :    1200.0
'''


# Find  outputs (Home  work)
import   time
list = [25 , 10.8 , 'Hyd' , True]
e = enumerate(list , start = 5)#yields each element in list from index 5
while   True:
	try:
		print(next(e))#(5,25)
		              #(6,10.8)
					  #(7,'Hyd')
					  #(8,True)
		time . sleep(1)#sleeps 1 seconds for each iteration
	except  StopIteration:
		break
print(list[5])#raises index error



'''
 (Home  work)
Can  string  be  enumerated ?
'''
import   time
a = input('Enter  any  string  :  ') #  Assume  that  input  is  'Hyd'
e = enumerate(a)
while   True:
	try:
		print(next(e))#(0,'h')
		              #(1,'y')
					  #(2,'d') 
					  # after all items exhausted next(e) raises StopIterationError 
		time . sleep(1)#sleeps 1 seconds for each iteration
	except  StopIteration:
		break
#Yes strings can be enumerated bcz string objects have indexs	




#  Can  set  be  enumerated  ?  (Home  work)
import  time
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25,10.8,'Hyd',True}
b = enumerate(a)
while   True:
	try:
		print(next(b))#(0, 25)
					  #(1, 10.8)
					  #(2, 'Hyd')
					  #(3, True)
		time . sleep(1)#sleeps 1 seconds for each iteration
	except  StopIteration:
		break
#yes set can be enumerated in Python, because a set is also an iterable




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
e1 = enumerate(a . keys())#Itreates keys
disp(e1)#executes disp function
e2 = enumerate(a . values())#iterates values
disp(e2)
e3 = enumerate(a . items())#iterates key and value
disp(e3)
e4 = enumerate(a , start = 5)#iterates keys from index 5
disp(e4)
	
'''
o/p:
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

e1=enumerate(a)
while   True:
	try:
		print(next(e1))
		time . sleep(1)
	except  StopIteration:
		break
e2=enumerate(b)
for i , state in enumerate(a):
	print(f'{state:<15}...{b[i]}')

'''
Write  code  to   print  the  following  outputs  using  enumerate  iterator
Telangana        ... Hyderabad
Andhra  Pradesh  ... Amaravathi
Karnataka        ... Bangalore
TamilNadu        ... Chennai
Maharastra       ... Mumbai

'''


# How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z1 = zip(a , b)
print(type(z1))#<class 'zip'>
print(z1)#type and address of object z1
print('Iterate  thru  zip  object  with   next()   function')
while True:
	try:
		print(next(z1))
		time.sleep(2)
	except StopIteration:
		break
#How  to   iterate  thru  zip  object  with  next()  function

print('Iterate  thru  zip  object  with  _next_  method')
z2=zip(a,b)
while True:
	try:
		print(z2.__next__())
		time.sleep(2)
	except StopIteration:
		break	
#How  to   iterate  thru  zip  object  with  __next__()  method
print('Iterate  thru  zip  object  with   for  loop')
z3=zip(a,b)
for i in z3:
	print(i)
	time.sleep(2)
#How  to   iterate  thru  zip  object  with  for  loop
print('Iterate  thru  elements  of  each  tuple  in  zip  object')
z4=zip(a,b)
for x,y in z4:
	print(x,y,sep='...')
#How  to   iterate  thru  elements  of  each  tuple  of  zip  object  with  for  loop
z5=zip(a,b)
print('Unpacks  zip  object  with   *  operator  :  ' , *z5)
print()
z6=zip(a,b)
print('zip   object  in  the  form  of   list  :  ' ,  list(z6))
print()
z7=zip(a,b)
print('zip   object  in  the  form  of   dictionary :  ' ,  dict(z7))
	  




#  Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
c = zip(a , b)
while   True:
	try:
		print(next(c))#('empno',25)
		              #('emp name','ramarao')
					  #('salary',10000.0)
					  #StopIterationError and excess elements ignored
		time . sleep(1)#sleeps one second for each iteration
	except  StopIteration:
		break



#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)#('Telangana','Hyderabad',50000000 )
	        #('Andhra  Pradesh','Amaravathi',40000000 )
			#('Karnataka','Banglore',70000000 )
			#('TamilNadu','Chennai',60000000 )
			#('Maharastra','Mumbai',30000000)
			#raises StopIterationError but for loop internally handled
	time . sleep(1)#sleeps one second for each iteration


# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)#5
	            #7
				#9
				# excess elements are ignored 
	time . sleep(1)




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
disp(z1)#(10,1)
        #(20,3)
		#(30,5)
z2 = zip(a , b . values())
disp(z2)#(10,2)
        #(20,4)
		#(30,6)
z3 = zip(a , b . items())
disp(z3)#(10,(1,2))
        #(20,(3,4))
		#(30,(5,6))
z4 = zip(a , b)
disp(z4)#(10,1)
        #(20,3)
		#(30,5)
z5 = zip(a)
disp(z5)#(10,)
        #(20,)
		#(30,)
z6 = zip(b)
disp(z6)#(1,)
        #(3,)
		#(5')
z7 = zip()
disp(z7)#raises StopIterationError but except suite executed which is nothing



# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))#zip((0,1,2,3,4),(20,21,22,23,24))
a = [ [x , y]  for  x , y   in   z]
print(a)#[[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]
         