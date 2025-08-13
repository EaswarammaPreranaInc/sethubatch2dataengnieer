x = 25
y = F'{x}'
print(y)          # 25
print(type(y))    # <class 'str'>
x = 10.8
y = F'{x}'
print(y)          # 10.8
print(type(y))    # <class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y)          # [10, 20, 30, 40]
print(type(y))    # <class 'str'>

a, b, c = 25, 10.8, 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')        # 25    	10.8   	Hyd     # → Normal f-string: prints values of a, b, c with tab spaces
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')  # a = 25   b  =  10.8   c  =  Hyd  # → Labels written manually, 
print(F'{a=}  \t   {b=}   \t  {c=}')   # a=25   b=10.8   c='Hyd'  # → f-string debug syntax (`{var=}`) shows both variable name and value   # → Strings get quotes automatically
print(F'{a:}  \t   {b:}   \t  {c:}')  # 25   10.8   Hyd   # → `:{}` is formatting style (used for width, alignment etc.) — here, default used
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')   # a  =  {a}   b  =  {b}   c  =   {c}   # → No `f` prefix → just prints as-is
print(F'a  =  a  \t  b  =  b  \t  c  =  c')  # a  =  a   b  =  b   c  =  c
print(F'{x =}  \t   {y =}   \t  {z =}')   # Error: name 'x', 'y', 'z' is not defined   

x = 25
print(F'{x}')            	              # 25
print(F'{{x}}')              	              # {x}
print(F'{{{x}}}')                          # {25}
print(F'{{{{x}}}}')                      # {{x}}
print(F'{{{{{x}}}}}')                  # {{25}}
print(F'{{{{{{x}}}}}}')              # {{{x}}}
print(F'{{{{{{{x}}}}}}}')          # {{{25}}}
print(F'{{{{{{{{x}}}}}}}}')      # {{{{x}}}}


#Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
try:
    a = int(input('Enter the first input : ')) #10
    b = int(input('Enter the second input : ')) #7
print(f'{a}+{b} = {a+b}') #10+7=17
print(f'{a}-{b} = {a-b}') #3
print(f'{a}*{b} = {a*b}') #70  
print(f'{a}/{b} = {a/b:.2f}') #1.43
print(f'{a}%{b} = {a%b}') #3
print(f'max({a},{b})={a if a>b else b}') #10
import math
print(f'sqrt({a})={math.sqrt(a):.2f}') #3.16
print(f'{a}^{b}={math.pow(a,b)}') #10000000.0
print(f'gcd({a},{b}) = {(math.gcd(a,b))}') #1
print(f'fact{a}={(math.factorial(a))}') #3628800
except ValueError:
    print('Invalid input! Input should be of type int')

#Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object
try:
    a = eval(input('Enter the first input : ')) #25
    b = eval(input('Enter the second input : ')) #’Hyd’
    a,b = b,a
    print(a,b,sep='\n') #Hyd
                                  #25
except NameError:
    print('string must be in quotes')
except SyntaxError:
    print(‘syntax must be correct')

# Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function
try:
    a = eval(input('Enter the first input : ')) # 10   
    b = eval(input('Enter the second input : ')) #20
    c = eval(input('Enter the third input : ')) #15
    print(a if a>b else b if b>c else c) #20
except NameError:
    print('strings must be in quotes')
except TypeError:
    print('Complex numbers  are not allowed as input')
except SyntaxError: 
      print("invalid syntax – don't use commas or operators. Enter only number or sequence.")

# Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,'<'  if  1st  input  <  2nd  input  and  '='  if  inputs  are  same
try:
    a = eval(input('Enter the first input : ')) #35
    b = eval(input('Enter the second input : ')) #45
    if(a>b):
     print('a>b')
    elif(a==b):
     print('a=b')
    else:
     print('a<b') #(a<b)
except NameError:
    print('values must be of type int or float')
except TypeError:
     print('complex values are invalid')
except SyntaxError: 
      print("invalid syntax – don't use commas or operators. Enter only one number.")

# Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0
try:
    a = eval(input('Enter the first input : ')) #0.0000001
    if(a>0):
     print('1') # 1
    elif(a==0):
     print('0')
    else:
     print('-1')
except NameError:
    print('values must be of type int or float')
except TypeError:
     print('complex values, sequences are n’ot allowed')
except SyntaxError: 
      print("invalid syntax – don't use commas or operators. Enter only one number.")

# Write  a  program  to  test  input  is  even  number  or  odd  number
try:
    a = eval(input('Enter the first input : ')) #28
    if a%2 == 0:
      print('a is divisible by 2')  # a is divisible by 2
    else:
      print('a is not divisible by 2')
except NameError:
    print('invalid input - strings are not allowed')
except TypeError:
    print('invalid input - Complex numbers, sequence are not allowed as input')
except SyntaxError: 
      print("invalid syntax – don't use commas or operators. Enter only one number.")



# Write  a  program  to  determine  area  and  perimeter  of  rectangle
try:
    a = eval(input('Enter the Length : ')) # 15
    b = eval(input('Enter the breadth : ')) # 10
    perimeter = 2*(a+b)
    area = a*b
    print('perimeter =',perimeter) # perimeter = 50
    print('area =',area) #area = 150
except NameError:
    print('invalid input - strings are not allowed')
except TypeError:
    print('invalid input - Sequences are not allowed as input')
except SyntaxError: 
      print("invalid syntax – don't use commas or operators. Enter only one number.")

# Write  a  program  to  determine  volume  of  a  sphere
import math
try:
    a = eval(input('Enter the Radius : ')) #13
    volume = 4/3*math.pi*a**3
    print(f"volume = {volume:.2f}") # 9202.77
except NameError:
     print('invalid input - strings are not allowed')
except TypeError:
     print('invalid input - sequences are not allowed as input')
except SyntaxError: 
      print("invalid syntax – don't use commas or operators. Enter only one number.")

# Write  a  program  to  determine  simple  interest  and  compound  interest
try:
    P = eval(input('Enter the Principle : ')) #1000
    R = eval(input('Enter the Rate of Interest : ')) #9
    T = eval(input('Enter the Time : ')) #2
    SI = (P*T*R)/100
    CI = P* (1  +  R  /  100)** T-P
    print(f'Simple Interest = {SI:.2f}') # 180.00
    print(f'Compound Interest = {CI:.2f}' ) # 188.10
except NameError:
     print('invalid input - strings are not allowed')
except TypeError:
     print('invalid input - sequences are not allowed as input')
except SyntaxError: 
      print("invalid syntax – don't use commas or operators. Enter only one number.")

#Write  a  program  to  swap  values  of  two  objects  with  using  3rd  object
try:
    x = eval(input('Enter the first value : ')) #10
    y = eval(input('Enter the second value : '))#25 
    z = x
    x = y
    y = z
    print(x,y,sep = "\n") #25	/n	10
except NameError:
     print('invalid input - strings must be in quotes')
except SyntaxError: 
      print("invalid syntax – don't use commas or operators. Enter only one number.")

#Write  a  program  to  swap  values  of  two  objects without using  3rd   object using One  addition  and  two  subtractions
try:
    x = eval(input('Enter the first value : ')) #25
    y = eval(input('Enter the second value : '))#10 
    x = x+y
    y = x-y
    x = x-y
    print(x,y,sep = "\n") #10	\n	25
except NameError:
     print('invalid input - strings must be in quotes')
except TypeError:
    print('invalid input - sequences are not allowed as input')
except SyntaxError: 
      print("invalid syntax – don't use commas or operators. Enter only one number.")

# Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object using One  multiplication  and  two  divisions
try:
    x = eval(input('Enter the first value : ')) # -200
    y = eval(input('Enter the second value : ')) #100
    x = x*y
    y = x//y
    x = x//y
    print(x,y,sep = "\n")#100 \n -200
except NameError:
      print('invalid input - str are not allowed')
except TypeError:
    print('invalid input - sequences are not allowed as input')
except SyntaxError: 
      print("invalid syntax – don't use commas or operators. Enter only one number.")
