#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
    print(index)
    index = a . find('is' , index +1)
print('End')


# In[2]:


'''  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
try:
    index1 = a . index('is')
    while  index1 != -1:
        print(index1)
        index1 = a . index('is' , index1 + 1)
except ValueError:
    print('End')
    



# In[5]:


'''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . rfind('is')
while  index != -1:
	print(index)
	index = a . rfind('is' ,0, index + 1)
print('End')


# In[8]:


'''  (Home  work)
rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
try:
    index = a . rindex('is')
    while  index != -1:
        print(index)
        index = a .rindex('is' ,0, index + 1)
except ValueError:
    print('End')



# In[28]:


'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  ---> ba**le
'''
a='babble'
print(a[0]+a[1:].replace(a[0],'*'))


# In[29]:


#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))
print(a)


# In[42]:


'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  123+45+6+789
Print  the  sum  result
'''

a=input('Enter the expression:')
b=a.split('+')
c=0
for i in b:
    c+=int(i)
print(c)


# In[56]:


'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself
'''

a=input("enter string: ")
if len(a)<3:
    print(a)
elif a.endswith('ing'):
    print(a+'ly')
else:
    print(a+'ing')
    


# In[61]:


# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())  #  False
print('\n  \t' . isspace()) #  True
print('\n  7\t' . isspace())
print('\n' . isspace())
print('\n  $\t' . isspace())
print('\t' . isspace())
print('' . isspace())
print(' ' . isspace())


# In[70]:


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a ,y=b,x=c))


# In[86]:


'''
Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  --->  Alphanumeric  character , Alphabet character , Upper case  alphabet

2) What  are  the  three  outputs  if  input  is  'a' ?  ---> Alphanumeric  character , Alphabet character , lower case  alphabet

3) What  are  the  two  outputs  if  input  is  '7' ?  ---> Alphanumeric  character , digit  character

4) What  is  the  output  if  input  is  '$' ?  ---> Special  character

5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space

6) What  is  the  output  if  input  is  <tab>  key ?  --->  White  space

7) What  is  the  output  if  input   is   <enter>   key ?  ---> White  space

8) Hint2:  Use  nested  if  and   elif
'''


a=input('Enter  any  character: ')
if a.isalpha():
    print('Alphabet character')
    print('Alphanumeric  character')
    if a.isupper():
        print('Upper case  alphabet')
    else: 
        print('lower case  alphabet')
elif a.isnumeric():
    print(' Alphanumeric  character')
    print("digit  character")
elif a.isspace():
    print('White space')
else:
    print("Special character")


# In[92]:


'''
Write  a  program  to  reverse  a  string  without  slice

1) Let  input  be   Hyd
    What  is  the  output ?  --->  dyH

2)   H       y      d
      -3     -2     -1

      i       a[-i]            b
    ---------------------------------------
                                ''
     1        'd'             '' + 'd' = 'd'
     2       'y'             'd' + 'y' = 'dy'
     3       'H'            'dy' + 'H' = 'dyH'
  ---------------------------------------------
'''
a=input('Enter string')
b=''
for i in range(1,len(a)+1):
   b+=a[-i]
print(b)


# In[93]:


'''
Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> city   green   is   Hyd

2) What  is  the  result  of  input . split() ?  --->  ['Hyd' , 'is' , 'green' , 'city']   --->   Assume  that  it  is  'b'

3) i        b[-i]           c
   ---------------------------------------------
                              ''
   1        'city'         '' + 'city' + ' '=  'city '
   2        'green'     'city ' + 'green' + ' ' = 'city green '
   3        'is'            'city green ' + 'is' + ' ' =  'city green is '
   4        'Hyd'        'city green is ' + 'Hyd' + ' ' = 'city green is Hyd '
   --------------------------------------------------------
'''
a=input("Enter String")
b=a.split()
c=''
for i in range(1,len(b)+1):
    c+=b[-i]+' '
print(c)
    


# In[95]:


'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''

a=input("enter sentence: ")
b=a.split()
c=''
for i in b:
    c+=i[::-1]+" "
print(c)


# In[104]:


'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1)What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z'
    digit = '' + '1' + '3' + '5' + '7' + '9'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''

a=input("enter string: ")
alpha=[]
digit=[]
for i in a:
    if i.isalpha():
        alpha.append(i)
    else:
        digit.append(i)
alpha.sort()
digit.sort()
sortedele=''
for i in alpha:
    sortedele+=i
for i in digit:
    sortedele+=i
print(sortedele)
    


# In[ ]:




