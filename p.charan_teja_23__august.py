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
print(a)
a.add(10, 20, 30)
a.add([10, 20, 30])



# --------- add() method demo ---------

a = set()                     # Create empty set
a.add(True)                   # Adds True (which counts as 1 in sets)
a.add(25)                     # Adds 25
a.add(10.8)                   # Adds 10.8
a.add(1)                      # Tries to add 1, but 1 is same as True, no effect as set is unique
a.add('Hyd')                  # Adds string 'Hyd'
a.add(25)                     # Already present, no effect
a.add(None)                   # Adds None
a.add('Hyd')                  # Already present, no effect
a.add(1.0)                    # 1.0 is same as 1 and True; no new addition
print(a)                      # Prints set. Output is unordered. Each value shows once.

a.add(10, 20, 30)             # ERROR: set.add() takes exactly one argument (3 given)
a.add([10, 20, 30])           # ERROR: list is unhashable, cannot be added to set

# --------- Tuple addition to set ---------

a = {25, 10.8, 'Hyd', True}   # True is 1, 'Hyd', 10.8, 25
tpl = (10, 20, 30)            # A tuple (immutable)
print(a)                      # Prints set
print(id(a))                  # Prints object id (memory address)
a.add(tpl)                    # OK; tuples are hashable
a.add('Sec')                  # Adds 'Sec'
print(a)                      # Prints set with tuple and 'Sec'
print(id(a))                  # ID stays same; set object is same
print(len(a))                 # Number of items including tuple and string

a.add([100, 200, 300])        # ERROR: list is mutable/unhashable
a.add(set())                  # ERROR: set is mutable/unhashable
a.add({})                     # ERROR: dict is mutable/unhashable

# --------- Adding a tuple to an empty set ---------

s = set()                     # Create empty set
tpl = (10, 20, 15, 18)        # A tuple (immutable)
s.add(tpl)                    # OK: adds tuple as element
print(s)                      # Prints set with tuple as single element
print(len(s))                 # 1, since one tuple added

# --------- update() method demo ---------

tpl = (10, 20, 15, 18, 10, 20) # Tuple with duplicates
s = set()                     # Empty set
s.update(tpl)                 # Adds each unique element of tuple (like extend for sets)
print(len(s))                 # Prints 4
print(s)                      # Prints set: {10, 20, 15, 18}
s.update(25)                  # ERROR: int is not iterable, update needs an iterable

# --------- update() with multiple sequences, add() error ---------

a = [10, 20, 30]              # List
b = {30, 40, 50}              # Set
c = (50, 60, 70)              # Tuple
s = set()
s.update(a, b, c)             # Adds unique elements from all collections
print(s)                      # Prints set: {10, 20, 30, 40, 50, 60, 70}
print(len(s))                 # 7
s.add(a, b, c)                # ERROR: add() only takes one argument

# --------- update() with string and non-sequence ---------

a = set()
a.update('Rama Rao')          # Treats string as sequence, adds each unique char
print(a)                      # Each character seen once in set
print(len(a))                 # Count of unique characters in string
a.update(3+4j, 10.8, True)    # ERROR: Each needs to be iterable, but these aren't

# --------- copy() method demo ---------

a = {10, 20, 15, 18}
print(a)
b = a.copy()                  # Creates deep copy (new set with same elements)
print(b)
print(a is b)                 # False, because different objects
print(a == b)                 # True, same elements
c = a
print(a is c)                 # True, c is just another name for a

# --------- pop() method demo ---------

a = {25, 10.8, 'Hyd', True}
print(a)
print(a.pop())                # Removes and returns a random element (order not guaranteed)
print(a.pop())                # Ditto
print(a.pop())                # Ditto
print(a.pop())                # Set will be empty after 4 pops
print(a.pop())                # ERROR: set is empty, KeyError raised
print(a)                      # Now empty set

b = {10, 20, 30, 40}
print(b.pop(2))               # ERROR: pop() takes no arguments

# --------- remove() method demo ---------

a = {25, 10.8, 'Hyd', True}
print(a)
a.remove('Hyd')               # Removes 'Hyd'
print(a)
a.remove('Sec')               # ERROR: 'Sec' not present, KeyError raised

# --------- discard() method demo ---------

a = {25, 10.8, 'Hyd', True}
print(a)
a.discard('Hyd')              # Removes 'Hyd'
print(a)
a.discard('Sec')              # Does nothing. No error.
print(a)
a.remove('Sec')               # ERROR: 'Sec' not present, raises KeyError

# --------- clear() method demo ---------

a = {10, 20, 15, 18}
print(a)
a.clear()                     # Removes all items; set becomes empty
print(a)
print(len(a))                 # 0

# --------- Set operations and errors ---------

a = {10, 20, 30, 40}
b = [30, 40, 50, 60]
print(a.union(b))             # OK: union with any iterable, {10, 20, 30, 40, 50, 60}
print(a | b)                  # ERROR: | (union) requires both as sets, TypeError
print(b.union(a))             # ERROR: 'list' object has no attribute 'union'
print(a + b)                  # ERROR: cannot add set and list, TypeError
