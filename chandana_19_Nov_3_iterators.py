#  Find  outputs 
from queue import LifoQueue
s=LifoQueue()
for i in range(1,6):
    s.put(10*i) #  insert  10 , 20 , 30 , 40 , 50  into  stack  object  with  for  loop
print('Deleted  elements')
while not s.empty():
    print(s.get()) #  remove  each  element  of   stack  object  and  also  print
#print(stack . get()) # error
print('End')
'''
o/p:
Deleted  elements
50
40
30
20
10
End
'''


#  Find  outputs 
from queue import PriorityQueue
import random
pq=PriorityQueue()
for i in range(5):
    n=random.randint(1,100)
    pq.put(n) #  insert  5  random  elements  into  object  PriorityQueue   object   with  for  loop
print('Deleted  elements')
while not pq.empty():
    print(pq.get()) #  remove  each  element  of  object  pq  and  also  print
#print(pq . get()) # error : queue id empty
print('End')


# Find  outputs  
from  queue  import  Queue
q = Queue()
q . put(('Hyd',10))
q . put(('Delhi',20))
q . put(('Chennai',15))
q . put(('Pune',5))
q . put(('Mumbai',12))
while not q.empty():
    print(q.get()) #  remove  each  tuple  of  object  'q'  and  also  print
'''
o/p:
('Hyd', 10)
('Delhi', 20)
('Chennai', 15)
('Pune', 5)
('Mumbai', 12)
'''

#  Find  outputs 
from  queue  import   LifoQueue
stack = LifoQueue()
stack . put(('Hyd' , 10))
stack . put(('Delhi' , 20))
stack . put(('Chennai' , 15))
stack . put(('Pune' , 5))
stack . put(('Mumbai' , 12))
while not stack.empty():
    print(stack.get()) #  remove  each  tuple  of  stack  object  and  also  print



#  Find  outputs
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Delhi' , 20))
pq . put(('Chennai' , 15))
pq . put(('Pune' , 5))
pq . put(('Mumbai' , 12))
while not pq.empty():
    print(pq.get()) #  remove  each  tuple  of  object  pq  and  also   print


# Find  outputs
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Hyd' , 20))
pq . put(('Hyd' , 15))
pq . put(('Hyd' , 5))
pq . put(('Hyd' , 12))
print('Deleted tuples')
while not pq.empty():
    print(pq.get()) #  remove  each  tuple  of  object  pq  and  also  print



#print  reversed  object  in  different  ways 
import  time
a = input('Enter  any  string  :  ')  
r1 = reversed(a)
print(type(r1)) # <class 'reversed'>
print(r1) # type and address of r1
print('Iterate  thru  reversed  object  with   next   function')
try:
    while True:
        print(next(r1))
        time.sleep(1)
except StopIteration:
    pass #  iterate  reversed  object  'r'  with  next()  function
print('Iterate  thru  reversed  object  with   __next__   method')
r2=reversed(a)
try:
    while True:
        print(r2.__next__())
except StopIteration:
    pass #  iterate  reversed  object   with  __next__()   method
print('Iterate  thru  reversed  object  with   for  loop')
r3=reversed(a) 
for x in r3:
    print(x) #  iterate  reversed  object   with  for  loop
print('Unpack  reversed  object  : ' ,*reversed(a))
print('List  of  chars  in  reverse  order  :  ' ,list(reversed(a)))
print('Reverse  string   :   ' ,''.join(reversed(a)))


# Find  outputs 
a = 'HYD'
b = reversed(a)
print(type(b)) # <class 'reversed'>
print(b) # type and address of b
print(id(b)) # address of b
print(*b) # D Y H
#print(b[0]) # error
#print(b[1 : 3]) # error
#print(b * 2) # error
#print(len(b)) # error


#Can tuple be reversed ? 
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))
for  x  in   b:
	print(x)
	time . sleep(1)
'''
o/p:
<class 'reversed'>
True
Hyd
10.8
25
'''


#   print  list_reverseiterator  object  in  different  ways  
import   time
a = [25 , 10.8 , 'Hyd' , True]
r1 = reversed(a)
print(type(r1)) # <class 'list_reverseiterator'>
print(r1) # type and address of of r1
print('Iterate   thru  list_reverseiterator  object  with   next()   function')
try:
    while True:
        print(next(r1))
        time.sleep(1)
except StopIteration:
    pass #  iterate   list_reverseiterator  object  with   next()   function
print('Iterate  thru  list_reverseiterator  object  with   _next_()   method')
r2 = reversed(a)
try:
    while True:
        print(r2.__next__())  
        time.sleep(1)
except StopIteration:
    pass #  iterate   list_reverseiterator  object  with   __next__()  method
print('Iterate  thru  list_reverseiterator  object  with   for  loop')
r3 = reversed(a)
for x in r3:
    print(x) #  iterate   list_reverseiterator  object  with   for  loop
print('Unpack  list_reverseiterator  object  :  ' ,*reversed(a))
print('Reverse  list  :  '  ,list(reversed(a)))
      


#  Can  set  be  reversed  ? 
a = {10, 20, 15 , 18}
#r = reversed(a) # set id not reversible as set is unordered



#Can  dictionary  be  reversed  ?
import   time
def   disp(r):
	while  True:
		try:
			print(next(r))
			time.sleep(1)
		except:
			break
a = {10 : 'Rama',20 : 'Sita',15 : 'Kiran',18 : 'Amar'}
r1 = reversed(a.keys())
disp(r1)
r2 = reversed(a.values())
disp(r2)
r3 = reversed(a.items())
disp(r3)
r4 = reversed(a)
disp(r4)
'''
o/p:
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
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint 1:  Both  input  and  output  are  dictionaries

Hint 2:  Use  reversed  iterator
'''
d =eval(input('Enter any dictionary : '))   
print('Original Dictionary :',d)
r =dict(reversed(d.items()))
print('Reversed Dictionary :',r)
'''
o/p:
Enter any dictionary : {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
Original Dictionary : {'Empno': 25, 'Emp Name': 'Rama  Rao', 'Sal': 10000.0}
Reversed Dictionary : {'Sal': 10000.0, 'Emp Name': 'Rama  Rao', 'Empno': 25}
'''



# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
for x in reversed(a.keys()):
    print(x)
    time.sleep(1)
print('Values in reverse order')
for x in reversed(a.values()):
    print(x)
    time.sleep(1)
print('Tuples in reverse order')
for x in reversed(a.items()):
    print(x)
    time.sleep(1)
print('Elements of each tuple in reverse order')
for x in reversed(a.items()):
    print(tuple(reversed(x)))  
    time.sleep(1)
print('Keys and values in reverse order')
for x in reversed(a.items()):
    print(x[0], ':', x[1])    
    time.sleep(1)
'''
o/p:
Keys  in   reverse   order
18
15
20
10
Values in reverse order
Kiran
Rajesh
Sita
Rama rao
Tuples in reverse order
(18, 'Kiran')
(15, 'Rajesh')
(20, 'Sita')
(10, 'Rama rao')
Elements of each tuple in reverse order
('Kiran', 18)
('Rajesh', 15)
('Sita', 20)
('Rama rao', 10)
Keys and values in reverse order
18 : Kiran
15 : Rajesh
20 : Sita
10 : Rama rao
'''