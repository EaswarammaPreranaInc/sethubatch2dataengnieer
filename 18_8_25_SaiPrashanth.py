#!/usr/bin/env python
# coding: utf-8

# In[48]:


'''
Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]
'''

a=eval(input("Enter List"))
b=int(input('Enter  element  to  be  deleted : '))
try:
    while True:
        a.remove(b)
except:
    print(a)


# In[51]:


'''
Tricky  program
Write  a  program  to  remove  all  duplicate  elements  of  the  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]

Hint:  Use  count()  and  append()  methods
'''


a=eval(input("enter list : "))
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
print(b)


# In[53]:


'''
Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

1) Let  input  be  [25 , 25 , 25 , 25]
    What  is  the  output ?  ---> All  the  elements  are  identical
    How  many  elements  are  in  the  list ?  --->  4
    How  many  times  is  first  element  repeated ?  ---> 4

2) Let  input  be  [10 , 10 , 20 ,  10]
    What  is  the  output ?  --->All  the  elements  are  not  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ? --->  3

3) Hint: Use  len()  and  count()
'''

a=eval(input('enter list : '))
if a.count(a[0])==len(a):
    print("All  the  elements  are  identical")
else:
    print("All  the  elements  are  not identical")


# In[ ]:





# In[ ]:




