'''
Modify  following  program  such  that  results  are  synchronized
i.e.  Outputs  should  be  [Hyd]
						               [Sec]
						               [Cyb]
'''
from  threading  import *
import  time
def   disp(s):
    l.acquire()
    print('[' , s , end = '')
    time . sleep(3)
    print(' ]')
    l.release()
t1 = Thread(target = disp , args = ('Hyd',))
t2 = Thread(target = disp , args = ('Sec',))
t3 = Thread(target = disp , args = ('Cyb',))
l=Lock()
t1 . start()
t2 . start()
t3 . start()

'''
Modify  following  program  such  that  final  balance  should  be  1300
'''
from  threading  import  *
import  time
class   Account:
	def  __init__(self , acno1 , bal1):
		self . acno = acno1
		self . bal = bal1
	def  credit(self , amt):
        l.acquire()
		s = current_thread() . name
		print(F'{s}  is  depositing  Rs. {amt}   into  account   {ac . acno}')
		x = self . bal
		time . sleep(1)
		self . bal = self.bal+ amt
        l.release()
ac = Account( 25 , 1000.0)
print('Initial  Balance :  ' , ac . bal )
t1 = Thread(target = ac . credit , name = 'Rama' , args = (100,))
t2 = Thread(target = ac . credit , name = 'Sita' , args = (200,))
l=Lock()
t1 . start()
t2 . start()
t1 . join()
t2 . join()
print('Final balance :  ' , ac . bal)

'''
Initial  Balance :   1000.0
Rama  is  depositing  Rs. 100   into  account   25
Sita  is  depositing  Rs. 200   into  account   25
Final balance :   1300.0
'''

#  Find  outputs  (Home  work)
from  threading  import  RLock
r = RLock()
r . acquire()
print('Locked')
r . acquire()
print('Locked')
r . release()
print('Unlocked')
r . release()
print('Unlocked')
# r . release() #Error
print('End')
'''
Locked
Locked
Unlocked
Unlocked
End
'''

# Find  outputs  (Home  work)
from threading import *
l = Lock()
l . acquire()
print('Locked')
l . acquire()
print('Locked')
l . release()
print('Unlocked')
l . release()
print('Unlocked')
print('End')  
#Deadlock  occurs  at  second  acquire()  method because  Lock  doesn't  allow  re-acquire  by  same  thread

#  Find  outputs (Home  work)
from threading import *
import time
def   f1():
        sem . acquire()
        name = current_thread() . name
        print(name , 'is   under   execution')
        time . sleep(1)
        print(name , 'finished  execution')
        sem . release()
sem = Semaphore(3)
t1 = Thread(target = f1 , name = 'One')
t2 = Thread(target = f1 , name = 'Two')
t3 = Thread(target = f1 , name = 'Three')
t4 = Thread(target = f1 , name = 'Four')
t5 = Thread(target = f1 , name = 'Five')
t6 = Thread(target = f1 , name = 'Six')
t7 = Thread(target = f1 , name = 'Seven')
t8 = Thread(target = f1 , name = 'Eight')
t9 = Thread(target = f1 , name = 'Nine')
t1 . start()
t2 . start()
t3 . start()
t4 . start()
t5 . start()
t6 . start()
t7 . start()
t8 . start()
t9 . start()
'''
One is   under   execution
Two is   under   execution
Three is   under   execution
One finished  execution
Four is   under   execution
Two finished  execution
Five is   under   execution
Three finished  execution
Six is   under   execution
Four finished  execution
Seven is   under   execution
Five finished  execution
Eight is   under   execution
Six finished  execution
Nine is   under   execution
Seven finished  execution
Eight finished  execution
Nine finished  execution


'''

#  Find  outputs
from  threading  import *
import  time
def    fact(n):
	sem . acquire()
	if   n  >  0:
		x = n * fact(n - 1) # 4*fact(3) 3*fact(2)  2*fact(1)  1*fact(0) 
	else: 
		x = 1
	sem . release()
	return   x
# End of the function
def    disp(n):
	print(n , ' != ' , fact(n))
# End of the function
sem = Semaphore(8)
t1 = Thread(target = disp , args = (4,))
t2 = Thread(target = disp , args = (7,))
t1 . start()
t2 . start()

'''
1   4*fact(3)    24  4 
2   3*fact(2)    6   3
3   2*fact(1)    2   2
4   1*fact(0)  x=1   1

 
1   7*fact(6)    5040  7
2   6*fact(5)    720  6
3   5*fact(4)    120  5
4   4*fact(3)    24  4 
5   3*fact(2)    6   3
6   2*fact(1)    2   2
7   1*fact(0)  x=1   1

4  !=  24
7  !=  5040
'''


#  Find  outputs  (Home  work)
from  threading  import  *
import  time
def  f1():
	l1 . acquire()
	print('1st  thread  locks  object  l1')
	time . sleep(1)
	l2 . acquire()
	print('1st  thread  is  under  execution')
	l2 . release()
	l1 . release()
	print('End  of  the  1st  thread')
def  f2():
	l2 . acquire()
	print('2nd   thread  locks  object  l2')
	time . sleep(1)
	l1 . acquire()
	print('2nd   thread  is  under  execution')
	l1 . release()
	l2 . release()
	print('End  of  the  2nd   thread')
	
#  End  of  the  function
l1 = Lock()
l2 = Lock()
t1 = Thread(target = f1)
t2 = Thread(target = f2)
t1 . start()
t2 . start()
time . sleep(1)
print('Deadlock')

'''
1st  thread  locks  object  l1
2nd   thread  locks  object  l2
Deadlock
'''

#  Find  outputs  (Home  work)
from queue import *
stack=LifoQueue()
for i in range(10,51,10):
    stack.put(i) #How  to  insert  10 , 20 , 30 , 40 , 50  into  stack  object  with  for  loop
print('Deleted  elements')
while not stack.empty():
    print(stack.get())#How  to  remove  each  element  of   stack  object  and  also  print
print(stack . get()) #waiting state because stack is empty
print('End')
'''
Deleted  elements
50
40
30
20
10
'''


#  Find  outputs  (Home  work)
from queue import *
pq=PriorityQueue()
for i in range(10,51,10):
    pq.put(i) #How  to  insert  10 , 20 , 30 , 40 , 50  into  stack  object  with  for  loop
print('Deleted  elements')
while not pq.empty():
    print(pq.get())#How  to  remove  each  element  of   stack  object  and  also  print
print(pq. get()) #waiting state because stack is empty
print('End')
'''
Deleted  elements
10
20
30
40
50
'''



#  Find  outputs  (Home  work)
from queue import *
from random import *

pq=PriorityQueue()
for i in range(5):
    pq.put(randint(1,10))
print('Deleted  elements')
while not pq.empty():
    print(pq.get())
print(pq. get())
print('End')
'''
Deleted  elements
4
6
7
8
9
'''

# Find  outputs  (Home  work)
from  queue  import  Queue
q = Queue()
q . put(('Hyd' , 10))
q . put(('Delhi' , 20))
q . put(('Chennai' , 15))
q . put(('Pune' , 5))
q . put(('Mumbai' , 12))
while not q.empty():
    print(q.get())#How  to  remove  each  tuple  of  object  'q'  and  also  print
'''
('Hyd', 10)
('Delhi', 20)
('Chennai', 15)
('Pune', 5)
('Mumbai', 12)
'''


#  Find  outputs  (Home  work)
from  queue  import   LifoQueue
stack = LifoQueue()
stack . put(('Hyd' , 10))
stack . put(('Delhi' , 20))
stack . put(('Chennai' , 15))
stack . put(('Pune' , 5))
stack . put(('Mumbai' , 12))
while not stack.empty():
    print(stack.get())

'''
('Mumbai', 12)
('Pune', 5)
('Chennai', 15)
('Delhi', 20)
('Hyd', 10)
'''


#  Find  outputs
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Delhi' , 20))
pq . put(('Chennai' , 15))
pq . put(('Pune' , 5))
pq . put(('Mumbai' , 12))
while not pq.empty():
    print(pq.get())
'''
('Chennai', 15)
('Delhi', 20)
('Hyd', 10)
('Mumbai', 12)
('Pune', 5)
'''

# Find  outputs
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Hyd' , 20))
pq . put(('Hyd' , 15))
pq . put(('Hyd' , 5))
pq . put(('Hyd' , 12))
print('Deleted tuples')
while  not pq.empty():
    print(pq.get())
'''
Deleted tuples
('Hyd', 5)
('Hyd', 10)
('Hyd', 12)
('Hyd', 15)
('Hyd', 20)
'''
    
#  Find  outputs (Home  work)
from  threading  import  *
import  time
def  f1():
	for  i  in  range(10): 
		print('child  thread')
		time . sleep(2) 
main = main_thread()
print(main . daemon) 
#main . daemon = True  #Error
new = Thread(target = f1)
print(new . daemon)
new . daemon = True
print(new . daemon)
new . start()
#new . daemon = True #Error
time . sleep(5) # 0 2 4
print('End  of  main  thread')

'''
False
False
True
child  thread
child  thread
child  thread
End  of  main  thread

'''


'''(Home  work)
Find  outputs

Assumption:   Time  is  elapsed  after  5  iterations  of  for  loop  for  each  thread
'''
from  threading  import  *
def    f1():
	name = current_thread() . name
	for  i  in  range(1 , 11):
			print(name , ' : ' , i)
	print(name , 'is  dead')
# End  of  the  function
t1 = Thread(target = f1 , name = 'One')
t2 = Thread(target = f1 , name = 'Two')
t3 = Thread(target = f1 , name = 'Three')
t3 . daemon = True
t1 . start()
t2 . start()
t3 . start()
print('main  thread  is  dead')


'''
main thread is dead
One : 1
One : 2
One : 3
One : 4
One : 5
...
Two : 1
Two : 2
Two : 3
Two : 4
Two : 5
...
Three : 1
Three : 2
Three : 3
Three : 4
Three : 5
One is dead
Two is dead
''' 

#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1)) 
print(r1) 
print('Iterate  thru  reversed  object  with   next   function')
while True:
    try:
        print(next(r1)) #How  to  iterate  reversed  object  'r'  with  next()  function
    except:
        break
print('Iterate  thru  reversed  object  with   __next__   method')
r2 = reversed(a)
while True:
    try:
        print(r2.__next__()) #How  to  iterate  reversed  object  'r'  with  __next__() function
    except:
        break
print('Iterate  thru  reversed  object  with   for  loop')
r3 = reversed(a)
for i in r3:
    print(i) #How  to  iterate  reversed  object   with  for  loop
r4 = reversed(a)
print('Unpack  reversed  object  : ' ,  *r4)
r6 = reversed(a)
print('List  of  chars  in  reverse  order  :  ' , list(r6))
r5 = reversed(a)
print('Reverse  string   :   ' , a[::-1])
'''
Enter  any  string  :  HYD
<class 'reversed'>
<type and address>
Iterate  thru  reversed  object  with   next   function
D
Y
H
Iterate  thru  reversed  object  with   __next__   method
D
Y
H
Iterate  thru  reversed  object  with   for  loop
D
Y
H
Unpack  reversed  object  :  D Y H
List  of  chars  in  reverse  order  :   ['D', 'Y', 'H']
Reverse  string   :    DYH
'''

# Find  outputs (Home  work)
a = 'HYD'
b = reversed(a)
print(type(b)) # class reversed
print(b) #Type and address
print(id(b)) # address
print(*b) # D Y H
print(b[0])#eRROR
print(b[1 : 3]) #eRROR
print(b * 2)#eRROR
print(len(b))#eRROR


# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b)) # class  reversed
print(b) #Type  and  address
for  x  in   b:
	print(x)
	time . sleep(1)
'''
True
Hyd
10.8
25
'''

#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
a = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(a)
print(type(r1))
print(r1)
print('Iterate   thru  list_reverseiterator  object  with   next()   function')
while True:
    try:
        print(next(r1)) #How  to  iterate   list_reverseiterator  object  with   next()  function
    except:
        break
print('Iterate  thru  list_reverseiterator  object  with   __next__()   method')
r2 = reversed(a)
while True:
    try:
        print(r2.__next__()) #How  to  iterate   list_reverseiterator  object  with   __next__()  method
    except:
        break
print('Iterate  thru  list_reverseiterator  object  with   for  loop')
for i in reversed(a):
    print(i) #How  to  iterate   list_reverseiterator  object  with   for  loop
print('Unpack  list_reverseiterator  object  :  ' , *reversed(a))
print('Reverse  list  :  '  ,  list(reversed(a)))

'''
<class 'list_reverseiterator'>
<type  and  address>
Iterate   thru  list_reverseiterator  object  with   next()   function
True
Hyd
10.8
25
'''

#  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a) 
'''
Not  possible  to  reverse  set  because  set  is  unordered 
'''


# Can  dictionary  be  reversed  ? (Home  work)
import   time
def   disp(r):
	while  True:
		try:
			print(next(r))
			time . sleep(1)
		except:
			break
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Kiran' , 18 : 'Amar'}
r1 = reversed(a . keys())
disp(r1)
r2 = reversed(a . values())
disp(r2)
r3 = reversed(a . items())
disp(r3)
r4 = reversed(a)
disp(r4)
'''
18
15
20
10

Amar
Kiran   
Sita
Rama

(18, 'Amar')
(15, 'Kiran')
(20, 'Sita')
(10, 'Rama')

18
15
20
10  
'''


'''
Tricky  program
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint 1:  Both  input  and  output  are  dictionaries

Hint 2:  Use  reversed  iterator
'''

a = {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
b={}
r1 = reversed(a)
for  k  in  r1:
	b[k]=a[k]
print(b)

'''
{'Sal': 10000.0, 'Emp Name': 'Rama  Rao', 'Empno': 25}
'''

# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
r1=reversed(a)
for k in r1:
    print(k)
print('Values  in  reverse  order')
r2=reversed(a.values())
for v in r2:
    print(v)
print('Tuples  in   reverse  order')
r3=reversed(a.items())
for t in r3:
    print(t)
print('Elements  of  each   tuple  in  reverse  order')
for x,y in (a.items()):
    print(str(x)[::-1],str(y)[::-1])
print('Keys  and  values  in   reverse   order')
for x,y in reversed(a.items()):
    print(y,x)

'''
Keys  in   reverse   order
18
15
20
10
Values  in  reverse  order
Kiran
Rajesh
Sita
Rama rao
Tuples  in   reverse  order
(18, 'Kiran')
(15, 'Rajesh')
(20, 'Sita')
(10, 'Rama rao')
Elements  of  each   tuple  in  reverse  order
01 oar amaR
02 atiS
51 hsejaR
81 nariK
Keys  and  values  in   reverse   order
Kiran 18
Rajesh 15
Sita 20
Rama rao 10
'''