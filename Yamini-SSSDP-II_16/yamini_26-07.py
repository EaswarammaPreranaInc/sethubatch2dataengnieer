x = 25 # assigning 25 to object x
y = F'{x}' # converting x to a formatted string int using fstring
print(y) #printing y i.e '25'
print(type(y)) # printing the type of y, which is a string
x = 10.8 # assigning 10.8 to object x
y = F'{x}' # converting x to a formatted string float using fstring
print(y) # printing y i.e '10.8'
print(type(y)) # printing the type of y, which is a string
x = [10,20,30,40] # assigning a list to object x
y = F'{x}' # converting x to a formatted string list using fstring
print(y) # printing y i.e '[10, 20, 30, 40]'
print(type(y)) # printing the type of y, which is a string



a ,  b , c = 25 , 10.8 , 'Hyd' # assigning values to a, b, c multiple assignment
print(F'{a}  \t   {b}   \t  {c}') #` printing values of a, b, c with tab space`
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') # printing values of a, b, c with objects with tab space
print(F'{a=}  \t   {b=}   \t  {c=}') # printing values of a, b, c with objects with tab space  using f-string
print(F'{a:}  \t   {b:}   \t  {c:}') # just prints the values without labels
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') #prints the whole string as we did not use f-string
print(F'a  =  a  \t  b  =  b  \t  c  =  c') # prints the whole string as we did not use {}
print(F'{x =}  \t   {y =} \t {z=}') # error because objects x, y, z are not defined



x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}') #  {{x}}  with 2 braces becaues total 4//2=2 and even braces so jst onbject name is printed
print(F'{{{{{x}}}}}') # {{25}} with 2 braces because total 5//2=2 and odd braces so value is printed
print(F'{{{{{{x}}}}}}') # {{{x}}} with 3 braces because total 6//2=3 and even braces so just object name is printed
print(F'{{{{{{{x}}}}}}}')   # {{{25}}} with 3 braces because total 7//2=3 and odd braces so value is printed
print(F'{{{{{{{{x}}}}}}}}') # {{{{x}}}} with 4 braces because total 8//2=4 and even braces so just object name is printed



prgm-1

import math
x=int(input('Enter 1st integer number: '))
y=int(input('Enter 2nd integer number: '))
print(x,' + ',y ,' = ',(x+y))
print(x,' - ',y, ' = ',(x-y))
print(x,' * ',y, ' = ',(x*y))
print(x,' / ',y, ' = ',(x/y))
print(x,'% ',y, ' = ',(x%y))
print('max(',x,',',y,') = ',max(x,y))
print('min(',x,',',y,') = ',min(x,y))
print(x,'^',y,' = ',(x**y))
print('sqrt(',x,') = ',math.sqrt(x))
print('gcd(',x,',',y,') = ',math.gcd(x,y))
print('fact(',x,') = ',math.factorial(x))


prgm-2

x=eval(input('Enter 1st input: '))
y=eval(input('Enter 2nd input: '))
print('Before swap: x =', x, ', y =', y)
x,y=y,x
print('After swap: x =', x, ', y =', y) 


prgm-3

x=eval(input('Enter 1st input: '))
y=eval(input('Enter 2nd input: '))
z=eval(input('Enter 3rd input: '))
result=x if x>y else y if y>z else z
print(result)

prgm-4

x=eval(input('Enter 1st input: '))
y=eval(input('Enter 2nd input: '))
result= '<' if (x<y) else '>' if (x>y) else '='
print(result)

prgm-5

x=eval(input('Enter any number: '))
result= '-1' if (x<0) else '1' if (x>0) else '0'
print(result)

prgm-6

x=eval(input('Enter any number: '))
result= 'Even number' if (x%2==0) else 'Odd number'
print(result)

prgm-7
length=eval(input('enter length of rectangle: '))
breadth=eval(input('enter breadth of rectangle: '))
area=length*breadth
perimeter=2*(length+breadth)
print("Area of rectangle is", area)
print("Perimeter of rectangle is", perimeter)

prgm-8

import math
radius=eval(input('enter radius of sphere: '))
volume=4/3*math.pi*radius**3
print('volume of sphere is:', volume)

prgm-9

principle=int(input("Enter the principal amount: "))
rate=int(input("Enter the rate: "))
time=int(input("Enter the time: "))
simple_interest = (principle * rate * time) / 100
compound_interest = principle * ((1 + rate / 100) ** time - 1)
print("Simple Interest:", simple_interest)
print("Compound Interest:", compound_interest)

prgm-10

x=eval(input("Enter 1st value: " ))
y=eval(input("Enter 2nd value: " ))
print("Before swapping: x =", x, ", y =", y)
temp=x
x=y
y=temp
print("After swapping: x =", x, ", y =", y)

prgm-11

x=eval(input("Enter 1st value: " ))
y=eval(input("Enter 2nd value: " ))
print("Before swapping: x =", x, ", y =", y)
x=x+y
y=x-y
x=x-y
print("After swapping: x =", x, ", y =", y)

prgm-12

x=eval(input("Enter 1st value: " ))
y=eval(input("Enter 2nd value: " ))
print("Before swapping: x =", x, ", y =", y)
x=x*y
y=x/y
x=x/y
print("After swapping: x =", x, ", y =", y)
