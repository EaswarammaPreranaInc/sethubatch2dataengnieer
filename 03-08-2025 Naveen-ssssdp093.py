#Determine area and circumference of circle

import math
try:
    r=float(input('Enter radius of circle: '))
    area=math.pi*r**2
    cir=2*math*pi*r
    print(F'Area : {area:.2f}')
    print(F'Circumference:{cir:.2f}')
except:
    print('Input should be float(or)integer')




#Add,subtract,multiply and divide two complex numbers
try:
    a=complex(input('Enter first complex number:'))
    b=complex(input('Enter second complex number:'))
    print('Sum:',a+b)
    print('Difference : ',a-b)
    print('Product:',a*b)
    print('Division:',a/b)
except:
    print('Input should be a complex number')




#Determine sum,difference,product,quotient,largest and smallest of two numbers Also find reminder,sqrt of first input,power,gcd and factorial of first input
import math
try:
       a=int(input("enter 1st integer number:"))
       b=int(input("enter 2nd integer number:"))
       print(f'{a}+{b}={a+b}')
       print(f'{a}-{b}={a-b}')
       print(f'{a}*{b}={a*b}')
       print(f'{a}/{b}={a/b}')
       print(f'{a}%{b}={a%b}')
       print(f'max({a},{b})={max(a,b)}')
       print(f'min({a},{b})={min(a,b)}')
       print(f'sqrt({a})={math.sqrt(a):.2f}')
       print(f'{a}^{b}={pow(a,b):.2f}')
       print(f'gcd({a},{b})={math.gcd(a,b)}')
       print(f'fact({a})={math.factorial(a)}')
except:
       print('Input should be an integer number')

       

#swap values of any two objects in a single statement without using third object
x=input("enter 1st input: ")
y=input("enter 2nd input: ")
print(f"befor swapping : x='{x}' \t'{y}'")
x,y=y,x
print(f"after swapping : x='{x}' \t'y={y}'")



#ternary operator
#determine largest inputs without using max() function
try:
    x=eval(input('Enter 1st input:'))
    y=eval(input('Enter 2nd input:'))
    max=x if x>y else y
    print('Largest input :',max)
except NameError:
    print('Input string should be in quotes')
except TypeError:
    print('Input can not be complex number')



#Determine largest of three inputs without using max() function
#nested ternary
try:
    a=eval(input('Enter 1st input:'))
    b=eval(input('Enter 2nd input:'))
    c=eval(input('Enter 3rd input:'))
    max=a if a>b and a>c else b if b>c else c
    print('Largest input:',max)
except NameError:
    print('Input string should be in quotes')
except TypeError:
    print('Input can not be complex number')



#assignment
try:
    a=eval(input('Enter 1st input:'))
    b=eval(input('Enter 2nd input:'))
    c='>' if a>b else '<' if a<b else '='
    print('Result:',c)
except NameError:
    print('Input string should be in quotes')
except TypeError:
    print('Input can not be complex number')




#assignment2
try:
    x=float(input('Enter any number:'))
    y=1 if x>0 else -1 if x<0 else 0
    print('Result:',y)
except:
    print('Input should be integer or float')




#test input is even number or odd number
try:
    x=int(input('Enter any +ve integer'))
    y='Even number' if x%2==0 else 'Odd number'
    print(y)
except:
    print('Input should be interger')




#getpass()
import getpass
usr=input('User name:')
pwd=getpass.getpass('Password:')
print('Logging in ...')
print('User name :',usr)
print('Password:',pwd)



#getsize0f()
import sys
print(sys.getsizeof(10000000))              # size of int object in terms of bytes
print(sys.getsizeof(10.8))                  # size of float object
print(sys.getsizeof(3+4j))                  # size of complex object
print(sys.getsizeof('Rama Rao'))            # size of str object
print(sys.getsizeof(True))                  # size of bool object
print(sys.getsizeof(None))                  # size of nonetype object
print(sys.getsizeof([10,20,15,18]))         # size of list 
#print(getsizeof())                         # error no getsize() function in current module




#print month calender
import calendar
try:
    month=int(input('Enter month(1-12):'))
    year=int(input('Enter year:'))
    print(calendar.month(year,month))
except:
    print('Input month number should be between 1 and 12')



#print year calendar
import calendar
year=int(input('Enter year:'))
print(calendar.calendar(year))



#determine area and perimeter of rectangle
try:
    l=float(input('Enter length of rectangle:'))
    b=float(input('Enter breadth of rectangle:'))
    area=l*b
    peri=2*(l+b)
    print(F'Area:{area:.2f}')
    print(F'Perimeter:{peri:.2f}')
except:
    print('Input should be float or integer')




#volume of a sphere
import math
try:
    r=float(input('Enter radius:'))
    v=4/3*math.pi*r**3
    print(F'Volume:{v:.2f}')
except:
    print('Input should be float or integer')



#simple interest and compound interest
try:
    p=float(input('Enter principle:'))
    t=float(input('Enter time:'))
    r=float(input('Enter rate of intrest:'))
    si=p*t*r/100
    ci=p*(1+r/100)**t-p
    print(F'Simple interest:{si:.2f}')
    print(F'Compund interest:{ci:.2f}')
except:
    print('Input should be float or integer')



#swap assignment1
try:
    x=input('Enter 1st input:')
    y=input('Enter 2nd input:')
    print(F'Before swap:{x=}\t{y=}')
    temp=x
    x=y
    y=temp
    print(F'After swap:{x=}\t{y=}')
except:
    print('Input string should be in quotes')



#swap assignment2
try:
    x=float(input('Enter 1st input:'))
    y=float(input('Enter 2nd input:'))
    print(F'Before swap:{x=}\t{y=}')
    x=x+y
    y=x-y
    x=x-y
    print(F'After swap:{x=}\t{y=}')
except:
    print('Input string should be float or integer')



#swap assignment3
try:
    x=float(input('Enter 1st input:'))
    y=float(input('Enter 2nd input:'))
    print(F'Before swap:{x=}\t{y=}')
    x=x*y
    y=x/y
    x=x/y
    print(F'After swap:{x=}\t{y=}')
except:
    print('Input should be float or integer')
