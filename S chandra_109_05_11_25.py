: # Producer-Consumer  problem
from  threading  import  *
import  time
from  random  import  randint
class  buffer:
	def   store(self ,  y):
		s = current_thread() . name
		self . x  =  y
		print(s  ,  'stores' ,  self . x)
	def   ret(self):
		s = current_thread() . name
		print(s  ,  'retrieves' ,  self . x)
def   f1(buf):
	i = 1
	while  True:
		buf . store(i)
		i += 1
		time . sleep(randint(1 , 4))
def  f2(buf):
	while  True:
		buf . ret()
		time . sleep(randint(1 , 4))
# End  of  the  function
buf = buffer()
p  = Thread(target = f1 , name = 'producer' , args = (buf,))
c  = Thread(target = f2 , name = 'consumer' , args = (buf,))
p . start()
c . start()
print('Press  ctrl + break  or  Fn+B  to  stop')
#################################
Press ctrl + break or Fn+B to stop
producer stores 1
consumer retrieves 1
producer stores 2
consumer retrieves 2
consumer retrieves 2
producer stores 3
producer stores 4
consumer retrieves 4
...




: # How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
How  to  iterate  list  with  for  loop
print(next(list))
list_itr1 = iter(list)
print(type(list_itr1))
print(list_itr1)
print('Iterate   thru  list_iterator  with  next()  function')
How  to  iterate  list_iterator  with  next()  function
print('Iterate  thru  list_iterator  with   _next_()  method')
How  to  iterate  list_iterator  with   _next_  method
print('Iterate   thru  list_iterator  with   for    loop')
How  to  iterate  list_iterator  with  for  loop
print('Unpacks  List_iterator   :    ' ,  ???)
##############################
import time
list = [10, 20, 15, 18]
print('Iterate list with for loop')
for x in list:
    print(x)

list_itr1 = iter(list)
print(type(list_itr1))
print(list_itr1)

print('Iterate thru list_iterator with next() function')
print(next(list_itr1))
print(next(list_itr1))
print(next(list_itr1))
print(next(list_itr1))

# Or re-create it again
list_itr2 = iter(list)
print('Iterate thru list_iterator with for loop')
for x in list_itr2:
    print(x)

print('Unpacks List_iterator :', *iter(list))
#################################
Iterate list with for loop
10
20
15
18
<class 'list_iterator'>
<list_iterator object at 0x000001E5C6DCC0A0>
Iterate thru list_iterator with next() function
10
20
15
18
Iterate thru list_iterator with for loop
10
20
15
18
Unpacks List_iterator : 10 20 15 18





: # Find  outputs
a = 25
print(a)
for  x   in   a:
	print(x)
print(iter(a))
print(next(a))
#######################
25
Traceback (most recent call last):
  File "...", line 3, in <module>
    for x in a:
TypeError: 'int' object is not iterable





: '''
Modify  following  program  such  that

1) Use  regular  function  instead  of  lambda  function

2) Use  for  loop  to  iterate  filter  instead  of  while  loop
'''
import  time
list = [25 , 9 , 10 , 15 ,  17 , 24 , 35 , 47 , 0 , 19 , 53 , 18 , 65 , 83]
f = filter(lambda  x :  x % 2 == 0  , list)
print(type(f))
print(f)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except  StopIteration:
		break

###############################

import time
def even_check(x):
    return x % 2 == 0

list = [25, 9, 10, 15, 17, 24, 35, 47, 0, 19, 53, 18, 65, 83]
f = filter(even_check, list)

print(type(f))
print(f)

for val in f:
    print(val)
    time.sleep(1)
########################
<class 'filter'>
<filter object at 0x000001E5C6DCC0A0>
10
24
0
18





: # Find  outputs (Home  work)
import  time
list = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda   x :   True ,   list)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

#################################
25
10.8
(3+4j)
Hyd
False




: #  Find  outputs (Home  work)
import  time
list = [25 , 10.8 , 3 + 4j ,  'Hyd' , True]
f = filter(lambda  x  :  False ,  list)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

###################################
The lambda returns False for every element → nothing passes through.

So the filter object is empty.

 Output:-(no output)





: # Find  outputs (Home  work)
import  time
list = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda   x   :   x   ,   list)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
##################################
25
10.8
(3+4j)
Hyd
(25,)

lambda x: x → passes all truthy elements.
Falsy values in Python: False, 0, 0.0, '', (), [], None.





: # Find outputs
import  time
def  disp(f):
	while  True:
		try:
			print(next(f))
			time . sleep(1)
		except:
			break
list = [10 , 0 ,  -25 , () , (25,) , 'Hyd', '' , [] , 10.8 , 0.0 , [10 , 20] , True , False]
f1 = filter(lambda  x : None  , list)
print('Filter  f1')
disp(f1)
f2 = filter(None  , list)
print('Filter  f2')
disp(f2)
########################
f1 = filter(lambda x: None, list)

The lambda always returns None → treated as False → no elements pass.

f2 = filter(None, list)

The filter automatically removes all falsy values.

Filter f1
(no output)
Filter f2
10
-25
(25,)
Hyd
10.8
[10, 20]
True




: # Find outputs  (Home  work)
import  time
list = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , list)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
#######################################
Rama Rao
Rajesh
Kiran
Amar
Manohar
Vamsi





: # Find  outputs (Home  work)
import   time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda   x  :   x[1]  >=  12 , list)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
########################################
('B', 20)
('C', 15)
('E', 18)





: # Find  outputs (Home  work)
import   time
list = [
             {
                'Roll Num' :  10 ,
                'Stud Name' : 'Rama Rao' ,
                'Marks' : 75
              } ,
              {
                'Roll Num' :  20 ,
                'Stud Name' : 'Sita' ,
                'Marks' : 52
              } ,
             {
               'Roll Num'  :  15 ,
               'Stud Name' : 'Kiran' ,
               'Marks' : 65
             } ,
             {
               'Roll Num'  :  18 ,
               'Stud Name' : 'Amar' ,
               'Marks' : 48
             } ,
             {
               'Roll Num' :  5 ,
               'Stud Name' : 'Rajesh' ,
               'Marks' : 82
             }
        ]
f = filter(lambda  x :  x['Marks'] >= 60 , list)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

########################################
{'Roll Num': 10, 'Stud Name': 'Rama Rao', 'Marks': 75}
{'Roll Num': 15, 'Stud Name': 'Kiran', 'Marks': 65}
{'Roll Num': 5, 'Stud Name': 'Rajesh', 'Marks': 82}





: # Find  outputs (Home  work)
import  time
def  disp(f):
	while  True:
		try:
			print(next(f))
			time . sleep(1)
		except:
			break
list = [   { 'country' : 'India' , 'sale' : 150.5} ,
          { 'country' : 'china' , 'sale' : 200.2} ,
          { 'country' : 'USA' , 'sale' : 300.3} ,
          { 'country' : 'UK' , 'sale' : 210.4} ]
f1 = filter (lambda  x  :   x['country'] . startswith('U') , list)
print('Filter  f1')
disp(f1)
f2 = filter(lambda  x  :  x['sale']  >=  200  , list)
print('Filter  f2')
disp(f2)
#####################################
Filter f1
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}
Filter f2
{'country': 'china', 'sale': 200.2}
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}




: # How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f1 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  thru  filter  object  with   next   function')
How  to iterate  thru  filter  object  with  next()  function
print('Iterate  thru  filter  object  with   for  loop')
How  to iterate  thru  filter  object  with  for  loop
print('Unpack  filter  object :  ' ,  ???)
print('filter  object  converted  to   list  :  ' ,  ???)
######################################
import time
a = [10, 15, 20, 17, 18, 19, 26]
f1 = filter(lambda x: x % 2 == 0, a)

print('Iterate thru filter object with next function')
f2 = filter(lambda x: x % 2 == 0, a)
while True:
    try:
        print(next(f2))
    except StopIteration:
        break

print('Iterate thru filter object with for loop')
f3 = filter(lambda x: x % 2 == 0, a)
for x in f3:
    print(x)

print('Unpack filter object:', *filter(lambda x: x % 2 == 0, a))
print('filter object converted to list:', list(filter(lambda x: x % 2 == 0, a)))

############################################
Iterate thru filter object with next function
10
20
18
26
Iterate thru filter object with for loop
10
20
18
26
Unpack filter object: 10 20 18 26
filter object converted to list: [10, 20, 18, 26]




: #  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator

######################
f = filter(lambda x: x % 2 != 0, range(1, 21))
for x in f:
    print(x)
########################
1
3
5
7
9
11
13
15
17
19





: Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
Input  is  string  and  output  is  set
##############################
s = input('Enter a string: ')
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
f = filter(lambda ch: ch in vowels, s)
print('Distinct vowels are:', set(f))
####################
Enter a string: Education
Distinct vowels are: {'a', 'E', 'i', 'o', 'u'}





: # Nested  filter  i.e.  filter  on  filter
import   time
list =  [ (10 , 'Rama' , 10000.0) ,
            (20, 'Sita' , 7000.0) ,
            (15 , 'Rajesh' , 15000.0) ,
            (5 , 'Amar' ,  12000.0) ,
            (18 , 'Ramesh' , 8000.0) ]
f = filter(lambda  x :  x[1] . startswith('R')  , filter(lambda  x :  x[2] >= 10000 , list))
while   True:
	try:
		print(next(f))
		time .  sleep(1)
	except:
		break
#####################################
(10, 'Rama', 10000.0)
(15, 'Rajesh', 15000.0)
