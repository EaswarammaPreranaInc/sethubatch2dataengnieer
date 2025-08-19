#!/usr/bin/env python
# coding: utf-8

# In[46]:


# eval()  function  demo  program
print(eval('25'))	#25
print(eval('10.8'))	#10.8
print(eval('False'))	#False	
print(eval('3+4j'))	#3+4j
#print(eval('Hyd'))	#Hyd
print(eval("    'Hyd'   "))	#Hyd
print(eval('3 + 4 * 5'))	#23
print(eval('[10 , 20 , 15 , 18]'))#[10,20,15,18]
print(eval('{10,20,15,18,20,12,18}'))#{10,20,15,18,12}
print(eval('(10 , 20 , 30)'))	#(10 , 20 , 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))#{10:'Sec'}
#print(eval(4+5))#Error input should be string


# In[48]:


#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))	#Hyd
hyd = 'Sec'
print(eval('hyd'))		#Sec
sec = '25'
print(eval('sec'))		#25
print(eval(sec))		#Error 
cyb = 10.8
print(eval('cyb'))		#10.8
#print(eval(cyb))		##Error input should be string


# In[51]:


#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))	#Hyd
				#None


# In[59]:


#  Find  outputs  (Home  work)
print(bool('False'))	#True
print(eval('False'))	#False
print(bool(''))		#True
print(eval('  ""  '))	#''
#print(eval(''))		#error
print(eval('  " "   '))#' '
#print(eval(' '))	#error


# In[60]:


# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))#Enter any input
print(type(x))		#type of input if string 'str' if float 'float'
print(x)		#object x


# In[64]:


# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')	#Enter any string
print(len(a))				#length of input string
print(a)				#object a
b = eval(input('Enter   any  string  : '))#Enter any string
print(len(b))				#len of object b
print(b)				#print object b



# In[ ]:




