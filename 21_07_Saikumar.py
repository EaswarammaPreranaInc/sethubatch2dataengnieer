# How  to  print  dictionary  in  different  ways

a = {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}

# 1. Print dictionary directly
print('Dictionary with print function:')
print(a)

# 2. Print keys of dictionary
print('Keys of dictionary:')
for key in a.keys():
    print(key)

# 3. Print values of dictionary
print('Values of dictionary:')
for value in a.values():
    print(value)

# 4. Print all tuples from dict_items
print('All the tuples of dict_items object:')
for item in a.items():
    print(item)

# 5. Print elements of each tuple
print('Elements of each tuple:')
for key, value in a.items():
    print(key, value)

# 6. Print keys and values of dictionary in list form
print('Keys and values of dictionary (dict_items object):')
print(list(a.items()))


# Find outputs (Home work)

a = {
    print('Hyd'),  # Executes immediately and prints "Hyd", returns None
    print('Sec'),  # Executes immediately and prints "Sec", returns None
    print('Cyb')   # Executes immediately and prints "Cyb", returns None
}
print(type(a))     # Since we are using curly braces, this creates a set
print(a)           # The set 'a' will contain only {None}, because print() returns None
print(len(a))      # Length of the set is 1


# Anonymous object demo program

_ = 25                  # Assigns 25 to the variable '_'
print(_)                # Prints 25
print(type(_))          # Prints the type of '_', which is <class 'int'>
a, _, c = 10, 20, 30    # Tuple unpacking a = 10, _ = 20 and c = 30
print(a)                # Prints 10
print(_)                # Prints 20 the new value of _ from tuple unpacking
print(c)                # Prints 30
for _ in range(5):      # Uses _ as the loop variable
    print(_, 'Hello')   # Prints the values 0 to 4 along with "Hello"


# Find outputs

a = 25                   # 'a' is assigned the value 25
print(id(a))             # Prints the address of the integer object 25
a = 35                   # 'a' is now reassigned to a new integer value 35
print(id(a))             # Prints the new address of the integer object 35


# Find outputs (Home work)

a = 25.7                  # Assigns the float value 25.7 to variable 'a'
print(id(a))              # Prints the address of float object 25.7
print(a)                  # Prints the value of 'a', which is 25.7
a = 35.6                  # 'a' is reassigned to a new float value 35.6
print(id(a))              # Prints the address of new float object 35.6
print(a)                  # Prints the value of 'a', which is 35.6
b = True                  # Assigns boolean value True to variable 'b'
print(id(b))              # Prints the address of True 
b = False                 # Reassigns 'b' to False
print(id(b))              # Prints the address of False 
c = None                  # Assigns NoneType value None to variable 'c'
print(id(c))              # Prints the address of None
c = None                  # Reassigns the same None value to 'c'
print(id(c))              # Prints the address again 


# Find outputs (Home work)

a = 'Hyd'                 # Assigns the string 'Hyd' to variable 'a'
print(id(a))              # Prints the address of the string 'Hyd'
a[1] = 'e'                # Error Strings are immutable, cannot assign value to index                      
a = 'Sec'                 # 'a' is reassigned to a new string value 'Sec'
print(id(a))              # Prints the address of the new string 'Sec'
b = (10, 20, 15, 18)      # Assigns a tuple to variable 'b'
print(id(b))              # Prints the address of the tuple
b[2] = 19                 # Error Tuples are immutable, cannot assign value to index                      
b = (30, 40, 35, 32)      # creates a new tuple of object b
print(id(b))              # Prints the address of the new tuple
c = range(5)              # Creates a range object (0 to 4)
print(id(c))              # Prints the address of the range object
c[3] = 10                 # Error range object does not support item assignment
c = range(5)              # Creates the new range object 
print(id(c))              # Prints the address of the new range object


# Find outputs (Home work)

a = 25                   # Assigns integer 25 to variable a
b = 25                   # Assigns integer 25 to variable b 
print(a is b)            # True  'a' and 'b' point to the same memory 
c = 'Hyd'                # Assigns string 'Hyd' to variable c
d = 'Hyd'                # Assigns string 'Hyd' to variable d
print(c is d)            # True because both refer to the same object
e = False                # Assigns boolean False to variable e
f = False                # Assigns boolean False to variable f
print(e is f)            # True because Boolean values are singleton objects in Python
g = range(10)            # Creates a range object from 0 to 9
h = range(10)            # Creates another range object from 0 to 9
print(g is h)            # False range() creates a new range object


# Find outputs (Home work)

a = [10, 20, 15, 18]      # Creates a list and assigns to 'a'
b = [10, 20, 15, 18]      # Creates another list with the same elements, but a different object
print(a is b)             # False  'a' and 'b' are two different list objects 
c = {10: 20, 30: 40}      # Creates a dictionary and assigns to 'c'
d = {10: 20, 30: 40}      # Creates another dictionary with same key-value pairs, but a different object
print(c is d)             # False 'c' and 'd' are different dictionary objects
e = (10, 20, 15, 18)      # Creates a tuple and assigns to 'e'
f = (10, 20, 15, 18)      # Creates another identical tuple
print(e is f)             # True for immutable objects like small tuples
g = {10, 20, 15, 18}      # Creates a set and assigns to 'g'
h = {10, 20, 15, 18}      # Creates another set with same values
print(g is h)             # False 'g' and 'h' are different set objects


# Find outputs (Home work)

print(10 + 20)                                   # Adds two integers 30
print(10.8 + 20.6)                               # Adds two float numbers 31.4
print(3 + 4j + 5 + 6j)                           # Adds two complex numbers (8+10j)
print(True + False)                              # In boolean, True=1, False=0 1 + 0 = 1
print('Hyder' + 'abad')                          # Concatenates two strings 'Hyderabad'
print('Sankar' + 'Dayal' + 'Sarma')              # Concatenates three strings 'SankarDayalSarma'
print('10' + '20')                               # Concatenates two strings '10' and '20' '1020'
print([10, 20, 30] + [1, 2, 3])                  # Concatenates two lists [10, 20, 30, 1, 2, 3]
print((25, 10.8, 'Hyd') + (3+4j, True, None))    # Concatenates two tuples (25, 10.8, 'Hyd', (3+4j), True, None)
print({10, 20} + {30, 40})                       # Error '+' not supported for set objects
print({10: 'Hyd'} + {20: 'Sec'})                 # Error '+' not supported for dict objects
print(range(4) + range(5))                       # Error '+' not supported for range objects
print(10 + '20')                                 # Error Cannot add int and str 
print([10, 20, 30] + 5)                          # Error Cannot add list and int 
print([10, 20, 30] + (40, 50, 60))               # Error Cannot add list and tuple 


# Find outputs (Home work)

print(25 * 3)                         # Multiplies two integers, result is 75
print(10.8 * 25.6)                    # Multiplies two floats, result is 276.48
print(True * False)                   # True is 1, False is 0, result is 0
print((3 + 4j) * (5 + 6j))            # Complex number multiplication, result is (-9+38j)
print(3 + 4j * 5 + 6j)                # 4j * 5 = 20j, then 3 + 20j + 6j = 3 + 26j
print('25' * 3)                       # Repeats string '25' three times, result is '252525'
print(3 * '25')                       # Same as above, result is '252525'
print('Hyd' * 4)                      # Repeats 'Hyd' four times, result is 'HydHydHydHyd'
print([10, 20, 15] * 2)               # Repeats list two times, result is [10, 20, 15, 10, 20, 15]
print((25, 10.8, 'Hyd', True) * 3)    # Repeats tuple three times
print([10, 20, 15] * 3.0)             # Error, list cannot be multiplied by a float
print({10, 20, 15} * 2)               # Error, set cannot be multiplied
print({10: 20, 30: 40} * 2)           # Error, dictionary cannot be multiplied
print([10] * [20])                    # Error, list cannot be multiplied by another list


# / operator demo program

print(9.0 / 2)        # Float / Int result is 4.5
print(9 / 2.0)        # Int / Float result is 4.5
print(9.0 / 2.0)      # Float / Float result is 4.5
print(9 / 2)          # Int / Int result is 4.5 
print(10.5 / 2)       # Float / Int result is 5.25
print(10 / 3)         # Int / Int result is 3.333....
print(10 / 2)         # Int / Int result is 5.0


# // operator demo program

print(9 // 2)           # Integer division 4 (floor of 4.5)
print(9.0 // 2)         # Float // Int 4.0 (floor of 4.5)
print(9 // 2.0)         # Int // Float 4.0 (floor of 4.5)
print(9.0 // 2.0)       # Float // Float 4.0 (floor of 4.5)
print(10.5 // 2)        # 5.0 (floor of 5.25)
print(10 // 3)          # 3 (floor of 3.333...)
print(10.0 // 3)        # 3.0 (floor of 3.333...)
print(8.5 // 3)         # 2.0 (floor of 2.833...)
print(18 // 4)          # 4 (floor of 4.5)
print(-18 // 4)         # -5 (floor of -4.5 is -5)
print(-(18 // 4))       # -4 (18 // 4 is 4, negated gives -4)


# % operator demo program

print(9 % 5)         # 4, remainder of 9 divided by 5
print(9.0 % 5)       # 4.0, float result, 9.0 divided by 5 gives remainder 4.0
print(9 % 5.0)       # 4.0, float result, same logic as above
print(9.0 % 5.0)     # 4.0, float result, same logic
print(10.5 % 2)      # 0.5, 10.5 divided by 2 leaves remainder 0.5
print(8.9 % 3)       # 2.9, 8.9 divided by 3 gives remainder 2.9

# Find Outputs

print(7 / 0)     #  Error division by zero is not possible
print(7 // 0)    #  Error integer division zero is not possible
print(7 % 0)     #  Error integer modulo by zero is not possible


# operator demo program

print(3 ** 4)                    # 81 (3 raised to the power of 4)
print(10 ** -2)                  # 0.01 (10 raised to the power of -2, i.e., 1/100)
print(4 ** 3 ** 2)               # 262144 (evaluated as 4 ** (3 ** 2) = 4 ** 9)
print(3 + 4 * 5 - 32 / 2 ** 3)   # 19.0


# Relational operators demo program (Home work)

print(9 >= 5)                 # True greater than condition is satisfied
print(9 >= 9)                 # True equal to condition is satisfied
print(9 >= 12)                # False neither greater nor equal
print(6 <= 8)                 # True less than condition is satisfied
print(6 <= 6)                 # True equal to condition is satisfied
print(6 <= 4)                 # False neither less nor equal
print(9 != 7)                 # True values are not equal
print(6 == 8)                 # False values are not equal
print(True > False)           # True True is 1, False is 0
print(3 + 4j == 3 + 4j)       # True both complex numbers are equal
print(3 + 4j == 5 + 6j)       # False complex numbers are different
print(3 + 4j != 5 + 6j)       # True complex numbers are not equal
print(10 == 10.0)             # True values are equal though types differ
print(3 + 4j > 3 + 4j)        # Error '>' not supported between complex numbers


# Find outputs (Home work)

print('Rama' > 'Rajesh')        # True 'm' > 'j' in alphabetical comparison
print('Rama' < 'Sita')          # True 'R' < 'S'
print('Hyd' == 'Hyd')           # True both strings are exactly equal
print('Rama' <= 'Ramana')       # True 'Rama' is a prefix of 'Ramana', so it's less
print('Rama Rao' >= 'Rama')     # True 'Rama Rao' comes after 'Rama' lexicographically
print('Hyd' != 'Sec')           # True the strings are not equal
print('HYD' < 'hyd')            # True uppercase letters come before lowercase in Unicode


# Chaining relational operators (Home work)

print(10 < 20 < 30)            # True  10 < 20 and 20 < 30
print(10 >= 20 < 30)           # False  10 >= 20 is False
print(10 < 20 > 30)            # False  20 > 30 is False
print(1 < 2 < 3 < 4)           # True  1 < 2 and 2 < 3 and 3 < 4
print(1 < 2 > 3 > 1)           # False  2 > 3 is False
print(4 > 3 >= 3 > 2)          # True  4 > 3 and 3 >= 3 and 3 > 2


# or operator demo program

print(True or False)           # True  At least one operand is True so the result is True
print(False or True)           # True  At least one operand is True so the result is True
print(True or True)            # True  Both operands are True so the result is True
print(False or False)          # False  Both operands are False so the result is False
print(10 or 20)                # 10  10 is truthy (non-zero) so it is returned without checking 20
print(0 or 20)                 # 20  0 is falsy so it returns the second truthy value 20
print(-25 or 0)                # -25  Non-zero numbers are truthy so -25 is returned
print('' or 35)                # 35  Empty string is falsy so the second operand 35 is returned
print(6j or 'Hyd')             # 6j  Non-zero complex number is truthy so 6j is returned
print(0.0 or 3 + 4j)           # (3+4j)  0.0 is falsy so the second operand is returned
print('Hyd' or 10.8)           # Hyd  Non-empty string is truthy so 'Hyd' is returned


# not operator demo program

print(not True)           # False The boolean value of True is negated to False
print(not False)          # True The boolean value of False is negated to True
print(not 25)             # False 25 is a non-zero number, so not 25 is False
print(not 0)              # True 0 is false, so not 0 is True
print(not 'Hyd')          # False Non-empty string is truthy, so not 'Hyd' is False
print(not '')             # True Empty string is false, so not '' is True
print(not -10)            # False Any non-zero number is true, so not -10 is False
print(not not 'Hyd')      # True 'Hyd' is true, not 'Hyd' is False, and not False is True


# Find outputs (Home work)

i = 10                                  # Assigns 10 to variable i
i = not i > 14                          # Evaluates (i > 14)  False, then not False = True
print(i)                                # Output: True
print(not(6 < 4 or 9 >= 5 and 6 != 6))  # Output: True

