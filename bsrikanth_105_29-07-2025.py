Leap year check:
------------------

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")

Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers:
-------------------------------------

a=int(input())
b=int(input())
c=int(input())
max_=a
min_=a
if b>max_:
    max_=b
if c>max_:
    max_=c
if b<min_:
    min_=b
if c<min_:
    min_=c
mid=(a+b+c)-(max_+min_)
print(max_,min_,mid)

------------------------------------
# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')			#Bye
	case  3:
		print('Three')
print('Bye')
--------------------------------------
# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:
		print('None of   the  above')	#Error
	case  2:
		print('Two')
print('Bye')
---------------------------------------
# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:				#Hello 
						 End
		print('Hello')
	case  _:
		print('Bye')
print('End')
------------------------------------------
#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')			#Hyd Bye
	case  1:
		print('Cyb')
print('Bye')
# Find  outputs  (Home  work)
-----------------------------------
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book')			#Book
						#Bye
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')
---------------------------------------------
 '''
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  --->   x-axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->y-axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> y- axis
8) What  is  the  output  when  input  is  ()  ?  --->  not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> not a point
10) What  is  the  output  when  input  is  (25,) ?  ---> not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  ---> not a point
'''
tpl = eval(input('Enter  any  point  in  the  form  of  (x , y) :  '))
match  tpl:
	case  (0 , 0):
		print('Origin')
	case   (0 , y):
		print('y - axis')
	case   (x , 0):
		print('x - axis')
	case   (x , y):
		print('Quadrant')
	case  _:
		print('Not  a  point')



----------------------------------

#  Find  outputs 
while  True:
	print('Hello')
print('Bye')

O/P:
Hello
Hello
Hello
Hello.
.
.
.
.
.
Hello
Bye

-------------------------------------


#  Find  outputs
while  False:     
	print('Hello')
print('Bye')


O/P:
Bye

----------------------------------
# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()
How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()
How  to  print  each  element  of   range(5)  with  for  loop


SYNTAX:

a = [10 , 20 , 15 , 18]
for i in a:
    print(i) 

	O/P:
	10
	20
	15
	18
	

b = 'Hyd'
for i in b:
    print(i)


	O/P:
	H
	y
	d

for i in range(5):
    print(i)


	O/P:
	0
	1
	2
	3
	4
	

---------------------------



# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)                                 

	O/P:
	10
	30
	50


print()


for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
print()

O/P:
20
40
60


for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
print()

O/P:

10:20
30:40
50:60


for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)

	
O/P:

10:20
30:40
50:60
-----------------------------------------------


# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') #10...20
	                            30...40
								50...60
for  x ,  y  in   a:
	print(x , y)                #Error

for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')     #Error


-------------------------------------------------


# Identify  error  (Home  work)
for  x  in   123:
        print(x)


0/P:
 123 is not iterable due to undefined
----------------------------------------
# Find  outputs  (Home  work)
for  x   in   ():
        print(x)      # empty
for  x   in  []:
        print(x)      #empty
for  x   in   {}:
        print(x)       #empty
for  x   in   set():
        print(x)      #empty
for  x   in   '':
        print(x)       #empty
for  x  in  range(10 , 10):
	print(x)            #empty
for  x  in   range():
	print(x)           # Error due to no arguement there in range
for  x  in   (25):
	print(x)          #not iterable Error


---------------------------------------




#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j) 
	print('Hello')        
print('Bye')               

0/P:

1 1
1 2
1 3
1 4
Hello
2 1 
2 2
2 3
2 4
Hello
3 1 
3 2 
3 3
3 4
Hello
Bye
----------------------------------------



# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')

for i in range(len(a)):
	print(i)


How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')

 
for i in range(len(a)):
	print(a[i])


How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)


for i in a:
	print(i)

---------------------------------------

#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')


for i in range(reversed(len(a))):
	print(a[i])


How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
  

  for i in reversed(a):
	print(i)

-------------------------------------


'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  ---> [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []

for i in range(min(len(a), len(b))):
    c.append(a[i] + b[i])

print('3rd list:', c)


How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)


i = 0
for x in a:
    if i < len(b):
        c.append(x + b[i])
        i += 1
    else:
        break

print('3rd list:', c)


How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)



#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']

How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop


print('Indexed for loop')
for i in range(2, 5):
    print(a[i])




How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice

print('For-each loop')
i = 0
for x in a:
    if 2 <= i <= 4:
        print(x)
    i += 1

-------------------------------------------



#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)           #a :  [11, 21, 15, 18]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)        #b : [10, 20, 15, 18]

