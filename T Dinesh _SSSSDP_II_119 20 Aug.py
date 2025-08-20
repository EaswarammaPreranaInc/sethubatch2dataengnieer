# Program to create a list with cubes of 2, 4, 6, 8, 10 using list comprehension

numbers = [2, 4, 6, 8, 10]
cubes = [n**3 for n in numbers]

print("Cubes:", cubes)




cities = eval(input("Enter list of lower case strings : "))

result = []

for city in cities:
    result.append(city[0].upper())

print(result)




cities = eval(input("Enter list of lower case strings : "))

result = [city[0].upper() for city in cities]

print(result)




sentence = input("Enter any sentence : ")

words = sentence.split()
result = []

for w in words:
    result.append([w.upper(), len(w)])

print(result)




sentence = input("Enter any sentence : ")
result = [[w.upper(), len(w)] for w in sentence.split()]
print(result)





list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))

result = []
length = min(len(list1), len(list2))

for i in range(length):
    result.append(list1[i] + list2[i])

print(result)





list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))
result = [list1[i] + list2[i] for i in range(min(len(list1), len(list2)))]
print(result)





rows = int(input("How many lists ?  : "))
cols = int(input("How many elements in each list ?  : "))

result = []

for i in range(rows):
    result.append([0] * cols)

print(result)




rows = int(input("How many lists ?  : "))
cols = int(input("How many elements in each list ?  : "))
result = [[0] * cols for _ in range(rows)]
print(result)





list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))

result = []

for item in list1:
    if item not in list2:
        result.append(item)

print("Elements of 1st list which are not in 2nd list : ", result)





list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))

result = [item for item in list1 if item not in list2]

print("Elements of 1st list which are not in 2nd list : ", result)




evens = [n for n in range(1, 21) if n % 2 == 0]

print("Even numbers between 1 and 20 : ", evens)




evens = [n for n in range(2, 21, 2)]

print("Even numbers between 1 and 20 : ", evens)





squares = [n**2 for n in range(1, 21) if (n**2) % 2 == 0]

print("Squares of 1 to 20 which are divisible by 2 : ", squares)




squares = [n**2 for n in range(2, 21, 2)]

print("Squares of 1 to 20 which are divisible by 2 : ", squares)





list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))

result = []

for i in list1:        
    for j in list2:    
        result.append(i + j)

print(result)





list1 = eval(input("Enter 1st list : "))
list2 = eval(input("Enter 2nd list : "))

result = [i + j for i in list1 for j in list2]

print(result)





str1 = input("Enter 1st string : ")
str2 = input("Enter 2nd string : ")

result = [ch1 + ch2 for ch1 in str1 for ch2 in str2]

print(result)





nested_list = eval(input("Enter nested list : "))

flat_list = []

for sublist in nested_list:  
    for item in sublist:        
        flat_list.append(item)

print(flat_list)





nested_list = eval(input("Enter nested list : "))

flat_list = [item for sublist in nested_list for item in sublist]

print(flat_list)




a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [x for x in a for y in x]
print(b)





a = [[j for j in range(i)] for i in range(5)]
print(a)





words = ['Swathi', 'Anand', 'Srinivas', 'Zebra', 'King', 'Amar']
c = []  
b = [] 

for w in words:
    first = w[0]  
    if first not in b:
        d = [x for x in words if x[0] == first]
        c.append(d)
        b.append(first)

print(c)







a = [10, 20, 30, 40, 50]
b = [5, 12, 20, 37]

c = []  # final merged list
i = j = 0  # pointers

while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

c.extend(a[i:])
c.extend(b[j:])

print("Merged List:", c)







a = [10, 20, 30, 25, 40, 35, 12, 5]
n = int(input("Enter which largest to be shown: "))

a_sorted = sorted(a, reverse=True)

if n <= len(a):
    print(f"{n}th largest element : {a_sorted[n-1]}")
else:
    print("Invalid input! n is larger than list size.")






a = [10, 20, 30, 25, 40, 35, 12, 5]

for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print("Sorted list:", a)
