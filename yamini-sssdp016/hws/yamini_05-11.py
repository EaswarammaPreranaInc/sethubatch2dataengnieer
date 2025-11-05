# How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
for x in list:
    print(x)
#How  to  iterate  list  with  for  loop
#print(next(list))   # error as argument for next function should be iterator
list_itr1 = iter(list)  # converting list to list_iterator
print(type(list_itr1))  # class list_iterator
print(list_itr1)    # type and adress of the object
print('Iterate   thru  list_iterator  with  next()  function')
while True:
    try:
        print(next(list_itr1))
    except:
        break       #How  to  iterate  list_iterator  with  next()  function
print('Iterate  thru  list_iterator  with   _next_()  method')
list_itr2 = iter(list)    
print('Iterate   thru  list_iterator  with  next()  function')
while True:
    try:
        print(list_itr2.__next__())
    except:
        break   # How  to  iterate  list_iterator  with   _next_  method
print('Iterate   thru  list_iterator  with   for    loop')
#How  to  iterate  list_iterator  with  for  loop
list_itr3 = iter(list)  
for x in list_itr3:
    print(x)

print('Unpacks  List_iterator   :    ' ,  *iter(list))

# Find  outputs
a = 25
print(a)    # 25
for  x   in   a:
	print(x)    # error as non sequence cant be iterated 
print(iter(a))  # error as for iter func argument should be sequence
print(next(a))  # error as argument for next function should be iterator

'''
Modify  following  program  such  that

1) Use  regular  function  instead  of  lambda  function

2) Use  for  loop  to  iterate  filter  instead  of  while  loop
'''
import  time
def even(x):
    return x%2==0
list = [25 , 9 , 10 , 15 ,  17 , 24 , 35 , 47 , 0 , 19 , 53 , 18 , 65 , 83]
f = filter(even , list)
print(type(f))
print(f)
for i in f:
    print(i)


# Find  outputs (Home  work)
import  time
list = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda   x :   True ,   list)    # as for every element in the list the result is true every element is returned to next function
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

#  Find  outputs (Home  work)
import  time
list = [25 , 10.8 , 3 + 4j ,  'Hyd' , True]
f = filter(lambda  x  :  False ,  list) # as the result is false for every element all elements of list are filtered
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

# Find  outputs (Home  work)
import  time
list = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda   x   :   x   ,   list)   # 25 is non 0-true,10.8-true,false-false,3+4j-true,0-false,hyd-true(non empty),''-false,(25,)-true(non empty),()-false
while  True:
	try:
		print(next(f))  # 25,10.8,3+4j,hyd,(25,)
		time . sleep(1)
	except:
		break

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
f1 = filter(lambda  x : None  , list)   # 10-true,0-false,-25-true,()-false,(25,)-true,hyd-true,''-false,[]-false,10.8-true,0.0-false,[10,20]-true,true-true,false-false
print('Filter  f1')
disp(f1)   #as x points to none nothing is returned to next
f2 = filter(None  , list)       # error as argument 1 should be either lambda or regular function
print('Filter  f2')
disp(f2)

# Find outputs  (Home  work)
import  time
list = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , list)  # Rama Rao,Rajesh, Kiran, Manohar, Vamsi
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

# Find  outputs (Home  work)
import   time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda   x  :   x[1]  >=  12 , list) # returns tuple which has second element >12
while   True:
	try:
		print(next(f))  #'B' , 20) , ('C' , 15) ,  ('E' , 18)
		time . sleep(1)
	except:
		break

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
		''' {
                'Roll Num' :  10 ,
                'Stud Name' : 'Rama Rao' ,
                'Marks' : 75
              } ,{
               'Roll Num'  :  15 ,
               'Stud Name' : 'Kiran' ,
               'Marks' : 65
             }, 
             {
               'Roll Num' :  5 ,
               'Stud Name' : 'Rajesh' ,
               'Marks' : 82
             } '''
		time . sleep(1)
	except:
		break


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
disp(f1)    # { 'country' : 'USA' , 'sale' : 300.3} , { 'country' : 'UK' , 'sale' : 210.4}
f2 = filter(lambda  x  :  x['sale']  >=  200  , list)
print('Filter  f2')
disp(f2)    # { 'country' : 'china' , 'sale' : 200.2} , { 'country' : 'USA' , 'sale' : 300.3} , { 'country' : 'UK' , 'sale' : 210.4}

# How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f1 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  thru  filter  object  with   next   function')
while  True:
		try:
			print(next(f1))
			time . sleep(1)
		except:
			break
#  End  of  the  function   How  to iterate  thru  filter  object  with  next()  function
print('Iterate  thru  filter  object  with   for  loop')
f2 = filter(lambda  x  :  x  %  2  ==  0 , a)
for  i  in  f2:
		print(i)
		time . sleep(1)
#How  to iterate  thru  filter  object  with  for  loop
f3 = filter(lambda  x  :  x  %  2  ==  0 , a)

print('Unpack  filter  object :  ' ,  *f3)
f4 = filter(lambda  x  :  x  %  2  ==  0 , a)

print('filter  object  converted  to   list  :  ' ,  list(f4)) 

#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator

r=range(1,21)
f=filter(lambda x: x%2!=0,r)
for i in f:
    print(i)

'''
Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
Input  is  string  and  output  is  set
'''
def vowel(s):
    for i in s:
        if i in 'AEIOU':
            return True
s=input().upper()
f=filter(vowel,s)
print(set(f))

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
1st we will start with inner filter
filter(lambda  x :  x[2] >= 10000 , list)
tuples with 3rd element >=10000 are returned
(10 , 'Rama' , 10000.0) ,
(15 , 'Rajesh' , 15000.0) ,
(5 , 'Amar' ,  12000.0)
	
now outer filter
filter(lambda  x :  x[1] . startswith('R')  , filter
we have to check the lambda condition with the result of each inner tuple
if the 12nd element of tuple starts with r return true
(10 , 'Rama' , 10000.0) ,
(15 , 'Rajesh' , 15000.0)

so finally these 2 tuples are returned to next function
'''

