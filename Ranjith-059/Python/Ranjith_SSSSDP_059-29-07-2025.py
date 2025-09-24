(29-07-2025)


'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  single  if  with  3  conditions  and  else
'''

a = int(input("Enter the Year: "))
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

Output
Enter the Year: 2024
Leap year
Enter the Year: 2025
Not a Leap year

'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
if (a > b and a > c) or (b > a and b > c):
    if a > b and a > c:
        print("Largest number =",a)
    if b > a and b > c:
        print("Largest Number = ",b)
else:
    print("Largest Number =",c)

#Output
Enter 1st number: 78
Enter 2nd number: 33
Enter 3rd number: 99
Largest Number = 99

'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''

a = int(input("Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius : "))
if a == 1:
    temp = float(input("Enter celsius temperature: "))
    f = 1.8 * temp + 32
    print("Fahrenheit  Equivalent:",f)
elif a == 2:
    temp = float(input("Enter  fahrenheit  temperature: "))
    c = (temp-32)/1.8
    print("celsius   equivalent: ",c)
else:
    print("Please enter a valid input")
    
#Output
'''
Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius : 1
Enter celsius temperature: 30
Fahrenheit  Equivalent: 86.0

Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius : 2
Enter  fahrenheit  temperature: 100
celsius   equivalent:  37.77777777777778
'''

'''
Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin

1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve

2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  --->  'x'  is  -ve  and  'y'  is  +ve

3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  ---> Both   are  -ve

4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  --->  'x'  is   +ve  and  'y'  is  -ve

5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0

6) What  are  the  values  of  x  and  y  on  y - axis ?  --->  'x'  is  0  and  'y'  is  non-zero

7) What  are  the  values  of  x  and  y  if  point  is  origin ?  --->  Both  are  zeroes

8) Hint:  Use  if  ..   elif
'''

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
if x > 0 and y > 0:
    print("1st quadrant")
elif x < 0 and y > 0:
    print("2nd Quadrant")
elif x < 0 and y < 0:
    print("3rd Quadrant")
elif x > 0 and y < 0:
    print("4th Quadrant")
elif x != 0 and y == 0:
    print("x - axis")
elif x == 0 and y != 0:
    print("y - axis")
else:
    print("Origin")

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
max = a if a > b and a > c else b  if b > a and b > c else c 
min = a if a < b and a < c else b  if b < a and b < c else c
print(f"Largest number = {max}")
print(f"Smallest number ={min}")
mid = (a+b+c) - (max+min)
print(f"Middle number ={mid}")

output
Enter 1st number: 23
Enter 2nd number: 99
Enter 3rd number: 34
Largest number = 99
Smallest number =23
Middle number =34

# Find  outputs  (Home  work)
m = 4 #Here reference m points to int-obj 4
match  m: #Here we are using the match to select something 
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')

#Output #Here the case 4 is not available so it directly prints bye
#Bye 

# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  :            #Here we should not use '' in the middle of the case statements it should be used end of all cases here it makes unreachable for remaining cases
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')

# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:
		print('Hello') #Already we have used match in the second case and it raises an error if we use '_' multiple times 
	case  _:
		print('Bye')
print('End')

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
print('Bye')

#outputs
Book
Bye

'''
1) What  are  the  outputs  if  input  is  -6 ? --->
2) What  are  the  outputs  if  input  is  15  ?  --->
3) What  are  the  outputs  if  input  is  10.8  ?  --->
4) What  are  the  outputs  if  input  is  0  ?  --->
5) What  are  the  outputs  if  input  is  -10  ?  --->
6) What  are  the  outputs  if  input  is  7  ?  --->
'''
x = eval(input('Enter any  number :  '))
match  x:
	case  7 |  -6  |  0:
		print('Hyd')
		print('Sec')
		print('Cyb')
	case  -10 | 15:
		print('One')
		print('Two')
		print('Three')
	case  _:
		print('India')
		print('China')
		print('Usa')
# End  of  match
print('Bye')

'''
#outputs
outputs  if  input  is  -6 = 
Hyd
Sec
Cyb
Bye

outputs  if  input  is  15
One
Two
Three
Bye

outputs  if  input  is  10.0
India
Chine
Usa
Bye

outputs  if  input  is  0
Hyd
Sec
Cyb
Bye

outputs  if  input  is  -10
One
Two
Three
Bye

outputs  if  input  is  7
Hyd
Sec
Cyb
Bye
'''
'''
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->   0 , 1 ,  1 , 2 ,  3 ,5 , 8


1) What  is  the  formula  for  10th  term ?  ---> 9th  term + 8th  term
    What  is  the  formula  for   3rd  term ?  ---> 	2nd  term + 1st  term
    What  is  the  formual  for  ith  term ?  --->  (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1  (No  formula)

3) Hint:  Use  while  loop
'''

n = int(input("Enter the value of x: "))
a = 0
b = 1

while a <= n:
    print(a)
    c = a + b
    a = b
    b = c
#outputs
Enter the maximum value: 10
0
1
1
2
3
5
8

#  Find  outputs
while  True:    #Here condition is always True so it goes to the infinite loop where it 'Hello' prints inifinte times
	print('Hello')
print('Bye')

#  Find  outputs
while  False:       #Here condition is False so it directly goes out of the loop and prints bye
	print('Hello')
print('Bye')

#Output
Bye

# Find  outputs  (Home  work)
#How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
#print()
#How  to  print  each  character  of   string  'Hyd'  with  for  loop
#print()
#How  to  print  each  element  of   range(5)  with  for  loop


l = [10, 20, 15, 18]
for i in l:
    print(i)
    
#Output
10
20
15
18

s = 'Hyd'
for i in s:
    print(i)
    
#Output
H
y
d

for i in range(5):
    print(i)
#Output
0
1
2
3
4

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)
print()
#outputs
10
30
50

for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
print()
#outputs
20
40
60

for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
print()
#outputs
(10, 20)
(30, 40)
(50, 60)

for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)
	
#outputs #Here it only returns keys
10
30
50
	
# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')

#outputs
10...20
30...40
50...60
	
for  x ,  y  in   a: #It gives us an error that we cannot unpack non-iterable objects
	print(x , y)
	
	
	
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}: # #It gives us an error that we cannot unpack non-iterable objects
	print(x , y , sep = '...')

# Identify  error  (Home  work)
for  x  in   123: #Here we cannot iterate thru int-object as it is a non-sequence
        print(x)

# Find  outputs  (Home  work)
for  x   in   ():
        print(x) #Returns nothing as it is an empty tuple
for  x   in  []:
        print(x) #Returns nothing as it is an empty list
for  x   in   {}:
        print(x) #Returns nothing as it is an empty dict
for  x   in   set():
        print(x) #Returns nothing as it is an empty set
for  x   in   '':
        print(x) ##Returns nothing as it is an empty string
for  x  in  range(10 , 10):
	print(x)     #Returns nothing as it start and end it at 10 so it also returns empty
for  x  in   range():
	print(x)    #Error because range object expects atleast one element range object cannot be empty
for  x  in   (25):
	print(x)        #Error as it is an int object which is non-sequence

#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')

#Output
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

# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
'''
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)

'''
for i in range(len(a)):
    print(i,a[i])
    
#Output
Indexed  based  for loop
0 25
1 10.8
2 Hyd
3 True

for item in enumerate(a):
    print(item[0], item[1]) 
    
#Output

0 25
1 10.8
2 Hyd
3 True

#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)

for i in range(len(a) - 1, -1, -1):
    print(i, a[i])


for item in reversed(a):
    print(item)


'''
#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
'''
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']

for i in range(2,5):
    print(a[i])
 
 
a = [25, 10.8, 'Hyd', True, 3 + 4j, None, 'Sec']

for i in range(len(a)):
    if i >= 2 and i <= 4:
        print(a[i])


#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)

#outputs
a : [11, 21, 16, 19]
#As we are using index to access the elements so it increment each iteration by 1


b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)

#outputs
b : [10, 20, 15, 18]
#Here we are using a temparory variable x which does not modify the list when changes are done to x so no changes