1.
a = \[10,20,15,12,14,15,18,19,15,12,25]

i = a.index(15)   # first occurrence

while True:

    print(i)

    try:

        i = a.index(15, i+1)  # next occurrence after index i

    except:

        print(f"15 is found {a.count(15)} times")

        break










2.
a = \[10, 20, 15, 12, 14, 15, 18, 19, 15, 12, 25]
try:

    i = -1   # start before the beginning

    while (i := a.index(15, i + 1)) is not None:

        print(i)

except ValueError:

    print(f'15 is found {a.count(15)} times')










3.
def is\_sublist(l1, l2):

    try:

        start = 0

        for elem in l1:

            start = l2.index(elem, start) + 1

        return True

    except ValueError:

        return False

\# Test cases

print(is\_sublist(\[10, 20, 30], \[15, 18, 10, 12, 19, 20, 14, 12, 30, 25, 16]))  # True

print(is\_sublist(\[10, 20, 20], \[15, 18, 10, 12, 19, 20, 14, 12, 30, 25, 16]))  # False

print(is\_sublist(\[2, 2, 5], \[2, 2, 3, 4, 5]))  # True

print(is\_sublist(\[2, 4, 3], \[2, 2, 3, 4, 5]))  # False








4.
\# Program to check if the first list is a sublist (subsequence) of the second list

\# Reading the lists from user input

l1 = eval(input("Enter the first list : "))

l2 = eval(input("Enter the second list : "))
try:

    start = 0

    for elem in l1:

        start = l2.index(elem, start) + 1

    print(True)

except ValueError:

    print(False)








5.
a = \[10, 20, 15, 18]

b = a.copy()        # copy() method returns a new list with same elements

print(b)            # \[10, 20, 15, 18]

print(a is b)       # False (b is a different list, not the same object as a)

print(a == b)       # True  (b has the same elements as a)

c = a\[:]            # Another way to copy list elements to a new list (list slicing)

print(c)            # \[10, 20, 15, 18]

print(a is c)       # False (c is also a new list, not the same object as a)

print(a == c)       # True  (c has the same elements as a)

d = a               # This does not copy the list; both d and a refer to the same object

print(d)            # \[10, 20, 15, 18]

print(a is d)       # True  (d is exactly the same object as a)

print(a == d)       # True  (d has the same elements, because it is a)












6.
\# Read input list from user

lst = eval(input("Enter List : "))

\# Convert list to set to get unique elements

unique\_elements = set(lst)

mode = None

max\_count = 0

\# Iterate over each unique element and count its occurrences in the list

for elem in unique\_elements:

    count = lst.count(elem)

    # Check if this element has a higher count than current max\_count

    if count > max\_count:

        mode = elem

        max\_count = count

print("Mode : ", mode)








7.
\# Nested List example

a = \[\[10, 20, 30, 40], \[50, 60, 70, 80], \[90, 100, 110, 120]]

print(a)          # Prints the entire nested list

print(len(a))     # Prints the number of inner lists, which is 3

\# How to print 1st inner list
print(a\[0])       # \[10, 20, 30, 40]

\# How to print 2nd inner list

print(a\[1])       # \[50, 60, 70, 80]

\# How to print 3rd inner list

print(a\[2])       # \[90, 100, 110, 120]

\# How to print 30 (3rd element of 1st inner list)

print(a\[2])    # 30

\# How to print 80 (4th element of 2nd inner list)

print(a\[1]\[3])    # 80

\# How to print 100 (2nd element of 3rd inner list)

print(a\[2]\[1])    # 100

'''

What is a nested list?

---> A list inside another list

'''







8.
a = \[\[10, 20], \[30, 40, 50], \[60, 70, 80, 90]]

\# How to print 1st inner list

print(a\[0])  # Output: \[10, 20]

\# How to print 2nd inner list

print(a\[1])  # Output: \[30, 40, 50]

\# How to print 3rd inner list

print(a\[3])  # Output: \[60, 70, 80, 90]

\# How to print number of elements in 1st inner list

print(len(a\[0]))  # Output: 2

\# How to print number of elements in 2nd inner list

print(len(a\[1]))  # Output: 3

\# How to print number of elements in 3rd inner list

print(len(a\[3]))  # Output: 4







9.
a = \[\[10, 20], \[30, 40, 50], \[60, 70, 80, 90]]

print('Nested list with print function')

print(a)   # Prints the whole nested list as it is

print('Each inner list of outer list without indexes')

\# Using for loop to print each inner list without indexes

for inner\_list in a:

    print(inner\_list)

print('Elements in the form of matrix without using indexes')

\# Nested loop to print elements in matrix style without indexes

for inner\_list in a:

    for elem in inner\_list:

        print(elem, end='\\t')  # Print elements separated by tab

    print()  # New line after each inner list

print('Elements in the form of matrix using indexes')

\# Nested loop with indexes to print elements in matrix style

for i in range(len(a)):

    for j in range(len(a\[i])):

        print(a\[i]\[j], end='\\t')

    print()  # New line after each inner list










10.
a = \[\[10, 20], \[30, 40, 50], \[60, 70, 80, 90]]

print('Nested list with print function')

print(a)  # Prints the whole nested list

print('Each inner list of outer list without indexes')

for inner\_list in a:

    print(inner\_list)  # Prints each inner list directly

print('Elements in the form of matrix without using indexes')

for inner\_list in a:

    for elem in inner\_list:

        print(elem, end='\\t')  # Print elements with tab spacing

    print()  # New line after each inner list

print('Elements in the form of matrix using indexes')

for i in range(len(a)):

    for j in range(len(a\[i])):

        print(a\[i]\[j], end='\\t')  # Access by indexes and print

    print()  # New line after each inner list

output:

Nested list with print function

\[\[10, 20], \[30, 40, 50], \[60, 70, 80, 90]]

Each inner list of outer list without indexes

\[10, 20]

\[30, 40, 50]

\[60, 70, 80, 90]

Elements in the form of matrix without using indexes

10      20

30      40      50

60      70      80      90

Elements in the form of matrix using indexes

10      20

30      40      50

60      70      80      90









11.
a = \[\[10, 20, 30], \[40, 50, 60], \[70, 80, 90]]

for x in a:

    print(x)

print()

for x, y, z in a:

    print(x, y, z, sep='...')

output:

\[10, 20, 30]

\[40, 50, 60]

\[70, 80, 90]


10...20...30

40...50...60

70...80...90

