# add() method demo
a = set()
a.add(True)
a.add(25)
a.add(10.8)
a.add(1)        # True and 1 are considered equal (same hash), so no duplicate
a.add('Hyd')
a.add(25)       # duplicate ignored
a.add(None)
a.add('Hyd')    # duplicate ignored
a.add(1.0)      # same as 1 → ignored
print(a)        # {True, None, 25, 10.8, 'Hyd'}

#a.add(10 , 20 , 30)   # ERROR add() takes exactly one argument
#a.add([10,20,30])     # ERROR unhashable type: 'list'


# Program: add() with tuple
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)              # {True, 10.8, 25, 'Hyd'}
print(id(a))
a.add(tpl)
a.add('Sec')
print(a)              # {True, 10.8, (10,20,30), 25, 'Hyd', 'Sec'}
print(id(a))          # same id (set modified in place)
print(len(a))         # 6
#a.add([100,200,300])  # ERROR unhashable type: 'list'
#a.add(set())          # ERROR unhashable type: 'set'
#a.add({})             # ERROR unhashable type: 'dict'


# Program: add() with tuple inside set
s = set()
tpl = (10 , 20 , 15 , 18)
s.add(tpl)
print(s)              # {(10, 20, 15, 18)}
print(len(s))         # 1


# update() method demo
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s.update(tpl)
print(len(s))         # 3
print(s)              # {10, 20, 15, 18}
#s.update(25)          # ERROR 'int' object is not iterable


# update() with multiple arguments
a = [10 , 20 , 30]
b = {30 , 40, 50}
c = (50 , 60 , 70)
s = set()
s.update(a , b , c)
print(s)              # {10, 20, 30, 40, 50, 60, 70}
print(len(s))         # 7
#s.add(a , b , c)      # ERROR add() takes 1 argument, got 3


# update() with string
a = set()
a.update('Rama Rao')
print(a)              # {' ', 'R', 'm', 'a', 'o'}
print(len(a))         # 5
#a.update(3+4j , 10.8 , True)  # ERROR complex is not iterable


# copy() method demo
a = {10 , 20 , 15 , 18}
print(a)              # {10, 20, 15, 18}
b = a.copy()
print(b)              # {10, 20, 15, 18}
print(a is b)         # False
print(a == b)         # True
c = a
print(a is c)         # True


# pop() method demo
a = {25 , 10.8 , 'Hyd' , True}
print(a)              # {True, 10.8, 25, 'Hyd'}
print(a.pop())        # random element removed
print(a.pop())        # another element removed
print(a.pop())        # another element removed
print(a.pop())        # last element removed
#print(a.pop())        # ERROR KeyError (empty set)
print(a)              # set()
b = {10 , 20 , 30 , 40}
#print(b.pop(2))       #  ERROR pop() takes no arguments


# remove() method demo
a = {25 , 10.8 , 'Hyd' , True}
print(a)              # {True, 10.8, 25, 'Hyd'}
a.remove('Hyd')
print(a)              # {True, 10.8, 25}
#a.remove('Sec')       # ERROR  KeyError: 'Sec'


# discard() method demo
a = {25 , 10.8 , 'Hyd' , True}
print(a)              # {True, 10.8, 25, 'Hyd'}
a.discard('Hyd')
print(a)              # {True, 10.8, 25}
a.discard('Sec')
print(a)              # {True, 10.8, 25} (no error)
#a.remove('Sec')       # ERROR  KeyError: 'Sec'


# clear() method demo
a = {10 , 20 , 15 , 18}
print(a)              # {10, 20, 15, 18}
a.clear()
print(a)              # set()
print(len(a))         # 0


# union() demo
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a.union(b))     # {10, 20, 30, 40, 50, 60}
#print(a | b)          #  ERROR  unsupported operand types: 'set' | 'list'
#print(b.union(a))     #  ERROR  'list' object has no attribute 'union'
#print(a + b)          #  ERROR  unsupported operand: set + list
