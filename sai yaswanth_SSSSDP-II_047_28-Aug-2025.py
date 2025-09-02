
'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes

Enter  mixed  case  string :  RamA raO
Distinct  vowels :   OA
'''
Code:
s = input("Enter a string: ")
s = s.upper()
chars = sorted(s)
a = {}
for ch in chars:
    if ch.isalpha() and (ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='u'): # ignore spaces and non-letters
        a[ch] = a.get(ch, 0) + 1
print(a)

# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b) #{'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
a . update(b) #error:list has no update method

#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a) #error:list of tuple has 3 values but dict can take only 2 values
print(b) #{}
c = [(10,) , (20,) , (30,)]
b . update(c)
print(b) #{10: None, 20: None, 30: None}

#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d) #{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d)) #<class 'dict'>

# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d) #{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b) #{15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c) #{10: 'Rama', 18: 'Rajesh' , 12: 'Rama Rao'}

# Find outputs  (Home  work)
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
Output:
Begin
Hyd
Sec
Cyb
None
<class 'NoneType'>
End

# Find  outputs  (Home  work)
def  f1():
    return  10 , 20 , 30
# End  of  the  function
x = f1() #(10,20,30)
print(x) #(10,20,30)
print(type(x)) # <class 'tuple'>
a , b , c =  f1() 
print(a) # 10
print(b) # 20
print(c) # 30
print('for  loop') # for  loop
for  k   in   f1():
    print(k) # 10\n20\n30

# Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin') #Begin
x = f1() #10
print(x) #10
print('End') #End
return   100 #This  line  will  throws error


#  Find  outputs
f1() #error: f1 is not defined
def   f1():
        print('Hello')
print(f1()) #Hello
print(f1) # <function f1 at address in hexadecimal>

# Find  outputs  (Home  work)
print('Hello') #Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi') #Hi
print(f1()) # f1  function None
print(f1) # <function f1 at address in hexadecimal>
print('Bye') #Bye

#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') #Begin
print(type(f1)) #<class 'function'>
print(id(f1)) #address in decimal 
print('End') #End

#  Find  outputs (Home  work)
def  add(a , b):
    return  a + b
#End  of  the  function
print(add(10 , 20)) # 30
print(add('Hyder' , 'abad')) # 'Hyderabad'
print(add(10.8 , 20.6)) # 31.4
print(add(True , False)) # 1
print(add(3 + 4j , 5 + 6j)) # (8+10j)
print(add(25 , 10.8)) # 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec'])) # [25 , 10.8 , 'Hyd' , True , None , 3+4j , 'Sec']
print(add(10 , '20')) #error:int and str cannot be added




# Find  outputs (Home  work)
def  f1():
    print('No-argument  function')
def  f1(x):
    print('Single  argument  function  : ' , x)
def  f1(x , y):
    print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
    print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30) # Three  argument  function :  10 20 30
f1(40 , 50) # error: z is  missing
f1(60) # error: y , z  are  missing
f1() # error: x , y , z  are  missing




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
def   prime(n):
    return  true   when  'n'  is  prime  number  and  False  otherwise
1) prime(25)  --->
    How  many  times  is  for  loop  executed ?  --->
2) prime(11) --->
    How  many  times  is  for  loop  executed ?  --->
3) prime(2) --->
    How  many  times  is  for  loop  executed ?  --->
4) prime(49) --->
    How  many  times  is  for  loop  executed ?  --->
How  to  read  a  number
if   input  is  invalid:
    print('Invalid  input')
elif  input  is  prime  number:
    print('Prime  number')
else:
    print('Composite  number')
'''
Code:
def prime(n):
    if n <= 1:
        return False  

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
try:
    n = int(input("Enter a number: "))
    if n <= 1:
        print("Invalid input")
    elif prime(n):
        print("Prime number")
    else:
        print("Composite number")
except ValueError:
    print("Invalid input (not a number)")


# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0) #Emp  Number  :  25        Emp Name  :  Rama  Rao          Salary  :  10000.0
disp('Sita' , 20000.0 , 35) #Emp  Number  :  Sita      Emp Name  :  20000.0         Salary  :  35

