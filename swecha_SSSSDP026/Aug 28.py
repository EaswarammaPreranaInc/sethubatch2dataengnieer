'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes

# Enter String:RamA raO
# {'A': 3, 'O': 1}

s = "RamA  raO"
s = s.upper()
Vowels = "AEIOU"
freq = {}
for ch in s:
   if ch in Vowels:
    freq[ch] = freq.get(ch , 0) + 1
result = {v : freq[v] for v in Vowels if v in freq}
print(result)

output: {'A' : 3, 'O' : 1}


Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b)#{'Y' : 'Yellow' , 'R' : 'Red' , 'G' : 'Green', 'B' : 'Blue}
a . update(b)#error

 Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
# b.update(a)
print(b)#error
c = [(10,) , (20,) , (30,)]
b . update(c)
print(b)#error

 Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d)# {0 : 0 , 1 : 1 , 2 : 8 , 3 : 27 , 4 : 64}
print(type(d))#<class 'dict'>

Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d)# {0 : 0 , 1 : 2 , 2 : 4 , 3 : 6 , 4 : 8}

Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)# {15 : sita , 17 : kiran}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)# {10 : 'Rama' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}

Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')
x = f1()
print(x)
print(type(x))
print('End')

output : Begin
         Hyd
         Sec
         Cyb
         None
         <class 'Nonetype'>
         End

Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x)
print(type(x))
a , b , c =  f1()
print(a)
print(b)
print(c)
print('for  loop')
for  k   in   f1():
	print(k)
 outputs: (10 , 20 , 30)
          <class 'tuple'>
           10
           20
           30
           for loop
            10
            20
            30

Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin')
x = f1()
print(x)
print('End')
return   100
 output: Begin
          10
           20
           30
           End
             error
 Find  outputs
f1()
def   f1():
        print('Hello')
print(f1())
print(f1)
output : Hello
         None
         address of f1

Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')
output : Hello
         Hi
         f1 function
         None
         address of f1
          Bye

 Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')
print(type(f1))
print(id(f1))
print('End')
output: Begin
          <class 'function'>
            address of f1
            End
         

 Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))# 30
print(add('Hyder' , 'abad'))# Hyderabad
print(add(10.8 , 20.6))#31.4
print(add(True , False))#1
print(add(3 + 4j , 5 + 6j))#8 + 10j
print(add(25 , 10.8))# 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))#[25 , 10.8 , 'Hyd' , True , None , 3 + 4j , 'Sec']
print(add(10 , '20'))#error

Find  outputs (Home  work)
def  f1():
	print('No-argument  function')# error
def  f1(x):
	print('Single  argument  function  : ' , x)#error
def  f1(x , y):
	print('Two  argument  function : ' , x , y)#error
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)#10 , 20 , 30
f1(10 , 20 , 30)
f1(40 , 50)
f1(60)
f1()
                 
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
def   prime(n):
	return  true   when  'n'  is  prime  number  and  False  otherwise
'''
1) prime(25)  --->
    How  many  times  is  for  loop  executed ?  --->

2) prime(11) --->
    How  many  times  is  for  loop  executed ?  --->

3) prime(2) --->
    How  many  times  is  for  loop  executed ?  --->

4) prime(49) --->
    How  many  times  is  for  loop  executed ?  --->

def prime(n):
        if n <= 1:
          return False
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
               return False
          return True
try:     
     n = int(input("enter a number:"))  
     if prime(n):
        print("prime number")   
     else:
         print("composite number")  
except ValueError:
       print("invalid input")


Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)
disp('Sita' , 20000.0 , 35)

output : Emp number : 25  Emp name : Rama Rao  Salary : 10000.0
         Emp name  : Sita  Emp name : 20000.0   Salary : 35