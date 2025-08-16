#!/usr/bin/env python
# coding: utf-8

# In[2]:


#  Find  outputs
print({10 , 20}  |  {30 , 20})	#{10 , 20 , 30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'}) #{10:'Hyd' , 20 : 'Vja' , 30 : 'Cyb}
#print(range(4) | range(5))	#error unsupported operand type
#print([10 , 20]  |  [30 , 20])	#error unsupported operand typ


# In[6]:


#  Assignment  operators  demo  program  (Home  work)
a = 25  #Ref a pointed to object 25
print(a)	#25
b =  a		#Ref b pointed to ref a
print(b)	#25
print(a  is  b)	#True 
x = 4		#Ref x pointed to object 4
y = 5		#Ref y pointed to object 5
z = x + y * 6	# y*6= 30 x+y=4+30=34
print(z)	#34
#25 = a		#error object cant point to ref
#a + b = x + y	#error object cant assess to object


# In[8]:


# Find outputs (Home work)
a = b = c = 25	#ref a is pointed to ref b is pointed to ref c is pointed to object 25
print(id(a))	#addresss of object 25
print(id(b))	#same address of object 25
print(id(c))	#same address of object 25
print(a,b,c)#25 25 25


# In[9]:


# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'	#ref x is ponited to object 25
				#ref y is pointed to object 10.8
				#ref z is pointed to object 'Hyd'
print(x)			#25
print(y)			#10.8
print(z)			#Hyd


# In[11]:


# Find outputs (Home work)
a , b , c = 3 , 4 , 5	#ref a is ponited to object 3
			#ref b is pointed to object 4
			#ref c is pointed to object 5
a*=b+c		#a=a*(b+c)=3*(4+5)=3*(9)=27
print(a)		#27


# In[14]:


#Find outputs (Home work)
a = 20		#ref a is ponited to object 20
a %= 3+2*4	#a=a%(3+2*4)=20%(3+8)=20%11=9
print(a)	#9


# In[15]:


# Find outputs (Home work)
a = 3		#ref a is ponited to object 3
a **= 4		#a=a**(4)=3**(4)=81
print(a)	#81


# In[17]:


# Identity operators demo program
a = 25		#ref a is ponited to object 25
b = 25		#ref b is ponited to same object 25
print(a  is  b)	#True
print(a  is  not  b)#False
print(a==b)	#True


# In[19]:


# Find outputs (Home work)
a = 25		#ref a is ponited to object 25
b = 25.0	#ref b is ponited to  object 25.0
print(a  is  b)	#False
print(a  is  not  b)	#True
print(a == b)	#True


# In[21]:


# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b)	#True
print(a  is  not  b)	#False
print(a == b)#True
print()	#empty line
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y)	#Fasle 
print(x  is  not  y)	#True
print(x == y)	#True
print()#empty line
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n)	#True
print(m  is  not  n)#Fasle
print(m == n)#True
print(x == m)#False


# In[25]:


# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)#True
print(19 in list)#False
print(14 not in list)#True
print(15 not in list)#False
s = 'Hyd is green city'
print( 'is' in s)#True
print('was' in s)#False
print('g' in s)#True
print('z' in s)#False
print(' ' in s)#True
print('gre' in s)#True
print('yd i' in s)#True
print('' in s)#True

print('' not in s)#False


# In[3]:


# Find outputs (Home work)
a = [10,20,30]
b = (10,20,30)
print(a  is  b) 
print(a==b)


# In[5]:


# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) 
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q)
m = range(5)
n = range(5)
print(m==n)


# In[ ]:




