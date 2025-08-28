Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}
 Program:-
-----------
s = input("Enter a string: ")

s = s.upper()     # convert to uppercase
vowels = ['A','E','I','O','U']
d = {}

for ch in s:
    if ch in vowels:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

print(d)
--------------------------------------------------

# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a) # {'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
print(b)
a . update(b) # error
----------------------------
#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a)
print(b) # error
c = [(10,) , (20,) , (30,)]
b . update(c)
print(b) # error
-----------------------------------------------
# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b) # {15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c) # {10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}
---------------------------------------
# Find outputs  (Home  work)
def   f1():
	print('Hyd') # Hyd
	print('Sec') # Sec
	print('Cyb') # Cyb
# End  of  the  function
print('Begin') # Begin
x = f1()
print(x) # None
print(type(x)) # <class 'Nonetype'>
print('End') # End
----------------------------------
# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x) # (10,20,30)
print(type(x)) # <class "tuple'>
a , b , c =  f1()
print(a) # 10
print(b) # 20
print(c) # 30
print('for  loop') # for loop
for  k   in   f1():
	print(k) #  10
			20
			30
------------------------------------------
 # Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin') # Begin
x = f1()
print(x) # 10
print('End') # End
return   100
----------------------------------
#  Find  outputs
f1() # error
def   f1():
        print('Hello')
print(f1())
print(f1)
-----------------------------
# Find  outputs  (Home  work)
print('Hello') # Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi') # Hi
print(f1()) # f1()
print(f1) # None
print('Bye') # Bye
------------------------------
#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') # Begin
print(type(f1)) #<class 'function'>
print(id(f1)) #Address
print('End') # End
-----------------------------------

