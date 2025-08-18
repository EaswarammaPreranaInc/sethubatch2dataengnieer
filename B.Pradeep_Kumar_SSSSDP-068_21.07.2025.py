# How  to  print  dictionary  in  different  ways 
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 15 : 'Amar' #   
print(a) # ('Dictionary  with  print  function') 
How  to  print  dictionary  with  print()  function 
Print(a.keys())     
# ('Keys  of  dictionary')  dict_keys([10,20,15,18]) 
How  to  print  each  key  of  dict  'a' 
Print(a.values())     
('Values  of  dictionary')   # dict_values([‘Ramesh’,’Kiran’,’Amar’,’Sita’]) 
How  to  print  each  value  of  dict  'a' 
Print(a.items)      
 #('All  the  tuples  of  dict_items   object')  -dict_items([(10 : 'Ramesh'),( 20 : 
'Kiran'),( 15 : 'Amar'),( 15 : 'Amar')]) 
How  to  print  each  tuple  of  the  list  in  dict_items  object 
Print()    #    ('Elements  of  each   tuple')  For i in a: 
Print(i) 
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object 
Print(a.items(key,value))      
('Keys  and  values  of  dictionary') 
How  to  print  each  key  and  corresponding  value  in  dict  'a' 
#  Find  outputs (Home  work) 
a = { 
print('Hyd') , 
print('Sec') , 
print('Cyb') 
} 
print(type(a))  # Class ‘set’ 
print(a)  #  hyd <nextline> Sec <nextline> Cyb 
print(len(a))   #   1 
#  Anonymous  object  demo  program 
_ = 25 
print(_)  # 25 
print(type(_))   #  class int 
a , _ , c = 10 , 20 , 30 
print(a)   #  10 
print(_)  # 20 
print(c)   #  30 
for  _  in  range(5): 
print(_ , 'Hello')     
line> 4Hello 
#  Find  outputs 
a = 25 
#  0Hello  <Next line>  1Hello <Next line>  2Hello <Next line>  3Hello <Next 
print(id(a))   #   Adress of 25  
a = 35 
print(id(a))   # Address of 35 
# Find  outputs (Home  work) 
a = 25.7 
print(id(a))    #  Address of object 25.7 
print(a)  #  25.7 
a = 35.6 
print(id(a))  # #  Address of object 35.6 
print(a)   #  35.6 
b = True 
print(id(b))   #  #  Address of object True 
b = False 
print(id(b))   #   #  Address of object False 
c = None 
print(id(c))  #  Address of object None 
#  Find  outputs  (Home  work) 
a = 'Hyd' 
print(id(a))   ##  Address of object ‘Hyd’ 
a[1] = 'e' 
a = 'Sec' 
print(id(a))  # address of a 
b = (10 , 20 , 15 , 18) 
print(id(b))   # addres of b 
b[2] = 19 
b = (30 , 40 , 35 , 32) 
print(id(b))   # address of new b 
c = range(5) 
print(id(c))   # Addres of range(5) 
c[3] = 10 
# Find  outputs  (Home  work) 
a = 25 
b = 25 
print(a  is  b)   #    True 
c = 'Hyd' 
d = 'Hyd' 
print(c  is  d)   # True 
e = False 
f = False 
print(e  is  f)   # True 
g = range(10) 
h = range(10) 
print(g  is  h)    # False 
#Find  outputs(Home  work) 
a = [10 , 20 , 15 , 18] 
b = [10 , 20 , 15 , 18] 
print(a  is  b)   #  False 
c =  {10 : 20, 30 : 40} 
d =  {10 : 20, 30 : 40} 
print(c  is  d)   #   False 
e = (10 , 20 , 15 , 18) 
f = (10 , 20 , 15 , 18) 
print(e  is  f)    #  True 
g = {10 , 20 , 15 , 18} 
h = {10 , 20 , 15 , 18} 
print(g  is  h)    # True 
# Find outputs (Home work) 
print(10 + 20)   # 30 
print(10.8 + 20.6)   #  31.4 
print(3 + 4j + 5 + 6j)   # 8+10j 
print(True + False)  # True 
print('Hyder' + 'abad')  #  Hyderabad 
print('Sankar' + 'Dayal' + 'Sarma')   # SankerDayalSarma 
print('10' + '20')  # 1020 
print([10 , 20 , 30] + [1 , 2 , 3])  #  [10,20,30,1,2,3] 
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))   # (25 , 10.8 , 'Hyd', 3 + 4j , True , None) 
print({10 , 20} + {30 , 40})   #{ 10,20,30,40} 
print({10 : 'Hyd'} + {20 : 'Sec'})   #   {10:’hyd’,20:’sec’} 
print(range(4) + range(5))  # Error range will not repeated 
print(10 + '20') # Error due to int not added to  str 
print([10 , 20 , 30] + 5)  # error 
print([10 , 20 , 30] + (40 , 50 , 60))   # error 
# Find outputs (Home work) 
print(25 * 3)   # 75 
print(10.8 * 25.6)   #  276.48 
print(True * False)  # 0 
print((3 + 4j) * (5 + 6j))   # # (-9+38j) 
print(3 + 4j * 5 + 6j)   #  # (3+26j) 
print('25' * 3)   # 252525 
print(3 * '25')   #’252525’ 
print('Hyd' * 4)  ‘HydHydHydHyd’ 
print([10 , 20 , 15] * 2)   #  [10,20,15,10,20,15] 
print((25, 10.8, 'Hyd', True) * 3)   #   (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True) 
print([10 , 20 , 15] * 3.0)  # error due to sequence vcannot mul by float 
print({10 , 20 , 15} * 2)   # error due to set elements not repeated 
print({10 : 20 , 30 : 40} * 2)   # error 
print([10] * [20])  # Error due to 1st is list then 2nd variable is int only 
#  /  operator  demo  program 
print(9.0 / 2)   #   4.5 
print(9 / 2.0)   #  4.5 
print(9.0 / 2.0)   #4.5 
print(9 / 2)  #  4.5 
print(10.5 / 2)   # 5.25 
print(10 / 3)  #   3.33 
print(10 / 2)  #  5.0 
#  //  operator  demo  program 
print(9 // 2)  #   prev  integer  of (4.5) = 4 
print(9.0 // 2)   #  4.0 
print(9 // 2.0)   #  4,0 
print(9.0 // 2.0)   # 4.0 
print(10.5 // 2)   # 5.0 
print(10 // 3)   #  3 
print(10.0 // 3)  #    prev  integer  of  3.33 = 3.0 
print(8.5 // 3)   #    2.0 
print(18 // 4)  #  4 
print(-18 // 4)   #  -5 
print(-(18 // 4))  # -4 
# % operator demo program 
print(9 % 5)  #  4.0 
print(9.0 % 5)   #   4.0 
print(9 % 5.0)  #  4.0 
print(9.0 % 5.0)  #  4.0 
print(10.5 % 2)  #   0.5 
print(8.9 % 3)   #  2.9 
# Find outputs 
print(7 / 0)  #  Error 
print(7 // 0)  #  Error 
print(7 % 0)  #  error 
# ** operator demo program 
print(3 ** 4)   #   # 81   
print(10 ** -2)  #  0.01 
print(4 ** 3 ** 2)  #   262144 
print(3 + 4 * 5 - 32 / 2 ** 3)  #  19 
#  Relational  operators  demo  program (Home  work) 
print(9 >= 5)  #   True :  >  is  satisfied 
print(9 >= 9)   #   True :  =  is  satisfied 
print(9 >= 12)   #  False :  Both  are  not  satisfied 
print(6 <= 8)  # True 
print(6 <= 6)   # True 
print(6 <= 4)  # False 
print(9 != 7)  # True 
print(6 == 8)  # False 
print(True > False)  # True 
print(3 + 4j == 3 + 4j)  # True 
print(3 + 4j == 5 + 6j)  # False 
print(3 + 4j != 5 + 6j)  # True 
print(10 == 10.0)  # True 
# print(3 + 4j > 3 + 4j)  # Error 
print('Rama' > 'Rajesh')  # True 
print('Rama' < 'Sita')  # True 
print('Hyd' == 'Hyd')  # True 
print('Rama' <= 'Ramana')  # True 
print('Rama Rao' >= 'Rama')  # True 
print('Hyd' != 'Sec')  # True 
print('HYD' < 'hyd')  # True 
print(10 < 20 < 30)  # True 
print(10 >= 20 < 30)  # False 
print(10 < 20 > 30)  # False 
print(1 < 2 < 3 < 4)  # True 
print(1 < 2 > 3 > 1)  # False 
print(4 > 3 >= 3 > 2)  # True 
print(True or False)  # True 
print(False or True)  # True 
print(True or True)  # True 
print(False or False)  # False 
print(10 or 20)  # 10 
print(0 or 20)  # 20 
print(-25 or 0)  # -25 
print('' or 35)  # 35 
print(6j or 'Hyd')  # 6j 
print(0.0 or 3 + 4j)  # (3+4j) 
print('Hyd' or 10.8)  # Hyd 
print(not True)  # False 
print(not False)  # True 
print(not 25)  # False 
print(not 0)  # True 
print(not 'Hyd')  # False 
print(not '')  # True 
print(not -10)  # False 
print(not not 'Hyd')  # True 
i = 10 
i = not i > 14 
print(i)  # True 
print(not(6 < 4 or 9 >= 5 and 6 != 6))   
