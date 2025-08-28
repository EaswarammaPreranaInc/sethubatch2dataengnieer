'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''

s=input('enter a string:')
s=s.upper()
vowels='AEIOU'
f={}

for a in vowels:
    c=s.count(a)
    if c>0:
        f[a]=c
print(f)

# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b)
a . update(b)#AtributeError

#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a)
print(b)#ValueError
c = [(10,) , (20,) , (30,)]
b . update(c)
print(b)#ValueError

#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d)# {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}

print(type(d))#class dict

# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)#{15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)#{10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}

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
#Begin
#Hyd
#Sec
#Cyb
#None
#<class 'NoneType'>
#End


# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x)#(10,20,30)
print(type(x))#class tuple
a , b , c =  f1()
print(a)#10
print(b)#20
print(c)#30
print('for  loop')#for loop
for  k   in   f1():
	print(k)
#10
#20
#30

# Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin')
x = f1()
print(x)
print('End')
return   100 # SytaxError

#  Find  outputs
f1()
def   f1():
        print('Hello')
print(f1())#Hello
print(f1)#Function f1

# Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')
# Hello
#Hi
#f1 function
#None
#function f1
#Bye


#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')# begin
print(type(f1))#class function
print(id(f1))# address of f`1
print('End')#End

#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))#30
print(add('Hyder' , 'abad'))#Hyderabad
print(add(10.8 , 20.6)#31.4
print(add(True , False))#TypeError
print(add(3 + 4j , 5 + 6j))#8+10j
print(add(25 , 10.8))#35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))#TypeError
print(add(10 , '20'))#TypeError

# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)
f1(40 , 50)
f1(60)
f1()
# Three arguments function: 10 20 30

'''
Write   a  function  to  test  a  number  is  prime  (or)  not.

'''
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

