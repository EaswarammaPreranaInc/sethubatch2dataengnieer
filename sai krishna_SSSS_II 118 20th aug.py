1.# Create a list with cubes of 2, 4, 6, 8, 10 using list comprehension
numbers = [2, 4, 6, 8, 10]
cubes = [x**3 for x in numbers]

print("Cubes of 2, 4, 6, 8, 10:", cubes)               # Cubes of 2, 4, 6, 8, 10: [8, 64, 216, 512, 1000]


2.input_list = ['hyd', 'pune', 'chennai', 'vijayawada']

output_list = []

for city in input_list:
    output_list.append(city[0].upper())

print(output_list)                                    # ['H', 'P', 'C', 'V']


3.input_list = ['hyd', 'pune', 'chennai', 'vijayawada']

output_list = [city[0].upper() for city in input_list]

print(output_list)                                    # ['H', 'P', 'C', 'V']


4.sentence = input("Enter any sentence: ")

words = sentence.split()

result = []

for word in words:
    capital_word = word.upper()
    length = len(capital_word)
    result.append([capital_word, length])

print(result)                                       # [['STUDENTS', 8], ['ARE', 3], ['GETTING', 7], ['BORED', 5]]


5.sentence = input("Enter any sentence: ")

result = [[word.upper(), len(word)] for word in sentence.split()]

print(result)                                       # [['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]


6.list1 = eval(input("Enter 1st list: "))
list2 = eval(input("Enter 2nd list: "))

result = []

min_len = min(len(list1), len(list2))

for i in range(min_len):
    result.append(list1[i] + list2[i])

print(result)                                      # [11, 22, 33, 44]


7.list1 = eval(input("Enter 1st list: "))
list2 = eval(input("Enter 2nd list: "))

result = [list1[i] + list2[i] for i in range(min(len(list1), len(list2)))]

print(result)                                      # [110 , 220 , 330 , 440]


8.rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

result = []
for _ in range(rows):
    result.append([0] * cols)

print(result)                                     # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


9.rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

result = [[0] * cols for _ in range(rows)]
print(result)                                    # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


10.list1 = [10, 20, 15, 18, 25, 32]
list2 = [30, 40, 10, 25, 15]
result = []
for item in list1:
    if item not in list2:
        result.append(item)

print(result)                                   # [20, 18, 32]


11.even_numbers = [x for x in range(1, 21) if x % 2 == 0]

print(even_numbers)                           # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]



12.even_numbers = [x for x in range(2, 21, 2)]
 
print(even_numbers)                          # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


13.squares_divisible_by_2 = [x**2 for x in range(1, 21) if (x**2) % 2 == 0]


print("Squares of 1 to 20 which are divisible by 2:", squares_divisible_by_2)                    # Squares of 1 to 20 which are divisible by 2: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]



14.squares_divisible_by_2 = [x**2 for x in range(2, 21, 2)]

print("Squares of 1 to 20 which are divisible by 2:", squares_divisible_by_2)                   # Squares of 1 to 20 which are divisible by 2: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]


15.list1 = [10, 20, 15]
list2 = [30, 40, 35, 32]

 result = []

for x in list1:
    for y in list2:
        result.append(x + y)

print(result)                               # [40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]





16.list1 = [10, 20, 15]
list2 = [30, 40, 35, 32]

result = [x + y for x in list1 for y in list2]

print(result)                              # [40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]


17.str1 = "HYD"
str2 = "PUNE"


result = [a + b for a in str1 for b in str2]

print(result)                             # ['HP', 'HU', 'HN', 'HE', 'YP', 'YU', 'YN', 'YE', 'DP', 'DU', 'DN', 'DE']



18.nested_list = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]

flat_list = []

for sublist in nested_list:
        for item in sublist:
        flat_list.append(item)

print(flat_list)                       # [10, 20, 30, 40, 50, 60, 70, 80, 90]



19.nested_list = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]

flat_list = [item for sublist in nested_list for item in sublist]


print(flat_list)                      # [10, 20, 30, 40, 50, 60, 70, 80, 90]




20.# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)                              # [[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]

 

21.a = [[j for j in range(i)] for i in range(5)]
print(a)                             # [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]



22.input_list = ['Swathi', 'Anand', 'Srinivas', 'Zebra', 'King', 'Amar']

processed_letters = []

result = []

for word in input_list:
    first_letter = word[0]
    if first_letter not in processed_letters:
        group = [w for w in input_list if w[0] == first_letter]
        result.append(group)
        processed_letters.append(first_letter)

print(result)                      # [['Swathi', 'Srinivas'], ['Anand', 'Amar'], ['Zebra'], ['King']]



23.
a = [10, 20, 30, 40, 50]
b = [5, 12, 20, 37]

c = []

i = 0
j = 0

while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

while i < len(a):
    c.append(a[i])
    i += 1

while j < len(b):
    c.append(b[j])
    j += 1

print(c)                         # [5, 10, 12, 20, 20, 30, 37, 40, 50]



24.nums = [10, 20, 30, 25, 40, 35, 12, 5]
n = 3

sorted_nums = sorted(nums, reverse=True)

nth_largest = sorted_nums[n - 1]

print(nth_largest)              # 30



25. nums = [10, 20, 30, 25, 40, 35, 12, 5]

n = len(nums)
for i in range(n):
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)                      # [5, 10, 12, 20, 25, 30, 35, 40]



















 