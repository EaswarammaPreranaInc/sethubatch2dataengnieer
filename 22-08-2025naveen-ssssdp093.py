
#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0   1    2     3    4    5   6    7    8    9    10
try:
    i = a . index(15)
    while  True:
        print('15 is found at index : ' , i)              # 2, 5, 8
        i = a . index(15 , i + 1)                         
except:
        print(F'15  is  found  {a . count(15)}  times')   #15 is found 3 times


#output
'''
15 is found at index : 2
15 is found at index : 5
15 is found at index : 8
15 is found 3 times
'''


#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35                 #error, elements of tuple can't be modified
print(a)                   #(10, 20, 30, 40, 50)
print(id(a))               #some address
a = a[:2] + (35,) + a[3:]  #new tuple created by replacing old element
print(a)                   #(10, 20, 35, 40, 50)
print(id(a))               #new address
print()

#output
'''
(10, 20, 30, 40, 50)
2599813978992
(10, 20, 35, 40, 50)
2599814217008

'''



# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
#a . remove(30)              #TypeError, tuple can't be modified
#del  a[2]                   #Type Error, tuple can't be modified
#a . pop(2)                  #AttributeError, tuple can't be modified
print(a)                    #(10, 20, 30, 40, 50)
print(id(a))                #some address
a = a[:2] + a[3:]           #How  to  remove  30  from  tuple  'a'
print(a)                    #(10, 20, 40, 50)
print(id(a))                #new address


#output
'''
(10, 20, 30, 40, 50)
2805039111024
(10, 20, 40, 50)
2805039347680
'''




#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)                            #( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a))                      #<class 'tuple'>
print(len(a))                       #3
print('How  to  print  1st  inner  tuple')
print(a[0])
print('How  to  print  2nd  inner  tuple')
print(a[1])
print('How  to  print  3rd  inner  tuple')
print(a[2])
print('How  to  print  20')
print(a[0][1])
print('How  to  print  50')
print(a[1][2])
print('How  to  print  90')
print(a[2][3])
      


# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print('How  to   print  inner  tuple')
print(a[0])
print('How  to   print  inner  tuple  in  another  way')
print(*a)
print('How   to  print   10')
print(a[0][0])
print('How   to  print   20')
print(a[0][1])
print('How   to  print   30')
print(a[0][2])
b = ((),)
print('How  to   print  inner  tuple  of  tuple  \'b\'')
print(b[0])
print('How  to   print  inner  tuple  of  tuple  \'b\'  in  another  way')
print(*b)
      




#  Find  outputs (Home  work)
a = ((10 , 20 , 30))  
print(a)   #(10,20,30)
print(*a)  #10,20,30
b = (())  
print(b)   #()
print(*b)  #new line

#output
'''
(10, 20, 30)
10 20 30
()
'''

# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)                       #{10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a))                 #<class 'str'>
b = eval(a)                    
print(b)                       #in any order: {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(b))                 #<class 'set'>

#output
'''
{10,20,15,18,20,12,18}
<class 'str'>
{18, 20, 10, 12, 15}
<class 'set'>
'''

#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})       #in any order: {10, 20, 30}
#print({[10 , 20 , 30]})       #Error, there can't be list in set
#print({{10 , 20 , 30}})       #Error, there can't be nested set
#print({{}})                   #Error, there can't be dict in set


# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  elements  of  set  with  for  loop')
for x in a:
    print(x, end=' ')   #25 10.8 Hyd True

#output
'''
{25, 10.8, True, 'Hyd'}
#Iterate  elements  of  set  with  for  loop
25 10.8 True Hyd
'''

# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)         #{'Hyd', True, 25} in any order
print(len(s))    #3
print(type(s))   #<class 'set'>

#output
'''
{True, 'Hyd', 25}
3
<class 'set'>
'''


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)                #{'Hyd',  25,  True,  10.8 }
a , b , c , d = s       #elements are assigned same as we iterate through the set
print(a)                #25 
print(b)                #'Hyd'  
print(c)                #10.8 
print(d)                #True 

#output
'''
{25, 'Hyd', 10.8, True}
25
Hyd
10.8
True
'''
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)         #{'Hyd',  25,  True,  10.8 }
a , *b = s       #first element in set iteration to a, remaining all to b
print(a)         #25 e.g
print(b)         #[ 10.8,True,'Hyd']
print(type(b))   #<class 'list'>

#output
'''
{25, 10.8, True, 'Hyd'}
25
[10.8, True, 'Hyd']
<class 'list'>
'''


# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)           #elements in any order e.g. {25, 10.8, 'Hyd', True}
a , *b , c = s     
print(a)           #25
print(b)           #[10.8, 'Hyd']
print(c)           #True

#output
'''
{25, True , 10.8 , 'Hyd'}
25
[10.8, 'Hyd']
True
'''

# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)    #any order e.g. {10, 20}
x , y = s   
print(x)    #10
print(y)    #20

#output
'''
{10, 20}
10
20
'''

# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)                  #any order: {100, 110, 120, 140, 130, 150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)       
print(d)                  #any order: {10, 20, 15, 18, 50, 12}
e = set('Rama  rAo')      
print(e)                  #any order: {'R', 'a', 'm', ' ', 'A', 'o'}
#print(set(25))            #error, arg must only be sequence
print(set())              #set()

#output
'''
{130, 100, 140, 110, 150, 120}
{10, 12, 15, 18, 50, 20}
{'m', 'A', 'o', 'a', ' ', 'R', 'r'}
set()
'''