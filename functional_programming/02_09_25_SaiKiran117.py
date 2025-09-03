#!/usr/bin/env python
# coding: utf-8

#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)  #  Tuple  of  4  elements  (or)  args  are  passed  to  the  function
f1()
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
f1('Hyd')
tpl = (100 , 200 , 150)
f1(tpl)
f1(t = (10 , 20 , 30))

'''
(10,20,15,18)
<class 'tuple'>
4

()
<class 'tuple'>
0

([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
<class 'tuple'>
3

('Hyd',)
<class 'tuple'>
1

((100 , 200 , 150),)
<class 'tuple'>
1

error 
'''
# In[5]:


#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function  (Home  work)
def  avg(*a):
	#Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
    try:
        print(sum(a)/len(a))
    except:
        print('give input as integer values only')
# End  of  the  function
print(avg(10 , 20 , 15 , 18))
print(avg(25 , 10.8 , True))
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
print(avg())
print(avg(25))
print(avg(3 + 4j , 5 + 6j))
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))


# In[7]:


#  Write  a  function  to  concatenate  strings  passed  to  the  function  (Home  work)
def  concat(*a):
	#Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
    try:
        print(" ".join(a))
    except:
        print("input should be string values only")
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
print(concat(1, 2, 3))

#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)#a : 10 <tab> b: (20 , 30 , 40)
f1(50 , 60) ##a : 50 <tab> b: (60,)
f1(70)  #a : 70 <tab> b: ()
f1(a = 80) ##a :80 <tab> b: ()
f1(b = (10 , 20 , 30) , a = 40)#error
f1()  ##a :25 <tab> b: ()
f1(a = 10 , (20 , 30 , 40)) #error 
f1(25 , b = (10 , 20 , 30)) #error
f1(25 , a = (10 , 20 , 30))  #error 
f1((10 , 20 , 30) , 10 , 20 , 30) #a : (10 , 20 , 30) <tab> b: (10, 20 , 30 )
f1(a = (10 , 20 , 30) , 10 , 20 , 30) #error #Find  outputs (Home  work)
def    f1(*a , b):
    print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)  #a  :  (10, 20, 30) <tab> b  :  40
f1(50 , b = 60)  #a  :  (50,)<tab>b  :  60
f1(b = 70) #a  :  ()<tab>b  :  70
f1(b = 10 , a = (20 , 30 , 40)) #error
f1(b = 10 , (20 , 30 , 40)) #error
f1() #error
f1(10 , 20 , 30 , (10 , 20 , 30)) #error
f1(10 , 20 , 30 , 40)
f1(25)
f1(10 , 20 , 30 , b = (10 , 20 , 30))  #a  :  (10, 20, 30)<tab> b  :  (10, 20, 30)#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)  #a  :  10<tab>b  :  (20, 30, 40)<tab>c  :  50
f1(60 , 70 , c = 80)  #a  :  60<tab>b  :  (70,)<tab>c  :  80
f1(90 , c = 100)  #a  :  90<tab>b  :  ()<tab>c  :  100
f1(a = 1 , 2 , c = 3)#error
f1(1 , 2 , 3)#error
f1(a = 1 , b = 2 , c = 3)#error
f1(a = 25 , 100 , 200 , 300 , c = 35)#error# Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b):  #invalid due to *b
        pass
def  f2(*a , b):#valid
        pass
def  f3(a , *b):#valid
        pass
def  f4(a , b): #valid
        pass
def    f5(a , *b , c): #valid
        pass
def   f6( * , a , *b , c): #invalid due to *b
       pass
def   f7(a , *b , c ,  /):  #invalid due to '/'
       pass# Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))
'''
outputs:
([10, 20], {40, 30}, (50, 60))
<class 'tuple'>
[10, 20]
<class 'list'>
{40, 30}
<class 'set'>
(50, 60)
<class 'tuple'>
'''# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')   #  Dictionary  is  passed  to  the  function
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
disp()

'''
Results
<class 'dict'>
{'RollNo': 10, 'StudName': 'Rama  Rao'}

Results
<class 'dict'>
{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

Results
<class 'dict'>
{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}

Results
<class 'dict'>
{}

'''# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')  #Results
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')  Empno ... 25 <next line> Empname ... Rama  Rao <next line> Salary ... 10000.0 <next line>Gender ... m
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)  
print()
f1('Hyd' , 10 , 20 , 30)
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)

'''
output
25

Hyd
(10, 20, 30)

10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}
'''
# In[ ]:




