# How  to  iterate   list_iterator  in  different  ways
import time
list = [10,20,15,18]
print('Iterate  list  with  for  loop')
r1=reversed(list)
for x in r1:
    print(x) # How  to  iterate  list  with  for  loop
#print(next(list)) # error : list is not iterable
list_itr1 = iter(list)
print(type(list_itr1)) # <class 'list_iterator'>
print(list_itr1) # type and address of list_itr1
print('Iterate   thru  list_iterator  with  next()  function')
r2=reversed(list)
try:
    while True:
        print(next(r2))
        time.sleep(0.5)
except StopIteration:
    pass # How  to  iterate  list_iterator  with  next()  function
print('Iterate thru list_iterator with __next__()  method')
r3=reversed(list)
try:
    while True:
        print(r3.__next__())
        time.sleep(0.5)
except StopIteration:
    pass # How  to  iterate  list_iterator  with   _next_  method
print('Iterate   thru  list_iterator  with   for    loop')
r3=reversed(list)
for x in r3:
    print(x) # How  to  iterate  list_iterator  with  for  loop
r4=reversed(list)
print('Unpacks List_iterator : ' ,*r4)



# Find  outputs
a = 25
print(a)
#for x in a:
#	print(x) # error : int object is not iterable 
#print(iter(a)) # error : iter(non-seq)
#print(next(a)) # error



'''
Modify  following  program  such  that

1) Use  regular  function  instead  of  lambda  function

2) Use  for  loop  to  iterate  filter  instead  of  while  loop
'''
import  time
def f1(x):
     return x%2==0
list = [25,9,10,15,17,24,35,47,0,19,53,18,65,83]
f = filter( f1,list)
print(type(f))
print(f)
while   True:
	try:
		print(next(f))
		time.sleep(0.5)
	except  StopIteration:
		break
'''
o/p:
<class 'filter'>
type and address of f
10
24
0
18
'''


# Find  outputs 
import  time
list = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda x : True , list)
while  True:
	try:
		print(next(f))
		time.sleep(0.5)
	except:
		break
'''
o/p:
25
10.8
(3+4j)
Hyd
False
'''

#  Find  outputs 
import  time
list = [25,10.8,3 + 4j,'Hyd',True]
f = filter(lambda x : False , list)
while  True: # no output as condition is false for every iteration
	try:
		print(next(f))
		time.sleep(0.5)
	except:
		break 


# Find  outputs 
import  time
list = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda x : x , list)
while  True: # filter() removes False, 0, '', () values as they are false values
	try:
		print(next(f))
		time.sleep(1)
	except:
		break
'''
o/p:
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
list = [10,0,-25,(),(25,),'Hyd','',[],10.8,0.0 ,[10 , 20] , True , False]
f1 = filter(lambda  x : None  , list) # lambda always returns None for every element. No elements pass the filter.
print('Filter  f1')
disp(f1)
f2 = filter(None , list) # prints non empty elements
print('Filter  f2')
disp(f2)
'''
o/p:
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


# Find outputs  
import  time
list = ['Rama Rao','Sita','Rajesh','Kiran','Amar','Manohar','Vamsi']
f = filter(lambda  x  : len(x) >= 5  , list) # filter elements with length >=5
while   True:
	try:
		print(next(f))
		time.sleep(1)
	except:
		break
'''
o/p:
Rama Rao
Rajesh
Kiran
Manohar
Vamsi
'''


# Find  outputs 
import   time
list=[('A',10) , ('B',20) , ('C',15) , ('D',5) , ('E',18)]
f = filter(lambda x : x[1] >= 12,list)
while   True:
	try:
		print(next(f))
		time.sleep(1)
	except:
		break
'''
o/p:
('B', 20)
('C', 15)
('E', 18)
'''


#Find  outputs 
import time
list = [
	        {
                'Roll Num':10 ,
                'Stud Name':'Rama Rao' ,
                'Marks' : 75
              } ,
              {
                'Roll Num' :  20 ,
                'Stud Name' : 'Sita' ,
                'Marks' : 52
              } ,
             {
               'Roll Num'  : 15 ,
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
f = filter(lambda  x :  x['Marks'] >= 60 , list) # filters with marks >=60
while   True:
	try:
		print(next(f))
		time.sleep(1)
	except:
		break
'''
o/p:
{'Roll Num': 10, 'Stud Name': 'Rama Rao', 'Marks': 75}
{'Roll Num': 15, 'Stud Name': 'Kiran', 'Marks': 65}
{'Roll Num': 5, 'Stud Name': 'Rajesh', 'Marks': 82}
'''
	

# Find  outputs 
import  time
def  disp(f):
	while  True:
		try:
			print(next(f))
			time.sleep(1)
		except:
			break
list = [  { 'country' : 'India' , 'sale' : 150.5} ,
          { 'country' : 'china' , 'sale' : 200.2} ,
          { 'country' : 'USA' , 'sale' : 300.3} ,
          { 'country' : 'UK' , 'sale' : 210.4} ]
f1 = filter (lambda x : x['country'].startswith('U') , list)
print('Filter  f1')
disp(f1)
f2 = filter(lambda x : x['sale']  >= 200, list)
print('Filter  f2')
disp(f2)
'''
o/p:
Filter  f1
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}
Filter  f2
{'country': 'china', 'sale': 200.2}
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}
'''


#How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f1 = filter(lambda x : x % 2 == 0 , a)
print('Iterate  thru  filter  object  with   next   function')
try:
	while True:
		print(next(f1)) 
		time.sleep(0.5)
except StopIteration:
	pass # How  to iterate  thru  filter  object  with  next()  function
print('Iterate  thru  filter  object  with   for  loop')
f2 = filter(lambda x : x % 2 == 0 , a)
for x in f2:
	print(x)
	time.sleep(0.5) # How  to iterate  thru  filter  object  with  for  loop
f3 = filter(lambda x : x % 2 == 0 , a)
print('Unpack  filter  object :  ' , *f3)
print('filter  object  converted  to   list  :  ',list(filter(lambda x : x % 2 == 0 , a)))


#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator
a=range(1,21)
f=filter(lambda x:x%2!=0 ,a)
while  True:
	try:
		print(next(f))
		time.sleep(0.5)
	except  StopIteration:
		break


'''
Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
Input  is  string  and  output  is  set
'''
a=input('enter a string : ').upper()
f=filter(lambda x:x in 'AEIOU' ,a)
b=[]
for x in f:
	if x not in b:
		b.append(x)
		time.sleep(0.5)
print(set(b))
'''
o/p:
enter a string : python
{'O'}
'''


# Nested  filter  i.e.  filter  on  filter
import   time
list =  [ (10 , 'Rama' , 10000.0) ,
            (20, 'Sita' , 7000.0) ,
            (15 , 'Rajesh' , 15000.0) ,
            (5 , 'Amar' ,  12000.0) ,
            (18 , 'Ramesh' , 8000.0) ]
f = filter(lambda  x :  x[1].startswith('R'), filter(lambda x :  x[2] >= 10000 , list))
while   True:
	try:
		print(next(f))
		time.sleep(1)
	except:
		break
'''
o/p:
(10, 'Rama', 10000.0)
(15, 'Rajesh', 15000.0)
'''