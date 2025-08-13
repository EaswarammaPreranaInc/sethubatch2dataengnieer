
num=int(input('Enter a year: '))
if (num%4==0 and num%100 !=0 or num%400==0):
    print(f'{num} is a leap year')
else:
    print(f'{num} not a leap year')

print()
a=int(input('Enter 1st number: '))
b=int(input('Enter 2nd number: '))
c=int(input('Enter 3rd number: '))
if(a>b and a>c):
    print('a is largest')
if(b>c and b>a):
        print('b is largest')    
else:
        print('c is largest')

print()
num=int(input('enter 1 to convert celsius to farenheit and 2 to convert farenheit to celsius '))
if (num==1):
    a=float(input('enter fahrenheit temperature :'))
    cel=(a-32)/1.8
    print('celsius equivalent :',cel)
elif(num==2):
    b=float(input('enter celsius temperature: '))
    fah=1.8*b+32
    print('fahrenheit eqivalent :',fah)
else:
    print('Invalidinput')

print()
num1=float(input('enter x-axis: '))
num2=float(input('Enter y-axis: '))
if (num1>0 and num2>0):
    print(F'({num1},{num2}) lies in 1st quadrant')
elif (num1<0 and num2>0):
    print(F'({num1},{num2}) lies in 2nd quadrant')
elif (num1<0 and num2<0):
    print(F'({num1},{num2}) lies in 3rd quadrant')
elif (num1>0 and num2<0):
    print(F'({num1},{num2}) lies in 4th quadrant')
else:
    print(F'({num1},{num2}) lies at origin')
    
print()

num1=float(input('enter 1st input: '))
num2=float(input('enter 2nd input: '))
num3=float(input('enter 3rd input: '))
max=num1
min=num2
if(num2>max):
    max=num2
if(num3>max):
    max=num3
if(num1<min):
    min=num1
if(num3<min):
    min=num3
print('largest number: ',max)
print('smallest number: ',min)
mid=(num1+num2+num3)-(max+min)
print('middle number ',mid)

print()
import math
a=float(input('enter 1st side of tri: '))
b=float(input('enter 2nd side of tri: '))
c=float(input('enter 3rd side of tri: '))
if((a+b)>c or(b+c)>a or (c+a)>b):
    if (a==b==c):
        print('area of qui triangle: ',math.sqrt(3)/4*a**2)
    if(((a==b) and b!=c) or (b==c and c!=a) or (c==a and a!=b)):
        print('perimeter of iso triangle: ',a+b+c)
    if((a!=b and b!=c and c!=a)):
        s=(a+b+c)/2
        print('area of scalene trinagle: ',math.sqrt(s*(s-a)(s-b)(s-c)))
        print('perimeter of scalene triangle: ',(a+b+c))
print()
import math
a=float(input('Enter the value of a: '))
b=float(input('Enter the value of b: '))
c=float(input('Enter the value of c: '))
disc=(b**2)-4*a*c
if(disc>0):
    print('Roots are Real and Distinct')
    print('Root1 :',(-b+math.sqrt(disc))/(2*a))
    print('Root1 :',(-b-math.sqrt(disc))/(2*a))
if(disc==0):
    print('Roots are Real and same')
    print('Root is :',-(b/(2*a)))
if(disc<0):
    print('Roots are complex')
    root1=-b/(2*a)
    root2=(math.sqrt(-disc/(2*a)))
    print(F'Root1 is : {root1}+{root2}j')
    print(F'Root1 is : {root1}-{root2}j')


print()
import math
num1=float(input('enter x-axis: '))
num2=float(input('Enter y-axis: '))
r=float(input('Enter radius :'))
dist=math.sqrt(num1*2+num2*2)
if(dist>r):
        print(F'({num1},{num2}) lie outside the circle)')
if(dist<r):
        print(F'({num1},{num2}) lie inside the circle)')
if(dist==r):
        print(F'({num1},{num2}) lie on the circle)')


# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')  #  Bye

# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	#case  _:
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')  #  Anonymous value should be written at end.

# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	#case  _:
		print('Hello')
	case  _:
		print('Bye')
print('End') # error 

#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')   #  Hyd <next line> Bye

# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book')
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye') #  Book <next line> Bye
print()
a = eval(input('Enter point  in  the  form  of  (x , y)'))
match  a:
	case  (0 , 0):
		print('Origin')
	case   (0 , y):
		print('y-axis')
	case   (x , 0):
		print('x-axis')
	case   (x , y):
		print('quadrant')
	case  _:
		print('Not point')
print()

units=int(input('Enter units : '))
match units//100:
    case 0:
        print('Bill amount: ',units*3.0)
    case 1:
        print('Bill amount: ',(100*3.0)+((units-100)*3.5))
    case 2|3:
        print('Bill amount: ',(100*3.0)+(100*3.5)+((units-200)*4.00))
    case 4|5|6:
        print('Bill amount: ',(100*3.0)+(100*3.5)+(200*4.00)+((units-400)*4.50))
    case _:
        print('Bill amount: ',(100*3.0)+(100*3.5)+(200*4.00)+(300*4.50)+((units-700)*5.00))

print()
x=int(input('Enter value of x: '))
a=0
b=1
print('Fibonacci series\n0\n1')
c=a+b
while (c<=x):
    print(c)
    a=b
    b=c
    c=a+b
print()
#  Find  outputs
while  True:
	print('Hello')
print('Bye')#prints hello indefinietly

#  Find  outputs
while  False:
	print('Hello')
print('Bye')#prints hello indefinietly

# Find  outputs  (Home  work)
#print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
l=[10,20,15,18]
for a in l:
    print(a)
#print  each  character  of   string  'Hyd'  with  for  loop
a='Hyd'
for b in a:
    print(b)
#print  each  element  of   range(5)  with  for  loop
x=range(5)
for i in x:
    print(x[i])

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)#10 <nextline> 30 <nextline> 50 <nextline> 
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)#10 <nextline> 30 <nextline> 50 <nextline>
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)#(10,20) <nextline> (30,40) <nextline> (50,60) <nextline>
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)#10<nextline> 30 <nextline> 50 <nextline>  

# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')  #10...20 \n 30...40 \n 50...60
for  x , y  in   a:
	#print(x , y) # error
#for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')  #error
	
# Identify  error  (Home  work)
for  x  in   123:
        print(x)  #int object is not iterable
        
# Find  outputs  (Home  work)
for  x   in   ():
       print(x)  #  no output
for  x   in  []:
        print(x)   #  no output
for  x   in   {}:
        print(x)   #   no output
for  x   in   set():
        print(x)   #  no output
for  x   in   '':
        print(x)   #  no output
for  x  in  range(10 , 10):
	print(x)   #  no output
for  x  in   range():
	print(x)  #  error
for  x  in   (25):
	print(x)   #   int obj is not iterable
    
#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j) 
	print('Hello')
print('Bye')
print()
# print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
# print  each  element  and  the  corresponding  index  with  index  based  for  loop
for i in range(len(a)):
    print(a[i])
print('For each loop')
# print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
i=0
for x in a:
    print(f'Index: {i}, Element: {x}')
    i += 1

# print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
# print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
for i in range(len(a)-1 , -1 , -1):
    print(a[i])
# print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)
for x in reversed(a):
    print(x)

#program to add two lists and store results in 3rd list
a = eval(input('Enter 1st list: '))
b = eval(input('Enter 2nd list: '))
c = []
n=min(len(a), len(b))
# add lists 'a' and 'b' and store results in list 'c' with indexed based for loop
for i in range(n):
    c.append(a[i] + b[i])
print('3rd list :', c)
# add lists 'a' and 'b' and store results in list 'c' with for each loop (Do not use 2nd variable)
c = []
i = 0
while i < n:
    c.append(a[i] + b[i])
    i += 1
print('3rd list :', c)

# print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
# print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
for i in range(2, 5):
    print(a[i])
# print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
i = 0
for x in a:
    if 2 <= i <= 4:
        print(x)
    i += 1

#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)  #  a : [11, 21, 16, 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)  #  b : [10, 20, 15, 18]            