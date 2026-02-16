1.
text
a = range(10 , 50 , 5)

print(type(a))
# Output: <class 'range'>
# Explanation: This prints the data type of the variable 'a', which is a 'range' object.

print(a)
# Output: range(10, 50, 5)
# Explanation: Printing a 'range' object directly shows its internal representation (start, end, step), rather than all the numbers it contains.

print(*a)
# Output: 10 15 20 25 30 35 40 45
# Explanation: The `*` operator unpacks the elements of the `range` object and passes them as separate arguments to the `print()` function, which then prints them separated by spaces.

print(id(a))
# Output: [A unique memory address, e.g., 140700346337456]
# Explanation: This prints the unique memory address where the `range` object 'a' is stored. The actual address will be different each time the program runs.

print(len(a))
# Output: 8
# Explanation: The `len()` function calculates the number of elements in the range. The formula is (stop - start) // step, which is (50 - 10) // 5 = 40 // 5 = 8.

print(*a[2 : 7] , sep = ' , ')
# Output: 20 , 25 , 30 , 35 , 40
# Explanation: This first creates a slice of the `range` object from index 2 (inclusive) to 7 (exclusive). This new range contains the numbers 20, 25, 30, 35, 40. The `*` operator unpacks these numbers and the `sep` argument specifies a comma and a space as the separator.

print(*a[ : : -1])
# Output: 45 40 35 30 25 20 15 10
# Explanation: This creates a reverse slice of the entire `range` object (step is -1), which generates the numbers in reverse order. The `*` operator unpacks and prints them.

a[4] = 32
# Output: Type Error: `range` object does not support item assignment
# Explanation: `range` objects are **immutable**, meaning their elements cannot be changed or modified after creation. Attempting to assign a new value to an index results in a `Type Error`.

# print(a * 2)
# Output: Type Error: unsupported operand type(s) for *: 'range' and 'int'
# Explanation: The `range` object does not support the multiplication operator. You cannot repeat or multiply a `range` object.



2.
text
r = range(10 , 17 , 3)

a , b , c = r
print(a , b , c)
# Output: 10 13 16
# Explanation: The `range` object `r` contains three elements (10, 13, 16). The variables 'a', 'b', and 'c' are assigned to these elements in order, and the `print()` function displays their values.

r = range(3)

x , y = r
# Output: Value Error: too many values to unpack (expected 2)
# Explanation: The `range` object `r` now contains three elements (0, 1, 2). The assignment statement tries to unpack these three elements into only two variables ('x' and 'y'). Since the number of elements does not match the number of variables, a `Value Error` is raised.

p , q , r , s = r
# Output: Value Error: not enough values to unpack (expected 4, got 3)
# Explanation: The `range` object `r` contains three elements (0, 1, 2). The assignment statement tries to unpack these into four variables ('p', 'q', 'r', 's'). Since there are not enough elements to fill all the variables, a `Value Error` is raised.

a , b , c = *r
# Output: Syntax Error: can't use starred expression here
# Explanation: The starred expression `*r` cannot be used on the right-hand side of a simple assignment statement in this manner. The correct way to unpack a sequence like `range` is `a, b, c = r` without the `*`. This is a `Syntax Error` and would prevent the program from running.




3.
text
# a = range(10 , 20)
# print(*a , sep = ',')
# Output: 10,11,12,13,14,15,16,17,18,19
# Explanation: A `range` object is created with a starting value of 10 (inclusive) and an ending value of 20 (exclusive). The default step is 1. The `*` operator unpacks these numbers and the `sep` argument specifies a comma as the separator.

# b = range(5)
# print(*b)
# Output: 0 1 2 3 4
# Explanation: When `range()` is called with a single argument, it is treated as the stop value, with the start defaulting to 0 and the step defaulting to 1. The `*` operator unpacks and prints the numbers with a default space separator.

# c = range(10 , 1 , -1)
# print(*c , sep = '...')
# Output: 10...9...8...7...6...5...4...3...2
# Explanation: A `range` is created starting at 10 and counting down to 1 (exclusive) with a step of -1. The `*` operator unpacks the numbers and the `sep` argument specifies '...' as the separator.

# d = range(-10 , 0)
# print(*d)
# Output: -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# Explanation: A `range` is created starting at -10 (inclusive) and ending at 0 (exclusive) with a default step of 1.

# e = range(-10)
# print(*e)
# Output: (empty line)
# Explanation: When `range()` is called with a single negative argument, it is interpreted as `range(0, -10)`. Since the start (0) is greater than the stop (-10) and the step is positive (the default 1), the range is empty. Unpacking an empty sequence results in no output.

# f = range(2 , 2)
# print(*f)
# Output: (empty line)
# Explanation: The start and stop values are the same. Since the `range` function's stop value is exclusive, the range is empty. Unpacking an empty sequence results in no output.

# g = range(10 , 11 , 0.1)
# Output: Type Error: 'float' object cannot be interpreted as an integer
# Explanation: The `range()` function requires all its arguments (start, stop, and step) to be integers. A `Type Error` is raised when a float (0.1) is used as the step.

# h = range('A' , 'F')
# Output: Type Error: 'str' object cannot be interpreted as an integer
# Explanation: The `range()` function requires all its arguments to be integers. A `Type Error` is raised when strings are used.
