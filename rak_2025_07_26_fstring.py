# F   string  demo  program
x = 25
print(F'{x}')       #Converts  object  'x'  to  string  i.e.  '25'
print(F'x')         #x  itself  :   Braces  are  missing  for  object  'x'
print('{x}')        #{x}
print('x')          #x
print(x)            #25
print(F'x = {x}')   #x = 25
print(F'{x =  }')   #x = 25
print(F'x =')       #x =
print(F'x : {x}')   #x : 25
print(F'{x:}')      #25  and  ignores  :


#  Find  outputs  (Home  work)
x = 25
y = F'{x}'         # Converts  int  object 'x' to  string '25'
print(y)           #    25
print(type(y))     # <class 'str'>
x = 10.8
y = F'{x}'         # Converts  float  object 'x' to string '10.8'
print(y)           #  10.8
print(type(y))     # <class 'str'>
x = [10,20,30,40]
y = F'{x}'         #  Converts   list  to string   list  '[10,20,30,40]'
print(y)           #  [10,20,30,40]
print(type(y))     # <class 'str'>


#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')                  #25 <tab> 10.8 <tab> Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')    #a = 25 <tab> b = 10.8 <tab> c = Hyd
print(F'{a=}  \t   {b=}   \t  {c=}')               #a = 25 <tab> b = 10.8 <tab> c = Hyd
print(F'{a:}  \t   {b:}   \t  {c:}')               #25 <tab> 10.8 <tab> Hyd  (Ignores  colons)
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')  #a  =  {a}   <tab>  b  =  {b}   <tab> c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')        #a =  a  <tab>  b = b  <tab>  c = c
#print(F'{x =}  \t   {y =}   \t  {z =}')           #NameError :   No  objects  x , y  and  z  in  the  program


#  Find  outputs  (Home  work)
x = 25
print(F'{x}')                #25
print(F'{{x}}')              #{x} 
print(F'{{{x}}}')            #{25}
print(F'{{{{x}}}}')          #{{x}}
print(F'{{{{{x}}}}}')        #{{25}}
print(F'{{{{{{x}}}}}}')      #{{{x}}}
print(F'{{{{{{{x}}}}}}}')    #{{{25}}}
print(F'{{{{{{{{x}}}}}}}}')  #{{{{x}}}}

# In f-strings: {} inserts value, {{ and }} print literal braces
# f"{{{x}}}" → '{{' gives '{', {x} becomes 25, '}}' gives '}' → result: '{25}'
# f"{{{{x}}}}" → '{{' gives '{', 'x' stays as text, '}}' gives '}' → result: '{x}'



import math
try:
    a = int(input("Enter 1st integer number:"))
    b = int(input("Enter 2nd integer number:"))
    print(f'{a} + {b} = {a+b}')
    print(f'{a} - {b} = {a-b}')
    print(f'{a} * {b} = {a*b}')
    print(f'{a} / {b} = {a/b:.2f}')
    print(f'{a} % {b} = {a%b}')
    print(f'max({a}, {b}) = {max(a,b)}')
    print(f'min({a}, {b}) = {min(a,b)}')
    print(f'{a} ^ {b} = {pow(a,b):.2f}')
    print(f'sqrt({a}) = {math . sqrt(a)}')
    print(f'gcd({a}, {b}) = {math.gcd(a,b)}')
    print(f'fact({a}) = {math.factorial(a)}')
except ValueError:
    print("Please enter only integer type")
except OverflowError:
    print("The values of integer are too big to find power")
except:
    print('Please enter a valid input')



try:
    a = eval(input('Enter 1st input:'))
    b = eval(input('Enter 2nd input:'))
    print(f'Before swap : {a=} \t {b=}')
    a, b = b, a
    print(f'After swap : {a=} \t {b=}')
except NameError:
    print('Strings must be enclosed in quotes')
except:
    print('please enter a valid input')


try:
	a  = eval(input('Enter 1st input : '))
	b  = eval(input('Enter 2nd input : '))
	c =  eval(input('Enter 3rd input : '))
	max =  a  if  a >  b   and  a >  c  else   b   if  b >  c  else  c
	print('Largest  Input  : ' , max)
except  NameError:
	print('Input  string  should  be  in  quotes')
except  TypeError:
	print('Input  can  not  be  complex number')
except:
    print('Please try again with valid input')



try:
	a = eval(input('Enter 1st input : '))
	b = eval(input('Enter 2nd input : '))
	ans =  '>'   if  a  >  b  else  '<'  if  a <  b  else  '='
	print('Result :  ' , ans)
except  NameError:
	print('Input  string  should  be  in  quotes')
except  TypeError:
	print('Input  can  not  be  complex number')

    

try:
	x = float(input('Enter any number : '))
	ans =  1  if  x > 0  else   -1   if  x < 0  else   0
	print('Result : ' ,  ans)
except:
	print('Input  should   be  integer (or) float')
      

try:
	x =  int(input('Enter any +ve integer : '))
	ans = 'Even  number'   if  x % 2 == 0  else  'Odd  number'
	print(ans)
except:
	print('Input  should be integer')



try:
    length = float(input('Please enter length of the rectangle:'))
    breadth = float(input('Please enter breadth of rectangle:'))
    print(f'Area of rectangle: {length*breadth:.2f} \n Perimeter of rectangle: {2 * (length+breadth):.2f}')
except ValueError:
    print('Please enter a valid number')
except:
    print('Please enter valid input')


import  math
try:
	r = float(input('Enter  radius  :  '))
	v = 4 / 3 * math . pi * r ** 3
	print(F'Volume  :  {v:.2f}')
except ValueError:
	print('Input  should  be  float (or) integer')
	


try:
	p = float(input('Enter  principle  :  '))
	t = float(input('Enter  time  : '))
	r = float(input('Enter  rate  of  interest :  '))
	si = p * t * r / 100
	ci = p * (1  +  r  /  100) **  t  -  p
	print(F'Simple  Interest : {si:.2f}')
	print(F'Compound  Interest : {ci:.2f}')
except ValueError:
	print('Input  should  float (or) integer')
except:
    print('Please try agin with valid input')
	



try:
    a = eval(input('Enter 1st input: '))
    b = eval(input('Enter 2nd input: '))
    print(f'Before swap: {a=} \t {b=}')
    c = a
    a = b
    b = c
    print(f'After swap: {a=} \t {b=}')
except NameError:
    print('Strings must be enclosed in quotes')
except:
    print('Please try again with valid input')


try:
	x = float(input('Enter  1st  input  : '))
	y = float(input('Enter  2nd  input  : '))
	print(F'Before  swap :  {x=}  \t  {y=}')
	x = x + y
	y = x - y
	x = x - y
	print(F'After  swap :  {x=}  \t  {y=}')
except ValueError:
	print('Input  should  be  float (or) integer')
except:
	print('Please enter valid input')



try:
	x = float(input('Enter  1st  input  : '))
	y = float(input('Enter  2nd  input  : '))
	print(F'Before  swap :  {x=}  \t  {y=}')
	x = x * y
	y = x / y
	x = x / y
	print(F'After  swap :  {x=}  \t  {y=}')
except ValueError:
	print('Input  should  be  float (or) integer')
except:
      print('Please try again with valid input')


