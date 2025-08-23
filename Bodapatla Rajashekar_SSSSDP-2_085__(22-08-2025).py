#index() and count() methods demo program (Home work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
# 0 1 2 3 4 5 6 7 8 9 10
try:
 i = a . index(15)
 while True:
  print('15 is found at index : ' , i)
  i = a . index(15 , i + 1)
except:
  print(F'15 is found {a . count(15)} times')

#o/p
'''
15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15 is found 3 times
'''

#2
# How to modify an element of tuple ? (Home work)
a = 10 , 20 , 30 , 40 , 50
# 0 1 2 3 4
a[2] = 35
print(a)                            #Error
print(id(a))                        #78945612378
How to modify 30 in tuple to 35     #a = a[:2] + (35,) + a[3:]
print(a)                            #(10, 20, 35, 40, 50)
print(id(a))                        #45613789789

#3
# How to delete an element of tuple ? (Home work)
a = 10 , 20 , 30 , 40 , 50
# 0 1 2 3 4
a . remove(30)                      #Error
del a[2]                            #Error
a . pop(2)                          #Error
print(a)                            #Error
print(id(a))                        #79741852963
How to remove 30 from tuple 'a'     #a = a[:2] + a[3:]
print(a)                            #(10 , 20 , 40 , 50)
print(id(a))                        #45678912396

#4
# Nested tuple (Home work)
a = ( (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90) )
print(a)                              #( (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90) )
print(type(a))                        #<class Tuple>
print(len(a))                         #3
print(How to print 1st inner tuple)   #a[0]
print(How to print 2nd inner tuple)   #a[1]
print(How to print 3rd inner tuple)   #a[2]
print(How to print 20)                #a[0][1]
print(How to print 50)                # #a[1][2]
print(How to print 90)                #a[2][-1]

#5
# Find outputs (Home work)
a = ((10 , 20 , 30),)
print(How to print inner tuple)                 #(*a)
print(How to print inner tuple in another way)  #a[0]
print(How to print 10)                          #a[0][0]
print(How to print 20)                          #a[0][1]
print(How to print 30)                          #a[0][2]
b = ((),)
print(How to print inner tuple of tuple 'b')                #(*b)
print(How to print inner tuple of tuple 'b' in another way)  #b[0]

#6
# Find outputs (Home work)
a = ((10 , 20 , 30))
print(a)     #((10,20,30))
print(*a)    #10,20,30
b = (())
print(b)    #()
print(*b)   #

#7 
# What are the outputs if input is {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter Set : ')
print(a)            #{10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a))      #<clss Str >
b = eval(a) 
print(b)            #{18, 20, 10, 12, 15}
print(type(b))      #<clss Set >

#8
# Find outputs (Home work)
print({(10 , 20 , 30)})        #{(10,20,30)}
print({[10 , 20 , 30]})        #Error
print({{10 , 20 , 30}})        #Error
print({{}})                    #Error

#9
# How to print set in differnet ways (Home work)
a = {25 , True , 'Hyd' , 10.8}
print('set with print function')

print(a)

print('Iterate elements of set with for loop')
#How to iterate set with for loop
for i in a:
   print(i)

#10
# Find outputs (Home work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)               #{'Hyd', True, 25}
print(len(s))          #3
print(type(s))         #<class Set >

#11
# Find outputs (Home work)
s = {'Hyd', 25, True, 10.8 }
print(s)
a , b , c , d = s
print(a)         #{25, 10.8, 'Hyd', True}
print(b)         #25
print(c)         #10.8
print(d)         #True

#12
# Find outputs (Home work)
s = {'Hyd', 25, True, 10.8 }
print(s)                #{'Hyd', 25, True, 10.8 }
a , *b = s
print(a)               #True
print(b)               #[ 10.8,'Hyd', 25 ]
print(type(b))         #<class List >

#13
# Find outputs (Home work)
print({(10 , 20 , 30)})    #{(10, 20, 30)}
print({[10 , 20 , 30]})    #Error
print({{10 , 20 , 30}})    #Error
print({{}})                #Error

#14.
# How to print set in differnet ways (Home work)
a = {25 , True , 'Hyd' , 10.8}
print('set with print function')
print(a)
print('Iterate elements of set with for loop')
#How to iterate set with for loop
for i in a:
     print(i)

#15

# set() function demo program (Home work)
a = range(100 , 151 , 10)
b = set(a)
print(b)                                          #{110,130,120,100,140}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)                 
print(d)                                         #{10,20,18,15,50,12}
e = set('Rama rAo')
print(e)                           #{'A','a','r','R','m',' '}
print(set(25))                      #Error
print(set())                        #()


'''