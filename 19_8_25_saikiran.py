#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
    i=-1
    while  (i := a . index(15 , i + 1)):
        print(i)
        
except:
    print(F'15  is  found  {a . count(15)}  times ')


# In[4]:


'''
Most   tricky  program
Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
Print  True  if  it  is  a  sublist  and  False  otherwise

1) First  list :  [10 , 20 , 30]
    Second  list :  [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
    What  is  the  output ?  --->  True  becoz  elements  10 , 20 , 30  are  in  2nd  list  in  same  order

2) First  list :  [10 , 20 , 20]
    Second  list :  [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
    What  is  the  output ?  ---> False  becoz   elements  10 , 20 , 30  are  not  in  2nd  list

3) First  list :  [2 , 2 , 5]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  True  becoz   elements  2 , 2 , 5  are  in  [2 , 2 , 3 , 4 , 5]

4) First  list :  [2 , 4 , 3]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  False  becoz   elements  2 , 4 , 3   are  not  in  [2 , 2 , 3 , 4 , 5]

5) Hint:  Use  index()  method
'''
a=eval(input("enter First List: "))
b=eval(input("enter Sencond List: "))
c=0
x=True
for i in a:
    if i in b[c:]:
        c=b.index(i)+1
    else:
        x=False
        break
print(x)


# In[6]:


'''
Tricky  program
Write  a  program  to  determine  mode

1) What  is  mode ?  ---> The  element  which  is  repeated  maximum  number  of  times  in  the  list

2) Let  input  be  [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
    What  is  set(list) ?  ---> {12 , 20 , 18 , 15 , 10}
    How  many  times  is  first  element  12  repeated  in  the  list  ?  --->  1
    How  many  times  is  2nd  element  20  repeated  in  the  list  ?  --->  3
    How  many  times  is  3rd  element  18  repeated  in  the  list  ?  --->  2
    How  many  times  is  4th  element  15  repeated  in  the  list  ?  --->  5
    How  many  times  is  last  element  10  repeated  in  the  list  ?  --->  4
    What  is  the  mode  ?  --->	15  becoz  it  is  repeated  max  number  of  times  i.e.  5

3) mode = 15
    ctr = 5
'''


a=eval(input("enter list: "))
mode=0
ctr=0
for i in set(a):
    if a.count(i)>ctr:
        mode=i
        ctr=a.count(i)
print(mode)


# In[10]:


a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print(a)
print(*a)


# In[19]:


#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')
print(a)
print('Each  inner  list   of   outer  list  without  indexes')
for i in a:
    print(i)
print('Elements  in  the  form   of  matrix   without  using  indexes')
for i in a:
    for j in i:
        print(j,end=" ")
    print()
print('Elements  in  the  form   of  matrix  using  indexes')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()


# In[ ]:




