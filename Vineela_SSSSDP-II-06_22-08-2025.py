#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')
  
  '''output: 
  15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15  is  found  3  times'''




#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35
print(a)
print(id(a))
How  to  modify  30  in  tuple  to  35
print(a)
print(id(a))    


a = (10, 20, 30, 40, 50)
print(a, id(a))

# Convert to list → modify → convert back to tuple
b = list(a)
b[2] = 35
a = tuple(b)

print(a, id(a))




# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0    1     2    3   4
a . remove(30)
del  a[2]
a . pop(2)
print(a)
print(id(a))
How  to  remove  30  from  tuple  'a'
print(a)
print(id(a))


a = (10, 20, 30, 40, 50)
a = a[:2] + a[3:]   # skip the index 2 element
print(a)                #  (10, 20, 40, 50)
print(id(a))             # different address



#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)                      # ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a))               # # <class 'tuple'>  
print(len(a))                # 3 
print(How  to  print  1st  inner  tuple)            # 1st inner tuple → (10, 20)
print(How  to  print  2nd  inner  tuple)            # 2nd inner tuple → (30, 40, 50)
print(How  to  print  3rd  inner  tuple)            # 3rd inner tuple → (60, 70, 80, 90)
print(How  to  print  20)                   # print(a[0][1])
print(How  to  print  50)                   # print(a[1][2]) 
print(How  to  print  90)                   # print(a[2][3])




# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(How  to   print  inner  tuple)                            # print(a[0])
print(How  to   print  inner  tuple  in  another  way)          # print(*a)
print(How   to  print   10)                             # print(a[0][0])
print(How   to  print   20)                             # print(a[0][1])
print(How   to  print   30)                             # print(a[0][2])
b = ((),)                                                  
print(How  to   print  inner  tuple  of  tuple  'b')         # print(b[0]) 
print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)      # print(*b) 




#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)            # ((10 , 20 , 30))
print(*a)           #  10, 20, 30 
b = (())            
print(b)            # ()
print(*b)           # Nothing because its empty




# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')        
print(a)                        # "{10 , 20 , 15 , 18 , 20 , 12 , 18}"   reads input as string
print(type(a))                  #  <class 'str'>    because input function reads string input
b = eval(a)
print(b)                         # {10, 12, 15, 18, 20}   (duplicates are removed and order may vary)
print(type(b))                   # #  <class 'set'>  





#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})         # {(10, 20, 30)}  (10, 20, 30) is a tuple → immutable → allowed. Elements of a set must be immutable
print({[10 , 20 , 30]})         # error  [10, 20, 30] is a list → mutable → not hashable.
print({{10 , 20 , 30}})         # error  {10, 20, 30} is itself a set → mutable → not hashable.
print({{}})                     # error  {} is an empty dictionary which is mutable..




# How  to  print  set  in  different ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  elements  of  set  with  for  loop')
How  to  iterate  set  with  for  loop
# for x in a:
    print(x)            # This prints each element on a new line (order may vary).
    
# Printing with * operator (unpacking)
print("Set with unpacking (*):")
print(*a)



# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)                    # s = {'Hyd', True, 25}
print(len(s))               # 3
print(type(s))              # <class 'set'>




# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)                            # {25, 10.8, 'Hyd', True}
a , b , c , d = s
print(a)                            # 25
print(b)                            # 10.8
print(c)                            # 'Hyd'
print(d)                            # True



# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)                            # {25, 10.8, 'Hyd', True}
a , *b = s
print(a)                            # 25
print(b)                            # [10.8, 'Hyd', True]
print(type(b))                      #  <class 'list'>




# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)                            # {25, 10.8, 'Hyd', True}
a , *b , c = s
print(a)                            # 'Hyd'
print(b)                            # [25,  True]
print(c)                            # 10.8




# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)                    # {10, 20} any order and duplicates are removed
x , y = s
print(x)                    # 10
print(y)                    # 20





# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)            # b = {100, 110, 120, 130, 140, 150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)              # c = [10, 20, 15, 18, 10, 50, 20, 12, 18]
print(d)                # d = {10, 20, 15, 18, 50, 12}
e = set('Rama  rAo')
print(e)                # {'R', 'a', 'm', ' ', 'r', 'A', 'o'}       duplicates are removed
print(set(25))          # TypeError: 'int' object is not iterable
print(set())            # set()


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  ---> Converts  sequence  to  set

2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set

3) How  many  arguments  can  set()  function  take ?  ---> Zero  (or) One  but  not  more  than  one

4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
'''