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
# producer stores 1 
# consumer retrives 1 
# Press  ctrl + break  or  Fn+B  to  stop
# (main thread is dead) 
# (assuming p was picked )
# producer stores 2
# consumer retrives 2
# (assuming c was picked by tS)
# consumer retrives 2
# producer stores 3 

# How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
# How  to  iterate  list  with  for  loop
for x in list:
	print(x)
print(next(list)) # error, arg should be iterator not iterable
list_itr1 = iter(list)
print(type(list_itr1))#list_iterator
print(list_itr1) #list_iterator address
print('Iterate   thru  list_iterator  with  next()  function')
#  How  to  iterate  list_iterator  with  next()  function
while True:
	try:
		print(next(list_itr1))
	except:
		break 
print('Iterate  thru  list_iterator  with   __next__()  method')
while True:
	try:
		print(list_itr1.__next__())
	except:
		break
# How  to  iterate  list_iterator  with   __next__  method

print('Iterate   thru  list_iterator  with   for    loop')
list_itr2 = iter(list)
for x in list_itr2:
	print(x)
list_itr3=iter(list)
# How  to  iterate  list_iterator  with  for  loop
print('Unpacks  List_iterator   :    ' ,  *list_itr3)

# Find  outputs
a = 25
print(a) #25
for  x   in   a: #error 
	print(x)
print(iter(a)) #error
print(next(a)) # error

'''
Modify  following  program  such  that

1) Use  regular  function  instead  of  lambda  function

2) Use  for  loop  to  iterate  filter  instead  of  while  loop
'''
def even(x):
	return x%2==0
import  time
list = [25 , 9 , 10 , 15 ,  17 , 24 , 35 , 47 , 0 , 19 , 53 , 18 , 65 , 83]
f = filter(even  , list)
print(type(f))
print(f)
for x in list:
	print(x)
	time.sleep(1)

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
# 25 , 10.8 , 3 + 4j , 'Hyd' , False

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
#no output empty results 

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
# 25 , 10.8 ,  3 + 4j , 'Hyd' ,(25,) 

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
f2 = filter(None  , list) # error 1st argument should be function
print('Filter  f2')
disp(f2)

#Filter f1 
# no output 
# filter f2
#no output 

# Find outputs  (Home  work)
import  time
list = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 
		'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , list)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
# 'Rama Rao' , 'Rajesh' , 'Kiran' ,  'Manohar' , 'Vamsi'

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
#A B C D E 

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
            #     {
            #     'Roll Num' :  10 ,
            #     'Stud Name' : 'Rama Rao' ,
            #     'Marks' : 75
            #   } 
            #  {
            #    'Roll Num'  :  15 ,
            #    'Stud Name' : 'Kiran' ,
            #    'Marks' : 65
            #  }
            #  {
            #    'Roll Num' :  5 ,
            #    'Stud Name' : 'Rajesh' ,
            #    'Marks' : 82
            #  }
			
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
# Filter f1 
#           { 'country' : 'USA' , 'sale' : 300.3} 
#           { 'country' : 'UK' , 'sale' : 210.4}
#Filter f2
        #   { 'country' : 'china' , 'sale' : 200.2} 
        #   { 'country' : 'USA' , 'sale' : 300.3} 
        #   { 'country' : 'UK' , 'sale' : 210.4} 

# How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f1 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  thru  filter  object  with   next   function')
# How  to iterate  thru  filter  object  with  next()  function
while True:
	try:
		print(next(f1))
	except:
		break
f2 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  thru  filter  object  with   for  loop')
# How  to iterate  thru  filter  object  with  for  loop
for x in f2:
	print(x)
f3= filter(lambda  x  :  x  %  2  ==  0 , a)
print('Unpack  filter  object :  ' ,  *f3)
f4 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('filter  object  converted  to   list  :  ' ,  list(f4))

#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator
l=[x for x in range(1,21)]
f=filter(lambda x:x%2 ==1,l)
for x in f:
	print(x)

# Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
# Input  is  string  and  output  is  set
str=input("Enter the string:")
f=filter(lambda x:x.upper() in ('A','E','I','O','U'),str)
res=set(list(f))
print(res)

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
            # (10 , 'Rama' , 10000.0) ,
            # (15 , 'Rajesh' , 15000.0) ,