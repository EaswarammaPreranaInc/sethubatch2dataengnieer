#!/usr/bin/env python
# coding: utf-8

# In[17]:


a=input("Enter first String")
b=input("Enter Second String")
if len(a)<2 and len(b)<2:
    print("Input  should  be  a  min  of  2-char  string")
else:
    c=a[:2]+b[2:]
    d=b[:2]+a[2:]
    print(d,c)


# In[19]:


a=input("Enter string")
if len(a)>4:
    print(a[:2]+a[-2:])
else:
    print()


# In[22]:


a=input("enter string")
print("forward direction")
for i in range(len(a)):
    print(f'Character  at  index  {i}  :  {a[i]}')
print("reverse directions")
for i in range(len(a)):
    print(f'Character  at  index  {-i-1}  :  {a[-1-i]}')
    


# In[24]:


#even and odd index
a=input("enter string")
even=''
odd=''
for i in range(len(a)):
    if i%2:
        even+=a[i]
    else:
        odd+=a[i]
print("String  at  even  indexes  : ",even)
print('String  at  odd  indexes  : ',odd)


# In[29]:


try:    
    t=input('Enter  any  string  with  alternate  character  and  digit : ')
    a=''
    for i in range(0,len(t),2):
        a+=t[i]*int(t[i+1])
    print(a)
except:
    print("String   should  have  alternate  character  and  digit")
    


# In[5]:


a=input("Enter first string")
b=input("enter second string")
c=''
i=0
while i<min(len(a),len(b)):
    c+=a[i]+b[i]
    i+=1
c += a[len(b):] if len(a) > len(b) else b[len(a):]
print(c)


# In[8]:


#duplicate
a=input("enter string: ")
b=''
for i in a:
    if i not in b:
        b+=i
print(b)


# In[ ]:


a=input("Enter  any  string  with  alternate  character  and  digit : ")
b=''
for i in range(len(a),2):
    c=ord(a[i])
    b+=a[i]+chr(c+int())

