##1
# Program to create a list with cubes of 2, 4, 6, 8, 10 using list comprehension

numbers = [2, 4, 6, 8, 10]
cubes = [x**3 for x in numbers]

print("Cubes of 2, 4, 6, 8, 10 are:", cubes)

##2
# Program to extract 1st character of each string in capital letters without list comprehension

cities = ['hyd', 'pune', 'chennai', 'vijayawada']
result = []

for city in cities:
    result.append(city[0].upper())

print(result)

##3
# Program to extract 1st character of each string in capital letters using list comprehension

cities = ['hyd', 'pune', 'chennai', 'vijayawada']
result = [city[0].upper() for city in cities]

print(result)

##4
# Program to append each word of the sentence and its length to a list (without comprehension)

sentence = "hyd is green city"
words = sentence.split()
result = []

for w in words:
    result.append([w.upper(), len(w)])

print(result)

##5
# Program to append each word of the sentence and its length to a list (with comprehension)

sentence = "hyd is green city"
result = [[w.upper(), len(w)] for w in sentence.split()]

print(result)
##6
# Program to add two lists of unequal length without comprehension

list1 = [10, 20, 30, 40, 50, 60, 70]
list2 = [100, 200, 300, 400]

result = []
min_len = min(len(list1), len(list2))

for i in range(min_len):
    result.append(list1[i] + list2[i])

print(result)
##7
# Program to add two lists of unequal length with comprehension

list1 = [10, 20, 30, 40, 50, 60, 70]
list2 = [100, 200, 300, 400]

result = [list1[i] + list2[i] for i in range(min(len(list1), len(list2)))]

print(result)
##8
# Program to initialize a nested list with zeroes without comprehension

rows = 3
cols = 4
result = []

for i in range(rows):
    result.append([0] * cols)

print(result)
##9
# Program to initialize a nested list with zeroes using comprehension

rows = 3
cols = 4

result = [[0] * cols for _ in range(rows)]

print(result)
##10
# Program to extract elements of 1st list not in 2nd list (without comprehension)

list1 = [10, 20, 15, 18, 25, 32]
list2 = [30, 40, 10, 25, 15]

result = []

for x in list1:
    if x not in list2:
        result.append(x)

print(result)
##11
# Program to extract elements of 1st list not in 2nd list (with comprehension)

list1 = [10, 20, 15, 18, 25, 32]
list2 = [30, 40, 10, 25, 15]

result = [x for x in list1 if x not in list2]

print(result)
##12
# Program to print even numbers between 1 and 20 using comprehension

evens = [x for x in range(1, 21) if x % 2 == 0]

print(evens)
##13
# Program to print even numbers between 1 and 20 using comprehension (without if)

evens = [x for x in range(2, 21, 2)]

print(evens)
##14
# Program to print squares of 1..20 divisible by 2 using comprehension

squares = [x**2 for x in range(1, 21) if (x**2) % 2 == 0]

print(squares)
##15
# Program to print squares of 1..20 divisible by 2 using comprehension (without if)

squares = [x**2 for x in range(2, 21, 2)]

print(squares)
##16
# Program to add each element of 1st list with all elements of 2nd list (without comprehension)

list1 = [10, 20, 15]
list2 = [30, 40, 35, 32]

result = []

for x in list1:
    for y in list2:
        result.append(x + y)

print(result)
##17
# Program to add each element of 1st list with all elements of 2nd list (with comprehension)

list1 = [10, 20, 15]
list2 = [30, 40, 35, 32]

result = [x + y for x in list1 for y in list2]

print(result)
##18
# Program to concatenate each character of 1st string with every character of 2nd string (with comprehension)

str1 = "HYD"
str2 = "PUNE"

result = [ch1 + ch2 for ch1 in str1 for ch2 in str2]

print(result)
##19
# Program to convert a nested list to a flat list (without comprehension)

nested = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
flat = []

for sublist in nested:
    for item in sublist:
        flat.append(item)

print(flat)
##20
# Program to convert a nested list to a flat list using comprehension

nested = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
flat = [item for sublist in nested for item in sublist]

print(flat)
##21
# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)#[[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]
##22
#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)
#[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]

##23
# Tricky program: group names by first letter into nested lists

names = ['Swathi', 'Anand', 'Srinivas', 'Zebra', 'King', 'Amar']
c = []
visited = []

for name in names:
    first = name[0]   # first character
    if first not in visited:
        d = []
        for n in names:
            if n[0] == first:
                d.append(n)
        c.append(d)
        visited.append(first)

print(c)
##24
# Program to merge two sorted lists into another sorted list

a = [10, 20, 30, 40, 50]
b = [5, 12, 20, 37]
c = []

i, j = 0, 0   # pointers for a and b

# Merge while both lists have elements
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

# Add remaining elements from a (if any)
while i < len(a):
    c.append(a[i])
    i += 1

# Add remaining elements from b (if any)
while j < len(b):
    c.append(b[j])
    j += 1

print(c)

##25
# Program to find n-th largest element of a list

numbers = [10, 20, 30, 25, 40, 35, 12, 5]
n = 3   # 3rd largest

numbers.sort(reverse=True)  # sort in descending order
nth_largest = numbers[n-1]  # index is n-1

print(nth_largest)
##26
# Program to sort a list without using sorted() or sort()

nums = [10, 20, 30, 25, 40, 35, 12, 5]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            # swap
            nums[i], nums[j] = nums[j], nums[i]

print(nums)
=======
##1
# Program to create a list with cubes of 2, 4, 6, 8, 10 using list comprehension

numbers = [2, 4, 6, 8, 10]
cubes = [x**3 for x in numbers]

print("Cubes of 2, 4, 6, 8, 10 are:", cubes)

##2
# Program to extract 1st character of each string in capital letters without list comprehension

cities = ['hyd', 'pune', 'chennai', 'vijayawada']
result = []

for city in cities:
    result.append(city[0].upper())

print(result)

##3
# Program to extract 1st character of each string in capital letters using list comprehension

cities = ['hyd', 'pune', 'chennai', 'vijayawada']
result = [city[0].upper() for city in cities]

print(result)

##4
# Program to append each word of the sentence and its length to a list (without comprehension)

sentence = "hyd is green city"
words = sentence.split()
result = []

for w in words:
    result.append([w.upper(), len(w)])

print(result)

##5
# Program to append each word of the sentence and its length to a list (with comprehension)

sentence = "hyd is green city"
result = [[w.upper(), len(w)] for w in sentence.split()]

print(result)
##6
# Program to add two lists of unequal length without comprehension

list1 = [10, 20, 30, 40, 50, 60, 70]
list2 = [100, 200, 300, 400]

result = []
min_len = min(len(list1), len(list2))

for i in range(min_len):
    result.append(list1[i] + list2[i])

print(result)
##7
# Program to add two lists of unequal length with comprehension

list1 = [10, 20, 30, 40, 50, 60, 70]
list2 = [100, 200, 300, 400]

result = [list1[i] + list2[i] for i in range(min(len(list1), len(list2)))]

print(result)
##8
# Program to initialize a nested list with zeroes without comprehension

rows = 3
cols = 4
result = []

for i in range(rows):
    result.append([0] * cols)

print(result)
##9
# Program to initialize a nested list with zeroes using comprehension

rows = 3
cols = 4

result = [[0] * cols for _ in range(rows)]

print(result)
##10
# Program to extract elements of 1st list not in 2nd list (without comprehension)

list1 = [10, 20, 15, 18, 25, 32]
list2 = [30, 40, 10, 25, 15]

result = []

for x in list1:
    if x not in list2:
        result.append(x)

print(result)
##11
# Program to extract elements of 1st list not in 2nd list (with comprehension)

list1 = [10, 20, 15, 18, 25, 32]
list2 = [30, 40, 10, 25, 15]

result = [x for x in list1 if x not in list2]

print(result)
##12
# Program to print even numbers between 1 and 20 using comprehension

evens = [x for x in range(1, 21) if x % 2 == 0]

print(evens)
##13
# Program to print even numbers between 1 and 20 using comprehension (without if)

evens = [x for x in range(2, 21, 2)]

print(evens)
##14
# Program to print squares of 1..20 divisible by 2 using comprehension

squares = [x**2 for x in range(1, 21) if (x**2) % 2 == 0]

print(squares)
##15
# Program to print squares of 1..20 divisible by 2 using comprehension (without if)

squares = [x**2 for x in range(2, 21, 2)]

print(squares)
##16
# Program to add each element of 1st list with all elements of 2nd list (without comprehension)

list1 = [10, 20, 15]
list2 = [30, 40, 35, 32]

result = []

for x in list1:
    for y in list2:
        result.append(x + y)

print(result)
##17
# Program to add each element of 1st list with all elements of 2nd list (with comprehension)

list1 = [10, 20, 15]
list2 = [30, 40, 35, 32]

result = [x + y for x in list1 for y in list2]

print(result)
##18
# Program to concatenate each character of 1st string with every character of 2nd string (with comprehension)

str1 = "HYD"
str2 = "PUNE"

result = [ch1 + ch2 for ch1 in str1 for ch2 in str2]

print(result)
##19
# Program to convert a nested list to a flat list (without comprehension)

nested = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
flat = []

for sublist in nested:
    for item in sublist:
        flat.append(item)

print(flat)
##20
# Program to convert a nested list to a flat list using comprehension

nested = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
flat = [item for sublist in nested for item in sublist]

print(flat)
##21
# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)#[[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]
##22
#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)
#[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]

##23
# Tricky program: group names by first letter into nested lists

names = ['Swathi', 'Anand', 'Srinivas', 'Zebra', 'King', 'Amar']
c = []
visited = []

for name in names:
    first = name[0]   # first character
    if first not in visited:
        d = []
        for n in names:
            if n[0] == first:
                d.append(n)
        c.append(d)
        visited.append(first)

print(c)
##24
# Program to merge two sorted lists into another sorted list

a = [10, 20, 30, 40, 50]
b = [5, 12, 20, 37]
c = []

i, j = 0, 0   # pointers for a and b

# Merge while both lists have elements
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

# Add remaining elements from a (if any)
while i < len(a):
    c.append(a[i])
    i += 1

# Add remaining elements from b (if any)
while j < len(b):
    c.append(b[j])
    j += 1

print(c)

##25
# Program to find n-th largest element of a list

numbers = [10, 20, 30, 25, 40, 35, 12, 5]
n = 3   # 3rd largest

numbers.sort(reverse=True)  # sort in descending order
nth_largest = numbers[n-1]  # index is n-1

print(nth_largest)
##26
# Program to sort a list without using sorted() or sort()

nums = [10, 20, 30, 25, 40, 35, 12, 5]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            # swap
            nums[i], nums[j] = nums[j], nums[i]

print(nums)
>>>>>>> b268d84614917afefaac6789b530fc94f37b63ae
