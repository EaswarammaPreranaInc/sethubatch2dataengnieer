#!/usr/bin/env python
# coding: utf-8

# In[18]:


'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
a=input("Enter  mixed  case  string :  ")
a=a.upper()
j=set(a)
b='AEIOU'
c=''
for i in j:
    if i in b:
        c+=i
print('Distinct  vowels :   ',c)
        
        


# In[ ]:




