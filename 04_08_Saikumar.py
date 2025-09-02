# Find  outputs  (Home  work)

for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')

'''
Output: 

1
Sec
Hello
2
Sec
Hello
3
4
Sec
Hello
5
Sec
Hello
6
7
Sec
Hello
Outside loop
'''

# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec')

# Error: because the if condition is empty, and the continue statement is used outside of a loop.


# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

'''
Output: 

1
Sec
Hello
2
Sec
Hello
3
Outside loop
'''


# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')

# Error: break used outside of a loop


# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass
		print('Hyd')
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

'''
Output: 

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
'''


# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

'''
Output: 

1
Sec
Hello
2
Sec
Hello
3

Program stops at i = 3 — no "Hyd" or "Outside loop" printed.

'''


# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if   i % 3 == 0:
		continue
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside  loop')

'''
Output:

1
Sec
Hello
2
Sec
Hello
3
4
Sec
Hello
5
Sec
Hello
6
7
Sec
Hello
else suite
Outside  loop
'''


# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if  i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
#End   of  the  loop
print('Outside  loop')

'''
Output:

1
Sec
Hello
2
Sec
Hello
3
Outside  loop
'''


# Find  outputs  (Home  work)

for  i  in  range(1 , 8):
	print(i)
	if  i == 8:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside loop')

'''
Output:

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
else suite
Outside loop
'''


#  Walrus   operator (:=)  demo  program

print(a := 25)         # valid assigns 25 to a and prints it
print(a = 25)          # ERROR: invalid syntax 
print(a)               # valid if line above didn't error
print(a := 6 + 7)      # assigns 13 to a and prints
print(a)               # prints 13
print((a := 6) + 7)    # assigns 6 to a, then adds 7 → prints 13
print(a)               # prints 6
print((a = 6) + 7)     # ERROR: '=' not allowed in expression must use ':='


# Find  outputs  (Home  work)

a = 0
if a == 0:
    print('Hyd')              # Output: Hyd
else:
    print('Sec')

if b := 0:
    print('Hyd')
else:
    print('Sec :', b)         # Output: Sec : 0

if c = 0:                     # Error Object is assigned to the reference c
    print('Hyd')
else:
    print('Sec')


#  del  operator  demo program  (Home  work)

a = 25
print(a)       # Output: 25
del a
print(a)       # Error because a is deleted


# Find  outputs  (Home  work)

a = b = c = 25
print(a, b, c)     # Output: 25 25 25
del a
print(b, c)        # Output: 25 25
print(a)           # Error because a is deleted
del b
print(c)           # Output: 25
print(b)           # Error because b is deleted
del c
print(c)           # Error because c is deleted

#  Can  multiple  objects  be  deleted  with  same  del  operator ?

a, b, c = 25, 10.8, 'Hyd'
print(a, b, c)      # Output: 25 10.8 Hyd
del a, b, c
print(a)            # Error because a is deleted
print(b)            # Error because b is deleted
print(c)            # Error because c is deleted


# Find outputs  (Home  work)

a = [10, 20, 15, 18]
print(a)            # Output: [10, 20, 15, 18]
del a[2]
print(a)            # Output: [10, 20, 18]
del a
print(a)            # Error because a is deleted
print(a[0])         # Error a doesn't exist

# Find outputs  (Home work)

a = (10, 20, 15, 18)
print(a)            # Output: (10, 20, 15, 18)
print(a[0])         # Output: 10
del a[2]            # Error tuples are immutable
del a
print(a)            # Error because a is deleted
print(a[0])         # Error because a is deleted


# Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

lst = eval(input("Enter any list: "))
x = eval(input("Enter the element to be searched: "))
found = False

for i in range(len(lst)):
    if lst[i] == x:
        print("Found at index:", i)
        found = True
        break

if not found:
    print("Not Found")


# Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element and  also  number  of  times  it  is  found (Assume  that  list  may  contain  duplicate  elements)

lst = eval(input("Enter the list: "))
x = eval(input("Enter the element to be searched: "))
count = 0

for i in range(len(lst)):
    if lst[i] == x:
        print(x, "is found at index", i)
        count += 1

if count > 0:
    print(x, "is found", count, "times")
else:
    print(x, "is not found")


#  Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z (without  walrus  operator)

total = 0
count = 0

try:
    while True:
        val = input("Enter input (ctrl + z to stop): ")
        total += eval(val)
        count += 1
except EOFError:
    pass

if count > 0:
    print("Average:", total / count)
else:
    print("No inputs provided.")


