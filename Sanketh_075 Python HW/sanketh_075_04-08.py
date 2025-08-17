 Find outputs - continue
for i in range(1, 8):
    print(i)
    if i % 3 == 0:
        continue
    else:
        print('Sec')
    print('Hello')
print('Outside loop')

# 2. Identify Error - continue outside loop
# Error: 'continue' outside loop and empty if condition
# if ():
#     print('Hyd')
#     continue
#     print('Sec')
# Output: SyntaxError

# 3. Find outputs - break
for i in range(1, 8):
    print(i)
    if i % 3 == 0:
        break
    else:
        print('Sec')
    print('Hello')
print('Outside loop')

# 4. Identify Error - break outside loop
# Error: 'break' outside loop and tuple in if
# if (10, 20, 30):
#     print('Hyd')
#     break
#     print('Sec')
# Output: SyntaxError

# 5. Find outputs - pass
for i in range(1, 8):
    print(i)
    if i % 3 == 0:
        pass
        print('Hyd')
    else:
        print('Sec')
    print('Hello')
print('Outside loop')

# 6. Find outputs - exit()
for i in range(1, 8):
    print(i)
    if i % 3 == 0:
        exit()
    else:
        print('Sec')
    print('Hello')
print('Outside loop')

# 7. Find outputs - continue with else suite
for i in range(1, 8):
    print(i)
    if i % 3 == 0:
        continue
    else:
        print('Sec')
    print('Hello')
else:
    print('else suite')
print('Outside loop')

# 8. Find outputs - break with else suite
for i in range(1, 8):
    print(i)
    if i % 3 == 0:
        break
    else:
        print('Sec')
    print('Hello')
else:
    print('else suite')
print('Outside loop')

# 9. Find outputs - i == 8 never true
for i in range(1, 8):
    print(i)
    if i == 8:
        break
    else:
        print('Sec')
    print('Hello')
else:
    print('else suite')
print('Outside loop')

# 10. Search element in list without using 'in'
lst = [10, 20, 15, 12, 18]
x = int(input("Enter element to search: "))
found = False
for i in range(len(lst)):
    if lst[i] == x:
        print("Found at index:", i)
        found = True
        break
if not found:
    print("Not found")

# 11. Search for all occurrences and count
lst = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]
x = int(input("Enter element to search: "))
count = 0
for i in range(len(lst)):
    if lst[i] == x:
        print(f"{x} is found at index {i}")
        count += 1
print(f"{x} is found {count} times")

# 12. Walrus operator demo
print(a := 25)
# print(a = 25) # SyntaxError
print(a)
print(a := 6 + 7)
print(a)
print((a := 6) + 7)
print(a)
# print((a = 6) + 7) # SyntaxError

# 13. Walrus operator in if and error
a = 0
if a == 0:
    print('Hyd')
else:
    print('Sec')
if (b := 0):
    print('Hyd')
else:
    print('Sec :', b)
# if (c = 0): # SyntaxError
#     print('Hyd')
# else:
#     print('Sec')

# 14. Average inputs until Ctrl+Z
total = 0
count = 0
try:
    while True:
        val = input("Enter input (Ctrl+Z to stop): ")
        total += eval(val)
        count += 1
except EOFError:
    pass
print("Average:", total / count)

# 15. del operator demo
a = 25
print(a)
del a
# print(a) # NameError

# 16. Multiple delete and errors
a = b = c = 25
print(a, b, c)
del a
print(b, c)
# print(a) # NameError
del b
print(c)
# print(b) # NameError
del c
# print(c) # NameError

# 17. Multiple del
a, b, c = 25, 10.8, 'Hyd'
print(a, b, c)
del a, b, c
# print(a) # NameError
# print(b) # NameError
# print(c) # NameError

# 18. Delete list index and list
a = [10, 20, 15, 18]
print(a)
del a[2]
print(a)
del a
# print(a) # NameError
# print(a[0]) # NameError

# 19. Delete tuple index and tuple
a = (10, 20, 15, 18)
print(a)
print(a[0])
# del a[2] # TypeError
del a
# print(a) # NameError
# print(a[0]) # NameError


try:
    sum = ctr = 0
    while True:
        if (x := eval(input('Enter input (ctrl + z to stop) : ')) is not None):
            sum += x
            ctr += 1
except EOFError:
    try:
        print(f'Average : {sum / ctr}')
    except ZeroDivisionError:
        print('Enter at least one input')
except (NameError, TypeError):
    print('Input cannot be string')
