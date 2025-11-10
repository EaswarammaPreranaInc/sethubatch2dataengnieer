# Program 1
# How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
for x in list:  # How  to  iterate  list  with  for  loop
    print(x)
    time.sleep(1)
#print(next(list))
list_itr1 = iter(list)
print(type(list_itr1))
print(list_itr1)
print('Iterate   thru  list_iterator  with  next()  function')
while True:  # How  to  iterate  list_iterator  with  next()  function
    try:
        print(next(list_itr1))
        time.sleep(1)
    except StopIteration:
        break
print('Iterate  thru  list_iterator  with   _next_()  method')
list_itr2=iter(list)
while True:   # How  to  iterate  list_iterator  with   _next_  method
    try:
        print(list_itr1.__next__())
        time.sleep(1)
    except StopIteration:
        break
list_itr3=iter(list)
print('Iterate   thru  list_iterator  with   for    loop')
for x in list_itr3:  # How  to  iterate  list_iterator  with  for  loop
    print(x)
    time.sleep(1)
list_itr4=iter(list)
print('Unpacks  List_iterator   :    ' , *list_itr4)

# Output :
Iterate  list  with  for  loop
10
20
15
18
<class 'list_iterator'>
<list_iterator object at 0x00000295E86F8BB0>
Iterate   thru  list_iterator  with  next()  function
10
20
15
18
Iterate  thru  list_iterator  with   _next_()  method
Iterate   thru  list_iterator  with   for    loop
10
20
15
18
Unpacks  List_iterator   :     10 20 15 18

# Program 2
# Find  outputs
a = 25
print(a) # 25
for  x   in   a: # Error due to Non-seqence cannot be iterated
	print(x)
print(iter(a)) # Error 
print(next(a))  # Error 

# Program 3
'''
Modify  following  program  such  that

1) Use  regular  function  instead  of  lambda  function

2) Use  for  loop  to  iterate  filter  instead  of  while  loop
'''
import  time
list = [25 , 9 , 10 , 15 ,  17 , 24 , 35 , 47 , 0 , 19 , 53 , 18 , 65 , 83]
def disp(x):
	return x%2==0
f = filter(disp  , list)
print(type(f))
print(f)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except  StopIteration:
		break

# Output :
<class 'filter'>
<filter object at 0x000001C0197F8700>
10
24
0
18

# Program 4
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

# Output :
25
10.8
(3+4j)
Hyd
False


# Program 5
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

# Output :
No results


# Program 6
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

# Output :
25
10.8
(3+4j)
Hyd

# Program 7
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

# Output :
Filter  f1
Filter  f2
10
-25
(25,)
Hyd
10.8
[10, 20]
True


# Program 8
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

# Output :
Rama Rao
Rajesh
Kiran
Manohar
Vamsi


# Program 9
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

# Output :
('B', 20)
('C', 15)
('E', 18)


# Program 10
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

# Output :
{'Roll Num': 10, 'Stud Name': 'Rama Rao', 'Marks': 75}
{'Roll Num': 15, 'Stud Name': 'Kiran', 'Marks': 65}
{'Roll Num': 5, 'Stud Name': 'Rajesh', 'Marks': 82}


# Program 11
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

# Output :
Filter  f1
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}
Filter  f2
{'country': 'china', 'sale': 200.2}
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}


# Program 12
# How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f1 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  thru  filter  object  with   next   function')
while True:  # How  to iterate  thru  filter  object  with  next()  function
  try:
    print(next(f1)
    time.sleep(1)
  except stopIteration:
          break
print('Iterate  thru  filter  object  with   for  loop')
f2 = filter(lambda  x  :  x  %  2  ==  0 , a)
for x in f2:  # How  to iterate  thru  filter  object  with  for  loop
    print(x)
    time.sleep(1)
f3 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Unpack  filter  object :  ' ,  *f3)
f4 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('filter  object  converted  to   list  :  ' , list(f4))

# Output :
Iterate  thru  filter  object  with   next   function
10
20
18
26
Iterate  thru  filter  object  with   for  loop
10
20
18
26
Unpack  filter  object :   10 20 18 26
filter  object  converted  to   list  :   [10, 20, 18, 26]



# Output :
Iterate  thru  filter  object  with   next   function
10
20
18
26
Iterate  thru  filter  object  with   for  loop
10
20
18
26
Unpack  filter  object :   10 20 18 26
filter  object  converted  to   list  :   [10, 20, 18, 26]


# Program 13  
#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator
import time 
y=int(input("Enter Odd Numbers from 1 to :"))
a=[x for x in range(1,y+1) ]
f1=filter(lambda x : x%2 !=0,a)
for x in f1:
    print(x)
    time.sleep(1)

# Output :
Enter Odd Numbers from 1 to :20
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


# Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
Input  is  string  and  output  is  set

# Program
import time 
a=input("Enter Mixed Case String :").upper()
def disp(y):
    for  x in y:
        if x in "AEIOU":
            return x
f1=filter(disp,a)
print(set(f1))

# Output :
Enter Mixed Case String :rama aro
Vowels in a String : {'O', 'A'}


# Program 15
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
# Output :
(10, 'Rama', 10000.0)
(15, 'Rajesh', 15000.0)
