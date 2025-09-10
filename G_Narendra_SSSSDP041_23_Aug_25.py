# add()  method  demo  program  (Home  work)
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
print(a)            # {True, 10.8, 'Hyd', None, 25}
a . add(10 , 20 , 30)    # TypeError: set.add() takes exactly one argument (3 given)
a . add([10,20,30])      # TypeError: unhashable type: 'list'

# Find outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)            # {True, 10.8, 25, 'Hyd'}
print(id(a))        # <id-1>
a . add(tpl)
a . add('Sec')
print(a)            # {True, 10.8, 25, 'Hyd', (10, 20, 30), 'Sec'}
print(id(a))        # <id-1>
print(len(a))       # 6
a . add([100 , 200 , 300]) # TypeError: unhashable type: 'list'
a . add(set())           # TypeError: unhashable type: 'set'
a . add({ })             # TypeError: unhashable type: 'dict'

# Find outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)            # {(10, 20, 15, 18)}
print(len(s))       # 1

# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))       # 4
print(s)            # {10, 18, 20, 15}
s . update(25)      # TypeError: 'int' object is not iterable

# Find outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)            # {70, 10, 40, 50, 20, 60, 30}
print(len(s))       # 7
s . add(a , b , c)  # TypeError: set.add() takes exactly one argument (3 given)

# Find outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)            # {'R', 'a', 'm', ' ', 'o'}
print(len(a))       # 5
a . update(3 + 4j , 10.8 , True)   # TypeError: 'complex' object is not iterable

# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)            # {10, 18, 20, 15}
b = a . copy()
print(b)            # {10, 18, 20, 15}
print(a  is  b)     # False
print(a  ==  b)     # True
c = a
print(a  is  c)     # True

# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)            # {True, 10.8, 25, 'Hyd'}
print(a . pop())    # True (could be any element, as set is unordered)
print(a . pop())    # 10.8 (actual value depends on internal order)
print(a . pop())    # 25 or 'Hyd'
print(a . pop())    # The last remaining element
print(a . pop())    # KeyError: 'pop from an empty set'
print(a)            # set()
b = {10 , 20 , 30 , 40}
print(b . pop(2))   # TypeError: pop() takes no arguments (1 given)

# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)            # {True, 10.8, 25, 'Hyd'}
a . remove('Hyd')
print(a)            # {True, 10.8, 25}
a . remove('Sec')   # KeyError: 'Sec'

# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)            # {True, 10.8, 25, 'Hyd'}
a . discard('Hyd')
print(a)            # {True, 10.8, 25}
a . discard('Sec')
print(a)            # {True, 10.8, 25}
a . remove('Sec')   # KeyError: 'Sec'

# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)            # {10, 18, 20, 15}
a . clear()
print(a)            # set()
print(len(a))       # 0

# Find outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))   # {40, 10, 50, 20, 60, 30}
print(a | b)          # TypeError: unsupported operand type(s) for |: 'set' and 'list'
print(b . union(a))   # AttributeError: 'list' object has no attribute 'union'
print(a + b)          # TypeError: unsupported operand type(s) for +: 'set' and 'list'
