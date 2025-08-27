#Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results

Let  inputs  be  10  and  7,
What  is  the  sum ?  --->  17
What  is  the  difference ?  --->  3
What  is  the  product ?  ---> 70
What  is  the  quotient ?  --->  1.42
What  is  the  remainder ?  --->  3
What  is  the  largest  number ?  ---> 10
What  is  the  smallest  number ?  --->  7
What  is  the  sqrt  of  1st  input ?  --->  3.16
What  is  the  result  of  power?  --->  10000000
What  is  the  gcd  of  2  numbers ?  ---> 1
What  is  the  factorial   of  1st  input ?  ---> 10!

# In[20]:


import math
try :
    a=int(input('Enter 1st integer number:'))
    b=int(input('Enter 2st integer number:'))
except:
    print("input should be int only")
#sum of no
print('sum of 2 numbers')
print(f'{a} + {b} = {a+b}')

#difference of nos
print('diff of 2 numbers')
print(f'{a} - {b} = {a-b}')

#product  of 2 nos
print('product of 2 numbers')
print(f'{a} * {b} = {a*b}')

#quotient  of 2 nos
print('quotient of 2 numbers')
print(f'{a} / {b} = {a/b}')

#remainder  of 2 nos
print('remainder of 2 numbers')
print(f'{a} % {b} = {a%b}')

#largest numbers of 2 nos
print('largest of 2 numbers')
print(f'max({a},{b}) = {max(a,b)}')

#smallest  of 2 nos
print('smallest of 2 numbers')
print(f'min({a},{b}) = {min(a,b)}')

#pow  of 2 nos
print('power of 2 numbers')
print(f'{a}^{b} = {pow(a,b)}')

#sqrt  of  no
print('sqrt of 1st number')
print(f'sqrt({a}) = {math.sqrt(a)}')

#gcd  of  2 nos
print('gcd of 2 number')
print(f'gcd({a,b}) = {math.gcd(a,b)}')

#factorial  of  no
print('factorial of 1st number')
print(f'fact({a}) = {math.factorial(a)}')

Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

# In[30]:


try :
    x=eval(input('Enter element:'))
    y=eval(input('Enter element:'))
    print('elements before swaping')
    print(f'x = \'{x}\' \t y = \'{y}\' ')
    x,y=y,x
    print('elements after swaping' )
    print(f'x = \'{x}\' \t y = \'{y}\' ')
except:
    print("enter string in quotes")


Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function
# In[1]:


try :
    m=eval(input('enter 1st input:'))
    n=eval(input('enter 2nd input:'))
    o=eval(input('enter 3rd input:'))
    print(m if m>n and m>o  else n if n>o else o) 
except:
    print('enter string in quotes')

Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,'<'  if  1st  input  <  2nd  input  and '='  if  inputs  are  same
# In[36]:


try:
    ele1=eval(input('enter 1st input:'))
    ele2=eval(input('enter 2nd input:'))
    print('>' if ele1>ele2 else '<' if ele2>ele1 else '=')
except:
    print('enter string in quotes')

Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0
# In[40]:


try :
    n1=int(input('enter any number'))
    print(1 if n1>0 else -1 if n1<0 else 0)
except:
    print('enter integer value only')


# In[41]:


try :
    n1=int(input('enter any +ve number'))
    print('Odd number' if n1%2!=0 else 'even number')
except:
    print('enter integer value only')

(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)

# In[2]:


try :
    length=float(input('enter len of rectangle:'))
    breadth=float(input('enter breadth of rectangle:'))
    print(f'length = {length}, breadth = {breadth}')
    area=length*breadth
    print(f'area = {area}')
    peri=2*(length+breadth)
    print(f'perimeter = {peri}')
except:
    print('enter float or integer value only')

(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3

# In[3]:


import math
try:
    r1=float(input('enter radius'))
    volume=(4/3)*math.pi*(r1**3)
    print(f'volume = {volume}')
except:
    print('enter float or integer value only')

(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
'''
# In[61]:


try:
    pri=float(input('enter priciple:'))
    time=float(input('enter time :'))
    interest=float(input('enter interest'))
    si=pri*time*interest/100
    print(f'simple interest ={si}')
    ci = pri * (1 + (interest / 100)) ** time - pri
    print(f'compound interest={ci}')
except:
    print('enter integer or float value only')

(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10

# In[64]:


try:
    int1=eval(input('enter number:'))
    int2=eval(input('enter number:'))
    temp=int1
    int1=int2
    int2=temp
    print(f'{int1 = } and {int2 = }')
except:
    print('enter integer only')

(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
# In[69]:


try:
    i1=int(input())
    i2=int(input())
    i1=i1+i2
    i2=i1-i2
    i1=i1-i2
    print(f'x = {i1} y = {i2}')
except:
    print('enter integer values only')

(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  -200
y =  100

# In[72]:


try:
    i1=int(input())
    i2=int(input())
    i1=i1*i2
    i2=i1//i2
    i1=i1//i2
    print(f'x = {i1} y = {i2}')
except:
    print('enter integer values only')


# In[ ]:



