1.
a = \[\[10, 'Rama', 1000.0], \[20, 'Sita', 2000.0], \[15, 'Rajesh', 3500.0], \[18, 'Kiran', 2800.0], \[5, 'Amar', 5000.0]]

print(sorted(a))

print(sorted(a, reverse=True))

print(a)


Output:
text
\[\[5, 'Amar', 5000.0], \[10, 'Rama', 1000.0], \[15, 'Rajesh', 3500.0], \[18, 'Kiran', 2800.0], \[20, 'Sita', 2000.0]]

\[\[20, 'Sita', 2000.0], \[18, 'Kiran', 2800.0], \[15, 'Rajesh', 3500.0], \[10, 'Rama', 1000.0], \[5, 'Amar', 5000.0]]

\[\[10, 'Rama', 1000.0], \[20, 'Sita', 2000.0], \[15, 'Rajesh', 3500.0], \[18, 'Kiran', 2800.0], \[5, 'Amar', 5000.0]]










2.
\# Program to create a list with cubes of 2, 4, 6, 8, 10 using list comprehension
\# Given numbers
numbers = \[2, 4, 6, 8, 10]

\# Using list comprehension to find cubes

cubes = \[num\*\*3 for num in numbers]

\# Print the result

print("Cubes of 2, 4, 6, 8, 10 are:", cubes)



3.
\# Without comprehension

strings = \['hyd', 'pune', 'chennai', 'vijayawada']

result = \[]

for s in strings:

&nbsp;   result.append(s\[0].upper())

print(result)   # \['H', 'P', 'C', 'V']

&nbsp;Output: \['H', 'P', 'C', 'V']




4.
With comprehension:

python

strings = \['hyd', 'pune', 'chennai', 'vijayawada']

result = \[s.upper() for s in strings]

print(result)   # \['H', 'P', 'C', 'V']

sentence = "hyd is green city"

words = sentence.split()

result = \[]

for w in words:

&nbsp;   result.append(\[w.upper(), len(w)])

print(result)

Output: \[\['HYD', 3], \['IS', 2], \['GREEN', 5], \['CITY', 4]]





5.
With comprehension

python

sentence = "hyd is green city"

result = \[\[w.upper(), len(w)] for w in sentence.split()]

print(result)



\# Without comprehension

a = \[10, 20, 30, 40, 50, 60, 70]

b = \[100, 200, 300, 400]

result = \[]

for i in range(len(b)):   # only till length of smaller list

&nbsp;   result.append(a\[i] + b\[i])

print(result)   # \[110, 220, 330, 440]







6.
With comprehension

python

a = \[10, 20, 30, 40, 50, 60, 70]

b = \[100, 200, 300, 400]



result = \[a\[i] + b\[i] for i in range(len(b))]

print(result)   # \[110, 220, 330, 440]


\# Without comprehension

rows, cols = 3, 4

result = \[]

for i in range(rows):

&nbsp;   result.append(\[0] \* cols)

print(result)

&nbsp;
Output: \[\[0,0,0,




7.
With comprehension

python

rows, cols = 3, 4

result = \[ \* cols for i in range(rows)]

print(result)







8.
a = [10, 20, 15, 18, 25, 32]
b = [30, 40, 10, 25, 15]

# Without comprehension
result = []
for x in a:
    if x not in b:
        result.append(x)
print(result)  # [20, 18, 32]
With comprehension
python
result = [x for x in a if x not in b]
print(result)  # [20, 18, 32]





9.
evens = [x for x in range(2, 21, 2)]
print(evens)
Output: `[2, 4, 6, 8, 10, 12, 14, 16, 18, because of step size 2)




10.
squares = [x**2 for x in range(1, 21) if (x**2) % 2 == 0]
print(squares)
 Output: `[4, 16, 36, 64, 100, 144, 196, 256,
squares = [(x*2)**2 for x in range(1, 11)]
print(squares)








11.
 Add each element of list1 with **all elements of list2**
```python
a = [10, 20, 15]
b = [30, 40, 35, 32]

# Without comprehension
result = []
for i in a:
    for j in b:
        result.append(i + j)
print(result)
Output: `[40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, comprehension
python
result = [i + j for i in a for j in b]
print(result)



12.
 Concatenate characters of 2 strings
python
a = "HYD"
b = "PUNE"
result = [x + y for x in a for y in b]
print(result)
Output: ['HP', 'HU', 'HN', 'HE', 'YP', 'YU', 'YN', 'YE', 'DP', 'DU', 'DN', 'DE']





13.
 Flatten nested list
python
a = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
result = [y for x in a for y in x]
print(result)
Output: `[10, 20, 30, 40, 50, 





14.
Group by first letter of string

python
words = ['Swathi', 'Anand', 'Srinivas', 'Zebra', 'King', 'Amar']

result = []
used = set()

for w in words:
    if w not in used:
        group = [x for x in words if x == w]
        result.append(group)
        used.add(w)
print(result)
Output: [['Swathi', 'Srinivas'], ['Anand', 'Amar'], ['Zebra'], ['King']]




15.
Merge 2 sorted lists
python
a = [10, 20, 30, 40, 50]
b = [5, 12, 20, 37]
c = []

i = j = 0
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

# Add remaining
c.extend(a[i:])
c.extend(b[j:])

print(c)
Output: `[5, 10, 12, 20, 20, 





16.
 n-th largest element

python
arr = [10,20,30,25,40,35,12,5]
n = 3   # 3rd largest
arr.sort(reverse=True)
print(arr[n-1])   # 30

