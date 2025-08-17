17/07: Homework 6
a = "Rama Rao"        # assigns "Rama Rao" to a
print(a)              # Rama Rao        # prints string
print(type(a))        # <class 'str'>   # type is string
print(id(a))          # e.g., 140500213205104  # memory address (id varies)

b = 'Hyd'             # assigns 'Hyd' to b
print(b)              # Hyd             # prints string


c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''  # multi-line string
print(c)              
# Hyd is green city.
# Hyd is hitec city.
# Hyd is beautiful city.
# multi-line string is printed as-is

a = 'Hyd'             # 'H'->0, 'y'->1, 'd'->2
# How to print 'H' of object 'a'?
print(a[0])           # H              # index 0 = first character
# How to print 'y' of object 'a'?
print(a[1])           # y              # index 1 = second character
# How to print 'd' of object 'a'?
print(a[2])           # d              # index 2 = third character

print(a[3])           # IndexError     # string index out of range (max index is 2)
# How to print 'd' of object 'a'?
print(a[-1])          # d              # negative index: -1 = last char
# How to print 'y' of object 'a'?
print(a[-2])          # y              # negative index: -2 = second last
# How to print 'H' of object 'a'?
print(a[-3])          # H              # negative index: -3 = first char

print(a[-4])          # IndexError     # index out of range
print(a[0] == a[-3])  # True            # a[0] == 'H', a[-3] == 'H'

a[2] = 'c'            # TypeError      # strings are immutable in Python

print(25[0])          # TypeError      # int object is not subscriptable
print('25'[0])        # 2              # indexing works on string, gives first char
print(True[1])        # TypeError      # bool object is not subscriptable
print('True'[1])      # r              # indexing string gives second char

a = 'Hyd'
print(a * 3)          # HydHydHyd      # string repeated 3 times
print(a * 2)          # HydHyd         # repeated twice
print(a * 1)          # Hyd            # repeated once
print(a * 0)          # ''             # repeated zero times = empty string
print(a * -1)         # ''             # negative repeats give empty string

print(25 * 3)         # 75             # 25×3 = 75 (number multiplication)
print('25' * 3)       # 252525         # string '25' repeated 3 times
print('25' * 4.0)     # TypeError      # float repeat count not allowed
print(3 * 'Hyd')      # HydHydHyd      # same as 'Hyd'*3
print('25' * True)    # 25             # True = 1, so repeated once

a = 'Hyd'
print(a, id(a))       # Hyd 140500213206576   # prints string and its memory id
a = a * 3             # creates a new string object 'HydHydHyd'
print(a, id(a))       # HydHydHyd 140500213207024  # id changes (new object)

a = """"Hyd"""        # syntax error in code (too many quotes)
# Corrected:
a = """Hyd"""         # assigns 'Hyd' to a
print(a)              # Hyd            # prints string
print(len(a))         # 3              # length of 'Hyd'
print(a[0])           # H              # first char of string

print("""Hyd"""")     # SyntaxError    # invalid syntax

b = """""Hyd"""       # syntax error in code (too many quotes)
# Corrected:
b = """Hyd"""         # assigns 'Hyd' to b
print(b)              # Hyd            # prints string
print(len(b))         # 3              # length of 'Hyd'

a = 'Sankar Dayal Sarma'

print(a[7:12])        # Dayal          # substring from index 7 to 11
print(a[7:])          # Dayal Sarma    # from index 7 to end
print(a[:6])          # Sankar         # from start to index 5
print(a[:])           # Sankar Dayal Sarma # whole string
print(a[::])          # Sankar Dayal Sarma # whole string
print(a[1:10:2])      # aka a          # slice from 1 to 9, step 2
print(a[0::2])        # SnkrDylSrm     # every second char starting at index 0
print(a[1::2])        # a a aa aa      # every second char starting at index 1
print(a[-5:-1])       # Sarm           # substring from index -5 to -2
print(a[::-1])        # amraS lay aD raknaS # reverse string
print(a[-1:-5:-1])    # amra           # reverse substring from -1 to -4
print(a[::-2])        # arSlyDrka      # reverse string, step -2
print(a[3:-3])        # kar Dayal Sar  # from index 3 to -4
print(a[2:-5])        # nkar Dayal Sa  # from index 2 to -6
print(a[-1:-5])       # ''             # empty (no slice because step defaults to +1)
print(a[3:3])         # ''             # empty (start and stop same)
