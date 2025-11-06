
# Producer-Consumer  problem
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
'''
3 problems in this problem as we cannot predict the output and 
1) Producer  may  overwrite  the  value  before  consumer  reads  it
2) Consumer  may  read  the  same  value  again  and  again
3) Producer  and  Consumer  may  access  the  buffer  at  the  same  time
'''
    
    
    
# How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]

print('Iterate  list  with  for  loop')
for x in list:
    print(x)
# How  to  iterate  list  with  for  loop
print(next(list)) # TypeError: 'list' object is not an iterator
list_itr1 = iter(list) # sequence is converted to iterator and iterator are always empty. 
print(type(list_itr1)) # list_iterator
print(list_itr1) # list_iterator object
print('Iterate   thru  list_iterator  with  next()  function')
while True:
    try:
        print(next(list_itr1))
    except StopIteration:
        break
		# time . sleep(1)
# How  to  iterate  list_iterator  with  next()  function
print('Iterate  thru  list_iterator  with   _next_()  method')
list_iter2 = iter(list)
while True:
    try:
        print(list_iter2.__next__())
    except:
        break
        
    
# How  to  iterate  list_iterator  with   _next_  method
print('Iterate   thru  list_iterator  with   for    loop')
list_iter3 = iter(list)
for y in list_iter3:
    print(y)
# How  to  iterate  list_iterator  with  for  loop
list_iter4 = iter(list)

print('Unpacks  List_iterator   :    ' ,  *list_iter4)



# Find  outputs
a = 25
print(a) # 25
for  x   in   a: # error
	print(x)
print(iter(a)) # error
print(next(a)) # error



'''
Modify  following  program  such  that

1) Use  regular  function  instead  of  lambda  function

2) Use  for  loop  to  iterate  filter  instead  of  while  loop
'''
import  time
def even(x):
    return x % 2 == 0
    
list = [25 , 9 , 10 , 15 ,  17 , 24 , 35 , 47 , 0 , 19 , 53 , 18 , 65 , 83]
f = filter(even ,list)
print(type(f))
print(f)
for y in f:
    print(y)


    
    
# Find  outputs (Home  work)
import  time
list = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda   x :   True ,   list)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
'''
25
10.8
(3+4j)
Hyd
False
'''

#  Find  outputs (Home  work)
import  time
list = [25 , 10.8 , 3 + 4j ,  'Hyd' , True]
f = filter(lambda  x  :  False ,  list)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
# no outputs
    
    
# Find  outputs (Home  work)
import  time
list = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda   x   :   x   ,   list)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
'''
25
10.8
(3+4j)
Hyd
(25,)
'''
    
    
    
# Find outputs
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
'''
Filter  f1
Filter  f2
10
-25
(25,)
Hyd
10.8
[10, 20]
True
'''
    
    
# Find outputs  (Home  work)
import  time
list = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , list)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
'''
Rama Rao
Rajesh
Kiran
Manohar
Vamsi
'''
    
    
# Find  outputs (Home  work)
import   time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda   x  :   x[1]  >=  12 , list)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
'''
('B', 20)
('C', 15)
('E', 18)
'''

    
    
# Find  outputs (Home  work)
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
'''
{'Roll Num': 10, 'Stud Name': 'Rama Rao', 'Marks': 75}
{'Roll Num': 15, 'Stud Name': 'Kiran', 'Marks': 65}
{'Roll Num': 5, 'Stud Name': 'Rajesh', 'Marks': 82}
'''
    
    

# Find  outputs (Home  work)
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
'''

Filter  f1
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}
Filter  f2
{'country': 'china', 'sale': 200.2}
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}
'''
    
    
    
# How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f1 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  thru  filter  object  with   next   function')
# How  to iterate  thru  filter  object  with  next()  function

while True:
    try:
        print(next(f1))
        time.sleep(1)
    except:
        break
        
print('Iterate  thru  filter  object  with   for  loop')
# How  to iterate  thru  filter  object  with  for  loop
f2 = filter(lambda  x  :  x  %  2  ==  0 , a)

for y in f2:
    print(y)
    time.sleep(1)
    
    
f3 = filter(lambda  x  :  x  %  2  ==  0 , a)

print('Unpack  filter  object :  ' ,  *f3)

f4 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('filter  object  converted  to   list  :  ' , list(f4) )


#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator
import time
f = filter(lambda x : x % 2 == 1, range(1,21))
for y in f:
    print(y)
    time.sleep(2)

    
    
# Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
# Input  is  string  and  output  is  set
s = input("Enter mixed case string: ")
s = s.upper()
vowel = 'AEIOU'
f = filter(lambda ch : ch in vowel , s)
print(set(f))
    
'''
{'A', 'O'}
'''
    
# Nested  filter  i.e.  filter  on  filter
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
'''
(10, 'Rama', 10000.0)
(15, 'Rajesh', 15000.0)

'''