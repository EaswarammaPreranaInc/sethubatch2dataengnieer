#!/usr/bin/env python
# coding: utf-8
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  ---> (3 + 4j) - (5 + 6j) =  -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 =  -9 + 38j


What  is  the  division ?  ---> (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
                                                                         =   (15 - 18j + 20j + 24) / (25 + 36)
																		 = 39 / 61 + 2j / 61
# In[15]:


try:
    a=complex(input('Enter first complex number'))
    b=complex(input('Enter second complex number'))
    print(f'Sum : {a+b}')
    print(f'Difference : {a-b}')
    print(f'product : {a*b}')
    print(f'Division : {a/b}')
except:
    print('enter complex no only')


# In[13]:


# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
try:
    n=int(input("enter any number: "))
    if n%2==0:
        print("even")
    else:
        print("odd")
except:
    print("enter int value only")


# In[9]:


# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
try:
    m=int(input('enter no between (1-12) '))
    if m==1:
        print('Jan')
    elif m==2:
        print('Feb')
    elif m==3:
        print('Mar')
    elif m==4:
        print('April')
    elif m==5:
        print('May')
    elif m==6:
        print('June')
    elif m==7:
        print('July')
    elif m==8:
        print('Aug')
    elif m==9:
        print('Sep')
    elif m==10:
        print('Oct')
    elif m==11:
        print('Nov')
    elif m==12:
        print('Dec')
    else:
        print('Enter no between (1-12) only')
except:
    print('Input  should  be  an  integer')


# In[19]:


'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''


try:
    d=int(input("enter no between 1-9 "))
    if d==0:
        print('Zero')
    else:
        if d==1:
            print('One')
        else:
            if d==2:
                print('Two')
            else:
                if d==3:
                    print('Three')
                else:
                    if d==4:
                        print('Four')
                    else:
                        if d==5:
                            print('Five')
                        else:
                            if d==6:
                                print('Six')
                            else:
                                if d==7:
                                    print('seven')
                                else:
                                    if d==8:
                                        print('Eight')
                                    else:
                                        if d==9:
                                            print('Nine')
                                        else:
                                            print('Invalid')
except:
    print('enter integer value only')

