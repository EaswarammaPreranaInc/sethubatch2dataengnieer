# Output:
1
Sec
Hello
2
Sec
Hello
3
# (continue skips the else block, so 'Sec' and 'Hello' not printed)
4
Sec
Hello
5
Sec
Hello
6
# (i % 3 == 0 → continue, skips the else and 'Hello')
7
Sec
Hello
Outside loop

#########################################################################

# Errors:

1) SyntaxError: expected expression inside `if ()’
   → The condition inside `if`is missing. Example fix: if (True):

2) SyntaxError: 'continue' not properly in loop
   → 'continue' can only be used inside loops (like for or while), not in an if block alone.

# Correct version (if placed inside a loop):
for i in range(1):
    if True:
        print('Hyd')
        continue
        print('Sec')
        
#################################################################################

# Output:
1
Sec
Hello
2
Sec
Hello
3
# (i % 3 == 0 → break, exits the loop immediately)
Outside loop

###################################################################################

# Errors:

1) SyntaxError: cannot use a comma-separated tuple directly as condition in `if’
   → `if (10, 20, 30)`creates a tuple, which is truthy, but not ideal or intended.
   → Fix: Use a proper condition like ‘if True:’or `if 10:’.

2) SyntaxError: 'break' outside loop
   → `break`can only be used inside a loop (like for or while), not inside an if-block alone.

# Correct version (if intended inside a loop):
for i in range(1):
    if True:
        print('Hyd')
        break
        print('Sec')

###################################################################

# Output:
1
Sec
Hello
2
Sec
Hello
3
Hyd
Hello
4
Sec
Hello
5
Sec
Hello
6
Hyd
Hello
7
Sec
Hello
Outside loop

############################################################################

# Output:
1
Sec
Hello
2
Sec
Hello
3
# i % 3 == 0 → exit() is called → program terminates immediately
# So nothing after this is executed

# Final Output:
1
Sec
Hello
2
Sec
Hello
3

##########################################################
# Output:
1
Sec
Hello
2
Sec
Hello
3
# (i % 3 == 0 → continue → skips 'else' and 'Hello')
4
Sec
Hello
5
Sec
Hello
6
# (i % 3 == 0 → continue → skips 'else' and 'Hello')
7
Sec
Hello
else  suite
Outside  loop

###########################################################

# Output:
1
Sec
Hello
2
Sec
Hello
3
# i % 3 == 0 → break → loop terminates immediately, skips else suite
Outside  loop

###########################################################

# Output:
1
Sec
Hello
2
Sec
Hello
3
Sec
Hello
4
Sec
Hello
5
Sec
Hello
6
Sec
Hello
7
Sec
Hello
else  suite
Outside loop

############################################################

# Input list and element to search
a = [10, 20, 30, 40, 50]
x = int(input("Enter element to search: "))

found = False

# Search using loop (not using 'in')
for i in a:
    if i == x:
        found = True
        break

# Result
if found:
    print("Found")
else:
    print("Not Found")
    
  ###############################################################

# Input list and element to search
a = eval(input("Enter any list: "))
x = eval(input("Enter the element to be searched : "))

found = False

# Manual search
for i in range(len(a)):
    if a[i] == x:
        print("Found at index :", i)
        found = True
        break

if not found:
    print("Not Found")  
    
##########################################################

# Input list and element to search
a = eval(input("Enter the list: "))
x = eval(input("Enter the element to search: "))

count = 0

# Loop to find all occurrences
for i in range(len(a)):
    if a[i] == x:
        print(x, "is found at index", i)
        count += 1

# Result
if count > 0:
    print(x, "is found", count, "times")
else:
    print(x, "is not found")

####################################################

print(a := 25)         # assigns 25 to a and prints 25
print(a := 6 + 7)      # assigns 13 to a and prints 13
print((a := 6) + 7)    # assigns 6 to a and prints 13
print(a)               # a is now 6

###################################################

# Analysis and Output:

a = 0
if a == 0:
    print('Hyd')           # a is 0 → prints 'Hyd'
else:
    print('Sec')

if b := 0:
    print('Hyd')           # b := 0 assigns 0 to b, 0 is False → goes to else
else:
    print('Sec :', b)      # prints 'Sec : 0'

if c = 0:
    print('Hyd')
else:
    print('Sec')

# ERROR:
# Line `if c = 0:`will raise:
# SyntaxError: cannot assign to comparison expression
# (because = is not allowed in condition, use == or :=) 

#######################################################################

# Program to determine average of inputs terminated with Ctrl + Z (without walrus operator)

total = 0
count = 0

try:
    while True:
        x = eval(input("Enter value: "))
        total += x
        count += 1
except EOFError:
    if count > 0:
        avg = total / count
        print("Sum =", total)
        print("Count =", count)
        print("Average =", avg)
    else:
        print("No inputs were given.")

##############################################################################

# Program to compute average of inputs terminated with Ctrl + Z (without walrus operator)

total = 0
count = 0

try:
    while True:
        x = eval(input("Enter input (ctrl + z to stop) : "))
        total += x
        count += 1
except EOFError:
    if count > 0:
        print("Average :", total / count)
    else:
        print("No inputs provided.")

#########################################################################

# del operator demo program

a = 25
print(a)      # Output: 25

del a         # Deletes the variable 'a'

print(a)      # Error: NameError: name 'a' is not defined

############################################################################

# Program Execution

a = b = c = 25         # All three point to the same value
print(a, b, c)         # Output: 25 25 25

del a
print(b, c)            # Output: 25 25

print(a)               # NameError: name 'a' is not defined

# The below lines will not execute due to the above error unless handled with try-except
# If continued forcefully:

del b
print(c)               # Output: 25

print(b)               # NameError: name 'b' is not defined

del c
print(c)               # NameError: name 'c' is not defined

#############################################################################

# Can multiple objects be deleted with the same del operator?

a, b, c = 25, 10.8, 'Hyd'
print(a, b, c)          # Output: 25 10.8 Hyd

del a, b, c             # Deletes all three variables

print(a)                # NameError: name 'a' is not defined
print(b)                # NameError: name 'b' is not defined
print(c)                # NameError: name 'c' is not defined

######################################################################################

# Program and Output

a = (10, 20, 15, 18)
print(a)          # Output: (10, 20, 15, 18)
print(a[0])       # Output: 10

del a[2]          # TypeError: 'tuple' object doesn't support item deletion

# Because of the above error, the following lines will NOT be executed:
# del a
# print(a)
# print(a[0]) 

  
