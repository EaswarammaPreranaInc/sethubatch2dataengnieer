#name: TARUN BANALA          04-08-2025

# Find outputs (Homework)
for i in range(1, 8):  # Loop from 1 to 7
    print(i)  # Prints current i value
    if i % 3 == 0:  # When i is divisible by 3 (3, 6)
        continue  # Skips rest of loop iteration
    else:  # For other numbers
        print('Sec')  # Prints 'Sec'
    print('Hello')  # Prints 'Hello' (except when continue executes)
# End of loop
print('Outside loop')  # Prints after loop completes

# Identify Error (Homework)
if ():  # Empty tuple is falsy, block won't execute
    print('Hyd')  # Never executes
    continue  # Error Due to continue outside loop
    print('Sec')  # Never executes

# Find outputs (Homework)
for i in range(1, 8):  # Loop from 1 to 7
    print(i)  # Prints current i value
    if i % 3 == 0:  # When i is divisible by 3 (3, 6)
        break  # Exits loop completely at i=3
    else:  # For other numbers
        print('Sec')  # Prints 'Sec'
    print('Hello')  # Prints 'Hello' (until break)
# End of the loop
print('Outside loop')  # Prints after loop exits

# Identify Error (Homework)
if (10, 20, 30):  # Non-empty tuple is truthy
    print('Hyd')  # Prints 'Hyd'
    break  # Error Due to break outside loop
    print('Sec')  # Never executes

# Find outputs (Homework)
for i in range(1, 8):  # Loop from 1 to 7
    print(i)  # Prints current i value
    if i % 3 == 0:  # When i is divisible by 3 (3, 6)
        pass  # Does nothing
        print('Hyd')  # Prints 'Hyd'
    else:  # For other numbers
        print('Sec')  # Prints 'Sec'
    print('Hello')  # Always prints 'Hello'
# End of the loop
print('Outside loop')  # Prints after loop completes

# Find outputs (Homework)
for i in range(1, 8):  # Loop from 1 to 7
    print(i)  # Prints current i value
    if i % 3 == 0:  # When i is divisible by 3 (3, 6)
        exit()  # Terminates program at i=3
    else:  # For other numbers
        print('Sec')  # Only executes for i=1,2
    print('Hello')  # Only executes for i=1,2
# End of the loop (never reached)
print('Outside loop')  # Never executes

# Find outputs (Homework)
for i in range(1, 8):  # Loop from 1 to 7
    print(i)  # Prints current i value
    if i % 3 == 0:  # When i is divisible by 3 (3, 6)
        continue  # Skips rest of iteration
    else:  # For other numbers
        print('Sec')  # Prints 'Sec'
    print('Hello')  # Prints 'Hello' (except when continue executes)
else:  # Loop else clause
    print('else suite')  # Executes after normal loop completion
# End of the loop
print('Outside loop')  # Prints after all completes

# Find outputs (Homework)
for i in range(1, 8):  # Loop from 1 to 7
    print(i)  # Prints current i value
    if i % 3 == 0:  # When i is divisible by 3 (3, 6)
        break  # Exits loop at i=3
    else:  # For other numbers
        print('Sec')  # Prints 'Sec'
    print('Hello')  # Prints 'Hello' (until break)
else:  # Loop else clause
    print('else suite')  # Doesn't execute (break used)
#End of the loop
print('Outside loop')  # Prints after loop exits

# Find outputs (Homework)
for i in range(1, 8):  # Loop from 1 to 7
    print(i)  # Prints current i value
    if i == 8:  # Never true (range ends at 7)
        break  # Never executes
    else:  # Always executes
        print('Sec')  # Prints 'Sec' each iteration
    print('Hello')  # Prints 'Hello' each iteration
else:  # Loop else clause
    print('else suite')  # Executes after normal loop completion
# End of the loop
print('Outside loop')  # Prints after all completes

# Walrus operator demo program
print(a := 25)  # Assigns and prints 25
print(a = 25)  # Error Due to invalid syntax (assignment in print)
print(a)  # Prints 25
print(a := 6 + 7)  # Assigns and prints 13
print(a)  # Prints 13
print((a := 6) + 7)  # Assigns 6, prints 13 (6+7)
print(a)  # Prints 6
print((a = 6) + 7)  # Error Due to invalid syntax

# Find outputs (Homework)
a = 0  # Assigns 0 to a
if a == 0:  # True
    print('Hyd')  # Prints 'Hyd'
else:  # Not executed
    print('Sec')  # Not executed
if b := 0:  # Assigns 0 to b, condition is False
    print('Hyd')  # Not executed
else:  # Executed
    print('Sec : ', b)  # Prints 'Sec : 0'
if c = 0:  # Error Due to invalid syntax (assignment in if)
    print('Hyd')  # Not executed
else:  # Not executed
    print('Sec')  # Not executed

# del operator demo program (Homework)
a = 25  # Creates variable a
print(a)  # Prints 25
del a  # Deletes a
print(a)  # Error Due to name 'a' is not defined

# Find outputs (Homework)
a = b = c = 25  # Creates 3 variables
print(a, b, c)  # Prints 25 25 25
del a  # Deletes a
print(b, c)  # Prints 25 25
print(a)  # Error Due to name 'a' is not defined
del b  # Deletes b
print(c)  # Prints 25
print(b)  # Error Due to name 'b' is not defined
del c  # Deletes c
print(c)  # Error Due to name 'c' is not defined

# Multiple objects deletion
a, b, c = 25, 10.8, 'Hyd'  # Creates 3 variables
print(a, b, c)  # Prints 25 10.8 'Hyd'
del a, b, c  # Deletes all three
print(a)  # Error Due to name 'a' is not defined
print(b)  # Error Due to name 'b' is not defined
print(c)  # Error Due to name 'c' is not defined

# Find outputs (Homework)
a = [10, 20, 15, 18]  # Creates list
print(a)  # Prints [10, 20, 15, 18]
del a[2]  # Deletes element at index 2
print(a)  # Prints [10, 20, 18]
del a  # Deletes entire list
print(a)  # Error Due to name 'a' is not defined
print(a[0])  # Error Due to name 'a' is not defined

# Find outputs (Homework)
a = (10, 20, 15, 18)  # Creates tuple
print(a)  # Prints (10, 20, 15, 18)
print(a[0])  # Prints 10
del a[2]  # Error Due to can't delete tuple elements
del a  # Deletes entire tuple
print(a)  # Error Due to name 'a' is not defined
print(a[0])  # Error Due to name 'a' is not defined
