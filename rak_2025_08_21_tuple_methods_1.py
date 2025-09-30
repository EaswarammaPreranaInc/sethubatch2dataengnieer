# Find outputs (Home work)
a = 25, 10.8, 3 + 4j, 'Hyd', True, None, 'Hyd', 25
print(a)               #(25, 10.8, 3 + 4j, 'Hyd', True, None, 'Hyd', 25)
print(type(a))         #<class 'tuple'>
#a[3] = 'Sec'           #TypeError, tuple can't be modified
#a[3:6] = 60, 70, 80    #error, tuple can't be modified


# Find outputs
a = (1,2,3) 
b = (4,5,6)
print(a, id(a))    #(1,2,3) <space> some id
a += b             #tuple's can be concatanated but new tuple is created 
print(a, id(a))    #(1, 2, 3, 4, 5, 6) <space> new id


# Find outputs
a = (1,2,3) 
b = (4,5,6)
print(a, id(a))    #(1, 2, 3) <space> some id
a = a + b          #new tuple is created with elements from a and b 
print(a, id(a))    #(1, 2, 3, 4, 5, 6) <space> new id


# What are the outputs if input is (10, 20, 30, 40)? (Home work)
a = input('Enter Tuple : ')
print(a)          #(10,20,30,40)
print(type(a))    #<class 'str'>
b = eval(a)       
print(b)          #(10,20,30,40)
print(type(b))    #<class 'tuple'>
print(len(b))     #4


# Find outputs (Home work)
a = (10, [20, 30, 40], 50, 60)
a[1][0] = 70            #20 in list is replaced by 70
print(a)                #(10, [70, 30, 40], 50, 60)
#a[1] = [80, 90, 100]    #TypeError, tuple can't be modified
print(a)                #(10, [70, 30, 40], 50, 60)


# Find outputs (Home work)
a = [10, (20, 30, 40), 50, 60]
#a[1][0] = 70        #TypeError, tuple cannot be modified
print(a)            #[10, (20, 30, 40), 50, 60]
a[1] = [80, 90]     #tuple replaced by a list
print(a)            #[10, [80, 90], 50, 60]


# Find outputs (Home work)
a = 25 
b = 10.8
c = 'Hyd'
d = True
x = a, b, c, d       #tuple created with 4 elements
print(x)             #(25, 10.8, 'Hyd', True)
print(type(x))       #<class 'tuple'>


# Find outputs (Home work)
x = 25, 10.8, 'Hyd', True    #tuple created with 4 elements
a, b, c, d = x               #tuple unpacked into 4 ref's
print(a)                     #25
print(b)                     #10.8
print(c)                     #Hyd
print(d)                     #True
#p, q, r = x                  #ValueError, tuple has 4 elements but only 3 on left side
#a, b, c, d, e = x            #ValueError, tuple has 4 elements but 5 on left side


# Find outputs (Home work)
x = 25, 10.8, 'Hyd', True
a, *b, c = x   #a = 25, c = True, b = [10.8, 'Hyd']
print(a)       #25
print(b)       #[10.8, 'Hyd']
print(c)       #True


# Find outputs (Home work)
tpl = 25, 10.8, 'Hyd', True
a, b, *c, d, e = tpl    #a = 25, b = 10.8, d = 'Hyd', e = True, c =[]
print(a)                #25
print(b)                #10.8
print(c)                #[]
print(d)                #Hyd
print(e)                #True


# Find outputs (Home work)
x = 25, 10.8, 'Hyd', True, 3 + 4j
a, b, _, d, _ = x    #a = 25, b = 10.8, _ = (3+4j), d = True
print(a)             #25
print(b)             #10.8
print(_)             #(3+4j)
print(d)             #True
print(_)             #(3+4j)


# tuple() function demo program (Home work)
a = range(100, 150, 10)
b = tuple(a)                
print(b)                   #(100, 110, 120, 130, 140)
print(type(b))             #<class 'tuple'>
c = [10, 20, 15, 18]
d = tuple(c)               
print(d)                   #(10, 20, 15, 18)
e = tuple('Vamsi')
print(e)                   #('V', 'a', 'm', 's', 'i')
#print(tuple(25))           #ValueError, argument must only be a sequence
print(tuple())             #Empty Tuple

