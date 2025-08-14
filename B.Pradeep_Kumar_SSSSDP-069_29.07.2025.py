'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  single  if  with  3  conditions  and  else
'''

year = int(input(" Enter a year number: "))

if year%4==0 and (year%100 !=0):
    print(" Yes its leap year")
else:
    print("Not a leap year")


'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''

a = int(input(" Enter 1st number: "))
b = int(input(" Enter 2nd number: "))
c = int(input(" Enter 3rd number: "))

if a>b and a>c:
    print(f"{a} is largest")
else:
    if b>c:
        print(f"{b} largest")
    else:
        print(f"{c} is largest")


'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8


Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  1
Enter  celsius  temperature :  30
Fahrenheit  Equivalent  :  86.0

Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  2
Enter  fahrenheit  temperature : 100
celsius   equivalent :  37.78
'''
a = int(input(" Enter a number(1 or 2): "))
if a==1:
    b=float(input(" Enter the Celcius temparature:  "))
    c=1.8*b + 32
    print(f"Faranheit Equivalent :{c}")
else:
    d=float(input(" Enter the Fahrenheit temparature:  "))
    e=(d-32)/1.8
    print(f"Celcius Equivalent :{e}")


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

8) Hint:  Use  if  ..   elif
'''
x = int(input(" Enter x number: "))
y = int(input(" Enter y number: "))
if x>0 and y>0:
    print(f"({x},{y}) is lies in 1st Quadrant")
elif x<0 and y>0:
    print(f"({x},{y}) is lies in 2nd Quadrant")
elif x<0 and y<0:
    print(f"({x},{y}) is lies in 3rd Quadrant")
elif x>0 and y<0:
    print(f"({x},{y}) is lies in 4th Quadrant")
elif x==0 and y==0:
    print(f"({x},{y}) is lies in Origin")


'''
Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

a = 10
b = 20
c = 7
max =  20
min =  7
mid =  (10 + 20 + 7) - (20 + 7) = 10

1) What  is  the  initial  value  of  max  ?  --->  a

2) Whichever  input >  max,  assign  that  input  to  max

3) What  is  the  initial  value  of  min  ?  --->  'a'

4) Whichever  input  <  min,  assign  that  input  to  min

5) How  to  obtain  middle  number ?  ---> Eliminate  max  and  min  from  a , b , c

6) Hint : Do  not  use  else  in  the  program
'''

a = int(input(" Enter 1st number: "))
b = int(input(" Enter 2nd number: "))
c = int(input(" Enter 3rd number: "))
total=a+b+c
l=max(a,b,c)
s=min(a,b,c)
mid=total-(l+s)
print(f" max = {l}")
print(f" min = {s}")
print(f" mid = {mid}")


# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')  # Bye

# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:
		print('None of   the  above') # Error
	case  2:
		print('Two')
print('Bye') 


# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:
		print('Hello')  # Hello
	case  _:
		print('Bye')
print('End')  #  End

#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd') # Hyd
	case  1:
		print('Sec') # Error
	case  1:
		print('Cyb')  #  Error
print('Bye')

# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book')  #  Book
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')  #  Bye


'''
1) What  are  the  outputs  if  input  is  -6 ? --->Hyd Sec Cyb Bye

2) What  are  the  outputs  if  input  is  15  ?  ---> 
One
Two
Three
Bye

3) What  are  the  outputs  if  input  is  10.8  ?  --->
India
China
Usa
Bye


4) What  are  the  outputs  if  input  is  0  ?  --->
Hyd
Sec
Cyb
Bye


5) What  are  the  outputs  if  input  is  -10  ?  --->
One
Two
Three
Bye

6) What  are  the  outputs  if  input  is  7  ?  --->
Hyd
Sec
Cyb
Bye

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


Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
------------------------------------------------------------
First  100  units(0 - 99)					Rs. 3.00 / unit

Next  100  units(100 - 199)				Rs. 3.50 / unit

Next  200  units(200 - 399)		    	Rs. 4.00 / unit

Next  300  units(400 - 699)				Rs. 4.50 / unit

Above  700  units(>= 700)				Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + 500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else
'''
units = int(input('Enter  units :   '))  #  75
match  units // 100:
	case  0:
				cost = units * 3.00


units = int(input("Enter units: "))
cost = 0
remaining = units

match units // 100:
    case 0:  # 0 - 99
        cost = units * 3.00
    case 1:  # 100 - 199
        cost = 100 * 3.00 + (units - 100) * 3.50
    case 2 | 3:  # 200 - 399
        cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
    case 4 | 5 | 6:  # 400 - 699
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
    case _:  # 700 and above
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00

print(f"Total bill amount for {units} units is: Rs. {cost}")



# Find  outputs  (Home  work)
for  x   in   ():
        print(x)  #  Empty
for  x   in  []:
        print(x)#  Empty
for  x   in   {}:
        print(x)#  Empty
for  x   in   set():
        print(x)#  Empty
for  x   in   '':
        print(x)#  Empty
for  x  in  range(10 , 10):
	print(x) #  Empty
for  x  in   range():
	print(x)  #  Empty
for  x  in   (25):
	print(x) # Error

#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice

a = [25, 10.8, 'Hyd', True, 3 + 4j, None, 'Sec']
print('Indexed for loop')
for i in range(2, 5): 
    print(a[i])


#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)  #  a :  [11, 21, 16, 19]

b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)  #  b = [10 , 20 , 15 , 18]