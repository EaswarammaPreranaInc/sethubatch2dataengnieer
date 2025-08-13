x=25
y=F'{x}' 
print(y) # 25
print(type(y))  # <class 'str'>
x=10.8
y=F'{x}' # converts float object 10.8 to string object '10.8'
print(y) # 10.8
print(type(y)) # <class 'str'>
x=[10,20,30,40]
y=F'{x}' 
print(y) # [10,20,30,40]
print(type(y)) # <class 'str'>
print()
a,b,c=25,10.8,'Hyd'
print(F'{a} \t {b} \t {c}') # 25   10.8   Hyd
print(F'a={a} \t b={b} \t c={c}') # a=25   b=10.8   c=Hyd
print(F'{a=} \t {b=} \t {c=}') # a=25   b=10.8  c=Hyd
print(F'{a:} \t {b:} \t {c:}') # 25  10.8  Hyd 
print('a={a} \t b={b} \t c={c}') # a={a}  b={b}   c={c}
print(F'a=a \t b=b \t c=c') # a=a b=b c=c 
#print(F'{x=} \t {y=} \t {z=}')# x,y,z are not defined
print()
x = 25
print(F'{x}')  #  25 
print(F'{{x}}')   #  {x} 
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}')  #  {{x}}
print(F'{{{{{x}}}}}')  #  {{25}}
print(F'{{{{{{x}}}}}}')  #  {{{x}}}
print(F'{{{{{{{x}}}}}}}')  #  {{{25}}}
print(F'{{{{{{{{x}}}}}}}}')   #  {{{{x}}}}
print()
import math
x=eval(input('Enter 1st integer number: '))  # 10
y=eval(input('Enter 2nd integer number: '))   #  7
print(F'{x} + {y} =',x+y) # 17
print(F'{x} - {y} =',x-y) # 3
print(F'{x} * {y} =',x*y) # 70
print(F'{x} / {y} =',x/y) # 1.4285714285714286
print(F'{x} % {y} =',x%y) # 3
print(F'max({x},{y}) =',max(x,y)) # 10
print(F'min({x},{y}) =',min(x,y)) # 7 
print(F'{x} ^ {y} =',math.pow(x,y)) # 10000000.0
print(F'sqrt({x}) =',math.sqrt(x)) # 3.1622776601683795
print(F'gcd({x},{y}) =',math.gcd(x,y)) # 1
print(F'fact({x}) =',math.factorial(x)) # 3628800
print()
#program to swap values of any two objects in a single statement without using 3rd values
x=eval(input('Enter 1st input: ')) 
y=eval(input('Enter 2nd input: ')) 
print('Before swap: x =', x, 'y =',y)  
x,y=y,x # swaps the references of x and y
print('After swap: x =', x, 'y =',y)
print()
#program to determine largest of three inputs without using max() function
x=eval(input('Enter 1st input: '))
y=eval(input('Enter 2nd input: '))
z=eval(input('Enter 3rd input: '))
print('Largest input',x if x>y>z else y if x<y>z else z)
print()
#program to print '>' if 1st input > 2nd input, '<' if 1st input < 2nd input and '=' if both are same
x=eval(input('Enter 1st input: '))
y=eval(input('Enter 2nd input: '))
print('Result: ', '>' if x>y else '<' if x<y else '=')
print()
#program to print 1  if  input is +ve, -1 if input is -ve and 0 if input is 0
x=eval(input('Enter any input: '))
print('Result: ', 1 if x>0 else -1 if x<0 else 0)
print()
#program to test if input is even number or odd number
x=eval(input('Enter any +ve input: '))
print('Result: ' , 'even number' if x%2==0 else 'odd number')
print()
#program to determine area and perimeter of rectangle
import math
x=eval(input('Enter length of rectangle: '))
y=eval(input('Enter breadth of rectangle: '))
area=x*y
perimeter=2*(x+y)
print('Area of the rectangle: ',area)
print('Perimeter of the rectangle: ',perimeter)
print()
#program to determine volume of a sphere
import math
r=eval(input('Enter radius: ')) 
v=4/3*math.pi*(r**3)
print('Volume of sphere: ',v)
print()
# program to determine simple interest and compound interest
p=eval(input('Enter principal: '))
t=eval(input('Enter time in years: '))
r=eval(input('Enter rate of interest: '))
simple_int=(p*t*r)/100
compound_int=p*(1+r/100)**t-p
print('Simple interest : ',simple_int)
print('compound interest : ',compound_int)
print()
#program to swap values of two objects using 3rd object
x=eval(input('Enter 1st input: '))
y=eval(input('Enter 2nd input: '))
print('Before swap: x =', x, 'y =',y)
z=x+y
x=z-x
y=z-y
print('After swap: x =', x, 'y =',y)
print()
#program to swap values of two objects without using 3rd object
x=eval(input('Enter 1st input: '))
y=eval(input('Enter 2nd input: '))
print('Before swap: x =', x, 'y =',y)
x=x+y
y=x-y
x=x-y
print('After swap: x =', x, 'y =',y)
print()
#program to swap values of two objects without using 3rd object
x=eval(input('Enter 1st input: ')) 
y=eval(input('Enter 2nd input: ')) 
print('Before swap: x =', x, 'y =',y) 
x=x*y
y=x/y
x=x/y
print('After swap: x =', x, 'y =',y)