#first program
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)
print(*a)
print(type(a))
print(id(a))
print(len(a))
a[2] = 'Sec'
print(a)
print(a[2 : 5])

#second program
# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a)
a . append(25)
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a)
a . remove('Hyd')
print(a)
a . remove('25')
print(a)

#third program
a = [25 , 10.8 , 'Hyd']
print(a)
print(id(a))
print(a * 3)
print(a * 2)
print(a * 1)
print(a * 0)
print(a * -1)
print(a * 4.0)
a = a * 3
print(a)
print(id(a))
a = [25]
#print(a * a)

#fourth program
# list()  function  demo  program
a = list('Hyd')
print(a)
print(type(a))
print(len(a))
b = (10 , 20 , 15 , 18)
print(list(b))
print(list(range(5)))
#print(list(25))

# fifth program
a = [ ]
print(type(a))
print(a)
print(len(a))
b = list()
print(b)
print(len(b))

#sixth program
# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7])
print(list[ : : ])
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])
print(list[ : : 2])
print(list[1 : : 2])
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2])
print(list[1 : 4])
print(list[-4 : -1])
print(list[3 : -3])
print(list[2 : -5])
#print(list[-1:-5])

# seventh program
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x)
print('y : ' , y)
for  x  in  list[2:7]:
	print(x)
	
# eighth program
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))
a[1 : 4] = [60 , 70]
print(a , id(a))
a[2: 4] = [100 , 200 ,  300]
print(a , id(a))

# ninth program
a =  [25]
print(a[1])
print(a[1:])

# tenth program
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(a * 4)
print(b * 4)
print(c * 4)
print(d * 4)

# eleventh program
# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a)
print(type(a))
print(len(a))
b = [10 , 20 , 15 , 18]
print(tuple(b))
print(tuple(range(5)))
#print(tuple(25))

# twelfth program
a = ()
print(type(a))
print(a)
print(len(a))
b = tuple()
print(b)
print(len(b))

# thirteenth program
a = (10 , 20 , 30)
print(a)
print(id(a))
a = a * 2
print(a)
print(id(a))

#fourteenth program
#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)
print(type(a))
print(len(a))
#print(a[2])
#print(a[1 : 4])
#a[2] = 'Sec'
#print(a * 2)
#print(a * a)

# fifteenth program
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)
print(len(a))
print(type(a))

# sixteenth program
#  set()  function demo  program
a = set('Rama rAo')
print(a)
print(len(a))
print(set([10 , 20 , 15 , 20]))
print(set((25 , 10.8 , 'Hyd' , 10.8)))
print(set(range(10 , 20 , 3)))
#print(set(25))
#print(set([25 , 10.8 , [] , 'Hyd']))

# seventeenth program
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(a)
print(b)
print(c)
print(d)

#eighteenth program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a)
print(len(a))
a . remove(25)
print(a)
#a . append(100)
#a . add(set())
a . add(())
#a . add([])
print(a)
#a . add({})

#nineteenth program
# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print(a)
print(*a)
print('Iterate  thru  set  with  for  loop')
for x in a:
    print(x)





