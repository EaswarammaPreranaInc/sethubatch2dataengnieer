# Write a program to create a list with cubes of 2 , 4 , 6 , 8 , 10 with list comprehension (Home work)
cubes = [pow(x,3) for x in range(2,11, 2)]
print(cubes)



# # (Home work)
# # Write a program to extract 1st character of each string in capital letters in a list of srings without comprehension
# Let input be ['hyd' , 'pune' , 'chennai' , 'vijayawada']
# What is the output ? ---> ['H' , 'P' , 'C' , 'V']
# Enter list of lower case strings : ['hyd' , 'pune' , 'chennai' , 'vijayawada']
# ['H', 'P', 'C', 'V']

list = eval(input('Enter a list of strings:  '))
ans = []
for str in list:
    ans.append(str[0])
print(ans)




'''
(Home work)
Repeat previous program with comprehension

Input : ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output : ['H' , 'P' , 'C' , 'V']
'''
list = eval(input('Enter a list of Strings:  '))
ans = [str[0] for str in list]
print(ans)




'''
Write a program to append each word of the sentence and its length to a list
(word should be in capital letters) without comprehension

Let input be hyd is green city
What is the output ? ---> [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
Enter any sentence : Students are getting bored
[['STUDENTS', 8], ['ARE', 3], ['GETTING', 7], ['BORED', 5]]
'''
list = eval(input('Enter the sentence:  '))
words = list.split()
ans = []
for w in words:
    ans.append([w.upper(), len(w)])
print(ans)


'''
(Home work)
Repeat previous program with comprehension

Input : hyd is green city

Output : [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
list = eval(input('Enter the sentence:  '))
words = list.split()
ans = [[w.upper(), len(w)] for w in words]
print(ans)





'''
Write a program to add two lists of unequal length without comprehension

Let 1st list be [10 , 20 , 30 , 40 , 50 , 60 , 70] and 2nd list be [100 , 200 , 300 , 400]
What is the result ? ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
Enter 1st list : [10,20,30,40,50,60,70]
Enter 2nd list : [1,2,3,4]
[11, 22, 33, 44]

'''
list1 = eval(input('Enter 1st list:  '))
list2 = eval(input('Enter 2st list:  '))
ans = []
for i in range(min(len(list1), len(list2))):
    ans.append(list1[i] + list2[i])
print(ans)



'''
(Home work)
Repeat previous program with comprehension

Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 : [100 , 200 , 300 , 400]
Output : [110 , 220 , 330 , 440]
'''
list1 = eval(input('Enter 1st list:  '))
list2 = eval(input('Enter 2st list:  '))
ans = [list1[i] + list2[i] for i in range(min(len(list1), len(list2)))]
print(ans)




'''
Write a program to initialize a nested list with zeroes without comprehension

Let inputs be 3 and 4
What is the output ? ---> [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint: Use repetition operator *

How many lists ? : 3
How many elements in each list ? : 5
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
'''

r = int(input('How many lists:  '))
c = int(input('How many elements in each list?  '))
ans = []
for i in range(r):
    ans.append([0] * c)
print(ans)


'''
(Home work)
Repeat previous program with comprehension

Inputs : 3 and 4

Output : [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''
r = int(input('How many lists:  '))
c = int(input('How many elements in each list?  '))
ans = [[0] * c for i in range(r)]
print(ans)




'''
Write a program to extract those elements of 1st list which are not in 2nd list without comprehension

Let 1st list be [10 , 20 , 15 , 18 , 25 , 32] and 2nd list be [30 , 40 , 10 , 25 , 15]
What is the output ? ---> [20 , 18 , 32]

Enter 1st list : [10,20,15,18,25,32]
Enter 2nd list : [30,40,10,25,15]
Elements of 1st list which are not in 2nd list : [20, 18, 32]
'''
list1 = eval(input('Enter 1st list:  '))
list2 = eval(input('Enter 2nd list:  '))
ans = []
for x in list1:
    if x not in list2:
        ans.append(x)
print(ans)



'''
(Home work)
Repeat previous program with comprehension

Input1 : [10 , 20 , 15 , 18 , 25 , 32]
Input2 : [30 , 40 , 10 , 25 , 15]
Output : [20 , 18 , 32]
'''
list1 = eval(input('Enter 1st list:  '))
list2 = eval(input('Enter 2nd list:  '))
ans = [x for x in list1 if x not in list2]
print(ans)



# Write a program to print even numbers between 1 and 20 with  comprehension
'''
Even numbers between 1 and 20 : [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''
even_nums = [x for x in range(1, 21) if x % 2 == 0]
print(even_nums)



'''
Repeat previous program with comprehension and without using if

Output: [Even numbers between 1 and 20]
'''
even_nums = [x for x in range(2, 21, 2)]
print(even_nums)




'''
Write a program to print those squares of 1 , 2 , 3 , 4 , ... 20 which are divisible by 2 with comprehension

What is the output ? ---> [4 , 16 , 36 , ... , 400]
Squares of 1 to 20 which are divisible by 2 : [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
'''
ans = [pow(x,2) for x in range(1, 21) if x % 2 == 0]
print(ans)


# Repeat previous program with comprehension and without  using  if
ans = [pow(x,2) for x in range(2, 21, 2)]
print(ans)




'''
Write a program to add each element of 1st list with all the elements of 2nd list without comprehension

Let 1st list be [10 , 20 , 15] and 2nd list be [30 , 40 , 35 , 32]
What is the result ? --->
[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops

Enter 1st list : [10,20,15]
Enter 2nd list : [30,40,35,12]
[40, 50, 45, 22, 50, 60, 55, 32, 45, 55, 50, 27]
'''
list1 = eval(input('Enter 1st list:  '))
list2 = eval(input('Enter 2nd list:  '))
ans = []
for x in list1:
    for y in list2:
        ans.append(x + y)
print(ans)

'''
(Home work)
Repeat previous program with comprehension

Input1 : [10 , 20 , 15]
Input2 : [30 , 40 , 35 , 32]
Output : [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''
list1 = eval(input('Enter 1st list:  '))
list2 = eval(input('Enter 2nd list:  '))
ans = [x + y for x in list1 for y in list2]
print(ans)






'''
Write a program to concatenate each character of 1st string with every character of 2nd string with comprehension

Let 1st string be HYD and 2nd string be PUNE
What is the result ? ---> ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same as previous  program
'''
string1 = eval(input('Enter 1st string:  '))
string2 = eval(input('Enter 2nd string:  '))
ans = [ch1 + ch2 for ch1 in string1 for ch2 in string2]
print(ans)



'''
Write a program to convert a nested list to list without comprehension

Let input be [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What is the output ? ---> [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
Enter nested list : [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
'''
nestedlist = eval(input('Enter the nested list:  '))
ans = []
for r in nestedlist:
    for c in r:
        ans.append(c)
print(ans)


'''
Write a program to convert a nested list to list with comprehension

Let input be [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

What is the output ? ---> [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
nestedlist = eval(input('Enter the nested list:  '))
ans = [c for r in nestedlist for c in r]
print(ans)




# Find outputs (Home work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x for x in a for y in x]
print(b)  #[[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]



# Nested comprehension demo program (Home work)
a = [ [ j for j in range(i)] for i in range(5)]
print(a)    #[ [], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3] ]




'''
Most tricky program
Input : List of strings
Eg: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
Output : Nested list
i.e. [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]

Hint: Do not sort the lists

1) b = ['S' , 'A' , , 'Z' , 'K' ]

2) c = []

3) Iteartion 1 : d = ['Swathi' , 'Srinivas']
c = [['Swathi' , 'Srinivas']]

4) Iteartion 2 : d = ['Anand' , 'Amar']
c = [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar']]

5) Iteartion 3 : d = ['Zebra']
c = [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra']]

6) Iteartion 4 : d = ['King']
c = [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]
Enter list of strings : ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
[['Swathi', 'Srinivas'], ['Anand', 'Amar'], ['Zebra'], ['King']]
'''
list = eval(input('Enter the list of strings:  '))
firstletters = [s[0] for s in list]
nestedlist = [ [word for word in list if word[0] == c] for c in set(firstletters)]
print(nestedlist)


'''
Write a program to merge two sorted lists to produce another sorted list
0 1 2 3 4
Eg: List 'a' ---> [10 , 20 , 30 , 40 , 50]
List 'b' ---> [5 , 12 , 20 , 37]
0 1 2 3
List 'c' ---> [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]

Hint1 : Unsorted lists can not be merged

Hint2 : Use single while loop
'''
list1 = eval(input('Enter the sorted list 1:  '))
list2 = eval(input('Enter the sorted list 2:  '))
merge = []
i = j = 0
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merge.append(list1[i])
        i += 1
    else:
        merge.append(list2[j])
        j += 1
if i < len(list1):
    merge.extend(list1[i:])
else:
    merge.extend(list2[j:])
print(merge)




'''
Write a program to determine n-th largest element of a list

Input1 : [10,20,30,25,40,35,12,5]
Input2 : 3 (3rd largest)
Output : 30
Enter list:[10,20,30,25,40,35,12,5]
Enter which largest which to be shown:4
4th largest element : 25
'''
list = eval(input('Enter the list of integers:  '))
n = int(input('Enter which largest which to be shown: '))
for i in range(n-1):
    largest = max(list)
    while largest in list:
        list.remove(largest)
print(max(list))


'''
Write a program to sort a list without using sorted() function and sort() method

Input : [10,20,30,25,40,35,12,5]
Output : [5,10,12,20,25,30,35,40]
Enter list:[10,20,15,12,5]
[5, 10, 12, 15, 20]
'''
list = eval(input('Enter list:  '))
ans = []
while(len(list) != 0):
    ans.append(min(list))
    list.remove(min(list))
print(ans)