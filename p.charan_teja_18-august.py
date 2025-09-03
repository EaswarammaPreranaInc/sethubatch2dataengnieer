1.
a = \[25, 10.8, 'Hyd', True]

print(len(a))   # 4

b = \[]

print(len(b))   # 0

c = \[\[10, 20], 30, 40]

print(len(c))   # 3




2.
a = \[25, 10.8, True]

print(sum(a))  # 36.8  (True acts as 1)

b = \[3 + 4j, 5 + 6j]

print(sum(b))  # (8+10j)

c = \[25, 10.8, True, 3+4j, False]

print(sum(c))  # 39.8+4j

d = \[10, 20, 15, 18]

print(sum(d))  # 63

sum(\[25, 10.8, 'Hyd', True]) → error (string mixed with numeric types).








3.

a = \[\[10, 20, 15, 18]]

print(sum(a))   # Error ("unsupported operand type")

a = \[\[10, 20, 15, 18]]

print(sum(a\[0]))          # Method 1 → 63

print(sum(\[\*a]))       # Method 2 → 63








4.
a = \[10, 20, 15, 18, 30, 5, 12]

print(max(a))   # 30

print(min(a))   # 5

b = \['Rama', 'Sita', 'Rajesh', 'Kiran', 'Amar']

print(max(b))   # 'Sita'  (lexicographically)

print(min(b))   # 'Amar'

Mixing numbers and strings (\[25, '35']) raises error.

max(\[]) / min(\[]) → ValueError: empty sequence










5.
a = (10, 20, 15, 18)

b = list(a)

print(b, type(b))   # \[10, 20, 15, 18] <class 'list'>

print(a is b)       # False (different objects)

print(a == b)       # True (same contents)

list('Vamsi')   # \['V', 'a', 'm', 's', 'i']

list()          # \[]

list(25)        # Error (int is not iterable)







6.
a = \[10, 20, 15, 5, 12]

b = sorted(a)

print(b)         # \[5,10,12,15,20]

print(a)         # original remains unchanged
c = sorted(a, reverse=True)

print(c)         # \[20,15,12,10,5]

Works only on compatible data types (e.g. not \[25, 10.8, 'Hyd']).








7.
a = \[12 > 10, 5 < 20, 30 == 30]

print(all(a))   # True

b = \[9 >= 6, 12 <= 9, 6 == 6]

print(all(b))   # False

c = \[25, 10.8, '', True, 3+4j, 'Hyd']

print(all(c))   # False   ('' is False)

d = \[0, 0.0, '', False]

print(any(d))   # False








8.
a = \[10, 20, 15, 18]

del a   # removes element at index 2

print(a)   # \[10,20,18]

del a      # deletes entire variable

print(a)   #  NameError








9.
lst = \[]

for x in range(0, 50, 10):

    lst.append(x)

print(lst)   # \[0, 10, 20, 30, 40]








10.
a = \[10, 20, 30]

a.append("Hyd")

print(a\[3])       # 'Hyd'          (4th element)

print(a)    # 'H'

print(a)    # 'y'

print(a)    # 'd'










11.
lst = \[10, 20, 15, 18, 15, 12, 15, 19]

lst.remove(15)          # removes \*\*first\*\* 15

print(lst)

\# Remove all occurrences of 15

 	while 15 in lst:

 		lst.remove(15)

print(lst)








12.
a = \[10, 20, 15, 18, 19, 15, 17, 20, 15, 14]

x = 15

output:

\[10, 20, 18, 19, 17, 20, 14]










13.
lst = \[10, 20, 15, 18]

lst.clear()

print(lst)   # \[]










14.
a = \[10, 20, 15, 18]

a.reverse()

print(a)   # \[18,15,20,10]










15.
a = \[10, 20, 15, 18, 5]

a.sort()

print(a)    # \[5,10,15,18,20]

a.sort(reverse=True)

print(a)    # \[20,18,15,10,5]

 Mixed types (int + str) → Error.








16.
a = \[10, 20, 15, 18, 15, 12, 14, 15, 19]

print(a.count(15))   # 3

print(a.count(25))   # 0








17.
a = \[10,20,15,10,14,10,18,20,19]

b = \[]

for x in a:

    if a.count(x) == 1:   # keep only unique values

        b.append(x)

print(b)   # \[15,14,18,19]








18.
a = \[25,25,25,25]

if a.count(a\[0]) == len(a):

    print("All elements identical")

else:

    print("Not identical")

