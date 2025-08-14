#!/usr/bin/env python
# coding: utf-8

# In[10]:


'''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

Let  list  be   [10 , 20 , 15 , 12 , 18]
1) What  is  the  output  if  15  is  seacrhed ?  --->  Found  at  index  2

2) What  is  the  output  if  19  is  seacrhed ?  --->  Not  found

3) What  action  to  be  made  when  'x'  does  not  match  with  the  current  element  of  list ?  --->
																						Compare  'x'  with  next  element  of  list

4) What  action  to  be  made  when  'x'  matches   with  list  element ?  --->
																				Print  found   message  along  with  index  and
																				do  not  search  for  'x'  in  rest  of  the  list

5) What  action  to  be  made  when  'x'   does  not  match  with  all  the  elements  of  list ?  --->
																										Print  not  found   message

6) Hint: Use  for  loop
'''
try:
    a=eval(input("enter any list: "))
    b=eval(input("Enter the element to be searched : "))
    for i in range(len(a)):
        if a[i]==b:
            print(f'Found  at   index  :   {i}')
            break
    else:
        print("Not  Found")
except:
    print("enter list values only")


# In[13]:


'''
Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found (Assume  that  list  may  contain  duplicate  elements)

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

Outputs :  15  is  found  at  index  2
                 15  is  found  at  index  5
                 15  is  found  at  index  8
                 15  is  found   3  times
'''

try:
    a=eval(input("enter any list: "))
    b=eval(input("Enter the element to be searched : "))
    c=0
    for i in range(len(a)):
        if a[i]==b:
            print(f'Found  at   index  :   {i}')
            c+=1
    if c>0:
        print(f'{b} is found {c} times')
    else:
        print("Not  Found")
except:
    print("enter list values only")


# In[18]:


'''
(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  ctrl + z

sum = 0 + 25 + 10.8 + True = 36.8
ctr = 0 + 1 + 1 + 1 = 3

1) What  is  ctrl + z ?  ---> End  of  inputs  i.e.  No  more  inputs

2) What  does  input()  function  do  when  input  is  ctrl + z ?  ---> Throws  EOFError

3) How  is   end  of  inputs  denoted  in  unix ?  ---> ctrl + d
'''
try:
    a=0
    while True:
        b=eval(input("Enter input  (ctrl + z  to  stop) : "))
        a+=b
except:
    print(a)


# In[ ]:




