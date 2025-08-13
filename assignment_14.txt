# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')
output:-
---------
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
--------------------------------------


# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec') # Syntax Error
--------------------------

# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

output:-
---------
1
Sec
Hello
2
Sec
Hello
3
Outside loop
--------------------------------

# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')  # Condition Invalid
--------------------------------------

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
print('Outside loop')

output:-
---------
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
-----------------------------

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')
 
output:-
---------
1
Sec
Hello
2
Sec
Hello
3
---------------------------------------------

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
print('Outside  loop')

output:-
----------  
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
Outside loop
----------------------

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
print('Outside  loop')

output:-
----------
1
Sec
Hello
2
Sec
Hello
3
Outside loop
------------------------------------

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
print('Outside loop')

output:-
---------
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
------------------------------

# Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

Program:-
------------
def search_element(element, lst):
    found = False  # Flag to indicate if the element is found
    for item in lst:
        if item == element:
            found = True  # Set the flag to True if the element is found
            break  # Exit the loop since we found the element
    if found:
        print("Found")
    else:
        print("Not Found")

-----------------------------------------------------

# Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found (Assume  that  list  may  contain  duplicate  elements)

Program:-
------------
def search_element(element, lst):
    indices = []  # List to store indices where the element is found
    for index, item in enumerate(lst):
        if item == element:
            indices.append(index)  
    if indices:
        for index in indices:
            print(f"{element} is found at index {index}")
        print(f"{element} is found {len(indices)} times")
    else:
        print(f"{element} is not found in the list")
----------------------------------------------------

# Walrus operator (:=) demo program

print(a := 25)          # Assigns 25 to a and prints it
print(a)                # Prints the value of a (25)
 print(a = 25)         # Incorrect usage, will raise an error

print(a := 6 + 7)      # Assigns the result of 6 + 7 (13) to a and prints it
print(a)                # Prints the value of a (13)

print((a := 6) + 7)    # Assigns 6 to a and then adds 7, printing the result (13)
print(a)                # Prints the value of a (6)
 print((a = 6) + 7)    # Incorrect usage, will raise an error
------------------------------------------------

# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd') # Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)  # Sec : 0
if  c = 0:
	print('Hyd')
else:
	print('Sec') # Syntax Error
-------------------------------------
# Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Program:-
----------
print("Enter numbers  (press Ctrl + Z to stop):")

total = 0
count = 0

try:
    while True:
        num = int(input())
        total += num
        count += 1
except EOFError:
    if count == 0:
        print("No numbers entered.")
    else:
        average = total / count
        print("Average:", average)

-----------------------------------------------

#  del  operator  demo program  (Home  work)
a = 25
print(a) # 25
del   a
print(a) # error
--------------------------------
# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) # 25 25 25
del   a
print(b , c) # 25 25
print(a) # error
del   b
print(c) # 25
print(b) # error
del   c
print(c) # error
-------------------------------------------------
#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25  10.8  Hyd
del   a , b , c
print(a) # error
print(b) # error
print(c)# error
-----------------------------------
# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10,20,15,18]
del  a[2] 
print(a) [10,20,18]
del  a 
print(a) # error
print(a[0]) # error
----------------------------------
# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a) # (10,20,15,18)
print(a[0]) # 10
del  a[2] # error
del  a
print(a) # error
print(a[0]) # error































