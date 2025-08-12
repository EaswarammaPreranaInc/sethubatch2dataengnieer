#  Find  outputs  (Home  work)

x = 25
y = F'{x}'
print(y)       # 25
print(type(y)) # <class Str>
x = 10.8
y = F'{x}'
print(y)    # 10.8
print(type(y))  #<class str>
x = [10,20,30,40]
y = F'{x}'
print(y)  # [10,20,30,40]
print(type(y))  #<class str>

#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')    #25  10.8  Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')  # a=25  b=10.8  c=Hyd
print(F'{a=}  \t   {b=}   \t  {c=}')  # a=25 b=10.8 c=Hyd
print(F'{a:}  \t   {b:}   \t  {c:}')   # 25  10.8  Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') # a={a} b{b} c{c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')    # a=a b=b c=c
print(F'{x =}  \t   {y =}   \t  {z =}')    # error

#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}')  # {{x}}
print(F'{{{{{x}}}}}')  # {{25}}
print(F'{{{{{{x}}}}}}')  # {{{x}}}
print(F'{{{{{{{x}}}}}}}')  # {{{25}}}
print(F'{{{{{{{{x}}}}}}}}') # {{{{x}}}}



'''
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results

Let  inputs  be  10  and  7,
 a=input("enter 1st integer number= ")
 b=input("enter 2nd integer number= ")
 
What  is  the  sum ?  --->  17
 #
 sum=a+b
 print(sum)

What  is  the  difference ?  --->  3
 #
 diff=a-b
 print(diff)

What  is  the  product ?  ---> 70
 #
 mult=a*b
 print(mult)

What  is  the  quotient ?  --->  1.42
 #
 div=a/b
 print(div)

What  is  the  remainder ?  --->  3
 #
 modul=a%b
 print(modul) 

What  is  the  largest  number ?  ---> 10
 #
  print("max(", a ,",", b, ")","=",max(a,b))
 
What  is  the  smallest  number ?  --->  7
 # 
  print("min(", a ,",", b, ")","=",min(a,b))

What  is  the  sqrt  of  1st  input ?  --->  3.16
 #
 print("sqrt(10)=",math.sqrt(a))

What  is  the  result  of  power?  --->  10000000
 #
 result=math.pow(a,b)
 print(result)

What  is  the  gcd  of  2  numbers ?  ---> 1
 #
 result=math.gcd(a,b)
 print(result)

What  is  the  factorial   of  1st  input ?  ---> 10!
 #
 result=math.factorial(a)
 print(result)

'''

''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25

Hint:  Swap  references  but  not  objects
#
 Enter  1st  input :  25
 Enter  2nd  input : Hyd
 Before  swap :  x='25'            y='Hyd'
 After  swap :  x='Hyd'            y='25'

 x=int(input('enter 1st input: ' )
 y=int(input('enter 2nd input: ' )
 temp=x
 x=y
 y=temp
 print('x:',x,'y:',y)
'''

'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20
 #
 x=int(input('enter 1st input: '))
 y=int(input('enter 2nd input: '))
 z=int(input('enter 3rd input: '))
 result=max(x,y,z)
 print('largest num= ',result)

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   --->  42.8
 # 
 x=float(input('enter 1st input: '))
 y=float(input('enter 2nd input: '))
 z=float(input('enter 3rd input: '))
 result=max(x,y,z)
 print('largest num= ',result)

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'
#
 x=input('enter 1st input: ')
 y=input('enter 2nd input: ')
 z=input('enter 3rd input: ')
 result=max(x,y,z)
 print('largest String= ',result)

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  ---> [10 , 20 , 32 , 19]
  # error

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''

'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  ---> <
 #
 x=int(input(enter 1st num: ))
 y=int(input(enter 2nd num: ))
 if x<y:
    print(x ,'x is smallest') 
 else:
    print(y,'y is smallest')

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >
 #
 x=int(input("enter 1st number: " ))
 y=int(input('enter 2nd number: '))
 if x>y:
    print(x ,'x is greater') 
 else:
    print(y , 'y is greater')

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =
 # 
 x=int(input('enter 1st num: '))
 y=int(input('enter 2nd num: '))
  if x==y:
    print('both are same')
  else 
    print('not same')
 

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  ternary  operator
'''