1.
# Find outputs (Home work)
a = 25
b = '%f' % a
# Explanation: `a` is an integer 25. The `%` format specifier is used for floating-point numbers.
# When an integer is formatted with `%`, it's converted to a float (25.0) and then formatted to 6 decimal places by default. # So, b becomes the string '25.000000'.
print(b)
# Output: 25.000000
print(type(b))
# Output: <class 'str'>
# Explanation: The result of string formatting is always a string.
x = 10.8
y =
'%d' % x
# Explanation: `x is a float 10.8. The `%` format specifier is used for integers.
# When a float is formatted with %d`, its decimal part is truncated (cut off, not rounded) before being converted to a string. # So, 10.8 becomes 10, and `y` becomes the string '10'.
print(y)
# Output: 10
print(type(y))
# Output: <class 'str'>
# Explanation: The result of string formatting is always a string.
m =
[10, 20, 15, 18]
n = '%s' % m
# Explanation: `m` is a list. The `%s format specifier is used to represent any object as a string.
# It effectively calls `str(m) to get the string representation of the list.
# So, `n becomes the string '[10, 20, 15, 18]'.
print(n)
# Output: [10, 20, 15, 18]
print(type(n))
# Output: <class 'str'>
# Explanation: The result of string formatting is always a string.




2.
# Find outputs (Home work)
a, b, c = 25, 10.8, 'Hyd'
# Explanation: Variables are initialized: a=25, b=10.8, c='Hyd'.
print(a, b, c, end = '---')
# Output segment 1: 25 10.8 Hyd---
# Explanation: Prints the values of a, b, c separated by default spaces.
# The `end='---'` argument replaces the default newline character with
# so the cursor remains on the same line immediately after 'Hyd---'.
print(a, b, c, sep = ',,,')
# Output segment 2: 25,,,10.8,,,Hyd
# Explanation: This print statement starts immediately after 'Hyd---' from the previous line. # It prints the values of a, b, c separated by `,,,`.
# Since no `end` argument is specified, it uses the default `end='\n'` (newline),
# moving the cursor to the next line after printing.
# Cumulative Output:
# 25 10.8 Hyd---25,,, 10.8,,,Hyd
print(a, b, c, sep
= :::' end =
'\t\t\t')
(followed by three tabs)
# Output segment 3: 25:::10.8::: Hyd
# Explanation: This print statement starts on the new line.
# It prints the values of a, b, c separated by `:::
# The `end='\t\t\t'` argument replaces the default newline with three tab characters,
# so the cursor remains on the same line after printing the tabs.
# Cumulative Output:
# 25 10.8 Hyd ---25,,, 10.8,,,Hyd
#25: 10.8::: Hyd
print(a, b, c)
(cursor here)
# Output segment 4: 25 10.8 Hyd
# Explanation: This print statement starts immediately after the three tabs from the previous line.
# It prints the values of a, b, c separated by default spaces.
# Since no `end` argument is specified, it uses the default `end='\n'`, moving the cursor to the next line. # Cumulative Output:
# 25 10.8 Hyd ---25,,, 10.8,,,Hyd
# 25:10.8::: Hyd
25 10.8 Hyd




3.
#sep argument demo program
a, b, c = 25, 10.8, 'Hyd'
# Explanation: Variables are initialized: a=25, b=10.8, c='Hyd.
print(a, b, c, sep = ', ')
# Output: 25,10.8, Hyd
# Explanation: The sep argument specifies the string to be used as a separator between the items printed. Here, it's a comma, so no spaces are inserted by default around the comma itself.
print(a, b, c, sep= # Output: 25
10.8
'\t') Hyd
# Explanation: The sep argument is set to '\t', which is the tab character. This inserts a tab space between each item.
print(a, b, c, sep= --')
# Output: 25---10.8---Hyd
# Explanation: The sep argument is set to
print(a, b, c, sep = '\n')
# Output:
# 25
# 10.8
# Hyd
so three hyphens are inserted between each item.
# Explanation: The sep argument is set to "\n", which is the newline character. This causes each subsequent item to be printed on a new line.
print(a, b, c)
# Output: 25 10.8 Hyd
# Explanation: when the sep argument is not specified, the default separator is a single space character.
print(a, b, c, separator =
# Output: TypeError: print() got an unexpected keyword argument 'separator'
# Explanation: The print() function's argument for specifying the item separator is sep", not "separator. Using an incorrect keyword argument name results in a TypeError", and the program execution stops at this point.






4.
# Find outputs (Home work)
print('Hyd')
# Output: Hyd
# Explanation: Prints the string 'Hyd' followed by a default newline character.
print()
# Output: (a blank line)
# Explanation: Calling 'print()` without any arguments simply prints a default newline character, resulting in a blank line.
print('Sec')
# Output: Sec
# Explanation: Prints the string 'Sec' followed by a default newline character.
print()
# Output: (another blank line)
# Explanation: Again, prints a newline character, creating another blank line.
print('Cyb')
# Output: Cyb
# Explanation: Prints the string 'Cyb' followed by a default newline character.






5.
# Find outputs (Home work)
a = [10, 20, 30, 40]
# Explanation: Variable `a` is initialized as a list.
print('%s' % a)
# Output: [10, 20, 30, 40]
# Explanation: The %s format specifier converts any object to its string representation.
# For a list, this is its standard literal string form.
print('%s', a)
# Output: %s [10, 20, 30, 40]
# Explanation: This is a `print()` function call with two separate arguments: the string literal
# `print()` prints each argument, separated by a default space. No string formatting occurs here. print('%s' a)
# Output: SyntaxError: invalid syntax
and the variable `a`.
# Explanation: This is a syntax error. You cannot place a string literal and a variable next to each other like this # without an operator (like `+ for concatenation) or using the correct formatting syntax (% operator or f-strings). # The program execution stops at this point.





6.
# Find Outputs (Home work)
a = 10.9274
print('%8.2f' % a)
# Output:
# Explanation:
10.93
# - ` .2f : Formats `a` to two decimal places. 10.9274 rounds to 10.93.
# - `8`: Specifies a total field width of 8 characters. The formatted number "10.93" is 5 characters long.
# - Padding: 8 - 5 = 3 spaces are added to the left to meet the specified width.
print('%9.1f' % a)
# Output:
# Explanation:
10.9
# - ` .1f: Formats `a` to one decimal place. 10.9274 rounds to 10.9.
# - `9`: Specifies a total field width of 9 characters. The formatted number "10.9" is 4 characters long. # - Padding: 9 4 5 spaces are added to the left.
print('%10.3f' % a)
# Output:
# Explanation:
=
10.927
# - `.3f: Formats `a` to three decimal places. 10.9274 rounds to 10.927.
# - `10: Specifies a total field width of 10 characters. The formatted number "10.927" is 6 characters long.
# - Padding: 10 6 4 spaces are added to the left.
print('%.2f' % a)
# Output: 10.93
# Explanation:
# - ` .2f : Formats `a` to two decimal places (10.93).
# - No width specified, so it uses only the necessary width.
print('%.6f' % a)
# Output: 10.927400
# Explanation:
# - `.6f`: Formats `a` to six decimal places. 10.9274 is padded with zeros to become 10.927400.
# - No width specified.
print('%f' % a)
# Output: 10.927400
# Explanation:
# - `%f`: Uses the default floating-point formatting, which typically means 6 decimal places if no precision is specified. 10.9274 is padded with zeros to become 10.927400.
#
-




7.
# Find outputs (Home work)
1
=
t =
[10, 20, 30, 40]
(10, 20 30 40)
,
J
S = {10, 20, 30, 40}
# Explanation: Variables are initialized as a list, a tuple, and a set respectively.
print(1, t, 5)
# Output: [10, 20, 30, 40] (10, 20, 30, 40) (10, 20, 30, 40}
# Explanation: The `print() function, when given multiple arguments, converts each argument to its string representation # and prints them separated by a single space (the default sep` argument).
#
#
Lists are printed with square brackets `[]`.
-
Tuples are printed with parentheses ()`.
# - Sets are printed with curly braces `{}`. Note that while sets are unordered internally,
# for simple numeric sets, Python's string representation often displays them in a consistent (e.g., sorted) order.




8.
# Tricky program
# Find output (Home work) print(eval('print("Hyd")'))
Hyd None




9.
# eval() function demo program print(eval('25'))
# 25
print(eval('10.8'))
# 10.8
print(eval('False'))
# False
print(eval('3+4j')) # (3+4j)
print(eval('Hyd'))
# NameError: name 'Hyd' is not defined
print(eval("
# Hyd
'Hyd' "))
print (eval('3 + 4 * 5'))
# 23
print(eval('[10, 20, 15, 18]'))
# [10, 20, 15, 18]
print (eval('{10, 20, 15, 18, 20,12,18}')) # {10, 12, 15, 18, 20}
print(eval('(10, 20, 30)'))
# (10, 20, 30)
print(eval("{10: 'Hyd', 10 : 'Sec'}"))
# {10: 'Sec'}
print (eval(4 + 5))
# TypeError: eval() arg 1 must be a string, bytes or code object







10.
# Tricky program
# Find outputs (Home work) print(eval("
# hyd
hyd = 'Sec'
'hyd'
print (eval(' hyd'))
# Sec
sec = '25'
print(eval('sec'))
# 25
print (eval (sec))
# 25
cyb = 10.8
print(eval('cyb'))
# 10.8
print(eval(cyb))
"))
# TypeError: eval() arg 1 must be a string, bytes or code object
