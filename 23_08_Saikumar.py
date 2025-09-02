# add() method demo program (Home work)

a = set()
a.add(True)        # {True}
a.add(25)          # {True, 25}
a.add(10.8)        # {True, 25, 10.8}
a.add(1)           # No effect (1 == True), set still {True, 25, 10.8}
a.add('Hyd')       # {True, 25, 10.8, 'Hyd'}
a.add(25)          # Duplicate ignored, no change
a.add(None)        # {True, 25, 10.8, 'Hyd', None}
a.add('Hyd')       # Duplicate ignored, no change
a.add(1.0)         # No effect (1.0 == 1 == True), no change
print(a)           # Output: {True, 25, 10.8, 'Hyd', None}
a.add(10, 20, 30)  # ERROR set.add() takes exactly one argument (3 given)
a.add([10,20,30])  # ERROR due type 'list'
a.update([10,20,30])   # {True, 25, 10.8, 'Hyd', None, 10, 20, 30}
print(a)               # Output: {True, 25, 10.8, 'Hyd', None, 10, 20, 30}


# Find outputs (Home work)

a = {25, 10.8, 'Hyd', True}
tpl = (10, 20, 30)
print(a)              # {True, 25, 10.8, 'Hyd'}
print(id(a))          # Some unique id (changes every run)
a.add(tpl)            # Adds tuple
a.add('Sec')          # Adds string
print(a)              # {True, 25, 10.8, 'Hyd', (10, 20, 30), 'Sec'}
print(id(a))          # Same id (set modified, not recreated)
print(len(a))         # 6
a.add([100, 200, 300])  # ERROR unhashable type: 'list'
a.add(set())            # ERROR unhashable type: 'set'
a.add({})               # ERROR unhashable type: 'dict'


# Find outputs (Home work)

s = set()
tpl = (10, 20, 15, 18)
s.add(tpl)
print(s)               # {(10, 20, 15, 18)}
print(len(s))          # 1


# update() method demo program (Home work)

tpl = (10, 20, 15, 18, 10, 20)
s = set()
s.update(tpl)
print(len(s))          # 4
print(s)               # {10, 20, 15, 18}
s.update(25)           # ERROR due to 'int' object


# Find outputs (Home work)

a = [10, 20, 30]
b = {30, 40, 50}
c = (50, 60, 70)
s = set()
s.update(a, b, c)
print(s)               # {10, 20, 30, 40, 50, 60, 70}
print(len(s))          # 7
s.add(a, b, c)         # ERROR set.add() takes exactly one argument


# Find outputs (Home work)

a = set()
a.update('Rama Rao')
print(a)               # {'R', 'a', 'm', ' ', 'o'}  
print(len(a))          # 5
a.update(3 + 4j, 10.8, True)  # ERROR due to 'complex' object 


# copy() method demo program (Home work)

a = {10, 20, 15, 18}
print(a)               # {10, 20, 15, 18}
b = a.copy()
print(b)               # {10, 20, 15, 18}
print(a is b)          # False
print(a == b)          # True
c = a
print(a is c)          # True


# pop() method demo program (Home work)

a = {25, 10.8, 'Hyd', True}
print(a)               # {True, 25, 10.8, 'Hyd'} (
print(a.pop())         # Removes & prints random element
print(a.pop())         # Removes another element
print(a.pop())         # Removes another element
print(a.pop())         # Removes last element
print(a.pop())         # ERROR set is empty
print(a)               # set()
b = {10, 20, 30, 40}
print(b.pop(2))        # ERROR pop() takes no arguments


# remove() method demo program (Home work)

a = {25, 10.8, 'Hyd', True}
print(a)               # {True, 25, 10.8, 'Hyd'}
a.remove('Hyd')
print(a)               # {True, 25, 10.8}
a.remove('Sec')        # ERROR 'Sec'


# discard() method demo program (Home work)

a = {25, 10.8, 'Hyd', True}
print(a)               # {True, 25, 10.8, 'Hyd'}
a.discard('Hyd')
print(a)               # {True, 25, 10.8}
a.discard('Sec')       # No error, nothing happens
print(a)               # {True, 25, 10.8}
a.remove('Sec')        # ERROR due to 'Sec'


# clear() method demo program (Home work)

a = {10, 20, 15, 18}
print(a)               # {10, 20, 15, 18}
a.clear()
print(a)               # set()
print(len(a))          # 0


# Find outputs (Home work)

a = {10, 20, 30, 40}
b = [30, 40, 50, 60]
print(a.union(b))      # {10, 20, 30, 40, 50, 60}
print(a | b)           # ERROR:  | is not perform union operations on 'set' and 'list'
print(b.union(a))      # ERROR: 'list' object has no attribute 'union'
print(a + b)           # ERROR:  + is not perform union operations on 'set' and 'list'

