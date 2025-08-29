# '''
# (Home  work)
# Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

# Let  input  be  RamA    raO
# What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

# Hint:  Same  as  prog23a  with  minor changes

# Enter String:RamA raO
# {'A': 3, 'O': 1}
# '''
# string = input('Enter String:  ')
# sorted_string = sorted(string.upper())
# ans = {}
# for c in sorted_string:
# 	if c in 'AEIOU':
# 		ans[c] = ans.get(c, 0) + 1
# print(ans)
		


# # Find outputs (Home  work)
# a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
# b = {'Y' : 'Yellow', 'G' : 'Gray'}
# b . update(a)
# print(b)        #{'Y' : 'Yellow', 'G' : 'Green', 'R' : 'Red', 'B' : 'Blue'}
# #a . update(b)   #errir, list do not have update method


# #  Find  outputs  (Home  work)
# a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
# b = {}
# #b.update(a)                    #error, each innersequence length should be exactly 2
# print(b)                       #{}
# c = [(10,) , (20,) , (30,)]    
# #b . update(c)                  #error, each innersequence length should be exactly 2
# print(b)                       #{}


# #  Find  outputs (Home  work)
# d = {x : x ** 3   for    x   in  range(5)}
# print(d)            #{0 : 0, 1 : 1, 2 : 8, 3 : 27, 4 : 64}
# print(type(d))      #<class 'dict'>


# # Find outputs   (Home  work)
# d = { x :  2 * x    for    x   in   range(5)}
# print(d)             #{0 : 0, 1 : 2, 2 : 4, 3 : 6, 4 : 8}



# # Find outputs  (Home  work)
# a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
# b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
# print(b)                                                          #{15 : 'Sita', 17 : 'Kiran'}
# c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
# print(c)                                                          #{10 : 'Rama', 17 : 'Rajesh', 12 : 'Rama Rao'}


# # Find outputs  (Home  work)
# def   f1():
# 	print('Hyd')
# 	print('Sec')
# 	print('Cyb')
# # End  of  the  function
# print('Begin')       #Begin
# x = f1()             #prints 3 statements of f1() and returns None
# print(x)             #None
# print(type(x))       #<class 'NoneType'>
# print('End')         #End



# # Find  outputs  (Home  work)
# def  f1():
# 	return  10 , 20 , 30
# # End  of  the  function
# x = f1()             #calls f1() and stores tuple (10, 20, 30)
# print(x)             #(10, 20, 30)
# print(type(x))       #<class 'tuple'>
# a , b , c =  f1()    #f1() called and tuple is unpacked to a, b ,c
# print(a)             #10
# print(b)             #20
# print(c)             #30
# print('for  loop')   #for loop
# for  k   in   f1():  #for k in 10,20,30
# 	print(k)         #10 <nl> 20 <nl> 30 <nl>


# # Find  outputs
# def    f1():
#         return  10
#         return  20
#         return  30
# # End  of  the  function
# print('Begin')    #Begin
# x = f1()          #f1 called and replaced by 10
# print(x)          #10
# print('End')      #'End'
# #return   100      #error return must only be in function



# #  Find  outputs
# #f1()                     #function can't be called before definition
# def   f1():
#         print('Hello')
# print(f1())              #prints 'Hello' and then 'None'
# print(f1)                #type, name and address of f1


# # Find  outputs  (Home  work)
# print('Hello')                    #Hello
# def  f1():
#         print('f1  function')
# #End  of   function
# print('Hi')                      #Hi
# print(f1())                      #f1 function <nl> None
# print(f1)                        #<function f1 at 0xlocation>
# print('Bye')                     #Bye



# #  Find  outputs
# def    f1():
#         print('Hyd')
#         print('Sec')
#         print('Cyb')
# #End  of  the  function
# print('Begin')     #Begin
# print(type(f1))    #<class 'function'>
# print(id(f1))      #address 
# print('End')       #End


# #  Find  outputs (Home  work)
# def   add(a , b):
#         return  a + b
# #End  of  the  function
# print(add(10 , 20))                                              #30
# print(add('Hyder' , 'abad'))                                     #Hyderabad
# print(add(10.8 , 20.6))                                          #31.4000.....2
# print(add(True , False))                                         #1
# print(add(3 + 4j , 5 + 6j))                                      #(8+10j)
# print(add(25 , 10.8))                                            #35.8
# print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))   #[25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']
# #print(add(10 , '20'))                                            #Error, str and int can't be added
          


# # Find  outputs (Home  work)
# def  f1():
# 	print('No-argument  function')
# def  f1(x):
# 	print('Single  argument  function  : ' , x)
# def  f1(x , y):
# 	print('Two  argument  function : ' , x , y)
# def  f1(x , y , z):
# 	print('Three  argument  function : ' , x , y , z)
# f1(10 , 20 , 30)   #Three argument function: <sp> 10 <sp> 20 <sp> 30
# #f1(40 , 50)        #Error, missing positional argument z
# #f1(60)             #Error, missing positional arguments y and z
# #f1()               #Error, missing positional arguments x, y , z


# '''
# Write   a  function  to  test  a  number  is  prime  (or)  not.
# 1) What  is  a  prime  number ?  ---> A  number  without  divisors  except  1  and  itself

# 2) Let  input  be  25
#     What  is  the  range  of  divisors ? ---> i =   2 , 3 , 4 , 5 , 6 , .....  12

# 3) Let  input   be  11
#     What  is   the  range  of  divisors ? ---> i =  2 , 3 , 4 , 5

# 4) What  action  to  be  made  if  'i'  is  not  a  divisor  of  input  number ?  ---> Move  to  the  next  element  of  range  object

# 5) What  action  to  be  made  if  'i'  is  a  divisor  of  input  number ?  --->  return   False

# 6) What  action  to  be  made  if  there  are  no  divisiors  to  input  number  ? ---> return  True  outside  the  loop
# '''
# '''
# 1) prime(25)  --->
#     How  many  times  is  for  loop  executed ?  --->

# 2) prime(11) --->
#     How  many  times  is  for  loop  executed ?  --->

# 3) prime(2) --->
#     How  many  times  is  for  loop  executed ?  --->

# 4) prime(49) --->
#     How  many  times  is  for  loop  executed ?  --->
# '''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
# n = int(input('Enter a number:  '))
# if is_prime(n):
#     print('Prime Number')
# else:
#     print('Composite Number')


# # Find  outputs  (Home  work)
# def   disp(empno , ename , sal):
#         print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# # End  of  the  function
# disp(25 , 'Rama  Rao' , 10000.0)  #Emp Number : 25 <t> Emp Name : Rama Rao <t> Salary : 10000.0
# disp('Sita' , 20000.0 , 35)       #Emp Number : Sita <t> Emp Name : 20000.0 <t> Salary : 35
