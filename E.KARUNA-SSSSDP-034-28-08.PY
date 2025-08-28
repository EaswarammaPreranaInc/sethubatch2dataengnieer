
'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}
Hint:  Same  as  prog23a  with  minor  changes
'''
a=input("Enter mixed case string : ").upper()
b=sorted(a)
vowels='AEIOU'
c={}
for i in b:
    if i in vowels:
        c[i]=c.get(i,0)+1
print(c)


# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)#{'Y' : 'Yellow', 'G' : 'Green','R':'red' ,'B':'blue'}
print(b)
#a . update(b) #error because list has no update method




#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
#b.update(a)#error because length 3,but required 2
print(b)#{}
c = [(10,) , (20,) , (30,)]
#b . update(c)#error
print(b)#{}




#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d)#{0:0,1:1,2:8,3:27,4:64}
print(type(d))#<class 'dict'>



# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)#{15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)#{10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}

# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d)#{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}



# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')
x = f1()
print(x)#Begin<next line>Hyd<nextline>sec<nextline>cyb<nextline>None
print(type(x))#<class 'Nonetype'>
print('End')#End

# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x)#(10,20,30)
print(type(x))#<class 'tuple'>
a , b , c =  f1()
print(a)#10
print(b)#20
print(c)#30
print('for  loop')
for  k   in   f1():
	print(k)#10<nextline>20<nextline>30
	


	         
# Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin')#Begin
x = f1()
print(x)#10
print('End')#end
#return  100#error:return statement must be inside function



#  Find  outputs
f1()#'f1' is not defined
def   f1():
        print('Hello')#Hello
print(f1())#None
print(f1)#<type and address>



# Find  outputs  (Home  work)
print('Hello')#Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi')#hi
print(f1())#None
print(f1)#<type address>
print('Bye')#Bye


#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')#Begin
print(type(f1))#<class 'function'>
print(id(f1))#address of f1 function
print('End')#end


#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))#30
print(add('Hyder' , 'abad'))#hyderabad
print(add(10.8 , 20.6))#31.400000
print(add(True , False))#1
print(add(3 + 4j , 5 + 6j))#8+10j
print(add(25 , 10.8))#35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))#[25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']
print(add(10 , '20'))#error

# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')#
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)#Three  argument  function:10 20 30
f1(40 , 50)#error :missing one required postional agrument
f1(60)#error :missing two required postional agrument
f1()#error :missing three required postional agrument



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
    if n<=1:
           return False
    for i in range(2,n): 
           if n%i==0:
                  return False
           return True
    print("25 is prime:",prime(25))#False
    print("11 is prime:",prime(11))#True
    print("2 is prime:",prime(2))#True
    print("49 is prime:",prime(49))#False
    num=int(input("enter a number:"))
    if prime(num):
           print("prime number")
    else:
           print("not a prime")       




