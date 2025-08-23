1.# add()  method  demo  program  (Home  work)
a = set()
a . add(True)
a . add(25)
a . add(10.8)
a . add(1)
a . add('Hyd')
a . add(25)
a . add(None)
a . add('Hyd')
a . add(1.0)
print(a)                                              # {None, True, 10.8, 'Hyd', 25}
#a . add(10 , 20 , 30)                                # set.add() takes exactly one argument (3 given)
#a . add([10,20,30])                                  # unhashable type: 'list'


2.# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)                                              # {25, 10.8, 'Hyd', True}
print(id(a))                                          # 136381240283808
a . add(tpl)
a . add('Sec')
print(a)                                              # {True, 10.8, (10, 20, 30), 'Sec', 25, 'Hyd'}
print(id(a))                                          # 136381240283808
print(len(a))                                         # 6
a . add([100 , 200 , 300])                           # unhashable type: 'list'
a . add(set())                                       # unhashable type: 'set'
a . add({ })                                          # unhashable type: 'dict'    


3.# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)                                            # {(10, 20, 15, 18)}
print(len(s))                                       # 1



4.# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))                                      # 4
print(s)                                           # {10, 18, 20, 15}
s . update(25)                                    # : 'int' object is not iterable


5.# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)                                         # {50, 20, 70, 40, 10, 60, 30}
print(len(s))                                    # 7
#s . add(a , b , c)                              # set.add() takes exactly one argument (3 given)   


6.# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)                                             # {'o', 'm', ' ', 'R', 'a'}
print(len(a))                                        # 5
a . update(3 + 4j , 10.8 , True)                    # 'complex' object is not iterable        


7.# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)                                        # {10, 18, 20, 15}
b = a . copy()
print(b)                                        # {10, 18, 20, 15}
print(a  is  b)                                 # False
print(a  ==  b)                                 # True
c = a
print(a  is  c)                                 # True


8.# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)                                     # {'Hyd', 25, 10.8, True}
print(a . pop())                             # Hyd
print(a . pop())                             # 25
print(a . pop())                             # 10.8
print(a . pop())                             # True
print(a . pop())                            # 'pop from an empty set'
print(a)
b = {10 , 20 , 30 , 40}                      # set()
print(b . pop(2))                           # set.pop() takes no arguments (1 given)


9.# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)                                     # {25, 10.8, 'Hyd', True}

a . remove('Hyd')
print(a)                                     # {25, 10.8, True}
#a . remove('Sec')                           # sec


10.# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)                                    # {25, 10.8, 'Hyd', True}
a . discard('Hyd')
print(a)                                    #  {25, 10.8, True}
a . discard('Sec')
print(a)                                    # {25, 10.8, True}
#a . remove('Sec')                          # Error sec


11.# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)
a . clear()                                         # {10, 18, 20, 15}
print(a)                                            # set()
print(len(a))                                       # 0


12.# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))                              # {40, 10, 50, 20, 60, 30}
print(a | b)                                    # unsupported operand type(s) for |: 'set' and 'list'
print(b . union(a))                             # : 'list' object has no attribute 'union'
print(a + b)                                    # unsupported operand type(s) for +: 'set' and 'list'                        