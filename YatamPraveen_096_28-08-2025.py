'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)
Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}
Hint:  Same  as  prog23a  with  minor  changes
'''

ip = input('Enter the string : ').upper()
res = {i:ip.count(i) for i in ip if i in 'AEIOU'}
print(res)





# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b)            #{'Y' : 'Yellow', 'G' : 'Green', 'R' : 'Red', 'B' , 'Blue'}
a . update(b)       #This throws error as update is not a method of list





#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a)         #This throws error as the inner elements of a must contain exactly 2 elements for update to work
print(b)            #{}
c = [(10,) , (20,) , (30,)]
b.update(c)         #This throws error as the inner elements of c must contain exactly 2 elements for update to work
print(b)            #{}





#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d)                #{0 : 0, 1 : 1, 2 : 8, 3 : 27, 4 : 64}
print(type(d))          #<class 'dict>





# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d)            #{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}





# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)        #{15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)        #{10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}





# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')          #Begin
x = f1()
print(x)                #Hyd<next line>Sec<next line>Cyb<next line>None
print(type(x))          #<class 'NoneType'>
print('End')            #End





# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x)                #(10, 20, 30)
print(type(x))          #<class 'tuple'>
a , b , c =  f1()
print(a)                #10
print(b)                #20
print(c)                #30
print('for  loop')      #for loop
for  k   in   f1():
	print(k)            #10<next line>20<next line>30





#  Find  outputs
#f1()                    #This causes error as function is called even before definition
def   f1():
        print('Hello')
print(f1())             #Hello<next line>None
print(f1)               #<function f1 at (some address)>





# Find  outputs  (Home  work)
print('Hello')                      #Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi')                         #Hi
print(f1())                         #f1 function<next line>None
print(f1)                           #<function f1 at (some address)>
print('Bye')                        #Bye





#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')          #Begin
print(type(f1))         #<class 'function'>
print(id(f1))           #Address of function f1
print('End')            #End





#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))                 #30
print(add('Hyder' , 'abad'))        #Hyderabad
print(add(10.8 , 20.6))             #31.4
print(add(True , False))            #1
print(add(3 + 4j , 5 + 6j))         #(8+10j)
print(add(25 , 10.8))               #35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))  #[25 , 10.8 , 'Hyd', True , None , 3+4j , 'Sec']
print(add(10 , '20'))               #Throws error as int and str can't be added





# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)    #Three  argument  function : 10 20 30
f1(40 , 50)         #This throws error as according to last function definition, f1 takes 3 arguments.
f1(60)              #Same error as above
f1()                #Same error as above





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
def prime(n):
    if n<=1:
        return False
    else:    
        for i in range(2, n//2+1):
            if n%i == 0:
                return False
        return True
x = int(input('num : ')	)
print(prime(x))