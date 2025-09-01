a = set()
a.add(True)
a.add(25)
a.add(10.8)
a.add(1)
a.add('Hyd')
a.add(25)
a.add(None)
a.add('Hyd')
a.add(1.0)
print(a)  # {None, True, 10.8, 'Hyd', 25} (any order)
a.add(10, 20, 30)  # Error: add() takes exactly one argument
a.add([10,20,30])  # Error: list is unhashable (cannot be added to set)

a = {25, 10.8, 'Hyd', True}
tpl = (10, 20, 30)
print(a)       # {True, 25, 10.8, 'Hyd'} (any order)
print(id(a))   # <some ID>
a.add(tpl)
a.add('Sec')
print(a)       # {True, 25, 10.8, 'Hyd', (10, 20, 30), 'Sec'} (any order)
print(id(a))   # <same ID>
print(len(a))  # 6
a.add([100, 200, 300])  # Error: list is unhashable (cannot be added to set)
a.add(set())             # Error: set is unhashable (cannot be added to set)
a.add({})                # Error: dict is unhashable (cannot be added to set)

s = set()
tpl = (10, 20, 15, 18)
s.add(tpl)
print(s)      # {(10, 20, 15, 18)} (any order)
print(len(s)) # 1

tpl = (10, 20, 15, 18, 10, 20)
s = set()
s.update(tpl)
print(len(s))  # 4
print(s)       # {10, 20, 15, 18} (any order)
s.update(25)   # Error: 'int' object is not iterable

a = [10, 20, 30]
b = {30, 40, 50}
c = (50, 60, 70)
s = set()
s.update(a, b, c)   
print(s)            # {10, 20, 30, 40, 50, 60, 70} (any order)
print(len(s))       # 7
s.add(a, b, c)      # Error: add() accepts only 1 element; you passed 3

a = set()
a.update('Rama Rao')print(a)  # {'o', 'a', 'm', 'R', ' '} (any order) 
print(len(a))  # 5
a.update(3 + 4j, 10.8, True)  # Error: 'complex' object is not iterable

a = {10 , 20 , 15 , 18}
print(a)  # {18, 10, 20, 15} (any order)
b = a.copy()
print(b)  # {18, 10, 20, 15} (any order)
print(a is b)  # False
print(a == b)  # True
c = a
print(a is c)  # True

a = {25,10.8,'Hyd',True}
print(a)  # {'Hyd', 25, 10.8, True} (any order)
print(a.pop())  # e.g., 'Hyd' 
print(a.pop())  # e.g., 25 
print(a.pop())  # e.g., 10.8 
print(a.pop())  # e.g., True 
print(a.pop())  # Error: empty set, nothing to pop
print(a)  # Not executed due to previous error
b = {10,20,30,40}
print(b.pop(2))  # Error: set.pop() takes no arguments

a = {25 , 10.8 , 'Hyd' , True}
print(a)  # {25, 10.8, 'Hyd', True}  (order may vary)
a.remove('Hyd')
print(a)  # {25, 10.8, True}  (order may vary)
a.remove('Sec')  # Error: Invalid argument.

a = {25 , 10.8 , 'Hyd' , True}
print(a)                     # {25, 10.8, 'Hyd',True}  (order may vary)
a . discard('Hyd')
print(a)                     # {25, 10.8, True} (order may vary)
a . discard('Sec')
print(a)                     # {25, 10.8, True} (order may vary)
a . remove('Sec')            # Error: 'Sec' not found in set

a = {10 , 20 , 15 , 18}
print(a)        # {10, 18, 20, 15} (order may vary)
a.clear()
print(a)        # set()
print(len(a))   # 0

a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a.union(b))   # {40, 10, 50, 20, 60, 30} (order may vary)
print(a | b)        # Error: unsupported operand type(s) for |: 'set' and 'list'
print(b.union(a))   # Error: 'list' object has no attribute 'union'
print(a + b)        # Error: unsupported operand type(s) for +: 'set' and 'list'
