a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)                       # [25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
print(*a)                      # 25 10.8 Hyd True (3+4j) None Hyd 25
print(type(a))                 # <class 'list'>
print(id(a))                   # ( 140240179993728)
print(len(a))                  # 8
a[2] = 'Sec'
print(a)                       # [25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
print(a[2 : 5])                # ['Sec', True, (3+4j)]
a = [ ]
print(a)                       # []
a.append(25)
a.append(10.8)
a.append('Hyd')
a.append(True)
print(a)                       # [25, 10.8, 'Hyd', True]
a.remove('Hyd')
print(a)                       # [25, 10.8, True]
a.remove('25')                 # error 
print(a)
a = [25 , 10.8 , 'Hyd']
print(a)                       # [25, 10.8, 'Hyd']
print(id(a))                   # (some integer ID)
print(a * 3)                   # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2)                   # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1)                   # [25, 10.8, 'Hyd']
print(a * 0)                   # []
print(a * -1)                  # []
print(a * 4.0)                 # error 
a = a * 3
print(a)                       # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(id(a))                   # new id 
a = [25]
print(a * a)                   # error 
a = list('Hyd')
print(a)                     # ['H', 'y', 'd']
print(type(a))               # <class 'list'>
print(len(a))                # 3
b = (10 , 20 , 15 , 18)
print(list(b))               # [10, 20, 15, 18]
print(list(range(5)))        # [0, 1, 2, 3, 4]
print(list(25))              # error
a = []
print(type(a))               # <class 'list'>
print(a)                     # []
print(len(a))                # 0
b = list()
print(b)                     # []
print(len(b))                # 0
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[2 : 7])           # [(3+4j), 'Hyd', True, None, 10.8]
print(list[ : : ])           # [25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[:])               # [25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[ : : -1])         # ['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2])          # [25, (3+4j), True, 10.8]
print(list[1 : : 2])         # [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2])         # ['Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2])       # [10.8, 'Hyd', 10.8]
print(list[1 : 4])           # [10.8, (3+4j), 'Hyd']
print(list[-4 : -1])         # [True, None, 10.8]
print(list[3 : -3])          # ['Hyd', True]
print(list[2 : -5])          # [(3+4j)]
print(list[-1:-5])           # []
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x)            # x :  Hyd
print('y : ' , y)            # y :  True
for  x  in  list[2:7]:
	print(x)                 # (3+4j) \n Hyd \n True \n None \n 10.8


a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))             # [10, 20, 30, 40, 50] 1402584668
a[1 : 4] = [60 , 70]
print(a , id(a))             # [10, 60, 70, 50] same ID
a[2: 4] = [100 , 200 ,  300]
print(a , id(a))             # [10, 60, 100, 200, 300] same ID
[19-07-2025 00:11] Sai Satwik: a =  [25]
print(a[1])                  # error
print(a[1:])                 # []
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))         # <class 'int'>
print(type(b))         # <class 'tuple'>
print(type(c))         # <class 'int'>
print(type(d))         # <class 'tuple'>
print(a * 4)           # 100
print(b * 4)           # (25, 25, 25, 25)
print(c * 4)           # 100
print(d * 4)           # (25, 25, 25, 25)
a = tuple('Hyd')
print(a)               # ('H', 'y', 'd')
print(type(a))         # <class 'tuple'>
print(len(a))          # 3
b = [10 , 20 , 15 , 18]
print(tuple(b))        # (10, 20, 15, 18)
print(tuple(range(5))) # (0, 1, 2, 3, 4)
print(tuple(25))       # error
a = ()
print(type(a))         # <class 'tuple'>
print(a)               # ()
print(len(a))          # 0
b = tuple()
print(b)               # ()
print(len(b))          # 0
a = (10 , 20 , 30)
print(a)               # (10, 20, 30)
print(id(a))           # some ID
a = a * 2
print(a)               # (10, 20, 30, 10, 20, 30)
print(id(a))           # (new ID, different from above)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)               # {None, 10.8, True, 'Hyd', (3+4j)}
print(type(a))         # <class 'set'>
print(len(a))          # 5
print(a[2])            # error
print(a[1 : 4])        # error
a[2] = 'Sec'           # error
print(a * 2)           # error
print(a * a)           # error
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)               # {'Hyd', 0.0, ''}
print(len(a))          # 3
print(type(a))         # <class 'set'>
a = set('Rama rAo')
print(a)                             # {'R', 'r', ' ', 'm', 'o', 'a', 'A'}
print(len(a))                        # 7
print(set([10 , 20 , 15 , 20]))      # {10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3)))       # {10, 13, 16, 19}
print(set(25))                       # error 
print(set([25 , 10.8 , [] , 'Hyd'])) # error
a = [ ]
b = ( )
c = { }
d = set()
print(type(a))                       # <class 'list'>
print(type(b))                       # <class 'tuple'>
print(type(c))                       # <class 'dict'>
print(type(d))                       # <class 'set'>
print(a)                             # []
print(b)                             # ()
print(c)                             # {}
print(d)                             # set()
a = set()
a.add(25)
a.add(10.8)
a.add('Hyd')
a.add(True)
a.add(None)
a.add('Hyd')
a.add(1)                             
print(a)                             # {10.8, 'Hyd', None, 1}
print(len(a))                        # 4
a.remove(25)
print(a)                             # {10.8, 'Hyd', None, 1}
a.append(100)                        # error 
a.add(set())                         # error 
a.add(())                            
a.add([])                            # error 
print(a)                             # error
a.add({})                            # error
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(How  to  print  set)            # error
print('Iterate  thru  set  with  for  loop')
How  to  iterate  thru  set  with  for  loop # error
a = {25, True, 'Hyd', 10.8}

print('set with print function')
print(a)                            # {'Hyd', 25, 10.8}

print('Iterate thru set with for loop')
for i in a:
    print(i)
