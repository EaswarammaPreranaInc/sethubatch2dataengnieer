'''
1) Modify  following  program  such  that  results  are  synchronized
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




#2) Modify  following  program  such  that  final  balance  should  be  1300
from threading import *
import time
class Account:
    def __init__(self, acno1, bal1):
        self.acno = acno1
        self.bal = bal1
    def credit(self, amt):
        l.acquire()
        s = current_thread().name
        print(f'{s} is depositing Rs. {amt} into account {self.acno}')
        x = self.bal
        time.sleep(1)
        self.bal = x + amt
        l.release()
l = Lock()
ac = Account(25, 1000.0)
print('Initial Balance:', ac.bal)
t1 = Thread(target=ac.credit, name='Rama', args=(100,))
t2 = Thread(target=ac.credit, name='Sita', args=(200,))
t1.start()
t2.start()
t1.join()
t2.join()
print('Final balance:', ac.bal)


# 3)  Find  outputs  (Home  work)
from  threading  import  RLock
r = RLock()
r . acquire() 
print('Locked') #Locked
r . acquire()
print('Locked') #Locked
r . release()
print('Unlocked') #Unlocked
r . release()
print('Unlocked') #Unlocked
r . release() #Error
print('End')

# 4) Find  outputs  (Home  work)
from threading import *
l = Lock()
l . acquire() 
print('Locked') #Locked
l . acquire() #infinite waiting for object 'l'
print('Locked') 
l . release() #Not executed 
print('Unlocked')
l . release()
print('Unlocked')
print('End')


# 5)  Find  outputs (Home  work)
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
from here on outputs cant be predicted
'''

# 6)  Find  outputs
from  threading  import *
import  time
def    fact(n):
	sem . acquire()
	if   n  >  0:
		x = n * fact(n - 1)
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
    lock        x value     unlock
1   4*6         24             4
2   3*2         6              3
3   2*1         2              2
4   1*fact(0)   x=1            1

4 != 24
7 !=5040
'''

# 7)  Find  outputs  (Home  work)
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
DeadLock

Then t1 waits for L2
and t2 waits for L1
which results in Deadlock
'''



# 8)  Find  outputs  (Home  work)
from queue import LifoQueue
stack=LifoQueue()
for i in range(10,51,10):
    stack.put(i)#How  to  insert  10 , 20 , 30 , 40 , 50  into  stack  object  with  for  loop
print('Deleted  elements')
while not stack.empty():
    print(stack.get())#How  to  remove  each  element  of   stack  object  and  also  print
print(stack . get()) #Thread goes to waiting state
print('End')
'''
Deleted  elements
50
40
30
20
10


'''

# 9)  Find  outputs  (Home  work)
import random
from queue import PriorityQueue
pq=PriorityQueue()
for i in range(1,6):
    x=random.randint(1,10)
    pq.put(i*x)
print('Deleted  elements')
while pq.empty():
    print(pq.get())
print(pq . get()) #Thread goes to waiting state
print('End')
'''
Deleted  elements
4
5
15
16
24


'''

#10)  Find  outputs  (Home  work)
from  queue  import  Queue
q = Queue()
q . put(('Hyd' , 10))
q . put(('Delhi' , 20))
q . put(('Chennai' , 15))
q . put(('Pune' , 5))
q . put(('Mumbai' , 12))
while not q.empty():
    print(q.get())
#How  to  remove  each  tuple  of  object  'q'  and  also  print
'''
('Hyd', 10)
('Delhi', 20)
('Chennai', 15)
('Pune', 5)
('Mumbai', 12)

'''

# 11)  Find  outputs  (Home  work)
from  queue  import   LifoQueue
stack = LifoQueue()
stack . put(('Hyd' , 10))
stack . put(('Delhi' , 20))
stack . put(('Chennai' , 15))
stack . put(('Pune' , 5))
stack . put(('Mumbai' , 12))
while not stack.empty():
    print(stack.get())
#How  to  remove  each  tuple  of  stack  object  and  also  print
'''
('Mumbai', 12)
('Pune', 5)
('Chennai', 15)
('Delhi', 20)
('Hyd', 10)
'''
# 12)  Find  outputs
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Delhi' , 20))
pq . put(('Chennai' , 15))
pq . put(('Pune' , 5))
pq . put(('Mumbai' , 12))
while not pq.empty():
    print(pq.get())
#How  to  remove  each  tuple  of  object  pq  and  also   print
'''
('Chennai', 15)
('Delhi', 20)
('Hyd', 10)
('Mumbai', 12)
('Pune', 5)
'''

# 13)  Find  outputs (Home  work)
from  threading  import  *
import  time
def  f1():
	for  i  in  range(10):
		print('child  thread')
		time . sleep(2)
main = main_thread()
print(main . daemon)
main . daemon = True #Error
new = Thread(target = f1)
print(new . daemon)
new . daemon = True
print(new . daemon)
new . start()
new . daemon = True #Error
time . sleep(5)
print('End  of  main  thread')
'''
False
False
True
Child thread
Child thread
Child thread
End  of  main  thread
'''

'''14) (Home  work)
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
One : 1
One : 2
One : 3
One : 4
One : 5
Two : 1
Two : 2
Two : 3
Two : 4
Two : 5
Three : 1
Three : 2
Three : 3
Three : 4
Three : 5
from here on outputs cant be predicted (incase t1 and t2 are before t3 then t3 remaining time slot will not be executed)
'''
# 15)  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r1 = reversed(a)
print(type(r1))
print(r1)
print('Iterate  thru  reversed  object  with   next   function')
while True:
    try:
        print(next(r1))
        time.sleep(1)
    except:
        break #How  to  iterate  reversed  object  'r'  with  next()  function
print('Iterate  thru  reversed  object  with   __next__   method')
r2 = reversed(a)
while True:
    try:
        print(r2.__next__())
        time.sleep(1)
    except:
        break #How  to  iterate  reversed  object   with  __next__()   method
print('Iterate  thru  reversed  object  with   for  loop')
r3 = reversed(a)
for x in r3:
    print(x) 
    time.sleep(1)#How  to  iterate  reversed  object   with  for  loop
r4 = reversed(a)
print('Unpack  reversed  object  : ' ,  *r4)
r5 = reversed(a)
print('List  of  chars  in  reverse  order  :  ' ,  list(r5))
print('Reverse  string   :   ' , a[::-1])
'''
<class 'reversed'>
<reversed object at 0x7dc15be05e10>
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

# 16) Find  outputs (Home  work)
a = 'HYD'
b = reversed(a)
print(type(b))
print(b)
print(id(b))
print(*b)
print(b[0]) #Error
print(b[1 : 3]) #Error
print(b * 2) #Error
print(len(b)) #Error
'''
<class 'reversed'
Type and Address
Address of b
DYH
'''
#17)  Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))
for  x  in   b:
	print(x)
	time . sleep(1)
'''
<class 'reversed'>
True
Hyd
10.8
25
'''

# 18)  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
a = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(a)
print(type(r1))
print(r1)
while True:
    try:
        print(next(r1))
        time.sleep(1)
    except:
        break #How  to  iterate  reversed  object  'r'  with  next()  function
print('Iterate  thru  reversed  object  with   __next__   method')
r2 = reversed(a)
while True:
    try:
        print(r2.__next__())
        time.sleep(1)
    except:
        break #How  to  iterate  reversed  object   with  __next__()   method
print('Iterate  thru  reversed  object  with   for  loop')
r3 = reversed(a)
for x in r3:
    print(x) 
    time.sleep(1)#How  to  iterate  reversed  object   with  for  loop
r4 = reversed(a)
print('Unpack  reversed  object  : ' ,  *r4)
r5 = reversed(a)
print('List  of  chars  in  reverse  order  :  ' ,  list(r5))
print('Reverse  string   :   ' , a[::-1])
'''
<class 'list_reverseiterator'>
<list_reverseiterator object at 0x78b9a550dba0>
True
Hyd
10.8
25
Iterate  thru  reversed  object  with   __next__   method
True
Hyd
10.8
25
Iterate  thru  reversed  object  with   for  loop
True
Hyd
10.8
25
Unpack  reversed  object  :  True Hyd 10.8 25
List  of  chars  in  reverse  order  :   [True, 'Hyd', 10.8, 25]
Reverse  string   :    [True, 'Hyd', 10.8, 25]
'''

#19)  Can  set  be  reversed  ?  (Home  work)
a = {10, 20, 15 , 18}
r = reversed(a) #Cannot reverse a set as it is unordered

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
(18 : 'Amar')
(15 : 'Kiran')
(20 : 'Sita')
(10 : 'Rama')
18
15
20
10
'''

'''
20) Tricky  program
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint 1:  Both  input  and  output  are  dictionaries

Hint 2:  Use  reversed  iterator
'''
a={'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
r1=reversed(a)
b={}
for x in r1:
    b[x]=a[x]
print(b)

# 21) Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
r1=reversed(a.keys())
print('Keys  in   reverse   order')
for x in r1: 
    print(x)
    time.sleep(1)
r2=reversed(a.values())
print('Values  in  reverse  order')
for x in r2: 
    print(x)
    time.sleep(1)
r3=reversed(a.items())
print('Tuples  in   reverse  order')
for x in r3:
    print(x)
    time.sleep(1)
print('Elements  of  each   tuple  in  reverse  order')
for x,y in a.items():
    print(str(x)[::-1],end=' ')
    print(y[::-1])
    time.sleep(1)
print('Keys  and  values  in   reverse   order')
for x,y in a.items():
    print(y,x,sep='\t')