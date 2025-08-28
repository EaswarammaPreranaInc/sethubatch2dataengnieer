'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

'''
'''
s = input("Enter a string: ")
s = s.upper()
vowels = ['A', 'E', 'I', 'O', 'U']
a = {}
for ch in s:
    if ch in vowels:
        a[ch] = a.get(ch, 0) + 1
print(a)
'''

# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]         # converts list to tuple
b = {'Y' : 'Yellow', 'G' : 'Gray'}                             
b . update(a)
print(b)                                                        # {'Y':'Yellow','G':'Green','R':'Red','B':'Blue}
a . update(b)                                                   # error ther is no update method in list

#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]         # converts list to tuple
b = {}                                                          
b.update(a)                                                     # error inner sequence lenght should be 2
print(b)                                                        # {}
c = [(10,) , (20,) , (30,)]                                     
b . update(c)                                                   # error inner sequence lenght should be 2
print(b)                                                        # {}


#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d)                                        # {0:0,1:1,2:8,3:27,4:64}
print(type(d))                                  # <class 'dict'>


# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d)                                        # {0:0,1:1,2:4,3:6,4:8}


# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}                      
print(b)                                                                            # {15:'Sita',17:'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)                                                                            # {10:'Rama',18:'Rajesh',12:'Rama Rao'}

# Find outputs  (Home  work)
def   f1():
	print('Hyd')                # Hyd
	print('Sec')                # Sec
	print('Cyb')                # Cyb
# End  of  the  function
print('Begin')                  # Begin
x = f1()                        # prints 3 statements of f1() and returns None
print(x)                        # None
print(type(x))                  # <class 'Nonetype'>
print('End')                    # End


# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()                        
print(x)                        # (10,20,30)
print(type(x))                  # <class 'tuple'>
a , b , c =  f1()
print(a)                        # 10
print(b)                        # 20
print(c)                        # 30
print('for  loop')              # for loop
for  k   in   f1():
	print(k)                    # 10
                                # 20
								# 30
	
# Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin')                  # Begin
x = f1()                        # function call f1 replaced by 10
print(x)                        # 10
print('End')                    # 'End'
#return   100                    # error return must be in the function


#  Find  outputs
f1()                            # Error
def   f1():                     
        print('Hello')          # Hello
print(f1())                     # print Hello and returns none
print(f1)                      


# Find  outputs  (Home  work)
print('Hello')                      # Hello
def  f1():
        print('f1  function')       
#End  of   function
print('Hi')                         # Hi
print(f1())                         # f1 function and returns none
print(f1)                           
print('Bye')                        # Bye


#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')                      # Begin
print(type(f1))                     # <class 'function'>
print(id(f1))                       # address of the function
print('End')                        # End


#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b                                           
#End  of  the  function
print(add(10 , 20))                                                    # 30
print(add('Hyder' , 'abad'))                                           # Hyderabad
print(add(10.8 , 20.6))                                                # 31.40
print(add(True , False))                                               # 1
print(add(3 + 4j , 5 + 6j))                                            # (8+10j)
print(add(25 , 10.8))                                                  # 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))         # [25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']
print(add(10 , '20'))                                                  # error string and int cannot be added


# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')                      # 10 20 30
def  f1(x):
	print('Single  argument  function  : ' , x)        
def  f1(x , y):
	print('Two  argument  function : ' , x , y)         
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)   
f1(10 , 20 , 30)
f1(40 , 50)              # error positional argument z is missing
f1(60)                   # error positional argument y,z is  missing
f1()                     # error positional argument x,y,z is missing


# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')         
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)                                                                # empno=25,ename='Rama Rao',sal=10000.0
disp('Sita' , 20000.0 , 35)                                                                     # empno='Sita',ename=20000.0,sal=35



'''
Write   a  function  to  test  a  number  is  prime  (or)  not.
1) What  is  a  prime  number ?  ---> A  number  without  divisors  except  1  and  itself

2) Let  input  be  25
    What  is  the  range  of  divisors ? ---> i =   2 , 3 , 4 , 5 , 6 , .....  12

3) Let  input   be  11
    What  is   the  range  of  divisors ? ---> i =  2 , 3 , 4 , 5

4) What  action  to  be  made  if  'i'  is  not  a  divisor  of  input  number ?  ---> Move  to  the  next  element  of  range  object

5) What  action  to  be  made  if  'i'  is  a  divisor  of  input  number ?  --->  return   False

6) What  action  to  be  made  if  there  are  no  divisiors  to  input  number  ? ---> return  True  outside  the  loop
'''

'''
1) prime(25)  --->
    How  many  times  is  for  loop  executed ?  --->

2) prime(11) --->
    How  many  times  is  for  loop  executed ?  --->

3) prime(2) --->
    How  many  times  is  for  loop  executed ?  --->

4) prime(49) --->
    How  many  times  is  for  loop  executed ?  --->
'''

def is_prime(n):
    if n < 2:
        print('Invalid Input')
        return
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print('Composite Number')
            return
    print('Prime Number')
n = int(input('Enter a number:  '))
is_prime(n)